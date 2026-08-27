---
layout: default
title: Catumaxomab
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 3
---

# Catumaxomab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Catumaxomab: From Malignant Ascites to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Catumaxomab (DrugBank ID: DB06607) is a trifunctional anti-EpCAM × anti-CD3 bispecific antibody originally developed for **malignant ascites** caused by EpCAM-positive carcinomas. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant Ascites (EpCAM-positive carcinoma) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.64% (rank 4336) |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is flagged as a data gap in the source records. Based on the repurposing rationale available in the evidence pack, catumaxomab is known to be a trifunctional bispecific antibody that simultaneously binds EpCAM on tumor cells and CD3 on T-cells, recruiting cytotoxic T-cells and accessory immune cells (via its intact Fc region) to destroy EpCAM-positive tumor cells. Its original approved use was for malignant ascites in EpCAM-positive carcinomas.

Diabetic retinopathy — including the severe nonproliferative stage — is driven by a fundamentally different pathology: chronic hyperglycemia, VEGF-driven microvascular damage, retinal ischemia, and low-grade inflammation. There is no known overlap between T-cell-mediated tumor cytotoxicity and the metabolic/vascular processes underlying diabetic retinopathy.

The evidence pack's own mechanistic assessment explicitly flags this as a low-plausibility, speculative link: the prediction is driven entirely by the TxGNN graph model's score, with no supporting literature, clinical trials, or biological rationale identified. The same caveat applies to the two lower-ranked candidates (drug-induced osteoporosis, rank 2; diabetic retinopathy, rank 3), both of which also lack any mechanistic or clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Catumaxomab is currently **not marketed** in Finland (0 approved authorizations on record); no license or product information is available for this candidate.

---

## Cytotoxicity

Catumaxomab's original approved use (malignant ascites in EpCAM-positive **carcinoma**) qualifies it as an antineoplastic/immuno-oncology agent, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (T-cell-engaging trifunctional bispecific antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has evidence level L5 — model prediction only, with zero supporting clinical trials or literature, and the evidence pack's own mechanistic analysis rates the biological plausibility as very low. Critical safety data (TFDA/Fimea package insert warnings and contraindications) is also flagged as a **Blocking** data gap, meaning no S1 safety pre-assessment can be performed yet.

**To proceed, the following is needed:**
- Package insert / regulatory label data (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Confirmed mechanism of action from DrugBank to properly assess mechanistic plausibility (DG002)
- Emergence of preclinical, mechanistic, or clinical evidence specifically linking EpCAM×CD3-directed T-cell engagement to diabetic retinopathy pathology before this candidate can be re-scored above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

