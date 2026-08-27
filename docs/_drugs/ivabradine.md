---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 6
---

# Ivabradine
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

# Ivabradine: From Heart Rate Reduction (Cardiovascular Disease) to Hypertrichosis

## One-Sentence Summary

Ivabradine is a selective inhibitor of the sinoatrial node I_f ("funny") current, used pharmacologically to lower heart rate in cardiovascular disease; it is not currently marketed in Finland and no local product label is on file.
The TxGNN model predicts it may be effective for **hypertrichosis (disease)**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure graph-based prediction with no known mechanistic link.
Given the absence of any trial, literature, or confirmed mechanism-of-action evidence, and a blocking gap in safety/label data, this candidate is not ready to advance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (Finland: unmarketed, no product license text); known pharmacological class use is heart-rate reduction in cardiovascular disease |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for ivabradine is not available in this evidence pack (DrugBank MOA field returned a data gap). Elsewhere in the collected evidence, ivabradine's known pharmacology is noted as selective inhibition of the sinoatrial node I_f ("funny") current, which reduces heart rate — the basis for its cardiovascular use.

There is no established or plausible biological pathway connecting I_f-channel inhibition to hair follicle growth or hypertrichosis. The evidence pack's own assessment for this candidate states explicitly that no clinical trials, no literature, and no MOA data exist to support the link, and that the prediction is a pure TxGNN graph output rather than a mechanism-grounded hypothesis.

The four other top-ranked predictions for this drug (Ambras-type hypertrichosis, an odontal/periodontal malformation syndrome, a Dandy-Walker malformation syndrome, and an isolated hair-shaft abnormality) are similarly unsupported — none show a credible mechanistic tie to sinoatrial rate control, and only one (the odontal/periodontal syndrome) returned any literature at all, and that literature is generic periodontal-disease background rather than ivabradine-specific research.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Ivabradine has no marketing authorization on file (`market_status`: Not Marketed; `total_licenses`: 0). No product license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in the evidence pack; the TFDA/label warning data gap is flagged as **Blocking** for safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (hypertrichosis) has no supporting clinical trials, no literature, and no mechanistic rationale — the evidence pack itself characterizes it as model noise. This is compounded by a blocking data gap on TFDA/label safety information, which prevents even a preliminary safety screen (S1).

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently blocking)
- Confirmed mechanism-of-action data from DrugBank
- Preclinical or mechanistic studies linking I_f-channel inhibition (or any other ivabradine target) to hair follicle biology
- Any pilot clinical or case-level evidence before this candidate can move past L5/S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

