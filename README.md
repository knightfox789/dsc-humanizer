# DSC Professional AI Skills

A reusable GitHub-based skill repository for DSC professional writing and procurement review workflows.

The repository contains two independent skills:

1. **DSC Humanizer** — fact-safe professional rewriting, including `kaushal-voice`.
2. **CPC Review** — independent DSC-wide procurement review, L1 verification and GREEN/AMBER/RED recommendation across all project states and programmes.

## Skill 1 — DSC Humanizer

The root [`SKILL.md`](SKILL.md) rewrites AI-assisted or rough drafts into clearer, more natural and credible prose while protecting factual and technical integrity.

**Core rule:** style may change; facts must not.

Best for:
- donor and CSR reports;
- water, agriculture, NRM and development-sector documentation;
- technical notes;
- case studies and project stories;
- Governing Board and management notes;
- compliance responses;
- web articles and professional posts.

### Kaushal Voice

The `kaushal-voice` profile favours:
- evidence before adjectives;
- technical reasoning connected to field conditions;
- practical `context → action → evidence → meaning → next step` flow;
- accurate institutional roles;
- calm acknowledgement of gaps;
- preservation of qualifiers such as `estimated`, `expected`, `reported`, `approximately`, `preliminary`, and `may`;
- restrained development-sector language;
- Indian English conventions unless another house style is requested.

See [`references/kaushal-voice.md`](references/kaushal-voice.md).

## Skill 2 — DSC CPC Review

The [`skills/cpc-review/SKILL.md`](skills/cpc-review/SKILL.md) skill reviews Development Support Centre Central Procurement Committee proposals independently from source evidence.

It applies across **all DSC project states, units, programmes and funding partners**. The core review framework is common across DSC, while project-, donor- and state-specific requirements are applied only when supported by the relevant documents.

It traces:

`procurement context → approved requirement → budget/procurement plan → applicable conditions → RFQ/specification → quotations → responsiveness → arithmetic → comparative statement → negotiation → price reasonableness → responsive L1 → CPC verdict`

The CPC skill explicitly separates:
- numerical L1 from responsive L1;
- L1 correctness from price reasonableness;
- critical evidence gaps from correctable documentation gaps;
- common DSC review principles from project/donor/state-specific requirements;
- legitimate procurement concerns from unsupported allegations.

For multi-state procurement, it also checks whether freight, installation, service obligations, delivery locations and landed cost differ by state and whether award is intended centrally, state-wise, lot-wise or item-wise.

### CPC verdicts

- **GREEN** — responsive L1 verified, price reasonably supported, no material gap remains.
- **AMBER** — procurement is supportable subject to explicit correction / clarification before PO or Work Order.
- **RED** — L1/procurement should not presently be approved because critical verification, technical, competition, compliance or price-discovery issues remain.

See [`skills/cpc-review/README.md`](skills/cpc-review/README.md) and [`skills/cpc-review/references/review-checklist.md`](skills/cpc-review/references/review-checklist.md).

## Repository structure

```text
dsc-humanizer/
├── SKILL.md                         # DSC Humanizer
├── README.md
├── VERSION
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── prompts/
│   ├── quick-start.md
│   └── kaushal-voice.md
├── references/
│   ├── ai-patterns-to-reduce.md
│   ├── case-study-style.md
│   ├── donor-report-style.md
│   ├── fact-preservation.md
│   ├── kaushal-voice.md
│   └── technical-writing-style.md
├── tests/
│   └── evaluation-cases.md
└── skills/
    └── cpc-review/
        ├── SKILL.md
        ├── README.md
        ├── prompts/
        │   └── quick-start.md
        ├── references/
        │   └── review-checklist.md
        └── tests/
            └── evaluation-cases.md
```

## Quick use — Humanizer

```text
Use dsc-humanizer.
mode: kaushal-voice
strength: medium
audience: donor / CSR partner

Rewrite:
[paste draft]
```

## Quick use — CPC Review

```text
Use the CPC review skill.
Read all uploaded procurement documents completely before giving any conclusion.
Identify the state, DSC project/unit and funding partner where available.
Give me document gaps, independent responsive-L1 verification, price reasonableness, material CPC observations, GREEN/AMBER/RED verdict, final recommendation, and a short CPC observation for the Purchase Note.
Do not assume missing facts or state/project-specific rules.
```

For re-review after new clarification/documents, or for multi-state procurement, use the recipes in [`skills/cpc-review/prompts/quick-start.md`](skills/cpc-review/prompts/quick-start.md).

## Quality principles

Across both skills:
- facts and source evidence take priority over style or assumptions;
- unsupported conclusions must be labelled as unverified;
- figures, units, dates and qualifiers must be preserved;
- technical terminology should not be diluted into vague language;
- recommendations should be practical and decision-oriented;
- no state-, donor- or project-specific procurement rule should be invented when the governing evidence is absent.

## Versioning

Current repository version: **0.4.0**

This repository follows Semantic Versioning:
- PATCH — wording fixes and small rule improvements;
- MINOR — new skills, modes, domain guides or substantial workflow improvements;
- MAJOR — incompatible redesign of skill interfaces or behaviour.

See [`CHANGELOG.md`](CHANGELOG.md).

## License

MIT License. See [`LICENSE`](LICENSE).
