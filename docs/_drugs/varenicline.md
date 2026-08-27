---
layout: default
title: Varenicline
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a nicotinic acetylcholine receptor (nAChR) partial agonist originally developed and marketed for smoking cessation. The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is currently supported by **0 clinical trials** and only **1 unrelated case report**, so the prediction remains speculative.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking Cessation (established use; not present in current regulatory dataset — see Data Gap below) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, varenicline is a partial agonist at α4β2 nicotinic acetylcholine receptors and a full agonist at α7 nAChR, and its efficacy in smoking cessation is well established through decades of clinical use.

There is a theoretical overlap between nAChR signaling and the trigeminovascular pain pathway implicated in migraine, which is the basis for the TxGNN model's prediction. However, this remains a purely mechanistic hypothesis — no clinical trial or pharmacological study in this Evidence Pack directly tests varenicline for migraine.

Critically, the only literature retrieved for this indication (PMID 19585710) is a case report of **cardiac arrest associated with varenicline use**, an adverse-event record with no relevance to migraine efficacy. There is currently no clinical evidence — positive or negative — that varenicline treats migraine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case Report | Therapie | Case report of cardiac arrest associated with varenicline use; an adverse-event record, not efficacy evidence for migraine |

## Finland Market Information

Varenicline currently has no marketing authorizations recorded in the Finland dataset (market status: Not Marketed; 0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert warnings/contraindications and DDI data are flagged as outstanding — DDI query returned no results, and package insert parsing is a Blocking-severity data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence tied to the Migraine Disorder prediction is an unrelated adverse-event case report (cardiac arrest), not an efficacy signal. Combined with the absence of MOA data and unresolved safety data gaps, there is insufficient basis to advance this indication.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data from DrugBank — currently a High-severity data gap
- Preclinical or mechanistic studies linking nAChR signaling to the trigeminovascular pain pathway
- Any dedicated clinical trial or observational data on varenicline in migraine patients (none currently exist)
- Note: rank-9 candidate "headache disorder" returned 5 trials and 14 publications, but nearly all concern smoking cessation, not headache treatment — this dataset should not be mistaken for supporting evidence for migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

