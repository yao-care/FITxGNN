---
layout: default
title: Ledipasvir
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Ledipasvir
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

# Ledipasvir: Repurposing Evaluation — Insufficient Data to Complete Assessment

## One-Sentence Summary

Ledipasvir (DB09027) is a small molecule drug currently under initial repurposing evaluation.
This Evidence Pack contains **no TxGNN predicted indications**, and both original indication and mechanism of action data are absent from the current dataset.
A full repurposing report **cannot be generated** until critical data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset |
| Predicted New Indication | None — no TxGNN predictions in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no predictions available) |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains no TxGNN model predictions and has blocking-severity data gaps in MOA and safety information; a repurposing evaluation cannot be meaningfully conducted at this stage.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve TFDA package insert warnings and contraindications to enable basic safety screening
- **[High]** Obtain mechanism of action (MOA) data from DrugBank (DB09027) to support mechanistic plausibility analysis
- **[Required]** Re-run TxGNN prediction pipeline for ledipasvir to generate candidate indications
- **[Required]** Populate original indication data (ledipasvir is expected to have registered HCV indications in other markets — confirm and import)
- **[Required]** After predictions are available, re-query clinical trial (ClinicalTrials.gov) and literature (PubMed) evidence for each candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

