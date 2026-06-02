# Interior Location Creation Blueprint

A repeatable recipe for turning a few reference photos of an interior into a
geometrically-consistent **3D wireframe location** + a set of **labeled
perspective views** + **paired Nano Banana Pro prompts** that render new camera
angles of the *same* room in the *same* style.

Built from the concrete-loft job. Reference implementation:
- `room_3d.py` — the 3D model, pinhole camera, coverage views, labels.
- `room_topdown.py` — the top-down floorplan + wall elevations (planning aid).
- `make_style_grid.py` — combine reference photos into one 2×2 style image.
- `nano_prompts_9views.md` — the generated paired prompts.

---

## Why this exists (the core problem)

You want **multiple camera angles of one location**, all consistent. Two naive
approaches both fail:

1. **Prompt-only** ("different camera view of this room") → the model invents a
   new room each time; layout drifts.
2. **AI reverse-angle off the photo** → looks plausible but is **not 3D-consistent**;
   furniture teleports, walls swap, you can't trust it for geometry.

The fix: build an actual **3D wireframe** of the room once, then render true
perspective line-drawings from any camera. The wireframe locks geometry; the
photos lock style. Feed both to the image model.

---

## Pipeline at a glance

```
reference photos
   │
   ▼
[1] Reconstruct geometry  ──►  [2] Top-down floorplan + wall elevations (confirm with user)
   │
   ▼
[3] Build parametric 3D wireframe (boxes, walls, features, furniture)
   │
   ▼
[4] Camera coverage set (corners + wall-facing) + coverage map
   │
   ▼
[5] Label objects (3D anchors) + de-overlap + distance scaling
   │
   ▼
[6] Render quality (depth line-weight, translucent fills, pinhole optics)
   │
   ├──►  [7] Combine photos into ONE 2×2 style grid
   │
   ▼
[8] Write paired prompt per view  ──►  run in Nano Banana Pro
```

---

## [1] Reconstruct the geometry — the hard part

This is where most of the time goes. Reference photos lie:

- **Wide-angle distortion** makes near things huge and far things tiny, and makes
  two **adjacent (perpendicular) walls look like opposite parallel walls.** Do not
  assume "windows left, arch right" means they face each other.
- **AI-generated reverse angles are geometrically inconsistent** — use them only
  as loose hints, never as truth. Trust the one real photo most.

Method:
1. List the **4 walls** and what is on each (e.g. WINDOW wall, ARCH/DUCT wall,
   OFFICE/desk wall, ART wall). Some rooms are **corner units** where glass wraps
   two adjacent walls.
2. Establish **adjacency** explicitly: which walls are perpendicular, which are
   opposite. **Confirm with the user** — they can see the real space; you can't
   resolve it from distorted photos alone. (On the loft this took several rounds:
   the key unlock was "window wall and arch/duct wall are *adjacent*," and "the
   plain wall is the south/office wall.")
3. Anchor orientation to **one trusted photo** ("the left wall in this shot is the
   east wall") so left/right/compass stop flip-flopping.
4. Note **object facing** while you're here (sofa backs to which wall, monitors
   face which way) — you'll need it for the prompt.

Common failure modes & cues:
- Glass that "wraps" the far corner → corner unit (two adjacent glass walls).
- A bright far wall in a wide shot is often the *same* side window receding, not a
  separate wall.
- The HVAC duct usually drops near a specific wall — use it as a fixed landmark.

---

## [2] Top-down floorplan + wall elevations (planning aid)

Before any 3D, draw a **top-down** to agree on the box. A floorplan alone can't
show what's *on* the walls, so add **four elevation strips** (one per wall)
showing arch, painting, door, windows, shelves, etc. See `room_topdown.py`.

- Use a real coordinate system in meters (e.g. X = 0..W west→east, Y = 0..H
  south→north). Pick which wall is which and **label every wall**.
- Mark camera positions and FOV cones on it.
- **Iterate with the user until the plan is right.** Cheap to fix here, expensive
  later.

---

## [3] Build the parametric 3D wireframe

Everything is parametric so edits are one-liners. See `room_3d.py`.

Coordinate system (meters): `x: 0=WEST .. RX=EAST`, `y: 0=SOUTH .. RY=NORTH`,
`z: 0=floor .. RZ=ceiling`.

Primitives:
- `seg(p0, p1, color, lw)` — a 3D line segment (appended to global `S`).
- `box(x0,x1,y0,y1,z0,z1, color, lw, fill=True)` — 12 edges (+ 6 translucent
  faces if `fill`). Use for all furniture/volumes.
- `rect_x / rect_y` — a flat quad on a constant-x or constant-y wall (paintings,
  doors, photos, the window mullion grid).
- arches / curves → sample points and connect with `seg`.

Build order:
1. **Room shell** as a box with `fill=False` (edges only — never fill the shell).
2. **Walls' features**: window mullion grid (`seg` lattice on the glass wall),
   arch (semicircle of segments), duct (boxes for the ceiling run + drop + an
   octagon vent), framed art/door (`rect_x`/`rect_y`).
3. **Furniture** as filled boxes: desks, monitors (RESTING ON the desk — embed the
   base a few cm into the desktop so there's no floating gap), chairs, sofas,
   coffee table, dining table + chairs, credenza, bookshelves, plants.

Gotchas learned:
- **Things floating**: an object that should rest on another must overlap it
  slightly in the axis of contact (monitors `z0` = desk top minus ~5cm). A small
  y/x offset reads as "hovering off the edge."
- Keep the shell unfilled or it fogs the whole frame.

---

## [4] Camera coverage set (avoid blind spots)

A natural lens from one corner leaves the wall *behind* the camera unseen. Cover
the whole room with a fixed set:

- **4 corner diagonals** at ~24mm (wide, for room context).
- **4 wall-facing** shots at ~28mm (one head-on per wall, kills the
  behind-camera blind spots).
- **+ any hero/special camera** (e.g. "from the painting toward the desks").

Render a **coverage map** (top-down with every camera's position + FOV cone) to
visually confirm nothing is missed.

Optics (critical — avoid wide-angle distortion):
- Camera takes a **focal length in mm** (full-frame equiv, 36mm sensor width).
- `hfov = 2*atan(36/(2*focal_mm))`. 24mm≈74°, 28mm≈65°, 35mm≈54°, 50mm≈40°.
- 20mm (≈88°) exaggerates near/far badly — **don't**. Use 24–35mm for interiors.
- Frame the plot so the hfov edge = ±1 (so the crop matches the lens).

Pinhole projection (no 3D lib needed):
```
f = normalize(target - eye);  up = (0,0,1)
right = normalize(cross(f, up));  u = cross(right, f)
focal = 1 / tan(hfov/2)
cam(P)  = ( (P-eye)·right , (P-eye)·u , (P-eye)·f )   # x,y,depth
proj(c) = ( c.x/c.depth*focal , c.y/c.depth*focal )
# clip segments at a near plane (depth <= 0.12) before projecting
```

---

## [5] Label the objects (so a box isn't ambiguous)

A wireframe cube could be a desk or a fridge. Put a **3D label anchor on each
object** (at its surface, not floating above it) and project the text into each
view. Only labels whose anchor is **in front of the camera and inside the frame**
are drawn — so each view self-documents exactly what it contains.

Three refinements that matter:
- **Anchor on the object's surface** (mid-height), or the label hovers above it.
- **Scale font by distance**: `fs = clip(8 * (4.5/depth), 5.5, 12)` — near labels
  big, far ones small (less clutter).
- **De-overlap with leader lines**: keep a dot at the true position; push
  colliding text apart vertically (force iteration); draw a thin line from moved
  text back to its dot. (See the `labs`/`GAP` loop in `room_3d.py`.)

---

## [6] Render quality (readability)

- **Depth-scaled line weight**: `lw_eff = clip(lw * (4.5/depth), 0.3, 3.2)` — near
  lines thick, far lines thin. Big depth cue.
- **Translucent volume fills**: draw each box's 6 faces as low-alpha polygons
  (`alpha≈0.10`) **sorted far→near (painter's algorithm)** so volumes read as
  solids and you can tell which lines bound which object. Edges drawn on top.
- Export each view full-size (one PNG per camera) + a contact sheet.

---

## [7] Combine reference photos into ONE 2×2 style grid

**Four separate style images get under-weighted and ignored.** Combining them into
a single 2×2 grid makes the model actually copy the look. See `make_style_grid.py`
(drop the photos in `style/`, run, get `style_grid.png`).

Final reference set per render = **2 images**: the wireframe (geometry) + the
style grid (look).

---

## [8] Write the paired prompt (the part that makes or breaks it)

Structure, in order:

1. **Task framing** — "IMAGE 1 = line wireframe (geometry only). IMAGE 2 = 2×2 grid
   of photos of THIS exact room. Render a new photo of the SAME room from the
   wireframe's angle that looks like a fifth photo from the same camera/film —
   indistinguishable in style." Framing it as *the same room, new angle* beats
   "in the style of."
2. **STYLE COMES ENTIRELY FROM IMAGE 2** — state the wireframe has **zero** color/
   texture/light, then list concrete look hooks pulled from the photos (mottled
   concrete, blown-out windows + star flare, desaturated cool grade, film grain,
   haze, lived-in mood). Forbid "clean 3D render / real-estate / HDR."
3. **Geometry** (from image 1 only) — lens mm, eye level, the composition (e.g.
   "two walls meet at a bright corner at ~45% across / 40% down"), contre-jour or
   side-lit.
4. **Object placement + FACING** — for **each object visible in this view**:
   - **frame position as percentages** (0% left/top → 100% right/bottom),
   - **depth** (nearest/large vs far/small),
   - **explicit FACING/orientation** in room terms (sofa back to which wall + seat
     toward what; monitor screens face which way; dining table long-axis; vent
     points down). *A box can't show facing — you must say it.*
   - neighbor relations ("directly behind", "flank the arch").
5. **Depth order** near→far (helps occlusion).
6. **BAN** — "do not draw the red labels/dots/leader lines"; no people/text/logos;
   no fisheye; **do NOT invent objects that are outside this view** (name them);
   no clean-render/HDR/oversaturated look; no rearranging.

### Only list what's actually visible
Compute per-view visibility from the camera (project each label anchor; keep those
with `depth>near` and `|x|<1.05, |y|<0.68`). List only those objects, and
explicitly ban the off-frame ones (the model loves to add a door/chairs it "knows"
should be there). On v3 this excluded the door, office chairs, and the art-wall
photo.

### Reusable template
```
TASK: IMAGE 1 = plain 3D LINE WIREFRAME (geometry/camera/layout only).
IMAGE 2 = 2x2 grid of four real photos of one specific <ROOM TYPE>.
Render ONE photoreal photo of THE SAME room from the wireframe's angle,
looking like a fifth photo from the same camera/film as IMAGE 2 — same style.

STYLE COMES ENTIRELY FROM IMAGE 2:
the wireframe has NO color/texture/light/mood (lines + red annotations you must
NOT draw). Copy directly from IMAGE 2: <materials> / <floor> / <color grade> /
<light + flare> / <film grain + haze> / <mood>. NOT a clean 3D render, NOT
real-estate, NOT HDR.

GEOMETRY (image 1 only): <lens mm>, eye level, <composition + where walls meet>,
<contre-jour or side-lit>.

OBJECT PLACEMENT + FACING (percent = frame position, 0%=left/top → 100%=right/bottom):
- "<label>": <near/far + size>, ~<x>%/<y>%. <what it is>. FACING: <orientation>.
- ... (only objects visible in THIS view)
Depth near→far: <list>.

BAN: don't draw red annotations; no people/text/logos; no fisheye/warp;
do NOT add <off-frame objects>; no clean-render/HDR/oversaturated; no rearranging.
```

---

## Lessons / failure modes → fixes (cheat sheet)

| Symptom | Fix |
|---|---|
| Model invents a new room each angle | Lock geometry with a 3D wireframe reference |
| Walls look opposite but user says adjacent | Trust the user/real photo; wide-angle fakes parallel walls |
| Reverse-angle reference looks wrong | AI reverse angles aren't 3D-consistent; don't trust for geometry |
| Near things huge, far tiny | Lower FOV: use 24–35mm, not 20mm |
| Object hovers above its surface | Overlap it slightly into the surface it rests on |
| Label floats above object | Anchor label at the object's surface height |
| Labels overlap/unreadable | Leader-line de-overlap + distance-scaled font |
| Can't tell which lines = which solid | Translucent depth-sorted volume fills |
| Wall behind camera never shown | Add wall-facing cameras; check a coverage map |
| Style from photos ignored | Combine photos into ONE 2×2 grid; lead with "same room/film" |
| Output looks like clean 3D render | State wireframe has no appearance; ban "render/HDR/real-estate" |
| Model adds a door/chairs not in view | List only visible objects; ban the off-frame ones by name |
| Sofa/monitor facing wrong | State FACING explicitly in room terms (box can't show it) |
| Red annotation boxes painted into image | Ban drawing the labels/dots/leader lines |

---

## Tooling notes

- Pure `matplotlib` + `numpy` (no 3D engine). Run in a venv:
  `python3 -m venv .venv && .venv/bin/pip install matplotlib`.
- `Date.now()`/random not needed; everything deterministic.
- Each script writes PNGs into `video-gen/`. Re-run after any parametric edit.
- Keep the model parametric — every wall/object is a few numbers, so user
  corrections ("move the desk", "duct is nearer the arch") are one-line edits.
```
