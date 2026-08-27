---
layout: default
title: Tagraxofusp
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Tagraxofusp
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

Using the evidence pack as given — note the pack's own `repurposing_rationale` for the top-ranked prediction (rank 1, esotropia) explicitly flags it as a likely embedding false-positive, and this is reflected faithfully below rather than dressed up.

# Tagraxofusp: From Blastic Plasmacytoid Dendritic Cell Neoplasm to Esotropia

## One-Sentence Summary

Tagraxofusp is a CD123 (IL-3Rα)-targeted diphtheria toxin fusion protein, referenced in this evidence pack's own trial data as approved for blastic plasmacytoid dendritic cell neoplasm (BPDCN). The TxGNN model's top-ranked prediction is **Esotropia**, but this association is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale describes it as a probable false positive arising from sparse-data embedding rather than a biologically grounded signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured regulatory data (Finland). Referenced only via trial background text as BPDCN. |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for tagraxofusp in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in the associated clinical trial records, tagraxofusp is a protein-drug conjugate combining a truncated diphtheria toxin with IL-3, redirected to kill CD123-expressing cells — the mechanism underlying its approval for BPDCN and its investigational use in CD123-positive AML/MDS.

Esotropia is a neuromuscular/structural disorder of ocular alignment involving the extraocular muscles and their innervation; it has no known association with CD123 expression or cytotoxic protein-toxin biology. There is no mechanistic pathway connecting tagraxofusp's cytotoxic, hematologic-malignancy-targeted action to this ophthalmologic condition.

Consistent with this, the evidence pack's own rationale for this candidate states there is "no mechanistic relationship" and attributes the score to a TxGNN embedding artifact under sparse data ("屬TxGNN在稀疏資料下的嵌入假陽性"). No clinical trials, registry entries, or publications were found linking the two, which is itself evidence against — not for — the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Tagraxofusp is not currently marketed in Finland — 0 authorizations on file, no license records available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CD123-directed cytotoxic fusion protein: truncated diphtheria toxin + IL-3) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is numerically high, but zero clinical trials and zero publications support a tagraxofusp–esotropia link, and the model's own mechanistic rationale identifies this as a likely false positive with no biological plausibility. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking gap, DG001) — required before any S1 safety review regardless of indication
- Confirmed mechanism-of-action data (DG002)
- Independent biological or pharmacological rationale for a CD123-targeted cytotoxic agent in esotropia, if this candidate is to be pursued further
- Consider redirecting evaluation effort to rank 2 ("pre-malignant neoplasm"), which carries stronger supporting evidence (L3, 5 clinical trials, decision stage S1) within the same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

