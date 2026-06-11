# Seedance 2.0 — English Prompting Blueprint (project canon)

The single reference for the **video-generation step**: how to turn an approved shot list +
storyboard into ≤15-second Seedance 2.0 generations, in English. Parallel doc to
[GPT_IMAGE_2_PROMPTING_GUIDE.md](GPT_IMAGE_2_PROMPTING_GUIDE.md) (which owns the *image* step).
The shot list owns *what happens*; the storyboard owns *what it looks like*; **this doc owns how
the prompt is written.**

Distilled from, in priority order:
1. **Official ByteDance/BytePlus "Dreamina Seedance 2.0 series prompt guide"**
   (docs.byteplus.com/en/docs/ModelArk/2222480, updated 2026-06) — formula, reference syntax,
   shot sequencing, consistency FAQ. **Overrides everything below where they conflict.**
2. [`seedance-2-pro-director/SKILL.md`](seedance-2-pro-director/SKILL.md) — anchoring, spatial
   locks, final-frame control
3. [`shotlist-builder/reference/PROMPT_DENSITY.md`](shotlist-builder/reference/PROMPT_DENSITY.md)
   + [`MICRO_BEATS.md`](shotlist-builder/reference/MICRO_BEATS.md) — chunking + performance
4. apiyi.com official-guide interpretation (6-step formula, 8 camera moves, speed keywords,
   negative checklist) · ChatCut/LinkedIn guide (@asset jobs, use-as vs reference, asset
   priority) · the 21-page "Cinematic Scene Instructions" PDF + "Same Day Again"/"Tired Girl"
   example prompts (beat-row structure, continuity locks, realism rules)
5. [`storyboard.md`](storyboard.md) — the per-panel handoff this blueprint supersedes for
   multi-shot chunks

> **Language decision:** prompts are written in **plain physical English**. The
> `shotlist-builder` Chinese house format exists in this repo but is NOT used for Sell-By Date
> unless explicitly switched.

---

## 0. Two official corrections (read first — they override earlier drafts)

1. **No hard timecodes inside the prompt.** Official guide, verbatim: *"The model's support for
   precise timing (such as 0–3 seconds) is unstable, and forcibly limiting duration may lead to
   abnormal generation results."* Use **`Shot 1: / Shot 2: / Shot 3:`** labels in story order
   and let the model pace naturally; steer rhythm with pacing words ("a brief flash", "a
   sustained hold"). The chunk map's timecodes remain **planning/edit targets**, not prompt
   text. (Community "timeline prompting" with 0–3s stamps exists and sometimes works — treat it
   as a fallback experiment, never the default.)
2. **Multi-view character sheets risk "twins."** Official guide, verbatim: *"Using
   multi-view character images is not recommended. Multi-view assets contain different angles of
   the same character, and the model may easily identify them as multiple different subjects."*
   **Project practice (proven across Ep1 videos 1–5): the WHOLE sheet works when framed with an
   explicit anti-twin clause** — *"@Image1 is his character reference sheet: it shows the SAME
   man from multiple angles — one person, not several people"* — plus the constraint *"appears
   exactly ONCE per shot, never two of him in any frame."* The official headshot-crop +
   full-body-crop split is the **fallback** if a take still produces duplicates or identity
   wobble (one-variable swap). Same anti-twin framing applies to multi-panel storyboards
   ("the panels show the SAME man at N moments — not N different people").
3. **Read [`Sell-By Date/EP1_SCENE_STATE.md`](Sell-By Date/EP1_SCENE_STATE.md) before writing
   any Ep1 prompt.** Rules live here; the scene's current ANSWERS (standing geography lock,
   prop/wound states, registers, produced chunks) live there — paste its lock blocks verbatim,
   never re-derive them. Update it after every approved generation.

---

## 1. Hard platform constraints

| Constraint | Value |
|---|---|
| Max output duration | **15 seconds** (4–15s selectable) · up to 2K, native audio |
| Aspect ratio (Sell-By Date) | **4:3 horizontal** (~1.33:1) — override every 16:9/21:9 default. Landscape also measurably reduces accidental subtitles |
| Inputs | ≤9 images (<30MB) · ≤3 videos (2–15s total ≤15s, <50MB) · ≤3 audio (≤15s, <15MB) · **≤12 files combined** |
| Recommended asset load | **4–5 assets only**: 1–2 character images + 1 scene + 1 camera-ref video + 1 audio. Maxing the limit causes style conflicts and subject confusion |
| Asset order = priority | The more precisely an asset must be followed, the **earlier** it goes in the prompt/upload order |
| References | **re-attach every prompt** — generations have no memory |
| Real faces | identifiable real-face photos are blocked — keep using our generated sheets |
| Dialogue budget (planning) | 2.5 words/sec; 3.5–4 wps only for written-panicked delivery |
| On-screen text | composited in post; prompts carry "avoid generating any text or subtitles" |

---

## 2. Chunking — shots → ≤15s videos

Run BEFORE writing any prompt. Output: a chunk map (video N = shots a–b, per-shot in/out
timecodes **for the edit**, not for the prompt).

**Group consecutive shots into one video when ALL hold** (PROMPT_DENSITY):
1. Same character set · 2. Same location · 3. Continuous temporal/emotional unit ·
4. Total ≤15s at 2.5 wps + pacing norms · 5. ≤ ~3 dominant actions

**Split when ANY fires:** location cut · major character entrance/exit · a performance arc
deserving its own envelope · a complex VFX event.

**FUSE into one continuous take when:** consecutive shots are same-axis tight coverage of one
subject (CU → CU → CU) — separate near-identical framings joined by cuts read as jump cuts,
and every cut-seam is an identity-drift opportunity. Write it as "one continuous
uninterrupted shot" with the storyboard panels re-framed as "consecutive MOMENTS within this
single shot," beats joined by "without a cut" connectives, and at most one camera move (e.g.
a slow push in the final beat). (Proven on Ep1 Video 4, shots 10–12.)

**The three shot-joint types inside one generation** (declare which, per joint):
1. **Hard cut** — "reached by a hard cut to a new fixed camera position" (default; cheapest).
2. **Cut-on-action** — hide the cut inside a motion that spans it: "joined by one cut hidden
   in the can-lift — he raises it in Shot 1, the cut lands mid-lift, Shot 2 opens on the
   raised object." Motivates inserts so they feel cut-to rather than dropped in; add "no
   jarring camera jump" to constraints. (Proven on Ep1 Video 6, shots 15–16.)
3. **Continuous take** — no joint at all (see FUSE above).

**Long take vs stitching (official):** continuous dialogue/emotional progression in one place →
one generation (or video *extension*); plot turns and fast action → separate clips stitched in
edit. Production reality is a mix.

**Action pacing norms:** whip/insert ~1.0–1.2s · violent beat ~1.5s · scramble/turn ~2.5s ·
establishing read ~3.0s · hook with caption-room ~3.0s · rack-focus reveal ~2.5–3.0s.

**Overflow dialogue → L-cut at edit:** budget the *visual* time in the chunk; the line continues
as off-screen audio over the next shots. Note it in the prompt's audio lines so delivery pacing
matches.

**Storyboard mapping:** chunk's first panel = first-frame anchor ("use as first frame" pins it);
every panel in the chunk is that shot's visual contract. Grid cells are previz only.

**Board production conventions (storyboard prompts):**
- **NUMBERLESS panels.** Baked panel numbers LEAK into the generated video as on-screen
  digits. Order is unambiguous in a strip (left→right); if a board must carry numbers for
  review, make a numberless duplicate for generation, and any prompt referencing a numbered
  board adds "IGNORE the small white numbers — sheet annotations, never rendered."
- **Strip sizes (gpt-image-2, 4:3 horizontal cells):** 2-up row `1536x576` · 3-up row
  `1536x512` · 2×2 `1536x1152` · 5-up (3+2 centered) `1536x768`. Always state "each panel
  framed 4:3 HORIZONTAL, filling its full rectangular frame, no circular vignettes" and
  "exactly N panels — do not add another."
- **Per-shot pinning policy in VIDEO prompts:** a SINGLE frame is safe to pin ("use as
  framing reference for Shot N"); a MULTI-PANEL board is referenced softly ("overall look,
  mood, grade, staging spirit — the Shot Breakdown is the authority") or mapped by position
  ("LEFT panel = Shot 1...") WITH the anti-twin clause — hard per-panel "match exactly"
  pinning of multi-panel boards caused duplicated characters and mid-shot hand-swaps.
- The board is where spatial errors are cheapest to catch — QA the geometry (against
  EP1_SCENE_STATE locks) on the board BEFORE any video generation.

---

## 3. Prompt anatomy — fixed section order

> **House surface format:** the content below is delivered in the team's header-block + shot-
> breakdown style (the "Same Day Again"/"Tired Girl" shape): labeled header fields
> `SUBJECT / PROP / ENVIRONMENT / VFX ASSET / STORYBOARD / MOOD / MUSIC / STYLE / COLOR LOGIC /
> LOGIC RULE`, `<<<image_N>>>` reference tokens, then `Shot Breakdown` lines —
> `SHOT N: [size], [lens] [move] / [transition] into [action + micro-beats] / SFX: [list]` —
> closing with `STYLE NOTE` + `CONSTRAINTS`. Worked example:
> [`Sell-By Date/12_Ep1_Seedance_Video1_Shots1-5.md`](Sell-By Date/12_Ep1_Seedance_Video1_Shots1-5.md).
> The A–H sections below define WHAT must be present; the house format is HOW it's laid out
> (A→header fields, C→ENVIRONMENT/LOGIC RULE, D→SHOT lines, E→STYLE/COLOR LOGIC/STYLE NOTE,
> F/H→CONSTRAINTS, G→written into the final SHOT line).

One prompt = one ≤15s generation. Sections in this order:

```
A. TASK + SETTINGS    One line: what this is. "Generate a 15-second 4:3 live-action scene,
                      [N] shots." (Duration/AR/resolution are also set as API/UI params.)
B. REFERENCE ROLES    One line per asset, exact job, priority order. Use the official verb
                      split: "use Image N as ..." (pins/controls) vs "reference Image N for ..."
                      (borrows). Bind characters: facial features → headshot image; body/
                      wardrobe/state → full-body image. Resolve conflicts explicitly.
C. UNIVERSAL LOCKS    Everything that must hold across all shots:
                      - location bearings (battlefield: banner LEFT, pike-wall RIGHT, ridge
                        ahead, mud foreground — these never flip)
                      - character anchors: identity + state (mud/blood) + wardrobe + 2 named
                        identity anchors, re-bound to images
                      - prop locks (VAGE can never leaves Drew's hand when hands visible)
                      - object specs (longsword ~1m slender blade, cruciform crossguard)
                      - STYLE LOCK block (see §5)
D. SHOT BLOCKS        "Shot 1: ... Shot 2: ..." in story order, NO timecodes. Each shot
                      written in the official internal order:
                      1) camera / transition ("cut to...", "the camera follows in a medium
                         shot", "slow push-in") — ONE primary camera move per shot
                      2) subject action + expression (body-part-specific, quantified,
                         micro-beats not adjectives)
                      3) position / spatial change (screen thirds, depth, contact points)
                      4) audio for this shot: <SFX>, {dialogue}, （music cue）
E. STYLE + QUALITY    One compact paragraph applying to the whole video (see §5).
F. CONTINUITY         "The character's face remains stable without deformation; movements are
                      natural and smooth, with no stutter or flicker." + what carries in from
                      the previous video (state, momentum) + anti-twin block if 2+ characters.
G. FINAL FRAME        One sentence: the exact composition the video ends on.
H. CONSTRAINTS        Short negative tail (see §7).
```

**Length discipline:** simple single-shot prompts ~60–100 words (official sweet spot);
multi-shot prompts run longer but every word must earn its place — *"Do not directly use the
complete script as the prompt"*; no redundancy, no semantic conflicts.

**Dialogue syntax (official):** dialogue in `{curly braces}` — *"She says {I was kidding}"*;
SFX in `<angle brackets>`; music in `（parentheses）`. One line per close-up; the speaker's shot
owns the line. Keep all dialogue one language.

---

## 4. Camera grammar

**The 8 supported movement families** (use standard terms — the model knows them):

| Move | Terms | Use for |
|---|---|---|
| Push-in | push-in, dolly in | emphasis, emotion, the Turn |
| Pull-out | pull-out, dolly out | reveal, aftermath |
| Pan | pan, lateral motion | scanning, re-framing |
| Tracking | tracking shot, follow | walking, chases |
| Orbit | orbit, arc | unify a group, product hero |
| Aerial | aerial, drone, crane | scale, establishing |
| Handheld | handheld, slight realistic shake | panic, documentary energy |
| Fixed | fixed, locked-off | trap a subject, let action play |

**Rules:**
1. **One primary camera move per shot** (official: *"Do not require push, pull, pan, and move
   at the same time"*). Compound = primary then secondary: "low tracking shot, then a subtle
   rise."
2. **Rhythm words, not specs:** slow / gentle / gradual / smooth / controlled / steady.
   Lens-mm and f-stops from the shot list translate to *composition language* ("tight close-up,
   compressed background"), not jargon the model reads loosely.
3. **Speed ladder:** imperceptible → slow → smooth/controlled → dynamic/swift. **"fast" is the
   single most quality-degrading word** — if pace must be fast, make only ONE element fast
   (camera OR subject OR cutting, never all).
4. **Camera and subject motion in separate sentences**, always: "The dancer spins slowly. The
   camera holds a fixed frame."
5. **Transitions are actions, not labels:** write what initiates the cut and what it resolves
   into ("the whip-pan lands on...", "cut on the grab to a low angle over Drew's shoulder").
6. Shot-list grammar → Seedance grammar: WHIP → "fast whip pan" (use sparingly); SNORRI →
   "camera locked to his body, background lurching"; RACK → "focus shifts from X to Y";
   DUTCH → "the frame tilts slightly off-level"; SLO/RAMP → "the moment stretches into slow
   motion, then snaps back."

---

## 4b. Spatial precision language (how to place anything in the frame)

Hard-won on Ep1 (hand-swaps, two-Drews, blade entering the wrong side, gauntlet on the wrong
collar). The model cannot do mirror math or infer trajectories — every spatial fact is
computed by US and written in SCREEN terms. Rules:

1. **Screen language is the primary coordinate system.** "Screen-left / screen-right /
   bottom-right corner / upper third — as we face the subject." Anatomical sides are stated
   only WITH their screen mapping: "his RIGHT hand — appearing on the SCREEN-LEFT of frame."
2. **Do the mirror math before writing; never delegate it.** A character FACING the camera
   mirrors (his left hand = screen-right). A character facing AWAY from camera — or standing
   between camera and subject, facing the subject — KEEPS his sides (his left = screen-left).
   Work out which case applies, then write only the resolved screen direction.
3. **Off-frame actors: specify each limb's FRAME-ENTRY EDGE, not just the contact point.**
   "His left gauntlet enters from the SCREEN-LEFT edge…" Contact-point-only specs let the
   model route both arms in from one side (the tangle failure). Companion rule, stated
   explicitly: "the two arms never enter from the same edge."
4. **Elongated objects get a TRAJECTORY: entry point + path + endpoint.** Not "the blade is
   at his neck" but "the blade enters at the BOTTOM-RIGHT corner and runs DIAGONALLY up and
   left, its flat meeting the SCREEN-LEFT side of his neck." Both endpoints, named path.
5. **Contact points are specified to the body-landmark level.** "Fist gripping the muddy
   shirt fabric just below the jaw on the screen-left side, at the junction of collar and
   shoulder, knuckles toward camera, the shirt bunched in its grip."
6. **Hand–object assignments are locked once, globally** (HAND LOCK block): which hand holds
   which prop, "never changes hands, never lets go" — then re-pinned inside any shot where
   the hands act.
7. **Congested regions get explicit stacking or time-staggering.** If three elements share
   screen-left (gauntlet, checking hand, blade tip), order them spatially ("just above the
   gripping fist") or temporally (the hand checks while the blade is eased off).
8. **Marks and wounds are side-locked with an exclusion:** "the thin blood line is on the
   SCREEN-LEFT side of his neck — and nowhere else."
9. **Two on-frame characters get side assignments + axis rule:** "Drew LEFT, the Commander
   RIGHT; they never swap sides and never cross the frame's vertical center axis" — held
   across every shot where both appear (the 180° rule, written as screen law).
10. **World landmarks vs camera freedom:** location bearings never flip ("banner LEFT,
    pike-wall RIGHT") but pair them with "each shot views the battlefield from its OWN
    camera position" — otherwise a location ref or bearings text freezes the camera.
11. **Crowd geometry is a number plus a constancy clause:** "the melee at about TEN PACES on
    all sides, same density and positions in every shot — only the camera changes."
12. **Name the negative twin of the failure you just fixed:** after moving the blade to the
    bottom-right entry, also write "no blade entering from the left edge." A corrected
    placement without its exclusion regenerates the old one ~half the time.
13. **Occlusion is stated from BOTH directions.** When two elements cross in depth, say who
    is in front AND who blocks whom: "the blade passes BEHIND his raised hand — the hand
    stays in FRONT, nearer the camera; where their paths cross, the hand occludes the
    blade." A bare "behind" gets the depth order wrong ~half the time. (Caught on the Ep1
    shots 10–12 board, middle panel.)

**Canonical worked example (Ep1 shots 10–12 GEOGRAPHY LOCK):**
> The Commander stands between camera and the man, just off-frame, facing him. His LEFT
> gauntleted hand enters from the SCREEN-LEFT edge and lies closed on the SCREEN-LEFT side
> of the man's collar — gripping the shirt just below the jaw, at the junction of collar and
> shoulder, knuckles toward camera. His RIGHT hand holds the longsword down and off frame at
> BOTTOM-RIGHT: the blade enters at the bottom-right corner and runs DIAGONALLY up and left,
> its flat meeting the SCREEN-LEFT side of the neck, just above the gripping fist. The blood
> line is on the screen-left side of the neck and nowhere else. The man's RIGHT hand appears
> screen-left and touches that spot; his LEFT hand, holding the can, hangs low at the
> BOTTOM-RIGHT edge, barely in shot. The two arms never enter from the same edge.

These rules apply equally to storyboard (GPT Image 2) and video (Seedance) prompts — the
storyboard is where spatial errors are cheapest to catch, so spend the precision there first.

---

## 5. Style lock (per-video, verbatim-stable)

Lighting is **the highest-leverage element in the whole prompt** (official emphasis). The style
lock is a fixed block pasted into EVERY video of a scene, never paraphrased — paraphrase = grade
drift between chunks.

Build it as: **medium + era/grade + lighting + palette + texture + realism clause.**

**Sell-By Date battlefield style lock (canonical, paste verbatim):**
> Live-action cinema footage shot on 35mm motion-picture film, candid and documentary, not
> retouched. LIGHT SOURCE: bright overcast sky from above and slightly behind the subjects —
> subjects' backs to the sky, their faces on the shadow side toward camera; low-key,
> high-contrast, cool ~5600K daylight diffused by smoke, volumetric beams breaking through;
> real specular highlights on polished armor. Muted faded color like a 1960s–70s European
> historical war epic: organic film grain, halation around the bright sky, soft focus falloff
> at frame edges, low saturation, rich light-and-shadow layers. Real skin with visible pores,
> sweat and grime; real fabric weave, real wet mud.

(The LIGHT SOURCE sentence comes from the shot list's own lighting lock — "camera from the
shadow side, subjects backs-to-sky, low-key high-contrast" — a named source + direction is
also the anti-plastic lever; never reduce it back to sourceless "soft overcast light.")

**Style keyword families that work:** cinematic film tone / 35mm look · film grain, analog,
vintage · warm tone, cool palette, desaturated · moody, documentary, natural · HD, rich
details, sharp. **Banned solo:** "cinematic" alone, epic, beautiful, amazing, masterpiece.

**Lighting vocabulary:** golden hour · rim light · natural/window light · neon · backlit ·
**overcast/diffused** (ours) · practical lamps · monitor glow. Name the light source and
direction every time it matters ("portal casts green spill light on the mud from screen-left").

**Named setups (from `shotlist transcriptions/` Eps 12–13 — the source of the shot list's
lighting locks; use per-shot where the beat calls for it):**
- **Short-side ("smart side") lighting** — light the side of the face away from camera =
  dramatic; this is what "camera from the shadow side" means. Broad side = approachable.
- **Backs-to-sun/sky** — subjects backlit by the bright source, faces in softer bounce
  (exterior-day default; ours).
- **Top lighting** — source overhead obscures the eyes in shadow = menace → the Commander's
  interrogation shots (hazy sky as top light, eyes in helmet shadow).
- **Split lighting** — key on half the face, no fill = ominous → Margo's warning (#54, as
  specced).
- **Catchlight/eyelight** — a glint in the eyes gives them life → use when calculation must
  read in a CU (Drew's Turn, #12).
- **Negative fill** — block fill to deepen the camera-side shadow; raises facial contrast
  without adding light (also an anti-plastic lever).
- **Warm-practical vs cool-spill contrast** — interior-night formula (warm lamps/monitor glow
  against the portal's cold spill) → the Scene 2 loft look; "either very rich and warm, or
  very cold."
- **Low-key / high-key** — fill strength sets the mood; ours is low-key high-contrast.

**Style drift fixes (official):** (a) add explicit style constraint words; (b) if a reference
image's style fights the target style, **convert the reference image to the target style first**
(GPT Image 2 edit pass), then use the converted image as the Seedance ref; (c) restate the
style lock identically in every chunk.

### Product-hero shots (the placed ad)

The one sanctioned exception to the anti-polish rule — split the treatment explicitly:
**"candid and unflattering on the man, clean and heroic on the product."** The hero insert
keeps the scene's grade and grain, but the product is crisp, condensation-beaded, label
razor-sharp, with its brand color as **the only saturated color in the frame** (the
brightest-object eye magnet). Land the dialogue's most aspirational clause ON the product
via L-cut ("...I carried it across the earth — for you" over the glinting can), and when
the chunk ends on the hero, **end held on the product** — the ad's last frame is the ad.
Motivate the insert with a cut-on-action joint (§2). (Proven on Ep1 Video 6, shot 16.)

### Anti-plastic protocol (AI/waxy skin — known failure, hit on Ep1 Video 1)

Root cause is usually the **reference**: plastic in, plastic out — Seedance treats refs as
appearance ground-truth. Two rules dominate everything else:

**Rule A — pixel budget: skin texture needs resolution to exist.** A face under ~300px tall
(any grid/sheet cell) physically cannot carry pores; Seedance reads its smooth shading as
"this man has smooth plastic skin." **Skin-bearing Seedance refs must be full-resolution
single images** (per-panel re-renders, headshot crops) — never grid cells, never whole sheets.
"Add pores" edits on small faces cannot work; there is nowhere for the pores to render.

**Rule B — give a physical camera reality, not texture adjectives.** The AI look = (1)
describing *what*, not *how it was photographed*; (2) lighting with no named source; (3)
asking for perfection. The fix formula for any prompt or de-AI edit:
> [camera body + lens + aperture + shutter] + [film stock + grain/halation/aberration/falloff]
> + [light SOURCE + direction + color temperature + shadow direction] + [explicit
> imperfection list: pores, sweat, grime in creases, stubble, asymmetry, chapped lips, slight
> motion blur] + [anti-perfection words: candid, documentary, amateur, unflattering,
> imperfect] — and drop "ultra-realistic / professional / high-resolution portrait" (they
> trigger the retouched-commercial prior). The model needs explicit permission to be imperfect.

Fix stack, in leverage order:
1. **Re-photograph the refs full-res** ("re-render this exact frame as if genuinely shot on
   35mm motion-picture film in 1975…" + Rule B formula; identity/composition preserve-list).
   One panel first as the one-variable test, then scale to all skin-bearing refs.
2. **Carry the camera formula into the Seedance STYLE block** ("Shot on an Arriflex 35BL,
   50mm at T2.8, Kodak color negative, organic grain, halation, slight edge falloff; candid,
   documentary, imperfect").
3. **Positive skin line in SUBJECT** (pores, sweat, grime, stubble, redness, uneven light).
4. **Break smooth shading physically:** wetness/particulates (damp hair, breath fog, mud in
   face creases) — soft overcast light flatters like a beauty dish.
5. **Negatives tail:** "no beauty filter, no skin smoothing, no plastic or waxy skin."
6. **Post fallback:** film-grain overlay + slight sharpen.

---

## 6. Reference discipline

**Syntax:** `Image 1 / Video 1 / Audio 1` or `@Image 1` — both official. Every asset gets ONE
explicit job line; an unassigned upload is noise.

**Verb split (changes behavior):**
- **"Use Image N as ..."** — pins/controls (first frame, identity, scene base)
- **"Reference Image/Video N for ..."** — borrows a quality (style, motion, camera, rhythm)
- For *editing/extending* an existing clip say `Video N` directly — *"do not use 'reference
  Video N'"* or the task is misread as a reference task.

**Character binding (official pattern):**
> Define the mud-caked man in Image 1 (headshot) and Image 2 (full body) as DREW. Drew's facial
> features follow Image 1; his body, wardrobe and mud state follow Image 2.
- Headshot = face only, minimal shoulders/background, neutral expression
- **Name the subject on every appearance** — *"Each time a subject is involved, it must be
  explicitly referred to."*
- 2+ characters: bind each to its image at every mention ("Drew (Image 1–2) ... the Commander
  (Image 3–4)") and add the anti-twin constraint (§7)
- >4 characters in frame degrades stability — pre-compose groups into one reference image

**Camera-movement video refs:** a 2–15s clip showing the move ("Reference Video 1 for camera
movement only") beats long prose — strongest tool for exotic moves (Snorricam, dolly-zoom,
whip-into-slow-mo). Build a small library of move-reference clips over time.

**Location-master refs FREEZE the camera.** An attached establishing/master frame pulls every
shot toward its exact camera position (and a per-shot "matching @ImageN" binding makes one
shot obey the image while its neighbors follow text — the source of crowd/density mismatches).
Either DROP the master and carry the location in text bearings + "each shot views the
location from its OWN camera position," or attach it with a style-only role: "reference ONLY
for terrain/atmosphere palette and grade — never for camera position, framing, or
composition." Masters are safest on tights (palette anchor), most dangerous on wides.

**Opening-state frame ref (seamless joins):** when a new chunk must open exactly where the
last ended, attach the previous clip's FINAL FRAME (or the desired expression frame) as
"@ImageN = the exact expression and state at the moment this video begins — the video starts
on this face and transitions out of it." Same face on both sides of the cut, change happens
on camera. For @Video tail refs, the §12 hard-cut rule applies (state-only, camera not
inherited).

**Other official template patterns:** subject reuse ("Reference the [subject] in Image N...
maintaining consistent features") · effects transfer ("the way the portal opens should
reference Video 1") · extension ("Extend Video 1 backward/forward + new content only") · track
completion ("Video 1 + transition description + followed by Video 2").

---

## 7. Constraints tail (standard block)

End every prompt with (trim to relevance):

> The characters' faces and body proportions remain stable without deformation. Movements are
> continuous and natural, not stiff, with no clipping, stutter, or flicker. Avoid jitter, bent
> limbs, temporal flicker, and identity drift. Keep it subtitle-free; avoid generating any text
> or captions; do not generate a logo or watermark. [If 2+ characters:] Throughout the video,
> characters with completely identical appearance, clothing, and accessories are prohibited —
> do not generate duplicate avatars or a twin effect; keep only the single corresponding
> character for each reference. [If a hero prop recurs across shots or appears in a macro
> insert:] ONE [can] only — never a second or duplicated [can]. [Project:] No modern objects
> except the VAGE can and Drew's clothing; no golden-hour warmth; no HDR; no 3D-render or
> animation look.

Plus the seedance-2-pro-director rule: anything expressible as a **positive lock** goes in C/D
("his boots stay planted on the same mud marks"), not here.

---

## 8. Performance writing (action + emotion)

- **Body-part-specific, quantified:** "slowly raises one hand", "pushes hard off the ground",
  "slightly lowers his head" — never bare "moves/reacts".
- **Prefer slow, coherent, subtle movement**; high-burst action (sprints, big jumps, violent
  rolls) is where AI video breaks — keep one burst per shot maximum, ground it with contact
  points.
- **Emotions externalized as physics** (official + MICRO_BEATS): terror → "breath fast and
  shallow through the mouth, eyes darting, hands half-raised, weight shifting backward";
  the closer waking up → "his breathing slows, the trembling stops, his eyes narrow from
  darting to fixed"; cold command → "unhurried, jaw set, eyes steady, words through gritted
  teeth".
- **Physical verbs over soft ones:** snap, whip, slam, drag, buckle — not "becomes/transitions".
- **Sound as motion cue:** a heavy <body fall thud> implies weight; <blade ring> implies
  impact. Write the SFX that *enforces* the physics.
- **Transitions between actions:** give the connective ("uses the recoil of the spray to
  stumble backward into the mud").

---

## 9. Cross-video continuity protocol

1. **State handoff:** video N's end state (positions, mud/blood, props, light) is written into
   video N+1's C/F sections as the opening condition. No reset in motion or posture.
2. **Character state escalation is explicit:** `drew_muddied` crops (shots 1–28) →
   `drew_muddied_bloodied` crops (shot 29+). Attach the matching state's images; never ask the
   model to add/remove blood itself.
3. **Re-paste everything every prompt** — identity bindings, style lock, bearings, prop locks.
   **Background population is continuity state too:** lock crowd density and placement
   ("the melee stays midground/background at the SAME density in every shot; the foreground
   pocket stays clear") — otherwise each shot invents its own crowd. (Caught: Ep1 Video 1,
   shot 2 vs shot 3 soldier counts.)
   **But constancy language FREEZES backgrounds unless motion is separately requested.**
   "Same density and positions" + "movement is minimal" (meant for the subject) gets applied
   to the whole frame — a still-photo background with no ambient sound. Always pair the
   constancy lock with explicit environmental motion ("the background battle is ALIVE and
   CONTINUOUSLY MOVING — blows traded, smoke drifting; constant density means same size and
   distance, NOT frozen") and a continuous-audio clause ("a continuous battle bed runs under
   the ENTIRE take — never silence"), and scope stillness to the subject ("Drew's stillness
   applies to HIM only"). The four motion layers — subject, internal, camera, environmental —
   are specified separately, every prompt. (Caught: Ep1 Video 4, frozen melee + silent bed.)
4. **Seams:** prefer chunk boundaries on hard cuts. Invisible seam needed → official
   **extension** ("Extend Video 1 forward...; original segments are not re-generated") or pass
   video N's final frame as "use as first frame" for video N+1. Stitch fix in edit: trim ~6
   frames from the end of clip N and ~1 frame from the start of clip N+1.
5. **Audio seams:** L/J-cuts are edit decisions; generate clean per-video audio.

### Voice consistency across runs (voice anchors)

Runs share no audio memory — a character's voice re-rolls every generation unless anchored.
Official mechanism: **"Reference the timbre in Audio N"** (≤3 audio clips/run, ≤15s each).

1. **Build a voice anchor library once, before batch production:** generate the character's
   first dialogue video a few times, pick the take with the right voice, extract a clean 5–10s
   solo-voice snippet (minimal bed noise — the "headshot crop" of audio), save it
   (`drew_voice_anchor.mp3`, `commander_voice_anchor.mp3`). Optionally regenerate the source
   video against its own anchor so video 1 conforms too.
2. **Attach + bind on every speaking run:** "Audio 1 = Drew's voice reference. Drew's dialogue
   uses the timbre of Audio 1 — [voice description]." Official FAQ: the clip AND a text
   description of the voice together, plus **write the line in the same register as the
   anchor** (a screamed line against a calm anchor drifts) — keep per-state anchor variants if
   a character spans registers.
3. **Slot budget:** one anchor per speaker; 2 speakers = 2 of 3 audio slots (1 left for
   ambience/music ref).
4. **Series fallback — TTS dub:** lock a TTS voice ID per character, generate Seedance with the
   dialogue (mouth animates to the line), replace the voice track in the edit. Perfect
   cross-episode consistency; use if anchor drift shows up.
5. **Clip-tail artifact (official):** dialogue clips often end with a click/cut-off — put an
   audio fade on every clip tail in the edit.

---

## 10. Iteration method (official)

1. Baseline: generate 2–3 takes of the prompt.
2. **Change ONE variable at a time** (camera, motion intensity, style, one shot's action).
3. Score on: continuity · instruction adherence · edit usability.
4. Keep a three-tier template per scene: **starter** (short, direction check) → **production**
   (full anatomy §3) → **fallback** (radically simplified when output destabilizes).

If a video jitters: more than one camera move? the word "fast"? fast camera + fast subject +
busy scene stacked? Fix those before re-rolling.

---

## 11. QA checklist (before any prompt ships)

- [ ] §0 corrections respected: Shot N labels (no timecodes), headshot+full-body crops (no
      multi-view sheet attached)
- [ ] Duration ≤15s; 4:3; settings in section A and as generation params
- [ ] 4–5 assets, each with exactly one job line, priority-ordered, "use as" vs "reference"
      chosen deliberately
- [ ] Characters bound to images at EVERY mention; anti-twin block if 2+
- [ ] One primary camera move per shot; camera and subject motion in separate sentences; no
      unqualified "fast"
- [ ] Spatial spec passes §4b: screen-language only (mirror math pre-resolved), frame-entry
      edges for off-frame limbs, trajectories for blades/elongated props, side-locked wounds,
      hand-object locks, axis rule for two-character shots, negative twin of any fixed
      placement
- [ ] Shot blocks in official internal order (camera → action → spatial → audio)
- [ ] Dialogue in {braces}, verbatim from script, owner-shot only, planned L-cuts noted
- [ ] Every speaking character has a voice anchor attached + bound with a timbre description
      (§9); line register matches the anchor
- [ ] Style lock pasted verbatim (not paraphrased); lighting source + direction named
- [ ] Emotions externalized as physical micro-beats; zero banned adjectives
- [ ] Prop/object specs present (can, longsword, portal design)
- [ ] Continuity + final frame sections present
- [ ] Constraints tail present; positive locks preferred over negatives
- [ ] No on-screen text requested; "subtitle-free" stated

---

## 12. Sell-By Date Ep1 — paste-ready blocks

### Reference set per battlefield video (priority order)
1. Image 1 — Drew headshot crop (from `drew_muddied` sheet)
2. Image 2 — Drew full-body crop (mud state)
3. Image 3 — Commander headshot crop · Image 4 — Commander full-body crop
4. Image 5 — VAGE can (front cell crop from the prop sheet)
5. Image 6 — battlefield master frame (scene + grade) · Image 7 — portal front view (video 1
   only)
(7 images total for Video 2-type shots is above the recommended 4–5 — drop the Commander
headshot or merge can-in-hand into the full-body crop if instability appears.)

### Bearings (section C, verbatim)
> The burning banner stands on the ridge to the LEFT. The dense silver pike-wall of infantry
> holds the RIGHT. The hazy slope rises ahead. Deep churned mud fills the foreground. These
> bearings never flip.

### Style lock — battlefield (section E, verbatim — directional version)
> Live-action cinema footage shot on 35mm motion-picture film, candid and documentary, not
> retouched. LIGHT SOURCE: bright overcast sky from above and slightly behind the subjects —
> subjects' backs to the sky, their faces on the shadow side toward camera; low-key,
> high-contrast, cool ~5600K daylight diffused by smoke, volumetric beams breaking through;
> real specular highlights on polished armor. Muted faded color like a 1960s–70s European
> historical war epic: organic film grain, halation around the bright sky, soft focus falloff
> at frame edges, low saturation, rich light-and-shadow layers. Real skin with visible pores,
> sweat and grime; real fabric weave, real wet mud.

### Drew binding + prop lock
> Define the mud-caked man in Image 1 (headshot) and Image 2 (full body) as DREW: dark hair,
> mud-caked white shirt, loosened dark tie. Drew's facial features follow Image 1; his body,
> wardrobe and mud state follow Image 2. Drew keeps the black VAGE can from Image 5 clutched in
> one hand in every shot where his hands are visible — he never drops it or sets it down.

### Commander binding + weapon
> Define the armored knight in Image 3 (headshot) and Image 4 (full body) as the COMMANDER:
> mirror-polished plate armor, the same helmet throughout. His weapon is a knightly LONGSWORD —
> a straight, slender, double-edged steel blade about one metre long with a simple cruciform
> crossguard; the full long blade is always shown, never a short sword or dagger.

### Portal (video 1)
> The portal from Image 7 is a FLAT vertical disc of acid-green energy with a ragged splattered
> rim and a bright near-white-green swirling core, standing at ground level — a flat planar
> disc, never a tunnel or hole. It casts green spill light on the mud and on Drew.

### Ep1 chunk map (edit targets; prompts use Shot N labels only)
| Video | Shots | Duration | Edit in/out per shot | Condition |
|---|---|---|---|---|
| **1 — "Arrival & Denial"** | 1–5 | ~13.7s (gen 14s) | 3.0 / 3.0 / 2.5 / 1.2 / 4.0 | Drew's line panicked ~3.5 wps; ends mid-word on the grab. PRODUCED |
| **2 — "The Grab"** | 6 alone | ~3s (gen 4s, trim) | single shot | continuity via @Video ref = Video 1's 3s tail; sword stays SHEATHED; ends on the locked grab. PRODUCED |
| **3 — "The Interrogation"** | 7–9 | ~14.3s | 7: 10.3 (draw+swing 1.5 + speech 8.8) / 8: 1.2 / 9: 2.8 | the sword DRAW opens shot 7 (6 ends sheathed); Commander's last ~4s of line L-cuts over 8–9; "Which?" lands on the body drop; casts the Commander's voice |
| **4 — "The Denial Dies"** | 10–12 | ~10.5s | 10: 2.0 / 11: 5.5 / 12: 3.0 | pure Drew performance arc; #12 the Turn needs air + a catchlight; first run attaching drew_voice_anchor |

Boundaries are hard cuts (clean seams). Single-shot chunks (like Video 2) take the previous
clip's ~3s tail as a @Video continuity reference — the strongest no-reset tool we have.

**Tail-reference rule (caught on Video 4):** a @Video tail ref makes the model try to
CONTINUE the tail's framing — it morphs/zooms from the old composition into the new shot.
Every tail-referenced prompt must declare: (1) in TASK — "this video OPENS on a HARD CUT;
its first frame is already Shot 1's framing from a new fixed camera position"; (2) in the
ref role — "@Video1 is a STATE reference only (appearance, light, crowd, grade), NOT opening
footage; the story continues, the camera does not"; (3) in CONSTRAINTS — "no camera movement
bridging from @Video1's composition — never a zoom, push, or morph from the previous
framing."

---

*Next step: draft Video 1 and Video 2 full prompts against §3, QA with §11.*
