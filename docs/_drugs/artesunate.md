---
layout: default
title: Artesunate
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 0
---

# Artesunate
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

# Artesunate: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

Artesunate is a semi-synthetic artemisinin derivative widely recognized as a frontline antimalarial agent.
The current Evidence Pack contains **no TxGNN predicted indications**, making a standard repurposing evaluation impossible at this stage.
Before proceeding, critical data gaps — including MOA, safety profile, and model predictions — must be resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction data absent |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack, and the TxGNN pipeline has not returned any predicted indications for artesunate. As a result, no mechanistic or evidence-based repurposing argument can be constructed at this time.

Artesunate belongs to the artemisinin class of antimalarials. It is publicly recognized for its role in treating severe and uncomplicated malaria, including multidrug-resistant *Plasmodium falciparum* infections. There is emerging research interest in its potential anticancer and anti-inflammatory properties — however, without TxGNN scoring and a complete input knowledge graph, any such direction remains speculative and cannot be formally evaluated here.

Re-running the TxGNN model with complete DrugBank MOA data and a properly linked disease knowledge graph is the necessary prerequisite for generating credible repurposing candidates.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN predicted indications and no original indication records, making it impossible to evaluate repurposing potential or assess benefit-risk balance at this stage. This is a data completeness issue, not a negative signal about the drug itself.

**To proceed, the following is needed:**

- **Re-run TxGNN model** with complete input data to generate predicted indication scores
- **Retrieve MOA data** from DrugBank (DB09274) — flagged as a High-severity gap (DG002)
- **Parse Finland package insert PDF** to obtain approved indications, key warnings, and contraindications — flagged as a Blocking gap (DG001)
- **Verify knowledge graph linkage** for artesunate to ensure disease–drug edges are correctly populated before re-prediction
- **Re-run DDI query** once the drug profile is complete
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

