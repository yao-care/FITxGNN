---
layout: default
title: Lonafarnib
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 1
---

# Lonafarnib
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

# Lonafarnib: From Progeria/Hepatitis D to Leprosy

## One-Sentence Summary

Lonafarnib is a farnesyltransferase inhibitor whose known clinical/investigational use centers on Hutchinson-Gilford Progeria Syndrome and chronic Hepatitis D; no TFDA/Finland-approved indication is recorded in this evidence pack.
The TxGNN model predicts it may be effective for **Leprosy**, but this prediction is currently supported by **0 clinical trials** and **0 publications**.
This is a pure knowledge-graph correlation with no mechanistic or empirical backing to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication on record; known investigational use in Progeria/Hepatitis D per rationale notes) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% (rank 8442) |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the rationale notes accompanying this prediction, Lonafarnib's known pharmacology is farnesyltransferase inhibition — blocking farnesylation of proteins such as Ras and the Hepatitis D virus large delta antigen — which underlies its use in Progeria and investigational use in chronic Hepatitis D.

Leprosy is caused by *Mycobacterium leprae* and is treated with antibiotics (dapsone, rifampicin, clofazimine) that act on bacterial cell-wall synthesis and metabolic pathways. There is no known biological overlap between host protein farnesylation inhibition and antimycobacterial activity. The rationale data explicitly states this prediction has no supporting mechanistic hypothesis — it is a computational association from the knowledge graph only, compounded by the fact that the drug's own MOA record is itself a data gap.

Given the absence of any mechanistic plausibility and zero corroborating studies, this prediction should be treated as exploratory/hypothesis-generating only, not as a candidate ready for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Lonafarnib has no marketing authorization on record (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, S0) with no clinical trials, no literature, and no plausible mechanistic link between farnesyltransferase inhibition and leprosy treatment — this does not meet the bar to advance to safety screening.

**To proceed, the following is needed:**
- TFDA/EMA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank or primary literature — High-severity gap (DG002)
- At minimum, preclinical or mechanistic evidence establishing biological plausibility for an antimycobacterial effect
- Re-query clinical trial registries (ClinicalTrials.gov, ICTRP) and PubMed periodically for emerging evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

