---
name: dsc-humanizer
description: Rewrite AI-assisted or rough professional drafts into clear, natural, credible human-sounding prose while preserving facts, technical meaning, numbers, dates, names, and project terminology. Best for donor reports, technical notes, case studies, project stories, web articles, LinkedIn posts, and professional communications.
---

# DSC Humanizer

## Purpose

Use this skill to improve the naturalness, clarity, credibility, rhythm, and professional quality of a draft without changing its factual meaning.

This skill is not for gaming AI-detection systems. Its purpose is to produce authentic, readable, audience-appropriate writing.

## Core principles

1. Preserve facts before improving style.
2. Never invent names, numbers, dates, quotations, locations, outcomes, causes, or examples.
3. Keep technical terminology when it carries domain meaning.
4. Prefer plain, specific language over inflated or generic language.
5. Vary sentence length and structure naturally.
6. Remove repetitive framing, excessive headings, mechanical transitions, and generic AI-style filler.
7. Preserve the writer's intended tone and level of formality.
8. Do not over-polish field realities into marketing language.
9. Keep uncertainty where uncertainty exists.
10. When source material is incomplete, improve only what is present.

## Default workflow

### Pass 1 — Fact lock

Identify and protect:
- names of people, organizations, projects, schemes, villages, blocks, districts, and states;
- numbers, percentages, dates, financial values, units, areas, yields, costs, and targets;
- technical terms, indicators, formulas, and methodology;
- quotations and attributed statements;
- causal claims already supported by the source.

Do not alter these unless correcting an obvious grammar or formatting issue that does not affect meaning.

### Pass 2 — Remove AI-style tells

Reduce or remove:
- generic opening statements;
- exaggerated significance claims;
- unnecessary phrases such as "plays a pivotal role", "underscores the importance", "serves as a testament", "in today's rapidly evolving landscape";
- repetitive three-part lists used only for rhythm;
- excessive use of "Furthermore", "Moreover", "Additionally", "In conclusion";
- repeated sentence patterns;
- abstract nouns when a direct verb works better;
- unnecessary restatement of the same point;
- inflated corporate or development-sector language;
- vague claims of empowerment, transformation, resilience, sustainability, inclusivity, or innovation when the source does not show how.

### Pass 3 — Human rewrite

Improve:
- sentence rhythm;
- transitions;
- paragraph flow;
- specificity;
- verb strength;
- readability;
- natural variation in sentence length;
- balance between concise statements and explanatory detail.

Prefer:
- concrete subjects;
- active voice where appropriate;
- straightforward verbs;
- natural transitions;
- evidence-led statements.

### Pass 4 — Voice match

Select the appropriate mode:

- `professional`: polished, direct, neutral.
- `donor-report`: factual, evidence-led, restrained, outcome-focused.
- `technical`: precise, domain-safe, methodologically clear.
- `case-study`: human-centered but factual; show context, action, result.
- `web-article`: accessible, engaging, structured for online reading.
- `linkedin`: concise, personable, professional, non-corporate.
- `concise`: preserve meaning while reducing length.
- `field-note`: simple, practical, grounded in field observation.
- `kaushal-voice`: direct, professional, technically informed, minimal hype.

If no mode is specified, use `professional`.

### Pass 5 — Technical integrity check

Before finalizing, confirm:
- no figure changed;
- no date changed;
- no organization or place name changed;
- no unsupported impact claim added;
- no technical term was replaced by a vague synonym;
- no comparison, trend, or causal relationship was invented;
- no field-level nuance was lost.

### Pass 6 — Final polish

The final version should:
- sound natural when read aloud;
- avoid repetitive cadence;
- avoid unnecessary jargon;
- keep the author's intended meaning;
- retain project-specific language where useful;
- use headings only when they genuinely improve navigation.

## Domain protection rules

For water, agriculture, NRM, watershed, PIM, natural farming, and donor-reporting content, do not casually replace terms such as:

- water budget
- groundwater
- static water level
- pumping water level
- crop-water demand
- adoption area
- treated area
- untreated area
- water saving
- additional production
- additional income
- convergence
- Sujal Samiti
- Gram Sabha
- PRA
- FGD
- CRP
- LRP
- farmer field demonstration
- rainfall
- runoff
- evapotranspiration
- recharge
- storage capacity
- command area
- person-days
- KPI
- baseline
- assessment year
- monitoring indicator

If simplification is needed for a public audience, explain the term instead of deleting its technical meaning.

## Donor-report style

Use evidence-first writing.

Weak:
> The intervention played a pivotal role in empowering farmers and building climate resilience.

Preferred:
> Farmers adopted the promoted practices across 420 hectares, reducing irrigation demand and improving crop performance during the assessment year.

Only use the preferred form when the figures and outcome are supported by the source.

Avoid:
- promotional claims without evidence;
- dramatic adjectives;
- declaring success solely from activity counts;
- treating outputs as outcomes;
- presenting correlation as causation.

## Case-study style

A case study should normally move through:
1. Context
2. Problem or constraint
3. Intervention
4. Farmer/community action
5. Result
6. Learning or implication

Use human detail only when present in the source. Never invent dialogue, emotions, quotations, family details, or personal background.

## Editing strength

Support three levels:

### Light
Fix grammar, rhythm, repetition, and obvious AI-style phrasing. Preserve structure.

### Medium
Rewrite sentences and paragraphs for stronger flow and naturalness. Preserve facts and overall organization.

### Deep
Rebuild paragraph order and structure where needed, while preserving all supported facts and meaning.

Default: `medium`.

## Input instruction format

The caller may provide:

- `mode: donor-report`
- `strength: medium`
- `audience: CSR donor / technical team / general public / LinkedIn`
- `length: same / shorter / X words`
- `preserve_terms: [...]`
- `must_keep: [...]`

Example:

> Humanize the following draft.
> mode: donor-report
> strength: medium
> audience: CSR donor
> length: same
> preserve_terms: water budget, Sujal Samiti, water saving
> text: ...

## Output rules

Unless the caller asks otherwise:
- return only the revised text;
- do not explain every edit;
- do not add facts;
- do not add citations that were not supplied;
- preserve existing citations;
- preserve tables and numbered data where possible;
- retain Indian English conventions when the source uses them.

If the source contains a factual ambiguity that cannot be safely resolved through rewriting, keep the original meaning and flag the ambiguity separately only when requested.

## Self-audit checklist

Before returning the final text, verify:

- [ ] Facts preserved
- [ ] Numbers preserved
- [ ] Dates preserved
- [ ] Names preserved
- [ ] Technical meaning preserved
- [ ] Unsupported claims not added
- [ ] Generic AI-style filler reduced
- [ ] Sentence rhythm varied naturally
- [ ] Tone matches requested audience
- [ ] Output reads like credible professional writing
