---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 6
---

# Rasagiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rasagiline: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Rasagiline is a selective, irreversible MAO-B inhibitor established for treating Parkinson's disease.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but this prediction is currently supported by **no clinical trials** and **no published literature** — it rests on model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (based on known pharmacological classification; not documented in Finland regulatory data as the drug is unmarketed there) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, rasagiline is a selective, irreversible monoamine oxidase type B (MAO-B) inhibitor used in Parkinson's disease, where it reduces dopamine breakdown in the central nervous system and has been studied for possible neuroprotective and antioxidant effects beyond simple symptomatic control.

PLA2G6-associated neurodegeneration (part of the NBIA/INAD disease spectrum caused by PLA2G6 gene mutations) shares clinical overlap with Parkinson's disease: certain adult-onset forms present with a dystonia-parkinsonism phenotype, and the underlying pathology involves iron accumulation, mitochondrial dysfunction, and membrane phospholipid metabolism disturbances.

The rationale for this prediction is therefore mechanistically plausible but highly indirect — rasagiline's MAO-B inhibition and theoretical neuroprotective properties could conceivably slow neurodegenerative processes, but there is no direct molecular link to PLA2G6 pathology, and the connection is inferred purely from phenotypic (parkinsonism) similarity rather than confirmed shared mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

No marketing authorizations currently exist in Finland — rasagiline is not marketed in this market (total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (evidence level L5) with zero clinical trials, zero literature, and no confirmed mechanistic link to PLA2G6-associated neurodegeneration — evidence is insufficient to advance beyond exploratory screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/regulatory package insert data (warnings, contraindications) — currently a Blocking data gap preventing safety pre-assessment
- Preclinical or mechanistic studies directly linking MAO-B inhibition to PLA2G6-related neurodegeneration pathology
- Case reports or observational data in NBIA/INAD spectrum patients, if any exist
- Drug interaction (DDI) profile, since none is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

