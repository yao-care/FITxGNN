---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 3
---

# Nintedanib
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

# Nintedanib: From Idiopathic Pulmonary Fibrosis to Dermatofibrosarcoma Protuberans

> **Note on data provenance:** The evidence pack does not include sourced original-indication or MOA data (`original_indications: []`, `original_moa: "[Data Gap]"`, flagged as DG001/DG002). The original indication cited here (idiopathic pulmonary fibrosis) reflects nintedanib's well-established public drug classification and requires confirmation against a primary source (DrugBank/Fimea label) before use in a formal safety review.

## One-Sentence Summary

Nintedanib is a multi-target tyrosine kinase inhibitor generally known for its use in fibrotic lung disease. The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans**, but this direction is currently supported by only **1 mechanism-related publication** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current evidence pack (blocking data gap — see DG001) |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nintedanib is not available in this evidence pack (DG002). Based on generally known pharmacology, nintedanib is a triple angiokinase inhibitor targeting VEGFR, FGFR, and PDGFR, and its efficacy in fibrotic lung disease has been established in the broader literature — but this has not been confirmed against a sourced document in this pack.

The single supporting publication (PMID 29408302) is a pharmacological review of small-molecule PDGFR inhibitors in neoplastic disease. Dermatofibrosarcoma protuberans is a tumour characteristically driven by a COL1A1–PDGFB gene fusion, which causes constitutive PDGFR pathway activation. If nintedanib's PDGFR-inhibitory activity is confirmed, there is a plausible mechanistic rationale for activity in PDGFR-driven sarcomas such as DFSP and liposarcoma — consistent with all three of TxGNN's top-ranked predictions being soft-tissue sarcomas.

This mechanistic link is presently supported by class-level literature only, not by drug-specific or disease-specific studies, and should be treated as hypothesis-generating rather than confirmatory.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disease; describes the PDGF/PDGFR signalling axis relevant to PDGFR-driven tumours such as DFSP, supporting a class-level mechanistic rationale rather than drug-specific efficacy data |

## Finland Market Information

Nintedanib is not currently marketed in Finland; no authorization records are available in the evidence pack (`total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single class-level mechanism review with no drug-specific or disease-specific clinical or preclinical data, no registered trials for any of the three predicted sarcoma indications, and no Finland market presence to draw on for real-world safety experience. The blocking data gap (DG001 — TFDA/Fimea package insert warnings and contraindications) also prevents entry into the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) to resolve DG001 and unblock S1 safety pre-screening
- Confirmed original indication and MOA from DrugBank or the approved label (DG002)
- Drug-specific preclinical or case-level evidence (e.g., PDGFR-inhibitor activity confirmed for nintedanib in DFSP or liposarcoma models)
- Continued literature/trial monitoring, as liposarcoma and ovarian myxoid liposarcoma currently have zero supporting evidence beyond the TxGNN score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

