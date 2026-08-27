---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trastuzumab Deruxtecan: From HER2-Positive Breast/Gastric Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Trastuzumab deruxtecan is a HER2-targeted antibody-drug conjugate (ADC) currently used to treat HER2-positive breast cancer, gastric cancer, and other tumours. The TxGNN model predicts a possible association with **drug-induced osteoporosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanism appears to point in the opposite direction of clinical plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer, gastric cancer, and other tumours (per drug mechanism description; no formal indication record in this dataset) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.31% (rank 7027) |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on known information in this evidence pack, trastuzumab deruxtecan is a HER2-targeted antibody-drug conjugate whose payload, DXd, is a topoisomerase I inhibitor — a cytotoxic chemotherapy agent class. It is clinically used for HER2-positive breast cancer, gastric cancer, and related tumours.

There is no known mechanistic pathway by which this drug would treat osteoporosis. On the contrary, cytotoxic ADCs and their associated cancer treatment regimens (chemotherapy, corticosteroids, ovarian/endocrine suppression) are recognized risk factors that **cause** bone loss rather than reverse it. The direction of the predicted association therefore runs counter to the drug's known pharmacology.

Given this, the prediction is best interpreted as likely model noise or a reversed/confounded association within the TxGNN knowledge graph, rather than a genuine repurposing signal. The absence of any supporting clinical trials, literature, or MOA documentation further limits confidence in this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

This drug is not currently marketed in Finland, and no marketing authorizations are on record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ADC) with cytotoxic payload — topoisomerase I inhibitor (DXd) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic drug handling precautions apply, given the cytotoxic (topoisomerase I inhibitor) payload |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is zero clinical trial or literature support (Evidence Level L5), and the proposed mechanism runs counter to the drug's known cytotoxic pharmacology — cytotoxic anticancer agents are more plausibly a *cause* of drug-induced osteoporosis than a treatment for it. This pattern is consistent with model noise rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Structured mechanism of action (MOA) data from DrugBank or another authoritative source
- TFDA/regulatory package insert data (warnings, contraindications) to complete a baseline safety assessment
- Independent biological rationale or preclinical evidence explaining any plausible link to bone metabolism before further investment
- Continued literature/trial monitoring in case new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

