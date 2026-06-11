# EXT. MUDDY BATTLEFIELD — Location Sheet (Ep1 "Cold Call")

Exterior location lock for the battlefield Drew tumbles into (script L25–63). Unlike
the loft interior, there is **no 3D wireframe** — exteriors are unbounded and have no
walls to teleport, so geometry is locked with a **text bearing layout + a master
establishing frame that every other angle chains from**. The portal/glowing tear is a
**separate asset** and is not part of this sheet.

Reference style grid: `~/Downloads/battlefield/battlefield_combined_ref.jpg` (2×2 plate
of the two establishing shots). Feed this as the appearance reference on every render.

---

## 1. Location bible

- **Type / scale:** open, churned-mud hillside; a brutal medieval pitched battle in
  progress. Vast, no architecture, sky-dominated.
- **Color palette:** muted, slightly faded vintage-film color; mirror-polished steel
  plate armor catching soft daylight; mud-browns; one muted warm note from the banner
  fire. Pale blue-grey hazy sky.
- **Ground:** deep wet churned mud, trampled grass, puddles, scattered fallen bodies
  and broken pikes in the distance. Foreground mud is the action surface (Drew lands,
  is shoved down, scrambles).
- **Atmosphere:** drifting smoke columns, fine drizzle/mist, embers, breath-fog, haze
  flattening the distance.

### Lighting / time lock (paste into EVERY prompt)
> Bright but hazy daylight, pale blue-grey sky thick with atmospheric haze and smoke
> that flattens the distance. Soft natural light catches the polished armor with real
> specular highlights — no harsh black shadows, no golden-hour warmth. Diffuse and
> slightly cool, gritty haze in the air. Vintage cinematic film stock — a still from a
> 1960s–70s European historical war epic: muted faded color, fine grain, soft
> naturalistic focus. Grand and grim but not dark. NOT golden-hour, NOT HDR, NOT a
> clean modern/3D-render look.

---

## 2. Landmark bearings (the "map", in words)

Orient everything to the establishing frame. "Up the hill" = **into the distance**.

- **AHEAD / up-slope (distance):** the enemy ridge — rising muddy hill, distant cavalry
  and infantry silhouettes cresting it, smoke behind. The pale sky glow sits here.
- **UPPER-LEFT of the ridge:** the **burning banner** on a pole — the one fixed,
  unmistakable landmark. It stays screen-LEFT in every wide.
- **RIGHT foreground → mid-ground:** the **friendly pike-wall** — a dense diagonal line
  of silver-armored infantry with raised pikes, angled up toward the ridge. Stays
  screen-RIGHT.
- **NEAR / foreground (camera side):** deep churned mud — **Drew's landing + action
  zone**. Bodies and broken weapons half-sunk in it.
- **LEFT / open field:** the field falls away into smoke and scattered dead; emptier
  than the right.

Consistency rule: **burning banner = always left, pike-wall = always right, hill rises
ahead, mud in front.** If a render flips any of these, regenerate.

---

## 3. Coverage set (shot-scale × beat, not "4 walls")

Generate the **master first**, then chain the rest off the approved master frame.

| ID | Shot | Beat (script) | Camera |
|----|------|---------------|--------|
| **A — MASTER** | Establishing wide, no subject | sets the world (L25) | low, ~24–28mm, foreground mud → ridge; banner left, pike-wall right |
| **B** | Low-angle action POV | Drew face-plants / is shoved (L27, L41) | ground level in the mud, looking up the slope toward the pike-wall |
| **C** | Reverse, toward the foreground | Drew scrambles back & dives out (L62–63) | from up-field looking back down toward the near mud (where the portal asset will go) |
| **D** | Medium, Commander | grabs Drew, chugs, ordered, cut down (L39–60) | eye-level on the Commander, pike-wall + ridge behind him |
| **E** | Ground/texture plate | inserts, mud detail | top-down / high angle on churned foreground mud |

You don't need more than this for a ~90-sec episode with one battlefield.

---

## 4. Paired prompts

Two reference images per render: **IMAGE 1** = the battlefield style grid (look/grade);
for B–E also attach **IMAGE 2** = the approved MASTER frame (geometry/landmarks to match).
Built for Nano Banana Pro (edit/extend) or Seedance image-ref. State the lighting lock
every time.

### A — MASTER establishing wide
```
A wide cinematic establishing shot of a brutal medieval battlefield, matching the exact
realistic photographic style, grade, and mood of the attached reference image — real
film photography, NOT an illustration, NOT a render.

COMPOSITION: low camera near the deep churned-mud foreground, ~24–28mm, looking up a
muddy slope into the distance. A burning banner on a pole on the ridge to the LEFT;
distant cavalry and infantry silhouettes cresting the hill ahead under a pale blown-out
hazy sky; a dense diagonal pike-wall of silver-armored infantry with raised pikes
filling the RIGHT foreground-to-midground. Scattered fallen bodies and broken pikes in
the mud. Drifting smoke columns.

[paste LIGHTING / TIME LOCK]

No modern objects, no text, no watermarks, no people in the immediate foreground (keep
the near mud clear for action), no clean/HDR/sunny look.
```

### B — Low-angle action POV (chain off MASTER)
```
Using IMAGE 1 (style grid) and IMAGE 2 (the master establishing frame) as the exact
location and style reference, render the SAME battlefield from a NEW angle: a low,
ground-level camera down in the churned mud, looking up the slope. The burning banner is
still on the ridge to the LEFT, the silver pike-wall of infantry is to the RIGHT and
closer/looming, the hazy ridge is ahead. Wet mud and a fallen body in the near
foreground. Same overcast light, same grade, same world — only the camera has moved.

[paste LIGHTING / TIME LOCK]

Keep the banner LEFT and pike-wall RIGHT exactly as in IMAGE 2. No clean/HDR look, no
text, no watermarks.
```

### C — Reverse toward foreground (chain off MASTER)
```
Using IMAGE 1 (style) and IMAGE 2 (master) as the location/style reference, render the
SAME battlefield from the REVERSE angle — camera up-field looking back DOWN the slope
toward the near churned-mud foreground (the escape direction). The pike-wall and burning
banner are now BEHIND/around the camera, so the frame is dominated by open muddy ground,
smoke, and scattered dead falling away downhill, ridge light behind. Same world, same
overcast grade.

[paste LIGHTING / TIME LOCK]

Leave a clear patch of foreground mud centre-frame (a separate portal asset will be
composited here later). No text, no watermarks, no clean/HDR look.
```

### D — Commander medium (chain off MASTER + Commander sheet)
```
Using IMAGE 1 (battlefield style/location) and IMAGE 2 (the Commander character sheet)
as references, render a medium shot of the armored Commander standing in the churned mud
on this SAME battlefield. The silver pike-wall of his infantry and the hazy ridge are
behind him; the burning banner sits on the ridge in the background. Overcast diffuse
light, smoke haze, same desaturated grade as the battlefield reference.

[paste LIGHTING / TIME LOCK]

Match the Commander's armor exactly to IMAGE 2. He is NOT holding any modern object. No
text, no watermarks, no clean/HDR look.
```

### E — Mud / texture plate
```
Using IMAGE 1 as the style/location reference, render a high-angle / near top-down plate
of the churned battlefield mud — deep wet trampled mud, puddles reflecting the pale sky,
boot prints, a half-sunk broken pike and a smear of blood, scattered trampled grass.
Overcast flat light, desaturated cool grade, smoke haze. No people, no text, no
watermarks, no clean/HDR look.
```

---

## 5. Generate + chain loop

```
generate A (master)  →  approve & lock it
        │
        ▼
attach A as IMAGE 2 for B, C, D  →  generate each (banner left / pike-wall right held)
        │
        ▼
inspect → targeted edit any drift (regenerate, don't fight it)
        │
        ▼
ONE uniform regrade pass across A–E (match grade/exposure; keep each frame's smoke)
        │
        ▼
assemble A–E into the battlefield location sheet grid
```

Then each approved frame is passed to Seedance 2.0 as the **scene/background reference**
on its matching shot (the way a character sheet is passed for identity). Re-paste the
landmark rule — *banner left, pike-wall right, hill ahead, overcast diffuse light* — into
every battlefield shot prompt.

---

## Why no wireframe (exterior vs interior)

| | Interior loft | This battlefield |
|---|---|---|
| Geometry lock | parametric 3D wireframe | text bearing layout (§2) |
| Failure mode | walls/furniture teleport | landmarks drift, light/sky flips |
| Main consistency tool | wireframe + style grid | **master frame chaining** + style grid |
| Dominant variable | object placement | time-of-day / weather / sun (§lighting lock) |

The audience can't detect metric error on an open field, only *relational* error — so a
written bearing layout plus a locked, chained master frame is the correct, cheaper lock.
