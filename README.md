# DSC Professional AI Skills

Reusable GitHub-based skills for DSC professional writing, analytical communication, programme strategy, systems-transition review and procurement intelligence.

## Skills

### 1. DSC Humanizer
The root [`SKILL.md`](SKILL.md) provides fact-safe professional rewriting, donor/technical modes and `kaushal-voice`.

#### Kaushal Voice — evidence, execution and systems reasoning
[`references/kaushal-voice.md`](references/kaushal-voice.md) is the evidence-first practitioner voice used for water security, agriculture, NRM, donor, technical, management and field communication.

Version 0.7.0 combined the analytical safeguards introduced in 0.6.0 with stronger execution and systems-transition discipline. It includes:
- descriptive, comparative, associational, causal and projected/modelled evidence classes;
- research-design and comparison-validity checks;
- safeguards against causal overstatement;
- denominator and aggregation discipline for rates and percentages;
- execution-realism checks so planning, coordination, documentation, supervision and troubleshooting are not omitted from effort estimates;
- a flexible 70–30 heuristic separating direct project delivery from strategic bridge work toward uptake, continuation and scale;
- `think roadmap, act project` logic connecting project outputs to institutional owners, next decisions and longer programme/system objectives;
- documentation-as-delivery guidance for preserving methods, field adaptations, failures and conditional learning while work is still fresh;
- activity-based resource logic linking deliverables, activities, person-days/resources, assumptions, phasing and cost;
- budget/scope integrity checks when resources are reduced;
- question-led data storytelling and visual selection;
- decision-oriented analytical narrative: evidence → interpretation → limitation → next step.

Reusable prompt recipes are in [`prompts/kaushal-voice.md`](prompts/kaushal-voice.md), with regression cases in [`tests/evaluation-cases.md`](tests/evaluation-cases.md).

### 2. DSC CPC Review + Procurement Intelligence
[`skills/cpc-review/SKILL.md`](skills/cpc-review/SKILL.md) provides DSC-wide procurement review across all project states, units, programmes and funding partners.

It combines:
- source-document CPC verification;
- responsive-L1 determination;
- independent arithmetic/landed-cost checking;
- price reasonableness;
- GREEN/AMBER/RED verdicts;
- historical item-rate comparison;
- vendor and recurrence intelligence;
- controlled automatic update of master CSV data after finalization;
- generated Excel procurement register.

## CPC procurement-intelligence architecture

```text
skills/cpc-review/
├── SKILL.md
├── README.md
├── data/
│   ├── procurement_reviews.csv
│   ├── item_quotes.csv
│   ├── awards.csv
│   ├── master_item_history.csv
│   ├── item_catalog.csv
│   ├── vendors.csv
│   ├── item_aliases.csv
│   └── comparison_config.json
├── schemas/
│   └── review-record.schema.json
├── examples/
│   └── review_record.template.json
├── scripts/
│   ├── common.py
│   ├── compare_history.py
│   ├── update_master.py
│   ├── run_pipeline.py
│   └── build_excel.py
├── references/
│   ├── review-checklist.md
│   └── procurement-intelligence.md
├── tests/
│   ├── evaluation-cases.md
│   └── test_procurement_intelligence.py
└── outputs/
    └── CPC_Master_Procurement_Register.xlsx
```

## CPC quick use

```text
Use the DSC CPC review skill.
Read all documents first, independently verify responsive L1 and price reasonableness, then compare recurring items with the CPC master procurement history. Show historical benchmark findings separately from current-bid evidence. Give GREEN/AMBER/RED and do not assume missing facts.
```

After a procurement is finalized, the skill should update the structured master data and rebuild the Excel view.

## Data principle

**CSV is the source of truth; Excel is the generated analyst view.** This keeps historical changes auditable in GitHub.

Historical rates are benchmark signals rather than automatic price caps. Specifications, units, quantity, freight, installation, taxes, geography and timing must be considered.

### 3. DSC Systems Transition Review
[`skills/systems-transition-review/SKILL.md`](skills/systems-transition-review/SKILL.md) reviews pilots, programmes, proposals and strategies for genuine scale readiness.

It is designed to prevent a successful pilot from being labelled `scalable` without a credible mechanism. The skill:
- defines the intended scale and system boundary;
- classifies the dominant pathway as replication, production-system/incentive transition, collective-action/trust transition, or hybrid;
- tests whether pilot conditions can realistically survive expansion;
- maps the current state and desired system state;
- distinguishes necessary, enabling and jointly sufficient conditions;
- separates external change from programme additionality;
- identifies the rate-limiting or make-or-break condition;
- checks institutional ownership, recurring finance, delivery ecosystem and resource realism;
- gives a **GREEN / AMBER / RED / GREY** scale-readiness verdict.

Quick prompts are in [`skills/systems-transition-review/prompts/quick-start.md`](skills/systems-transition-review/prompts/quick-start.md), with regression cases in [`skills/systems-transition-review/tests/evaluation-cases.md`](skills/systems-transition-review/tests/evaluation-cases.md).

### 4. Water Security Intelligence newsletter
[`skills/water-security-intelligence/SKILL.md`](skills/water-security-intelligence/SKILL.md) produces Kaushal Gadariya's India-first weekly LinkedIn publication package: verified research, a 900–1,200-word article, SEO metadata and a branded cover.

The newsletter now applies the Systems Transition Review lens only when a consequential story or central argument claims scale, systems change, institutionalisation, replication, collective governance or government uptake. Routine technical or service-delivery developments are not forced into a systems-change frame.

### Recall in a new chat

Paste this instruction:

> Read and follow https://github.com/knightfox789/dsc-humanizer/blob/main/skills/water-security-intelligence/SKILL.md and its linked references. Use it to create the next complete Water Security Intelligence newsletter package. Establish the previous edition cutoff, verify 12–18 consequential developments, and apply Kaushal's voice and the fixed-logo rules. Complete routine work autonomously; flag only genuine blockers.

For copy only, add "Write-up only." For a cover revision, add "Redesign the current edition cover."

GitHub storage makes the instructions retrievable; it does not automatically install a skill in every new ChatGPT session. If GitHub access is unavailable, supply the relevant skill file and references in the chat.

**Approved brand asset:** the original [Water Security Intelligence logo](skills/water-security-intelligence/assets/water-security-intelligence-logo.png) is bundled and referenced by the newsletter skill. The file is an unchanged copy of the user-uploaded PNG. Future editions must load this asset and preserve its geometry and colours; substituting a generated logo is forbidden. Alpha transparency must be checked before compositing.

References: [Editorial and brand rules](skills/water-security-intelligence/references/editorial-and-brand.md) · [Edition continuity and ledger](skills/water-security-intelligence/references/continuity.md).

## Version

Current repository version: **0.8.0**

See [`CHANGELOG.md`](CHANGELOG.md).
