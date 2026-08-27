---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Rheumatoid Arthritis to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra is a recombinant IL-1 receptor antagonist whose original indication (rheumatoid arthritis) is not included in this evidence pack. The TxGNN model's top-ranked prediction for this drug is **Extracutaneous Mastocytoma**, but this direction currently has **no clinical trials** and **no supporting literature** — it is a pure model prediction with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (publicly, anakinra's original approved indication is rheumatoid arthritis — flagged here as background, not evidence-pack data) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (marked as a High-severity data gap). Based on known information, anakinra belongs to the class of IL-1 receptor antagonists (interleukin-1 blocking biologic agents), and its efficacy in IL-1-mediated inflammatory conditions has been established in clinical use; mechanistically it is expected to be applicable primarily to diseases driven by excess IL-1β signaling.

However, the evidence pack's own repurposing rationale for this specific prediction is skeptical: extracutaneous mastocytoma is a localized mast cell proliferative lesion driven predominantly by **KIT signaling**, not IL-1-dependent inflammation. There is no described IL-1 pathway involvement in this disease's pathogenesis, and the link is characterized in the source data as lacking mechanistic support.

No clinical trials or publications currently connect anakinra to extracutaneous mastocytoma (evidence level L5, decision stage S0). This prediction should be treated as an unvalidated model output rather than a substantiated repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Anakinra is not currently marketed in Finland — no marketing authorizations (0 licenses) are recorded in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (extracutaneous mastocytoma) has no clinical trial or literature support, and the mechanistic rationale in the evidence pack itself questions the IL-1 dependency of this disease. Evidence level L5 (model prediction only) does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/regulatory package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Confirmed mechanism of action data from DrugBank or equivalent source (currently a High-severity data gap)
- Dedicated literature or preclinical search specific to IL-1/mast cell biology in extracutaneous mastocytoma to test the mechanistic hypothesis

**Note on alternative candidates:** Within this same evidence pack, two other TxGNN-predicted indications for anakinra show substantially stronger support and may warrant separate, prioritized evaluation:
- **Autosomal recessive Familial Mediterranean Fever** (L3, Proceed with Guardrails) — 20 literature results, including reports of anakinra use in colchicine-resistant patients, consistent with anakinra's established IL-1-blocking mechanism.
- **Pyogenic autoinflammatory syndrome (PAPA/PSTPIP1-spectrum)** (L3, Proceed with Guardrails) — 19 literature results directly describing anakinra treatment in PAPA/PAPASH, mechanistically well aligned with IL-1β overproduction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

