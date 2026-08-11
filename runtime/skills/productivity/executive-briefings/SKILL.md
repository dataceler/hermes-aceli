---
name: executive-briefings
description: "Use for executive briefings. Turn signals into actions."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [briefing, executive, operations, prioritization, reporting]
    related_skills: [google-workspace, document-to-action-items]
---

# Executive Briefings

## Overview

Executive briefings are decision tools, not activity reports. They must answer four questions quickly: **where are we, what matters most, what does it mean, and what happens next?**

Optimize for decision quality and execution. Omit information that does not change a priority, decision, owner, deadline, or risk posture.

## When to Use

Use this skill for:

- daily or weekly leadership updates;
- client, delivery, revenue, pipeline, or operating-risk summaries;
- meeting-to-execution updates for decision makers;
- scheduled briefings built from calendars, mail, project sources, CRM, financial summaries, or documented context.

Do not use it for broad news digests, capability catalogs, unfiltered data dumps, or general research roundups.

## Operating Model

### 1. Establish the decision horizon

Define the period and the decision window before collecting data:

- **Daily:** what can change today or requires attention before the next business day.
- **Weekly:** what can change the week’s commercial, delivery, or operating outcome.
- **Project:** what changes milestone, scope, quality, budget, client confidence, or risk.

Completion criterion: the briefing has one clear time horizon and cannot accidentally mix stale history with live priorities.

### 2. Collect only decision-relevant evidence

Start from authorized primary operational sources: pipeline/CRM, delivery tracker, calendar, meeting records, financial summary, customer communication, and infrastructure status. Use only the smallest set needed to assess the current state.

For each signal, record internally:

- **fact:** what was actually observed;
- **impact:** revenue, customer, deadline, efficiency, quality, or risk affected;
- **confidence:** verified, inferred, or insufficient data;
- **actionability:** whether a leader can act on it now.

Do not repeat private source contents verbatim. Summarize only what the recipients legitimately need to act.

Completion criterion: every included signal has an operational consequence or supports a required decision.

### 3. Prioritize one central message

Rank candidates by:

1. impact if ignored;
2. urgency of the decision or action;
3. confidence in the evidence;
4. reversibility and cost of delay.

Choose one central message. The remaining facts serve as context, not competing headlines.

Completion criterion: a reader can restate the priority in one sentence without reading the entire briefing.

### 4. Convert the priority into execution

Set one measurable objective and one or two required actions. Every action must contain:

- suggested accountable owner;
- concrete verb and object;
- deadline or decision point;
- expected result.

If an approval is needed, state the exact choice and its consequence. Do not ask broad discovery questions disguised as actions.

Completion criterion: someone can execute the next step without needing a second interpretation meeting.

## Default Daily Structure

Use this format unless the user specifies another:

```markdown
**PANORAMA**
- **Comercial:** [one verified status sentence]
- **Entregas:** [one verified status sentence]
- **Operação:** [one verified status sentence]

**MENSAGEM-CHAVE**
[One sentence: what the panorama means for revenue, client, timeline, efficiency, or risk.]

**OBJETIVO DE HOJE**
[One measurable outcome.]

**PRÓXIMAS AÇÕES**
1. **[Owner] — [concrete action] — [deadline] — [expected result].**
2. [Only if indispensable.]

**DECISÃO NECESSÁRIA**
[Include only when an executive must approve or choose something.]
```

Keep the default daily version to roughly 8–12 useful lines. Use fewer lines when the situation is simple.

## Handling Missing Data

Never manufacture a panorama from generic possibilities. When evidence is missing:

- say **“sem dados suficientes”** for the specific front;
- name the missing source or field in a few words;
- make the recovery action specific, assigned, and time-bound only if it is needed to unlock a real decision.

Bad: “Ganhar mais visibilidade comercial.”

Good: “Responsável do pipeline — atualizar etapa, valor e próxima ação dos três negócios em negociação até 14h — previsão comercial revisada.”

## Prompt and Automation Discipline

Scheduled briefings must load only the context and tools needed for the report. Large reference skills or generic capability inventories consume budget and weaken the signal-to-noise ratio.

Prefer a compact prompt that states:

- approved data sources;
- selection criteria;
- exact output structure;
- line budget;
- privacy limits;
- explicit prohibition on fabricated facts and generic filler.

Completion criterion: the scheduled task can produce the expected structure without importing unrelated setup instructions or long manuals.

## Common Pitfalls

1. **Capability catalog instead of leadership brief.**
   - Fix: remove descriptions of what the agent could do unless they directly unlock today’s action.

2. **Several priorities presented as equal.**
   - Fix: select one message-key; label other items as context or omit them.

3. **Facts without a “so what?”.**
   - Fix: state the consequence in business terms immediately after the panorama.

4. **Abstract actions.**
   - Fix: name owner, object, deadline, and expected result.

5. **Forced content when sources are weak.**
   - Fix: disclose the exact information gap and request only the decision-critical data.

6. **A concise but confusing report.**
   - Fix: preserve the hierarchy Panorama → Message-key → Objective → Actions. Brevity does not replace structure.

7. **Prompt bloat in a recurring run.**
   - Fix: embed the minimal read-only retrieval routine in the job prompt; do not attach a large general-purpose skill unless it is essential.

## Verification Checklist

- [ ] The report has a defined time horizon.
- [ ] Every factual statement is traceable to an authorized source or marked as insufficient data.
- [ ] It has one unambiguous central message.
- [ ] The business impact is explicit.
- [ ] There is one measurable objective.
- [ ] Each recommended action has owner, action, deadline, and expected result.
- [ ] There are no generic capability lists, news filler, or unranked recommendations.
- [ ] The line budget and privacy constraints are respected.

## References

- `references/dataceler-daily-briefing.md` — Dataceler-specific default framing and examples derived from user feedback.
