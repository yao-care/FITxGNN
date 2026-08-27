---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# LONOCTOCOG ALFA: From Factor VIII Replacement Therapy to Pseudo-von Willebrand Disease

## One-Sentence Summary

> Lonoctocog alfa is a single-chain recombinant Factor VIII (rFVIII) replacement product acting within the intrinsic coagulation cascade (FVIIIa–FIXa tenase complex).
> The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**,
> but this candidate — along with 3 other platelet-disorder candidates — has **no supporting clinical trials or literature**, and the drug's own mechanistic rationale explicitly argues against biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no approved license/indication text is available in this evidence pack (drug is not marketed in Finland) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not directly available (`original_moa` is a data gap). However, the repurposing rationale entries in this evidence pack consistently describe lonoctocog alfa as a single-chain recombinant Factor VIII (rFVIII) that does **not** contain von Willebrand Factor (VWF), and that functions as the FVIIIa cofactor within the intrinsic coagulation tenase complex (FVIIIa–FIXa).

Critically, the mechanistic analysis for the top-ranked candidate, pseudo-von Willebrand Disease, explicitly states that this disorder originates from a **gain-of-function mutation in platelet GPIbα** — an abnormally increased platelet affinity for VWF that depletes high-molecular-weight VWF multimers. The pathology sits at the platelet receptor level, not at the coagulation-factor level. Supplementing FVIII does not correct GPIbα–VWF binding abnormalities, so there is no direct mechanistic link between the drug and this indication.

The same pattern holds across all four TxGNN-ranked candidates (pseudo-vWD, primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome): each is a **platelet-function or platelet-receptor disorder**, whereas lonoctocog alfa addresses **coagulation-factor deficiency**. The evidence pack's own rationale concludes that TxGNN's high scores most likely reflect topological proximity within a "hemostasis/coagulation" disease cluster in the knowledge graph, rather than a genuine pharmacological pathway. Even for Scott syndrome, where FVIIIa is a literal component of the relevant enzyme complex, the defect is in platelet membrane phospholipid scrambling (ANO6), not FVIII availability — so supplementation cannot restore the missing biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Lonoctocog alfa currently holds no marketing authorization in Finland (0 licenses on record); no product/dosage-form/indication data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other TxGNN-Ranked Candidates (Not Primary)

For completeness, three additional platelet-disorder candidates were flagged at similarly high TxGNN scores but with the same lack of supporting evidence and the same mechanistic disconnect (receptor/granule/scramblase defects vs. coagulation-factor replacement):

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|-----------------|----------|
| 2 | Primary release disorder of platelets | 99.84% | L5 | Hold |
| 3 | Glanzmann thrombasthenia | 99.76% | L5 | Hold |
| 4 | Scott syndrome | 99.44% | L5 | Hold |

None have registered clinical trials or literature support.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications are supported only by TxGNN model scores (L5), with zero clinical trials and zero literature identified across 12 targeted searches. The drug's own mechanistic rationale for each candidate explicitly argues against biological plausibility, since the target disorders are platelet-function/receptor defects rather than coagulation-factor deficiencies that FVIII replacement can address.

**To proceed, the following is needed:**
- Original indication and regulatory approval history for lonoctocog alfa (currently missing)
- Mechanism of action (MOA) data from DrugBank or manufacturer labeling
- TFDA/Fimea package insert warnings and contraindications (currently a Blocking data gap per `DG001`)
- Independent pharmacological or preclinical rationale connecting FVIII supplementation to any of the four candidate platelet disorders before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

