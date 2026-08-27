---
layout: default
title: Turoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog Alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa is a recombinant Factor VIII product used to treat and prevent bleeding in Haemophilia A. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this candidate currently has **no supporting clinical trials and no supporting literature**, and the model's own rationale flags the mechanistic link as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (Factor VIII replacement) — not verifiable from local licence text, as the product is not currently marketed here |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on known pharmacology, turoctocog alfa is a recombinant Factor VIII (FVIII) concentrate; its proven role is replacing deficient FVIII clotting activity in Haemophilia A.

Primary release disorder of platelets, however, is a platelet granule secretion defect (e.g. δ-storage pool disease) rather than a coagulation factor deficiency. The bleeding tendency in this condition arises from platelets failing to release their granule contents, not from insufficient FVIII. The evidence pack's own repurposing rationale explicitly states this link is weak: FVIII supplementation cannot correct a platelet granule-release defect.

In short, the TxGNN score is high, but the underlying biology does not obviously support extrapolating FVIII replacement to this platelet disorder. This is a case where a strong model score is not accompanied by a plausible mechanistic story, and no clinical or literature evidence currently exists to independently corroborate the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Turoctocog alfa currently holds **no marketing authorizations** in Finland (`market_status: 未上市`, `total_licenses: 0`); no licence records are available to list.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently unavailable — DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication sits at the lowest evidence tier (L5) — no clinical trials, no literature, and the mechanistic rationale itself is assessed as weak (a platelet granule-release defect vs. a coagulation factor replacement mechanism). Several lower-ranked candidates in this same evidence pack (e.g. thrombotic thrombocytopenic purpura) even carry a plausible safety concern, since FVIII supplementation is pro-coagulant and could theoretically worsen a pro-thrombotic condition — reinforcing that these TxGNN scores should not be acted on without mechanistic and clinical scrutiny.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) documentation for turoctocog alfa (DG002, High severity)
- Local package insert / regulatory warnings and contraindications (DG001, Blocking severity — required before any S1 safety screening)
- A hematology/coagulation specialist review of whether FVIII replacement has any plausible role in platelet granule-release disorders
- Continued literature/trial surveillance, as none currently exists for any of the 10 predicted indications in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

