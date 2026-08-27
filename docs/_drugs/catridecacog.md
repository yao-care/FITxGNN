---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 3
---

# Catridecacog
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

# Catridecacog: From Unspecified Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

Catridecacog (DrugBank DB09310, recombinant coagulation Factor XIII A-subunit) has no original indication or mechanism-of-action data available in the current evidence pack. The TxGNN model predicts a possible link to **Primary Release Disorder of Platelets**, with a prediction score of **99.29%**, but currently **0 clinical trials** and **0 publications** support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Finland license data, `original_indications` empty) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for catridecacog in this evidence pack, and no original indication is documented either (DrugBank query returned no `original_moa`, and no Taiwan/Finland licenses exist to infer approved use from).

Based on the drug's identity as a recombinant Factor XIII A-subunit, and the mechanistic rationale supplied alongside the TxGNN prediction, the biological link to the predicted indication is weak rather than strong:

Primary release disorder of platelets is caused by a defect in platelet granule (dense granule/alpha granule) release, which impairs the secondary amplification of platelet activation signaling — a primary hemostasis defect. Factor XIII, by contrast, acts at the terminal step of the coagulation cascade, cross-linking fibrin monomers to stabilize an already-formed clot. It has no direct biochemical relationship to the platelet granule-release mechanism; at most it could exert an indirect effect through overall clot stabilization. **The mechanistic linkage between the drug and the predicted indication is explicitly assessed as low.**

This means the prediction should be read as a hypothesis-generating signal from the model rather than a mechanistically well-supported repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies solely on a TxGNN model score (L5 evidence level) with zero clinical trials and zero literature support. The supplied mechanistic rationale itself rates the biological linkage as low — Factor XIII's fibrin cross-linking role does not directly address the platelet granule-release defect underlying this indication.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking (DG001)
- Mechanism of action (MOA) data via DrugBank API — currently high-severity gap (DG002)
- Preclinical or case-level evidence specifically linking Factor XIII supplementation to platelet release disorders, pseudo-von Willebrand disease, or Glanzmann thrombasthenia (the other two candidates in this pack carry the same L5/Hold status and equally weak mechanistic links)
- Confirmation of original approved indication(s) for catridecacog, since none are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

