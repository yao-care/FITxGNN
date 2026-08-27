---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB), an established antihypertensive drug class. TxGNN's highest-scoring prediction for this drug is **Prinzmetal angina**, but currently **no clinical trials and no literature** support this specific drug-disease link, and the drug's own mechanism does not align with the accepted treatment pathway for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class; no formal marketing authorization or licensed indication text on file in this market) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for telmisartan is not available in this evidence pack. Based on known information, telmisartan is an angiotensin II type 1 (AT1) receptor blocker within the ARB class, and its efficacy in hypertension management is well established in general clinical practice.

Prinzmetal (variant) angina, however, is caused by coronary artery vasospasm, and its first-line treatment is calcium channel blockers, not RAAS-pathway agents. According to the evidence pack's own mechanistic assessment, ARB blockade has no established direct pharmacological pathway to coronary vasospasm, and this candidate is supported by neither trials nor literature — the mechanistic link is explicitly rated as weak.

In other words, this is a case where TxGNN's network-similarity score is high, but the underlying pharmacology and the evidence base do not yet corroborate it. The prediction should be treated as a hypothesis-generating signal only, not as a validated repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Telmisartan currently has no active marketing authorizations on file in this jurisdiction (market status: not marketed; 0 licenses). No approved product/indication text is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert data for warnings and contraindications is flagged as a Blocking data gap (DG001) in this evidence pack — this should be resolved before any safety-based decision-making.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for Prinzmetal angina is high, but there is no clinical trial or literature evidence, and the drug's ARB mechanism does not plausibly explain efficacy in a coronary-vasospasm-driven condition whose standard therapy operates through a different pathway (calcium channel blockade). Evidence Level L5 (model prediction only) does not support progression.

**To proceed, the following is needed:**
- Detailed mechanism-of-action (MOA) data for telmisartan (High-severity gap, DG002)
- TFDA/Fimea package insert — warnings and contraindications (Blocking gap, DG001)
- Preclinical or mechanistic studies linking AT1 blockade to coronary vasospasm, to establish biological plausibility before further investment

---

### Other Candidate Indications in This Evidence Pack

This evidence pack is a multi-indication candidate set; two other TxGNN-predicted indications carry substantially stronger evidence than Prinzmetal angina and may warrant separate evaluation:

- **Cerebral artery occlusion** (rank 4, score 99.95%) — Evidence Level L2, recommendation "Research Question." Supported by 1 completed Phase 4 RCT (n=1,228) and 17 preclinical publications showing neuroprotective effects in stroke models, though human causal evidence remains indirect.
- **Intracerebral hemorrhage** (rank 9, score 99.93%) — Evidence Level L2, recommendation "Research Question." Supported by the completed Phase 3 TRIDENT trial (n=1,671) for recurrence prevention, though telmisartan was one component of a triple-pill combination rather than an independently tested agent.

These would be better candidates for a dedicated evaluation report than Prinzmetal angina.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

