---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog originally used to treat Type 1 and Type 2 diabetes mellitus. The TxGNN model predicts a possible link to **Autoimmune Oophoritis**, but this prediction currently has **no supporting clinical trials or literature**, and the underlying rationale describes only an indirect, disease-co-occurrence relationship rather than a treatment mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (Type 1 and Type 2) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% (model rank 1777) |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on known pharmacology, insulin glargine is a long-acting recombinant human insulin analog that provides basal glycemic control by activating the insulin receptor; its efficacy in diabetes mellitus is well established.

The proposed link to autoimmune oophoritis, however, is not a pharmacological treatment relationship. Autoimmune oophoritis is a component of autoimmune polyendocrine syndrome (APS) and can co-occur with Type 1 diabetes, but there is no direct mechanistic pathway by which insulin would treat ovarian autoimmune inflammation. The model's own rationale explicitly describes this as a "knowledge-graph proximity effect" driven by shared autoimmune/endocrine disease nodes, rather than a genuine drug-disease treatment signal.

Given this, the prediction should be interpreted as a hypothesis-generating signal only — it reflects disease co-occurrence patterns learned by the model, not evidence of therapeutic benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Insulin glargine currently has no registered marketing authorizations in Finland under this evidence pack (0 licenses on file; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert warnings, contraindications, and drug interaction data are flagged as a blocking data gap (DG001) in this evidence pack and could not be retrieved for this evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (autoimmune oophoritis) has an L5 evidence level — a model prediction only, with zero supporting clinical trials or literature, and the rationale explicitly identifies the link as an indirect co-occurrence artifact rather than a treatment mechanism. This does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Fimea/TFDA package insert data (warnings, contraindications) — currently a blocking gap (DG001)
- Confirmed mechanism of action data (DG002)
- Targeted literature/trial search specifically on insulin and autoimmune oophoritis or APS-related ovarian failure to test whether any indirect supportive evidence exists
- Consider re-evaluating **pancreatic agenesis** (rank 6 in this candidate set) as an alternative direction: it carries a stronger mechanistic rationale (congenital β-cell absence requiring exogenous insulin) and has 6 associated literature records, though none directly studies this rare condition — it is currently staged at S1 with a "Research Question" recommendation rather than "Hold."
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

