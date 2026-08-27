---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), with its established clinical use limited to HIV-1 prevention and treatment. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic review found no known biological pathway connecting HIV integrase inhibition to rheumatoid inflammation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the Finland registry (drug is unmarketed); known pharmacology is HIV-1 infection via integrase inhibition |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured drug record (marked as a data gap). What is known from the evidence pack's own mechanistic review is that cabotegravir is an INSTI — its only established pharmacological activity is inhibition of the HIV-1 integrase enzyme, which blocks viral DNA integration into the host genome.

There is no structural or pathway overlap between this mechanism and the immune-inflammatory pathways implicated in rheumatoid arthritis (e.g., TNF-α, IL-6, JAK-STAT signaling). The evidence pack's repurposing rationale explicitly states this: the high TxGNN score reflects **knowledge-graph topological similarity only**, not a biologically grounded hypothesis.

The same pattern holds across the other four TxGNN-ranked candidates for this drug (sclerosing cholangitis, bronchitis, a rare developmental syndrome, and diabetic retinopathy) — each carries a similarly high score but no corroborating mechanistic, trial, or literature evidence. This suggests the model's embedding space for cabotegravir may be sparse or noisy, and none of the five predictions currently rise above a pure model-score signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Cabotegravir is not currently marketed in Finland — no marketing authorizations are on file (0 licenses registered).

## Safety Considerations

Please refer to the package insert for safety information. Note: retrieval of the Finnish/EU package insert warnings and contraindications for cabotegravir is flagged as a **blocking data gap** in this evidence pack, meaning this candidate cannot yet proceed to a formal S1 safety pre-assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on TxGNN's model score (L5, S0) with no clinical trials, no literature, and an explicit lack of mechanistic plausibility linking cabotegravir's INSTI activity to rheumatoid arthritis. Combined with the unmarketed status in Finland and a blocking gap in safety/label data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (currently blocking — required before any S1 safety screening)
- Confirmed mechanism-of-action documentation from DrugBank or an equivalent primary source
- Preclinical or mechanistic studies establishing biological plausibility for an immune-inflammatory indication
- Ongoing monitoring for any emerging trials or literature on cabotegravir outside HIV, given the current absence of both
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

