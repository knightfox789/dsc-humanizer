# Changelog

All notable changes to this project will be documented here.

The project follows Semantic Versioning: `MAJOR.MINOR.PATCH`.

## [0.9.0] - 2026-09-15

### Added
- New reusable `skills/systems-effectiveness-tracking/` skill for organisational effectiveness, programme performance, intervention MEL and wider-system/landscape measurement.
- Four-layer measurement architecture separating organisational health, programme efficiency/delivery, intervention effectiveness and external system condition.
- Stakeholder/decision-first indicator design so metrics are selected for the question they need to answer rather than collected by habit.
- Results-chain mapping across inputs → activities → outputs → outcomes → impacts/system condition.
- Explicit time-horizon and spatial-scale checks, including wet/dry-year, seasonal, plot/farm, village, aquifer, watershed, canal-command and wider-system fit.
- Continuous/repeated-monitoring decision rules for dynamic biophysical and seasonal systems.
- Unintended-consequence and trade-off checks, including rebound/Jevons-type effects, redistribution and zero-sum water constraints.
- Cost-per-output, funding-leverage and SROI safeguards covering benchmark availability, attribution, deadweight, displacement, time horizon and uncertainty.
- Data-system readiness checks covering ownership, metadata, protocols, QA, storage, privacy/ethics, analysis, versioning and archiving.
- GREEN / AMBER / RED / GREY measurement-readiness verdicts.
- Dedicated quick-start prompts for full MEL review, water-security MEL, indicator design, value-for-money review, systems-change progress tracking and Board dashboards.
- Sixteen regression cases covering output/outcome confusion, farm-vs-watershed inference, seasonal timing, continuous monitoring, leverage attribution, SROI misuse, rebound, redistribution, composite-index trade-offs and data-system readiness.

### Changed
- `systems-transition-review` now explicitly hands off critical system conditions to `systems-effectiveness-tracking` when the task is to monitor whether a transition is actually occurring.
- Systems Transition Review README now cross-links the effectiveness-tracking workflow.
- Repository README now indexes effectiveness tracking as a separate reusable skill rather than overloading scale-readiness or Kaushal Voice.
- Kaushal Voice, CPC procurement logic and Water Security Intelligence production rules were intentionally left unchanged by this release because the new learning belongs to a distinct measurement/MEL workflow.
- Repository version bumped to 0.9.0.

## [0.8.0] - 2026-09-15

### Added
- New reusable `skills/systems-transition-review/` skill for pilot-to-scale, institutionalisation and systems-change review.
- Scale-pathway classification: replication/service delivery, production-system/incentive transition, collective-action/trust transition, and hybrid pathways.
- Explicit safeguard that successful pilots do not automatically establish scale readiness.
- Current-state → desired-state system mapping across actors, institutions, markets, policy, infrastructure, technology, data, skills, incentives, trust and relevant biophysical conditions.
- Necessary / enabling / jointly sufficient condition analysis for systems transitions.
- Programme-additionality check separating project contribution from changes already driven by government, technology, markets, demography or other actors.
- Rate-limiting-condition analysis to identify the make-or-break constraint that can block scale even when easier activities succeed.
- Scale-architecture review covering institutional ownership, decision authority, recurring finance, delivery capacity, quality control, data systems, market/policy alignment and collective governance.
- Resource-realism check comparing pilot staffing, subsidy, transaction cost, facilitation intensity and supervision with the proposed scale model.
- GREEN / AMBER / RED / GREY scale-readiness verdicts.
- Dedicated quick-start prompts for full scale review, water/groundwater, agriculture/natural farming, collective action and scale-claim auditing.
- Fourteen regression cases covering gold-plated pilots, replication, market/incentive constraints, aquifer governance, programme additionality, rate-limiters, institutional ownership, distributed facilitation and hydrological system boundaries.

### Changed
- Water Security Intelligence now invokes the Systems Transition Review lens only when consequential claims concern scale, systems change, institutionalisation, replication, collective governance or government uptake.
- Water Security Intelligence quality gates now require a stated mechanism and evidence for consequential scale/system claims rather than treating promising local results as proof of scale.
- Repository README now indexes the Systems Transition Review as a separate skill instead of overloading Kaushal Voice.
- `CONTRIBUTING.md` now reflects the repository's multi-skill architecture and directs contributors to update the most appropriate skill rather than defaulting every learning to the root Humanizer or Kaushal Voice.
- CPC procurement logic and Kaushal Voice were intentionally left unchanged by this release because the new learning belongs to a distinct programme-strategy workflow.
- Repository version bumped to 0.8.0.

## [0.7.0] - 2026-09-15

### Added
- Execution-realism layer to `kaushal-voice` so effort estimates consider planning, review, coordination, documentation, administration, supervision, troubleshooting and technical delivery rather than only the visible task.
- 70–30 systems heuristic for balancing direct project-output delivery with strategic bridge work toward outcomes, institutional uptake, continuation and scale.
- Explicit rule that 70–30 is a planning heuristic rather than a mandatory staffing or budget allocation.
- `Think roadmap, act project` logic connecting project outputs to intended users/owners, next decisions, institutional adoption and longer programme or systems objectives.
- Documentation-as-delivery guidance for capturing methods, field adaptations, decisions, failures, conditional lessons and reusable implementation knowledge during execution.
- Activity-based resource logic linking deliverables → activities → person-days/resources → assumptions → timing/phasing → cost.
- Budget/scope integrity safeguard: material resource reductions should trigger transparent review of activities, quality controls, milestones and scope assumptions rather than hidden under-budgeting.
- New Kaushal Voice prompt modes: `execution-realism`, `systems-roadmap` and `activity-based-resource`.
- Regression cases for hidden execution effort, deferred documentation, rigid 70–30 use, budget cuts with unchanged scope, and unsupported claims of scale.

### Changed
- Expanded Kaushal Voice from evidence-first analytical communication into an evidence-first, execution-realistic and systems-aware practitioner profile.
- Root DSC Humanizer now invokes execution and systems checks when Kaushal Voice is used for staffing, planning, budgeting, sustainability or scale.
- Governing Board, donor, technical and workplan guidance now distinguishes project delivery from the strategic bridge required for uptake and longer-term outcomes.
- Repository version bumped to 0.7.0.

## [0.6.0] - 2026-09-15

### Added
- Research-quality reasoning layer to `kaushal-voice` covering descriptive, comparative, associational, causal and projected/modelled evidence classes.
- Explicit safeguard against strengthening claims beyond what the research design, data or calculation supports.
- Comparison-validity checks for group selection, units, periods, indicator definitions, crop/specification differences and other material confounders.
- Denominator and aggregation discipline for percentages, rates, per-unit indicators and village/block/programme roll-ups.
- Guidance to distinguish observed treated-versus-untreated differences from defensible causal attribution.
- Data-storytelling sequence: question → evidence → valid comparison → calculation → interpretation → limitation → decision implication → visual/story.
- Visual-question-fit guidance for time series, maps, dumbbells, scatterplots, heatmaps, bars and tables.
- New Kaushal Voice prompt modes for research-quality analysis and dashboard/data-storytelling work.
- Regression cases covering causal overreach, denominator mismatch, weak comparison groups, temporal-vs-spatial visual choice and dashboard storytelling.

### Changed
- Expanded Kaushal Voice from an evidence-first writing profile into an evidence-first practitioner reasoning and analytical-communication profile.
- Preferred paragraph logic now supports `Context → Action → Evidence → Meaning → Limitation → Next step` when a material limitation exists.
- Donor, technical, management, public-article and dashboard guidance now requires clearer separation of fact, inference, uncertainty and attribution.
- Repository version bumped to 0.6.0.

## [0.5.0] - 2026-09-11

### Added
- CPC procurement-intelligence data layer using Git-versioned CSV source tables.
- `procurement_reviews.csv`, `item_quotes.csv`, `awards.csv`, item/vendor masters and item-alias normalization.
- Generated `master_item_history.csv` for fast recurring-item benchmarking.
- `comparison_config.json` with a 24-month default window and 10/20/30% variance review bands.
- Historical comparison engine showing latest/median/mean/min/max rates, same-state vs DSC-wide counts, variance flags and comparison confidence.
- Automatic master-update script with controlled benchmark eligibility.
- End-to-end pipeline script for compare → finalize → master update → Excel rebuild.
- Structured JSON review-record schema and template.
- Generated `CPC_Master_Procurement_Register.xlsx` analyst workbook.
- GitHub Actions validation workflow and unit tests.
- Procurement-intelligence reference guidance and historical-comparison rules.

### Changed
- CPC review now checks historical master data for recurring items before final verdict when reliable comparables exist.
- CPC output adds a dedicated Historical Price Intelligence section.
- Historical variance is explicitly a review signal, not an automatic rejection rule.
- Only finalized/approved awards normally become benchmark-eligible records.
- Repository version bumped to 0.5.0.

## [0.4.0] - 2026-09-11

### Changed
- Generalised the CPC Review skill from Maharashtra-specific use to **all DSC project states, units, programmes and funding partners**.
- Added explicit state / project / unit / donor context identification at the start of every procurement review.
- Added rule that state-, donor- and project-specific procurement requirements must be evidenced rather than assumed.
- Added multi-state procurement logic for freight, installation, service obligations, delivery locations, landed cost and award structure.
- Added cross-state price-comparison safeguards so historical rates from one state are not treated as automatic caps in another.
- Updated CPC README, quick-start prompts, review checklist and evaluation cases for DSC-wide use.
- Added regression tests for Gujarat, Madhya Pradesh, Rajasthan, cross-state benchmarking and multi-state procurement.
- Repository version bumped to 0.4.0.

## [0.3.0] - 2026-09-11

### Added
- New reusable `skills/cpc-review/` skill for DSC Central Procurement Committee reviews.
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
