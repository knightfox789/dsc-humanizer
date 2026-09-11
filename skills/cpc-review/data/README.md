# CPC Procurement Intelligence Data

The CSV files in this folder are the authoritative procurement history for the CPC review skill.

## Source-of-truth tables
- `procurement_reviews.csv` — one row per CPC review/procurement.
- `item_quotes.csv` — one row per vendor quote per item.
- `awards.csv` — one row per awarded/finalized item.
- `item_catalog.csv` — normalized item names, categories, units and specification keys.
- `vendors.csv` — normalized vendor directory.
- `item_aliases.csv` — aliases used to normalize recurring item descriptions.

## Generated view
- `master_item_history.csv` — flattened award history used for quick benchmark review.

The generated Excel workbook mirrors these datasets and adds a dashboard. CSV remains the source of truth because GitHub can diff it reliably.

## Benchmark eligibility
Only finalized/approved awards should normally have `benchmark_eligible=Y`. RED, pending or unresolved reviews remain in the audit history but must not become future price benchmarks.

Historical price differences are review signals, not automatic rejection rules. Specification, unit, quantity, freight, installation, taxes, geography and procurement timing must be considered before judging a rate.
