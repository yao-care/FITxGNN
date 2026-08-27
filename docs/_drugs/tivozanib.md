---
layout: default
title: Tivozanib
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: From Renal Cell Carcinoma to Endocervical Carcinoma

> **Note on data completeness**: This Evidence Pack does not populate `original_indications` or `original_moa` (both flagged as data gaps DG001/DG002, with DG001 rated *Blocking*). The original indication below is based on general pharmacological knowledge of tivozanib (a marketed VEGFR TKI for renal cell carcinoma) and requires confirmation against the TFDA/Fimea package insert before this report can be used for decision-making.

## One-Sentence Summary

Tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor originally developed for renal cell carcinoma. The TxGNN model predicts it may be effective for **Endocervical Carcinoma**, but currently **0 clinical trials** and **0 publications** support this specific direction — the signal is a pure graph-based prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (general knowledge; not present in evidence pack — data gap) |
| Predicted New Indication | Endocervical carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is marked as a data gap in this evidence pack. However, according to the repurposing rationale attached to the prediction, tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor that suppresses tumor angiogenesis.

Endocervical carcinoma, like renal cell carcinoma, can be angiogenesis-dependent, and other anti-angiogenic agents (e.g., bevacizumab) are already approved for advanced cervical cancer. This gives the prediction a plausible mechanistic analogy at the drug-class level.

That said, the link is derived purely from TxGNN's knowledge-graph similarity — there is no tivozanib-specific study, case report, or preclinical data in endocervical carcinoma to confirm the mechanism actually translates to clinical benefit in this tumor type.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Tivozanib currently has no marketing authorization in Finland (0 licenses on record); no product table is available.

## Cytotoxicity

Tivozanib is an antineoplastic agent (VEGFR tyrosine kinase inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR-1/2/3 tyrosine kinase inhibitor / anti-angiogenic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN graph score (L5, decision stage S0) with zero supporting clinical trials or literature across all 10 candidate gynecological indications queried, and the drug's own TFDA/Fimea label data is unresolved (a Blocking-severity gap).

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications, DDI) — currently Blocking gap DG001
- Confirmed original MOA and approved indication from DrugBank/regulatory source — DG002
- Preclinical or case-level evidence of VEGFR pathway relevance specifically in endocervical carcinoma before any trial-stage investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

