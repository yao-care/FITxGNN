---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomide: Repurposing Candidate — Evaluation On Hold

## One-Sentence Summary

Leflunomide is an immunomodulatory disease-modifying antirheumatic drug (DMARD), known in clinical practice for rheumatoid arthritis and psoriatic arthritis treatment.
However, the current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, and key data fields including mechanism of action, safety warnings, and original indication records are absent.
Without a predicted indication to evaluate, this report documents the data gaps and recommends a Hold decision pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction unavailable; no supporting studies) |
| Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

The Evidence Pack for Leflunomide (DrugBank ID: DB01097) returned an empty `predicted_indications` array. Two possible explanations exist:

1. **Pipeline upstream failure**: If the drug node for DB01097 was not present or not properly embedded in the knowledge graph used for TxGNN inference, the model would produce no ranked candidates.
2. **Filtered output**: Predictions may have been generated but fell below the confidence threshold applied during post-processing.

Until the root cause is confirmed, no repurposing hypothesis can be assessed. The data gaps recorded in the Evidence Pack (DG001: TFDA package insert warnings; DG002: mechanism of action) further limit the safety and mechanistic review that would normally accompany any predicted indication.

---

## Market Information

Leflunomide is **not marketed** under any current local authorization. The regulatory query returned zero licenses (total_licenses: 0), with no dosage form or approved indication data on file.

> Note: The DrugBank query (query log ID 3) and TFDA package insert query (query log ID 4) both returned result_count ≥ 1, indicating source records exist. However, the structured fields in this Evidence Pack were not populated from those results. Remediation should re-extract approved indication text and safety warnings from these confirmed sources.

---

## Safety Considerations

All safety fields in the current Evidence Pack are marked as data gaps:

- Key warnings: not available
- Contraindications: not available
- Drug–drug interactions: query returned no results

Please refer to the package insert and DrugBank record (DB01097) for safety information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack returned no TxGNN predictions, and the two data gaps rated High/Blocking (MOA and TFDA safety warnings) have not been resolved. There is no repurposing hypothesis to evaluate at this time.

**To proceed, the following is needed:**

- **Re-run TxGNN inference** for DB01097 and confirm whether the drug node is present in the knowledge graph; if absent, add it and re-embed.
- **Resolve DG002 (MOA)**: Query DrugBank API for mechanism of action and pharmacological class data for DB01097.
- **Resolve DG001 (Safety)**: Download and parse the TFDA package insert PDF to extract warnings and contraindications; populate `key_warnings` and `contraindications` fields.
- **Re-populate original_indications**: The TFDA package insert query (log ID 4) confirmed a result exists — extract the approved indication text and populate the field before the next evaluation cycle.
- Once a predicted indication is available, regenerate this report using the full Evidence Pack template.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

