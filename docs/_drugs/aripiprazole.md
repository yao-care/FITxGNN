---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: From Psychiatric Disorders — New Indications Pending TxGNN Prediction

## One-Sentence Summary

Aripiprazole is a well-established atypical antipsychotic agent used globally for schizophrenia, bipolar disorder, and adjunctive treatment of major depressive disorder.
The current Evidence Pack contains **no TxGNN-predicted new indications**, as the prediction pipeline did not return results for DB01238.
Evaluation cannot be completed at this stage; a **Hold** decision is recommended until critical data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Bipolar disorder (general domain knowledge; not populated in data package) |
| Predicted New Indication | — (No predictions returned) |
| TxGNN Prediction Score | — |
| Evidence Level | Insufficient Data |
| Finland Market Status | Not Marketed *(see note below)* |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

> ⚠️ **Data Integrity Note:** Aripiprazole (brand name Abilify and generics) is among the most widely prescribed psychiatric agents in Europe and is routinely available in Finland. A result of zero authorizations strongly suggests a **data collection issue** rather than an actual absence from the Finnish market. The regulatory query should be re-run and verified before proceeding.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known clinical information, Aripiprazole is classified as an atypical antipsychotic with partial agonist activity at dopamine and serotonin receptors. Its efficacy in schizophrenia and mood disorders has been extensively established, and mechanistically it may be applicable to neurological and psychiatric comorbidities.

However, because **no TxGNN-predicted new indications were returned**, a full mechanism-to-indication mapping cannot be performed at this time. This section will be completed once predictions are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Aripiprazole (DB01238) is critically incomplete — no TxGNN predicted indications were returned, and both the mechanism of action and safety warning fields are unpopulated. No repurposing evaluation can proceed without at minimum one scored candidate indication.

**To proceed, the following is needed:**

- **\[Blocking\]** Re-run the TxGNN prediction pipeline for DB01238 and confirm it produces at least one scored candidate indication before regenerating the Evidence Pack
- **\[Blocking\]** Download and parse the regulatory authority package insert PDF to populate key warnings and contraindications (currently blocking safety screening Stage S1)
- **\[High\]** Query DrugBank API for mechanism of action (MOA) for DB01238 to enable mechanism-to-indication reasoning
- **\[High\]** Investigate the Finland authorization query returning zero results — cross-check against EMA/Fimea databases directly, as this result is inconsistent with known global market status of Aripiprazole
- Once the above gaps are resolved, regenerate the Evidence Pack (target version: v5) and re-submit for full evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

