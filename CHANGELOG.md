# Changelog

All notable changes to this project will be documented here.

The project follows Semantic Versioning: `MAJOR.MINOR.PATCH`.

## [0.3.0] - 2026-09-11

### Added
- New reusable `skills/cpc-review/` skill for DSC Maharashtra Central Procurement Committee reviews.
- Independent document/source mapping before L1 determination.
- Requirement, quantity, unit, pack-size and scope reconciliation.
- Vendor-wise technical and commercial responsiveness classification.
- Independent arithmetic and landed-cost verification.
- Source quotation vs comparative-statement reconciliation.
- Explicit distinction between numerical L1 and responsive L1.
- Explicit distinction between L1 correctness and price reasonableness.
- GREEN / AMBER / RED verdict gates with approval conditions.
- CPC review checklist, quick-start prompts and regression evaluation cases.
- Re-review workflow for newly submitted clarification/documents.
- CPC observation and optional response-email workflow compatible with `kaushal-voice` tone.

### Changed
- Repository README now acts as an index for multiple professional AI skills rather than only the humanizer skill.
- Repository version bumped to 0.3.0.

## [0.2.0] - 2026-09-10

### Added
- Dedicated `references/kaushal-voice.md` profile derived from recurring strengths in prior professional writing samples.
- Kaushal-voice guidance for donor/CSR reports, technical notes, Governing Board notes, public articles, and compliance/observation responses.
- `prompts/kaushal-voice.md` with reusable prompt recipes.
- Regression cases for evidence-first writing, accountable responses, field-condition reasoning, institutional roles, and Indian English conventions.

### Changed
- Strengthened qualifier preservation for words such as `estimated`, `expected`, `reported`, `approximately`, `preliminary`, and `may`.
- Expanded domain protection to include Water User Groups / Associations and Measurement Books.
- Refined `kaushal-voice` from a generic low-hype mode into an evidence-first, technically grounded, practical, accountable, institution-aware practitioner voice.
- Added explicit activity → output → outcome → impact safeguards to the core workflow.

## [0.1.0] - 2026-09-10

### Added
- Core `SKILL.md` humanization workflow.
- Fact-lock and technical-integrity safeguards.
- Writing modes for professional, donor-report, technical, case-study, web-article, LinkedIn, concise, field-note, and Kaushal voice.
- Light, Medium, and Deep editing strengths.
- Reference guides for donor reporting, technical writing, case studies, fact preservation, and AI-pattern reduction.
- Reusable prompt examples and evaluation cases.
- Contribution and release guidance.
