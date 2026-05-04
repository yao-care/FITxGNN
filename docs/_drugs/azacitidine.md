---
layout: default
title: Azacitidine
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 0
---

# Azacitidine
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

# Azacitidine: Repurposing Analysis — Evidence Pack Incomplete

## One-Sentence Summary

Azacitidine is a pyrimidine nucleoside analogue (hypomethylating agent) indicated for myelodysplastic syndromes (MDS) and acute myeloid leukemia (AML). **This Evidence Pack contains no TxGNN-predicted new indications**, and critical data — including mechanism of action and safety warnings — could not be retrieved. A complete repurposing evaluation cannot be issued until the data gaps listed below are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myelodysplastic Syndromes (MDS) / Acute Myeloid Leukemia (AML) |
| Predicted New Indication | Not available — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Taiwan Market Status | Not marketed (TFDA: 0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is the Analysis Incomplete?

This Evidence Pack is missing two categories of data that are required before any repurposing evaluation can proceed:

**1. TxGNN Predicted Indications**
The `predicted_indications` field is an empty array. TxGNN model output is the primary signal driving candidate selection in this pipeline. Without predictions, there is no new indication to evaluate, rank, or recommend. This is the most critical missing input.

**2. Mechanism of Action (MOA)**
MOA data was not retrieved into this Evidence Pack (DG002, severity: High). From pharmacological literature, azacitidine is known to act as a DNA hypomethylating agent — it incorporates into DNA and RNA, inhibits DNA methyltransferase (DNMT), and thereby reactivates silenced tumour suppressor genes, inducing cancer cell differentiation or apoptosis. However, because this information is not formally confirmed in the Evidence Pack, mechanistic plausibility analysis for any future predicted indication cannot be systematically validated against structured data.

---

## Taiwan Market Information

Per the TFDA query in this Evidence Pack (query date: 2026-03-29), azacitidine currently has **no market authorizations on record in Taiwan**. The query returned 0 results.

> **Note for cross-border context:** In the EU/EMA market, azacitidine (Vidaza®, Onureg®) holds approved indications for MDS, AML, and chronic myelomonocytic leukemia (CMML). If this report is intended for the Finnish (Fimea) market, a separate Fimea regulatory query is required to confirm current market status.

---

## Cytotoxicity

Azacitidine is an antineoplastic agent. Even without full Evidence Pack data, its pharmacological class (pyrimidine nucleoside analogue / DNA hypomethylating agent) permits the following classification:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Epigenetic modifier (DNA hypomethylating agent) |
| Myelosuppression Risk | **High** — neutropenia, thrombocytopenia, and anaemia are common dose-limiting toxicities |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential (at minimum before each cycle), serum creatinine, liver function tests, serum bicarbonate |
| Handling Protection | Must follow cytotoxic drug handling regulations (closed-system transfer devices, full PPE) |

---

## Safety Considerations

Please refer to the package insert for safety information.

All safety fields (key warnings, contraindications, drug interactions) returned no data in this Evidence Pack. The TFDA package insert query was logged as successful (query ID 4), but no content was parsed into the structured fields. The DDI query returned `not_found`.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack for Azacitidine (DB00928) is critically incomplete across all three key evaluation domains — predicted indications, mechanism of action, and safety data. Issuing a repurposing recommendation without these inputs would not meet minimum evidence standards.

**To proceed, the following is needed:**

1. **Run TxGNN predictions** for Azacitidine (DB00928) to populate the `predicted_indications` field — this is blocking for all downstream analysis
2. **Retrieve MOA data from DrugBank API** (resolves DG002) — required for mechanistic plausibility assessment
3. **Parse the TFDA package insert** (resolves DG001) — the PDF was located (query ID 4 returned success) but warnings and contraindications were not extracted into structured fields
4. **Verify DDI coverage** — the DDI query returned `not_found`; cross-check against DrugBank interaction database or other DDI sources
5. **Confirm Finland/Fimea market status separately** if this candidate is intended for the Finnish repurposing pipeline, as TFDA and Fimea regulatory records are independent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

