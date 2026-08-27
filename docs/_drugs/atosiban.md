---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: Repurposing Evaluation — Insufficient Data to Proceed

## One-Sentence Summary

Atosiban (DrugBank ID: DB09059) is an oxytocin/vasopressin receptor antagonist, widely known as a tocolytic agent for the management of preterm labor (approved in the EU under the brand name Tractocile).
The current Evidence Pack contains **no TxGNN-predicted new indications**, and critical data gaps in mechanism of action and safety information prevent a full repurposing evaluation.
**The recommended decision is Hold** until data collection is complete.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Known tocolytic for preterm labor (not registered in Taiwan) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction not generated; no supporting studies |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Atosiban is a competitive antagonist of the oxytocin and vasopressin V1a receptors. By blocking oxytocin-induced uterine contractions, it is used clinically to delay imminent preterm birth between 24–33 weeks of gestation. It has been approved in the European Union, but is not registered in Taiwan.

No TxGNN predicted indications were generated for this candidate. This may reflect missing molecular features, insufficient input data fed into the model, or the drug's narrow receptor profile limiting cross-disease applicability. Without predicted indications, a mechanistic bridge to any new disease cannot be assessed.

A full repurposing rationale will become possible once the TxGNN pipeline is re-run with complete drug features, and the mechanism of action data is retrieved from DrugBank.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for new indications.

---

## Literature Evidence

Currently no related literature available for new indications.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Atosiban contains no TxGNN-predicted new indications and has blocking-level data gaps in safety information and mechanism of action; a repurposing evaluation cannot be responsibly conducted at this stage.

**To proceed, the following is needed:**

- **TxGNN model re-run**: Generate predicted indications using complete drug feature input (DrugBank molecular profile, target annotations)
- **Mechanism of action (MOA)**: Retrieve from DrugBank API (DB09059) — flagged as High severity data gap
- **Safety data**: Download and parse the TFDA or EMA/EU package insert to extract key warnings, contraindications, and drug-drug interactions — flagged as Blocking severity data gap
- **Evidence collection**: Once a predicted indication is available, run clinical trial and literature queries (ClinicalTrials.gov, PubMed) scoped to the new target disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

