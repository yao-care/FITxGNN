---
layout: default
title: Baloxavir Marboxil
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 0
---

# Baloxavir Marboxil
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

# Baloxavir Marboxil: Evaluation Report — Insufficient Data to Generate Repurposing Analysis

## One-Sentence Summary

Baloxavir marboxil (DB13997) is a drug for which original indication data and mechanism of action are currently unavailable in this Evidence Pack.
The TxGNN model returned **no predicted new indications** for this candidate, meaning no repurposing direction can be evaluated at this time.
This report documents the data gaps and provides a remediation roadmap before any clinical evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none exist) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The Evidence Pack contains an empty `predicted_indications` array. There are two likely causes:

**1. Upstream data gaps blocking the TxGNN pipeline.** The model requires a populated drug node in the knowledge graph, including mechanism-of-action edges and indication edges. With `original_moa` flagged as unavailable and no approved indications recorded for this drug in Taiwan, the graph embedding for Baloxavir marboxil may be insufficiently connected to generate confident disease-node predictions.

**2. No Taiwan regulatory footprint.** With zero TFDA licenses on file, the drug's pharmacological profile has not been formally characterised within the local data pipeline. Without this anchor, the integration step that merges regulatory data with TxGNN scores cannot produce output.

Until both gaps are resolved and the pipeline is re-run, repurposing evaluation cannot proceed.

---

## Taiwan Market Information

No authorization records found. Baloxavir marboxil is **not currently marketed in Taiwan** and has no registered licenses in the TFDA database as of the data cut-off date (2026-04-20).

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication, or drug-interaction data is available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions for this candidate, and critical upstream data — including mechanism of action and TFDA safety labelling — are absent. There is no evidence base on which to conduct a clinical or regulatory evaluation.

**To proceed, the following is needed:**

1. **Retrieve mechanism of action (MOA)** — Query the DrugBank API for DB13997 to populate pharmacological action, target, and pathway data; this is required for knowledge-graph edge generation.
2. **Retrieve TFDA package insert warnings and contraindications** — Download and parse the PDF from the TFDA official website to complete the safety profile (currently a blocking gap per DG001).
3. **Re-run the TxGNN prediction pipeline** — Once MOA and original indication data are populated, re-run the KG + DL + Mapping phases (Phase 2) to generate disease-node predictions.
4. **Confirm original approved indication** — Cross-check international sources (FDA, EMA, PMDA) to populate `original_indications`, as the Taiwan database returned zero results.
5. **Re-generate this Evidence Pack** — After steps 1–4, regenerate the v4 pack and submit for a full repurposing evaluation following the standard L1–L5 evidence-level framework.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

