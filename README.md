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
