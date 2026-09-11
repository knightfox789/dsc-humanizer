---
name: cpc-review
description: Independently review Development Support Centre (DSC) Central Procurement Committee (CPC) proposals across all DSC project states and programmes, using source-document verification, responsive-L1 logic, price reasonableness, historical procurement intelligence, GREEN/AMBER/RED verdicts, and controlled master-data updates.
---

# DSC Central Procurement Committee (CPC) Review Skill

## Purpose

Use this skill for DSC CPC approval emails, procurement proposals, Purchase Notes, comparative statements, vendor-selection packs, rate approvals, works, services and material procurement across all DSC project states, units, donors and programmes.

The review must be independent and evidence-based. Do not accept a Purchase Note, comparative statement, proposed L1, historical rate or field-team conclusion at face value.

## Core rules

1. **Do not approve a conclusion that the available evidence cannot support.**
2. **Responsive L1, not numerical L1, is the CPC decision basis.**
3. **Correct L1 does not automatically mean reasonable price.**
4. **Historical price is a benchmark signal, not an automatic ceiling.**
5. **Only finalized/approved awards should normally become future price benchmarks.**
6. If a fact, rule or threshold is missing, say `not verified`; do not invent it.

## Files to load

For a full review, use:
- `references/review-checklist.md` for document and procurement checks;
- `references/procurement-intelligence.md` for historical comparison and master-data rules;
- `data/comparison_config.json` for comparison windows and review flags;
- CSV files under `data/` for historical procurement evidence.

## Mandatory review sequence

### 1. Procurement identity
Record where available:
- state;
- DSC project/unit/district;
- project name;
- funding partner/donor;
- procurement category;
- procurement reference;
- approved/estimated value;
- review/procurement date.

### 2. Read all available source documents
Build a source map before giving a conclusion. Check requisition, budget/plan, RFQ, specification/BoQ, all quotations, comparative statement, negotiation note/minutes, eligibility evidence, technical note, previous rates/price discovery, and draft PO/WO where available.

Classify missing evidence as `Critical`, `Material but correctable`, or `Informational`.

### 3. Requirement, specification and scope
Reconcile quantity, unit, pack size and scope. Confirm vendors quote against a comparable specification. Do not treat a cheaper incomplete/non-responsive bid as L1.

### 4. Independent commercial verification
Recalculate quantity × rate, GST/tax, freight, loading/unloading, installation, testing/commissioning, accessories, discounts and final evaluated/landed cost. Compare every value in the comparative statement with its source quotation.

### 5. Responsiveness and L1
Classify each bid:
- Responsive;
- Responsive subject to clarification;
- Non-responsive / incomplete.

Show both numerical rank and responsive rank. Use responsive L1 for recommendation. If scope changes materially, recalculate all responsive bids on the same basis or recommend fresh quotations/re-bidding.

### 6. Current price reasonableness
Check available current evidence: responsive bids, approved estimate/budget, market survey, documented price discovery, catalogue/e-marketplace where suitable, engineer estimate for works, or other valid benchmark.

### 7. Historical procurement intelligence — mandatory for recurring items
Before final CPC verdict, check the master procurement history when the item may have been procured previously.

Create a structured `review_record.json` using `schemas/review-record.schema.json`, then run:

```bash
python skills/cpc-review/scripts/compare_history.py review_record.json
```

For each item, report when available:
- same-state comparable count;
- all-DSC comparable count;
- latest comparable landed unit rate/date/state;
- historical median, mean, minimum and maximum;
- current-rate variance vs latest and median;
- benchmark basis: same state or all DSC states;
- comparison confidence;
- variance review flag.

Historical matching should prefer:
1. same normalized item;
2. same canonical unit;
3. same specification key;
4. benchmark-eligible finalized awards within the configured history window;
5. same-state history first, then comparable DSC-wide history.

Do not declare a rate high or low from variance alone. Check specification, quality/grade, quantity, freight, installation, tax, location, season/time, delivery and service conditions.

If no comparable history exists, explicitly state: `No reliable historical CPC benchmark found.`

### 8. Vendor and recurrence observations
Use historical data only where relevant to note:
- recurring vendor participation;
- prior awarded rates for the same item;
- same vendor across units/states;
- unusual current price movement;
- repeated items that may benefit from rate contracts, centralized sourcing, framework agreements or consolidated price discovery.

These are suggestions, not findings of wrongdoing.

### 9. Verdict

**GREEN** — responsive L1 verified, price reasonableness supported, historical/current checks do not reveal an unresolved material issue, and required approval evidence is materially complete.

**AMBER** — procurement is broadly supportable but explicit corrections/clarifications/validation are required before PO/WO, and the open point is not presently expected to invalidate the comparison.

**RED** — L1 cannot be reliably established, bids are materially non-comparable/non-responsive, competition/approval evidence is inadequate, all rates appear unreasonable without support, or fresh price discovery/quotations/re-tendering are required.

Historical variance alone must not automatically create RED.

## Standard output

### A. Executive summary
State/project/unit, funding partner, procurement, proposed vendor/value, CPC verdict.

### B. Document completeness
`Evidence | Status | Materiality | Comment`

### C. L1 verification
`Vendor | Evaluated total | Responsiveness | Numerical rank | Responsive rank | Key issue`

### D. Historical price intelligence
`Item | Current landed rate | Latest comparable | Historical median | Comparable count | Variance | Flag | Confidence`

### E. Price reasonableness
State whether reasonableness is `Established`, `Partially established`, or `Not established`, explaining current and historical evidence separately.

### F. Key CPC observations
Only material decision points.

### G. CPC verdict and recommendation
GREEN/AMBER/RED with exact conditions/action.

### H. CPC observation for record
Short paragraph suitable for Purchase Note/minutes.

### I. Reply email
Only when requested.

## Structured record and automatic master update

During every full CPC review, prepare a structured record compatible with `schemas/review-record.schema.json`.

### Before decision
Run historical comparison. Do **not** update the benchmark master yet.

### After procurement/review is finalized
Run:

```bash
python skills/cpc-review/scripts/run_pipeline.py review_record.json --finalize
```

This will:
1. compare the current item against history;
2. upsert the procurement review;
3. store all vendor quote rows;
4. update normalized item/vendor masters;
5. add award rows;
6. mark benchmark eligibility according to final status;
7. rebuild `master_item_history.csv`;
8. rebuild the Excel register where the spreadsheet runtime is available.

When operating through GitHub, commit changed data files and the generated workbook with a procurement-specific commit message.

### Benchmark protection
- GREEN/finalized approved awards may be benchmark eligible.
- AMBER may enter the benchmark only after required conditions are closed and final approval is recorded.
- RED/pending/unresolved records may remain in review history but must have `benchmark_eligible=N`.
- Never promote an unapproved quotation to an approved historical benchmark.

## Re-review after clarification
For each previous observation mark `Closed`, `Partially closed`, `Open`, or `New issue identified`. Recalculate L1/history if scope, rate, tax, freight, installation or specification changes. State whether verdict changes.

## Cross-state and multi-state procurement
Check landed cost by delivery location where required; identify whether award is central, state-wise, lot-wise or item-wise; and do not apply one state's historical price unchanged to another without considering logistics and specification differences.

## Review style
Be concise, evidence-rich, firm on material gaps, non-accusatory, clear about verified vs unverified facts, and practical about corrective action.
