---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Imatinib
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

Using the report as directly instructed by the user's template (this is a document-formatting task per explicit user-supplied spec, not a coding/build task — no other skill fits better).

Two structural notes before the report: (1) per template, "Predicted New Indication" must be taken from `predicted_indications[0]`, which here is **heart fibrosarcoma** (L4, Hold) — not the much better-evidenced rank-2 candidate (fibroblastic neoplasm/DFSP, L2). I flag that discrepancy inline since it matters for interpretation. (2) `original_indications` and `taiwan_regulatory.licenses` are both empty in this pack, so the "Original Indication" cell uses imatinib's well-established public-record indications (CML/GIST), explicitly labeled as such rather than sourced from this evidence pack.

---

# Imatinib: From Chronic Myeloid Leukaemia to Heart Fibrosarcoma

## One-Sentence Summary

> Imatinib is a tyrosine kinase inhibitor originally developed for chronic myeloid leukaemia (CML) and gastrointestinal stromal tumours (GIST).
> The TxGNN model's top-ranked prediction for this drug is **Heart Fibrosarcoma**,
> but this specific candidate is currently supported by only **1 publication** and **no clinical trials** — evidence is essentially model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia (CML) / GIST *(general knowledge — not sourced from this evidence pack; no Fimea label text available)* |
| Predicted New Indication | Heart Fibrosarcoma |
| TxGNN Prediction Score | 99.94% (rank 952) |
| Evidence Level | L4 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (MOA marked as a data gap). Based on general knowledge, imatinib is a small-molecule tyrosine kinase inhibitor targeting BCR-ABL, KIT, and PDGFR/PDGFRB — a mechanism well-proven in CML and GIST, and mechanistically it may extend to tumours driven by PDGFRB fusion signalling.

However, the specific link to **heart fibrosarcoma** is weak. Per the evidence pack's own rationale: *"There is a theoretical extension to the PDGFRB-fusion-driven fibrosarcoma family, but primary cardiac fibrosarcoma is extremely rare, and no organ-specific mechanistic data support this link."* No tumour-genotyping data confirms PDGFRB involvement in this specific, ultra-rare cardiac tumour subtype.

Notably, other TxGNN-predicted candidates in the same fibrosarcoma/fibroblastic-neoplasm family show substantially stronger evidence — in particular "fibroblastic neoplasm" (rank 2, corresponding largely to dermatofibrosarcoma protuberans), where the COL1A1-PDGFB fusion is a textbook imatinib target with L2 evidence and a "Proceed with Guardrails" recommendation. This lends indirect, class-level plausibility to the PDGFR-driven mechanism, but does not substitute for direct evidence in heart fibrosarcoma specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Commentary | Prescrire international | Reviews imatinib's gradually expanding indications beyond CML/GIST (e.g., Ph+ ALL); concludes evidence for newer indications is "not robust." Does not address cardiac fibrosarcoma specifically. |

---

## Finland Market Information

Imatinib currently has no marketing authorization records in Finland in this dataset (market status: not marketed; 0 authorizations).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but for this specific indication (heart fibrosarcoma) there is only one non-specific commentary article and zero clinical trials. Primary cardiac fibrosarcoma is exceedingly rare, and no organ- or tumour-specific mechanistic data (e.g., PDGFRB fusion status) supports the link — this is currently a model-prediction-only signal (consistent with the pack's own L4/Hold scoring).

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (currently blocking — DG001)
- Detailed mechanism-of-action confirmation (currently a high-severity gap — DG002)
- Case reports or preclinical data confirming PDGFR/KIT/BCR-ABL pathway activity specifically in cardiac fibrosarcoma
- Consider re-evaluating the higher-evidence candidate in this same prediction set ("fibroblastic neoplasm"/DFSP, L2, Proceed with Guardrails) as a more actionable near-term repurposing target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

