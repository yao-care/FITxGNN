---
layout: default
title: Metreleptin
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# METRELEPTIN: From an Undocumented Original Indication to Familial Generalized Lentiginosis

## One-Sentence Summary

Metreleptin (DrugBank DB09046) is a recombinant human leptin analog; its original approved indication and mechanism of action are not documented in the current data pack. TxGNN predicts a possible link to **Familial Generalized Lentiginosis**, but this prediction is supported by **zero clinical trials** and **zero publications**, and the model's own rationale flags it as a likely false-positive artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no approved indications on file; MOA marked as a High-severity data gap) |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Blocking/High data gaps DG001 and DG002 — TFDA package insert and MOA are both unresolved). Based on general pharmacology, metreleptin is a recombinant leptin analog acting on hypothalamic leptin receptors to regulate energy metabolism and adipose-related endocrine function.

The top-ranked predicted indication, Familial Generalized Lentiginosis, is a pigmentary/melanocytic disorder generally associated with genes such as PTPN11 and the RAS-MAPK pathway — a biological system with no established connection to leptin/JAK2-STAT3 signaling. The evidence pack's own mechanistic assessment for this candidate explicitly states that no known mechanistic link exists, and characterizes the prediction as most likely a false-positive artifact arising from embedding similarity between rare-syndrome nodes in the TxGNN knowledge graph, rather than a genuine biological signal.

The remaining nine ranked candidates (ranks 2–10, all rare genetic syndromes or oncologic conditions such as Moynahan syndrome, rhabdoid tumor, and peripheral nerve schwannoma) show the same pattern: no mechanistic rationale, no trials, and no literature. In two cases (rhabdoid tumor, peripheral nerve schwannoma) the rationale even notes that leptin signaling is more plausibly tumor-promoting than tumor-suppressive, meaning a leptin agonist could theoretically work against the therapeutic goal. Taken together, this indication cluster should be treated as a low-confidence signal requiring independent validation before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Metreleptin is not currently marketed in Finland — no marketing authorizations are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication rests on evidence level L5 (model prediction only) with no clinical trials or literature support, and the mechanistic rationale itself questions the biological plausibility of the link. Combined with a Blocking data gap on the TFDA package insert (needed for any safety assessment) and an unresolved MOA, this candidate cannot proceed past initial screening (decision_stage S0).

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data via DrugBank API (DG002, High)
- Confirmation of metreleptin's original approved indication(s), currently absent from the dataset
- Independent mechanistic or preclinical evidence linking leptin signaling to familial generalized lentiginosis before any further investment in this candidate
- If pursuing other ranked candidates (rhabdoid tumor, peripheral nerve schwannoma), directional risk should be clarified first, since leptin agonism may plausibly promote rather than inhibit tumor growth in these contexts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

