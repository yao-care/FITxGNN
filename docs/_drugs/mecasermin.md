---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 5
---

# Mecasermin
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

# Mecasermin: From Growth Hormone Insensitivity to Monosomy X (Turner Syndrome)

## One-Sentence Summary

Mecasermin is a recombinant human IGF-1 analogue whose established mechanism is to bypass the growth hormone receptor and directly supply downstream IGF-1 in patients with GH insensitivity (e.g. Laron syndrome). The TxGNN model predicts a possible new application in **monosomy X (Turner syndrome)**, but this candidate currently has **no supporting clinical trials or literature**, and the evidence pack itself flags the mechanistic link as likely a co-occurrence artifact rather than a direct pathological connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Fimea-approved indication text on file (drug not marketed in Finland); known use per DrugBank-derived rationale is growth failure due to GH insensitivity |
| Predicted New Indication | Monosomy X (Turner syndrome) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic rationale attached to a related prediction in this same batch, mecasermin's known pharmacology is to act as a recombinant IGF-1 that bypasses the GH receptor, directly supplying downstream IGF-1 signalling — the basis for its use in GH-insensitivity-related growth failure.

For monosomy X (Turner syndrome), the proposed link is that affected patients commonly present with growth delay and sometimes respond poorly to GH therapy, so IGF-1 supplementation is theoretically plausible as a downstream growth-stimulating adjunct. However, the growth delay in Turner syndrome is primarily attributed to SHOX gene haploinsufficiency, not classical IGF-1 deficiency — making the mechanistic overlap indirect and non-specific.

Notably, the evidence pack's own rationale cautions that the high TxGNN score may reflect a "growth-related disease" co-occurrence pattern in the knowledge graph rather than a direct pathological mechanism. This should be treated as a hypothesis-generating signal only, not a validated mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

No authorized products on file — mecasermin is not currently marketed in Finland (0 licenses recorded).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert warnings and contraindications are marked as a Blocking data gap (DG001) in this evidence pack and could not be extracted for this report.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has L5 evidence (model prediction only), zero clinical trials or literature support, and the evidence pack itself notes the mechanistic link is likely an indirect/spurious knowledge-graph co-occurrence rather than a validated pathological connection. Combined with the absence of safety data, there is no basis to advance beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Targeted literature search for IGF-1 use in Turner syndrome / SHOX-related growth delay to test the mechanistic hypothesis
- Confirmation of Finland regulatory/market status before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

