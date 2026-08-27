---
layout: default
title: Mepolizumab
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mepolizumab: From Eosinophilic Inflammatory Disease to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab is a humanized anti-IL-5 monoclonal antibody publicly known for treating eosinophilic-driven conditions such as severe eosinophilic asthma and hypereosinophilic syndrome (HES); this specific original indication is not recorded in the current evidence pack. The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but this direction is currently supported by only **1 case-report-level publication** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not marketed in Finland; no license records) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 (single case report / mechanistic evidence only) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on publicly known drug information, mepolizumab is a humanized IgG1 monoclonal antibody that binds circulating interleukin-5 (IL-5), blocking its interaction with the IL-5 receptor on eosinophils and thereby reducing eosinophil production, activation, and survival. It is established for eosinophil-driven diseases such as severe eosinophilic asthma, hypereosinophilic syndrome (HES), and eosinophilic granulomatosis with polyangiitis (EGPA).

The predicted new indication — thrombocytopenia due to immune destruction — may be mechanistically linked through eosinophil-mediated immune injury pathways. Hypereosinophilic states can trigger secondary immune-mediated platelet destruction and thrombotic microangiopathy via eosinophil-derived granule products and complement activation. This is directly illustrated in the single literature case identified below (PMID 28648630), where mepolizumab resolved a steroid-resistant hypereosinophilic immune process with concomitant improvement of an associated thrombotic microangiopathy involving platelet consumption.

Because the original indication field is empty in this evidence pack, this mechanistic rationale should be treated as background context rather than a pack-verified claim, and confirmed against DrugBank/Fimea sources before use in decision-making.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells, Molecules & Diseases | Mepolizumab, combined with anti-C5 therapy, resolved a steroid-resistant hypereosinophilic immune process in a patient with atypical HUS-associated eosinophilia, with concomitant amelioration of a mixed thrombotic microangiopathy |

## Finland Market Information

Mepolizumab is currently not marketed in Finland; no drug license records are on file (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single case report with no controlled or registered clinical trials, and the safety-labeling data gap (DG001) is flagged as Blocking, meaning the candidate cannot yet pass initial safety screening. Mepolizumab is also not currently marketed in Finland, removing local regulatory precedent to lean on.

**To proceed, the following is needed:**
- Fimea/TFDA-equivalent package insert data (warnings, contraindications) to resolve DG001
- Confirmed original indication and mechanism of action documentation to resolve DG002
- Additional clinical evidence (case series or controlled studies) specific to immune thrombocytopenia
- A completed drug-drug interaction (DDI) query, since the current query returned "not_found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

