---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Tumor Lysis Syndrome–Associated Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase established for treating hyperuricemia associated with tumor lysis syndrome in cancer patients. The TxGNN model's top-ranked prediction is **Renal Hypouricemia**, but this prediction is mechanistically implausible — rasburicase *lowers* uric acid, while renal hypouricemia is a condition of *abnormally low* uric acid — and it is supported by **zero clinical trials and zero publications**. A stronger mechanistic candidate exists further down the ranked list (HPRT partial deficiency), also without any supporting studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tumor lysis syndrome–associated hyperuricemia (per pharmacological context in the evidence pack; not sourced from a formal license, as none exists) |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is flagged as a data gap (DG002) in this evidence pack. However, the pack's own rationale text confirms rasburicase's known pharmacology: it is a recombinant urate oxidase that oxidizes uric acid into allantoin, used to *reduce* uric acid levels in oncology patients at risk of tumor lysis syndrome.

**The top-ranked prediction, Renal Hypouricemia, should be treated with significant caution.** Renal hypouricemia is a disorder of *abnormally low* uric acid, typically caused by defective renal tubular urate transporters. Administering a uric acid–lowering agent to a patient who already has too little uric acid runs directionally opposite to the disease and would be expected to worsen rather than improve the condition. The evidence pack itself explicitly characterizes this as a likely high-score false positive of the TxGNN model, not a biologically coherent hypothesis.

A more mechanistically defensible candidate appears at rank 2: **HPRT partial deficiency** (e.g., Kelley-Seegmiller syndrome), where a blocked purine salvage pathway causes uric acid overproduction and urate nephropathy. Here, rasburicase's uric-acid-oxidizing action has a direct, logical connection to the underlying metabolic abnormality. However, this candidate carries no clinical trial or literature support either, and was not selected as the model's top hit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Rasburicase is not currently marketed in Taiwan (0 authorizations on record), so no product/authorization data is available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA package insert retrieval is a blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (renal hypouricemia) is mechanistically contradictory to rasburicase's known pharmacology and is best treated as a probable model artifact rather than a genuine repurposing signal. The mechanistically more plausible candidate (HPRT partial deficiency) has no clinical or literature evidence at all. With evidence level L5 across all ten predictions and no real-world use, marketing, or safety documentation, none of these candidates are ready for further evaluation stages.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed original indication and formal MOA documentation (DG002)
- Preclinical or case-level evidence specifically testing rasburicase in HPRT partial deficiency–related urate nephropathy, if this candidate is to be pursued instead of the top-ranked (implausible) hit
- Re-scoring or manual override review of the renal hypouricemia prediction, given the directional mechanistic conflict identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

