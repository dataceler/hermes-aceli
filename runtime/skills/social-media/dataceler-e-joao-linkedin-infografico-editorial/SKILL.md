---
name: dataceler-e-joao-linkedin-infografico-editorial
description: Create sourced LinkedIn posts for João Cordeiro and Dataceler with deterministic, code-rendered single-image infographics.
version: 0.3.0
author: Hermes
metadata:
  hermes:
    tags: [LinkedIn, Infographic, Content, Founder-Led, B2B, Branding]
---

# Dataceler e João — LinkedIn com Infográfico

Create deep LinkedIn content from João Cordeiro's real expertise and Dataceler's official brand, paired with a deterministic single-image infographic. This skill does not govern Instagram carousels, automate posting, invent platform claims, or replace the author's voice.

## When to Use

- “Crie um post de LinkedIn com infográfico para João Cordeiro.”
- “Transforme esta pesquisa em um infográfico de uma imagem para a Dataceler.”
- “Quero gerar autoridade e conversas B2B no LinkedIn.”
- “Analise nossa marca antes de criar o infográfico.”
- “Esse post parece genérico, raso ou comercial demais.”
- “Refaça o conceito; ficou brega, frio ou fora da marca.”
- “Crie uma matriz, framework, processo, diagrama ou one-page para LinkedIn.”

Do not use this skill for Instagram or LinkedIn carousels. Use `dataceler-instagram-carousel-editorial` for carousel sequence, pagination, slide navigation, carousel CTA, and slide-level QA.

## Prerequisites

- Nome e função do executivo que assinará o conteúdo.
- ICP ou público que o conteúdo deve atrair.
- Um tema em que o executivo tenha experiência real.
- Ao menos uma fonte: URL, documento, entrevista, reunião ou notas.
- Objetivo: autoridade, educação, conversa, lead ou relacionamento.
- Para conteúdo da Dataceler: carregar `references/dataceler-editorial-profile.md` antes de redigir e aplicar suas regras de autor, público, tom, CTA e evidência.
- Para infográficos comparativos em retrato: carregar `references/portrait-comparison-matrix-rendering.md`.
- Para renderização: carregar `references/deterministic-infographic-rendering.md`; Python + Pillow e DejaVu Sans/Mono são obrigatórios.
- Para visuais: URL oficial da marca ou logotipo enviado pelo usuário.
- Para publicar: autorização explícita e uma integração separada com a plataforma; esta skill apenas pesquisa, cria e revisa.

## How to Run

Use `web_extract` or `read_file` to gather every named source, `web_search` to verify time-sensitive claims, and `vision_analyze` to inspect official brand assets. Every post must include an image; default to an infographic that compresses or clarifies the reasoning. Draft the content, create and inspect the visual, save the approved artifacts, and verify both before delivery.

Canonical sequence:

```text
sources → thesis → founder voice → visual format → draft → critique → revision → verified artifact
```

## Quick Reference

- Source URL: `web_extract(urls=["URL"])`
- Current claim: `web_search(query="CLAIM + official source")`
- Local source: `read_file(path="PATH")`
- Brand files: `search_files(pattern="*brand*", target="files", path="PATH")`
- Logo analysis: `vision_analyze(image_url="URL_OR_PATH", question="...")`
- Deterministic renderer: Python + Pillow with DejaVu Sans and DejaVu Sans Mono
- Save artifact: `write_file(path="APPROVED_PATH", content="...")`
- Final text inspection: `read_file(path="APPROVED_TEXT_PATH")`
- Final image inspection: `vision_analyze(image_url="APPROVED_IMAGE_PATH", question="...")`
- Final LinkedIn infographic rendering: all text, shapes, matrices, arrows, colors, and logo placement must be coded deterministically.
- Portrait comparison matrices: `references/portrait-comparison-matrix-rendering.md`
- Keep format-specific learning scoped: single-image infographic rules stay here; carousel work belongs in `dataceler-instagram-carousel-editorial`.
- Primary format: one 1080 × 1350 PNG plus a complementary LinkedIn caption
- Primary signals: saves, substantive comments, shares, dwell time, qualified conversations

## Procedure

1. **Capture every source.**
   - Use `web_extract` for each URL and `read_file` for each named file.
   - When a YouTube transcript helper is blocked, try `web_extract` on the watch URL; do not use account cookies to evade an IP block.
   - Preserve requirements that follow a source, such as “focus on X” or “skip Y.”
   - Completion: every source and requirement is represented in working notes.

2. **Define the authority territory.**
   - Write one sentence for each axis: industry, executive expertise, ICP problem, defensible point of view, and business objective.
   - Prefer a narrow topic the author can discuss from experience over broad trend commentary.
   - Completion: the proposed topic belongs credibly to the author and matters to the ICP.

3. **Choose the publishing identity.**
   - Default to João Cordeiro's profile for founder-led content; use the company page as support, archive, proof, or redistribution.
   - Do not present personal experience as if spoken by an institution.
   - Completion: the author, account, audience, and CTA owner are explicit.

4. **Build a specific thesis.**
   - Extract evidence, tension, mechanism, consequence, and recommended action from the sources.
   - Treat algorithm names, reach multipliers, format shares, and similar figures as source claims until verified with `web_search` against current first-party material.
   - Remove unsupported numbers rather than laundering them through confident prose.
   - Completion: one debatable, useful thesis is backed by attributable evidence.

5. **Build a saveable single-image argument.**
   - Every LinkedIn post governed by this skill must include one infographic, not a decorative illustration or carousel.
   - Give the infographic a real information structure: comparison, matrix, process, framework, diagram, evidence map, or decision model.
   - Use plain text as the caption that develops the visual, never as the only deliverable.
   - If the idea genuinely requires pagination or a slide sequence, stop and switch to `dataceler-instagram-carousel-editorial` instead of importing carousel rules here.
   - Completion: the single image teaches independently, the caption adds depth instead of repeating it, and the actual rendered PNG is available for review.

6. **Write in João Cordeiro's voice.**
   - Include concrete decisions, examples, trade-offs, observations, or mistakes supplied by the author.
   - Develop a mechanism, criteria, model, or consequence; a strong slogan without reasoning is not depth.
   - Use AI to structure and sharpen, not to replace lived experience.
   - Avoid generic openings, empty superlatives, fake vulnerability, engagement bait, and comments such as “ótimo post.”
   - Remove sales copy unless the user explicitly requests a commercial post; educational value comes before lead capture.
   - Completion: the draft could not be published unchanged by an unrelated executive and gives the reader a reusable idea.

7. **Align and verify the visual against the official brand.**
   - Inspect the official site and logo with `web_extract` and `vision_analyze`; extract palette, geometry, contrast, and tone instead of guessing.
   - For every LinkedIn infographic, render the final image deterministically with Python and Pillow, using DejaVu Sans and DejaVu Sans Mono. Position all text, shapes, matrices, arrows, colors, and logo placement in code. This is mandatory, not a fallback.
   - Do not use `image_generate` for LinkedIn infographics unless the user explicitly requests a generative illustrative asset. Even then, Pillow must compose the final piece, and generated imagery must never control typography, matrices, labels, arrows, colors, or logo placement.
   - For a 1080 × 1350 comparison with three or more options, load `references/portrait-comparison-matrix-rendering.md`; prefer stacked comparison bands over narrow columns when mobile legibility would suffer.
   - Add programmatic overflow guards, but do not treat them as visual QA. Open the real PNG and inspect gutters, dividers, callout bottoms, label-to-value spacing, and the longest title/subtitle combination.
   - Inspect the rendered image at profile/feed size with `vision_analyze`; check spelling, clipping, overlap, contrast, axis direction, low/high mapping, and logo proportions.
   - If feedback rejects the concept itself—“brega,” “assustador,” “genérico”—change visual territory instead of polishing the rejected object.
   - Completion: the final image, not just its source or dimensions, is legible, branded, relevant to the thesis, and approved in direction.

8. **Design for depth, not vanity.**
   - Give the reader a reason to pause, expand, save, share privately, or write a substantive response.
   - Keep outbound links out of the body when reach is the priority unless current evidence or campaign needs justify them; place the destination in a follow-up path instead.
   - Use a CTA that advances the business objective without pretending every post must go viral.
   - Completion: the intended reader action and its business value are explicit.

9. **Run a critique loop.**
   - Ask for judgment on thesis, voice, usefulness, visual direction, and commercial fit—not just “gostou?”.
   - Translate blunt feedback into a concrete design or editorial constraint.
   - Preserve approved elements and change only what feedback invalidated.
   - Completion: no unresolved rejection remains hidden behind cosmetic edits.

10. **Save and measure.**
    - Use `write_file` only after the output path and final direction are approved.
    - Track performance beyond the first hour: saves, substantive comments, shares, qualified profile visits, DMs, leads, and sales-cycle effects.
    - Compare posts by topic, format, author, and CTA; do not optimize only for likes.
    - Completion: the artifact is readable from disk and the measurement window is defined.

## Pitfalls

- **Treating a creator's algorithm analysis as platform documentation.** Attribute it and verify time-sensitive claims.
- **Using the company page as the only organic voice.** Founder-led content needs an accountable human perspective.
- **Publishing generic AI prose.** Specific experience, mechanisms, and trade-offs are the antidote.
- **Chasing first-hour engagement.** Valuable B2B content may compound over several days.
- **Optimizing for likes.** Saves, meaningful comments, shares, DMs, and qualified leads better reflect depth.
- **Publishing without an image.** Every post needs a visual; default to an infographic that teaches independently.
- **Writing sales copy instead of analysis.** Build a mechanism, criteria, or framework before adding any CTA.
- **Adding a visual that merely decorates.** The visual must compress or clarify knowledge.
- **Forcing a three-column matrix into portrait.** Use stacked comparison bands with repeated criteria when narrow columns would create small type or four-line cells.
- **Trusting overflow checks as QA.** Programmatic guards catch known limits, not optical collisions; inspect the PNG for titles crossing dividers, labels touching values, and final callouts clipped near the footer.
- **Mixing format-specific skills.** Keep single-image infographic techniques in this skill and carousel-only sequence, pagination, navigation, and correction rules in `dataceler-instagram-carousel-editorial`.
- **Guessing brand colors.** Inspect official assets first.
- **Refining a rejected concept.** When the direction is wrong, pivot the concept.
- **Using cookies to bypass YouTube blocking.** Cloud IP blocking is not consent to risk an account ban.
- **Posting without authorization.** Drafting permission is not publishing permission.

## Verification

Use `read_file(path="APPROVED_TEXT_PATH")` to inspect the final caption and `vision_analyze(image_url="APPROVED_IMAGE_PATH", question="Check spelling, clipping, hierarchy, contrast, margins, positional meaning, logo proportions, and mobile feed-size legibility; report blockers.")` to inspect the actual rendered PNG. Confirm: named author and ICP, one specific thesis, attributable evidence, no unsupported current-platform claim, concrete example or authorized experience, analytical depth, one mandatory infographic, caption and visual that add complementary value, brand alignment, restrained commercial language, explicit CTA, no secrets, and defined success metrics. Also confirm 1080 × 1350 RGB output, use of DejaVu Sans and DejaVu Sans Mono, deterministic Python/Pillow composition, no generative image model unless explicitly requested, and no unresolved visual blocker. The skill worked only if the real rendered artifacts pass.
