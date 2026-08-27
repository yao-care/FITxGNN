---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fentanyl: From Undocumented Original Indication to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

The original indication data for fentanyl is not captured in this evidence pack, and the drug is currently **not marketed in Finland**. The TxGNN model predicts fentanyl may be relevant to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, with a high model score (**99.46%**) but **zero supporting clinical trials or literature** identified to date.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no licenses or original indications on file) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.46% (embedding rank 5778) |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Mechanism of action data for fentanyl is not available in this evidence pack (`original_moa: [Data Gap]`), and the drug's original indication(s) are also undocumented here, so the relationship between fentanyl's known pharmacology and NSIAD cannot be substantiated from the data on hand.

The model's own repurposing-rationale fields for this candidate (`mechanistic_link`, `similarity_to_original`) are marked **pending** — meaning no mechanistic or similarity analysis has been completed for this prediction yet. This is purely an embedding-based association from TxGNN with no corroborating clinical trials, literature, or expert-reviewed rationale at this time.

Without MOA data, original indication context, or any supporting studies, this prediction should be treated as an unvalidated model output rather than a mechanistically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Fentanyl currently has no Fimea marketing authorizations on file (`total_licenses: 0`), so no product/authorization table can be produced.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert data is flagged as a **Blocking** data gap — its absence prevents completion of the initial S1 safety review for this candidate.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN model score with no clinical trials, no literature, and no completed mechanistic rationale (evidence level L5). The drug is also unmarketed in Finland, and a **Blocking**-severity data gap (missing TFDA/Fimea package insert) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — blocking gap, required before any S1 safety review
- Drugbank-sourced mechanism of action (MOA) data for fentanyl
- Original indication history for fentanyl to assess mechanistic similarity to NSIAD
- Completion of the pending mechanistic-link and similarity-to-original analysis for this candidate
- Targeted literature/clinical trial search specifically for fentanyl–NSIAD association, since current PubMed/ClinicalTrials.gov/ICTRP queries returned zero results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

