---
layout: default
title: Elafibranor
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 1
---

# Elafibranor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Elafibranor: From Primary Biliary Cholangitis (in development) to Amenorrhea

## One-Sentence Summary

Elafibranor is a PPARα/δ dual agonist being developed for **primary biliary cholangitis (PBC)**; it is not yet marketed in Taiwan. The TxGNN model predicts a possible link to **Amenorrhea**, but this direction currently has **no clinical trials and no supporting literature** — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary biliary cholangitis (PBC) — per repurposing rationale; drug is under indication development, not yet TFDA-approved |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.86% (rank 1953) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is not available in DrugBank for this record. Based on the repurposing rationale provided, elafibranor is a PPARα/δ dual agonist under development for primary biliary cholangitis, acting mainly on hepatic lipid and bile acid metabolism pathways.

There is no established mechanistic link between this pathway and amenorrhea. The PPAR receptor family has some indirect literature association with adipose tissue and certain steroidogenesis processes, but this connection has not been validated for elafibranor or its drug class, and there is no known direct interaction with the hypothalamic-pituitary-ovarian axis or gonadotropin regulation.

In short, the mechanistic connection between PBC and amenorrhea is speculative rather than established, and on its own is insufficient to support a causal hypothesis for repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5), with zero clinical trials, zero literature, and no validated mechanistic link between PPARα/δ agonism and amenorrhea. Combined with a Blocking data gap on TFDA labeling (DG001), this is not ready to advance.

**To proceed, the following is needed:**
- TFDA package insert / warnings & contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Preclinical or mechanistic evidence connecting PPAR pathway activity to menstrual/reproductive endocrine function
- Any emerging clinical trial or case-report signal for amenorrhea/reproductive effects (including as an adverse event in existing PBC trials)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

