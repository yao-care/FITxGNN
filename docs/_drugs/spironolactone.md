---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone: From Hypertension/Oedema to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a mineralocorticoid receptor antagonist widely used for hypertension, oedema, heart failure and primary hyperaldosteronism, and is already used off-label for androgen-driven hair conditions such as female pattern hair loss and hirsutism. The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the disease itself is a genetic/structural hair-follicle disorder with no known link to the drug's mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, oedema, primary hyperaldosteronism (general clinical knowledge; not captured in this evidence pack — `original_indications` and Taiwan license data are both empty) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.26% (rank 7,390) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature found) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable in the evidence pack (marked as a data gap, DG002 — High severity). Based on general pharmacological knowledge, spironolactone is a mineralocorticoid receptor antagonist that also blocks the androgen receptor and inhibits steroidogenesis, which is why it is used off-label for androgenetic alopecia and hirsutism in women.

However, **hypotrichosis simplex of the scalp** is an autosomal dominant hair follicle developmental disorder, mainly associated with *APCDD1* mutations. It is a structural/developmental condition, not an androgen- or mineralocorticoid-driven process, and there is no established pathological link to spironolactone's mechanism.

The second predicted indication in this pack, **congenital hypotrichosis with milia** (score 99.04%, rank 9,158), shows the same pattern — another rare genetic hair/skin disorder (associated with genes such as *LIPH*) with no known androgen or mineralocorticoid pathway involvement. The fact that both top predictions fall into the same "hair loss/hypotrichosis" disease cluster suggests the TxGNN score is likely driven by embedding proximity between "drug ↔ hair loss" concepts generally, rather than by a specific, verified mechanistic connection to these particular genetic disorders. This is a plausible but unverified hypothesis, and should be treated as speculative rather than confirmed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on the TxGNN model score (L5, no supporting clinical trials or literature), and the target disease is a genetic/structural hair follicle disorder with no established mechanistic link to spironolactone's antimineralocorticoid/antiandrogen activity. The apparent similarity to a second, unrelated hypotrichosis prediction further suggests the score may reflect disease-cluster proximity in the model's embedding space rather than a real pharmacological signal.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Targeted literature/preclinical search on *APCDD1*-related hypotrichosis and any androgen/mineralocorticoid pathway involvement
- Dermatology/genetics expert review of biological plausibility before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

