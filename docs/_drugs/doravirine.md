---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used to treat HIV-1 infection. The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence level L5, model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI; derived from model rationale notes — official Taiwan label text not yet available) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured DrugBank field (blocking data gap). Based on the model's own rationale notes, doravirine is an NNRTI that binds an allosteric pocket unique to HIV-1 reverse transcriptase (RT), and its efficacy in HIV-1 infection is well established.

The predicted new indication, FIV, is caused by a different lentivirus whose RT sequence diverges substantially from HIV-1's, and the NNRTI binding pocket is not conserved across species — NNRTIs are typically highly species/virus-specific with no cross-reactivity to FIV RT. TxGNN's high score for this pairing most likely reflects a superficial "same enzyme class, same viral family" association in the knowledge graph rather than a validated cross-species mechanism; this is exactly what the model's own generated rationale flags as unsupported.

Two other candidates were generated for doravirine at similarly high scores: simian immunodeficiency virus (SIV) infection — whose only associated literature (PMID 31658118) actually discusses islatravir, a different drug with a different mechanism (nucleoside RT translocation inhibitor, not NNRTI) — and a rare genetic neurodevelopmental disorder with no plausible mechanistic link to reverse transcriptase inhibition at all. None of the three candidates have clinical trial, preclinical, or case-report support, and all three are scored L5 / Hold in the source data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Doravirine currently holds no marketing authorization in Taiwan (0 licenses on file; market status: Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All three TxGNN-predicted indications for doravirine sit at evidence level L5 (model prediction only), with no clinical trials and no directly relevant literature.
- The top prediction, FIV, has a flagged cross-species mechanistic gap (NNRTI binding pocket not conserved between HIV-1 and FIV RT); it is also a veterinary rather than human indication.
- A blocking data gap exists: the TFDA package insert (warnings/contraindications) is unavailable, which by itself prevents S1 safety pre-screening regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert / product label — blocking gap (DG001)
- Confirmed original MOA and approved indication from a structured DrugBank record (DG002)
- Preclinical evidence of doravirine activity against FIV or SIV reverse transcriptase, if this line is to be pursued further
- Resolution of the outstanding DDI query (currently `not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

