# DSC Humanizer

A reusable GitHub-based writing skill for professional, technical, donor-facing, and project communication.

## What it does

`dsc-humanizer` improves AI-assisted or rough drafts while protecting factual and technical integrity.

It is designed especially for:
- donor reports;
- water and agriculture project documentation;
- technical notes;
- case studies;
- project stories;
- web articles;
- LinkedIn posts;
- professional communications.

## Repository structure

```text
dsc-humanizer/
├── SKILL.md
├── README.md
├── LICENSE
├── examples/
│   └── examples.md
└── references/
    ├── donor-report-style.md
    ├── technical-writing-style.md
    ├── case-study-style.md
    ├── ai-patterns-to-reduce.md
    └── fact-preservation.md
```

## Recommended prompt

```text
Use the dsc-humanizer skill.

mode: donor-report
strength: medium
audience: CSR donor
length: same
preserve_terms: water budget, Sujal Samiti, groundwater, water saving

Rewrite:
[paste draft]
```

## Modes

- professional
- donor-report
- technical
- case-study
- web-article
- linkedin
- concise
- field-note
- kaushal-voice

## Editing strengths

- Light — grammar, repetition, rhythm
- Medium — sentence and paragraph rewrite
- Deep — structural rewrite while protecting facts

## Design philosophy

This skill is designed for authentic and credible writing. It does not exist to bypass AI-detection systems.

The strongest rule is simple: **style may change; facts must not.**
