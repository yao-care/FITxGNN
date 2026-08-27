---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From an Undocumented Original Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Tadalafil is a PDE5 inhibitor (per the evidence pack's own rationale text, already approved for WHO Group 1 pulmonary arterial hypertension); its original indication record for this evaluation is not documented.
> The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital multi-hair syndrome,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — the model's own rationale flags it as a likely embedding-space artifact rather than a mechanistic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Finland licensing data absent) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tadalafil is flagged as a gap in this evidence pack (DG002). The only mechanistic context available comes from the model's own rationale text across the eight candidate indications: tadalafil is described there as a PDE5 inhibitor that raises cGMP levels and relaxes vascular smooth muscle, and is already an approved therapy for WHO Group 1 pulmonary arterial hypertension.

For the top-ranked candidate — Ambras type hypertrichosis universalis congenita, a rare genetic syndrome typically linked to chromosome 8q rearrangements — the evidence pack's rationale explicitly states there is **no known pathological connection** to PDE5 inhibition, cGMP signaling, or vascular smooth muscle relaxation. It characterizes the high TxGNN score as most likely an artifact of embedding-space similarity rather than a genuine mechanistic inference.

A weaker, secondary hypothesis appears for the related rank-2 prediction (hypertrichosis, general): topical vasodilators such as minoxidil can promote follicular growth, and PDE5 inhibitors share vasodilatory pharmacology in principle. However, this remains speculative extrapolation with no clinical or case-report support in the current evidence, and does not apply to the rank-1 Ambras-syndrome prediction, which is a distinct and much rarer genetic entity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Tadalafil is currently **not marketed** in Finland per this evidence pack (0 authorizations recorded), so no product/license table can be generated.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — obtaining the TFDA/Fimea package insert is flagged as a **blocking** data gap, DG001, required before any safety pre-screening can proceed.)

## Other Predicted Signals & Safety Note

The evidence pack screened 8 TxGNN predictions for tadalafil; all scored in a similarly high but narrow range (99.42%–99.98%), and all but two returned zero supporting literature/trials:

- **Kyphoscoliotic heart disease** (rank 7, L4, stage S1 "Research Question") is the most mechanistically plausible of the set: severe kyphoscoliosis can cause restrictive lung disease with Group 3 pulmonary hypertension, and tadalafil is an approved Group 1 PAH therapy. However, PDE5 inhibitors in hypoxia/lung-disease-related (Group 3) PH are controversial — they can worsen ventilation-perfusion mismatch — and no direct trial evidence exists for this population.
- **Migraine with brainstem aura** (rank 8, L4) surfaced one case report (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)) describing tadalafil-**associated/induced** typical aura without headache — this is an **adverse-effect signal, not therapeutic evidence**, and the rationale explicitly warns TxGNN may have inverted the drug–disease relationship direction. This should be read as a caution, not a repurposing lead.
- The "malformation syndrome with odontal/periodontal component" candidate returned 20 literature hits, but all are general periodontitis pathophysiology reviews with no tadalafil-specific content — a keyword co-occurrence artifact, not real evidence.
- The remaining candidates (hair-shaft abnormality, Dandy-Walker syndrome, familial trichomegaly) have no known mechanistic link and no supporting data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis) has zero clinical trials, zero literature, and no plausible mechanistic link per the model's own rationale — this is a model-score-only signal (L5) with a strong internal warning that it is a statistical artifact. No candidate among the 8 screened reaches even L2/L3 evidence.

**To proceed, the following is needed:**
- Resolve the blocking gap (DG001): obtain the TFDA/Fimea package insert for warnings, contraindications, and DDI before any safety pre-screening (S1) can begin
- Obtain confirmed original MOA and original indication data from DrugBank (DG002) to properly ground any repurposing rationale
- If pursuing further, redirect evaluation toward the more mechanistically defensible candidate — kyphoscoliotic heart disease / Group 3 PH — rather than the top TxGNN-ranked but unsupported hypertrichosis prediction
- Treat the migraine-aura literature signal as a pharmacovigilance flag for existing tadalafil use, not a repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

