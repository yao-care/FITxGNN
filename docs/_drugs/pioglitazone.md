---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 9
---

# Pioglitazone
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (PPAR-γ agonist) insulin sensitizer whose established use is in Type 2 Diabetes Mellitus.
The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare skeletal dysplasia,
but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as likely model noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (established use; not captured in this evidence pack — licensing data is empty) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, pioglitazone is a thiazolidinedione that acts as a PPAR-γ agonist, improving insulin sensitivity and beta-cell function; its efficacy in Type 2 Diabetes Mellitus is well established.

Opsismodysplasia, however, is a rare skeletal dysplasia caused by mutations in *INPPL1*, affecting bone growth and ossification. There is no known mechanistic overlap between the PPAR-γ/insulin-sensitizing pathway and the pathophysiology of this condition. The evidence pack's own rationale for this pairing states that despite the high TxGNN similarity score, no identifiable biological plausibility exists, and the association is most likely model noise rather than a genuine repurposing signal.

Consequently, this specific top-ranked prediction should not be interpreted as a credible repurposing lead. Notably, several lower-ranked predictions in the same batch (localized/centrifugal lipodystrophy, ranks 5–8) have a substantially stronger mechanistic rationale, since PPAR-γ is a well-characterized regulator of adipocyte differentiation and lipid storage — though these too currently lack any clinical trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Pioglitazone is currently not marketed in Finland (0 marketing authorizations on record), so no product-level licensing table is available.

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** TFDA/Fimea package insert warnings and contraindications are recorded as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety evaluation can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Opsismodysplasia) has no clinical trial or literature support and no plausible mechanistic link — the evidence pack itself characterizes it as likely model noise. Combined with the absence of MOA data, safety data, and Finland market presence, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/Fimea package insert for warnings/contraindications
- Resolve DG002 (High): confirm mechanism of action via DrugBank API
- If pursuing repurposing signals from this batch, prioritize the lipodystrophy cluster (ranks 5–8) for targeted literature/trial searches given their stronger PPAR-γ mechanistic rationale, rather than the top-ranked but mechanistically unsupported Opsismodysplasia signal
- Note: the 9 literature hits under "pancreatic agenesis" (rank 9) are general T2DM/PPAR-γ reviews, not disease-specific — do not count these as supporting evidence without further screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

