---
layout: default
title: Diroximel Fumarate
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the evidence pack directly (no external lookups) since `original_indications` is empty and MOA/safety fields are explicit data gaps — I'm not filling those in from outside knowledge.

# Diroximel Fumarate: From Undocumented Original Indication to Diabetic Cataract

## One-Sentence Summary

The evidence pack does not document diroximel fumarate's original approved indication or detailed mechanism of action (both flagged as data gaps), and the drug is not currently marketed in Finland. The TxGNN model predicts potential effectiveness for **Diabetic Cataract**, but this and all nine other ranked ocular indications are currently supported by **zero clinical trials** and **zero publications** — the prediction is a pure model-score hypothesis with no external validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.9993% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank returned no MOA text for this drug). Based on the mechanistic rationale included in this evidence pack, diroximel fumarate's active metabolite, monomethyl fumarate (MMF), is understood to activate the Nrf2-ARE antioxidant pathway. This same pathway is proposed as the theoretical link across all ten TxGNN-predicted indications, which cluster almost entirely around cataract subtypes and diabetic retinopathy.

Because `original_indications` is empty in the evidence pack, the relationship between the drug's original approved use and diabetic cataract cannot be assessed from the data available here.

Mechanistically, diabetic cataract formation is associated with oxidative aggregation of lens crystallin proteins under hyperglycemic stress. Nrf2 pathway activation could theoretically reduce this oxidative damage, which is why the model surfaces this as a plausible signal. However, the rationale itself explicitly notes this is an indirect, unproven mechanistic hypothesis — there is no ophthalmic preclinical or clinical evidence confirming that systemically administered diroximel fumarate reaches therapeutic concentrations in lens or retinal tissue.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Diroximel fumarate is not currently marketed in Finland (0 authorizations on record); no license data is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a TxGNN model score (L5) with no supporting clinical trials, literature, or preclinical ocular data, and the drug is not marketed in Finland. Core drug-level facts — original indication, confirmed MOA, and TFDA safety/label data — are all unresolved data gaps (DG001 is flagged Blocking, DG002 High), so the candidate cannot yet enter safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications, DDI) — currently Blocking per DG001
- Confirmed original indication and mechanism of action from DrugBank or regulatory source — DG002
- Preclinical evidence that systemic dosing achieves Nrf2-pathway activation in lens/retinal tissue
- Any in vitro or animal data on antioxidant effect in diabetic cataract or retinopathy models
- Route-of-administration feasibility assessment for ocular target engagement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

