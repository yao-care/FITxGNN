---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 1
---

# Rivastigmine
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

# Rivastigmine: From Alzheimer's/Parkinson's Disease Dementia to Glaucoma

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor conventionally used to treat Alzheimer's and Parkinson's disease dementia (this evidence pack does not include a confirmed original-indication record — see note below). The TxGNN model predicts it may be effective for **Glaucoma**, currently supported by **0 clinical trials** and **3 publications**, including one preclinical animal study.

> Note: `taiwan_regulatory.licenses` and `drug.original_indications` are empty in this evidence pack, so the original indication above reflects the drug's well-established clinical use rather than a Fimea-sourced label. Rivastigmine (DB00989) is not currently marketed in Finland per this data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Fimea licensing data (0 licenses on file); conventionally used for Alzheimer's/Parkinson's disease dementia |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, rivastigmine is a selective acetylcholinesterase (AChE) inhibitor, a class of agents typically used to raise acetylcholine levels in the central nervous system for Alzheimer's and Parkinson's disease dementia.

The mechanistic link to glaucoma comes from the cholinergic system's role in intraocular pressure (IOP) regulation: acetylcholine acts on M3 muscarinic receptors in the trabecular meshwork to increase aqueous outflow and lower IOP. Non-selective AChE inhibitors have long been used clinically as IOP-lowering miotics, and the literature in this pack notes that "mild inhibition of AChE has been shown to have therapeutic relevance in Alzheimer's disease, myasthenia gravis, and glaucoma."

A direct preclinical study (PMID 10673128) found that topical rivastigmine lowered IOP in rabbits, supporting biological plausibility for repurposing beyond its established CNS use. However, this remains animal/mechanistic evidence — no human trials in glaucoma patients have been identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical (animal study) | Journal of Ocular Pharmacology and Therapeutics | Topical rivastigmine, a selective AChE inhibitor, lowered intraocular pressure in normotensive rabbits over 8 hours |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review | Frontiers in Molecular Biosciences | Reviews cholinergic (muscarinic) agents for IOP reduction via the trabecular meshwork; notes systemic side effects limit current M3 agonists |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review | Expert Opinion on Therapeutic Patents | Surveys AChE inhibitors/reactivators; notes mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis, and glaucoma |

---

## Finland Market Information

Rivastigmine is currently not marketed in Finland — no Fimea authorizations are on file in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to one preclinical rabbit study and two mechanistic reviews, with no clinical trials or human data in glaucoma; the drug is also not currently marketed in Finland, and safety/warning data are unavailable (a blocking gap for S1 safety screening).

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action record from DrugBank (DG002)
- Confirmed original indication/licensing record for rivastigmine
- Human proof-of-concept or Phase 1/2 trial data in glaucoma or ocular hypertension
- DDI data before any clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

