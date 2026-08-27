---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Silodosin is a highly selective alpha-1A adrenergic receptor antagonist originally used to relieve lower urinary tract symptoms associated with benign prostatic hyperplasia (BPH). The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** with a 99.99% score, but this and all five other top-ranked predictions are supported by **zero clinical trials and no relevant literature** — the evidence pack itself flags them as likely embedding-space artifacts with no plausible biological mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lower urinary tract symptoms associated with benign prostatic hyperplasia (BPH) — not present in this evidence pack; TFDA package insert data is flagged as a blocking gap (DG001) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita (congenital generalized hypertrichosis) |
| TxGNN Prediction Score | 99.99% (rank 153 among all disease candidates) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this evidence pack (flagged as data gap DG002), but based on publicly available drug reference data, silodosin is a highly α1A-selective adrenergic receptor antagonist that relaxes smooth muscle in the prostate and urethra, relieving BPH-related voiding symptoms. Its selectivity for α1A over α1B receptors is what limits cardiovascular side effects relative to older, non-selective alpha blockers.

There is no known or biologically plausible mechanistic pathway connecting α1A-adrenergic antagonism to Ambras syndrome, which is a congenital disorder linked to chromosomal rearrangements near 8q affecting *TRPS1* gene regulation and hair follicle development — an entirely distinct biological system from smooth-muscle adrenergic signaling.

The evidence pack's own repurposing rationale is explicit on this point: the TxGNN score of 0.9999 is assessed as a likely **spurious correlation within the model's knowledge-graph embedding space**, with no supporting biological hypothesis. The same pattern repeats across all six top-ranked predictions in this pack (hypertrichosis, a periodontal malformation syndrome, Dandy-Walker malformation, a hair-shaft structural disorder, and familial trichomegaly) — none has a credible mechanistic link to α1A antagonism, and the periodontal-disease literature that did surface (20 PubMed hits) was confirmed to be keyword-matching noise unrelated to silodosin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Silodosin is not currently marketed in Finland (0 authorizations on record), so no product license information is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trials, no relevant literature, and no biologically plausible mechanistic link to silodosin's known α1A-adrenergic antagonism — the evidence pack itself characterizes the TxGNN score as a likely spurious embedding-space correlation. All five other top-ranked predictions in this pack show the identical pattern (L5 evidence, Hold recommendation), reinforcing that this candidate set is not ready for further evaluation.

**To proceed, the following is needed:**
- TFDA/official package insert with warnings, contraindications, and confirmed original indication text (blocking gap, DG001)
- Verified mechanism-of-action data from DrugBank or equivalent primary source (DG002)
- A biologically grounded hypothesis (e.g., from dermatology/endocrinology literature) before any further investment in the hypertrichosis-related predictions
- Re-screening once TxGNN model version or training data is updated, given the current rank (153) is far outside typical high-confidence repurposing candidates

Sources:
- [Silodosin: Uses, Interactions, Mechanism of Action | DrugBank](https://go.drugbank.com/drugs/DB06207)
- [Silodosin - Wikipedia](https://en.wikipedia.org/wiki/Silodosin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

