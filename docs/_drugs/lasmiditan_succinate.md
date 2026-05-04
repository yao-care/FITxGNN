---
layout: default
title: Lasmiditan Succinate
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Lasmiditan Succinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Lasmiditan Succinate: Evaluation on Hold — Insufficient Data

## One-Sentence Summary

Lasmiditan Succinate is a drug currently with no registered authorizations in Finland.
This Evidence Pack contains **no TxGNN predicted indications**, and critical data gaps — including mechanism of action, original approved indications, and safety information — prevent any substantive repurposing evaluation at this stage.
Without predicted indication data, evidence level assessment and clinical trial review cannot be conducted.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction data absent |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains no TxGNN predicted indications and is missing all foundational drug data required for evaluation; no repurposing candidate analysis can be performed until these gaps are resolved.

**To proceed, the following is needed:**

- **TxGNN prediction results** — the `predicted_indications` array is empty; re-run the TxGNN pipeline for this drug to obtain candidate indications with scores and evidence links
- **Mechanism of action (MOA)** — query DrugBank API (DrugBank record was found per query log ID 3, but MOA was not extracted into the Evidence Pack)
- **Original approved indication(s)** — `original_indications` is empty; retrieve from the package insert (query log ID 4 indicates a successful fetch — extract and populate)
- **Safety warnings and contraindications** — package insert was successfully retrieved (query log ID 4); parse and populate `key_warnings` and `contraindications`
- **Drug interaction data** — DDI query returned not_found; consider querying alternative sources (e.g., DrugBank interaction API, SFINX)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

