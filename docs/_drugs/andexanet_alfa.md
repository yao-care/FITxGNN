---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Andexanet Alfa: Anticoagulant Reversal Agent — TxGNN Predictions Not Yet Available

## One-Sentence Summary

Andexanet alfa (Ondexxya/Andexxa) is a recombinant modified human Factor Xa decoy protein, approved internationally as a reversal agent for life-threatening or uncontrolled bleeding caused by Factor Xa inhibitors (apixaban, rivaroxaban).
The TxGNN model has **not yet generated predicted indications** for this drug in the current Evidence Pack — clinical trial and literature evidence tables are therefore unavailable.
This report documents the current data status and outlines the remediation steps required before a repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Reversal of anticoagulation due to Factor Xa inhibitors in life-threatening/uncontrolled bleeding (FDA/EMA approved; not yet registered in Finland) |
| Predicted New Indication | ⚠️ Not available — TxGNN predictions absent from Evidence Pack |
| TxGNN Prediction Score | — |
| Evidence Level | — (cannot determine without predicted indications) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (Data Gap DG002). Based on known pharmacological information, andexanet alfa is a catalytically inactive recombinant human Factor Xa variant. It acts as a "decoy receptor" that competitively binds and sequesters circulating Factor Xa inhibitors — including apixaban and rivaroxaban — thereby restoring endogenous thrombin generation and reversing anticoagulant effect.

Because the TxGNN model requires a mechanistic and graph-based evidence foundation to generate repurposing candidates, the absence of MOA data (DG002) and the lack of any predicted indications in this Evidence Pack means it is not currently possible to evaluate whether andexanet alfa's mechanism is applicable to any new indication.

Before a mechanistic repurposing rationale can be constructed, the two blocking data gaps (DG001: safety/package insert; DG002: MOA) must be resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a predicted new indication — TxGNN predictions are absent from this Evidence Pack.

---

## Literature Evidence

Currently no related literature available for a predicted new indication — TxGNN predictions are absent from this Evidence Pack.

---

## Finland Market Information

Andexanet alfa is not currently authorised or marketed in Finland. No licences on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No authorisations found |

> **Note:** Andexanet alfa is marketed in the United States as **Andexxa** (AstraZeneca/Pfizer) and in the EU as **Ondexxya** (AstraZeneca). An EMA marketing authorisation exists (EU/1/19/1404), but this drug has not been registered through Fimea for the Finnish market as of the data cut-off date.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Data Gap DG001 (Blocking):** Package insert warnings and contraindications data have not been parsed into the Evidence Pack. This gap must be resolved before any safety screening (S1 Safety Gate) can be performed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for andexanet alfa contains two unresolved data gaps — a blocking gap in safety/package insert data (DG001) and a high-severity gap in mechanism of action data (DG002) — and the TxGNN model has produced no predicted indications for this drug. Without predicted indications, there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

1. **Resolve DG001 (Blocking):** Download and parse the TFDA/Fimea package insert PDF to extract approved warnings, contraindications, and special population restrictions — required for S1 Safety Gate entry.
2. **Resolve DG002 (High):** Query the DrugBank API for andexanet alfa's full MOA, pharmacodynamics, and protein targets — required for mechanistic plausibility analysis.
3. **Re-run TxGNN pipeline:** Once MOA and safety data are populated, resubmit andexanet alfa through the TxGNN prediction pipeline to generate candidate disease indications with scores.
4. **Verify EMA/Fimea status:** Confirm whether Ondexxya's EMA authorisation has been extended to the Finnish market through the decentralised or mutual-recognition procedure, which would change the Finland Market Status from "Not marketed" to "Marketed."
5. **Re-evaluate Evidence Pack version:** Current version is v4 with `inputs_received: ["drugbank"]` only. A complete v5 pack should include TFDA/Fimea regulatory data, DDI data, and TxGNN predictions before the full report can be generated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

