# DSC Professional AI Skills

Reusable GitHub-based skills for DSC professional writing and procurement review.

## Skills

### 1. DSC Humanizer
The root [`SKILL.md`](SKILL.md) provides fact-safe professional rewriting, donor/technical modes and `kaushal-voice`.

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

Current repository version: **0.5.0**

See [`CHANGELOG.md`](CHANGELOG.md).

## Water Security Intelligence newsletter

[Water Security Intelligence skill](skills/water-security-intelligence/SKILL.md) produces Kaushal Gadariya's India-first weekly LinkedIn publication package: verified research, a 900–1,200-word article, SEO metadata and a branded cover.

### Recall in a new chat

Paste this instruction:

> Read and follow https://github.com/knightfox789/dsc-humanizer/blob/main/skills/water-security-intelligence/SKILL.md and its linked references. Use it to create the next complete Water Security Intelligence newsletter package. Establish the previous edition cutoff, verify 12–18 consequential developments, and apply Kaushal's voice and the fixed-logo rules. Complete routine work autonomously; flag only genuine blockers.

For copy only, add "Write-up only." For a cover revision, add "Redesign the current edition cover."

GitHub storage makes the instructions retrievable; it does not automatically install the skill in a new ChatGPT session. If GitHub access is unavailable, supply the skill file and references in the chat. An installed skill-capable client can invoke the skill by its name, water-security-intelligence.

**Brand asset dependency:** the exact approved logo/poster binaries are not yet bundled. The skill records retrieval identifiers and requires the approved asset to be retrieved or attached before a branded poster is finalised. It forbids substituting a generated logo.

References: [Editorial and brand rules](skills/water-security-intelligence/references/editorial-and-brand.md) · [Edition continuity and ledger](skills/water-security-intelligence/references/continuity.md).
