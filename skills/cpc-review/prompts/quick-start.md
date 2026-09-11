# CPC Review — Quick Start Prompts

## 1. Full CPC review with historical intelligence

```text
Use the DSC CPC review skill.

Read all uploaded procurement documents completely first.
Identify the state, DSC project/unit and funding partner.
Independently verify requirement, scope, specification, all vendor quotations, arithmetic, comparative statement, responsiveness, responsive L1 and price reasonableness.

For recurring items, compare the current landed unit rate with the CPC master procurement history. Show same-state and DSC-wide comparable counts, latest comparable rate, historical median/range, variance and comparison confidence. Historical variance is a review signal, not an automatic rejection rule.

Give:
1. Executive summary
2. Document completeness/gaps
3. Vendor-wise L1 verification
4. Historical price intelligence
5. Price reasonableness
6. Key CPC observations
7. GREEN / AMBER / RED verdict
8. Final CPC recommendation
9. Short CPC observation for Purchase Note/minutes

Do not assume missing facts.
```

## 2. Historical-price-only check

```text
Use the CPC procurement-intelligence layer. Normalize the item, confirm unit and specification key, then compare the current landed unit rate with benchmark-eligible finalized awards from the previous 24 months. Prefer same-state history first, then comparable DSC-wide records. Show latest, median, mean, min/max, counts, variance and confidence. Explain material comparability limitations.
```

## 3. Finalize and update master

```text
The CPC review/procurement is now finalized. Prepare the structured review_record.json, ensure award status and benchmark eligibility are correct, update all CPC master CSV tables, rebuild master_item_history.csv and rebuild the Excel register. Do not add unresolved RED/pending data as an approved price benchmark.
```

Command:
```bash
python skills/cpc-review/scripts/run_pipeline.py review_record.json --finalize
```

## 4. Re-review after clarification

```text
Re-review this CPC proposal using the CPC review skill. Compare new clarification/documents with the previous findings. Mark each earlier observation Closed, Partially closed, Open, or New issue identified. Recalculate responsive L1 and historical comparison if scope, specification, rate, tax, freight or installation changed. State whether the verdict changes and give revised CPC observation/recommendation.
```

## 5. Multi-state procurement

```text
Use the CPC review skill for this multi-state DSC procurement. Identify each delivery state/unit and verify whether specification, quantity, freight, installation, service obligations, taxes and landed cost differ by location. Compare historical rates on a genuinely comparable landed-cost basis. Confirm whether award is central, state-wise, lot-wise or item-wise and determine responsive L1 accordingly.
```

## 6. CPC reply email

```text
After completing the CPC review, draft a short, constructive and professional reply email to the project/procurement team. Mention only material conditions and any relevant historical-price observation. Do not dilute RED or AMBER requirements.
```
