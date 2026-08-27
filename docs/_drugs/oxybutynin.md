---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynin: From Unspecified Original Indication to Restless Legs Syndrome

## One-Sentence Summary

> Oxybutynin (DrugBank DB01062) is an antimuscarinic/antispasmodic agent; its original approved indication is not documented in the current evidence pack.
> The TxGNN model predicts it may be effective for **Restless Legs Syndrome**,
> but **no clinical trials** and **no literature** currently support this direction — it is a **pure algorithmic prediction**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.74% (model rank 3291) |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack, and no original indication is on record, so the drug's established pharmacology cannot be cross-checked here. From general DrugBank classification, oxybutynin is known as a musculotropic antispasmodic with moderate antimuscarinic (M3-predominant) activity.

According to the model's own mechanistic assessment for this prediction, restless legs syndrome is primarily driven by dopaminergic system dysfunction and iron metabolism disturbances — pathways with **no known relationship** to oxybutynin's anticholinergic/smooth-muscle-relaxant mechanism. No plausible mechanistic hypothesis links the two, and there are zero clinical trials or publications connecting oxybutynin to RLS.

In short, this prediction rests entirely on the TxGNN model's statistical association score, without mechanistic, clinical, or literature support at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Oxybutynin is not currently marketed in Finland under this evidence pack (0 authorizations on record).

---

## Additional Predicted Indications Evaluated

This evidence pack ("multi" candidate) evaluated two further TxGNN predictions beyond restless legs syndrome, both also at Hold status:

| Rank | Disease | TxGNN Score | Evidence Level | Notes |
|------|---------|-------------|-----------------|-------|
| 2 | Gastroduodenitis | 99.62% | L5 | No clinical trials or literature; rationale based only on general antispasmodic effect on GI smooth muscle |
| 3 | Peptic Ulcer Disease | 99.31% | L4 | 3 older publications (1964–1990) found; one ([PMID 2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/)) describes oxybutynin-**inducing** reflux esophagitis by lowering lower esophageal sphincter tone — a signal working *against* this indication rather than supporting it. Modern PUD pathology (H. pylori, NSAIDs) is not addressed by an antimuscarinic mechanism |

None of the three candidates reach beyond Hold-level evidence.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (restless legs syndrome) has no mechanistic plausibility, no clinical trials, and no literature support (L5/S0). The next two candidates are similarly unsupported or carry a contrary safety signal (reflux esophagitis risk noted for the PUD pathway). The drug is also not currently marketed in Finland.

**To proceed, the following is needed:**
- Fimea/TFDA package insert (warnings, contraindications) — currently blocking safety review
- Verified mechanism of action (MOA) data from DrugBank
- Confirmed original approved indication(s) for the drug
- Any prospective mechanistic or preclinical rationale connecting oxybutynin to restless legs syndrome before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

