# CPC Procurement Intelligence Framework

## Purpose

The procurement-intelligence layer gives CPC a reusable historical evidence base for recurring items, vendor participation and price reasonableness.

It does **not** replace current quotations or market validation. Historical prices are context, not automatic ceilings.

## Data model

The system records three levels:

1. **Procurement review** — state, project/unit, donor, reference, quarter/year, verdict and final status.
2. **Vendor quote** — every quoted vendor/item combination, commercial components, responsiveness and ranking.
3. **Award** — finalized selected vendor, quantity and evaluated/landed unit cost.

Item and vendor master tables normalize names across time.

## Historical comparison sequence

For every recurring item:

1. Normalize the item name using `item_aliases.csv` where possible.
2. Match the same canonical unit.
3. Match the same `specification_key` when available.
4. Prefer benchmark-eligible awards from the same state within the configured history period.
5. If same-state history is unavailable, use comparable awards across DSC states and identify the benchmark basis clearly.
6. Show latest comparable rate, median, mean, minimum, maximum and count.
7. Calculate variance of current responsive-L1/award landed unit rate against latest and median history.
8. Flag large variance for review; do not automatically reject.
9. CPC must examine specification, quantity, freight, installation, taxes, geography, season/time and market conditions before interpreting a difference.

## Benchmark eligibility

A historical award should normally enter the benchmark pool only when:
- the CPC review/procurement is finalized or approved;
- the award is actually confirmed;
- the item specification and unit are sufficiently recorded;
- the rate represents an evaluated landed/turnkey basis appropriate for comparison.

RED, pending or unresolved AMBER proposals may remain in the audit dataset, but they should not become approved historical benchmarks.

## Item normalization

Keep both the original procurement description and a normalized recurring item name.

Descriptions such as `20mm Gitti`, `20 mm stone aggregate`, and `20 mm aggregate` may share a normalized item name only when the technical specification is genuinely comparable.

Do not merge distinct grades, pressure classes, capacities, brands/specifications or service scopes merely because the short item name is similar.

## Variance flags

Default configuration flags absolute variance against historical median at 10%, 20% and 30% bands.

These are review prompts only. They are **not** procurement approval rules and must not override evidence in the current procurement.

## Automatic update workflow

During a CPC review:

`documents → review → structured review_record.json → historical comparison → CPC decision`

After the procurement/review is finalized:

`final record → update_master.py → source CSVs → master_item_history.csv → build_excel.py → CPC_Master_Procurement_Register.xlsx`

When working through the GitHub skill, commit the changed data files and generated workbook with a procurement-specific commit message.
