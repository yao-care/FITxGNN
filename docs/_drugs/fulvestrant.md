---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

> Fulvestrant (DB00947) is a selective estrogen receptor degrader most widely known for treating ER-positive breast cancer, though this Evidence Pack does not itself confirm an approved original indication or mechanism of action (data gap). The TxGNN model predicts it may be effective for **HIV infectious disease**, but currently only **0 clinical trials** and **1 tangentially related publication** support this direction, and that publication concerns a different retrovirus (HTLV-1), not HIV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in evidence pack — Fimea/TFDA label text unavailable (Data Gap DG001, Blocking) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002, High severity). Based on general pharmacological knowledge, fulvestrant is a selective estrogen receptor degrader (SERD) most commonly associated with hormone receptor–positive breast cancer, but this Evidence Pack does not itself supply confirmed original-indication or MOA data to validate that context.

Critically, the repurposing rationale explicitly generated for this prediction states that fulvestrant has **no known antiviral or immunomodulatory mechanism** that would map onto HIV infection. There is no plausible pharmacological pathway connecting estrogen receptor degradation to retroviral suppression or immune reconstitution in HIV disease.

The single supporting publication does not actually address HIV — it is a cross-omics/bioinformatics analysis of HTLV-1-associated myelopathy (HAM), a distinct retrovirus with a different clinical syndrome (neuroinflammatory, not immunodeficiency). It is a data-mining/systems-biology study, not evidence of a drug intervention, and its relevance to this prediction is marked "pending." This pattern — a very high TxGNN score with no corroborating mechanism or clinical evidence — is characteristic of a network-based prediction artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics/Bioinformatics (preprint, Tier 3) | Research Square | Multi-cohort (epi)genomic analysis of HTLV-1-associated myelopathy (HAM), a neuroinflammatory disease caused by a different retrovirus than HIV; identifies disease mechanisms/targets for HAM, not HIV, and does not evaluate fulvestrant as an intervention |

---

## Finland Market Information

Fulvestrant is not currently marketed in Finland — no authorization records are available in the evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical trial evidence, no mechanistic rationale linking fulvestrant's estrogen-receptor activity to HIV pathophysiology, and the only literature hit is about an unrelated retroviral disease (HTLV-1, not HIV). This is an L5 (model-prediction-only) evidence level with no supporting studies.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (currently blocked by DG001/DG002)
- A plausible antiviral or immune mechanism specific to HIV before further investment
- Any preclinical or in-vitro evidence directly testing fulvestrant against HIV
- Re-evaluation of lower-ranked predicted indications (e.g., rheumatoid arthritis, rank 6) where estrogen-pathway biology is at least mechanistically plausible, given available literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

