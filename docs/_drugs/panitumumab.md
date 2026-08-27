---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 2
---

# Panitumumab
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

# Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Panitumumab is a fully human IgG2 monoclonal antibody targeting EGFR, historically used in metastatic colorectal cancer. TxGNN predicts two novel indications — **Drug-Induced Osteoporosis** (top-ranked) and **Severe Nonproliferative Diabetic Retinopathy** — but neither is currently supported by any registered clinical trials or published literature, so both remain purely model-driven hypotheses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (based on known EGFR-inhibitor pharmacology; structured original-indication data not available) |
| Predicted New Indication | Drug-Induced Osteoporosis (primary candidate); Severe Nonproliferative Diabetic Retinopathy (secondary candidate) |
| TxGNN Prediction Score | 99.13% (Drug-Induced Osteoporosis); 99.05% (Severe Nonproliferative Diabetic Retinopathy) |
| Evidence Level | L5 (both candidates) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for panitumumab is not available in the structured evidence pack. Based on known pharmacological information, panitumumab is a fully human IgG2 monoclonal antibody directed against the epidermal growth factor receptor (EGFR), and its efficacy in metastatic colorectal cancer is well established in clinical practice.

For **Drug-Induced Osteoporosis**, the rationale rests on a theoretical, indirect signaling link — EGFR pathway activity has been discussed in some basic research on osteoclast/osteoblast differentiation. However, this connection has not been demonstrated for EGFR-targeted monoclonal antibodies specifically, and "drug-induced osteoporosis" as a clinical entity is typically associated with agents like corticosteroids rather than EGFR inhibitors. Whether panitumumab would act as a causative factor or a therapeutic candidate for this condition is itself unclear, making the mechanistic link weak and directionally ambiguous.

For **Severe Nonproliferative Diabetic Retinopathy**, the rationale draws on theoretical crosstalk between EGFR and VEGF signaling in angiogenesis regulation, suggesting EGFR inhibition could plausibly modulate pre-proliferative retinal vascular changes. This too is a pathway-level inference only — a high TxGNN score does not equate to mechanistic validation — and there is no animal, case-report, or clinical data addressing intraocular pharmacokinetics or the immune-related/ocular safety profile of systemic panitumumab in this context.

Both candidates should be treated as early-stage, hypothesis-generating signals rather than mechanistically validated leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for either Drug-Induced Osteoporosis or Severe Nonproliferative Diabetic Retinopathy).

---

## Literature Evidence

Currently no related literature available (for either Drug-Induced Osteoporosis or Severe Nonproliferative Diabetic Retinopathy).

---

## Finland Market Information

Panitumumab currently has no marketing authorizations recorded in Finland (0 licenses on file; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Low (mAb-targeted therapies generally carry lower myelosuppression risk than conventional cytotoxic chemotherapy; specific hematologic toxicity data not available) |
| Emetogenicity Classification | Low (typical of monoclonal antibody infusions) |
| Monitoring Items | Serum magnesium and electrolytes (EGFR inhibitors are associated with hypomagnesemia), skin toxicity/dermatologic assessment, infusion-related reaction monitoring |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by TxGNN model scores (L5 evidence) with no clinical trials, no published literature, and mechanistic rationales that are speculative and, in the case of osteoporosis, directionally ambiguous. There is currently no basis for advancing either candidate beyond exploratory research.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a **Blocking** data gap
- Confirmed mechanism-of-action data from DrugBank or primary literature — currently a **High**-severity data gap
- Preclinical or mechanistic studies directly linking EGFR inhibition to bone metabolism (for the osteoporosis candidate) or retinal vascular outcomes (for the diabetic retinopathy candidate)
- Drug-drug interaction (DDI) profile, which is currently unavailable ("not_found")
- Reassessment once any clinical trial or literature signal emerges for either indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

