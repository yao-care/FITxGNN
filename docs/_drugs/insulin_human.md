---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin Human is the physiological hormone replacement used for insulin-dependent diabetes mellitus.
The TxGNN model predicts it may be relevant to **Autoimmune Oophoritis**,
but this ranking currently has **no supporting clinical trials and no supporting literature** — the association appears to reflect a shared autoimmune comorbidity pattern rather than a direct treatment mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (well-established use; no local approved-indication text is available in this evidence pack) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for insulin human is not available in this evidence pack. Based on known clinical information, insulin human is the standard replacement therapy for insulin-dependent (Type 1) diabetes, restoring glucose uptake and metabolic regulation via the insulin receptor pathway.

Autoimmune oophoritis is one component of polyglandular autoimmune syndrome (APS) and can co-occur with Type 1 diabetes because the two conditions share an underlying autoimmune predisposition — not because insulin acts therapeutically on ovarian tissue. The TxGNN score most likely captures this comorbidity/co-occurrence pattern in the knowledge graph rather than a genuine pharmacological mechanism linking insulin to ovarian autoimmunity.

Given this, the prediction should be read as a hypothesis-generating signal only. No clinical trial, case report, or mechanistic study in the current evidence pack supports insulin as a treatment for autoimmune oophoritis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (autoimmune oophoritis) has zero clinical trials and zero literature support, and the proposed mechanistic link is a comorbidity association rather than a causal treatment pathway — this does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Direct mechanistic or preclinical evidence that insulin modulates ovarian autoimmune activity (not merely diabetes co-occurrence)
- At least one case series or observational study specifically evaluating insulin in autoimmune oophoritis
- TFDA/package-insert safety data (currently a blocking data gap — DG001) before any S1 safety screening can begin
- Formal MOA data from DrugBank (DG002) to support or refute the mechanistic rationale

**Note on other candidates in this evidence pack:** two lower-ranked predictions have notably stronger, direct mechanistic support than the top-ranked one and may warrant separate evaluation — *thiamine-responsive dysfunction syndrome* (rank 4) and *pancreatic agenesis* (rank 9), both scored "Proceed with Guardrails" because insulin is the established standard-of-care replacement therapy in the underlying genetic diabetes subtypes involved, even though formal trial data is still absent for both.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

