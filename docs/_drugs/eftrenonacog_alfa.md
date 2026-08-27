---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Eftrenonacog Alfa: From Hemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Eftrenonacog alfa is a recombinant, extended half-life Factor IX (FIX) replacement therapy used to treat Hemophilia B. The TxGNN model's top-ranked prediction suggests possible relevance to **Pseudo-von Willebrand Disease**, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale is itself assessed as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia B (congenital Factor IX deficiency) — per drug mechanism description; not confirmed by TFDA/regulatory license text |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data is not available from DrugBank for this candidate (flagged as a High-severity data gap). Based on descriptive information captured in this evidence pack, eftrenonacog alfa is a recombinant FIX product that replaces deficient endogenous Factor IX, restoring thrombin generation via the intrinsic coagulation pathway — its established use is Hemophilia B.

The predicted indication, Pseudo-von Willebrand Disease, is a platelet-membrane disorder caused by gain-of-function mutations in *GP1BA*, resulting in abnormally increased affinity of platelet glycoprotein Ib for von Willebrand factor. This is a platelet-adhesion defect, not a coagulation-factor deficiency. While both conditions fall under the broad category of "bleeding disorders," their pathophysiology is fundamentally different — platelet-vWF interaction versus thrombin-generation cascade — so replacing FIX has no established rationale for correcting a platelet-adhesion abnormality.

This evidence pack also surfaces two additional TxGNN-predicted candidates for this drug, both with similarly weak mechanistic plausibility and identical L5/Hold ratings: **primary release disorder of platelets** (platelet granule-release defect, score 99.42%) and **Glanzmann thrombasthenia** (GPIIb/IIIa integrin deficiency impairing platelet aggregation, score 99.28%). In all three cases, the predicted disease involves a platelet-function defect rather than a coagulation-factor deficiency, and none has any supporting rFIX-specific trial or literature evidence — these appear to be graph-similarity artifacts rather than mechanistically grounded repurposing candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by TxGNN model scoring (L5), with no clinical trials, no literature, and a mechanistically weak rationale (platelet-adhesion disorder vs. coagulation-factor replacement). The drug is also not currently marketed in Finland, and TFDA safety/warning data is a Blocking-severity gap that prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action and formal original-indication labeling from DrugBank
- Any preclinical or mechanistic studies linking FIX replacement to platelet-adhesion/aggregation/release disorders
- Real-world or case-level evidence (e.g., hemostatic use in platelet disorders), if it exists outside registered trials/PubMed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

