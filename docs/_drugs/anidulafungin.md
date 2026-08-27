---
layout: default
title: Anidulafungin
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 0
---

# Anidulafungin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Anidulafungin: Evaluation Report — No Repurposing Candidates Identified

## One-Sentence Summary

Anidulafungin (DB00362) is an echinocandin antifungal agent approved in multiple markets for the treatment of candidemia and invasive candidiasis. The TxGNN model did not return any predicted new indications for this drug in the current analysis run. Due to the absence of predictions and multiple data gaps in the Evidence Pack, a full repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack (known use: candidemia, esophageal candidiasis) |
| Predicted New Indication | None — TxGNN returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; no candidates to evaluate |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Returned

The Evidence Pack for Anidulafungin contains an empty `predicted_indications` array, which indicates that the TxGNN knowledge graph model did not identify any disease nodes with a repurposing score above the reporting threshold for this compound in the current run.

Two compounding data gaps likely limited the model's ability to generate predictions:

1. **Mechanism of Action (MOA) is absent** — Without structured MOA data in DrugBank format (e.g., enzyme targets, receptor bindings, pathway annotations), the graph neural network has limited pharmacological edges to traverse and score against disease nodes.

2. **Original indication list is empty** — The Evidence Pack carries no structured indication entries. If the model relies on indication-level graph anchoring to seed its prediction walk, the absence of a seed node would suppress all candidate scores.

These two gaps together represent a compound failure: neither the "from" anchor (indication) nor the "why" signal (MOA) is available for the model to reason from.

---

## Finland Market Information

Anidulafungin is **not currently marketed in Finland**. No authorizations, product names, dosage forms, or approved indications are recorded in the Evidence Pack.

> For reference, in markets where it is authorized (e.g., USA, EU via EMA under the brand name Eraxis), anidulafungin is approved as an intravenous antifungal for candidemia and invasive Candida infections including esophageal candidiasis. This information is provided for context only and does not substitute for a formal regulatory search.

---

## Safety Considerations

All safety fields in the current Evidence Pack contain data gaps. No key warnings, contraindications, or drug interaction data are available for reporting.

> Please refer to the current Summary of Product Characteristics (SmPC) or package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no repurposing candidates for Anidulafungin, and critical input data (MOA, structured original indications) are missing — meaning the pipeline lacks the minimum inputs required to produce or evaluate a prediction. Without candidates, no repurposing case can be made.

**To proceed, the following is needed:**

- **Resolve DG002 (MOA):** Query DrugBank API for Anidulafungin's mechanistic data (target: β-1,3-D-glucan synthase; pathway: fungal cell wall synthesis). Populate `original_moa` field and re-run TxGNN.
- **Resolve DG001 (Safety):** Download the Finnish SmPC or EMA product monograph and extract key warnings and contraindications. Populate `key_warnings` and `contraindications`.
- **Populate original indications:** Add structured ICD-10 or MeSH disease entries for candidemia and esophageal candidiasis to `original_indications`. This provides a graph anchor for the TxGNN walk.
- **Re-run TxGNN prediction pipeline** after data gaps are closed; reassess whether candidates emerge at a lower score threshold if the standard threshold still yields zero results.
- **Check if Eraxis or a generic holds an EMA centralised authorisation** that would apply to Finland — this would change market status from "Not marketed" to "Marketed (EMA)."
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

