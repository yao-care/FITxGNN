---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# LATANOPROST: Evaluation on Hold — No TxGNN Predictions Available

## One-Sentence Summary

LATANOPROST (DB00654) is a prostaglandin analogue with established clinical use in lowering intraocular pressure, though its original indication data was not retrieved in this Evidence Pack.
The current Evidence Pack contains **no TxGNN prediction results**, meaning there is no repurposing hypothesis to evaluate.
This report documents the data gaps and outlines the remediation steps required before a full evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved (empty in Evidence Pack) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | — |
| Evidence Level | N/A — predictions not yet run |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why This Evaluation Cannot Proceed

The Evidence Pack for LATANOPROST is missing two critical inputs required to run a repurposing evaluation:

**1. No TxGNN predictions available.**
The `predicted_indications` array in the Evidence Pack is empty. Without a predicted indication target, there is no repurposing hypothesis to score, no clinical trials to surface, and no mechanistic bridge to explain. The entire downstream evaluation framework depends on at least one TxGNN candidate indication.

**2. Mechanism of action data is absent.**
MOA data was flagged as a High-severity data gap (DG002). While latanoprost is broadly understood to be a prostaglandin F2α analogue that reduces intraocular pressure via increased aqueous humour outflow, the structured DrugBank MOA record needed for mechanistic cross-indication analysis was not retrieved. Without this, it is not possible to assess whether the mechanism is plausibly applicable to any new indication.

Additionally, TFDA package insert warnings and contraindications were flagged as a Blocking data gap (DG001), which would prevent a proper safety screening even if a predicted indication were available.

---

## Taiwan Market Information

Latanoprost is **not currently marketed in Taiwan**. No authorized products were found in the TFDA database (0 licenses). There is no local regulatory reference point for dosage form, approved indication text, or package insert.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions have been generated for LATANOPROST, and two blocking data gaps (regulatory safety data and MOA) remain unresolved. A meaningful repurposing evaluation cannot be produced from the current Evidence Pack.

**To proceed, the following is needed:**
- Run the TxGNN prediction pipeline for LATANOPROST (DB00654) to generate at least one candidate indication
- Retrieve MOA data from DrugBank API (remediation for DG002)
- Download and parse the TFDA package insert PDF to extract warnings and contraindications (remediation for DG001)
- Re-submit the completed Evidence Pack for a full evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

