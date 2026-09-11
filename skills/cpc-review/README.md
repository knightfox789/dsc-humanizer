# DSC CPC Review + Procurement Intelligence

Reusable DSC-wide procurement review skill with historical price and vendor intelligence.

## What v0.5.0 adds

The CPC reviewer no longer treats each proposal as an isolated case. It can compare recurring items against Git-versioned historical procurement records and then update the master dataset after the procurement is finalized.

Historical intelligence includes:
- normalized previous item rates;
- same-state and DSC-wide comparisons;
- latest, median, mean, minimum and maximum landed unit rates;
- variance against latest/median;
- vendor participation and award history;
- quarter and financial-year tracking;
- project/unit, state and funding-partner context.

Historical variance is a review prompt, not an automatic approval/rejection rule.

## Source of truth

The CSV files under `data/` are authoritative. The Excel workbook is a generated analysis view.

Key files:
- `data/procurement_reviews.csv`
- `data/item_quotes.csv`
- `data/awards.csv`
- `data/master_item_history.csv`
- `data/item_catalog.csv`
- `data/vendors.csv`
- `data/item_aliases.csv`
- `data/comparison_config.json`

## During review

1. Read all procurement documents.
2. Perform normal CPC verification.
3. Generate a structured record using `examples/review_record.template.json`.
4. Run historical comparison:

```bash
python skills/cpc-review/scripts/compare_history.py review_record.json
```

5. Include historical findings separately in the price-reasonableness assessment.

## After final approval/closure

```bash
python skills/cpc-review/scripts/run_pipeline.py review_record.json --finalize
```

This updates the CSV master data and rebuilds the Excel register where `artifact_tool` is available.

## Item normalization

Store the original item wording and a normalized item name. Use `specification_key` to prevent false comparison between materially different grades, sizes, pressure classes, capacities or service scopes.

## Benchmark eligibility

Pending/RED/unresolved items are retained for audit history but are not approved benchmark records. Only finalized approved awards should normally be marked `benchmark_eligible=Y`.

## Excel register

`outputs/CPC_Master_Procurement_Register.xlsx` contains:
- Dashboard
- Procurement Reviews
- Item Quotes
- Awards
- Master Item History
- Item Catalog
- Vendors
- Item Aliases

CSV remains the source of truth so GitHub history stays auditable.
