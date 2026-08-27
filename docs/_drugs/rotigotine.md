---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease/Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

Rotigotine is a non-ergot, broad-spectrum (D1–D5) dopamine agonist with highest affinity for D3 receptors, referenced in the literature as being used to treat Parkinson's disease and restless legs syndrome. The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, but currently **0 clinical trials** and only **3 tangentially related publications** (none specific to rotigotine-ADHD) support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured regulatory data (Taiwan/Finland licensing fields are empty); literature within this pack (PMID 37221270) references Parkinson's disease and restless legs syndrome as rotigotine's established uses |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.997% (rank 49) |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for rotigotine is currently a flagged data gap (DG002, High severity, pending DrugBank API query). Based on information available within this evidence pack, rotigotine is described in the literature as a "pan-agonist" acting across all five dopamine receptor subtypes (D1–D5), with preferential affinity for D3, and is used to treat Parkinson's disease and restless legs syndrome (PMID 37221270). No formal `original_indications` record was returned, and no Taiwan/Finland marketing authorizations exist to cross-check against an approved indication label — this drug is not currently marketed in Finland.

The predicted link to ADHD is mechanistically weak. ADHD's dopamine hypothesis centers on D4 receptor polymorphisms and reduced prefrontal cortical dopamine signaling; first-line stimulant therapy works by increasing synaptic dopamine availability rather than direct receptor agonism. Rotigotine, as a D3-preferential direct agonist, has limited pathway overlap with the D4/prefrontal circuitry implicated in ADHD, and direct full agonism could theoretically disrupt normal phasic dopamine signaling — a mechanism not typically leveraged in ADHD pharmacotherapy. None of the three supporting publications directly studies rotigotine in ADHD populations; they concern restless legs syndrome reviews and receptor-heteromerization pharmacology.

Given the absence of disease-specific clinical or literature evidence and a mechanistically speculative rationale, this candidate should be treated as hypothesis-generating only at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic Science/Receptor Pharmacology | Pharmacological research | D4 receptor–α2A adrenoceptor heteromerization affects pharmacology relevant to impulsive-control disorders including ADHD; does not study rotigotine directly in ADHD |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current pharmaceutical design | Review of pharmacological options for restless legs syndrome in children; not ADHD-focused |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | General review of restless-legs syndrome; not ADHD-focused |

---

## Finland Market Information

Currently no marketing authorizations in Finland (market status: Not Marketed; 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently flagged as data gaps — TFDA package insert retrieval, DG001, is a Blocking-severity gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or ADHD-specific literature support rotigotine repurposing for ADHD, and the proposed mechanistic link (D3-preferential agonism vs. ADHD's D4/prefrontal pathway) is speculative. Combined with a Blocking-severity safety data gap (no TFDA label available), this candidate does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/EU package insert retrieval to resolve DG001 (Blocking) before any safety review can begin
- DrugBank MOA confirmation to resolve DG002
- Targeted literature/trial search specifically combining "rotigotine" and "ADHD" (current hits are RLS/receptor-pharmacology reviews only)
- Note: within this same evidence pack, the rank-2 candidate (schizophrenia, L3/S1, "Research Question") has stronger supporting literature but carries a distinct safety concern — theoretical risk of psychotic symptom exacerbation given rotigotine's known association with psychosis in Parkinson's disease patients — and would need independent evaluation if pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

