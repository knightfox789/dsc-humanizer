---
name: dsc-humanizer
description: Rewrite AI-assisted or rough professional drafts into clear, natural, credible human-sounding prose while preserving facts, technical meaning, numbers, dates, names, qualifiers, and project terminology. Best for donor reports, technical notes, case studies, project stories, web articles, Board notes, compliance responses, LinkedIn posts, and professional communications.
---

# DSC Humanizer

## Purpose

Use this skill to improve the naturalness, clarity, credibility, rhythm, and professional quality of a draft without changing its factual meaning.

This skill is for authentic, readable, audience-appropriate writing. It is not for gaming AI-detection systems.

## Core rule

**Style may change; facts must not.**

## Core principles

1. Preserve facts before improving style.
2. Never invent names, numbers, dates, quotations, locations, outcomes, causes, examples, or evidence.
3. Preserve uncertainty and qualification such as `estimated`, `expected`, `reported`, `approximately`, `preliminary`, and `may`.
4. Keep technical terminology when it carries domain meaning.
5. Prefer plain, specific language over inflated or generic language.
6. Vary sentence length and structure naturally.
7. Remove repetitive framing, mechanical transitions, and generic AI-style filler.
8. Do not over-polish field realities into marketing language.
9. Distinguish activity, output, outcome, and impact.
10. When source material is incomplete, improve only what is supported.

## Default workflow

### Pass 1 — Fact lock

Identify and protect:
- names of people, organizations, projects, schemes, villages, blocks, districts, and states;
- numbers, percentages, dates, financial values, units, areas, yields, costs, and targets;
- technical terms, indicators, formulas, and methodology;
- quotations and attributed statements;
- uncertainty and qualification;
- causal claims already supported by the source.

Do not alter these unless the user explicitly asks for a factual correction.

### Pass 2 — Remove AI-style tells

Reduce or remove:
- generic opening statements;
- exaggerated significance claims;
- phrases such as `plays a pivotal role`, `underscores the importance`, `serves as a testament`, or `in today's rapidly evolving landscape` when they add no evidence;
- repetitive three-part lists used only for rhythm;
- excessive `Furthermore`, `Moreover`, `Additionally`, and `In conclusion`;
- repeated sentence patterns;
- abstract nouns when a direct verb works better;
- unnecessary restatement;
- inflated corporate or development-sector language;
- vague claims of empowerment, transformation, resilience, sustainability, inclusivity, or innovation when the source does not show how.

See `references/ai-patterns-to-reduce.md`.

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

Prefer concrete subjects, straightforward verbs, natural transitions, and evidence-led statements.

### Pass 4 — Voice match

Select the appropriate mode:

- `professional`: polished, direct, neutral.
- `donor-report`: factual, evidence-led, restrained, outcome-focused.
- `technical`: precise, domain-safe, methodologically clear.
- `case-study`: human-centred but factual; show context, action, result.
- `web-article`: accessible, engaging, structured for online reading.
- `linkedin`: concise, personable, professional, non-corporate.
- `concise`: preserve meaning while reducing length.
- `field-note`: simple, practical, grounded in field observation.
- `kaushal-voice`: evidence-first, technically grounded, practical, accountable, institution-aware, and low-hype.

If no mode is specified, use `professional`.

When `mode: kaushal-voice` is requested, apply `references/kaushal-voice.md` as the primary voice guide in addition to all fact-lock rules. Audience-specific guidance inside that file should shape the final tone.

### Pass 5 — Technical integrity check

Before finalizing, confirm:
- no figure changed;
- no date changed;
- no organization or place name changed;
- no qualifier was strengthened or removed;
- no unsupported impact claim was added;
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

## Mode references

Use these supporting guides when relevant:

- `references/fact-preservation.md` — always applicable.
- `references/donor-report-style.md` — donor and CSR reporting.
- `references/technical-writing-style.md` — methods and technical documentation.
- `references/case-study-style.md` — project stories and cases.
- `references/ai-patterns-to-reduce.md` — style cleanup.
- `references/kaushal-voice.md` — personal professional voice profile.

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
- Water User Group / Water User Association
- Measurement Book (MB)
- PRA
- FGD
- CRP
- LRP
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
> Farmers adopted the promoted practices across 420 hectares, with an estimated reduction in irrigation demand during the assessment year.

Only use the preferred form when the figures and result are supported by the source.

Avoid:
- promotional claims without evidence;
- dramatic adjectives;
- declaring success solely from activity counts;
- treating outputs as outcomes;
- presenting correlation as causation.

## Kaushal-voice style

When this mode is active, favour the practical sequence:

**Context → Action → Evidence → Meaning → Next step**

Use the sequence flexibly rather than mechanically.

Prefer:
- evidence before adjectives;
- technical reasoning tied to field conditions;
- explicit institutional roles when relevant;
- calm acknowledgement of documentation or implementation gaps;
- clear distinction between the available record and what still needs verification;
- corrective action when a review observation is valid;
- Indian English conventions unless another house style is requested.

For detailed guidance, use `references/kaushal-voice.md`.

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

### Light
Fix grammar, rhythm, repetition, and obvious AI-style phrasing. Preserve structure.

### Medium
Rewrite sentences and paragraphs for stronger flow and naturalness. Preserve facts and overall organization.

### Deep
Rebuild paragraph order and structure where needed, while preserving all supported facts and meaning.

Default: `medium`.

## Input instruction format

The caller may provide:

- `mode: donor-report | technical | kaushal-voice | ...`
- `strength: light | medium | deep`
- `audience: CSR donor | technical team | Governing Board | general public | LinkedIn`
- `length: same | shorter | X words`
- `preserve_terms: [...]`
- `must_keep: [...]`
- `priority: evidence | method | outcomes | accountability | ...`
- `response_type: observation-response` when applicable.

Example:

> Humanize the following draft.
> mode: kaushal-voice
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

If the source contains a factual ambiguity that cannot be safely resolved through rewriting, preserve the ambiguity. Flag it separately only when the user asks for review notes or when rewriting it as certain would be misleading.

## Self-audit checklist

Before returning the final text, verify:

- [ ] Facts preserved
- [ ] Numbers preserved
- [ ] Dates preserved
- [ ] Names preserved
- [ ] Qualifiers preserved
- [ ] Technical meaning preserved
- [ ] Unsupported claims not added
- [ ] Activity/output/outcome/impact levels not inflated
- [ ] Generic AI-style filler reduced
- [ ] Sentence rhythm varied naturally
- [ ] Tone matches requested audience
- [ ] Output reads like credible professional writing
- [ ] In `kaushal-voice`, evidence is more visible than adjectives and the writing sounds like a practitioner rather than a marketing writer
