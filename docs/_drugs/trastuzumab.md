---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Normal Breast-like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab is an anti-HER2 humanized monoclonal antibody originally developed for HER2-overexpressing breast and gastric cancer. The TxGNN model's top-ranked prediction for this drug is the **normal breast-like subtype of breast carcinoma**, but this subtype is molecularly defined by the *absence* of a dominant HER2-driven phenotype, and the supporting evidence (**12 clinical trials, 1 publication**) is drawn from general HER2-positive breast cancer trials rather than subtype-specific studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-overexpressing breast cancer (established public labeling; no TFDA/local license text available in this evidence pack) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as data gap DG002, High severity). Based on known public information, trastuzumab binds the extracellular domain of HER2/ERBB2, blocking downstream proliferative signaling and mediating antibody-dependent cellular cytotoxicity (ADCC) against HER2-overexpressing tumor cells. This mechanism has been proven effective in HER2-positive breast and gastric cancer.

However, the "normal breast-like" subtype identified by gene-expression profiling is, by definition, characterized by low proliferation and a gene expression profile resembling normal breast epithelium rather than HER2 overexpression. As the model's own rationale states, this subtype has no direct mechanistic link to trastuzumab's HER2-targeting activity.

The clinical trials retrieved in support of this prediction are all general HER2-positive neoadjuvant/metastatic breast cancer trials — none were designed to specifically enroll or stratify by the normal-like molecular subtype. The single supporting publication is a morphological review of basal-like carcinoma that only tangentially references the five intrinsic subtype classification. Taken together, the prediction appears to be a model-level association driven by the broader "breast carcinoma" disease class rather than a subtype-specific mechanistic signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine + chemotherapy + HER2-targeted mAb as neoadjuvant therapy in breast cancer |
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Phase 2 | Active, not recruiting | 55 | Atezolizumab + trastuzumab + vinorelbine in HER2+ advanced/metastatic BC, focusing on ER-negative/non-luminal cohorts |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Drug-screening-guided neoadjuvant therapy strategy for HER2-positive early breast cancer |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant paclitaxel ± carboplatin in triple-negative (largely basal-like) breast cancer; not specific to normal-like subtype |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Phase 3 | Withdrawn | 0 | T-DXd vs CDK4/6 inhibitors in non-Luminal A, ER-positive/HER2-low metastatic breast cancer |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Phase 1/2 | Unknown | 120 | Hydroxychloroquine combined with antibody-drug conjugate vs ADC alone in advanced breast cancer |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab as preoperative therapy for inflammatory breast cancer |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | T-DXd vs standard preoperative treatment with biology-driven neoadjuvant selection in HER2+ breast cancer |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib ± fulvestrant in metastatic HER2 non-amplified but HER2-mutant breast cancer |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Efficacy/safety of optimal neoadjuvant-to-adjuvant anti-HER2 therapy in Nigerian women with HER2+ breast cancer |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Review | Breast Cancer (Tokyo, Japan) | Reviews morphological/cytopathological features of the basal-like subtype among the five intrinsic breast carcinoma subtypes (including normal breast-like); does not address trastuzumab treatment of the normal-like subtype specifically |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; ADCC-mediated, non-cytotoxic-chemotherapy mechanism) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (normal breast-like subtype) has only L4 evidence — all supporting trials target general HER2-positive breast cancer populations, not this specific molecular subtype, and the subtype's biology (low proliferation, non-HER2-driven) directly conflicts with trastuzumab's mechanism of action. Additionally, TFDA safety data (warnings/contraindications) is a Blocking-severity data gap, which prevents this candidate from advancing to the S1 safety pre-assessment stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (Blocking gap, DG001)
- Verified mechanism of action data from DrugBank (High-priority gap, DG002)
- Molecular/HER2-status characterization confirming whether "normal breast-like" patients in the cited trials actually carry HER2 amplification
- Dedicated trials or subgroup analyses specific to the normal-like intrinsic subtype

**Note:** Within this same evidence pack, two other predicted indications show materially stronger support and may be more promising repurposing candidates: *progesterone-receptor negative breast cancer* (rank 3, L1 evidence — includes a completed Phase 3 RCT with n=3,270 — "Proceed with Guardrails") and *progesterone-receptor positive breast cancer* (rank 2, L2 evidence, "Proceed with Guardrails"), both of which align mechanistically with trastuzumab's approved HER2-positive breast cancer indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

