---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Thyroid Eye Disease to Monosomy X

## One-Sentence Summary

Teprotumumab is an anti-IGF-1R monoclonal antibody whose established use (referenced in the evidence pack's mechanistic rationale) is thyroid eye disease; formal original-indication data was not returned by this query. The TxGNN model's top prediction is **Monosomy X** (Turner syndrome karyotype) with a 99.79% score, but this candidate is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the prediction as a likely knowledge-graph false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in source data (`original_indications` empty; mechanistic rationale references thyroid eye disease as the known use) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this query (`original_moa: [Data Gap]`). Based on information embedded in the evidence pack's own rationale fields, teprotumumab is understood to act as an IGF-1R (insulin-like growth factor 1 receptor) antagonist, with established use in thyroid eye disease.

The top-ranked prediction, monosomy X, is the cytogenetic form of Turner syndrome. The evidence pack's own repurposing rationale flags a **direction conflict**: Turner syndrome is clinically managed with growth-hormone/IGF-1-axis therapies that *promote* growth in affected patients, whereas teprotumumab *blocks* IGF-1R signaling. Blocking the same axis that clinicians are trying to stimulate is mechanistically backwards, not complementary.

Compounding this, 6 of the 10 top-ranked predictions (ranks 1, 4, 6, 7, 8, 10) are all variants of the same Turner-syndrome/sex-chromosome-anomaly disease cluster, and 3 more (ranks 2, 3, 9) are all variants of a single venous/vascular disease cluster (esophageal varices, varicose disease). This pattern is consistent with TxGNN embedding proximity within disease-similarity clusters rather than 10 independent pharmacological hypotheses. With zero clinical trials and zero literature across all 10 candidates, none currently clears even a preliminary plausibility bar.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Teprotumumab currently holds no marketing authorization in Finland (0 licenses on file); no dosage forms or approved-indication text are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package-insert warnings/contraindications for this drug are flagged in the evidence pack as a Blocking data gap — DG001 — pending PDF retrieval and parsing from the TFDA site.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (monosomy X) and all 9 runner-up candidates sit at Evidence Level L5 with zero clinical trials and zero literature support. The evidence pack's own mechanistic rationale identifies a direction conflict for the Turner-syndrome cluster (IGF-1R blockade vs. the growth-promoting therapy this population needs) and attributes the remaining candidates to graph-clustering artifacts rather than independent biological hypotheses.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed original indication and MOA from DrugBank (currently Data Gap, DG002)
- A mechanistically coherent hypothesis for any candidate indication, independently reviewed before further evidence-gathering is commissioned
- Preclinical or case-level evidence for at least one candidate before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

