---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Cutaneous Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab is an anti-PD-1 immune checkpoint inhibitor originally developed for advanced cutaneous squamous cell carcinoma, basal cell carcinoma, and non-small cell lung cancer. The TxGNN model's top-ranked prediction for this candidate is **gallbladder adenosquamous carcinoma**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure network-based prediction with no external validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/metastatic cutaneous squamous cell carcinoma (CSCC); also approved for basal cell carcinoma and NSCLC (based on known drug class information, not present in this evidence pack) |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack. Based on known information, cemiplimab is a fully human IgG4 monoclonal antibody belonging to the anti-PD-1 immune checkpoint inhibitor class. Its efficacy in cutaneous squamous cell carcinoma, basal cell carcinoma, and non-small cell lung cancer has been clinically proven and is well established outside this dataset.

Gallbladder adenosquamous carcinoma contains a squamous differentiation component, which in theory could express PD-L1 and thus respond to PD-1 blockade in the same way cemiplimab acts against squamous tumors elsewhere. However, the immuno-oncology evidence base for gallbladder cancer as a whole is weak, and biliary tract tumors are generally considered a low tumor-mutational-burden, poorly immunogenic ("cold") setting compared to skin or lung squamous cancers.

As a result, this mechanistic link should be read as a network-derived hypothesis rather than a validated pharmacological rationale — it is a purely predictive association with no supporting clinical or literature evidence in the current dataset.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Cemiplimab does not currently hold a marketing authorization in Finland (0 licenses on file in this evidence pack). No product name, dosage form, or approved-indication text is available from the Fimea registry for this candidate.

## Cytotoxicity

Cemiplimab is an antineoplastic agent (immune checkpoint inhibitor used across multiple carcinomas), so this section applies. No drug-specific toxicity data was returned by DrugBank in this evidence pack; the table below reflects general characteristics of the anti-PD-1 monoclonal antibody class and should be confirmed against the package insert once available.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (checkpoint inhibitors do not directly suppress bone marrow; hematologic irAEs are uncommon) |
| Emetogenicity Classification | Low (minimal direct emetogenic potential compared to cytotoxic chemotherapy) |
| Monitoring Items | Baseline and periodic thyroid function, liver function (ALT/AST/bilirubin), renal function, and clinical monitoring for immune-related adverse events (colitis, pneumonitis, dermatitis, endocrinopathies) |
| Handling Protection | Standard IV infusion precautions for monoclonal antibodies; cytotoxic drug handling regulations (e.g., closed-system transfer devices) are not required as with conventional chemotherapy |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (gallbladder adenosquamous carcinoma) has no supporting clinical trials or literature, and the tumor's immunologically "cold" biology weakens the mechanistic rationale. With no Finland market presence and a TFDA package insert (DG001, blocking) and full MOA record (DG002, high) still outstanding, this candidate cannot advance past model prediction (L5/S0) at this time.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed full mechanism of action and DrugBank toxicity profile
- Preclinical or case-level evidence of PD-L1 expression / immune infiltrate in gallbladder adenosquamous carcinoma
- Consider prioritizing rank 4 (external ear basal cell carcinoma) instead, which already has L4 evidence, an S1 decision stage, and one supporting case report, since it extends an indication cemiplimab is already approved for
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

