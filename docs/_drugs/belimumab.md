---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 6
---

# Belimumab
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

# Belimumab: From an Undocumented Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

The evidence pack does not contain Belimumab's original approved indication or mechanism of action (both flagged as data gaps). The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but this direction is currently supported by only **1 clinical trial** (assessed as not actually relevant to the predicted indication) and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only — the one associated trial is a label mismatch, not true supporting evidence) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Belimumab is not available in this evidence pack, and no original indication is on file either — both are flagged as data gaps (DG001, DG002).

Based on the repurposing rationale that is available, the evidence pack itself concludes there is **no known mechanistic link** between Belimumab and primary release disorder of platelets: Belimumab is known to act on BAFF/BLyS signaling affecting B-cell survival and autoantibody production, a pathway unrelated to platelet granule release. The only associated clinical trial (NCT01610492) was reviewed and graded "C" — its actual subject was idiopathic membranous glomerulonephropathy, not a platelet disorder, and it was judged a database label mismatch rather than genuine supporting evidence.

Taken together, this prediction currently rests on the TxGNN model score alone, without a corroborating mechanistic hypothesis or relevant trial/literature evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Studied belimumab in anti-PLA2R-positive idiopathic membranous glomerulonephropathy — **not** platelet-related; reviewer graded this a label mismatch and not valid supporting evidence for the predicted indication |

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Belimumab currently holds no marketing authorization in Taiwan (0 licenses on file; market status: 未上市).

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA package insert warnings/contraindications data is flagged as a **Blocking** data gap (DG001) and must be obtained before any safety pre-assessment (S1) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — the prediction is supported only by the TxGNN model score, with no confirmed mechanistic link and no relevant clinical trial or literature evidence (the single associated trial is a documented label mismatch). The drug is also not currently marketed in Taiwan, and safety data is a blocking gap.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — resolve blocking gap DG001
- Confirmed mechanism of action data — resolve gap DG002
- Belimumab's original approved indication(s), for mechanistic comparison
- Genuine clinical trial or literature evidence specific to primary release disorder of platelets (or a re-screen of the other 5 lower-ranked candidates, all of which are similarly at Hold/L5 with no supporting studies)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

