---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Normal Breast-like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab emtansine (T-DM1, marketed as Kadcyla) is an antibody-drug conjugate approved internationally for HER2-positive breast cancer.
The TxGNN model predicts it may be effective for **normal breast-like subtype of breast carcinoma**,
but this direction is currently supported by only **1 clinical trial** and **no published literature**, and the mechanistic link to this specific molecular subtype is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive (HER2+) breast cancer (Kadcyla) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information, trastuzumab emtansine is an antibody-drug conjugate (ADC) that links trastuzumab, a monoclonal antibody targeting HER2, to DM1, a maytansinoid microtubule inhibitor. Its efficacy depends on HER2 overexpression (IHC3+/FISH+) in tumor cells, and it is currently used under the brand Kadcyla for HER2-positive breast cancer.

"Normal breast-like" is a PAM50 intrinsic molecular subtype classification, defined by gene-expression profiling rather than HER2 receptor status. This is a different classification axis from HER2 positivity, which is the actual determinant of T-DM1 activity. According to the evidence pack's own mechanistic assessment, the link between T-DM1 and the normal-like subtype is "indirect and unclear," since normal-like tumors are not defined by, and do not reliably correlate with, HER2 overexpression.

As a result, while the TxGNN prediction score is very high (99.82%), the underlying biological rationale is weaker than for HER2-status-based predictions. This is reflected in the low evidence level (L4) and the single supporting trial, which only broadly addresses anti-HER2 therapy in HER2+ breast cancer without specifically confirming a T-DM1 arm or normal-like subtype enrollment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Evaluates efficacy and safety of anti-HER2-based therapy (neoadjuvant to adjuvant) in Nigerian women with HER2+ breast cancer; does not confirm a specific T-DM1 arm or normal-like subtype focus (relevance grade B). |

## Literature Evidence

Currently no related literature available

## Finland Market Information

This drug is currently not marketed in Finland (未上市), and no market authorization records are available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate with a cytotoxic maytansinoid payload, DM1) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (normal breast-like subtype) has a very high TxGNN score but a weak and indirect mechanistic basis, minimal clinical trial support (1 trial, relevance grade B), and no supporting literature — insufficient to advance. Notably, other predicted indications for this drug (PR-positive and PR-negative breast cancer) show much stronger evidence (L1–L2, multiple direct T-DM1 trials and literature) but largely overlap with the drug's existing HER2-positive breast cancer indication rather than representing genuine repurposing.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a blocking data gap
- DrugBank mechanism of action (MOA) data to strengthen mechanistic-relevance analysis
- Confirmation of whether any T-DM1 trials specifically enroll or stratify by PAM50 normal-like subtype
- Additional literature search specific to T-DM1 and normal-like/basal molecular subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

