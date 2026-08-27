---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor whose established use is ALK-positive non-small cell lung cancer (NSCLC), per the drug-safety literature included in this evidence pack. The TxGNN model's top-ranked prediction for this candidate is **Fibromatosis, Gingival**, but this association is currently supported by **0 clinical trials** and **0 publications**, and the accompanying rationale flags it as likely model noise rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive Non-Small Cell Lung Cancer (NSCLC) — derived from literature context (e.g. PMID 38554546); not confirmed via Finland regulatory filing, as none exists |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap for this record). Based on the literature retrieved for this candidate's broader evidence set, lorlatinib is a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor whose established clinical activity is in ALK-rearranged malignancies, principally NSCLC.

Gingival fibromatosis, however, is a hereditary connective-tissue overgrowth condition most commonly linked to genes such as *SOS1* and *REST*. There is no known involvement of the ALK or ROS1 signalling pathways in its pathophysiology, and no oncogenic driver relationship connects it to lorlatinib's target profile.

The repurposing rationale attached to this candidate explicitly states that the prediction has no supporting clinical trial or publication evidence and describes it as arising "purely from model prediction noise" (原文：純屬模型預測雜訊), with no plausible mechanistic bridge between lorlatinib's pharmacology and this disease. This candidate should therefore not be interpreted as a credible repurposing signal in its current form.

*Note: this evidence pack ranked 10 candidate indications for lorlatinib; this report covers the top-ranked one by TxGNN score. Two other candidates in the same batch (lung hilum carcinoma; lung germ cell tumor) reached evidence level L3 with literature support, though both were also flagged for disease-label/ontology mapping concerns and would warrant separate evaluation.*

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Lorlatinib is not currently marketed in Finland (market status: 未上市). No marketing authorizations are on file for this product.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor; non-cytotoxic mechanism) |
| Myelosuppression Risk | Low — not a conventional cytotoxic agent; myelosuppression is not a prominent finding in the available literature |
| Emetogenicity Classification | Low, consistent with other ALK inhibitors |
| Monitoring Items | Lipid panel (hypercholesterolemia/hypertriglyceridemia reported in case literature), liver function, weight/BMI, mood and cognitive status, pulmonary symptoms (rare ARDS reported in case literature) |
| Handling Protection | Oral targeted therapy; standard institutional oral-oncolytic handling precautions apply. No cytotoxic (hazardous drug) handling classification confirmed — please refer to the package insert for definitive guidance |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is TxGNN's highest-scoring prediction for lorlatinib, but it has zero clinical trial or literature support, and the disease's known genetic etiology (SOS1/REST-related) shows no mechanistic link to lorlatinib's ALK/ROS1 target. The evidence pack itself flags this as likely prediction noise, so it does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action data from DrugBank (currently a High-severity data gap, DG001)
- TFDA-equivalent (Finland) package insert warnings/contraindications (currently a Blocking data gap)
- Independent mechanistic or preclinical evidence linking ALK/ROS1 inhibition to gingival fibromatosis before any further investment
- If repurposing research continues on this drug, prioritize re-evaluating the higher-evidence candidates in the same batch (e.g., lung hilum carcinoma, lung germ cell tumor) after resolving their noted disease-ontology mapping issues, rather than this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

