---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

The `txgnn-pipeline` skill covers infrastructure management, not report generation — my system prompt already defines the report format. Proceeding directly to generate the report.

---

# Apixaban: Evidence Pack Incomplete — No Repurposing Candidates Identified

## One-Sentence Summary

Apixaban is a direct oral anticoagulant (Factor Xa inhibitor), widely used internationally for stroke prevention in atrial fibrillation and venous thromboembolism (VTE) treatment.
The current Evidence Pack (v4) returned **zero TxGNN-predicted new indications**, and critical inputs — including mechanism of action and safety data — remain unresolved.
This report is a triage placeholder; a full repurposing evaluation cannot proceed until the data gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | None identified |
| TxGNN Prediction Score | N/A |
| Evidence Level | — (no predictions to evaluate) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Predictions Are Available

The TxGNN model returned an empty `predicted_indications` list for Apixaban. Based on the query log, DrugBank was successfully queried (result_count: 1) but the pipeline did not produce scored candidates. Three likely causes:

1. **Missing original indications**: The `original_indications` field is empty, which may have caused the disease–drug graph traversal to start from an undefined anchor point, producing no candidate paths.
2. **MOA gap (DG002, High severity)**: Without mechanism of action data, TxGNN cannot build the mechanism-level similarity features used to score candidate disease links.
3. **Safety gate not cleared (DG001, Blocking severity)**: The TFDA package insert query returned a result but the warnings/contraindications were not parsed into the Evidence Pack. This blocking gap prevents the pipeline from advancing to safety pre-screening (S1), which may have halted the full workflow.

Until all blocking gaps are resolved and the TxGNN run is re-executed, no drug repurposing candidates can be evaluated.

---

## Taiwan Market Information

Apixaban has **no registered marketing authorizations** with the Taiwan FDA (TFDA). The drug is not commercially marketed in Taiwan under any product name as of the data cutoff (2026-04-20).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two unresolved data gaps — one Blocking (DG001: TFDA package insert safety data) and one High (DG002: MOA) — prevent even a preliminary evaluation. Additionally, the TxGNN model produced zero predictions, meaning there is no repurposing hypothesis to assess at this time.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN pipeline** after resolving DG001 and DG002 — the `predicted_indications` array must be populated before any evaluation can begin
- [ ] **Resolve DG001 (Blocking)**: Download and parse the TFDA package insert PDF to extract warnings and contraindications; this is required for S1 safety pre-screening
- [ ] **Resolve DG002 (High)**: Query DrugBank API for Apixaban's mechanism of action (Factor Xa inhibition pathway) and populate `original_moa`
- [ ] **Populate `original_indications`**: Add the approved indication list (e.g., stroke prevention in non-valvular AFib, VTE treatment/prophylaxis) to provide TxGNN with correct graph anchor nodes
- [ ] **Re-run DDI query**: The DDI lookup returned `not_found`; verify whether this reflects a true absence of interaction data or a query failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

