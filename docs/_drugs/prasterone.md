---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From No Approved Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Prasterone (DHEA, DrugBank DB01708) is not currently marketed in this jurisdiction and has no on-file approved indication, so its original clinical use cannot be established from available data. The TxGNN model's top-ranked prediction points to **Heparin Cofactor 2 Deficiency**, but this signal is supported by **0 clinical trials** and **0 publications**, and the proposed mechanism plausibly runs in the *wrong direction* — androgenic steroids are generally associated with a procoagulant, not anticoagulant, profile. This candidate should be treated as speculative until independent mechanistic or clinical evidence emerges.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — drug is not marketed in this market, no approved indication text available |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Prasterone. Based on known information, Prasterone is a naturally occurring adrenal precursor steroid that is metabolized into androgens and estrogens; it has not been established as approved therapy in this market, so its clinical efficacy profile here is undocumented.

Heparin cofactor 2 (HCII) deficiency is a rare hereditary condition in which reduced activity of an anticoagulant plasma protein raises the risk of venous thrombosis. A therapeutically useful agent for this condition would need to support anticoagulant activity or otherwise reduce thrombotic tendency. The evidence pack's own mechanistic assessment flags a direction problem: androgenic/DHEA-related compounds are more commonly reported in the literature as having a *procoagulant* association (e.g., elevated thrombophilia risk in high-androgen states such as PCOS, cited under a related predicted indication in this same pack) rather than a protective one.

Taken together, the TxGNN score most likely reflects proximity between DHEA-related nodes and coagulation-pathway nodes in the knowledge graph, rather than a validated therapeutic relationship. Without any clinical trial or literature confirmation, and with a plausible mechanistic contradiction, this prediction should be treated as a hypothesis-generating signal only, not a repurposing lead ready for evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying data pack flags the TFDA/regulatory package insert as a Blocking data gap — this must be resolved before any safety-based go/no-go decision.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Heparin Cofactor 2 Deficiency) has no clinical trial or literature support (L5, purely model-derived), and the proposed mechanism may run counter to the therapeutic need — androgenic activity is more often linked to increased thrombotic risk than to correction of an anticoagulant deficiency. Combined with the absence of MOA data and TFDA/Fimea labeling information, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Prasterone from DrugBank or primary pharmacology sources
- Regulatory package insert (warnings, contraindications, DDI) to close the Blocking data gap (DG001)
- Preclinical or pharmacodynamic data specifically addressing DHEA's effect on HCII activity/thrombotic risk, to resolve the directional mechanistic concern
- If this program continues, consider re-scoping toward **scleroderma** (rank 7 in the same evidence pack), which reached decision stage S1 with L4 evidence — six cohort/case-control studies consistently show reduced serum DHEA-S in systemic sclerosis patients correlating with disease severity, offering a more coherent (deficiency-replacement) mechanistic rationale than the top-ranked candidate here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

