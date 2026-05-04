---
layout: default
title: Larotrectinib Sulfate
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Larotrectinib Sulfate
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

# Larotrectinib Sulfate: From NTRK Fusion-Positive Solid Tumors — No TxGNN Predictions Available

## One-Sentence Summary

Larotrectinib sulfate (Vitrakvi) is a first-in-class selective TRK inhibitor approved in the US and EU for adult and paediatric patients with NTRK gene fusion-positive solid tumours, regardless of tumour histology.
However, the current Evidence Pack contains **no TxGNN-predicted new indications** and is missing critical fields including original indication records, mechanism of action details, and all safety data.
A **Hold** decision is recommended until the data gaps are resolved and the prediction pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory records found (not marketed in Taiwan; approved in US/EU outside this system's scope) |
| Predicted New Indication | Not available — TxGNN returned no predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Taiwan Market Status | ✗ Not marketed (0 licenses) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is No Prediction Available?

Larotrectinib sulfate is a highly selective, pan-TRK inhibitor that targets TRKA, TRKB, and TRKC — the protein products encoded by the *NTRK1*, *NTRK2*, and *NTRK3* genes. Its unique tumour-agnostic approval (FDA 2018, EMA 2019) means it is indicated for any solid tumour harbouring an NTRK gene fusion, irrespective of the tissue of origin. This mechanism is fundamentally different from most small-molecule oncology drugs whose activity is histology-bound.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, Larotrectinib sulfate belongs to the kinase inhibitor class; its efficacy in NTRK fusion-positive solid tumours has been proven in multiple basket trials (LOXO-TRK-14001, SCOUT, NAVIGATE), and mechanistically it may be applicable to any tumour type where aberrant TRK signalling is the driver oncogenic event.

The absence of TxGNN predictions in this pack most likely reflects a data pipeline issue — either the drug was not matched to a node in the Knowledge Graph, or the NTRK fusion-positive biomarker-gated indication could not be encoded as a standard disease node. This should be investigated before drawing any conclusion about the drug's repurposing potential.

---

## Clinical Trial Evidence

Currently no related clinical trial evidence is available in this Evidence Pack.

> **Note:** This reflects missing data in the pipeline, not an absence of trials. Larotrectinib has been studied in multiple Phase 1/2 basket trials (NCT02122913, NCT02637687, NCT02576431). The evidence collection step should be re-run once the TxGNN prediction pipeline produces output.

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

---

## Taiwan Market Information

No Taiwan regulatory authorizations found for Larotrectinib Sulfate.

---

## Cytotoxicity

Larotrectinib sulfate is an antineoplastic targeted therapy (TRK inhibitor). Because no safety data was returned in this Evidence Pack, the following is a general assessment based on the drug class:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Selective TRK kinase inhibitor) |
| Myelosuppression Risk | Low to moderate — please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low (oral targeted agent) |
| Monitoring Items | Liver function tests (ALT/AST), neurological assessment (dizziness, paraesthesia), weight and nutritional status in paediatric patients |
| Handling Protection | Standard oral antineoplastic handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in this Evidence Pack are currently flagged as data gaps:

- TFDA package insert warnings and contraindications were not successfully parsed (Data Gap DG001 — **Blocking severity**)
- Drug–drug interaction data: no interactions found in the DDI database query

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is incomplete — there are no TxGNN-predicted indications, no original indication records, no MOA data, and no safety data. No repurposing evaluation can be performed in the current state.

**To proceed, the following is needed:**

- [ ] **Resolve DG001 (Blocking):** Download and parse the TFDA package insert PDF to extract warnings and contraindications
- [ ] **Resolve DG002 (High):** Retrieve MOA data from DrugBank API using the DrugBank ID for Larotrectinib (DB12703)
- [ ] **Investigate TxGNN pipeline failure:** Confirm whether Larotrectinib is mapped to a node in the Knowledge Graph; if not, add NTRK-pathway mappings and re-run the prediction step
- [ ] **Re-run evidence collection:** Once TxGNN produces `predicted_indications`, trigger the ClinicalTrials.gov and PubMed evidence collection steps
- [ ] **Consider scope clarification:** Larotrectinib's approved indication is biomarker-gated (NTRK fusion-positive); the repurposing question may need to be reframed as "which additional NTRK fusion-positive tumour types?" rather than a standard disease-level prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

