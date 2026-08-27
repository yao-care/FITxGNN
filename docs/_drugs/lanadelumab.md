---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: Evidence Pack Incomplete — Repurposing Evaluation Pending

## One-Sentence Summary

Lanadelumab (DrugBank: DB14597) has been queried through the data pipeline, but the current Evidence Pack contains **no original indication data**, **no TxGNN predicted indications**, and **two unresolved data gaps** (one Blocking, one High severity).
A full repurposing evaluation cannot be completed until these gaps are remediated — this report documents the current data state and outlines the steps required to proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | — (no data retrieved) |
| Predicted New Indication | — (TxGNN predictions not yet generated) |
| TxGNN Prediction Score | — |
| Evidence Level | N/A — prediction pipeline has not produced output |
| Finland Market Status | Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Mechanistic Analysis Is Possible

Currently, detailed mechanism of action data is not available for Lanadelumab in this Evidence Pack.

Two data gaps block the mechanistic reasoning step:

- **DG002 (High severity)** — MOA is missing from the DrugBank query results. Without this, it is impossible to draw a mechanistic link between any original indication and a predicted new indication.
- **DG001 (Blocking severity)** — TFDA package insert warnings and contraindications have not been parsed. This prevents the mandatory Safety Pre-Screen (S1) from running.

Until DG001 is resolved, the pipeline **cannot advance to safety evaluation**. Until DG002 is resolved, any predicted indication cannot be assessed for biological plausibility.

---

## Finland Market Information

Lanadelumab is not currently marketed in Finland. No marketing authorizations were found in the regulatory query conducted on 2026-03-29.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack has zero predicted indications and contains a Blocking-severity data gap (missing regulatory safety data), making it technically and ethically premature to issue any repurposing recommendation.

**To proceed, the following is needed:**

1. **[DG001 — Blocking]** Download the TFDA package insert PDF for Lanadelumab and parse warnings, contraindications, and special population restrictions. This is a prerequisite before any safety pre-screen can run.
2. **[DG002 — High]** Query DrugBank API (`/drugs/DB14597`) to retrieve the mechanism of action, pharmacodynamics, and drug categories. This is required for mechanistic plausibility analysis.
3. **Re-run the TxGNN prediction pipeline** for DB14597 to generate `predicted_indications` with scores, supporting clinical trials, and literature.
4. Once predictions are available, re-generate this Evidence Pack (v5+) and run a full L1–L5 evidence evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

