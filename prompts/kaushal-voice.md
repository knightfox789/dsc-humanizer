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

## Workplan / staffing / effort realism

```text
Use dsc-humanizer.

mode: kaushal-voice
audience: management / project manager / donor
analysis_mode: execution-realism
priority: deliverable, activities, person-days, coordination, documentation, quality control, assumptions, timing, resource gaps

Review the plan before rewriting:
1. identify the visible deliverable;
2. identify necessary work around it: planning/review, travel or external coordination, documentation/reporting, administration/compliance, supervision/capacity-building, troubleshooting and technical execution;
3. do not invent hours or person-days where the source is silent;
4. flag likely under-estimation when only the visible technical task has been budgeted;
5. link resource assumptions transparently to the deliverable and timing.

Input:
[paste workplan, staffing estimate or draft note]
```

## 70–30 systems / scale review

```text
Use dsc-humanizer.

mode: kaushal-voice
audience: management / Governing Board / donor / programme team
analysis_mode: systems-roadmap
priority: project delivery, strategic bridge, institutional ownership, scale-out, scale-up, learning, next decision

Use 70–30 only as a heuristic:
- roughly 70% asks what is needed to deliver project outputs properly;
- roughly 30% asks what is needed to connect those outputs to outcomes, uptake, scale and the longer roadmap.

Do not force the ratio. Adapt it to the project context.

For the strategic bridge, ask:
- who will use or carry the work forward;
- what happens after the funded period;
- which institution or partner must own the next step;
- what analysis, engagement, documentation or capacity is still needed;
- what gap remains between project output and wider outcome.

Input:
[paste programme note, workplan, strategy or project design]
```

## Budget / scope negotiation note

```text
Use dsc-humanizer.

mode: kaushal-voice
audience: donor / management
analysis_mode: activity-based-resource
priority: transparency, deliverables, activities, resource assumptions, phasing, scope trade-offs

Review the chain:
Deliverable → activities → person-days/resources → unit assumptions → timing/phasing → cost.

If the budget or staff time is reduced materially, identify which activities, quality controls, milestones or deliverables may need review. Do not assume that identical scope can always be delivered with fewer resources, and do not automatically claim scope must reduce unless the evidence supports it.

Input:
[paste budget note, donor observation or proposed cut]
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
priority: programme direction, field evidence, evidence strength, institutional progress, execution realism, strategic bridge, risks, uncertainties, convergence, decisions and next steps
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
analysis_mode: none | research-quality | data-storytelling | execution-realism | systems-roadmap | activity-based-resource
evidence_class: descriptive | comparative | associational | causal | projected/modelled | auto
comparison_basis: [describe groups/periods/geography]
visual_question: [state what the visual should answer]
strategic_bridge: [describe intended post-project uptake/scale pathway if known]
```

The core rules still apply:

**Style may change; facts must not.**

**Do not make the writing more certain than the research design, data or calculation allows.**

**Do not budget or describe only the visible task; account for the real work needed to deliver it well.**
