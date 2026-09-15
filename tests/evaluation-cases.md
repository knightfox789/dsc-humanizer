# Evaluation cases

Use these cases whenever the skill changes.

## 1. Fact preservation

Input:
> In 2026, 428 farmers adopted micro-irrigation across 612.5 ha, resulting in an estimated annual water saving of 1.83 MCM.

Pass criteria:
- 2026 remains 2026.
- 428 remains 428.
- 612.5 ha remains 612.5 ha.
- 1.83 MCM remains 1.83 MCM.
- `estimated` remains qualified.
- No new causal explanation is invented.

## 2. Technical terminology

Input:
> Static water level and pumping water level were monitored in selected open wells and borewells.

Pass criteria:
- SWL/PWL concepts are not replaced with vague terms such as `water conditions`.
- Monitoring method is not expanded beyond the source.

## 3. Remove inflated language

Input:
> The transformative intervention played a pivotal role in empowering communities and fostering sustainable water stewardship.

Pass criteria:
- Inflated claims are reduced.
- The rewrite does not add outcomes that are absent from the input.

## 4. Activity vs outcome

Input:
> The project conducted 25 trainings attended by 640 farmers.

Pass criteria:
- Output is stated accurately.
- The rewrite does not claim adoption, behaviour change, income increase, resilience, or impact unless supplied.

## 5. Uncertainty

Input:
> Preliminary field observations suggest that irrigation frequency may have declined in some demonstration plots.

Pass criteria:
- `preliminary`, `suggest`, `may`, and `some` are not strengthened into certainty.

## 6. Kaushal voice — evidence before adjectives

Input:
> The project made remarkable progress in water security. Water Security Plans were reviewed in 150 villages during the year.

Pass criteria:
- The 150-village evidence is made more prominent than `remarkable progress`.
- `remarkable` is removed or justified rather than repeated automatically.
- No additional water-security result is invented.

## 7. Kaushal voice — accountable observation response

Input:
> Stage-wise dates were not recorded in the Measurement Book. The measured quantities are available in the engineering records and the dates can be checked against execution records.

Pass criteria:
- The omission is acknowledged directly.
- The rewrite does not become defensive.
- It distinguishes documentation completeness from measured quantities only to the extent supported by the input.
- It does not claim that the omission had `no impact` unless evidence for that conclusion is supplied.
- A reasonable corrective action may be stated only if it follows from the provided text or is requested by the caller.

## 8. Kaushal voice — field condition and technical reasoning

Input:
> Excavation of the central foundation was deferred during the monsoon to keep a drainage passage open. The remaining work will be taken up after safe drainage is ensured.

Pass criteria:
- The practical site reason remains visible.
- The rewrite does not add design calculations, flood data, or safety certification that are not in the source.
- The sequence of condition, decision, and next step remains clear.

## 9. Kaushal voice — institution role

Input:
> The Sujal Samiti reviewed the village water budget and discussed demand-side and supply-side priorities before preparation of the Water Security Plan.

Pass criteria:
- Sujal Samiti, water budget, demand-side, supply-side, and Water Security Plan remain intact.
- The institution's role is described accurately rather than converted into a generic `community empowerment` claim.

## 10. Indian English conventions

Input:
> The programme organised farmer training and measured the structure in metres.

Pass criteria:
- When no alternative house style is requested, `programme`, `organised`, and `metres` may be retained.
- Units are not converted automatically.

## 11. Kaushal voice — descriptive versus causal claim

Input:
> Treated farmers recorded an average irrigation depth of 350 mm, compared with 430 mm among untreated farmers.

Pass criteria:
- The rewrite may state that treated farmers recorded lower irrigation depth in the observed sample.
- It must not automatically say the intervention `reduced irrigation by 18%` or `caused water saving`.
- If relevant context is absent, crop, soil, water source, farmer characteristics, season or selection effects may be flagged as possible confounders rather than invented as explanations.

## 12. Kaushal voice — denominator and aggregation discipline

Input:
> Village A saved 10% water across 100 ha and Village B saved 30% across 10 ha. The programme average water saving was reported as 20%.

Pass criteria:
- The skill recognises that a simple average of percentages may be misleading because denominators differ.
- It does not silently replace the reported 20% unless underlying numerators/denominators permit a defensible recalculation.
- It may state that programme-level aggregation should use underlying totals or an appropriate weighted method.

## 13. Kaushal voice — comparison validity

Input:
> Yield in the demonstration group was higher than the comparison group. The demonstration farmers mainly grew wheat, while the comparison group included wheat and mustard.

Pass criteria:
- The difference may be described.
- The crop-composition difference is retained as a material comparability limitation.
- The rewrite does not attribute the full yield difference to the intervention.

## 14. Kaushal voice — visual-question fit

Input:
> A GIS map was prepared to show how groundwater levels changed from 2024 to 2026 across 150 villages.

Pass criteria:
- The skill asks what the analytical question is.
- If the main question is temporal change, it may recommend time-series or small-multiple views rather than assuming the map is sufficient.
- A map may still be retained if the spatial pattern of change is itself important.
- Visual choice is justified by the question, not by the availability of GIS data.

## 15. Kaushal voice — evidence-to-decision storytelling

Input:
> The dashboard contains 24 charts on rainfall, groundwater, crop area, irrigation depth, adoption, water saving and additional production.

Pass criteria:
- The rewrite or analytical guidance does not simply narrate all 24 charts.
- It identifies the decision-relevant question, strongest evidence, comparison, limitation and implication.
- It favours a small number of defensible messages over a chart-by-chart description.

## 16. Kaushal voice — execution effort realism

Input:
> The analysis itself will take two days. The estimate does not include data cleaning, review meetings, revisions, documentation or coordination with the field team.

Pass criteria:
- The skill does not treat two days as the full delivery effort.
- It identifies the omitted categories as part of the work required to complete the deliverable properly.
- It does not invent a multiplier, hours or person-days that are not supported by the source.
- It may recommend estimating the omitted effort from calendar records, prior experience or explicit assumptions.

## 17. Kaushal voice — documentation is part of delivery

Input:
> The team plans to document lessons after the project closes. Field adaptations and implementation decisions are currently not being recorded systematically.

Pass criteria:
- The skill recognises a risk of losing implementation learning if documentation is deferred entirely.
- It may recommend capturing material decisions, methods and lessons alongside implementation.
- It does not require unnecessary publication work or invent a documentation schedule.
- Documentation is framed as preserving accountability and learning value, not as decorative communication.

## 18. Kaushal voice — 70–30 is a heuristic, not a formula

Input:
> Apply exactly 70% of staff time to project outputs and exactly 30% to strategy in every DSC project.

Pass criteria:
- The skill does not impose the ratio as a universal rule.
- It explains that 70–30 is a planning heuristic for balancing project delivery with strategic bridge work.
- It allows the balance to vary by project stage, duration, role, funding model and operating context.
- It keeps strategic work tied to a clear mission, roadmap or pathway to uptake/scale.

## 19. Kaushal voice — resource cut and scope integrity

Input:
> The donor has reduced the available budget by 15%, but the note assumes the same activities, quality controls, milestones and deliverables will be maintained without change.

Pass criteria:
- The skill flags the need to review effort, scope, phasing or delivery assumptions.
- It does not automatically claim the project is impossible or that scope must reduce by exactly 15%.
- It makes the resource-to-activity-to-deliverable trade-off transparent.
- It avoids hiding under-budgeting behind optimistic language.

## 20. Kaushal voice — project output to systems bridge

Input:
> The pilot model is complete and the report has been submitted. The draft says the model will now scale across the state, but it does not identify who will adopt it, finance it, approve it or maintain it.

Pass criteria:
- The skill does not describe state-wide scale as established.
- It asks for or states the missing bridge: institutional owner, decision, financing, capability, evidence or implementation mechanism.
- It distinguishes completed project output from demonstrated uptake or scale.
- It may frame the pilot as a building block in a longer roadmap if the source supports that interpretation.
