# CPC Review Skill

A reusable review skill for Development Support Centre (DSC) Maharashtra Central Procurement Committee (CPC) procurement proposals.

## Primary objective

Independently verify whether a proposed procurement and L1 recommendation are supportable from the underlying evidence.

The skill does not simply accept the Purchase Note or comparative statement. It traces the procurement chain:

`approved requirement → budget/procurement plan → RFQ/specification → quotations → responsiveness → arithmetic → comparative → negotiation → price reasonableness → responsive L1 → CPC verdict`

## Files

```text
skills/cpc-review/
├── SKILL.md
├── README.md
├── prompts/
│   └── quick-start.md
├── references/
│   └── review-checklist.md
└── tests/
    └── evaluation-cases.md
```

## Core distinctions

The skill deliberately separates:

1. **Numerical L1** from **responsive L1**.
2. **L1 correctness** from **price reasonableness**.
3. **Critical evidence gaps** from **correctable documentation gaps**.
4. **Procurement concerns** from unsupported allegations.

## Verdicts

- **GREEN** — responsive L1 verified; price reasonably supported; no material gap remains.
- **AMBER** — procurement is supportable subject to explicit correction / clarification before PO or Work Order.
- **RED** — L1/procurement should not presently be approved; critical verification, technical, competition or price-discovery problem remains.

## Quick use

```text
Use the CPC review skill.
Read all uploaded procurement documents completely before giving any conclusion.
Give me document gaps, independent L1 verification, material CPC observations, GREEN/AMBER/RED verdict, final recommendation, and a short CPC observation for the Purchase Note.
Do not assume missing facts.
```

See [`prompts/quick-start.md`](prompts/quick-start.md) for additional workflows.
