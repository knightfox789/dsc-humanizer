# DSC Professional AI Skills

Reusable GitHub-based skills for DSC professional writing, analytical communication and procurement review.

## Skills

### 1. DSC Humanizer
The root [`SKILL.md`](SKILL.md) provides fact-safe professional rewriting, donor/technical modes and `kaushal-voice`.

#### Kaushal Voice — evidence and analytical reasoning
[`references/kaushal-voice.md`](references/kaushal-voice.md) is the evidence-first practitioner voice used for water security, agriculture, NRM, donor, technical, management and field communication.

Version 0.6.0 strengthens Kaushal Voice beyond writing style. It now includes:
- descriptive, comparative, associational, causal and projected/modelled evidence classes;
- research-design and comparison-validity checks;
- safeguards against causal overstatement;
- denominator and aggregation discipline for rates and percentages;
- explicit handling of confounders, missing variables and generalisation limits;
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

## Version

Current repository version: **0.6.0**

See [`CHANGELOG.md`](CHANGELOG.md).

## Water Security Intelligence newsletter

[Water Security Intelligence skill](skills/water-security-intelligence/SKILL.md) produces Kaushal Gadariya's India-first weekly LinkedIn publication package: verified research, a 900–1,200-word article, SEO metadata and a branded cover.

### Recall in a new chat

Paste this instruction:

> Read and follow https://github.com/knightfox789/dsc-humanizer/blob/main/skills/water-security-intelligence/SKILL.md and its linked references. Use it to create the next complete Water Security Intelligence newsletter package. Establish the previous edition cutoff, verify 12–18 consequential developments, and apply Kaushal's voice and the fixed-logo rules. Complete routine work autonomously; flag only genuine blockers.

For copy only, add "Write-up only." For a cover revision, add "Redesign the current edition cover."

GitHub storage makes the instructions retrievable; it does not automatically install the skill in a new ChatGPT session. If GitHub access is unavailable, supply the skill file and references in the chat. An installed skill-capable client can invoke the skill by its name, water-security-intelligence.

**Approved brand asset:** the original [Water Security Intelligence logo](skills/water-security-intelligence/assets/water-security-intelligence-logo.png) is bundled and referenced by the skill. The file is an unchanged copy of the user-uploaded PNG. Future editions must load this asset and preserve its geometry and colours; substituting a generated logo is forbidden. Alpha transparency must be checked before compositing.

References: [Editorial and brand rules](skills/water-security-intelligence/references/editorial-and-brand.md) · [Edition continuity and ledger](skills/water-security-intelligence/references/continuity.md).
