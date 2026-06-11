# ASSET — "The Portal" / Green Swirl Splat (Sell-By Date series device)

The glowing portal Drew tumbles out of and dives back through (Ep1 script L27, L62–63; "shrinks to a
seam and snaps shut", L77). A **separate VFX asset**, kept out of the battlefield and loft location
sheets so it can be **composited into both** (and every future episode) unchanged. This sheet locks its
shape, swirl, glow, and open→close states.

> **Style direction (this version): a flat, swirling acid-green "splat" portal** — the energy-puddle /
> flung-paint disc look. Captures that vibe with an **original execution**; we do **not** name or clone
> any trademarked cartoon's portal, and the prompt never names the IP (keeps it non-infringing and
> avoids model refusals). The earlier jagged white-cyan *tear* is the alternate — see §5.

> **Script reconciliation:** a round swirl can't "shrink to a seam." Its close is an **iris collapse to
> a bright green pinpoint**. If you adopt this look, update script L27/L77 wording (offer stands).

---

## 1. Why this sheet is built differently

| | Character / prop sheets | This portal |
|---|---|---|
| Background | neutral light-grey | **pure black** — it's an *additive glow*; black keys cleanly with screen/add blending for compositing |
| What's locked | solid identity / geometry | disc silhouette + swirl signature + **open→close states** |
| Lighting | flat studio | self-emissive (the asset IS the light source) |

## 2. Design lock — "The Portal" (green swirl splat)

- **Shape:** a **flat, roughly circular disc** of energy standing vertically in the air (you pass
  through it). Slightly irregular, taller-than-wide is fine. It is a 2D plane — seen edge-on it
  collapses to a thin bright line.
- **Edge:** a ragged, **splattered rim** like flung wet paint — uneven blobs, tendrils, and a scatter
  of green **droplets/specks flying off** the perimeter. Never a clean machined ring.
- **Swirl:** concentric **turbulent swirling** energy inside — a brighter near-white-green hot zone
  toward the centre fading to deeper saturated green at the rim, with a sense of slow rotation / vortex.
- **Colour:** bright **acid / lime green** with teal-green depth. Self-emissive, casts a green glow and
  green spill light, faint heat-haze / refraction just outside the rim.
- **Through it:** an abstract churn of green light and depth — a hint of "elsewhere", never a readable
  scene.

---

## 3. GPT Image 2.0 prompt — PORTAL ASSET SHEET (multi-view + states)

*Text-to-image generate. `model gpt-image-2`, `size="1536x1024"`, `quality="high"` (fine splatter +
swirl detail). Pure black for compositing. ~7 cells.*

```
A VFX reference sheet of a single glowing portal — a swirling disc of energy — on a pure black
background. This is a clean asset/reference document for compositing into film shots, NOT a finished
scene. The same portal is shown from several angles and in several states. Small plain white labels
under each cell.

LAYOUT (tidy grid):
- Top row — four views of the SAME portal:
  "FRONT": facing the portal straight on — the full circular swirling disc.
  "3/4": the disc rotated ~40°, foreshortened into an ellipse, making clear it is a flat plane.
  "EDGE-ON": the disc seen from the side at 90° — it collapses into a thin, bright vertical line of
    green light, proving it is a flat planar disc, not a sphere.
  "TOP": looking straight down from above — the standing disc reads as a thin green elliptical line,
    again showing it is a flat vertical plane.
- Bottom row — three STATES of the same portal, left to right:
  "OPEN": fully open, widest swirling disc.
  "CLOSING": the disc collapsing inward like an iris, smaller and brighter.
  "PINPOINT": almost shut — just a single bright green point of light an instant before it blinks out.

THE PORTAL: a flat, roughly circular disc of bright ACID-GREEN / lime energy standing vertically in the
air. A ragged, SPLATTERED rim like flung wet paint — uneven blobs, tendrils, and a scatter of green
droplets and specks flying off the perimeter (never a clean machined ring). Inside, concentric
TURBULENT SWIRLING energy with a brighter near-white-green hot zone toward the centre fading to deep
saturated green at the rim, suggesting a slow vortex. Self-emissive: it casts a green glow and a faint
heat-haze / refraction just outside the rim. Through the disc, an abstract churn of green light and
depth — a hint of elsewhere, never a readable scene.

STYLE: self-emissive energy, photorealistic VFX element, crisp glow falloff, fine splatter and swirl
detail, no environment, no floor, no horizon, pure black background so it can be keyed for compositing.

CONSTRAINTS — do not include: any background scenery, room, sky, ground or horizon; any person, hand,
character or product; any can or drink; a clean smooth machined ring or solid sphere/orb; readable
imagery or a recognizable scene through the portal; any cartoon character, mascot, or recognizable
branded/trademarked portal design; text other than the small view/state labels; watermarks or logos;
multiple unrelated portals.

Aspect ratio: 3:2 landscape, 1536×1024.
```

**Single-hero variant** (one clean FRONT portal for compositing, no grid) — drop the LAYOUT block and
say: *"A single front-on view of the swirling green portal, centered, on pure black, with generous
black padding for compositing."* Run at `1024x1024` or `1024x1536`.

---

## 4. Compositing / handoff notes

- Render on black, composite with **screen / add / linear-dodge** so the black drops and only the green
  glow + spill land over the loft or battlefield plate.
- The **EDGE-ON** and **PINPOINT** cells are the animation guide: the "snaps shut" beat tweens OPEN →
  CLOSING (iris) → PINPOINT → gone. Drew's entrance/exit reverses it.
- Pass the approved FRONT/3-4 cells to Seedance 2.0 as the portal reference on the loft entrance and the
  battlefield landing/escape shots, re-pasting the §2 design lock each time.
- Keep the chosen green identical across every episode — it's the series' visual signature.

## 5. Alternate look (parked)

The original **jagged white-hot + electric-cyan vertical TEAR** (matches the script's "tear / shrinks to
a seam" wording literally). If you ever prefer that over the green swirl, swap §2/§3's "disc / swirl /
splattered rim / acid-green" language for "vertical jagged tear / frayed edges of light / white-hot core
/ electric-cyan rim / collapses to a thin vertical seam." Pick one and lock it series-wide.
