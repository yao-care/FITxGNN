---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol's original indication cannot be confirmed from this evidence pack — no Finland market licenses and no mechanism-of-action record are currently available. The TxGNN model predicts a possible link to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this is currently supported by **0 clinical trials** and only **1 general review article** that does not specifically evaluate mannitol for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text found in the evidence pack (0 Finland licenses on record) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for mannitol is not currently available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, mannitol is an osmotic diuretic that draws free water into the vascular space and promotes renal excretion of water; this general property is the basis for the model's mechanistic link to NSIAD.

NSIAD is a rare congenital disorder caused by gain-of-function mutation of the V2 vasopressin receptor, producing hyponatremia that mimics SIADH. The repurposing rationale notes that mannitol's osmotic diuresis could theoretically raise serum sodium acutely, but this is **not** the standard-of-care treatment for NSIAD (fluid restriction or urea are standard). The single supporting publication (PMID 26706473) is a general review on pitfalls in evaluating hyponatremia — it does not report any actual mannitol efficacy data for NSIAD specifically.

Given this, the mechanistic plausibility is theoretical rather than evidence-based. It is also worth noting that all 10 TxGNN-predicted indications for mannitol in this evidence pack were rated "Hold," and several carry specific caveats worth flagging: the malignant-hyperthermia-related predictions (ranks 3–4, 7, 8, 10) may reflect confounding with dantrolene (mannitol is a common excipient/co-administered diluent for IV dantrolene, not an active MH therapy), and the nephrogenic diabetes insipidus prediction (rank 9) may reflect the *opposite* causal direction — mannitol is a recognized cause of nephrogenic diabetes insipidus symptoms rather than a treatment for it. This overall pattern suggests the model score alone is not yet a reliable signal for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | General review of common diagnostic pitfalls in hyponatremia evaluation; does not evaluate mannitol therapy specifically for NSIAD |

---

## Finland Market Information

No marketing authorizations are on record for mannitol in Finland (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — the TFDA/Fimea label data gap is flagged as Blocking, and the DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (NSIAD) rests on a theoretical mechanistic argument, not standard-of-care use, and is backed by a single non-specific review article with no clinical trials. Combined with the blocking gap in label/safety data and the drug's unconfirmed original-indication and non-marketed status in Finland, there is not yet sufficient evidence to advance past initial screening (S0).

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap
- Confirmed original indication / licensing history for mannitol in Finland
- Dedicated clinical or mechanistic studies directly evaluating mannitol in NSIAD (not general hyponatremia reviews)
- Drug interaction (DDI) dataset — current query returned no results
- Manual review to rule out confounding for the malignant-hyperthermia-related and nephrogenic-diabetes-insipidus predictions noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

