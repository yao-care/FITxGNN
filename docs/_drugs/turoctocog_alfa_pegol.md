---
layout: default
title: Turoctocog Alfa Pegol
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog Alfa Pegol: From Hemophilia A (Congenital Factor VIII Deficiency) to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa pegol (DB14738) is a PEGylated recombinant Factor VIII (rFVIII) product; its established clinical role is factor replacement in congenital FVIII deficiency (Hemophilia A). The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets**, but no clinical trials or literature currently support this direction, and the model's own mechanistic annotation flags the biological link as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Factor VIII deficiency (Hemophilia A) — inferred from evidence pack rationale text; not directly recorded in `original_indications` |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for turoctocog alfa pegol is not available (Data Gap). Based on known information, this drug is a PEGylated recombinant Factor VIII replacement therapy, and its efficacy in congenital FVIII deficiency (Hemophilia A) is well established through the FVIII replacement mechanism.

However, for the top-ranked predicted indication, primary release disorder of platelets, the evidence pack's own mechanistic annotation is explicitly cautionary: this condition reflects a defect in platelet granule release — an intrinsic platelet functional disorder — which has **no direct mechanistic relationship** to coagulation factor replacement. The TxGNN score is very high (99.97%, rank 64), but a high similarity score in the knowledge graph does not by itself establish biological plausibility.

Notably, among the other predictions in this evidence pack, rank 4 — "acquired coagulation factor deficiency" — has a mechanistically coherent rationale, since it sits on the same replacement-therapy logic as the approved indication. That candidate carries a "Research Question" recommendation rather than "Hold," and may warrant separate follow-up (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

(Key warnings, contraindications, and drug-interaction data are all marked as Data Gap or "not found" in the current evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (primary release disorder of platelets) has no clinical trial or literature support, and the model's own mechanistic rationale indicates weak biological plausibility for a coagulation-factor replacement product. Evidence level is L5 (model prediction only), which does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a Blocking data gap preventing S1 safety review
- Confirmed mechanism of action (MOA) via DrugBank API — currently a High-severity gap
- Independent mechanistic/preclinical evaluation of platelet granule-release physiology relative to FVIII pharmacology, before any further investment
- Consider evaluating rank 4 ("acquired coagulation factor deficiency") as a mechanistically stronger alternative candidate for a dedicated research-question track, given its direct overlap with the approved replacement-therapy logic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

