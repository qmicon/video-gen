# video-gen — AI video production pipeline (Sell-By Date series)

Pipeline: script → shot list → **storyboard** → **Seedance 2.0 video**, in ≤15s chunks.

## Canon documents (read the one for your step BEFORE writing any prompt)

| Step | Canon |
|---|---|
| Shot lists + QA | `Sell-By Date/10_Ep1_Shot_List.md` + `shotlist transcriptions/SHOTLIST_QA_CHECKLIST.md` |
| Storyboards / beat boards | `STORYBOARD_BLUEPRINT.md` |
| Video prompts (Seedance 2.0) | `SEEDANCE_2_PROMPTING_BLUEPRINT.md` |
| Image-model mechanics (gpt-image-2) | `GPT_IMAGE_2_PROMPTING_GUIDE.md` |

`storyboard.md` (root) is legacy — superseded by `STORYBOARD_BLUEPRINT.md` where they
conflict.

## MANDATORY: the scene-state contract

**Before writing ANY Ep1 storyboard or video prompt:** read
`Sell-By Date/EP1_SCENE_STATE.md` and **paste its lock blocks verbatim** (geography, state
ledger, registers). Never re-derive screen geometry, prop states, or who-holds-what — that
file holds the answers; re-derivation is how sides flip and swords change hands.

**After EVERY approved generation (board or video):** update `EP1_SCENE_STATE.md` — the
state ledger (sword/grip/blood/props), the produced-chunk ledger, the asset registry, and
any new lock the chunk established. A stale state file silently corrupts every later prompt.

When spawning subagents for prompt work, include both halves of this contract in their
instructions — subagents do not inherit this file automatically unless they work in this
directory.

## Hard project locks (apply everywhere, no exceptions)

- Aspect: **4:3 horizontal** (1440×1080) — never 16:9/9:16/3:4.
- English prompts, the team's house format (header fields + Shot Breakdown; see worked
  example `Sell-By Date/12_Ep1_Seedance_Video1_Shots1-5.md`).
- Storyboards: numberless panels, 4:3 cells, board approved BEFORE video.
- Anti-plastic: the 1975/Arriflex/Kodak physical-reality block + directional light in every
  board and video prompt; "ultra-realistic/professional" are banned polish words.
- Comedy lives in the performance, never the filmmaking — camera and grade stay dead serious.
- On-screen text is composited in post; prompts forbid generated text (the VAGE can label is
  the only exception).
