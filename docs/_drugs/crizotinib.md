---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK/ROS1-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is an ALK/ROS1/MET tyrosine kinase inhibitor, established in non-small cell lung cancer (NSCLC) harboring ALK or ROS1 gene rearrangements (per the literature evidence in this pack).
The TxGNN model's top-ranked prediction is **Fibromatosis, Gingival**, but this candidate currently has **zero clinical trials** and **zero publications** supporting it — it is a pure model-generated hypothesis with no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK/ROS1-positive non-small cell lung cancer (NSCLC) — inferred from literature evidence in this pack; not separately confirmed by Finland (Fimea) licensing data, as the drug is not marketed there |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking data gap). Based on the literature captured elsewhere in this evidence pack, crizotinib is a small-molecule ATP-competitive inhibitor of the receptor tyrosine kinases ALK, ROS1, and c-MET, with proven efficacy in ALK/ROS1-rearranged NSCLC.

For the top-ranked predicted indication, **gingival fibromatosis**, no clinical trial or publication evidence was found in any of the three source databases (ClinicalTrials.gov, ICTRP, PubMed). Gingival fibromatosis is a benign fibrous overgrowth condition with no established relationship to ALK, ROS1, or MET signaling. The TxGNN score reflects the model's internal graph-based similarity metric only — it does not correspond to any documented pharmacological, clinical, or case-based rationale linking crizotinib's known targets to this disease.

Given the absence of both mechanistic plausibility and empirical evidence, this candidate should not be interpreted as a validated repurposing signal at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Crizotinib currently holds no marketing authorization in Finland (0 licenses on record; market status: 未上市/Not Marketed). No product, dosage form, or approved-indication data is available from Fimea for this drug.

---

## Cytotoxicity

Crizotinib is an antineoplastic agent (per its known ALK/ROS1/MET tyrosine kinase inhibitor class, evidenced throughout the literature entries in this pack, e.g. its established use in ALK/ROS1-positive NSCLC).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | No structured toxicity dataset is available in this pack; literature elsewhere among the other candidates references hepatotoxicity, QT prolongation/cardiotoxicity, and interstitial lung disease as known crizotinib safety signals — liver function, ECG/QTc, and pulmonary status should be considered, pending confirmation from the official package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (gingival fibromatosis) is supported only by a TxGNN model score, with no clinical trials, no literature, and no mechanistic hypothesis connecting ALK/ROS1/MET inhibition to this disease (Evidence Level L5). In addition, TFDA package insert data (warnings/contraindications) is a blocking data gap, so this candidate cannot even enter S1 safety screening.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently blocking
- Confirmed DrugBank mechanism of action data
- A preclinical or mechanistic rationale linking crizotinib's ALK/ROS1/MET targets to gingival fibromatosis pathology
- At minimum, case-report or in vitro evidence to escalate this candidate beyond L5

**Note:** This evidence pack contains other predicted indications for crizotinib with substantially stronger support — e.g., *lung hilum carcinoma* (L3, Proceed with Guardrails) and *lung benign neoplasm* / *lung germ cell tumor* (L4, Research Question) — largely reflecting crizotinib's already-established ALK/ROS1/MET-driven NSCLC biology. Several of these appear to be disease-ontology mapping mismatches (e.g., "lung benign neoplasm" literature is almost entirely about malignant ALK/ROS1+ NSCLC) and would need manual disease-label verification before advancing. If a report on one of these higher-evidence candidates is desired instead of the top TxGNN-ranked (but evidence-free) prediction, let us know.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

