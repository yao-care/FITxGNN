---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Aflibercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Aflibercept: From Retinal Vascular Diseases to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF-A/VEGF-B/PlGF trap protein established for retinal vascular diseases (wet AMD, DME, RVO), though structured original-indication and Finnish licensing data are not currently on file. The TxGNN model assigns a high prediction score (**99.38%**) for **Esotropia**, but this is supported by **zero clinical trials** and **zero publications**, and the evidence pack itself flags the prediction as a likely knowledge-graph artifact rather than a genuine mechanistic relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the Finnish license registry (drug not marketed); known clinical use is retinal vascular disease (wet AMD, DME, RVO) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug-level mechanism-of-action field is a recorded data gap in this evidence pack. However, the prediction rationale attached to this specific indication does describe Aflibercept's known pharmacology: it is a VEGF-A/VEGF-B/PlGF trap protein that blocks pathological angiogenesis, the mechanism underlying its established clinical use in wet age-related macular degeneration (AMD), diabetic macular edema (DME), and retinal vein occlusion (RVO).

Esotropia, by contrast, is a disorder of ocular motility caused by extraocular muscle imbalance or a neurogenic cause (e.g., abducens/cranial nerve VI palsy). It is a mechanical/neurological condition, not a vascular or angiogenic one, and the evidence pack finds **no established pathophysiological link** between VEGF signaling and esotropia.

The high TxGNN score most plausibly reflects an artifact of knowledge-graph structure: Aflibercept (an ophthalmic drug) and Esotropia (an ophthalmic disease) sit close together simply because both cluster under "ophthalmology" nodes, producing embedding proximity that does not represent a real mechanistic relationship. The evidence pack's own rationale explicitly labels this as a **potential false positive**, and no supporting clinical or literature evidence has been found to counter that assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack's own mechanistic analysis finds no plausible biological link between Aflibercept's VEGF-trap activity and esotropia, and this prediction is supported by zero clinical trials and zero publications (Evidence Level L5, model prediction only). Combined with the drug not being marketed in Finland (0 authorizations), there is currently no basis to advance this candidate beyond initial screening.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: TFDA/Fimea package insert (warnings, contraindications) — required before any S1 safety pre-assessment can begin
- Resolve high-severity data gap DG002: confirmed mechanism-of-action data from DrugBank, to properly assess (or rule out) mechanistic relevance
- Independent biological plausibility review by an ophthalmology/neuro-ophthalmology specialist, given the rationale's own false-positive flag
- Continued surveillance of ClinicalTrials.gov, ICTRP, and PubMed for any future Aflibercept–esotropia evidence, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

