# SELL-BY DATE — Script QA Checklist

Every script runs through these gates **before it's called locked**. Each item exists because it was a real mistake in the Episode 1 session that had to be hand-fixed. Pair this with `07_Dialogue_Blueprint.md` and `08_OnScreen_Text_Blueprint.md` (the detailed specs); this is the pass/fail gate.

---

## Gate 0 — Setup (before writing a word)
- [ ] **Read the repo guides first.** `screenwriter-skill/`, `../hooks.md`, `../formats.md`, `../spec-screenplay.md`, the StudioBinder transcriptions, and both blueprints. *(Mistake: worked freeform and ignored the existing frameworks until told.)*
- [ ] **Right format for the medium.** Short-form vertical = `spec-screenplay.md` format (header block, camera-blind), NOT a Hollywood feature screenplay. *(Mistake: wrote Hollywood format.)*
- [ ] **Genre, tonal register, and duration confirmed with the user.** *(Mistake: drifted thriller → comedy, then dry → big comedy.)*
- [ ] **Don't import conventions that don't fit.** Short-form needs no "pilot"; every episode is self-contained. *(Mistake: forced a pilot.)*

## Gate 1 — Structure
- [ ] Self-contained: a cold viewer gets it with no prior episode.
- [ ] Beats connect by **but / therefore**, never "and then."
- [ ] The scene **turns** (a value shifts).

## Gate 2 — Hook (first 0.4s, per `hooks.md`)
- [ ] First frame = **body in motion / extreme face / visible incongruity / reaction-to-impact.** Never a static establishing shot or an object. *(Mistake: opened on "a glowing tear hangs in the air" and a "FINAL NOTICE" sticker.)*
- [ ] Passes the **mute test**.
- [ ] Opens a loop still unresolved at second 6.

## Gate 3 — On-screen text (per `08`)
- [ ] ≤14 words, lands in 3s, stacks ≥2 triggers.
- [ ] **Completes the visual — never labels it.** *(Mistake: "Drew's first sales call.")*
- [ ] Contains **one concrete number** (the "$20K" move). *(Mistake: vague rewards.)*
- [ ] Not corny/clunky. *(Mistake: "meet the sun god.")*
- [ ] 3 variants written for A/B.

## Gate 4 — Dialogue (per `07`) — the one that broke most
- [ ] **Picturable / concrete.** Ban abstractions. *(Mistake: "we disappear," "that's a market.")*
- [ ] **Literal, never a riddle** — no pun-as-logic. *(Mistake: "that hand was wearing 1684," "that's a warrant.")*
- [ ] **No line assumes a premise the audience doesn't have yet.** *(Mistake: "no ad blockers" three lines in.)*
- [ ] **No recycled construction.** *(Mistake: "that's not a problem, that's a ___" used ~4×.)*
- [ ] **Smart-character exposition via the "English, Doc!" device** (real jargon → "English" → specific plain line) — not fake jargon. *(Mistake: "paradox index.")*
- [ ] **Realizations/pitches are fragmented exchanges with reactions + concrete margin** — never a tidy monologue/thesis. *(Mistake: "four thousand years of rich people back there.")*
- [ ] Every character in their **locked voice** (Drew / Kai / Margo / period guests).
- [ ] **Comedy from character + situation + spectacle**, not dry quips; matches the established register. *(Mistake: drifted into dry office/corporate deadpan; user preferred the big period/fish-out-of-water comedy.)*
- [ ] **Read every line aloud** — if it sounds written, rewrite. *(Mistake: "no one speaks like this.")*
- [ ] **Grounded in real reference cadence**, not improvised voice. *(Mistake: had to be told to search references repeatedly.)*

## Gate 5 — Logic & continuity
- [ ] **Characters only know what they witnessed.** *(Mistake: Margo "knew" the warlord was dead though she never saw it.)*
- [ ] **Physical/spatial state tracks.** *(Mistake: "Margo steps in front of the tear" — but the tear was already closed; reopening needs the control/rig.)*
- [ ] **Reactions fit the actual stimulus.** *(Mistake: "What is that?" to a bloodied man, instead of "What the hell happened?")*
- [ ] Prop/action cause-and-effect stays consistent across the scene.

## Gate 6 — Platform safety
- [ ] Profanity / graphic content flagged for Meta/TikTok suppression, with a clean-cut option provided. *(Flag: "What the fuck.")*

## Gate 7 — Lock
- [ ] **Never declare "final" or save-as-locked without explicit user sign-off.** *(Mistake: presented a "final" version and moved to save before the user had locked it.)*

---

## Appendix — the Episode 1 iteration log (what this checklist prevents)
1. Ignored the repo's frameworks (skill, transcriptions, hooks/formats/spec) until prompted — twice.
2. Wrote in Hollywood feature format instead of the short-form spec format.
3. Fired multi-option question menus instead of one narrow binary (violating the screenwriter rule).
4. Dialogue read "very AI" — generic, ungrounded.
5. Wrong comedy register — dry office/Better-Off-Ted deadpan; user wanted big period fish-out-of-water comedy ("the Louis script was better," "it's not funny").
6. Riddle/nonsense lines: "that hand was wearing 1684," "no ad blockers," "that's a warrant."
7. Recycled the "that's not a problem, that's a ___" construction repeatedly.
8. Vague consequence ("we disappear") and fake jargon ("paradox index") — fixed with the "English, Doc!" device + specificity ("we were never born").
9. Tidy thesis monologue ("four thousand years of rich people") — fixed to a fragmented margin exchange ("$200 of cans → $20K in gold").
10. Weak hook (static first frame) and label-style on-screen text ("Drew's first sales call").
11. Continuity breaks — Margo knowing an off-screen death; standing in front of a closed tear.
12. Reaction mismatch — "What is that?" vs "What the hell happened?" + "Close it!"
13. Tried to present/save a "final" before it was locked.
14. Forced a TV "pilot" onto a short-form series.
15. Improvised dialogue/text instead of grounding in real references until told to search.
