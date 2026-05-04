---
layout: default
title: Avatrombopag Maleate
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 0
---

# Avatrombopag Maleate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Avatrombopag Maleate: Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Avatrombopag maleate is a thrombopoietin receptor agonist (TPO-RA) used to treat thrombocytopenia in adults.
The TxGNN model returned **no predicted new indications** for this drug in the current Evidence Pack, and key data fields including mechanism of action and safety information were not successfully populated.
This evaluation **cannot be completed** until the data pipeline gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved in this Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indications were returned by TxGNN for avatrombopag maleate in this Evidence Pack. Without a target indication, mechanistic bridging analysis cannot be performed.

Mechanism of action data was flagged as a data gap (severity: High) and was not populated despite a successful DrugBank query being logged. This prevents any assessment of whether the drug's pharmacology could plausibly extend to a new disease area.

From publicly available knowledge, avatrombopag maleate belongs to the TPO receptor agonist class and stimulates platelet production — but without TxGNN's candidate output, there is no repurposing hypothesis to evaluate at this stage.

---

## Finland Market Information

Avatrombopag maleate is currently **not marketed in Finland**. No Fimea authorizations are on record (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is critically incomplete — TxGNN returned no predicted indications, mechanism of action is missing, and safety data (warnings, contraindications, DDI) was not retrieved. There is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for avatrombopag maleate and confirm candidate indications are written to `predicted_indications`
- **Retrieve MOA from DrugBank** — a successful query was logged (result\_count: 1) but data was not propagated into the Evidence Pack; investigate the parsing step
- **Parse package insert** — TFDA package insert query also returned 1 result (result\_count: 1) but warnings and contraindications remain empty; check PDF extraction logic
- **Confirm original approved indication** from Fimea / EMA regulatory filings to establish the repurposing baseline
- Once the above are resolved, re-generate the Evidence Pack (v5+) and resubmit for full evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

