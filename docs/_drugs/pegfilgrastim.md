---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Pegfilgrastim: From Chemotherapy-Induced Neutropenia to Severe Nonproliferative Diabetic Retinopathy

> **Note on localization:** The evidence pack for this candidate (`TW-DB00019-multi`) is Taiwan-scoped (`taiwan_regulatory`, TFDA data gaps in `meta.data_gaps`), so this report uses Taiwan/TFDA terminology rather than the Finland/Fimea labels in the report template.

## One-Sentence Summary

Pegfilgrastim is a pegylated recombinant G-CSF used to support neutrophil recovery in patients receiving myelosuppressive chemotherapy. The TxGNN model predicts a possible link to **severe nonproliferative diabetic retinopathy (NPDR)**, but the supporting rationale itself flags a **mechanistically opposing, potentially harmful** direction (promotion rather than suppression of pathological neovascularization), and there are currently **zero clinical trials and zero publications** supporting this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (`original_indications` is empty; TFDA package insert is a Blocking data gap — DG001). Pegfilgrastim's internationally recognized use is prophylaxis of chemotherapy-induced (febrile) neutropenia. |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% (rank 1638) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` = data gap, DG002). Based on the mechanistic notes accompanying this prediction, pegfilgrastim is a G-CSF receptor agonist whose primary pharmacological action is to mobilize bone-marrow granulocyte precursors and endothelial progenitor cells (EPCs) into systemic circulation.

The relationship between the original use (supporting neutrophil counts during chemotherapy) and the predicted new indication (severe NPDR, a pre-proliferative stage of diabetic retinopathy) is not a straightforward "same mechanism, new disease" story. According to the rationale provided with this prediction, EPC/granulocyte mobilization is more commonly associated in the literature with **promoting** pathological retinal neovascularization — the exact process severe NPDR is at high risk of progressing toward — rather than treating it. In other words, the mechanistic link supports a plausible **safety concern (accelerating progression to proliferative disease)** rather than a therapeutic rationale.

Given this, the high TxGNN score likely reflects an indirect disease–gene/receptor co-occurrence pattern in the knowledge graph rather than a causal or directionally supportive treatment relationship. This is explicitly noted as a case where the model's confidence should **not** be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (0 results from ClinicalTrials.gov and ICTRP for both "severe nonproliferative diabetic retinopathy" and "diabetic retinopathy" queries, dated 2026-04-20).

---

## Literature Evidence

Currently no related literature available (0 PubMed results for both associated disease terms, queried 2026-04-20).

---

## Taiwan Market Information

Pegfilgrastim currently has **no marketing authorization in Taiwan** (`market_status`: 未上市; `total_licenses`: 0; `licenses`: none on file). No product name, dosage form, or approved indication text is available to extract.

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this evidence pack — key warnings, contraindications, and DDI — are currently data gaps; the TFDA package insert data gap (DG001) is flagged as **Blocking**, meaning a formal S1 safety pre-assessment cannot proceed until it is resolved.)

---

## Additional Note: Related Predicted Indication

A second, closely related prediction — **diabetic retinopathy** (general, unspecified severity) — scored 99.73% (rank 3482), also L5, also with no clinical trials or literature, and carries the same mechanistic caution as above (potential promotion rather than treatment of retinal neovascularization). It is not pursued separately here since it overlaps in disease category and evidence status with the primary candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has L5 evidence only (model prediction, no clinical trials, no literature), and the mechanistic rationale itself raises a plausible safety concern — that G-CSF-driven progenitor cell mobilization could **accelerate** rather than treat neovascular progression in diabetic retinopathy. Combined with the Blocking data gap on TFDA safety labeling, there is currently no basis to advance this candidate beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) to resolve Blocking gap DG001, required before any S1 safety pre-assessment
- Confirmed original mechanism of action from DrugBank to resolve gap DG002, and to properly assess directionality of the G-CSF/retinal-neovascularization relationship
- Preclinical or mechanistic studies specifically examining pegfilgrastim's effect on diabetic retinopathy progression (both risk and potential benefit directions), since none currently exist
- Confirmation of pegfilgrastim's original approved indication and Taiwan licensing status (currently absent from this evidence pack)
- If this candidate is retained for monitoring, an explicit pharmacovigilance flag for retinal/ophthalmologic adverse events given the safety-concern hypothesis raised above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

