---
layout: default
title: Talimogene Laherparepvec
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
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

# Talimogene Laherparepvec: From Unresectable Cutaneous Melanoma to CMM7 (Cutaneous Malignant Melanoma Locus)

## One-Sentence Summary

Talimogene laherparepvec (T-VEC) is a GM-CSF-armed, ICP34.5/ICP47-deleted HSV-1 oncolytic virus originally developed for unresectable cutaneous, subcutaneous and nodal melanoma lesions. The TxGNN model's top prediction, **CMM7** (a cutaneous malignant melanoma susceptibility locus), scores **99.20%** but is currently backed by **0 clinical trials** and **0 publications** in this evidence pack. Because "CMM7" essentially names the same disease class the drug is already known to be approved for elsewhere, this candidate reads more as a data-gap artifact than a genuine new indication — the registry shows the drug as "not marketed" and lists no original indication, which conflicts with T-VEC's known real-world approval (Imlygic) and should be reconciled before any decision is finalized.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this registry (market status shows "not marketed," no license text) — known global approved use is unresectable cutaneous/subcutaneous/nodal melanoma; this is a data gap needing reconciliation |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma, locus nomenclature) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 (mechanism-based reasoning only; no supporting trials or literature) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in this record, but the repurposing rationale supplied with the prediction describes it: T-VEC is a GM-CSF-modified HSV-1 oncolytic virus (ICP34.5/ICP47-deleted) that, upon intratumoral injection, selectively lyses tumor cells and triggers a systemic anti-tumor immune response.

CMM ("Cutaneous Malignant Melanoma") is a gene-locus naming convention for melanoma susceptibility, and it overlaps almost completely with T-VEC's known approved indication — unresectable cutaneous, subcutaneous, and lymph-node melanoma lesions. In other words, the model is not proposing a mechanistically novel indication so much as re-identifying the drug's existing disease class under a different name.

The evidence pack itself flags this: `original_indications` is empty and market status is "not marketed," which contradicts the well-established approval of Imlygic (T-VEC) for melanoma. This is judged to be a data-completeness gap in the source registry rather than a mechanistic failure — the underlying biology strongly supports the link, but the administrative record needs correction before this can be treated as an actionable "new" indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Cytotoxicity

*(Included because T-VEC targets melanoma and is administered as an oncolytic viral immunotherapy for cancer.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (oncolytic virus therapy) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions (live, replication-competent virus — biosafety handling precautions for injection preparation and disposal are typically required for this drug class) |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (CMM7) has zero supporting clinical trials or literature and the drug's own regulatory record (original indication, MOA, TFDA labeling) is incomplete — including a blocking gap on package-insert warnings/contraindications needed for any safety review. The lower-ranked candidates (pediatric leptomeningeal melanoma, uveal melanoma, and several non-melanoma carcinomas) score similarly high but were already assessed as Hold due to blood-brain-barrier, tissue-accessibility, or histology mismatches — reinforcing that TxGNN's score here is driven by lexical/knowledge-graph similarity to "melanoma" rather than validated new biology.

**To proceed, the following is needed:**
- Resolve the original-indication/market-status discrepancy by pulling the actual Imlygic (T-VEC) approval record (Fimea/EMA) to correct `original_indications` and `market_status`
- Obtain the TFDA/EMA package insert for key warnings, contraindications, and DDI data (currently blocking safety review)
- Retrieve confirmed mechanism-of-action documentation from DrugBank or the manufacturer label
- If CMM7 is intended as a genuinely distinct target population, define it precisely and search for dedicated trials/literature under that specific term rather than relying on melanoma-adjacent scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

