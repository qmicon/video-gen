# Storyboard Blueprint (project canon — the image step between shot list and video)

The single reference for **producing storyboards/beat boards** with GPT Image 2.0. Sits
between [the shot list] and [SEEDANCE_2_PROMPTING_BLUEPRINT.md](SEEDANCE_2_PROMPTING_BLUEPRINT.md):
the shot list owns *what happens*, the board owns *what each moment looks like*, the video
blueprint owns *how it moves*. Model mechanics (sizes, edit calls, text rules) live in
[GPT_IMAGE_2_PROMPTING_GUIDE.md](GPT_IMAGE_2_PROMPTING_GUIDE.md). **This doc supersedes the
older `storyboard.md` wherever they conflict** (that doc predates gpt-image-2, the 4:3 lock,
and the filmic pipeline).

> **Before any Ep1 board: read [`Sell-By Date/EP1_SCENE_STATE.md`](Sell-By Date/EP1_SCENE_STATE.md)
> and paste its lock blocks verbatim. After approval: update it.**

---

## 1. Role and workflow

1. **One board per generation chunk** (per the video blueprint's chunk map), drawn from the
   shot-list rows. Boards are mandatory before video — *"it helps the video model a lot"*,
   and the board is where spatial/expression errors are cheapest to catch.
2. **Approval gate:** the board is QA'd (§6) and human-approved before any video generation.
   Iterate the board, not the video — a face is re-rolled in seconds; a clip is not.
3. **Handoff:** approved panels become the video prompt's per-shot composition refs (§7).

## 2. Prompt anatomy (fixed order)

```
A. REFERENCE ROLES   One line per attached image, exact job:
                     - character sheets: "shows the SAME man from multiple angles — one
                       person, not several; reproduce this exact man; do not redesign him"
                       (the anti-twin clause, every time)
                     - location master: STYLE-ONLY — "reference ONLY for background
                       content/palette/grade — never for camera position, framing, or
                       composition" (masters freeze the camera; safest on tights)
                     - prior approved board: STATE-ONLY — "reference ONLY for the man's
                       exact state, blade/gauntlet design, light, grade — NOT for framing"
                     - an actual video frame: "the PHYSICAL TRUTH of the moment — match
                       grip, blade, light, grade exactly"
B. GEOGRAPHY LOCK    Pasted from EP1_SCENE_STATE, in screen language per video-blueprint
                     §4b (frame-entry edges, trajectories, occlusion both directions,
                     side-locked wounds, hand-object assignments, negative twins).
C. TASK + LAYOUT     "A STORYBOARD STRIP of EXACTLY N sequential film frames..." — panels of
                     identical size, each 4:3 HORIZONTAL filling its full rectangular frame
                     (no circular vignettes), thin black gutters, matte-black ground,
                     NUMBERLESS (see §4), "exactly N panels — do not add another", "NO text
                     of any kind" (the product label is the only exception, when in frame).
D. PHYSICAL REALITY  The anti-plastic block, verbatim: "frames genuinely photographed on
                     35mm motion-picture film on a working film set in 1975 — Arriflex 35BL,
                     spherical lenses, Kodak 35mm color negative. Organic film grain,
                     halation, soft focus falloff at frame edges. Candid, documentary,
                     imperfect — not retouched, no beauty filter, no digital polish."
E. LIGHT             The scene's directional light lock (named source + direction + temp +
                     contrast), never sourceless "soft light".
F. CONTINUITY        Character state (mud/blood per the state ledger), prop-in-hand locks,
                     skin realism positives (pores, sweat, grime), background crowd alive
                     and at its locked distance, "never identical twins" on extras.
G. PER-PANEL BLOCKS  One per panel (§3).
H. CONSTRAINTS       The negative tail: no extra panel; no text/numbers/watermarks; no
                     speech bubbles; no comic/sketch style; no portrait or square panels; no
                     gore beyond the state ledger; weapon spec ("slender longsword, never a
                     cleaver"); no plastic/waxy skin; no character drift; the negative twin
                     of every recently-fixed placement.
```

## 2b. Spatial precision — placing people, hands, weapons, props in the frame

The board's core job. The model cannot do mirror math, infer trajectories, or guess depth
order — every placement is computed by US and written in SCREEN terms. (Full doctrine:
video blueprint §4b; this is the working set for boards, where these errors are cheapest to
catch.)

**Geometry authority hierarchy — use the highest rung available:**
1. **An actual produced frame** that shows the standing geometry → **delta-prompt from it**
   (§2c). Don't re-specify in words what the frame already proves.
2. No frame covers it → **paste the written lock from EP1_SCENE_STATE verbatim.**
3. Brand-new geography (first time staged) → derive it yourself with the rules below, then
   write the result into EP1_SCENE_STATE after approval.

1. **Screen language first:** "screen-left / screen-right / bottom-right corner — as we
   face the subject." Anatomical sides only WITH their mapping: "his RIGHT hand — appearing
   on the SCREEN-LEFT of frame."
2. **Mirror math is pre-resolved, never delegated:** a character FACING camera mirrors (his
   left = screen-right); a character facing away — or standing between camera and subject,
   facing the subject — keeps his sides. Work out which case applies; write only the result.
   Better: paste the resolved lock from EP1_SCENE_STATE instead of deriving at all.
3. **Off-frame actors: name each limb's FRAME-ENTRY EDGE**, not just its contact point
   ("his left gauntlet enters from the SCREEN-LEFT edge…"), plus the companion rule: "the
   two arms never enter from the same edge."
4. **Elongated objects (swords, spears, poles) get a TRAJECTORY** — entry point + path +
   endpoint: "the blade enters at the BOTTOM-RIGHT corner and runs DIAGONALLY up and left,
   its flat meeting the SCREEN-LEFT side of his neck." Never just "the blade is at his neck."
5. **Contact points to the body-landmark level:** "fist gripping the muddy shirt at the
   junction of collar and shoulder, just below the jaw, knuckles toward camera, the shirt
   bunched in its grip."
6. **Hand–object assignments locked:** which hand holds which prop ("the can stays in his
   LEFT hand — screen-right — throughout"), and which hand performs each action ("he touches
   his neck with his RIGHT hand only").
7. **Depth/occlusion stated from BOTH directions:** "the blade passes BEHIND his raised
   hand — the hand stays in FRONT, nearer camera; where they cross, the hand occludes the
   blade." A bare "behind" gets depth order wrong ~half the time.
8. **Congested screen regions get explicit stacking or time-staggering:** if three elements
   share screen-left (gauntlet, checking hand, blade tip), order them spatially ("just above
   the gripping fist") or across panels (the hand checks while the blade is eased off).
9. **Marks/wounds side-locked with an exclusion:** "the thin blood line is on the
   SCREEN-LEFT side of his neck — and nowhere else."
10. **Two on-frame characters: side assignments + axis rule:** "Drew LEFT, the Commander
    RIGHT; they never swap sides and never cross the frame's vertical center axis" — held
    across every panel where both appear.
11. **Negative twins:** after fixing any placement, ban its old position ("no blade entering
    from the left edge") — a corrected placement without its exclusion regenerates the old
    one about half the time.
12. **Subject placement per panel:** state where the subject sits (center-frame /
    off-center frame-left with a blurred shoulder edging frame-right), what occupies the
    foreground vs background, and where the attention magnet is.

## 2c. Delta prompting from a produced frame (the strongest geometry tool)

When a panel continues a moment that already exists on film, attach **the actual frame**
(cropped from the produced video — prefer it over a beat-board panel: it is the exact
preceding state, grade included) and write the panel as a **delta**:

> "Image N = the ACTUAL FRAME from the immediately preceding shot: the physical truth of
> this moment. Panel X continues directly from Image N — take its exact subject and
> blocking and change ONLY [TWO] things: [the camera angle] and [the raised hand]."

Rules of the pattern:
- **Count and name the deltas** ("change ONLY TWO things") — then direct each delta with
  full §2b precision (the low angle's effect: "the camera dropped BELOW him looking UP, the
  sky filling the space behind his head"; the new placement: "the can held up beside and
  slightly above his head at top-right").
- **Enumerate the UNCHANGED list explicitly** — the standing geometry (grip, blade, blood,
  wardrobe) listed as "UNCHANGED from Image N", not re-specified by side/edge in fresh
  words. Fresh words can only agree with the frame or fight it.
- **Anchor constraints to the frame, not to prose:** "blood anywhere except where it appears
  in Image N" · "the blade stays at his throat exactly as in Image N" — the frame becomes
  the constraint baseline.
- **QA against the source frame:** verify each named delta happened (compare the new angle
  to the frame's eye-level) and nothing else changed.

Same pattern serves video prompts (opening-state frame, §6 of the video blueprint) and
single-panel edits (§5) — it is the general form of "change only X, keep everything else."

## 3. Panel doctrine

- **One panel = one shot's REPRESENTATIVE MOMENT** — usually mid-shot, the frame that proves
  the beat (the grab landed, the blade placed, the expression turned). Pull it from the
  shot-list action line.
- **Camera spec translated, not pasted:** the row's size/angle/lens become composition
  language ("low-angle medium close-up over his soft foreground shoulder, 50mm compression").
- **Expressions are decomposed micro-beats**, never adjectives — and contradictory states are
  spelled out ("his face must read both things at once: still afraid, already selling";
  "the smile assembles mouth first, eyes last").
- **Every key panel names its attention device** (brightest object / leading line / color
  pop) and should pass the silhouette test.
- **Continuous-take chunks:** the panels are "consecutive MOMENTS within one single
  continuous shot, not separate shots" — say so in the prompt that consumes the board.
- **The hardest panel gets the budget.** One panel per board is the acting/geometry target
  (the Turn, the blade placement) — be pickiest there; everything downstream inherits it.

## 4. Conventions

- **NUMBERLESS panels.** Baked numbers leak into the generated video as on-screen digits.
  Reading order is left→right (state it). If a numbered copy is needed for review, generate
  a numberless duplicate for production use.
- **Strip sizes** (gpt-image-2, `images.edit`, `quality="high"`): 2-up `1536x576` · 3-up
  `1536x512` · 2×2 `1536x1152` · 5-up (3 top + 2 centered) `1536x768`. All cells 4:3
  horizontal. Singles/full-res re-renders: `1024x768` or `1536x1152`.
- **Resolution rule (anti-plastic Rule A):** faces under ~300px cannot carry skin texture —
  if a panel's face is too small to judge, re-render that panel solo at full frame; the solo
  render doubles as the video's expression reference.
- **Combining separately-generated panels** into one board: composite mechanically (PIL/
  ffmpeg — equal heights, black ground, thin gutter), don't re-generate.

## 5. Iteration (one variable at a time)

- **Single-panel edits, never re-rolls of a good board:** "Edit Image 1. DO NOT change the
  LEFT panel. DO NOT change the RIGHT panel. Change ONLY the MIDDLE panel, and in it change
  ONLY the sword. Keep everything else exactly as rendered." Name what's preserved
  explicitly (faces, grade, layout).
- **Spatial fixes name both directions of occlusion** ("the blade passes BEHIND his raised
  hand — the hand stays in FRONT, nearer camera, occluding the blade") and **the negative
  twin** of the failure ("remove the blade fragment at the screen-right edge; no blade
  enters from the left edge").
- **Plastic skin on a board:** don't "add pores" — re-photograph the panel full-res with the
  PHYSICAL REALITY block (the 1975 formula). Texture adjectives don't flip the prior;
  a complete camera reality does.
- **Stubborn artifacts:** total-removal-plus-one-allowed-remnant ("remove ALL blade metal
  except a single out-of-focus sliver at the extreme bottom-right corner") beats
  repositioning instructions.

## 6. Board QA (before approval)

- [ ] Geometry matches EP1_SCENE_STATE's lock: entry edges, blade trajectory, wound side,
      hand-object assignments, two-character sides
- [ ] State ledger respected (mud/blood stage, prop in the right hand, sword up/down per the
      current shot number)
- [ ] The hardest panel's expression reads (decomposed beats visible, catchlight if specced)
- [ ] All panels 4:3 horizontal, uniform size, numberless, no text/vignettes
- [ ] Skin filmic (no wax), grade matches produced footage, background crowd present at the
      locked distance, extras varied
- [ ] Attention device legible per key panel; silhouette test on the ★★★ frames

## 7. Handoff to the video prompt

- A **single approved frame** may be pinned hard ("use as the framing reference for Shot N"
  / "use as first frame").
- A **multi-panel board** is referenced softly ("overall look, mood, grade, staging spirit —
  the Shot Breakdown is the authority") or position-mapped ("LEFT panel = Shot 1...") WITH
  the anti-twin clause. Hard per-panel "match exactly" pinning of multi-panel boards caused
  duplicated characters and mid-shot hand-swaps.
- Crops taken from boards for video use are 4:3 crops.
- After the chunk is approved: **update EP1_SCENE_STATE.md** (state ledger, chunk ledger,
  any new locks the chunk established).
