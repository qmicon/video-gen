# GPT Image 2.0 — Prompting Guide (project canon)

The single reference for the **image-generation step** in this pipeline. Every "sheet" we build —
[character sheets](character-sheet.md), [interior location blueprints](INTERIOR_LOCATION_BLUEPRINT.md),
battlefield/exterior location sheets, and product/prop sheets (e.g. `Sell-By Date/PRODUCT_VAGE_energy_drink.md`)
— renders through this model. Those docs hold *what* to draw; this doc holds *how to prompt the model*.

Distilled from OpenAI's official **`gpt-image-2` prompting guide**
(developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide), published with
the model on **2026-04-21**. Re-verify against the source if a render behaves unexpectedly.

---

## 1. What "GPT Image 2.0" actually is

- Real model id: **`gpt-image-2`** ("ChatGPT Images 2.0"), released **2026-04-21**.
- Native reasoning ("thinks before it draws"), **~99% in-image text accuracy**, multi-panel layouts
  (up to ~8 distinct panels), strong photorealism, and **identity-preserving edits** — the feature our
  whole consistency pipeline leans on.
- Predecessors still callable: `gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini`. **Default to
  `gpt-image-2`** for anything brand- or identity-sensitive (i.e. all our sheets).

### Parameters — these live in the API call, NOT in the prompt text
| Param | Values | Our default |
|---|---|---|
| `model` | `gpt-image-2` | always |
| `size` | `1024x1024`, `1024x1536` (HD portrait), `1536x1024` (HD landscape); gpt-image-2 also allows **flexible sizes** (edges multiple of 16, long:short ratio ≤ 3:1, ≤ 2K reliable, > 2K experimental) | sheets: `1536x1024`; vertical hero/storyboard: `1024x1536` |
| `quality` | `low`, `medium`, `high` | **`high`** whenever there is small/dense text or fine identity detail; `low` only for fast throwaway ideation |
| `n` | integer | use `n=4` for logo/variant exploration |
| `background` | `opaque` / (transparent via downstream removal) | `opaque`; cut out in post if you need alpha |
| `input_fidelity` | *(disabled on gpt-image-2 — always high)* | n/a |

> There is **no negative-prompt field.** State every exclusion inline in the prompt prose
> ("do not include…"). This is why all our sheet docs fold bans into the body.

ChatGPT UI equivalent: pick **Landscape (3:2)** / **Portrait (2:3)** and **high** quality — you don't
type pixel sizes there. An `Aspect ratio: …` line inside the prompt is only a soft hint; `size` is the
real control.

---

## 2. Prompting fundamentals (OpenAI's, verbatim intent)

1. **Structure + goal.** Write in a consistent order — **background/scene → subject → key details →
   constraints** — and **name the intended use** ("a product-reference sheet", "a UI mockup", "an ad")
   to set the model's *mode* and polish level. For complex requests use **short labeled segments / line
   breaks**, not one long paragraph.
2. **Format is flexible.** Minimal prompts, descriptive paragraphs, JSON-ish, instruction-style, and
   tag lists all work. Prioritize a **skimmable template** over clever syntax.
3. **Specificity + quality cues.** Be concrete about materials, shapes, textures, and the medium
   (photo / watercolor / 3D render). Add the literal word **"photorealistic"** to engage photoreal mode
   (also "real photograph", "professional photography"). Detailed camera specs are read loosely — use
   them for *look*, not exact simulation.
4. **Composition.** Specify framing/viewpoint (close-up, wide, top-down), angle (eye-level, low-angle),
   lighting/mood, and **explicit placement** ("logo top-right", "subject centered, negative space left").
5. **People/pose/action.** Describe scale, body framing, gaze, and object interaction ("full body, feet
   included", "hands gripping the handlebars", "looking down at the book, not the camera").
6. **Constraints — change vs preserve.** State exclusions and invariants explicitly. For edits, use
   **"change only X" + "keep everything else the same"** and **restate the preserve-list every
   iteration** to stop drift.
7. **Text in images.** Put literal copy in **quotes** and/or **ALL CAPS**, specify typography (font
   style, size, color, placement), demand **verbatim, render-once**. **Spell tricky/brand/made-up words
   letter-by-letter** — e.g. `"VAGE" (V-A-G-E)` — to maximize character accuracy. Use `quality` ≥ medium
   for small or multi-font text.
8. **Multi-image inputs.** Reference each by **index + description** ("Image 1: product photo… Image 2:
   style reference…") and describe how they interact ("apply Image 2's style to Image 1"; "put the dog
   from Image 2 next to the woman in Image 1").
9. **Iterate, don't overload.** Start from a clean base prompt; refine with **small single-change
   follow-ups** ("make the lighting warmer", "remove the extra can"). Re-specify critical details if
   they begin to drift.

---

## 3. Reusable prompt skeleton

```
A [photorealistic] [INTENDED USE — e.g. product-reference sheet / character sheet / ad] on a
[background]. [One-line mode statement — what this is FOR, and what it is NOT].

LAYOUT: [framing / grid / cell placement, labels].

SUBJECT: [subject + build/materials/colors + 2+ named identity anchors].

TEXT (verbatim, spelled letter-by-letter): "WORD" (W-O-R-D) — [font style, size, color, placement].
Render no other text.

MATERIALS / STYLE: [textures, finish], [lighting], [medium], sharp focus.

CONSTRAINTS — do not include: [exclusions: people, props, scenery, watermarks, extra colors,
gibberish text, etc.].
```
Settings: `model gpt-image-2`, `size=…`, `quality="high"`. (For edits: add `image=[Image 1, …]` and a
"change only X / keep the rest" line.)

---

## 4. Use-case patterns that map to our pipeline

### 4.1 Identity / character consistency  → **character & prop sheets**
OpenAI's "character anchor" workflow is exactly our sheet model: **establish one anchor image, then
reuse it on every later generation with a strict preserve-list.**
- Anchor: lock appearance, proportions, outfit, palette on a plain background, "no text, no watermark".
- Continuation/edit: *"Continue using the same character. Same [outfit], same facial features,
  proportions, and palette. Do not redesign the character."* — restated **every** time.
- This is why our character sheet is a turnaround on neutral grey, and why both the sheet *and* the
  anchor get re-passed into Seedance on every shot.

### 4.2 Product mockups & label integrity  → **product/prop sheets (e.g. VAGE can)**
- *"Preserve product geometry and label legibility exactly. Add only light polishing… Do not restyle the
  product; only [the requested change]."*
- Keep `background="opaque"`; do background removal downstream if you need a transparent cutout.
- Cans/cylinders: a true **back view is low value** (just a wrap + nutrition panel) and invites
  gibberish text — render the back as a near-blank panel instead.

### 4.3 Logos & wordmarks  → **brand marks / lockups**
- Describe brand personality + use case, ask for "clean, original, vector-like shapes, strong
  silhouette, balanced negative space, reads at small and large sizes, flat, plain background, no
  watermark." Use **`n=4`** to explore variants.

### 4.4 Marketing creatives with real in-image text  → **ads, end cards, the brand button**
- Exact copy in quotes, **verbatim, appears once, perfectly legible**, typography + placement specified,
  "no watermarks, no logos" unless intended.

### 4.5 Multi-image compositing & style transfer  → **location chaining / Seedance handoff**
- *"Place [element] from Image 2 into Image 1 at [position]; match lighting, perspective, scale, and
  shadows; do not change anything else."* Mirrors our battlefield "chain off the master frame" method.

---

## 5. This-project gotchas (hard-won)

- **Small repeated label text on a grid can still go soft.** If "BERSERKER ENERGY" / side-strip text
  wobbles, OpenAI's own advice is to render those areas clean and **composite the fine text/logo in
  post** rather than re-rolling endlessly.
- **A supplied logo won't reproduce perfectly from text alone.** Attach it as **Image 1** via an *edit*
  call with the "reproduce this exact mark, do not redesign" line — or render a blank badge area and
  composite the real logo on.
- **Don't overload one pass.** ~6–9 cells is the safe ceiling for a single sheet; cut cells before
  splitting into a second image (the [character sheet doc](character-sheet.md) covers this in depth).
- **Neutrality of reference sheets.** Flat studio light, neutral background, no mood — a sheet that
  acquires a mood passes that mood into every downstream Seedance shot as a constraint.
- **Keep model params out of the prose.** Set `size`/`quality` in the API call; the in-prompt aspect
  line is only a hint.

---

## 6. Pre-flight checklist (any sheet/asset before it ships)
- [ ] Intended use named in the first line (sets the mode)
- [ ] Labeled segments, scene → subject → details → constraints order
- [ ] 2+ named identity anchors (for identity/product sheets)
- [ ] Literal text in quotes + ALL CAPS, brand words spelled letter-by-letter, "render no other text"
- [ ] Exclusions stated inline (no negative-prompt field exists); watermarks/logos banned unless intended
- [ ] `model gpt-image-2`, `size` set correctly, `quality="high"` if any small text/fine detail
- [ ] For edits: "change only X / keep everything else the same", preserve-list restated
- [ ] Reference images addressed by index ("Image 1: …") when attached
