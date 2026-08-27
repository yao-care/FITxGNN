---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From Respiratory Bronchodilation to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is a long-acting β2-adrenergic receptor agonist (LABA) bronchodilator used in respiratory disease (COPD/asthma), most commonly as part of fixed-dose combinations with glycopyrronium and/or mometasone. The TxGNN model's top-ranked prediction for this candidate pack is **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this ranks among the pack's ten predictions with **zero clinical trials and zero publications** supporting it, and the accompanying mechanistic review explicitly finds no plausible biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on record (see note below); evidence pack confirms indacaterol acts as a LABA bronchodilator for respiratory disease |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty (drug not marketed in Finland), so no formal approved-indication text is available from that source.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on information within this evidence pack, indacaterol is a long-acting β2-adrenergic receptor agonist that activates β2 receptors on bronchial smooth muscle, raising intracellular cAMP and producing bronchodilation — the established mechanism underlying its core respiratory use (see the "bronchial disease" candidate below, which is strongly evidence-backed but represents an already-known use rather than a novel repurposing signal).

For the top-ranked candidate — Nephrogenic Syndrome of Inappropriate Antidiuresis — the evidence pack's own mechanistic review finds **no plausible link**: NSIAD results from activating mutations of the renal V2 vasopressin receptor, and its standard management (fluid restriction or vaptans/V2-receptor antagonists) operates through a pathway with no known interaction with β2-adrenergic signaling. The high TxGNN score therefore appears to reflect a graph-embedding similarity rather than a biologically grounded hypothesis, and no clinical trials, ICTRP records, or PubMed literature exist to corroborate it (query log entries #5–#7, all zero results).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Indacaterol is not currently marketed in Finland — 0 authorizations are on record (`taiwan_regulatory.market_status`: 未上市 / Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert warnings/contraindications are flagged as a **Blocking** data gap — DG001 — pending retrieval and parsing before any S1 safety review can proceed.)

## Other Predicted Indications in This Evidence Pack

This candidate pack (`TW-DB05039-multi`) contains 10 TxGNN predictions for indacaterol. For context, they are summarized below; only rank 7 currently has meaningful supporting evidence, and it reflects an already-established use (respiratory bronchodilation) rather than a new repurposing opportunity.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Nephrogenic syndrome of inappropriate antidiuresis | 99.54% | L5 | Hold |
| 2 | Headache disorder | 99.53% | L5 | Hold |
| 3 | Trigeminal autonomic cephalalgia | 99.33% | L5 | Hold |
| 4 | Paratenonitis | 99.26% | L5 | Hold |
| 5 | Calcific tendinitis | 99.25% | L5 | Hold |
| 6 | Hypertrichosis (disease) | 99.23% | L5 | Hold |
| 7 | Bronchial disease | 99.18% | L1 | Proceed with Guardrails (known indication, not novel) |
| 8 | Myositis | 99.12% | L5 | Hold |
| 9 | Anaphylaxis | 99.07% | L4 | Hold |
| 10 | Ambras type hypertrichosis universalis congenita | 99.06% | L5 | Hold |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for NSIAD is high (99.54%), it is unsupported by any clinical trial or literature evidence, and the mechanistic review within this evidence pack explicitly finds no biological rationale connecting β2-adrenergic bronchodilation to a V2-receptor-mediated water-balance disorder. This is an L5 candidate (model prediction only) with a Hold recommendation from the scoring stage itself.

**To proceed, the following is needed:**
- TFDA/Finnish package insert warnings and contraindications (Blocking gap DG001) before any safety evaluation is possible
- Confirmed mechanism of action data (High-priority gap DG002)
- Preclinical or mechanistic studies specifically testing β2-agonism in NSIAD or related water-balance disorders, since none currently exist
- If pursuing a repurposing candidate from this pack, consider prioritizing better-evidenced signals (e.g., rank 9, anaphylaxis, L4) over the current top-ranked but mechanistically unsupported prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

