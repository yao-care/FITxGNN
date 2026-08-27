---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is a next-generation ALK/ROS1 tyrosine kinase inhibitor originally developed for ALK-positive non-small cell lung cancer (NSCLC). The TxGNN model's top-ranked prediction proposes potential relevance to **Fibromatosis, Gingival**, a benign connective-tissue overgrowth condition, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale identifies no known biological link between the two.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC)* |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% (global rank 1633) |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Formal `original_indications` and `original_moa` fields are marked as data gaps in this evidence pack (DG002). The original indication above is inferred from literature embedded in this pack's lower-ranked candidates (see Rank 5), not from a coded source field.

## Why is This Prediction Reasonable?

Brigatinib's formal mechanism-of-action record is flagged as a data gap in this evidence pack (DG002, High severity). Based on literature embedded elsewhere in this pack, brigatinib is known to act as a next-generation ALK/ROS1 tyrosine kinase inhibitor with activity against certain EGFR mutations, and its efficacy in ALK-positive NSCLC is well established through completed Phase 3 trials (e.g., ALTA-1L, ALTA-3).

Gingival fibromatosis, however, is a benign connective-tissue overgrowth disorder with no known driver-kinase pathology, and it is not associated with ALK, ROS1, or EGFR signaling. The evidence pack's own mechanistic rationale for this prediction states explicitly that there is "no known mechanistic association" between the drug's kinase-inhibition activity and this disease.

Because both the mechanistic rationale and the evidentiary record (zero trials, zero literature) point away from plausibility, this rank-1 prediction should be treated as a low-confidence model artifact rather than a genuine repurposing signal, and no further action is warranted at this time beyond monitoring.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Brigatinib is not currently marketed in Finland — no authorizations are on record (0 licenses).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 predicted indication (gingival fibromatosis) has zero supporting clinical trials or literature, and the model's own mechanistic rationale confirms no known biological link to brigatinib's ALK/ROS1 kinase-inhibition activity — this is an L5, model-only signal with no real-world corroboration.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings, contraindications, and DDI data (DG001, Blocking — currently missing entirely)
- Confirmed DrugBank mechanism-of-action and drug categorization (DG002)
- If repurposing research continues, re-triage the pack's lower-ranked candidates with actual literature (Ranks 5, 8, 10) — their disease labels appear to be ontology mismatches masking genuine ALK-inhibitor evidence (e.g., NF2-related schwannomatosis under Rank 10) that may be more promising than the top-ranked candidate
- Any preclinical or mechanistic data specifically linking ALK/ROS1/EGFR pathways to gingival fibromatosis pathology, since none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

