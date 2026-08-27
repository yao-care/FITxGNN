---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

# Selpercatinib: From RET-Altered Cancer to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib is a selective RET kinase inhibitor used in RET fusion/mutation-positive cancers (based on literature context; formal original-indication data is not yet populated). The TxGNN model predicts a possible effect in **pulmonary hypertension**, but a review of the **3 supporting publications** found none actually address pulmonary vascular disease — the top prediction currently has no real mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured data (data gap); literature context suggests RET fusion/mutation-positive cancers (e.g., NSCLC, medullary thyroid carcinoma) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% (rank 8099) |
| Evidence Level | L5 (model prediction only) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available for selpercatinib (data gap). Based on the literature retrieved for this candidate, selpercatinib is a selective RET tyrosine kinase inhibitor developed for RET fusion-positive NSCLC and RET-mutant medullary thyroid carcinoma — it blocks, rather than activates, RET/GDNF signaling.

There is no established biological rationale linking RET inhibition to pulmonary hypertension. A check of the three cited publications shows none support this connection: the FAERS real-world study (PMID 39372206) reports selpercatinib-associated cardiopulmonary adverse events as pulmonary embolism, deep vein thrombosis, pericardial effusion, and systemic hypertension — not pulmonary hypertension. The other two papers (a retrospective NSCLC analysis and a medullary thyroid carcinoma case report) are unrelated to pulmonary vascular disease and appear to have matched on keyword overlap (RET / hypertension) rather than clinical relevance.

No clinical trials, preclinical studies, or mechanistic literature currently link the GDNF-RET axis to pulmonary vascular remodeling in a therapeutically actionable way. The high TxGNN score therefore reflects a purely data-driven association without corroborating biological or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Cohort (FAERS real-world AE analysis) | Frontiers in Pharmacology | Compares adverse-event profiles of pralsetinib vs. selpercatinib; reported cardiopulmonary AEs are pulmonary embolism, DVT, pericardial effusion, and systemic hypertension — not pulmonary hypertension |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective (SIREN) | Therapeutic Advances in Medical Oncology | Real-world efficacy of selpercatinib in RET fusion-positive NSCLC through an access program; no relevance to pulmonary vascular disease |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Case report | Cureus | Case of MEN2B-associated medullary thyroid carcinoma with RET M918T mutation on targeted therapy; unrelated to pulmonary hypertension |

---

## Finland Market Information

Selpercatinib currently holds no marketing authorization in Finland (0 licenses on record).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) — inferred from literature context; formal DrugBank/MOA classification is a data gap |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA labeling data (warnings/contraindications) could not be retrieved, which blocks formal safety pre-screening (S1) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but verification of the cited literature shows no actual mechanistic or clinical evidence connecting RET inhibition to pulmonary hypertension, and no clinical trials exist for this indication. Combined with the missing TFDA safety data, this candidate cannot advance past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) to unblock safety pre-screening
- Confirmed original indication and mechanism-of-action data from DrugBank
- Preclinical or mechanistic evidence specifically linking RET/GDNF signaling to pulmonary vascular remodeling before further pursuing this indication
- If migraine-related predictions (rank 2/3) are of interest, dedicated literature and trial searches, as none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

