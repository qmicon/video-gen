# Shot List QA Checklist — pre-flight before calling a shot list "done"

A reusable validation pass for any StudioBinder-method shot list in this pipeline. Derived from real mistakes caught while building `Sell-By Date/10_Ep1_Shot_List.md` (Ep1 run), then expanded by a full audit of all 27 source transcriptions (2026-06). Run every row through this before moving to storyboards. Tags like `[07]` point to `./README.md` / the source transcription.

---

## A. Physical-consistency checks (the spec must be possible)

1. **Wide/fisheye lens ≠ shallow focus.** `[04][07]` Ultra-wide and fisheye glass (≤~24mm) has huge depth of field — you *cannot* throw the background soft. Wide/fisheye → **DEEP**. Only 50mm+ can carry SHALLOW. (Caught at #8: fisheye + SHALLOW.)
   - **1b. RACK requires shallow-capable glass.** A rack tagged on ≤35mm in a WS won't read — both planes are already near-sharp. Lengthen the lens (50mm+) or restage as deep-focus two-plane blocking with eye-trace. (Caught at #9, #30.)
   - **1c. A zoom's END focal length must satisfy the Focus tag too**, not just its start (e.g. a dolly-zoom ending at 35mm can't promise SHALLOW without a note).
2. **Rig vs. camera-height must agree.** `[05]` A **Snorricam** is body-mounted to the actor (face locked, world spins) — it is **not** ground-level or on a tripod. Don't pair `SNORRI` with `GND`/`STATIC`. Snorricam's natural home is an upright, moving, panicked subject. (Caught at #1 and #17.)
   - **2b. Body-mounted rigs LOCK subject framing.** No size changes (`MS→FS`) within a SNORRI row — the mount fixes the distance. And the rig must survive the physical action staged inside its own row (no chest rig grinding into the mud). (Caught at #31.)
3. **`STATIC` + `RACK` is legal** (a focus-pull on a locked camera) — *not* a contradiction. Don't "fix" it.
   - **3b. But `STATIC` is incompatible with any mid-shot angle/position change.** `EYE→DUTCH` is a camera **ROLL** — a movement. Mid-shot changes require a movement token. (Caught at #29: "STATIC hold" + "EYE→DUTCH".)
4. **A rack/lens move between two subjects = at least a 2-shot.** `[02][04]` If a shot racks from a foreground person to a background person, both are in frame — it can't be a clean `1S`. (Caught at #16.)
5. **Slow-mo/undercrank discipline.** `[08]` Only tagged SLO/RAMP/UNDER shots leave 24fps. Confirm each deviation is intentional.
   - **5b. Every SLO/RAMP/UNDER states a numeric capture rate or slow-down factor** (48fps/2x vs 120fps/5x is the difference between drama and spectacle); presentation rate (24fps) stated once at the top. `[08]`
   - **5c. A RAMP must resolve within a single shot.** A ramp annotation spanning a cut is two separate speed decisions — specify each. (Caught at #28→#29.)
6. **Lens changes mid-shot must be achievable on one zoom.** `MACRO→50`, `FISH→35`, prime-to-prime: impossible on one piece of glass. (Caught at #41.)
7. **MACRO is only legal for static micro-detail** an actual macro lens could hold (blood bead, label, keycap). Fast-moving or hand-scale action inserts take standard glass. `[07]` (Caught at #26, #19.)
8. **POV legality.** `[02][10]` A POV may never frame its own holder (face OR body — you can't watch your own chest), the camera position must be a plausible eye position, and every POV/POV-insert has an **owning eyeline** in an adjacent shot. POV rows carry **subjective audio** (hear what they hear). (Caught at #26, #36, #41.)
9. **Legend↔grid token sync.** Every Move/Rig/FX/angle token used in any row exists in the legend (ROLL and ZOOM were used but missing). Lens column uses one format (`mm` everywhere), with the format anchor ("all mm = full-frame equivalent") declared once. `[25]`
10. **Every Move cell names move + platform.** A bare "WHIP-pan" with no rig is an uncommitted cell. `[26]` (Caught at #28.)
11. **Cap simultaneous within-shot changes at two.** More than two `→` transitions in one row (size + framing + angle + lens at once) = split the shot or write an explicit justification — each stacked transition multiplies AI-generation failure odds. `[26]` (Caught at #41: four.)

## B. Direction-of-technique checks (the move must point the right way)

12. **Dolly-zoom focal direction.** `[16]`
   - *dolly-IN + zoom-OUT* → subject grows, background **stretches/expands** → lens goes **long→short** (e.g. `85→35`). Feeling: world opens up / realization.
   - *dolly-OUT + zoom-IN* → subject fixed, background **compresses/closes in** → lens goes **short→long**. Feeling: paranoia / closing in.
   - Pick the feeling first, then make the lens arrow match. (Caught at #31: lens arrow was backwards.)
   - **12b. A dolly-zoom row must specify its BACKGROUND** — deep, layered, with parallax cues / leading lines behind the subject. A close or flat background kills the effect before it's shot (the Severance failure). State start/end shot size and whether the subject-size ratio is deliberately broken (Squid-Game variant). `[16]`
13. **Push-in vs zoom are different.** `[06]` Push = camera moves (emphasis/internal). Zoom = focal length changes, "unnatural," for unease/creep. Use the one the emotion calls for.
14. **Low = power, High = weak.** `[03]` Confirm the angle matches who should feel dominant in the beat.
   - **14b. Power-pairing completeness.** In any dominance scene, the weak party actually receives HIGH coverage — not only the strong party receiving LOW. Half a pairing understates the imbalance. `[03]`
   - **14c. Reverses respect established VERTICAL positions.** If one party is on the floor, the reverse onto the standing party is LOW (from the grounded side), not EYE. (Caught at #34, #39.)
15. **In `OTS (X fg)`, X is the foreground *shoulder* — the subject is the OTHER person.** `[02]` And the angle's emotional effect lands on **that in-focus subject, not the foreground shoulder.** Cross-check: (a) does the OTS favor whoever the beat is about? (b) does the angle empower the right person? Tell: if a line belongs to X but the row says `OTS (X fg)`, you've framed the *listener* — verify intended. (Caught at #14 and #17.)
16. **`cut-on-action` requires the action to span the cut.** `[10]` Incompatible with a `1S→2S` entrance being the cut point: an in-frame arrival is a mid-shot event. Either `1S→2S` + in-frame intrusion (cut on a *later* motion), or `2S` + cut-on-action. (Caught at #6.)
17. **Moving rows state blocking direction.** TRACK/FOLLOW = lead / trail / lateral — the direction *is* the emotion (trail = suspense, lead = power, lateral = spectacle). `[18]`
18. **Move-duration sanity.** Slow PUSH / ARC / dolly-zoom rows need enough seconds in the timing plan to actually read. A 10s speech on a 2s slot isn't a slow push. `[18]`

## C. Notation hygiene (one shot per row)

19. **No either/or slashes in spec cells.** A `/` like `OTS/POV` or a range like `18–24` forces the reader to pick. **Commit to one.** Genuine alternatives get an explicit `Alt:` note. (Caught at #1, #8, #12, #16, #18, #39, #43.)
20. **`→` only means change *within* the shot.** Never splice spec categories (`FS→2S` mixes size and framing). (Caught at #5.)
21. **Framing column is never empty.** Every row has a framing, even inserts. (Caught at #39.)
22. **Notes must not re-introduce slashes** the grid removed.
23. **No unresolved placeholders** (`[BRAND]`, TBD) in any cell once the referenced asset sheet exists. (Caught at #16: `[BRAND]` despite a locked VAGE sheet.)

## D. Coherence checks (it must add up as a sequence)

24. **Every spec serves the stated Lever.** If the Lever says "Vulnerability," the angle/size/focus should diminish, not empower.
25. **Shot/reverse pairs share geometry.** `[10]` A reverse roughly mirrors the angle/lens of the shot it answers (and see 14c for vertical positions).
26. **Cross-references stay in sync.** Grid ↔ deep-dive ↔ transitions map ↔ sequence map.
27. **"Dirty single" needs a real dirty element.** `[02]`
28. **Track physical state continuously — restraint, vertical position, hero props, AND background population.** Crowd density/placement around the subject is continuity state — a clear foreground in one shot can't become a surrounding melee in the next. (Caught in generation: Ep1 shots 2→3.) `[24]` Grab → release → up/down, *and* every hero prop's holder/position shot-to-shot (the can after the Commander dies — who has it?). Any prop an actor engages with late must be **planted** in an earlier master. (Caught: collar release ~#17; Drew's fall #29→#31; can after #23; VAGE case at #48 unplanted.)
29. **Scene-coverage check.** Every scene has an establishing AND a master (or an explicit decision not to) — the master fixes character geography for the edit and is the cross-chunk continuity anchor for AI generation. `[01]`
30. **Size-curve pass.** Chart sizes across each scene: CUs sit on climaxes, a wide re-grounds after them; flag any run of ≥6 consecutive tight singles. `[15]`
31. **Every RACK names source → target AND speed** (snap = shock, slow = contemplative) — rack speed is an emotional spec. `[04]`
32. **Transition labels are precise.** `[09][10]`
   - **J/L direction:** "A's audio over B's image" = **L-cut**; "B's audio before leaving A's image" = **J-cut". Name whose audio leads/trails. (Caught at #35: mislabeled J.)
   - A **match cut** must name the matched element (shape/color/movement/sound) in both shots; a **smash cut** specifies the contrast on both visual AND audio axes; **dip-to-black** is within-scene, **fade-to-black** is closure.
33. **Every ★★★ shot names its single attention device** (focal point / leading line / brightest-object / color pop) — if you can't name what pulls the eye, the storyboard guesses. Plus a **brightest-object audit**: nothing in the spec outshines the stated attention magnet in the same frame. `[11]`

## E. Lighting checks `[12][13]`

34. **Vocabulary is correct per scene:** natural/ambient (exterior day) vs practical vs motivated. "Practicals-only" cannot describe a daytime battlefield.
35. **Every light and every mid-scene lighting CHANGE names its motivation** (sun, lamp, monitor, portal, fire, gold-bounce). An unmotivated source under a motivated-only rule fails. (Caught at #45: "warm key creeps in" — motivate as gold-bounce.)
36. **Track lighting state like body state.** A lighting change introduced mid-scene (#45's warm creep) must be resolved in subsequent rows — persists, dies, or wins.
37. **Per-scene contrast-ratio target stated** (e.g. S1 ≈8:1 grim low-key; S2 ≈4:1) — the one number that keeps separately-generated chunks consistent. Color temperature per source stated once and held.
38. **Every ★★★ CU/MCU carries a face-lighting spec** — key direction, fill ratio, catchlight y/n. Eye-acting beats (a Turn, a conversion) get explicit **catchlights**; concealed-intent beats get top-light/eyes-in-shadow.

## F. Sound checks `[19][21][22]`

39. **Acoustic-space tag per scene** (exterior-open / interior-room) — generated dialogue must not contradict the space (no podcast-booth voices at swordpoint).
40. **Dialogue audibility plan** wherever dialogue shares the frame with a loud bed (battle): prompt the bed down, or strip/rebuild in post.
41. **A continuous background bed per scene** spans every chunk boundary (battle bed S1, room tone S2) — beds glue AI chunk seams and cover dialogue imperfections. Never total silence; designed near-silence keeps a floor.
42. **Recurring design effects are single reusable assets** (portal whoosh, can crack-hiss, blade SHING, coin cascade) — identical at every occurrence, never chunk-baked. List them.
43. **POV rows carry subjective audio** (muffled, close-breath).
44. **Audio workflow gates:** picture lock → dialogue pass → effects → music → mix. Treat generated audio as the dialogue stem only.

## G. Motion / performance checks (the 12 principles) `[20]`

45. **Anticipation:** every major physical action (grab, throw, swing, dive) includes its windup, unless surprise is the explicit point — and even then the *mover* gets one.
46. **Moving holds:** every freeze/stare row specifies micro-motion (breath, blink, drip, settle) — a truly still character reads dead or morphs.
47. **Follow-through:** impact/stop rows specify what continues and settles (cloak, hair, coins, cloth).
48. **Secondary action** named where it characterizes (trembling hands under a smooth sales voice) and kept away from the face.
49. **Silhouette test** every ★★★ storyboard frame: the beat must read with faces and color removed.
50. **No twinning** in group shots — asymmetric poses across characters.

## H. Pipeline / production checks `[14][23][24][27]`

51. **Ref/asset column:** every row points to its locked asset sheets and the correct character-sheet STATE variant (drew_muddied vs drew_muddied_bloodied from #29).
52. **Every location and hero prop appearing in any row has a locked asset sheet** (Ep1 gaps: loft, gold pouch/coins, VAGE case).
53. **Per-shot durations exist; every generation block sums to ≤15s;** dialogue timed at 2.5 wps fits its shot's seconds.
54. **Caption plan exists** (muted-feed ads): ≤17 chars/sec, ≤2 lines × ≤50 chars, one sentence per caption; hero-visual rows tagged NO-CAPTION (product hero, money shot, the kill); captions never straddle a scene cut without ending past it; committed contrast treatment (border/shadow).
55. **Animatic gate:** TTS/scratch-record the dialogue and cut the previz boards to it BEFORE any video generation — validates every block duration on arithmetic, not hope.
56. **Generation-status field** per row (boarded / first-frame approved / rendered / final) so the edit isn't archaeology.

---

## How to run it
Read each row left-to-right as one sentence, then check it against A–H. The fastest tell for a broken row: you can't picture a single, physically-possible frame from it. If you have to ask "which option?", it fails check 19. Then run the scene-level passes (29, 30, 37, 41, 53–55) once per scene.
