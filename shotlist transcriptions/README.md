# Shotlist Transcriptions — AI Video-Ad Reference

A working reference for the ViralAdsGen video-gen pipeline, distilled from the 27 transcriptions in this folder (StudioBinder's "The Shot List" series + related episodes). It covers two things:

1. **The production reference** — everything in the transcriptions that matters for generating video ads: the vocabulary you feed a text-to-video model, the technical numbers to set as defaults, and the craft systems that make output look intentional.
2. **The emotion → technique recipe book** — start from the *feeling* you want the viewer to have and get the stacked techniques that produce it.

**Grounding rule:** every fact below is extracted directly from the transcriptions. Each item is tagged with its source file (e.g. `[07]` = `07_Ep07_Camera_Lenses.txt`). Quoted figures are verbatim. Nothing is invented — where a transcript didn't state something, it's left out. Open the cited file for full explanations, film examples, and detail beyond this summary.

> **Core principle (from the whole series):** every technical choice is an emotional lever. Nothing is neutral. A "neutral" choice (eye-level, medium shot, 24fps, soft cut) is itself a deliberate decision to *not* push the viewer.

### Contents
- [Part 1 — The prompt vocabulary](#part-1--the-prompt-vocabulary)
- [Part 2 — Technical defaults (the numbers)](#part-2--technical-defaults-the-numbers)
- [Part 3 — Lighting setups](#part-3--lighting-setups)
- [Part 4 — Transitions & editing](#part-4--transitions--editing)
- [Part 5 — Sound design pipeline](#part-5--sound-design-pipeline)
- [Part 6 — Production design & color](#part-6--production-design--color)
- [Part 7 — Motion quality: the 12 principles](#part-7--motion-quality-the-12-principles)
- [Part 8 — Camera rigs](#part-8--camera-rigs-movement--look)
- [Part 9 — Shot-list workflow](#part-9--shot-list-workflow)
- [Emotion → technique recipe book](#emotion--technique-recipe-book)
- [Source index](#source-index)

---

# PART 1 — THE PROMPT VOCABULARY
*The precise terms text-to-video models respond to. Use these as the building blocks of a shot prompt: `[shot size] + [framing] + [angle] + [focus] + [movement] + [lens] + [lighting]`.*

### 1.1 Shot sizes `[01]`
- **Establishing shot** — wide enough to establish geography, time of day, and scale of subjects in their environment; opens a scene or film.
- **Master shot** — confirms location/geography, which characters are present and where, captured as the scene plays out in its entirety.
- **Wide shot (WS)** — subject far from camera; about the *scale* of the subject (vs. establishing, which is about location). Makes subjects look lost, lonely, overwhelmed.
- **Full shot (FS)** — subject's entire body fills top-to-bottom of frame; statements about physicality.
- **Medium full / Cowboy shot** — top of head to just below the waist; named for "the height of gun holsters"; confident, dangerous, confrontational.
- **Medium shot (MS)** — "the most popular shot size in all of cinema"; starts above the waist/below the chest to just above the head; neutral.
- **Medium close-up (MCU)** — mid-chest to just above the head; intimacy without losing physicality.
- **Close-up (CU)** — shoulders to top of head; "the most powerful visual weapon for highlighting a change in emotion"; usually at eye level.
- **Extreme close-up (ECU)** — isolates one area (lips, ears, eyes); "the most intimate, dramatic and potentially startling."
- **Insert shot** — isolates a crucial prop/detail; "one of the greatest tools for emphasis."
- **Aerial shot** `[03]` — extreme high angle establishing environments/characters in a larger world.

### 1.2 Framing `[02]`
- **Single** — one character alone. *Clean single* = no other character visible (isolation). *Dirty single* = a limited presence of another character in frame.
- **Two shot** — two characters, both faces clearly visible; builds a relationship.
- **Three shot / crowd shot** — three+ characters; beyond counting it's a "crowd shot."
- **Over-the-shoulder (OTS)** — "a hybrid between a single and a two shot"; covers conversation, "a sense that we are included in the moment."
- **Point of view (POV)** — audience experiences a character's perspective; "often paired with POV audio."

### 1.3 Camera angles & heights `[03]`
- **Low angle** — below the eyeline looking up; makes a subject "look more powerful, perfect for heroes and villains."
- **High angle** — looks down; "diminish a character making them appear weak or vulnerable." Pair with low angle to "heighten the imbalance of power."
- **Overhead / bird's-eye / God's-eye** — camera directly above shooting straight down; detached, objective; good for complex movement.
- **Dutch angle** — skews the horizontal axis; unease, mania; increase tilt as tension rises.
- **Eye level** — most natural, "doesn't impose judgment."
- **Shoulder / hip / knee / ground level** — progressively lower mounts; lower heights often double as low angles; hip level lives in Westerns (holster height); knee/ground are stylish ways to track movement.

### 1.4 Depth of field / focus `[04]`
- **Deep focus** — subject and background both crisp; lets the eye explore; layered action across foreground/middle/background.
- **Shallow focus** — sharp plane of focus, rest soft; isolates a subject; produces **bokeh** (out-of-focus points of light).
- **Soft focus** — no part 100% sharp (diffusion filters, or historically silk/vaseline on the lens); dreams, flashbacks.
- **Rack focus** — a *verb*; shifts the plane of focus between points within a shot without cutting; reveals or connects.
- **Split diopter** — two separate focal points sharp, the area between soft; "an impossible perspective" the human eye can't replicate.
- **Tilt shift** — bends light so an extremely narrow band is sharp; can make a life-size subject look like a miniature.

### 1.5 Camera movement `[06]`
- **Static** — zero movement (locked tripod); dialogue, painterly compositions; can "trap a character."
- **Pan / whip pan** — horizontal rotation from a fixed position; slow pan = anticipation, whip pan = energy + time/space transition.
- **Tilt** — camera points up/down; verticality, dominance/vulnerability.
- **Push in** — moves toward subject; emphasis, internal conflict, rising tension.
- **Pull out** — moves away; "signal to disconnect"; isolation, abandonment.
- **Zoom / crash zoom** — changes focal length (no human-eye equivalent → "unnatural"); slow zoom = unease, crash zoom = drama or comedy.
- **Dolly zoom (vertigo effect)** — dolly + zoom in opposite directions; conflict (internal/external). Also called the Hitchcock shot. `[16]`
- **Camera roll** — turns on the long axis; disorienting; panic/conflict.
- **Tracking shot** — moves *with* a subject (vs. push/pull which move toward/away); immersion. `[18]`
- **Trucking** — lateral left/right movement.
- **Arc shot** — orbits a subject; dynamic energy on a still subject; fast arc = dizziness.
- **Boom shot** — up/down via crane, jib, or pedestal; small = reveal, large = follow action.
- **Random movement** — shake, incidental zooms; "a documentary look," "events happening in real time."

### 1.6 Lenses & focal length `[07]`
Focal length = distance from the lens's optical center to the sensor, in mm. Longer (e.g. 100mm) = narrower angle of view; shorter (e.g. 24mm) = wider.
- **Fisheye** — extreme wide-angle with heavy distortion; named example "a four millimeter fisheye"; "exaggerate facial features when used in close proximity."
- **Extreme wide-angle** — **18mm–24mm**; close-ups and landscapes in one shot.
- **Wide-angle** — **24mm–35mm**; accentuates movement; creates distance in tight spaces; stylized.
- **Standard / normal** — **35mm–50mm**; "most similar to how the human eye sees the world"; grounded, natural. (Call Me by Your Name shot entirely on 35mm; The Godfather mostly on a 40mm.)
- **Telephoto / long lens** — **70mm and up**; distant subjects; "compress space"; "isolating a character in a crowd." (Named extreme: "a 1200 telephoto lens.")
- **Macro / micro** — defined by 1:1 (or 5:1) magnification and minimum focusing distance, not a fixed focal range; sharpest extreme close-ups.
- **Prime vs zoom** — prime = fixed focal length, sharper, larger aperture (more light, shallower DoF); zoom = variable focal length, smaller aperture, saves time.

### 1.7 Composition `[11]`
- **Rule of thirds** — place the subject at one of the four intersections of the vertical/horizontal thirds.
- **Golden triangle / golden ratio (1:1.618) / golden spiral** — diagonal + perpendicular lines, or the Fibonacci spiral, for balanced focal points.
- **Lines** — vertical = height/strength; horizontal = distance/calm; diagonal = off-tilt energy; curved = grace. **Leading lines** pull the eye.
- **Shapes & frames within frames** — clean geometry = tidy/satisfying; irregular = natural/chaotic; a frame-within-frame narrows focus.
- **Space** — *headroom* (kept minimal), *lead/looking room* (more space in front of a subject than behind), *negative space* (isolation), *filling the frame* (sensory overload/chaos).
- **Depth** — foreground / middle ground / background; the illusion of 3D in a 2D medium.
- **Balance** — *rule of odds* (odd-numbered groups are more pleasing), symmetry (Wes Anderson).
- **Color & tone** — schemes: monochromatic, analogous, complementary, triadic; "color can even overrule other methods of composition"; the eye goes to the brightest part of the image.

### 1.8 Aspect ratio for close-ups `[15]`
- Narrow (**4:3**, or The Lighthouse's **1.19:1**) — removes background, all attention on the face.
- Wide (**1.85**, **2.39**, Munich's **2.35**) — preserves background, enables two-shots.
- Lens on faces: **50mm and above** flattens the face; **28mm and below** stretches/distorts it.

---

# PART 2 — TECHNICAL DEFAULTS (the numbers)
*Set these as pipeline presets. All figures quoted from source.*

### 2.1 Frame rate `[08]`
- **24 fps** — "the most cinematic frame rate"; emulates traditional cinema.
- **48 fps** (The Hobbit — reduce motion blur/3D eye strain), **120 fps** (Gemini Man) — high frame rates, hyper-real.
- **Slow motion** = shoot *higher* than the playback rate (overcranking, e.g. 48 or 120 fps); "the higher the frame rate the slower you can slow down footage while maintaining smooth motion."
- **Fast motion** = shoot *below* 24 fps (undercranking; Austin Powers fembots at "two frames").
- **Step printing** — low fps + slow shutter for blur/streak, then frames copied to reach 24 fps (Domino: 6 fps, each frame printed 4 extra times).
- **Speed ramp** — transition between speeds within a single shot (300).
- **Capture rate vs presentation rate** — "for normal speed motion the presentation rate must equal the capture rate"; "it is your presentation rate that matters."
- **Rule:** "don't mix frame rates if you want normal looking motion" — only mix deliberately for slow-mo or a choppy/jittery aesthetic.

### 2.2 Color temperature (Kelvin) `[12]` `[13]`
- **Daylight ≈ 5600K** (bluer). **Tungsten ≈ 3200K** (warmer/orange). **Moonlight ≈ 4100K.**
- Mixing: "tungsten lights adding orange and daylight adding blue."
- Reference values from setups: Prey lights set **6,000–8,000K** for a cyan moon (greened in post).

### 2.3 Audio levels & EQ `[21]` `[22]`
- **On-set recording peaks: between −6 and −12 dB.** "Hitting zero dB could cause distortion."
- **Mix: dialogue centered at around −10 dB**, effects built around it. "Nothing should hit zero dB" (peaking → distortion).
- **EQ rules of thumb:** cut background at **1200 Hz** so the voice feels prominent; **boost 160 Hz** for power; **boost 5,000 Hz** for presence; **4,000–10,000 Hz** for clarity.
- **Sampling rate** — most won't record below **48 kHz**; many use **96 or 192 kHz**. **Bit depth** — at least **16 bits** (65,536 values).
- **Room tone** — capture ~**2 minutes** of set silence; laid under the mix "so there's never total silence and cuts between dialogue aren't as jarring."

### 2.4 Captions / subtitles `[27]`
*Critical for muted social feeds — this is where the message lands when sound is off.*
- **≤17 characters per second** of footage.
- **≤2 lines**, **≤50 characters per line**.
- **2–4 frame gaps** between consecutive subtitles, kept consistent.
- Appear "just as a character begins to speak," may linger slightly after; if text lingers past a cut, "make sure it ends a bit after the cut to avoid a visual flicker."
- **Segmentation** — one sentence per caption; break at speech pauses; don't split syntactic units (noun+adjective, first+last name) across a line break.
- **Contrast** — text must contrast with the scene; fix with shadowing or bordering.
- Keep brief in busy scenes; "if there is an important visual you want your audience to see, show it without a subtitle" (subtitles "are very good at attracting a viewer's eye").

### 2.5 Sensor / camera — the "common mistake" `[25]`
- "In practice, lenses, lighting, and composition often have a bigger impact in your image than sensor size alone." "A great shot is a great shot, no matter the sensor size."
- "Larger sensors create shallower depth of field… but only when framing and exposure are matched."
- Larger sensors: better low light, wider dynamic range, shallower DoF, greater field of view. Smaller: cheaper, portable, deeper focus, lighter lenses.
- **Rolling shutter** "scans an image sequentially" → skew artifacts on quick movement; **global shutter** captures the whole frame at once (more noise, narrower dynamic range, runs hotter).

---

# PART 3 — LIGHTING SETUPS `[12]` `[13]`

**Three-point lighting** — *key* (primary/strongest), *fill* (softens the key's shadows; dim/absent = low-key, near key strength = high-key), *backlight* (rim of light separating subject from background). **Negative fill** blocks unwanted light to raise contrast. **Catchlights/eyelights** = reflections in the eyes that "give them life and depth."

**Contrast ratio:**
- **High-key** — low contrast, evenly lit; brighter, happier scenes.
- **Low-key** — high contrast, large light/shadow difference; darker, dramatic scenes.
- **Chiaroscuro** — extreme low-key; film noir.

**Hard vs soft** — hard light = stark shadows, dramatic/intense; soft (diffused) light = romantic/happy; best natural soft light is **golden/magic hour** (just after sunrise, just before sunset).

**Named portrait setups:**
- **Rembrandt** — key higher + dimmed fill → triangle of light on the shadow-side cheek.
- **Butterfly / paramount** — single high frontal key → butterfly shadow under the nose; glamour, smooths imperfections, highlights cheekbones.
- **Loop** — key ~45° and just above eyeline; lengthens the face.
- **Split** — key on half the face, no fill; ominous mystery.
- **Overhead / top** — obscures the eyes. **Underlighting** — unnatural horror shadows.

**Volumetric lighting** `[13]` — light given visible shape (beams) via smoke/dust (Sicario). **Motivated lighting** `[12]` — a logical in-world justification for the light. Exterior tip: place subjects "with their backs to the sun" so it acts as a backlight.

---

# PART 4 — TRANSITIONS & EDITING

### 4.1 Transitions `[09]`
- **Cut** — instant switch; the most common transition.
- **Fade** — to/from a solid color. Fade from black eases in; fade to black = closure or a beat to breathe (Pulp Fiction); within a scene = "dip to black." **Fade to white** = dream, dying, or an ending left to interpretation.
- **Dissolve** — gradual transition into another shot; passage of time, memory, dream. **Superimposition** = both shots visible at once mid-dissolve.
- **Match cut** — uses elements (shapes, composition, color, movement, sound) of one scene to match the next; connects instantly; bridges time/space. **Match dissolve** = the smoothed version.
- **Iris** — focuses the scene on a single emotion/idea; vintage.
- **Wipe** — shot B pushes shot A out from a direction; vintage look (Star Wars).
- **Passing / pass-by (mask) transition** — a moving object or camera move hides the cut; seamless (Edgar Wright).
- **Whip / swish pan** — quick blurred rotation; sustains momentum (Boogie Nights).
- **Smash cut** — abrupt high-contrast cut (quiet↔loud, still↔chaotic); shock or comedy.
- **J-cut (pre-lap)** — audio of the next scene precedes its image (anticipation, flashbacks). **L-cut** — audio carries over into the next scene (narration). "Sound A plus image B creates a more complicated and nuanced meaning."

### 4.2 Editing techniques `[10]`
"Almost all of an editor's work comes down to three choices: what to show, when to cut, and what to cut to."
- **Cut / cutaway** — basic shot-to-shot; cutaway = away from the main action.
- **Rule of Six** — Walter Murch's prioritized criteria for each cut. *(Source names it but does not enumerate the six.)* Pacing drives feel: long holds = mournful/contemplative, rapid cutting = frantic.
- **Eyeline match** — cut to what a character looks at; can build intrigue by withholding the reveal.
- **Shot/reverse shot** — cut between subjects in reverse angles; conversation geography/clarity.
- **Insert** — a detail shot emphasizing a prop/element.
- **Cross cutting** — cut between simultaneous scenes in different locations; ironic juxtaposition (Godfather baptism), multi-front action (Rogue One).
- **Eye trace** — consecutive shots focusing on the same frame area so the eye stays fixed; ideal for action (Mad Max — "put the crosshairs on her nose").
- **Split edits (J/L cut)** — sound or image changes before the other; controls dialogue rhythm, catches reactions.
- **Intellectual montage / Kuleshov effect** — meaning manufactured from juxtaposed images; the viewer makes the connection.
- **Cut on action / cut on impact** — cut during movement for a seamless transition; cutting on impact "gives each punch and kick extra force."

---

# PART 5 — SOUND DESIGN PIPELINE `[19]` `[21]` `[22]`

**Order of work:** dialogue is edited **first** — "it will lay out the framework for the sounds that will fill in around it." The three element categories are **voice, music, sound effects.**

**Effect types `[21]`:** *spot / cut / hard effects* (obvious on-screen sounds — door slams, punches); *design effects* (unnatural noises that must be built); *background / ambient effects* (longer ambient beds). **Foley** = performed everyday sounds (footsteps, cloth). **ADR** = dialogue replacement, "avoided unless absolutely necessary."

**Score vs soundtrack `[21]`:** *score* = music written by a composer for the film; *soundtrack* = any music in the film, including licensed songs not made for it.

**The sound envelope `[21]`:** attack (time to full volume), decay (how fast it levels off), sustain (how long it's held), release (how long it takes to dissipate).

**Why sound matters `[21]` `[19]`:** sound "hits a more primitive area of the brain than images" (its power in horror/thriller); "audiences forgive bad image, never bad sound." Capture clean dialogue on set — reverb and ambience are added in post.

**Capture basics `[22]`:** shotgun mic "no more than 3 feet away"; lavaliers at the costume edge with minimal clothing noise; reduce reverb on set (soft materials, furnies); **dead cat / blimp** for wind, but "the more protection… the more the high frequencies risk getting reduced."

**Deliverables `[21]`:** stereo, 5.1, 7.1, stems (separate dialogue/music/effects), theatrical (more dynamic range) vs streaming/online mixes (less). "Changes to a locked picture are avoided at all costs."

---

# PART 6 — PRODUCTION DESIGN & COLOR `[24]`

- **Goal: "believable, not realistic"** — "the perfect setting for the story… one that is immersive and situates an audience within the narrative."
- **Easiest path to believability:** shoot in a real location.
- **Set decoration** — make a space "feel real and lived in" (furniture, wall decor, textiles, surface clutter) tied to "the psychology of each character… how they live, where they live."
- **Props** — objects an actor engages with directly (vs. decoration, which they don't).
- **Color palette** — "not just an aesthetic consideration. It can symbolize an idea or emotion, direct attention, and can enhance mood." A film can use evolving palettes scene to scene (The Aviator). Designers build **swatch boards** and coordinate with the cinematographer; costumes/makeup must not "clash."
- "A shot can only look as good as what's in it."

---

# PART 7 — MOTION QUALITY: THE 12 PRINCIPLES `[20]` `[14]`
*The rubric for judging whether AI-generated motion reads as alive vs. uncanny (Disney's Thomas & Johnston, "The Illusion of Life," 1981).*

1. **Squash & stretch** — weight and malleability; **maintain constant volume** (stretch one axis → squash the other).
2. **Anticipation** — the windup that prepares the audience for an action.
3. **Staging** — present the core idea of the frame clearly (silhouette test).
4. **Straight ahead vs pose to pose** — frame-by-frame (unpredictable motion like fire/water) vs. key poses then in-betweens (controlled motion).
5. **Follow through & overlapping action** — inertia: appendages keep moving after the body stops; *drag*, *overlapping action*, *moving hold* (idle breathing/blinking).
6. **Slow in & slow out (easing)** — "nothing can stop on a dime"; more frames at the start/end of an action.
7. **Arc** — natural motion travels in arcs, not straight lines.
8. **Secondary action** — supports the primary action without distracting from it.
9. **Timing** — number of frames sets speed and meaning; on ones (detail), twos (faster action), threes (anime/background).
10. **Exaggeration** — heightens emotional reality over strict realism.
11. **Solid drawing** — weight, depth, balance; avoid **twinning** (perfectly symmetrical pose/limbs).
12. **Appeal** — charisma/charm: simplicity, purposeful design, baby-face features for likeability (Dumbo, Mickey).

**Frame-cadence note `[14]`:** US/Disney animates "on ones or twos" (smoother movement); anime "on threes" (more detail per frame). Persistence of vision is the underlying illusion of all motion.

---

# PART 8 — CAMERA RIGS (movement → look) `[05]` `[26]`

Core principle `[26]`: "Every camera rig exists… to best serve the story." "The goal of a good rig is not to be noticed, but to make the best shot possible."

- **Handheld** — meant to be shaky; jagged = intensity, subtle = intimacy/realism; "works best when movement is intentional and limited."
- **Tripod** — fixed support; fluid head pans/tilts; static framing avoids distraction in dialogue.
- **Pedestal** — vertical up/down moves; match an actor, build suspense.
- **Dolly** — wheeled, on straight/curved track; smooth push/pull/track. Economical alternatives: **slider**, **cable cam**.
- **Crane / jib** — extend and glide; isolation, freedom, spectacle in one long take.
- **Stabilizer (Steadicam / gimbal)** — moves freely without shake; ideal for long takes.
- **Snorricam (body mount)** — rigged to the actor's body; vertigo, dizziness, panic.
- **Drone** — aerial establishing and chase shots.
- **Overhead rig / motion control / vehicle mount / underwater housing** — specialty supports for top-down, repeatable, vehicle, and submerged shots.

**Stated mistake `[26]`:** "Beginners… add accessories because they've seen them on other rigs, not because the shot requires them… If it doesn't [help], it's just extra weight." "There is no perfect rig. There is only the best rig that helps you get the shot your story needs."

---

# PART 9 — SHOT-LIST WORKFLOW `[23]`
*The pre-production method to systematize before generation.*

"Showing up to set without a plan can lead to a lot of wasted time and confusion."

1. Start blank or **import the script** so each scene is ready for shot listing.
2. Use the scene preview — **select a line, create a shot from it.**
3. Adjust the details.
4. **Customize specs:** framing, movement, lenses, and more; upload reference images.
5. Arrange shots in shooting order.
6. Customize the column layout.
7. Choose the aspect ratio.
8. **Color-code important shots.**
9. Add prep/shoot times, banners, meal breaks.
10. Group scenes by location or shoot day.
11. Print custom PDFs.
12. Generate a share link so the crew can check off shots on set.

---

# EMOTION → TECHNIQUE RECIPE BOOK
*Start from the feeling you want a shot (or sequence) to land. The levers **stack** — layering shot size + angle + focus + movement + lens + lighting + sound compounds the effect.*

### 😌 Trust / Warmth / Approachability
*Use for: testimonials, founder intros, "we care about you" beats.*
- **Lighting:** high-key, soft/diffused, golden-hour warmth → happy, trustworthy, flattering — `[12]` `[13]`
- **Angle:** eye level → non-judgmental, builds rapport (esp. fourth-wall break to camera) — `[03]`
- **Framing:** medium / medium close-up → natural human-interaction distance — `[01]` `[02]`
- **Color/design:** warm palette, lived-in real location → believable, grounded — `[24]`
- **Sound:** clean, present dialogue (mic close, room tone under it) → intimacy, seamless immersion — `[22]` `[21]`

### 💪 Power / Authority / Aspiration
*Use for: the hero result, the "after" state, the confident expert.*
- **Angle:** low angle → powerful, intimidating, heroic — `[03]`
- **Movement:** slow push-in → emphasis, building importance — `[06]`
- **Framing:** full shot / cowboy shot → physicality, confidence, "in all their glory" — `[01]`
- **Composition:** deep focus = power hierarchy; vertical lines = strength — `[11]`
- **Sound:** boost ~160Hz for vocal power; bespoke score swell — `[21]`

### 🥺 Vulnerability / Empathy / Pain Point
*Use for: the "before" state, the struggle the customer is in now.*
- **Angle:** high angle → weak, small, powerless — `[03]`
- **Framing:** wide shot + large negative space → lost, lonely, dwarfed, isolated — `[01]` `[11]`
- **Movement:** pull-out → disconnection, abandonment — `[06]`
- **Focus:** shallow focus isolating the subject → inner emotional state — `[04]`
- **Color/design:** desaturated / gray-on-gray palette → oppression, unease — `[24]`

### ❤️ Intimacy / Emotional Connection
*Use for: the human moment, the relationship, the close personal stakes.*
- **Shot size:** close-up / medium close-up → the "empathy machine," prioritizes feeling — `[01]` `[15]`
- **Framing:** over-the-shoulder, two-shot → shared moment, relationship — `[02]`
- **Focus:** shallow depth of field → intimacy, isolates the face — `[04]` `[25]`
- **Lens:** standard/normal 35–50mm → natural, "our own eyes" — `[07]`
- **Sound:** ambient mood bed + foley realism → subconscious closeness — `[21]`

### ⚡ Energy / Excitement / Momentum
*Use for: fast-paced product montages, "feel the buzz," hooks.*
- **Movement/rig:** handheld, whip pan, fast tracking → urgency, chaos, kinetic energy — `[06]` `[26]`
- **Editing:** cut-on-action/impact, cross-cutting, smash cut → force and drive — `[10]`
- **Transitions:** passing/pass-by, whip/swish pan, J-cuts → seamless momentum — `[09]`
- **Composition:** diagonal lines, filling the frame → off-tilt energy, sensory load — `[11]`
- **Frame rate:** speed ramps → punch and weight on key beats — `[08]`

### 🏆 Drama / Grandeur / "Hero Moment"
*Use for: the transformation reveal, the money shot.*
- **Frame rate:** slow motion (overcrank) → **amplifies whatever it shows** — single highest-leverage lever — `[08]`
- **Movement/rig:** crane/jib, drone → spectacle, scale, freedom — `[05]` `[06]`
- **Lighting:** low-key with strong key, volumetric light beams → cinematic drama — `[12]` `[13]`
- **Sound:** score swell + spot/design effects → epic emphasis — `[21]`

### 😨 Tension / Unease / Suspense
*Use for: the problem agitation, "don't let this happen to you," curiosity hooks.*
- **Angle:** Dutch/canted tilt → on-edge, mania (increase tilt as tension rises) — `[03]` `[11]`
- **Lighting:** low-key, hard light, underlighting, split lighting → mystery, menace — `[12]` `[13]`
- **Movement:** slow zoom, tracking-behind-subject, static "can't look away" hold → dread — `[06]`
- **Editing:** cross-cutting, withholding the eyeline reveal → sustained suspense — `[10]`
- **Sound:** rising strings + descending hum; cut background ~1200Hz so it creeps — `[21]`

### 🤯 Realization / The Turn / "Aha"
*Use for: the moment the offer clicks, before→after pivot.*
- **Dolly zoom (vertigo shot):** the dedicated lever for "something just changed" — `[16]`
- **Rack focus:** shifts attention without a cut → reveal — `[04]`
- **Match cut:** subconscious connection across time/space — `[09]`
- **Smash cut:** jolt of contrast — `[09]`

### 🔀 Comparison / Before-and-After
*Use for: the core ad structure — problem vs solution, them vs you.*
- **Split screen:** forces juxtaposition, parallel lives, disparity — `[17]`
- **Cross-cutting / superimposition:** parallel or comparison between two subjects — `[09]` `[10]`
- **Color arc:** palette evolves scene-to-scene to track the emotional shift — `[24]`
- **Match dissolve:** smooth, warm bridge between two states — `[09]`

### 😵 Disorientation / Distortion / Altered State
*Use for: stylized hooks, "your world feels off right now."*
- **Lens:** fisheye / extreme wide → warped, drugged perception — `[07]`
- **Rig:** Snorricam (body mount) → vertigo, panic, nausea — `[05]`
- **Focus:** split diopter, tilt-shift → impossible/unreal — `[04]`
- **Frame rate:** step printing → visceral, dreamy, disorienting — `[08]`
- **Camera roll:** disorientation, marks reversals — `[06]`

### Stacking cheat sheet (the meta-rule)
- To **empower** a subject → low angle + push-in + close-up + low-key key light + deep focus.
- To **diminish** a subject → high angle + wide shot + pull-out + negative space + cool palette + telephoto.
- To **unsettle** → Dutch tilt + slow zoom + split diopter + underlight + rising-string sound bed.
- To **warm/connect** → eye level + close-up + soft golden light + standard lens + ambient sound bed + clean dialogue.

**Sound is the most underrated lever** (`[21]` `[22]`): it "hits a more primitive part of the brain than images," which is why it carries horror and emotion. In ad work, the mood bed + score does more emotional work than any single visual choice — budget time for it.

---

# SOURCE INDEX

| # | File | Covers | Strongest emotion levers |
|---|------|--------|---------------------------|
| 01 | `01_Ep01_Camera_Shots_Shot_Sizes.txt` | Shot sizes (wide→extreme close-up) | isolation, empathy, confidence |
| 02 | `02_Ep02_Camera_Framing_Composition.txt` | Singles, two-shots, OTS, POV | relationship, isolation, inclusion |
| 03 | `03_Ep03_Camera_Angles.txt` | Angle & height | power, vulnerability, unease |
| 04 | `04_Ep04_Depth_of_Field_Focus.txt` | DoF, rack/soft focus, diopter | intimacy, isolation, reveal, shock |
| 05 | `05_Ep05_Camera_Gear_Rigs.txt` | Handheld, dolly, crane, Snorricam | intensity, immersion, vertigo |
| 06 | `06_Ep06_Camera_Movement.txt` | Push/pull, pan, tilt, zoom, tracking | tension, disconnection, dread |
| 07 | `07_Ep07_Camera_Lenses.txt` | Wide→telephoto, fisheye, macro | distortion, voyeurism, naturalism |
| 08 | `08_Ep08_Frame_Rate.txt` | Slow-mo, ramps, step printing | drama amplification, energy |
| 09 | `09_Ep09_Scene_Transitions.txt` | Cuts, fades, match cuts, wipes | connection, shock, momentum |
| 10 | `10_Ep10_Editing_Techniques.txt` | Cross-cut, eyeline, montage, cut-on-action | suspense, parallel tension, force |
| 11 | `11_Ep11_Composition_and_Framing.txt` | Thirds, lines, negative space, balance | isolation, calm, energy, unease |
| 12 | `12_Ep12_Cinematic_Lighting.txt` | High/low-key, hard/soft, three-point | mood baseline (happy↔tense) |
| 13 | `13_Cinematic_Lighting_Pt2.txt` | Portrait setups, color temp, volumetric | drama, intimacy, mystery |
| 14 | `14_Ep14_History_of_Animation.txt` | Animation history, on ones/twos | (mostly craft/context) |
| 15 | `15_Closeup_Shots.txt` | Close-up craft, aspect ratio, lens on faces | intensity, claustrophobia, arc |
| 16 | `16_Dolly_Zoom.txt` | The vertigo / Hitchcock shot | realization, paranoia, vertigo |
| 17 | `17_Split_Screen.txt` | Split screen & diopter | comparison, omnipresence |
| 18 | `18_Tracking_Shot.txt` | Dolly/Steadicam/handheld tracking | immersion, control, urgency |
| 19 | `19_Science_of_Sound.txt` | Sound capture fundamentals | (technical; "never bad sound") |
| 20 | `20_12_Principles_of_Animation.txt` | Disney's 12 principles | lifelike, weighted, appealing motion |
| 21 | `21_Post_Production_Sound.txt` | Score, foley, mix, envelope | **primary emotional driver** |
| 22 | `22_Recording_Sound.txt` | Mics, room tone, reverb control | immersion, intimacy, scale |
| 23 | `23_Shot_Lists_in_StudioBinder.txt` | Shot-list workflow | (pre-production method) |
| 24 | `24_Production_Design.txt` | Color, set decoration, location | mood, character psychology |
| 25 | `25_Cameras_Common_Mistake.txt` | Sensor size myth, the cinematic look | intimacy via shallow DoF |
| 26 | `26_How_Camera_Rigs_Shape_Movies.txt` | Rig choice = feeling | energy, control, realism |
| 27 | `27_Subtitles.txt` | Subtitle craft & creative use | readability, tone, comedy |

---

*Extracted from source-grounded sub-agent analysis of all 27 transcriptions, 2026-05-31. Update this file as new transcriptions are added or as pipeline-specific recipes are validated against ad performance.*
