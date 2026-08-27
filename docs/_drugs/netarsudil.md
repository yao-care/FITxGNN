---
layout: default
title: Netarsudil
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 2
---

# Netarsudil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the `data-report` skill's fidelity principle (no fabricating fields, no silently dropping caveats) since this is a data-driven report — I'll build it strictly from the evidence pack, using real values only.

A structural note before the report: `predicted_indications[0]` (rank 1, **primary hereditary glaucoma**) is the top TxGNN hit and drives the title/overview per your template rules, but its own direct evidence is thin (1 indirect trial, 0 literature). The much stronger dataset (36 trials, 20 papers, L1) sits under rank 2, **glaucoma** — netarsudil's already-established indication elsewhere. I used that context only in the mechanism section, as the rationale text itself frames rank 1 as an extrapolation from rank 2's evidence base; the trial/literature tables strictly follow rank 1's own evidence per the template rule.

---

# Netarsudil: From Glaucoma/Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Netarsudil is a Rho-kinase (ROCK) / norepinephrine transporter (NET) dual inhibitor with an established IOP-lowering mechanism used in glaucoma and ocular hypertension (marketed elsewhere as Rhopressa/Rocklatan). The TxGNN model predicts it may also be effective specifically for **Primary Hereditary Glaucoma**, but this narrower prediction is currently supported by only **1 indirectly related clinical trial** and **no dedicated publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle Glaucoma / Ocular Hypertension (established use per literature; not currently marketed in Finland under this dataset) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Netarsudil is a dual Rho-kinase (ROCK) and norepinephrine transporter (NET) inhibitor. It acts on the trabecular meshwork to reduce resistance to aqueous humour outflow and lowers episcleral venous pressure, thereby reducing intraocular pressure (IOP). This mechanism underlies its well-documented efficacy in open-angle glaucoma and ocular hypertension — an indication supported, per this evidence pack's rank-2 prediction, by 36 clinical trials (including multiple completed Phase 3 pivotal studies such as the ROCKET and MERCURY series) and 20 publications, at evidence level L1.

Primary hereditary glaucoma is a genetic subtype of glaucoma typically linked to structural or functional defects in the trabecular meshwork (e.g., mutations affecting outflow-pathway genes). Because netarsudil's IOP-lowering effect works directly on that same outflow pathway, it is mechanistically plausible that it could increase outflow regardless of the underlying hereditary defect — theoretically bypassing rather than correcting the genetic abnormality.

However, no trial in this evidence pack directly tests netarsudil's IOP efficacy in a genetically confirmed hereditary glaucoma population. The only related trial (NCT06969586) evaluates corneal endothelial protection in glaucoma patients with Fuchs endothelial corneal dystrophy — a different endpoint entirely — and is graded "C" (indirect relevance). The rank-1 prediction is therefore best understood as an extrapolation from strong general open-angle glaucoma evidence, not as direct proof in the hereditary subtype.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A | Enrolling by Invitation | 50 | Evaluates whether topical ROCK inhibitors protect corneal endothelial cells after cataract surgery in patients with glaucoma and Fuchs endothelial corneal dystrophy (FECD); compares topical ROCK inhibitor vs. placebo. Graded "C" relevance — endpoint is corneal endothelial cell loss, not IOP efficacy in hereditary glaucoma, and enrollment is invitation-only. |

## Literature Evidence

Currently no related literature available specific to primary hereditary glaucoma.

## Finland Market Information

Netarsudil is not currently marketed in Finland (market status: 未上市 / Not Marketed; 0 authorizations on record), so no product/authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data for netarsudil are not yet available in this evidence pack — TFDA/Fimea package insert retrieval is flagged as a blocking data gap, see below.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 TxGNN prediction (primary hereditary glaucoma) currently rests on a single indirectly relevant trial with no supporting literature (L4, decision stage S1) — insufficient to advance. Netarsudil's mechanism is well-validated for glaucoma broadly, but that stronger evidence base does not directly confirm efficacy in the hereditary subtype, and a blocking safety data gap (no TFDA/Fimea package insert) prevents even an initial safety screen.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently blocking safety evaluation (S1)
- Confirmed mechanism-of-action documentation from DrugBank (currently a data gap)
- A trial or study directly assessing IOP efficacy in genetically confirmed primary hereditary glaucoma, rather than extrapolation from general open-angle glaucoma data
- Drug-drug interaction (DDI) data, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

