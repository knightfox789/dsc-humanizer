# Contributing

## What belongs in this repository

Changes should improve one or more of the following:
- clarity and factual integrity;
- natural professional writing and communication;
- research and analytical reasoning;
- domain-aware review behaviour;
- programme, systems or decision-quality reasoning;
- procurement intelligence and other structured professional workflows;
- reproducibility, auditability, tests or reusable skill documentation.

A new rule or skill should solve a real recurring professional problem. Do not add complexity simply because a concept is interesting.

## Core rules

**Style may change; facts must not.**

**Reasoning must not be stronger than the evidence.**

Do not introduce rules whose main purpose is to evade AI-detection systems. The repository is intended to improve authentic professional work, analytical quality and repeatable decision support.

## Suggested workflow

1. Identify the most appropriate existing skill before changing the root Humanizer or Kaushal Voice.
2. If the learning represents a distinct recurring workflow, prefer a separate skill under `skills/<skill-name>/` rather than overloading an unrelated skill.
3. Update `SKILL.md` or the relevant reference/workflow file.
4. Add or revise at least one evaluation case for any material behaviour change.
5. Check that names, figures, dates, units, technical terms, evidence classes and supported claims remain unchanged unless the task explicitly authorises correction.
6. Check interactions with other repository skills and update cross-references only where the workflow genuinely overlaps.
7. Update `README.md`, `CHANGELOG.md` and `VERSION` when the change is user-visible or adds a new skill.
8. Do not modify unrelated skills merely to keep versions or wording symmetrical.

## Skill architecture

Prefer clear ownership of reasoning:
- root `SKILL.md` — professional rewriting/humanisation and shared fact-preservation behaviour;
- `references/kaushal-voice.md` — Kaushal's professional voice and practitioner reasoning profile;
- `skills/cpc-review/` — procurement review and procurement intelligence;
- `skills/water-security-intelligence/` — weekly water-sector research and publication workflow;
- `skills/systems-transition-review/` — pilot-to-scale and systems-transition review.

New skills should normally include:
- `SKILL.md`;
- a concise `README.md`;
- reusable prompts when helpful;
- evaluation cases for material reasoning behaviour.

## Versioning

- PATCH: wording fixes, examples, small rule improvements.
- MINOR: new skill, new reasoning mode, new domain reference, or substantial workflow improvement.
- MAJOR: incompatible redesign of a skill interface, repository architecture or expected behaviour.
