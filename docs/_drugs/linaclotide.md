---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Linaclotide
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

# Linaclotide: From an Undocumented Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Linaclotide's original indication and mechanism of action are not documented in the current evidence pack.
The TxGNN model predicts a possible association with **Cauda Equina Syndrome**, with a **99.96%** prediction score,
but **no clinical trials** and **no literature** currently support this direction — the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for linaclotide in this evidence pack, and the original indication field is also empty. Without either data point, it is not possible to assess mechanistic plausibility between linaclotide's known pharmacology and cauda equina syndrome.

The TxGNN model assigns a high confidence score (99.96%, rank 696) to this association, but the model output is currently unsupported by any external evidence — no registered clinical trials, no ICTRP records, and no published literature were found for this drug-disease pair. The other two model-flagged candidates (obsolete neurogenic bladder, score 99.89%; insomnia, score 99.51%) show the same pattern: high model confidence with zero corroborating trials or publications.

Given this, the prediction should be treated as a hypothesis-generation signal only, pending retrieval of the drug's actual original indication, MOA, and any supporting mechanistic or clinical literature.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Linaclotide currently has no marketing authorization in Finland (0 licenses on record; market status: 未上市).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5) with no clinical trial or literature corroboration, and key drug-level data — original indication, MOA, and TFDA/Fimea label warnings and contraindications — are missing, one of them flagged as a **Blocking** data gap that prevents initial safety screening (S1).

**To proceed, the following is needed:**
- Official label/package insert data (warnings, contraindications, DDI) — currently a Blocking gap
- Mechanism of action (MOA) confirmation via DrugBank or equivalent source
- Documentation of linaclotide's original approved indication(s)
- Ongoing monitoring for new clinical trials or literature on cauda equina syndrome, neurogenic bladder, or insomnia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

