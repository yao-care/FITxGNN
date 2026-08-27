---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tildrakizumab: From Immune-Mediated Inflammatory Disease (Original Indication Not on File) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab (DrugBank DB14004) is an anti-IL-23p19 monoclonal antibody; its originally approved indication is not present in the current evidence pack. The TxGNN model predicts a possible effect on **Severe Nonproliferative Diabetic Retinopathy**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (original_indications empty, no marketed license on file) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for tildrakizumab (`original_moa` is flagged as a data gap). Based on the mechanistic notes embedded in the prediction rationale, tildrakizumab is an anti-IL-23p19 monoclonal antibody that blocks the Th17 signaling axis — the same target class used in IL-23/Th17-driven immune-mediated inflammatory conditions.

The proposed link to diabetic retinopathy rests on an indirect inflammatory hypothesis: elevated vitreous IL-17A has been observationally associated with diabetic retinopathy activity, and the reasoning is that upstream IL-23 blockade could theoretically dampen this downstream inflammatory and neovascular response. For the top-ranked candidate, "severe" nonproliferative diabetic retinopathy is treated as a late-stage subtype of the broader disease, but the evidence pack explicitly notes there is no subtype-specific mechanistic data — the link is inferred from the general diabetic-retinopathy hypothesis, not validated independently.

Three related but lower-confidence signals appear in the same prediction set — diabetic retinopathy (general), diabetic cataract, and drug-induced osteoporosis — each also rated L5/Hold. The diabetic cataract link is explicitly flagged by the evidence pack as having no known mechanistic bridge to IL-23/IL-17 biology (its pathophysiology is polyol-pathway and glycation-driven), and the osteoporosis link relies only on the general IL-17/osteoclast literature rather than any tildrakizumab-specific data. None of these four predictions currently have any clinical trial or literature support — they are network-prediction outputs only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Tildrakizumab is not marketed in Finland (0 marketing authorizations on file). No licensed product/dosage-form/indication data is currently available for this candidate.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the evidence pack flags the absence of Fimea/label-level warnings and contraindications as a Blocking data gap — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a purely computational (L5) signal with zero supporting clinical trials or literature, no confirmed mechanistic bridge specific to the proposed indication, and the drug is not currently marketed in Finland. There is no basis yet to advance this candidate past initial screening.

**To proceed, the following is needed:**
- Official package insert / label warnings and contraindications (currently a Blocking data gap — required before any safety pre-screening)
- Structured mechanism-of-action confirmation from DrugBank or equivalent source (currently a High-severity data gap)
- Original approved indication and regulatory history for tildrakizumab
- Preclinical or translational data specifically linking IL-23/Th17 inhibition to diabetic retinopathy pathophysiology (subtype-specific, not inferred from general DR hypotheses)
- Any emerging clinical trial or case-report evidence in this indication space, to re-evaluate evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

