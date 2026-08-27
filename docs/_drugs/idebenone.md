---
layout: default
title: Idebenone
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Idebenone
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

# Idebenone: From Mitochondrial Protection to Hepatic Porphyria

## One-Sentence Summary

Idebenone is a synthetic coenzyme Q10 analogue best known for its mitochondrial electron-transport and antioxidant activity; no confirmed original approved indication is documented in this dataset, and the drug is not currently marketed in Finland. The TxGNN model predicts it may be effective for **hepatic porphyria**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure graph-based inference with no direct experimental backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (0 Finland authorizations); Idebenone is generally known as a mitochondrial-support/antioxidant CoQ10 analogue |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate record. Based on general pharmacological knowledge, Idebenone is a short-chain benzoquinone that acts on the mitochondrial electron transport chain and functions as an antioxidant; it has no formally documented approved indication in the present dataset, and Idebenone is not currently marketed in Finland (0 authorizations).

The TxGNN-generated rationale for hepatic porphyria explicitly flags a weak mechanistic link: Idebenone's mitochondrial/antioxidant activity does not directly overlap with the heme biosynthesis pathway that is the core pathology of porphyria. The stated hypothesis is that oxidative stress could be a shared secondary contributor between the two conditions, but this is speculative rather than evidence-based.

Given the absence of any supporting clinical trials or literature, this prediction should be treated as a hypothesis-generation signal from the knowledge graph rather than a mechanistically grounded repurposing candidate at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A blocking data gap exists — TFDA/Fimea package insert warnings and contraindications have not yet been retrieved (DG001), so no safety-related decision can currently be supported by this evidence pack.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is at decision stage S0 with evidence level L5 — supported only by a knowledge-graph score, with zero clinical trials, zero literature, and a mechanistic rationale the model itself describes as weak. Idebenone is also not marketed in Finland, and core safety data (warnings/contraindications) is missing (blocking gap).

**To proceed, the following is needed:**
- Idebenone package insert / TFDA-equivalent safety data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action and original approved indication data (DG002)
- Preclinical or mechanistic studies directly linking mitochondrial/antioxidant pathways to heme biosynthesis or porphyria pathophysiology
- Any emerging clinical trial or case-report evidence in hepatic porphyria before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

