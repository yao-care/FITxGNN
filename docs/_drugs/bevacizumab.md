---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: From Advanced Solid Tumors to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab (DB00112) is a recombinant humanized anti-VEGF-A monoclonal antibody, globally used as part of combination regimens for various VEGF-driven solid tumors. The TxGNN model predicts it may be effective for **Epiglottis Neoplasm** (its highest-scoring candidate, score 0.9990), but this evidence pack currently contains **zero clinical trials** and **zero publications** specific to this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`original_indications` empty; Finland: unmarketed, no license record) |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (`original_moa`: Data Gap DG002). Based on known information, bevacizumab is a monoclonal antibody that binds and neutralizes vascular endothelial growth factor-A (VEGF-A), blocking angiogenesis; it is globally used as part of combination chemotherapy regimens across a range of VEGF-driven solid tumors (e.g., metastatic colorectal cancer, non-squamous NSCLC, renal cell carcinoma, ovarian cancer, cervical cancer, glioblastoma). No Finland-specific marketing authorization exists in this evidence pack (`market_status`: 未上市 / Not Marketed, 0 licenses).

For epiglottis neoplasm specifically, the evidence pack contains no clinical trials or literature at all. The mechanistic rationale is limited to a class-level generalization: bevacizumab has been studied in other head-and-neck tumor sites (see related candidates below), and anti-VEGF therapy has a plausible biological rationale in head-and-neck squamous cell carcinomas broadly. However, for epiglottis neoplasm this remains an unverified extrapolation with no site-specific supporting data — the TxGNN score alone (99.90%) is not accompanied by any confirmatory trial or publication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Bevacizumab is currently not marketed in Finland (`total_licenses` = 0; no license records on file).

## Cytotoxicity

Bevacizumab is an antineoplastic agent (anti-VEGF monoclonal antibody used exclusively in oncology regimens), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-angiogenic monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.90%), but there is no clinical trial or literature evidence specific to epiglottis neoplasm — evidence level is L5 (model prediction only), and this drug is not marketed in Finland.

**To proceed, the following is needed:**
- Site-specific clinical trial or literature evidence for bevacizumab in epiglottis neoplasm
- TFDA/Finland package insert warnings and contraindications (DG001, Blocking — currently missing)
- Confirmed detailed mechanism of action data (DG002)
- Verification that "epiglottis neoplasm" is a correctly mapped disease ontology term in the TxGNN prediction

---
**Note:** Within this same evidence pack, a lower-ranked candidate — **cystic neoplasm** (rank 7, TxGNN score 99.89%) — has substantially stronger supporting evidence (8 clinical trials including a Phase 3 RCT, 20 publications, Evidence Level L1, decision stage S3, recommendation "Proceed with Guardrails"), largely driven by bevacizumab's established use in low-grade serous ovarian cancer. That candidate may warrant separate evaluation as a higher-priority repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

