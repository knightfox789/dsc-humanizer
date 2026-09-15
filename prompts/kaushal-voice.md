# Kaushal Voice prompts

Use these prompts when you want the output to follow the `kaushal-voice` profile.

## General professional rewrite

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: professional
length: same

Rewrite:
[paste draft]
```

## Donor / CSR report

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: donor / CSR partner
priority: evidence, scale, outcome, implementation quality, attribution limits, next step
preserve_terms: [add project-specific technical terms]

Rewrite:
[paste draft]
```

## Technical note

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: technical team
priority: method, assumptions, measurement, comparison validity, calculation, field conditions, uncertainty, limitations

Rewrite:
[paste draft]
```

## Research / analytical interpretation

```text
Use dsc-humanizer.

mode: kaushal-voice
audience: technical / donor / management
analysis_mode: research-quality
priority: research design, evidence class, comparison validity, denominator logic, confounders, interpretation, limitations, decision implication

Before rewriting:
1. classify important claims as descriptive, comparative, associational, causal, or projected/modelled;
2. check whether comparison groups, periods, units and definitions are genuinely comparable;
3. check denominator and aggregation logic for percentages, rates and per-unit indicators;
4. identify material confounders or missing variables that could change the interpretation;
5. prevent causal wording unless the evidence supports causality.

Then rewrite in Kaushal Voice.

Text / findings:
[paste analytical draft or findings]
```

## Dashboard / data-storytelling note

```text
Use dsc-humanizer.

mode: kaushal-voice
audience: management / donor / technical team
analysis_mode: data-storytelling
priority: question, valid comparison, key evidence, interpretation, limitation, decision implication

For every important visual or finding:
- state the analytical question;
- identify the evidence class;
- select or assess the visual based on the question, not on available software;
- distinguish spatial, temporal, paired-comparison and relationship questions;
- avoid narrating every number;
- surface the one or two conclusions the evidence can defend;
- state what cannot yet be concluded when material.

Input:
[paste chart description, dashboard findings or draft narrative]
```

## Donor observation / compliance response

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: donor / reviewer
response_type: observation-response
priority: acknowledge valid gap, explain evidence, distinguish documentation from technical issue where justified, state what is verified versus inferred, state corrective action

Rewrite:
[paste observation and draft response]
```

## Governing Board note

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: Governing Board
priority: programme direction, field evidence, evidence strength, institutional progress, risks, uncertainties, convergence, decisions and next steps
length: concise

Rewrite:
[paste draft]
```

## Useful optional controls

```text
length: same | shorter | X words
preserve_terms: [...]
must_keep: [...]
strength: light | medium | deep
analysis_mode: none | research-quality | data-storytelling
evidence_class: descriptive | comparative | associational | causal | projected/modelled | auto
comparison_basis: [describe groups/periods/geography]
visual_question: [state what the visual should answer]
```

The core rules still apply:

**Style may change; facts must not.**

**Do not make the writing more certain than the research design, data or calculation allows.**
