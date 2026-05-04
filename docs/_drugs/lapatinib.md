---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: Drug Repurposing Evaluation Report

## One-Sentence Summary

Lapatinib is a dual tyrosine kinase inhibitor targeting HER2 (ErbB2) and EGFR (ErbB1), originally developed for HER2-positive advanced breast cancer.
**This Evidence Pack is critically incomplete: the `predicted_indications` field is empty**, meaning no TxGNN repurposing predictions are available for evaluation at this time.
Without a predicted new indication, a full repurposing analysis cannot be generated — a **Hold** decision applies until the Evidence Pack is completed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HER2-positive advanced or metastatic breast cancer (from domain knowledge; not present in Evidence Pack) |
| Predicted New Indication | **Not available** — `predicted_indications` is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | Cannot be determined |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (`original_moa: [Data Gap]`). Based on publicly known pharmacology, Lapatinib (DrugBank ID: DB01259) is a small-molecule, reversible dual inhibitor of the intracellular tyrosine kinase domains of HER2/ErbB2 and EGFR/ErbB1. By blocking downstream RAS/MAPK and PI3K/AKT signalling pathways, it inhibits tumour cell proliferation and survival in HER2-overexpressing cancers.

Because no TxGNN prediction exists in this Evidence Pack, it is not possible to assess mechanistic plausibility for any specific new indication. Once a target indication is provided by the prediction pipeline, the mechanistic link between HER2/EGFR signalling and that disease can be formally evaluated.

**This section will be completed once `predicted_indications` is populated.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

> *Reason: `predicted_indications` is empty. Clinical trial evidence is indication-specific and cannot be retrieved without a target disease.*

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

> *Reason: `predicted_indications` is empty. Literature evidence is indication-specific and cannot be retrieved without a target disease.*

---

## Finland Market Information

Lapatinib has **0 authorizations** in the regulatory database queried. The drug is currently **not marketed**.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No authorizations on record |

---

## Cytotoxicity

Lapatinib is an antineoplastic targeted therapy (HER2/EGFR dual tyrosine kinase inhibitor). The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — HER2/EGFR dual tyrosine kinase inhibitor |
| Myelosuppression Risk | Low to moderate (less myelosuppressive than conventional cytotoxics; neutropenia reported but less frequent) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs), cardiac function (LVEF), CBC, electrolytes (QTc monitoring required) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

> *All safety fields (`key_warnings`, `contraindications`, DDI) are marked as data gaps in the current Evidence Pack. The TFDA package insert query returned a result (query log ID 4, status: success), but the parsed content was not loaded into this Evidence Pack version. Remediation: parse the TFDA package insert PDF.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is missing the two most critical components for repurposing analysis — `predicted_indications` (TxGNN output) and `original_moa` — making it impossible to assess either the candidate indication or the mechanistic plausibility of the prediction.

**To proceed, the following is needed:**

- **[Blocking]** Run TxGNN prediction pipeline for DB01259 and populate `predicted_indications` with at least one candidate disease, including `txgnn.score`, `evidence.clinical_trials`, and `evidence.literature`
- **[High]** Retrieve Lapatinib MOA from DrugBank API (DrugBank query returned success with 1 result in query log ID 3 — this data should already be parseable)
- **[High]** Parse TFDA package insert PDF (query log ID 4 returned success) to extract `key_warnings` and `contraindications` and resolve data gaps DG001/DG002
- **[Medium]** Re-run DDI query with a broader search scope (current result: `not_found`; consider synonym or brand name search for Lapatinib/Tykerb)
- Once `predicted_indications` is populated, regenerate this report using Evidence Pack v5+
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

