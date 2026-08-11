# Dataceler / Sansão mascot reference

## Primary sources

- Website: `https://dataceler.com.br`
- Official symbol asset: `https://dataceler.com.br/logo-dataceler.png`
- The official asset is a square transparent PNG containing only the geometric mark, with no wordmark.

## Verified palette

Extracted from the official site CSS:

- Charcoal: `#111111`
- Matte bronze/gold: `#B8956A`
- Pale gold/sand: `#E8C99A`
- Dark bronze: `#8A6A42`
- Off-white may be used as a supporting neutral around `#F4F1EA`

For a friendly character, use pale sand/off-white as the dominant body color, charcoal for the background and facial details, and bronze as a restrained brand accent. A bronze-dominant body became visually heavy.

## Durable user direction

The bot remains named **Sansão**, but the user does not want an animal identity.

Target:

- original abstract mascot;
- cute, friendly pocket-virtual-pet energy;
- simple, rounded, memorable silhouette;
- warm expressive eyes with visible highlights;
- small gentle smile;
- adult-quality brand execution rather than a childish illustration;
- readable as a Telegram/Discord avatar;
- official Dataceler mark integrated as a small chest emblem.

Avoid:

- lions or any other recognizable animal;
- cowboy/peão, rustic, sertanejo, or heroic-animal associations;
- mascot work that feels “brega”: ornamental metallic surfaces, gamer lighting, literal circuitry, excessive detail, crowns, armor, or generic tech clichés;
- dark void faces, empty glowing eyes, angular threatening forms, cocoon/monk silhouettes, or anything frightening;
- a pure abstract logo with no expression—the user asked for a mascot, not only a symbol;
- direct copying of Tamagotchi characters or hardware. Use only the general emotional language of a classic friendly virtual pet.

## Iteration lessons

1. A technological lion was rejected as culturally and aesthetically distant.
2. A non-animal geometric symbol was too impersonal.
3. A dark abstract core with orbital bronze parts read as frightening.
4. A pale rounded virtual-pet character with dark glossy eyes, tiny smile, bronze cheeks, and small limbs achieved the intended friendliness.
5. Replacing the placeholder chest circuit with the official Dataceler mark materially improved brand specificity.

## Logo integration technique

When image-to-image editing is unavailable, the logo can be composited deterministically:

1. Download the official transparent logo.
2. Remove the generated placeholder emblem using inpainting or smooth local gradient reconstruction.
3. Crop the logo to its alpha bounding box.
4. Recolor it to matte bronze.
5. Add a restrained dark depth layer and soft shadow matching the mascot’s 2.5D finish.
6. Center it on the chest at a size that remains recognizable in a small avatar.
7. Visually verify that the placeholder is gone and no halo, seam, or distortion remains.

Do not use the full wordmark at avatar scale.
