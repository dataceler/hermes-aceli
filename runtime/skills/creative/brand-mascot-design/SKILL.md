---
name: brand-mascot-design
description: Design and iteratively refine original brand mascots and profile avatars, from brand-source discovery through thumbnail verification and logo integration.
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [branding, mascot, avatar, image-generation, visual-identity]
---

# Brand Mascot Design

Use this skill when creating or revising a mascot, bot avatar, profile image, character icon, or branded visual identity. Treat mascot work as identity design, not merely prompt writing.

## References

- `references/dataceler-sansao.md` — Dataceler/Sansão palette, logo sources, user corrections, and accepted direction.

## Core distinction

Establish which artifact the user actually wants before generating:

- **Symbol:** abstract mark with no personality.
- **Mascot:** recognizable character with personality and expression.
- **Portrait/avatar:** face-led identity, human or non-human.
- **Abstract mascot:** nonliteral character with a readable personality; it must be more than a logo but need not resemble an animal, human, or robot.

Never silently convert “mascot” into an animal. Ask or infer from explicit feedback whether the character should be animal, human, robot, object, or abstract.

## Workflow

### 1. Discover the brand from primary sources

Prefer official sources: website, brand guide, logo asset, social profile, or user-provided files. Extract:

- dominant, secondary, and accent colors;
- logo geometry and line language;
- typography character;
- brand adjectives;
- visual anti-goals.

Do not infer a palette from unreliable search snippets. If a site blocks browser rendering, retrieve its HTML/CSS and count recurring color tokens, then inspect the official logo image separately.

### 2. Lock the visual brief before generation

State a compact brief containing:

- artifact type;
- three desired adjectives;
- three anti-goals;
- representational category;
- intended crop and smallest display size;
- whether the official logo must appear literally or only inspire geometry.

When prior feedback contains frustration (“brega”, “assustador”, “parece X”), translate it into concrete constraints rather than merely changing nouns.

Examples:

- “Brega” may mean excessive chrome, ornamental detail, literal symbolism, gamer lighting, or generic 3D mascot treatment.
- “Scary” may mean a dark void face, glowing empty eyes, hard angular silhouette, or insufficiently warm expression.
- “Cute” should map to rounded massing, large eyes with highlights, a small mouth, light-dominant face/body, and simple proportions—not to childish clutter.

### 3. Generate by direction, not random variation

For uncertain briefs, produce two or three clearly different directions with labels. Do not generate three minor prompt variations.

For an abstract mascot, useful direction families include:

1. modular virtual pet;
2. soft geometric being;
3. expressive object/entity;
4. floating core with readable face.

Avoid copyrighted character replication. “Tamagotchi-like” means the emotional simplicity of a classic pocket virtual pet, not copying an existing creature or device.

### 4. Control color proportion

A brand palette does not require every color to dominate equally. For friendly mascots:

- use the lightest brand tone for the primary body or face;
- reserve the darkest tone for background and facial details;
- use the corporate accent on small identity-bearing modules;
- avoid large metallic surfaces unless the brand explicitly calls for them.

This prevents warm bronze or gold palettes from becoming heavy, rustic, gamer-like, or threatening.

### 5. Verify visually before delivery

Inspect the generated image and reject it when it violates the brief. Check:

- immediate emotional read at first glance;
- accidental resemblance to an animal, person, robot, ghost, cocoon, monk, toy, or unrelated cultural archetype;
- expression and eye highlights;
- silhouette at 24–32 px;
- centered circular-crop safety;
- absence of unwanted text, letters, crowns, armor, circuits, neon, or visual clutter;
- brand color balance;
- whether it feels ownable rather than stock.

A technically successful generation is not a successful mascot. Regenerate when the first-glance read is wrong.

### 6. Integrate an official logo carefully

Use an official transparent asset. Do not redraw the mark from memory. At avatar scale, prefer the icon over a full wordmark.

Integration options:

- generate a clean badge area and composite the official mark;
- remove a placeholder emblem with inpainting, then apply the mark;
- for smooth surfaces, reconstruct the local gradient and overlay a recolored mark with restrained depth and shadow.

Verify that the old emblem is fully removed and that the official mark has no halo, rough crop, distortion, or unreadable detail.

### 7. Deliver a versioned artifact

Save the selected image locally in a stable cache or project path. Report:

- format and dimensions;
- intended use;
- what was verified;
- whether it is a final identity or a direction candidate.

Do not claim finality when the user is still choosing the visual direction.

## Prompt construction

A strong prompt should specify:

1. identity and role;
2. representational category;
3. emotion and personality;
4. silhouette and proportions;
5. exact palette and color hierarchy;
6. finish (flat, clay-like, vector, subtle 2.5D);
7. avatar constraints;
8. explicit anti-goals.

Negative constraints should target likely failure modes, not become an unbounded list.

## Iteration discipline

- Admit a failed aesthetic read directly.
- Explain the visual cause in one sentence.
- Change the design system, not just one object.
- Preserve approved traits while replacing rejected traits.
- Use humor only when the user signals it; never use humor to dodge the correction.

## Final checklist

- [ ] Primary brand source inspected
- [ ] Representational category explicit
- [ ] Desired emotional read explicit
- [ ] Anti-goals translated into visual constraints
- [ ] No unintended animal/human/robot resemblance
- [ ] Works at 24–32 px
- [ ] Safe circular crop
- [ ] Official logo used from source asset if requested
- [ ] Final file saved and visually verified
