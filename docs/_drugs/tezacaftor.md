---
layout: default
title: Tezacaftor
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 3
---

# Tezacaftor
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

# Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease

## One-Sentence Summary

Tezacaftor is a CFTR (cystic fibrosis transmembrane conductance regulator) corrector, a class of drug used to treat cystic fibrosis by improving CFTR protein folding and membrane trafficking. The TxGNN model predicts it may be effective for **HIV infectious disease**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags no known mechanistic link between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (inferred from drug class; no TFDA-approved indication text available — Tezacaftor is not marketed in Taiwan) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the evidence pack's own rationale notes, Tezacaftor is known as a CFTR corrector used in cystic fibrosis treatment, where it helps misfolded CFTR protein traffic correctly to the cell membrane.

There is no known mechanistic overlap between CFTR modulation and HIV pathophysiology (viral replication, reverse transcription, or host immune pathways). The evidence pack explicitly states that this TxGNN score reflects knowledge-graph embedding similarity only, without biological plausibility, and is not corroborated by any clinical trial or literature evidence.

For context, TxGNN also flagged **leprosy** (score 99.14%) and **multiple endocrine neoplasia** (score 99.06%) for this drug — both rank 2 and 3 candidates carry the same caveat: no mechanistic rationale, no trials, and no literature. None of the three predictions in this evidence pack currently have independent scientific support beyond the model score itself.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Tezacaftor is not currently marketed in Taiwan (0 authorizations, market status: 未上市/Not Marketed). No TFDA-approved product or indication text is available.

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA package insert warnings/contraindications are marked as a **Blocking** data gap (DG001) — this drug currently cannot proceed to the S1 safety pre-assessment stage until this data is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction reflects pure knowledge-graph embedding similarity (L5, decision stage S0) with no mechanistic rationale, clinical trial, or literature support for HIV infectious disease — and the other two ranked candidates (leprosy, multiple endocrine neoplasia) fare no better. A blocking data gap on TFDA safety labeling also prevents any safety pre-assessment from starting.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required before any S1 safety evaluation can begin
- Official mechanism of action documentation from DrugBank or the manufacturer
- Independent preclinical or mechanistic evidence linking CFTR modulation to HIV pathophysiology, before committing further evaluation resources
- If no such evidence emerges, this candidate should not advance beyond model-prediction stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

