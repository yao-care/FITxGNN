---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Upadacitinib: Indication Data Not Yet Available → Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib's original approved indication and mechanism-of-action details are not yet available in this evidence pack (data gap). The TxGNN model predicts potential activity against **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare congenital developmental disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license/indication data on file) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.61% (rank 4612) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for upadacitinib is not currently available in this evidence pack, and no original indication is on file, so a direct mechanistic bridge cannot be constructed from the input data alone. Based on the model's own rationale output, upadacitinib is a JAK1-selective inhibitor acting on cytokine signaling (IL-6, IL-4/13, IFN pathways).

Colobomatous microphthalmia-rhizomelic dysplasia syndrome, however, is a structural/developmental disorder — congenital ocular malformation combined with proximal limb skeletal dysplasia — typically linked to ciliopathy or peroxisomal gene defects (e.g., PEX7-related rhizomelic chondrodysplasia punctata), not to inflammatory or autoimmune signaling. There is no established link between JAK-STAT cytokine signaling and the ocular/skeletal embryonic developmental pathways implicated in this syndrome.

The model's own repurposing rationale concludes that the high TxGNN score most likely reflects **knowledge-graph node proximity** (e.g., clustering with other rare/developmental disease nodes) rather than genuine mechanistic plausibility. No mechanistic, preclinical, or clinical evidence currently supports this pairing — this is consistent with the L5 evidence level and Hold recommendation.

A second candidate, brachydactyly-syndactyly syndrome (score 99.58%, rank 4924), shows the same pattern: a skeletal/limb-development disorder (HOX, BMP/GDF, GLI3 pathways) with no direct overlap to JAK1 inhibition, and likewise zero supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Upadacitinib is not currently marketed in Taiwan (0 authorizations on file), so no local product/authorization data is available.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications and MOA data are flagged as unresolved data gaps — see Conclusion below.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are algorithm-only (L5) signals with no supporting clinical trials, literature, or plausible mechanistic link — the model's own rationale suggests the high scores likely reflect knowledge-graph proximity rather than biological relevance. The drug is also not marketed in Taiwan, and core drug-level data (MOA, TFDA label) remain unresolved.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently a **Blocking** data gap
- Mechanism-of-action confirmation from DrugBank — currently a **High**-severity data gap
- Original approved-indication data for upadacitinib
- Preclinical or mechanistic studies directly linking JAK1 inhibition to either candidate disease before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

