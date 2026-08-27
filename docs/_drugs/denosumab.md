---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 2
---

# Denosumab
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

# Denosumab: From Bone Loss to Diabetic Retinopathy

## One-Sentence Summary

Denosumab is an anti-RANKL monoclonal antibody; registry data on its original approved indication is unavailable in this jurisdiction (0 authorizations on file), though trial context in this evidence pack points to established use for bone-loss prevention related to androgen-deprivation therapy. The TxGNN model's top prediction is **Severe Nonproliferative Diabetic Retinopathy** (score 99.63%), with a related broader diagnosis, **Diabetic Retinopathy** (score 99.23%), also flagged. Evidence support is currently thin: **1 clinical trial** (a safety-only study, not an efficacy trial) and **2 publications**, none specific to the top-ranked indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry (drug not marketed, 0 authorizations); trial context (NCT00925600) references denosumab used for bone loss due to androgen-deprivation therapy |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy (rank 1); Diabetic Retinopathy (rank 2, broader category) |
| TxGNN Prediction Score | 99.63% (severe NPDR, rank 4411/all predictions) / 99.23% (diabetic retinopathy, rank 7686) |
| Evidence Level | L5 (severe NPDR — model prediction only) / L4 (diabetic retinopathy — indirect/observational) |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Denosumab is an anti-RANKL monoclonal antibody (per the evidence pack's mechanistic rationale). The RANKL/RANK/OPG signaling axis has a theoretical role in retinal vascular disease: osteoprotegerin (OPG) is commonly used as a serum biomarker correlating with diabetic retinopathy severity. This provides a plausible, but not yet demonstrated, mechanistic bridge between denosumab's known pharmacology and the predicted indication.

The link to the original indication is currently only inferable from trial context, not confirmed registry data — denosumab appears to be used for prevention of treatment-related bone loss (e.g., androgen-deprivation therapy) rather than a disease with obvious pathophysiological overlap with diabetic retinopathy. The connection between bone metabolism and retinal microvascular disease is therefore indirect, running through the shared RANKL/OPG pathway rather than shared organ system or original indication.

For the top-ranked candidate (severe nonproliferative diabetic retinopathy), no clinical or preclinical data currently support an actual treatment effect — this remains a pure mechanistic hypothesis (L5). For the broader "diabetic retinopathy" category, real-world cohort data show denosumab use in osteoporosis populations is associated with lower incidence of type 2 diabetes and diabetic foot ulceration versus bisphosphonates, which is an indirect signal but does not report retinopathy-specific outcomes.

---

## Clinical Trial Evidence

*Note: the trial below was identified under the broader "diabetic retinopathy" search and is a safety (not efficacy) study; no trials were found for the top-ranked "severe nonproliferative diabetic retinopathy" indication.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Evaluated new/worsening lens opacification (cataract) in men with non-metastatic prostate cancer receiving denosumab for ADT-related bone loss. This is an ophthalmic **safety** endpoint study, not a diabetic retinopathy efficacy trial (relevance grade C). |

---

## Literature Evidence

*Identified under the broader "diabetic retinopathy" search; none specific to severe nonproliferative diabetic retinopathy.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohort + Meta-analysis | Diabetes, Obesity & Metabolism | Real-world cohort comparing denosumab vs. bisphosphonates in osteoporosis patients: denosumab associated with lower incidence of type 2 diabetes, reduced foot ulceration, and lower all-cause mortality. Microvascular outcomes (incl. retinopathy) were assessed as part of the analysis, but retinopathy-specific effect size is not detailed in the abstract. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Review/Methodology | Cureus | Discusses FRAX fracture-risk assessment in type 2 diabetes populations; general context on fracture risk and anti-osteoporotic therapy in T2DM, not specific to denosumab or retinopathy. |

---

## Finland Market Information

Denosumab is currently **not marketed** in this jurisdiction — 0 authorizations are on file, so no product/dosage-form table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (severe nonproliferative diabetic retinopathy) is supported only by a mechanistic hypothesis with no clinical or preclinical evidence (L5). The broader "diabetic retinopathy" signal (L4) rests on indirect, non-disease-specific real-world cohort data and a single safety-only trial — not efficacy evidence. Combined with the drug's non-marketed status and a complete absence of local safety/warning data, this candidate is not ready to advance beyond a research question.

**To proceed, the following is needed:**
- TFDA/local package insert with warnings, contraindications, and DDI data (currently a Blocking data gap)
- Confirmed original approved indication and mechanism of action from DrugBank or manufacturer labeling (currently a High-severity data gap)
- Disease-specific preclinical or clinical studies directly evaluating denosumab in diabetic retinopathy (ideally severe NPDR), rather than inferred from osteoporosis-population cohorts
- Retinopathy-specific outcome data from the 2024 cohort study (PMID 38899553), beyond the current abstract-level summary
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

