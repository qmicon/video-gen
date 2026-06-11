# EP 1 — SEEDANCE VIDEO 1 "Arrival & Denial" (shots 1–5)

Production prompt per [SEEDANCE_2_PROMPTING_BLUEPRINT.md](../SEEDANCE_2_PROMPTING_BLUEPRINT.md)
§3. Edit targets (not in prompt): shot 1 ~3.0s · 2 ~3.0s · 3 ~2.5s · 4 ~1.2s · 5 ~4.0s ≈ 13.7s.
Ends on a hard cut mid-word (the grab opens Video 2).

## Generation settings (params, not prompt text)
Duration **14s** · Aspect **4:3 horizontal** · Resolution highest available · Mode **R2V**

## References to attach (upload in this order — order = priority)

| # | Asset | Source | Role |
|---|---|---|---|
| Image 1 | Drew **headshot crop** | cropped from `drew_muddied` sheet | facial identity |
| Image 2 | **`drew_muddied` character sheet** (full multi-view sheet) | as rendered | body, wardrobe, mud — framed in-prompt as "the SAME man, one person" |
| Image 3 | VAGE can front view | crop from product sheet render | prop exactness |
| Image 4 | Battlefield master frame | approved location render | scene + grade |
| Image 5 | Portal front view (on black) | portal asset sheet render | VFX design |
| Image 6 | **5-shot storyboard sheet** (approved) | this scene's storyboard | shot sequence + composition |

No audio refs this run — **this generation casts Drew's voice**: run 2–3 takes, pick the voice,
extract a 5–10s clean snippet as `drew_voice_anchor` for every later run.

If output is unstable (style conflict / subject confusion), drop Image 6 first and replace
with storyboard **panel 1 cropped alone** as "use as first frame".

## THE PROMPT (copy-paste — house format; Seedance UI @-mention syntax)

```
SUBJECT: DREW — facial features follow @Image1 (headshot). @Image2 is his character reference
sheet: it shows the SAME man, Drew, from multiple angles — one person, not several people. His
body, mud-caked white dress shirt, loosened dark tie, and mud coverage follow @Image2. Mid-40s
American ad man, dark hair. He is the only principal character; all soldiers are background
extras.
PROP: @Image3 — VAGE energy can, matte-black 473ml, electric-cyan lightning-bolt logo,
reproduced exactly. Stays clutched in Drew's hand in every shot where he appears.
ENVIRONMENT: @Image4 — medieval battlefield mid-battle. Burning banner on the ridge
LEFT, dense silver pike-wall of infantry RIGHT, hazy slope ahead, deep churned mud foreground;
bearings never flip. LIGHT SOURCE: bright overcast sky from above and slightly behind the
subjects — their backs to the sky, faces on the shadow side toward camera; low-key,
high-contrast, cool ~5600K daylight diffused by smoke, volumetric beams breaking through,
real specular highlights on polished armor.
VFX ASSET: @Image5 — the portal: a FLAT vertical disc of acid-green energy, ragged
splattered rim, bright near-white-green swirling core, standing at ground level. A flat
planar disc, never a tunnel or hole. Casts green spill light.
STORYBOARD: @Image6 — shot order and composition reference only; its five panels show
the SAME man, Drew, at five moments — not five different people.
MOOD: Drugged, disoriented arrival; whiplash denial rising to panic; ends cut off mid-word.
MUSIC: None — the battle bed is the soundtrack.
STYLE: Gritty live-action cinema footage shot on 35mm motion-picture film. Candid, documentary.
COLOR LOGIC: 1960s-70s European War Epic Look — muted faded color, low saturation, fine
grain, soft naturalistic focus, rich light-and-shadow layers. No golden hour, no HDR, no
clean modern render look.
LOGIC RULE: Keep logical consistency in Drew's identity, mud state, the can in his hand, the
battlefield bearings, and action continuity across all shots. Fisheye distortion exists only
in Shot 1.

Shot Breakdown

SHOT 1: MS, 14mm fisheye ground-level handheld / The green portal disc from @Image5 rips open and Drew
tumbles out, face-planting into deep mud, one fist holding the can clear of the muck, green
glow spilling across the wet mud and his back — a brief violent beat / SFX: deep whoosh, heavy
wet mud slap, battle roar swelling in.
SHOT 2: EST WS, 20mm crane slowly descending / Hard cut into the full melee matching @Image4 — clashing steel,
burning banner LEFT, horses, pike-wall RIGHT, smoke columns, fighting layered front to back;
Drew small in the near-foreground mud, just pushing himself up, can still in his fist — an
unhurried reveal of scale / SFX: clashing steel, distant hooves, fire crackle, men shouting.
SHOT 3: FS, 28mm handheld / Cut on action into Drew scrambling to his feet and turning in a
circle, arms half-raised, can gripped in one hand; eyes wide and darting, mouth slack, breath
fast and visible — refusing to believe it; soldiers fight at depth around him / SFX: wet
squelching footsteps, panicked breathing close, battle bed continues.
SHOT 4: POV WS, 24mm rapid whip pan / Whip into Drew's own point of view — the battlefield
smears with horizontal motion blur, a passing horse, clashing soldiers, smoke streaking,
horizon slightly tilted; Drew NOT in frame — a quick disorienting flash / SFX: hooves rushing
past, whipping wind, steel ringing.
SHOT 5: MCU dirty single, 50mm shallow / Cut into Drew slightly off-center, a blurred
soldier's shoulder edging the frame; one muddy hand raised in protest, the other clutching
the can at chest height, clearly visible; battle a soft out-of-focus chaos behind him.
DIALOGUE (fast, panicked, cracking — dry American male voice, mid-40s): {This is a set. This
is a movie set — somebody yell cut. Where's the—} — the line cuts off abruptly mid-word and
the video ends on that instant, his mouth still open / SFX: his voice close and dry, battle
muffled behind.

STYLE NOTE: Live-action footage shot on an Arriflex 35BL, 50mm at T2.8, Kodak 35mm color
negative — organic film grain, halation around the bright sky, soft focus falloff at frame
edges. Candid, documentary, imperfect. Real skin with visible pores, sweat and grime in the
creases; real fabric weave, real mud, real fire and smoke. No 3D render, no CGI, no animation,
no beauty-filter look, no skin smoothing, no plastic or waxy skin, no AI smoothing artifacts.

CONSTRAINTS: Avoid jitter, bent limbs, temporal flicker, identity drift. Drew appears once
per shot only — no duplicate copies of him, and never two Drews in the same frame. Faces stable without deformation; movement
continuous and natural, no stutter or flicker. No modern objects except the can and Drew's
clothing. No music. No subtitles. No on-screen text except the VAGE label on the can itself.
```

## QA after render
Bearings hold (banner L / pike-wall R) · one Drew only (no twins from Image 6) · can in hand
shots 1,2,3,5 · portal = flat green disc · line cut off mid-word at the end · grade matches
Image 4 across all five shots · no captions/subtitles burned in.
