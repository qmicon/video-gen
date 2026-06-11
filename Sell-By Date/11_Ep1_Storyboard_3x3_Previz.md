# EP 1 "COLD CALL" — 3×3 STORYBOARD GRID, SHOTS 1–9 (GPT Image 2.0)

One-image, nine-panel storyboard grid covering **shots 1–9 verbatim** from
[10_Ep1_Shot_List.md](10_Ep1_Shot_List.md) — the hook (portal tumble → battlefield reveal →
denial) through the sword-at-the-throat interrogation and the real spear-death. All nine panels
are Scene 1 battlefield, one lighting lock.

> **Scope (per `storyboard.md` Format B):** a composite grid is **previz only**. Per-panel
> resolution is too low to anchor identity downstream — **never feed grid cells to Seedance as
> references.** Final boards = one panel per shot, generated sequentially (Format A).

> **Cell-count warning (per `GPT_IMAGE_2_PROMPTING_GUIDE.md`):** gpt-image-2 is reliable to
> ~8 distinct panels; 9 is at the edge. Fix soft cells with a targeted edit
> ("change only panel N, keep all other panels exactly the same"), don't re-roll the grid.

> **Character-state note:** Drew is mud-caked from the shot-1 face-plant, so the
> **`drew_muddied`** sheet is the identity ref for the whole grid. The clean `drew` sheet isn't
> needed here; `drew_muddied_bloodied` (blood across the face) only enters at shot #29.
> Shot #8's neck blood-bead is described in text.

> **Text rule:** shot 1's HOOK CAPTION is **not** baked into the panel — on-screen text is
> composited in post (per `storyboard.md`). Only panel numbers render.

---

## How to run it

`images.edit` (ChatGPT: attach images), `model gpt-image-2`, `quality="high"`,
`size="1536x1152"` (exact 4:3 — nine 4:3 cells tile to a 4:3 canvas, edges multiples of 16).
ChatGPT UI fallback: Landscape + high quality.

### Reference images to attach (in this index order)

| Index | Asset | Used in panels |
|---|---|---|
| **Image 1** | **`drew_muddied`** character sheet | 1, 3, 5, 6, 7, 8 (neck), 9 (fg shoulder) — all but the POV panel 4 |
| **Image 2** | **`commander`** character sheet | 6, 7, 9 |
| **Image 3** | **VAGE can prop sheet** ([PRODUCT_VAGE_energy_drink.md](PRODUCT_VAGE_energy_drink.md)) | 1 |
| **Image 4** | **Battlefield master frame / style grid** (`~/Downloads/battlefield/battlefield_combined_ref.jpg`) | all — bearings + grade |
| **Image 5** | **Portal asset** (green swirl FRONT, [PORTAL_tear_asset_sheet.md](PORTAL_tear_asset_sheet.md)) | 1 |

---

## Shot → panel map

| Panel | Shot | Spec (from shot list) | Frozen moment |
|---|---|---|---|
| 1 | #1 | MS · GND · FISH 14mm · HH | face-plant out of the portal, can in fist |
| 2 | #2 | EST · HIGH · crane · 20mm | full battle reveal, banner L / pike-wall R |
| 3 | #3 | MS→FS · EYE · HH 28mm | Drew mid-spin, refusing to believe |
| 4 | #4 | WS · **POV** · WHIP-pan 24mm | his POV — chaos smeared with motion blur |
| 5 | #5 | MCU dirty 1S · EYE · 50mm shallow | "this is a movie set" mid-shout |
| 6 | #6 | FS 1S→2S · EYE · HH whip 35mm | Commander seizes Drew's collar |
| 7 | #7 | MCU OTS (Drew fg) · LOW · 50mm | sword across the throat, interrogation |
| 8 | #8 | ECU · MACRO | blade bites, one bead of blood on the neck |
| 9 | #9 | WS OTS (Drew fg) · EYE · 35mm RACK | the real death — a soldier drops behind the Commander |

---

## THE PROMPT (copy-paste)

```
Image 1 = DREW's character sheet (mud-caked state) — reproduce this exact man (face, hair,
build, muddy white shirt and loosened tie) wherever Drew appears; do not redesign him. Image 2
= the armored COMMANDER's character sheet — reproduce his exact armor and helmet. Image 3 = the
"VAGE" energy drink can — matte-black 473ml can with an electric-cyan lightning-bolt logo;
reproduce it exactly. Image 4 = the battlefield location and film grade: burning banner on the
ridge LEFT, silver pike-wall of infantry RIGHT, hazy slope ahead, churned-mud foreground — keep
these bearings and this grade in every panel. Image 5 = the portal asset: a FLAT vertical disc
of acid-green energy with a ragged splattered rim and a bright near-white-green swirling core —
reproduce this exact design. It is a flat disc, never a tunnel, hole, or wormhole.

THE COMMANDER'S WEAPON: a long medieval knightly LONGSWORD — a straight, slender, double-edged
steel blade about one metre (a full arm-plus in length) with a simple cruciform crossguard.
Wherever the sword appears, always render the FULL long blade — never a short sword, stubby
arming sword, broad cleaver, or dagger.

Task: a photorealistic 3x3 STORYBOARD GRID — nine sequential cinematic film stills from one
continuous scene of a live-action absurd action-comedy, reading in story order left-to-right,
top-to-bottom. This is a previsualization planning document for a film pipeline, NOT a poster,
NOT a collage. One composite image: nine panels of identical size, each individually framed 4:3
horizontal and filling its full rectangular frame (no circular vignettes or lens masks),
separated by thin black gutters. A small plain white number "1" through "9" sits in the
bottom-left corner of each panel. Render no other text, captions, titles, or logos anywhere
(the VAGE can label from Image 3 is the only exception).

CONTINUITY: one continuous scene on the same battlefield, minutes of story time. Drew (Image 1)
is the identical mud-caked man in panels 1, 3, 5, 6, 7 and 9; panel 8 is a macro detail of his
neck; panel 4 is his own point of view, so he does not appear in it. The Commander (Image 2) is
identical in panels 6, 7 and 9. PROP CONTINUITY (important): Drew never lets go of the black
VAGE can (Image 3) — he keeps it clutched in one hand in every panel where his hands are
visible (panels 1, 2, 3, 5, 6 and 9).

LIGHTING — ALL NINE PANELS: bright but hazy overcast daylight, pale blue-grey sky thick with
smoke and atmospheric haze flattening the distance; soft natural light catching polished armor
with real specular highlights; muted faded color like a still from a 1960s-70s European
historical war epic on vintage film stock — fine grain, soft naturalistic focus. No golden hour,
no HDR, no clean modern 3D-render look.

PANEL 1 — Ground-level still, camera low in the mud, fisheye wide-angle distortion but a FULL
rectangular frame (no black circular vignette): DREW mid face-plant into deep churned mud, body
still tumbling forward out of the flat acid-green swirl portal (Image 5) standing at ground
level directly behind him, one fist gripping the black VAGE can (Image 3) clear of the mud.
Green glow spills across the wet mud; the battle rages distorted at the frame edges.

PANEL 2 — High crane establishing wide matching Image 4: the full medieval melee — clashing
steel, the burning banner on the ridge to the LEFT, horses, the dense silver pike-wall of
infantry to the RIGHT, drifting smoke columns, deep layered foreground/midground/background;
Drew a tiny lone mud-covered figure down in the near-foreground mud, still clutching the can.

PANEL 3 — Eye-level full shot, handheld feel: Drew on his feet, mud-caked, frozen mid-spin as he
turns in a circle, arms half-raised with the VAGE can gripped in one hand, face in disbelieving
panic; soldiers fighting at depth all around him.

PANEL 4 — Drew's own POINT OF VIEW, a whip-pan frozen mid-motion: the battlefield smeared with
strong horizontal motion blur — a passing horse, clashing soldiers and smoke streaking across
the frame, horizon slightly tilted. Disorienting. Drew is NOT in this panel.

PANEL 5 — Eye-level medium close-up, shallow focus, Drew slightly off-center with a blurred
soldier's shoulder edging the frame: Drew mid-shout, mouth open, one muddy hand raised in
protest while the other still clutches the VAGE can, eyes scanning for a film crew that isn't
there; the battle a soft out-of-focus chaos behind him.

PANEL 6 — Full shot, kinetic, mid-action: the armored COMMANDER (Image 2) storms into frame and
seizes Drew by the collar with one gauntleted fist, yanking him close — Drew off-balance, heels
dragging through the mud, still gripping the VAGE can in his free hand.

PANEL 7 — Low-angle medium close-up over Drew's soft out-of-focus foreground shoulder: the
Commander in sharp focus towering against the hazy sky, the long slender blade of his longsword
laid flat across Drew's throat, the full length of the blade reaching across the frame and its
cruciform crossguard visible in his fist, steel glinting close to camera, his face cold
mid-interrogation; vertical dominance.

PANEL 8 — Extreme macro close-up of the SIDE OF DREW'S NECK in profile — the underside of the
jawline and chin at the top, the ear, a few strands of muddy hair, the neck tendon, the muddy
shirt collar at the bottom: the long slender edge of the longsword blade pressed flat and
horizontal against the throat (a thin sword edge, not a broad cleaver), a single small bead of
bright red blood running down from where the edge bites. Razor-sharp steel texture, shallow
macro focus. Clearly a neck and jaw, not a shoulder or torso; no hand in frame.

PANEL 9 — Wide shot over Drew's soft foreground shoulder, eye level: the Commander has NOT
released him — the full long blade of the longsword stays pressed flat and horizontal across
Drew's throat in the foreground, the long blade spanning the gap between them, the Commander
gripping him close, not stepped back. Behind the Commander, in the
mid-background, a soldier is struck by a spear and collapses mid-fall, the focus drawn past the
Commander to the dying man; scattered fallen bodies and broken pikes in the mud around them.

STYLE: photorealistic cinematic film stills, real cinema photography, consistent vintage war-
epic grade across all nine panels, professional previz storyboard quality.

CONSTRAINTS — do not include: any text other than the nine small panel numbers and the VAGE can
label; no watermarks; no speech bubbles or captions; no comic-book or sketch style; no extra
panels; no circular vignettes or lens masks on any panel; no modern objects anywhere except the
VAGE can and Drew's clothing; the portal is a flat green disc, never a dark tunnel or hole; no
golden-hour or HDR look; no graphic gore, impalement detail, severed parts, or open wounds —
panel 8 is one small blood bead, panel 9's death reads from the fall, not from wounds; the
Commander's sword is always a full-length longsword, never a short sword, stubby arming sword,
broad cleaver, or dagger; no character drift — Drew and the Commander match their sheets in
every panel where they appear, and the VAGE can stays in Drew's hand in every panel his hands
are visible.
```

---

## After it renders — QA + iterate

1. **Bearings:** banner LEFT / pike-wall RIGHT in panels 2, 3, 7, 9; portal acid-green (panel 1).
2. **Identity:** same Drew in 1/3/5/6/7/9; same Commander in 6/7/9. Drift → single-panel edit.
3. **Panel 4 check:** must contain NO Drew (it's his POV). If he appears, edit it out.
4. **Approve → sequential pass:** then board shots 1–9 (and onward) one panel at a time
   (Format A), re-supplying `drew_muddied` + `commander` sheets every 5–8 panels.

## Web references used (how this prompt shape was derived)

- **floatboat.ai — "Can One Person Build a Full Storyboard with GPT Image 2?"** — the model
  executes a shot list, it doesn't write one; ~8 frames of continuity per prompt; surgical
  "change only X" edits beat re-rolling; identity refs re-pasted per frame.
- **Instagram (OiiOii) grid template** — "storyboard grid with thin black borders separating
  each frame, bold sans-serif number per frame" → thin gutters + small panel numbers.
- **YouTube "How to Make Storyboard with AI"** — "expand the reference image into a 9-frame
  storyboard grid showing a cohesive cinematic scene unfolding over time" → one cohesive scene
  in reading order, anchored to attached refs.
