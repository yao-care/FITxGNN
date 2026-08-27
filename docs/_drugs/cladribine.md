---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside (deoxyadenosine) analog historically used to treat hairy cell leukemia, acting through selective cytotoxicity to lymphocytes and monocytes via DNA double-strand breaks.
The TxGNN model predicts possible activity against **Parameningeal Embryonal Rhabdomyosarcoma** (score **99.77%**), but this is currently a **pure graph-based association** — **0 clinical trials** and **0 publications** support this specific prediction, and no mechanistic link between cladribine's known biology and rhabdomyosarcoma has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy cell leukemia *(general drug knowledge; no license/indication record present in evidence pack)* |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% (rank 2900) |
| Evidence Level | L5 — model prediction only, no clinical or literature support |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured MOA data was not available in the evidence pack (`original_moa: [Data Gap]`). However, the model's own rationale field describes cladribine as a lymphocyte/monocyte-selective cytotoxic deoxyadenosine analog, working through DCK-mediated phosphorylation and induction of DNA double-strand breaks — this is consistent with its established clinical role in hairy cell leukemia, a lymphoid/monocytic hematologic malignancy.

Parameningeal embryonal rhabdomyosarcoma, in contrast, is a skeletal-myoblast-lineage solid tumor with a fundamentally different cell of origin and proliferative biology. The evidence pack's own repurposing rationale explicitly states there is **no known direct mechanistic connection** between cladribine's lymphocyte-targeted cytotoxicity and rhabdomyosarcoma pathogenesis — the high TxGNN score reflects a graph-relationship prediction, not a validated pharmacological hypothesis.

This pattern is consistent across all 7 ranked predictions in this evidence pack (5 rhabdomyosarcoma subtypes, rhabdomyosarcoma as a general category, and liver sarcoma) — all are scored L5/Hold, and none have supporting mechanistic rationale. The single literature hit found anywhere in this evidence pack (PMID 15241520, under rank 7 "liver sarcoma") concerns cladribine's use in smoldering systemic mastocytosis — a hematologic mast-cell disorder, not a sarcoma — and does not constitute relevant supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Cytotoxicity

Cladribine is a conventional cytotoxic antineoplastic (purine nucleoside/deoxyadenosine analog, antimetabolite class), currently used in hematologic malignancy treatment.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — purine nucleoside (deoxyadenosine) analog / antimetabolite |
| Myelosuppression Risk | Mechanistically expected to be significant, as the drug's activity depends on selective lymphocyte/monocyte depletion via DNA double-strand breaks; no quantified hematologic toxicity data available in this evidence pack — please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (particularly lymphocyte count), liver and renal function |
| Handling Protection | Antineoplastic — cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert warnings and contraindications are recorded as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has L5 evidence only — a TxGNN association score with zero supporting clinical trials or literature, and no identified mechanistic link between cladribine's known lymphocyte/monocyte-selective cytotoxicity and rhabdomyosarcoma biology. All 7 predicted indications in this evidence pack share the same Hold status for the same reason. The drug is also not currently marketed in Finland, and safety/label data required for even a preliminary safety assessment (S1) is missing.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Verified original indication and MOA data from DrugBank (DG002)
- Preclinical or mechanistic studies specifically linking cladribine to rhabdomyosarcoma or sarcoma biology
- Drug-drug interaction data
- Re-screening of lower-ranked candidates as new trial/literature evidence accumulates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

