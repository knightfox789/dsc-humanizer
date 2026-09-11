# DSC CPC Review Skill

A reusable procurement-review skill for the **Development Support Centre (DSC) Central Procurement Committee (CPC)** across all DSC project states, units, programmes and funding partners.

This skill is **not state-specific**. It applies to procurements from Gujarat, Maharashtra, Madhya Pradesh, Rajasthan and any other DSC project geography, while allowing project-, donor- and state-specific requirements to be checked when they are actually evidenced in the procurement file.

## Core purpose

The skill independently verifies procurement proposals rather than accepting the Purchase Note, comparative statement or proposed L1 at face value.

It reviews:
- requirement and approval trail;
- quantity, unit and scope reconciliation;
- specification comparability;
- source quotations;
- arithmetic and landed cost;
- technical and commercial responsiveness;
- numerical L1 vs responsive L1;
- price reasonableness;
- commercial terms;
- vendor eligibility where applicable;
- documentation gaps and red flags;
- GREEN / AMBER / RED verdict;
- CPC recommendation and observation for record.

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

## Standard use

```text
Use the CPC review skill.

Read all procurement documents completely first.
Identify the state, project/unit and funding partner where available.
Independently verify requirement, scope, specification, quotations,
arithmetic, comparative statement, responsiveness, L1 and price reasonableness.

Give:
1. Executive summary
2. Document completeness and gaps
3. Vendor-wise L1 verification
4. Price reasonableness
5. Key CPC observations
6. GREEN / AMBER / RED verdict
7. Final CPC recommendation
8. Short CPC observation for Purchase Note/minutes

Do not assume missing facts.
```

## Important DSC-wide rule

The review logic is common across DSC, but the skill must **not invent or transfer a state-specific, donor-specific or project-specific procurement rule** when the applicable document is not available.

Where a special rule matters, the review should say what evidence is missing and whether that gap affects approval.

## Multi-state procurement

For centralised or multi-state procurement, the skill also checks whether delivery locations, freight, installation, service obligations and landed cost vary by state, and whether award is intended centrally, state-wise, lot-wise or item-wise.

## Re-review

When the project team submits clarifications or additional records, use the re-review prompt in [`prompts/quick-start.md`](prompts/quick-start.md). The skill will classify earlier observations as **Closed, Partially closed, Open, or New issue identified** and reassess the CPC verdict.
