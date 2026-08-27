---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity Rescue to Diabetic Cataract

## One-Sentence Summary

Glucarpidase (DrugBank DB08898) is a recombinant bacterial carboxypeptidase G2 clinically used to rapidly inactivate methotrexate in patients with impaired renal clearance and toxic plasma methotrexate concentrations. The TxGNN model predicts potential efficacy in **Diabetic Cataract**, but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and the evidence pack's own mechanistic review flags the prediction as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Toxic methotrexate concentrations (folate-antagonist rescue therapy) — not captured in the structured `original_indications` field; derived from the mechanistic description in the evidence pack |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.85% (rank 2057) |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured record (`original_moa` is a data gap). However, the evidence pack's own rationale notes that glucarpidase is a recombinant carboxypeptidase G2 whose sole established pharmacological role is hydrolyzing methotrexate into inactive metabolites, used to rescue patients from toxic methotrexate exposure in the setting of renal impairment.

Diabetic cataract pathophysiology is driven by non-enzymatic glycation of lens crystallins, activation of the polyol/sorbitol pathway, and oxidative stress — none of which intersect with folate-analog metabolism. The evidence pack's mechanistic analysis explicitly states there is no known biological overlap between glucarpidase's enzymatic activity and lens pathology, and glucarpidase has no established pharmacokinetic basis for ocular tissue exposure.

Notably, all 10 of this drug's top-ranked TxGNN predictions are cataract subtypes or diabetic retinopathy, with near-identical scores (99.82–99.85%) clustered tightly together. This pattern is more consistent with a statistical artifact of embedding-space proximity than a genuine pharmacological signal, and should be weighed accordingly when interpreting the score.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Glucarpidase is not marketed in Finland; no marketing authorizations are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical trial or literature evidence for glucarpidase in diabetic cataract (or any of the other 9 predicted cataract/retinopathy indications), the evidence level is L5 (model prediction only), and the evidence pack's own mechanistic review finds no plausible biological link between methotrexate-inactivation and lens/retinal pathology. The drug is also not marketed in Finland.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data to resolve the blocking safety data gap (DG001)
- Confirmed structured original-indication and MOA data from DrugBank or regulatory labeling (DG002)
- Independent literature/preclinical search specifically probing any lens or retinal exposure/pharmacokinetic data for glucarpidase
- Re-evaluation of the TxGNN signal given the suspicious clustering of near-identical scores across 10 cataract/retinopathy terms, which suggests possible embedding-space artifact rather than a true repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

