# PRODUCT — "VAGE" Energy Drink (Ep1 "Cold Call" hero product)

The modern product Drew accidentally sells to the battlefield Commander (script L29–60). Like a
character sheet locks a face and the battlefield sheet locks a place, this sheet locks the **prop**
so the can looks identical in every Seedance shot — Drew gripping it in the mud, the Commander
ripping it from his hand and chugging it, the case he grabs in the loft.

---

## 1. The name — **VAGE**

**VAGE** — the agency's own house energy drink. The in-show joke: ViralAds**GE**n (V-A-G-E) names a
can after itself and dumps it into history.

- **Pronounced to rhyme with "RAGE."** Reads instantly as the energetic core of **ra·VAGE** /
  **RAGE** — a battle word a warlord understands without translation. Perfect for the first customer
  being a bloodied medieval commander.
- **Catchy + meta:** it's literally the brand's acronym, so it doubles as a sight gag for anyone who
  clocks "ViralAdsGen → VAGE," and works as a real-feeling energy-drink name for everyone who doesn't.
- **Tagline options:** *"UNLEASH THE VAGE."* / *"GO BERSERK."* / *"PURE VAGE."*

## 2. Brand mark + can design language (locked)

**Brand logo (provided):** a rounded-square badge in **electric cyan (#1AF0FF aqua)** with a solid
**black lightning bolt** angled across it. The bolt is the hero glyph and the cyan is the single
accent color — deliberately *hyper-electric*, so the can clashes maximally with the muddy medieval
battlefield (nothing in the 1300s is glowing aqua).

| Element | Lock |
|---|---|
| Format | 473 ml (16 oz) sleek aluminium can |
| Body | **matte black**, soft-touch, beaded with cold condensation |
| Accent | a single **electric cyan / aqua** — no red, no gold, no second hue |
| Brand mark | the **provided VAGE logo (Image 1)** — cyan rounded-square badge with a solid black lightning bolt — **reproduced exactly** (shape, proportions, colour) and centred large on the front face. Do **not** redesign or recolour it. |
| Optional bolt-only | if you'd rather the bolt sit on the bare matte-black body without the square, extract **only the bolt** from Image 1 and render it in glowing electric cyan, keeping its exact silhouette from Image 1 |
| Wordmark | **VAGE** — heavy condensed *italic* uppercase sans, electric cyan, slightly distressed/eroded edges |
| Subline | thin white **"BERSERKER ENERGY"** under the wordmark |
| Side strip | thin cyan vertical band reading **"ENERGY · FOCUS · FURY"** in small black caps |
| Top / base | brushed matte-silver lid, pull-tab, and base rim |

**Identity anchors (re-paste into every prompt):** the VAGE logo from Image 1 reproduced exactly;
matte-black body + single electric-cyan accent; "VAGE" heavy condensed italic cyan wordmark;
"BERSERKER ENERGY" subline; brushed-silver top.

---

## 3. GPT Image 2.0 prompt — PROP REFERENCE SHEET (primary, feed to Seedance)

*This is an **edit / image-reference** prompt: you supply the **VAGE logo PNG as Image 1**, and the
model reproduces that exact mark on the can rather than inventing a bolt. Same sheet discipline as a
character sheet — ~5 cells (front / 3-4 / side / plain back / emblem crop), no detailed rear nutrition
panel. Written to OpenAI's `gpt-image-2` guide: input referenced by index, "reproduce exactly / change
only the can", text spelled letter-by-letter, exclusions inline.*

> **How to run it:** `images.edit` (ChatGPT: "edit / attach image"), `model gpt-image-2`,
> `image=[VAGE_logo.png]`, `size="1536x1024"` (HD landscape), `quality="high"`, `input_fidelity` is
> auto-high on gpt-image-2. The logo is **content** to copy, not a background to keep — the prompt says
> so explicitly. The `Aspect ratio` line is a soft hint; `size` is the real control.

```
Image 1 = the VAGE brand logo: a rounded-corner square in electric cyan (aqua) containing a solid
black lightning bolt. Treat Image 1 as the brand mark to PLACE on the product, not as a background.

Task: create a photorealistic PRODUCT-REFERENCE SHEET of an energy-drink can that carries the logo
from Image 1. This is a clean design/reference document for a 3D and video pipeline, NOT an
advertisement. One composite image on a flat light-grey studio background, even diffuse studio light.
The same can is shown several times.

LAYOUT (tidy grid):
- Top row: the same can in FRONT view, 3/4 view, and SIDE profile — standing upright, identical
  height, evenly spaced.
- Bottom row: a plain BACK view (mostly blank matte black, no nutrition panel, no paragraphs of text)
  and one CLOSE-UP crop of the front logo + wordmark.
- Small plain labels under each cell: "FRONT", "3/4", "SIDE", "BACK".

THE CAN: a 473 ml sleek aluminium can, matte black soft-touch body, a single ELECTRIC CYAN (aqua)
accent. On the FRONT face, centered and large, reproduce the VAGE logo from Image 1 EXACTLY — same
lightning-bolt silhouette, same proportions, same cyan — as the hero brand mark. Do not redesign,
recolour, restyle, or add detail to the logo; keep it identical to Image 1, only conformed to the
curve of the can.

TEXT on the can (render exactly, spelled letter by letter):
- Wordmark below the logo: "VAGE" (V-A-G-E) — heavy condensed ITALIC uppercase sans-serif, electric
  cyan, slightly distressed edges.
- Small white line under the wordmark: "BERSERKER ENERGY".
- Thin cyan vertical stripe up the right side: "ENERGY · FOCUS · FURY" in small white caps.
Render no other text or lettering anywhere.

MATERIALS: brushed matte-silver lid, pull-tab and base rim; fine cold condensation droplets across the
matte black surface; accurate matte-black vs brushed-metal materials.

STYLE: flat even studio light, neutral light-grey seamless background, sharp focus, photorealistic, no
environmental shadows, no mood lighting, no scene.

CHANGE vs PRESERVE: the only thing you are designing is the can and its layout. Keep the VAGE logo
identical to Image 1. Do not invent any alternative logo.

CONSTRAINTS — do not include: any background scenery or props, hands or people, dramatic/coloured/rim
lighting, smoke, lens flare, room reflections, multiple different cans, any red or gold or extra accent
colour, a detailed nutrition-facts panel, watermarks, any logo other than the VAGE mark from Image 1,
gibberish or placeholder text, dented or crushed can.

Aspect ratio: 3:2 landscape, 1536×1024.
```

**Bolt-only variant:** if you want the bolt to sit on the bare black body without the cyan square,
swap the "THE CAN" front-face line for: *"…reproduce ONLY the lightning bolt from Image 1 (its exact
silhouette), enlarged and rendered in glowing electric cyan, centered on the front — drop the square
background of the logo."*

## 4. GPT Image 2.0 prompt — HERO / END-CARD SHOT (optional glamour)

*For the cold-open beauty frame or the 1:20 brand button. Best run as an **edit** once the §3 sheet is
approved: supply the approved FRONT-view can render as **Image 1** so the logo + layout are already
correct and you're only relighting it. 9:16 vertical (1024×1536).*

```
Image 1 = the approved VAGE can (front view). Keep the can, its VAGE logo, wordmark and layout
EXACTLY as in Image 1 — do not redesign the logo, label, text, colours or proportions. Change only the
scene and lighting around it.

Re-stage Image 1 as a single dramatic hero product shot: the same can stands upright on a wet
reflective black floor, lit by a hard low key-light with a deep electric-cyan rim-glow behind it, dense
black background, faint drifting smoke, a few water droplets flicking off the surface caught mid-air.
Cinematic high-contrast energy-drink advertising photography, 85mm, shallow depth of field,
photorealistic.

Keep all text from Image 1 verbatim ("VAGE", "BERSERKER ENERGY", "ENERGY · FOCUS · FURY"); add no new
text. No people, no hands, no watermark, no accent colour beyond electric cyan and silver.

Aspect ratio: 9:16 vertical, 1024×1536.
```

*(If you don't yet have an approved can render, you can run this from the logo instead — set Image 1 to
the VAGE logo and paste the full "THE CAN" + "TEXT" blocks from §3 so the can gets built here.)*

---

## 5. Continuity note

Once the prop sheet renders and is approved, pass it to Seedance 2.0 as a **reference image on every
shot the can appears in** (cold-open grip, the Commander's chug, the case in the loft) and re-paste
the §2 identity anchors into each shot prompt — same contract as a character or location sheet.
The electric-cyan glow is the visual gag: a smear of impossible neon in a muddy 1960s-war-epic frame.
