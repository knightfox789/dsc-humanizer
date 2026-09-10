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
