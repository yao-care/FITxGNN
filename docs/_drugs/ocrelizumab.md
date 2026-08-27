---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody approved for multiple sclerosis, acting by depleting CD20-expressing B cells.
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
but currently **0 clinical trials** and **0 relevant publications** support this specific link — the evidence pack itself flags the prediction as a likely knowledge-graph embedding artifact rather than a mechanism-driven signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (per drug background; formal DrugBank/MOA record is a data gap) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap). Based on known background information, ocrelizumab is an anti-CD20 monoclonal antibody that depletes CD20-positive B cells and is approved for multiple sclerosis, an autoimmune disease driven by aberrant B-cell activity.

HER2-positive breast carcinoma, by contrast, is driven by HER2/neu receptor overexpression fueling proliferative signaling pathways — a mechanism with no established biological link to B-cell depletion. The evidence pack's own repurposing rationale is explicit on this point: it assesses the high TxGNN score as most likely reflecting proximity in the knowledge-graph embedding space rather than any true mechanistic connection.

No supporting mechanistic, preclinical, or clinical rationale bridges CD20-targeted B-cell depletion to HER2-driven tumor biology. This prediction should be treated as a candidate for further model-validation research, not as a pharmacologically grounded hypothesis at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/Fimea package insert warnings and contraindications are currently a **Blocking** data gap (DG001) and must be resolved before any safety pre-assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Across all five TxGNN-predicted indications for this candidate (all breast cancer subtypes — HER2-positive, normal-like, PR-positive, luminal A/B, PR-negative), there is no supporting clinical trial or credible literature evidence. The one literature hit found (19 papers retrieved for "breast tumor luminal A or B") is a false-positive keyword match on the letter "B" (hepatitis B vaccines, HLA-B typing, B-1/B-2 lymphocyte biology) with no actual relevance to breast cancer or ocrelizumab. The evidence pack's own analysis concludes the high prediction scores likely reflect knowledge-graph embedding proximity rather than a real mechanistic signal. Combined with the blocking absence of TFDA/Fimea safety data, this candidate does not currently meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently blocking
- Formal mechanism of action record from DrugBank
- Preclinical/in vitro evidence evaluating any role of CD20+ B cells in HER2-driven or other breast cancer subtypes
- Targeted literature search using breast-cancer-specific and ocrelizumab-specific terms to rule out further keyword-driven false positives across the other four ranked candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

