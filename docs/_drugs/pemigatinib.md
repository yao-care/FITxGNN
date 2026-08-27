---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From Undocumented Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

> The evidence pack for pemigatinib does not include original indication data, though the drug is characterized elsewhere in this pack as a selective FGFR1/2/3 kinase inhibitor.
> The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**,
> but this direction currently has **0 clinical trials** and **0 publications** supporting it, and the model's own rationale flags a lack of mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for pemigatinib in this evidence pack (flagged as a High-severity data gap). Based on information embedded elsewhere in the pack's repurposing rationales, pemigatinib is consistently described as a **selective FGFR1/2/3 kinase inhibitor**, consistent with its classification (in an independently retrieved review) among FDA-approved small-molecule protein kinase inhibitors.

For the top-ranked prediction, Multiple Endocrine Neoplasia, the model's own generated rationale is explicitly skeptical: MEN is primarily driven by *RET*, *MEN1*, and *CDKN1B* mutations, none of which have an established link to FGFR signaling. The rationale states this high score likely reflects a lack of underlying mechanistic support rather than a genuine biological signal.

By contrast, a lower-ranked prediction in the same pack — HER2-positive breast carcinoma (rank 3, L4, "Research Question") — has a more coherent mechanistic story (FGFR1 amplification as a known trastuzumab-resistance pathway) and at least one supporting literature reference, even though it still lacks disease-specific data or trials. This suggests the top-ranked prediction may not be the most biologically credible candidate in this pack, and rank 3 may merit separate follow-up.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Pemigatinib currently holds no marketing authorizations in Finland (market status: Not Marketed; 0 registered authorizations).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1/2/3 selective kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are marked as a Blocking data gap in this evidence pack — this item must be resolved before any S1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Multiple Endocrine Neoplasia) has no clinical trials, no literature, and the model-generated rationale itself questions the mechanistic basis for the score. Combined with the drug's unmarketed status in Finland and a blocking gap in TFDA safety data, there is currently no basis to advance this specific indication.

**To proceed, the following is needed:**
- TFDA/EMA package insert extraction (warnings, contraindications, DDI) — currently a blocking gap
- Confirmed original indication and mechanism-of-action data for pemigatinib
- Any preclinical or mechanistic evidence directly linking FGFR1/2/3 signaling to MEN pathophysiology
- Consider redirecting research attention to the HER2-positive breast carcinoma signal (rank 3, L4), which has a more plausible mechanistic rationale and at least preliminary literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

