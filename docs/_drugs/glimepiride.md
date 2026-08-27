---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea antidiabetic drug used to manage Type 2 Diabetes Mellitus by stimulating pancreatic insulin secretion.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure graph-embedding signal with no pharmacological or clinical evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from sulfonylurea drug class; not present in the evidence pack's license records) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a blocking-severity data gap). Based on known pharmacology, glimepiride is a sulfonylurea that binds SUR1 on the pancreatic β-cell KATP channel to trigger insulin release, and its efficacy in Type 2 Diabetes Mellitus is well established.

Focal stiff limb syndrome is a localized variant of stiff person syndrome, a rare autoimmune neurological disorder in which anti-GAD65 antibodies attack GABAergic neurons, causing muscle rigidity and spasm. There is no established pharmacological or clinical relationship between insulin-secretagogue activity and this autoimmune neuromuscular condition.

The evidence pack's own rationale for this prediction is explicit that the link is not mechanistically grounded: it states that no sulfonylurea pharmacological mechanism supports the connection, and that the high TxGNN score likely reflects an indirect statistical association in the knowledge graph (possibly via GAD/insulin-pathway gene overlap with adjacent predictions) rather than biological plausibility. No clinical or molecular evidence currently exists to support this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 prediction (model output only) with no clinical trials, no supporting literature, and no plausible pharmacological mechanism connecting glimepiride's insulin-secretagogue action to the autoimmune pathophysiology of focal stiff limb syndrome — the evidence pack's own rationale flags the mechanistic link as absent.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a blocking data gap
- Verified mechanism of action (MOA) data from DrugBank — currently a high-severity data gap
- Preclinical or mechanistic studies establishing biological plausibility for this indication
- Drug interaction (DDI) data, currently unavailable
- If pursued, note that other predicted indications for glimepiride (e.g., pancreatic agenesis, rank 9) carry a marginally stronger — though still weak — mechanistic rationale via monogenic neonatal diabetes and may warrant comparative prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

