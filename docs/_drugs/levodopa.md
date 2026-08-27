---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa: From Parkinsonism (Movement Disorders) to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor whose clinical use centers on Parkinson's disease and related movement disorders. The TxGNN model predicts a possible link to **Rasmussen subacute encephalitis**, a rare pediatric autoimmune/inflammatory brain condition, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Finland regulatory dataset (no licenses on file); known clinical use is Parkinson's disease / movement disorders per the drug's mechanism description |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% (rank 9079) |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack ([Data Gap] DG002). Based on known pharmacology, levodopa is converted centrally to dopamine to replenish nigrostriatal dopamine deficits, and its efficacy in Parkinsonian movement disorders is well established.

Rasmussen subacute encephalitis, however, is a rare pediatric chronic inflammatory encephalitis driven by T-cell–mediated cortical inflammation and neuronal loss, causing intractable seizures and progressive hemiparesis. Standard treatment relies on immunomodulation (IVIG, corticosteroids, plasma exchange) or hemispherectomy — a pathophysiology (autoimmune neuroinflammation) that does not overlap with levodopa's dopaminergic mechanism.

No established mechanistic link connects dopamine replacement therapy to autoimmune encephalitis. The high TxGNN score (0.99) most likely reflects graph-topological proximity between nodes in the knowledge graph rather than validated biological plausibility, and should be interpreted with caution given the absence of any supporting trial or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Levodopa currently has no active marketing authorizations on file in Finland (0 licenses; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/label warnings and contraindications are currently unavailable (Blocking data gap, DG001), which prevents a full S1 safety pre-assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN model output (L5, no clinical trials or literature), and no plausible mechanistic link exists between levodopa's dopaminergic action and Rasmussen encephalitis's autoimmune-inflammatory pathology. A blocking safety data gap (TFDA label unavailable) also prevents safety review.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — DG001, blocking
- Levodopa mechanism of action detail from DrugBank — DG002
- Preclinical or mechanistic studies establishing biological plausibility for a dopaminergic–neuroinflammatory link
- Ongoing surveillance for emerging trials or literature on this indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

