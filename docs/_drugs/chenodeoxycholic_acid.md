---
layout: default
title: Chenodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 5
---

# Chenodeoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the drug-repurposing evaluation report template to generate this report from the supplied Evidence Pack.

---

# Chenodeoxycholic Acid: From Bile Acid Metabolism Disorders to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Chenodeoxycholic acid (CDCA) is a naturally occurring primary bile acid; the evidence pack does not record a specific Taiwan/Finland-approved original indication for this compound, though it is historically associated with disorders of bile acid synthesis and cholesterol metabolism (e.g., gallstone dissolution, cerebrotendinous xanthomatosis).
> The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia**,
> with **0 clinical trials** and **1 publication** currently identified, and that publication addresses a related — not the same — disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug.original_indications is empty; original_moa is a data gap) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only for this indication; the sole related publication concerns a different, mechanistically adjacent disease) |
| Finland Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for chenodeoxycholic acid in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, CDCA is a primary bile acid involved in bile acid synthesis regulation; it has been used clinically in bile acid–related and cholesterol-metabolism–related disorders, which provides a plausible mechanistic bridge to lipid/cholesterol disease states.

The single retrieved publication (PMID 25424010) is a review of cerebrotendinous xanthomatosis (CTX) — a rare autosomal-recessive lipid storage disease caused by CYP27A1 mutations that disrupts bile acid synthesis and causes cholesterol/cholestanol accumulation. CTX is treated with CDCA replacement, and the underlying biology (defective bile acid/cholesterol handling) is conceptually related to homozygous familial hypercholesterolemia (HoFH), which also involves severe disruption of cholesterol regulation. This overlap in cholesterol-pathway biology is a reasonable basis for the TxGNN model's association, but it should be treated as a mechanistic hypothesis rather than direct evidence, since no study in the pack examines CDCA specifically in HoFH patients.

Because original_moa and original_indications are not populated in this evidence pack, mechanistic linkage strength cannot be fully assessed; this is recorded as data gap DG002 and should be resolved via DrugBank/product labeling before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Review | Orphanet Journal of Rare Diseases | Comprehensive review of cerebrotendinous xanthomatosis (CTX), a CYP27A1-mutation bile acid synthesis disorder causing cholestanol accumulation; CDCA is the established replacement therapy for CTX. Disease is mechanistically related to, but distinct from, homozygous familial hypercholesterolemia. |

## Finland Market Information

Chenodeoxycholic acid is not currently marketed in Finland — `taiwan_regulatory.market_status` is "未上市" (Not Marketed) with 0 registered authorizations, so no authorization/product table is available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all recorded as data gaps in this evidence pack — TFDA labeling review, flagged DG001, is a Blocking-severity gap.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials for this predicted indication, no Taiwan/Finland market presence, and the single supporting publication addresses a related but distinct disease (CTX, not HoFH). Combined with a Blocking-severity data gap on TFDA labeling, the evidence base is currently insufficient to advance beyond model prediction.

**To proceed, the following is needed:**
- TFDA/EMA package insert (warnings, contraindications) — resolves blocking gap DG001
- DrugBank/MOA detail on CDCA's mechanism relevant to lipid metabolism — resolves gap DG002
- Dedicated clinical or preclinical studies of CDCA specifically in HoFH or related dyslipidemia populations
- DDI data query resolution (current status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

