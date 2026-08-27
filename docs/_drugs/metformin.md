---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 5
---

# Metformin
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

# Metformin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a biguanide antidiabetic agent, well established for the treatment of type 2 diabetes mellitus (this specific detail is not recorded in the evidence pack, which lists no original indications).
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests entirely on graph-embedding similarity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (Metformin is generically known as a Type 2 Diabetes Mellitus treatment) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Metformin in this evidence pack ([Data Gap]). Based on general pharmacological knowledge, Metformin's known mechanism involves AMPK activation and inhibition of mitochondrial complex I — mechanisms central to its glucose-lowering effect.

Focal Stiff Limb Syndrome and classic Stiff Person Syndrome sit on a disease spectrum driven primarily by GABAergic neurotransmission deficits and anti-GAD65 autoimmune pathology. There is no established mechanistic link between AMPK/mitochondrial pathways and this neuro-autoimmune process. The connection surfaced by TxGNN appears to be a pure graph-embedding association rather than a biologically grounded hypothesis, and should be treated as exploratory only.

Notably, the four other TxGNN-ranked candidates for Metformin (classic stiff person syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, and drug-induced localized lipodystrophy) show similarly weak or even conflicting mechanistic rationale — the thiamine-responsive candidate in particular runs counter to Metformin's known interference with thiamine/B12 absorption, and should be flagged as a potential mechanistic contraindication rather than a treatment opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN embedding score (L5, S0) with zero clinical trials and zero literature across all five predicted indications, and a Blocking data gap on TFDA package insert warnings/contraindications currently prevents even an initial (S1) safety review.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently Blocking
- Confirmed original mechanism of action (MOA) for Metformin
- Preclinical or mechanistic literature specifically linking AMPK/mitochondrial pathways to GABAergic/anti-GAD65 pathology
- Reassessment of Finland/Taiwan market and licensing status, currently recorded as not marketed with zero authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

