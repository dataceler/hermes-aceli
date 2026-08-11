---
name: agent-identity-design
description: Design, review, and install durable AI-agent identities through collaborative SOUL.md interviews, balancing mission, voice, autonomy, stakeholders, values, confidentiality, and error behavior.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [identity, soul, personality, voice, governance, interview]
---

# Agent Identity Design

Use this skill when a user wants to create, revise, or collaboratively define an agent's durable identity, especially a Hermes `SOUL.md`.

## Goal

Produce a concise identity document that changes how the agent consistently thinks and communicates without turning the identity file into a project runbook, policy dump, or list of transient environment facts.

## Important Hermes behavior

- `SOUL.md` is loaded from `$HERMES_HOME/SOUL.md`, not from the current working directory.
- It is the primary identity and replaces the built-in default identity rather than merely appending to it.
- A missing or empty file falls back to the built-in identity.
- Existing sessions retain their already-loaded identity; start a fresh session (normally `/new`) to evaluate changes.
- Project procedures belong in skills or project context files, not in `SOUL.md`.
- Re-check current Hermes documentation before asserting lifecycle behavior if the product has changed.

## Collaborative workflow

1. **Inspect before interviewing**
   - Check whether `$HERMES_HOME/SOUL.md` exists and read it.
   - Distinguish a generic starter file from a meaningful custom identity.
   - Preserve useful identity choices; do not overwrite silently.

2. **Explain the consequence**
   - Tell the user that this file becomes the primary identity.
   - Set expectations: interview first, draft second, install only after approval.

3. **Interview one dimension at a time**
   - Prefer one short question per turn or interactive prompt.
   - Offer 3–4 concrete options plus free-form input when useful.
   - Reflect each answer back as a crisp design decision before moving on.
   - Ask follow-ups when an answer is adaptive (for example, "depends on risk") rather than forcing a false fixed choice.

4. **Cover the core dimensions**
   - Central role and mission.
   - Primary stakeholders and loyalty model.
   - Autonomy calibrated by clarity, reversibility, impact, and risk.
   - Everyday tone, energy, warmth, humor, and formality.
   - Whether and how the agent should challenge weak decisions.
   - Value priority when principles conflict.
   - Desired response depth and adaptability.
   - Unacceptable behaviors and failure modes.
   - Information quality standard and evidence threshold.
   - Confidentiality assumptions among authorized people.
   - Error admission, root-cause analysis, correction, and prevention.
   - Metaphor, mascot, motto, or signature identity traits.

5. **Synthesize tensions explicitly**
   - Convert "all of the above" autonomy into context-sensitive rules.
   - Reconcile trust with least-disclosure handling of secrets.
   - Reconcile competitive energy with respect and non-arrogance.
   - Reconcile speed with verification based on impact.
   - Prefer behavioral tests ("what should the agent do when...") over adjective piles.

6. **Draft the identity**
   - Use the structure in `templates/SOUL.template.md` as a starting point, not a rigid schema.
   - Write in the language the agent should naturally use.
   - Include enough baseline identity to stand alone because the default identity is replaced.
   - Use clear positive directives and explicit anti-patterns.
   - Keep operational commands, credentials, hostnames, current projects, and temporary goals out.

7. **Review before writing**
   - Show the complete draft.
   - Ask whether to approve, adjust specific sections, revise substantially, or start over.
   - Do not install merely because the interview is complete.

8. **Install and verify**
   - Write the approved text to `$HERMES_HOME/SOUL.md`.
   - Read it back and verify the full content, not just file existence.
   - Report the exact path and explain how to start a fresh session for testing.

9. **Evaluate in behavior**
   - In a fresh session, test with scenarios that exercise disagreement, ambiguity, risk, errors, and normal conversation.
   - Revise the identity if it creates excessive verbosity, aggression, passivity, or repetitive disclaimers.

## Quality rules

- Identity should produce useful behavior, not theatrical role-play.
- A strong SOUL states what the agent optimizes for and how it behaves under tension.
- "Direct" must not become rude; "loyal" must not become blindly agreeable; "autonomous" must not become reckless.
- If the user identifies inaccurate information or wasted time as unacceptable, encode verification, uncertainty labeling, and no-fabrication behavior explicitly.
- If the user wants detailed root-cause analysis for errors, keep routine success responses concise; error analysis should not spill into unrelated work.
- Do not place secrets or personal data in the identity file.

## Supporting files

- Interview question bank and synthesis guidance: `references/interview-question-bank.md`
- Adaptable SOUL starter: `templates/SOUL.template.md`
