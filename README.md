# DSC Humanizer

A reusable GitHub-based writing skill for professional, technical, donor-facing, and project communication.

**Core rule:** style may change; facts must not.

## What it does

`dsc-humanizer` rewrites AI-assisted or rough drafts into clearer, more natural and credible prose while protecting factual and technical integrity.

It is designed especially for:
- donor and CSR reports;
- water, agriculture, NRM and development-sector documentation;
- technical notes and methodology write-ups;
- case studies and project stories;
- Governing Board and management notes;
- donor observations and compliance responses;
- web articles;
- LinkedIn and professional posts;
- field notes and concise professional communication.

The skill is intended to improve authentic writing quality. It is not designed to bypass AI-detection systems.

## v0.2.0 — Kaushal Voice

Version 0.2.0 adds a dedicated `kaushal-voice` profile based on recurring strengths identified across prior professional writing samples. Project-specific text is not copied into the public profile; the skill captures writing habits instead.

The profile favours:
- evidence before adjectives;
- technical reasoning connected to field conditions;
- practical `context → action → evidence → meaning → next step` flow;
- accurate roles for community institutions and government/convergence partners;
- calm acknowledgement of documentation or implementation gaps;
- explicit distinction between what is measured, estimated, expected, reported, or still to be verified;
- restrained development-sector language;
- Indian English conventions unless another house style is requested.

See [`references/kaushal-voice.md`](references/kaushal-voice.md).

## Repository structure

```text
dsc-humanizer/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── improvement.md
├── prompts/
│   ├── quick-start.md
│   └── kaushal-voice.md
├── examples/
│   └── examples.md
├── references/
│   ├── ai-patterns-to-reduce.md
│   ├── case-study-style.md
│   ├── donor-report-style.md
│   ├── fact-preservation.md
│   ├── kaushal-voice.md
│   └── technical-writing-style.md
└── tests/
    └── evaluation-cases.md
```

## How to use

For an agent or workflow that supports `SKILL.md`-style skills, use this repository as the skill source and load `SKILL.md` as the primary instruction file. The files under `references/` provide additional domain and style guidance.

### General donor-report mode

```text
Use dsc-humanizer.

mode: donor-report
strength: medium
audience: CSR donor
length: same
preserve_terms: water budget, Sujal Samiti, groundwater, water saving

Rewrite:
[paste draft]
```

### Kaushal voice

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: donor / CSR partner
priority: evidence, technical clarity, outcome, implementation quality, next step
preserve_terms: [add project-specific terms]

Rewrite:
[paste draft]
```

For donor observations or compliance responses:

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: donor / reviewer
response_type: observation-response
priority: acknowledge valid gap, explain evidence, distinguish documentation from technical issue where justified, state corrective action

Rewrite:
[paste observation and draft response]
```

More prompt recipes are available in [`prompts/quick-start.md`](prompts/quick-start.md) and [`prompts/kaushal-voice.md`](prompts/kaushal-voice.md).

## Writing modes

| Mode | Best for |
| --- | --- |
| `professional` | General polished professional writing |
| `donor-report` | Evidence-led CSR and donor reporting |
| `technical` | Methods, indicators, calculations and technical notes |
| `case-study` | Human-centred but fact-safe project stories |
| `web-article` | Accessible long-form online content |
| `linkedin` | Concise professional social posts |
| `concise` | Shortening while preserving meaning |
| `field-note` | Practical, grounded field documentation |
| `kaushal-voice` | Evidence-first, technically grounded practitioner writing |

## Editing strength

- **Light** — fixes grammar, repetition, rhythm and obvious AI-style wording while preserving structure.
- **Medium** — rewrites sentences and paragraphs for stronger flow while preserving facts and organisation.
- **Deep** — can reorganise paragraphs and structure while keeping supported facts and technical meaning intact.

Default strength: `medium`.

## Fact-lock principle

Before rewriting, the skill protects:
- names and organisations;
- places and project titles;
- dates and periods;
- numbers, percentages and financial values;
- units, areas, yields and targets;
- formulas and indicators;
- technical terminology;
- quotations and attribution;
- supported causal claims;
- qualifiers such as `estimated`, `expected`, `reported`, `approximately`, `preliminary`, and `may`.

The skill must not turn an activity into an outcome, an output into an impact, or uncertainty into certainty.

See [`references/fact-preservation.md`](references/fact-preservation.md) for the full safeguards.

## Domain-aware writing

The skill includes specific protection for terminology used in water security, agriculture, watershed, NRM, PIM and natural-farming documentation. Terms such as `water budget`, `groundwater`, `static water level`, `crop-water demand`, `adoption area`, `water saving`, `Sujal Samiti`, `Water User Group`, `Measurement Book`, `PRA`, `FGD`, `KPI` and `baseline` should not be replaced with vague language when they carry technical meaning.

## Quality checks

Changes to the skill should be checked against [`tests/evaluation-cases.md`](tests/evaluation-cases.md), including:
- exact preservation of figures and units;
- preservation of technical terminology;
- reduction of inflated AI-style language;
- distinction among activity, output, outcome and impact;
- preservation of uncertainty;
- evidence-first Kaushal-voice writing;
- accountable handling of review observations;
- field-condition reasoning without invented technical evidence;
- accurate institutional roles.

## Versioning

Current version: **0.2.0**

This repository follows Semantic Versioning:
- PATCH — wording fixes and small rule improvements;
- MINOR — new modes, domain guides or substantial workflow improvements;
- MAJOR — incompatible redesign of the skill interface or behaviour.

See [`CHANGELOG.md`](CHANGELOG.md) for release notes.

## Contributing

Improvements are welcome. Please keep the core principle intact: **style may change; facts must not.** Add or update an evaluation case when making meaningful changes to the skill.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT License. See [`LICENSE`](LICENSE).
