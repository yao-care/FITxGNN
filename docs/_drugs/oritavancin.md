---
layout: default
title: Oritavancin
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 3
---

# Oritavancin
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

# Oritavancin: Predicted New Indication — Bacteroidaceae Infectious Disease

## One-Sentence Summary

> Oritavancin's original approved indication is not documented in the current data pack (data gap).
> The TxGNN model's top prediction for this drug is **Bacteroidaceae infectious disease**, with a score of **99.48%**,
> but **0 clinical trials** and **0 publications** currently support this direction, and the drug's own mechanism of action directly contradicts the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data (data gap) |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed original-indication and formal MOA data are not available for oritavancin in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes attached to the prediction itself, oritavancin is a lipoglycopeptide antibiotic that inhibits bacterial peptidoglycan transglycosylation/transpeptidation and disrupts cell membrane integrity — a mechanism active only against Gram-positive organisms (including MRSA and VRE).

This mechanism does not support the top prediction. *Bacteroidaceae* are Gram-negative anaerobes whose outer membrane blocks glycopeptide penetration to the target site — glycopeptides are pharmacologically known to be ineffective against Gram-negative bacteria. The prediction therefore conflicts directly with established pharmacology despite its high TxGNN score.

The same pattern holds for the two next-ranked candidates in this evidence pack: ophthalmic herpes zoster (rank 2, score 99.03%) is caused by a virus (VZV), for which a cell-wall-targeting antibacterial has no plausible mechanism; and *Mycoplasma pneumoniae* pneumonia (rank 3, score 99.01%) involves a pathogen that entirely lacks a cell wall, the sole known target of oritavancin. All three top predictions for this drug are flagged internally as mechanistically unsupported, which is an important caveat when interpreting the raw TxGNN scores.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Oritavancin is not currently marketed in Finland; no authorization records are available (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.48%), the repurposing rationale attached to this candidate explicitly identifies a mechanistic contradiction — glycopeptide antibiotics are not active against the Gram-negative anaerobic target — and there is zero supporting real-world evidence (no clinical trials, no literature). The two next-ranked candidates for this drug show the same pattern (viral etiology and cell-wall-deficient pathogen, respectively, both incompatible with the drug's cell-wall-targeting mechanism), and safety data (warnings, contraindications, DDI) is a Blocking data gap that prevents any S1 safety screening.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently Blocking gap (DG001)
- Confirmed original indication and formal MOA documentation — currently High-severity gap (DG002)
- Independent pharmacological review reconciling the TxGNN score with the mechanistic contradiction before any further evaluation
- DDI/safety database query (current status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

