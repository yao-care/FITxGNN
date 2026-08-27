---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From Unrecorded Original Indication to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen's original indication and mechanism of action could not be retrieved from the available regulatory sources for this candidate. The TxGNN model's top prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare GDF5-related skeletal dysplasia, but **no clinical trials and no literature** currently support this direction, and the drug is not marketed in Finland.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available regulatory data |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ibuprofen in this evidence pack. Based on general pharmacological knowledge, Ibuprofen is a non-selective COX-1/COX-2 inhibitor with analgesic and anti-inflammatory activity, but this was not confirmed through the DrugBank query underlying this candidate.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare skeletal dysplasia caused by *GDF5* mutations affecting endochondral ossification — a pathway unrelated to prostaglandin synthesis or COX inhibition. The evidence pack's own mechanistic assessment states there is **no known mechanistic link** between Ibuprofen and the GDF5/BMP signaling pathway, and suggests the high TxGNN score more likely reflects a learned association with joint-symptom comorbidity (e.g., osteoarthritis-type pain management common to skeletal dysplasias) rather than a disease-modifying mechanism.

The remaining six predicted indications (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, and colobomatous microphthalmia-rhizomelic dysplasia syndrome) show the same pattern: TxGNN scores above 99%, but each rationale explicitly notes an absent or purely symptomatic (not disease-modifying) mechanistic basis. This is consistent with the model surfacing a shared "rare skeletal disorder + analgesic comorbidity" signal rather than a genuine repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Ibuprofen has no active marketing authorizations recorded for this candidate (0 authorizations; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trial or literature support, no confirmed mechanistic link, and the underlying regulatory/safety data (original indication, MOA, TFDA warnings, DDI) are all missing — this candidate does not meet even a minimal evidentiary bar to proceed.

**To proceed, the following is needed:**
- TFDA/EMA package insert (warnings, contraindications, DDI) to clear the blocking safety data gap
- Confirmed mechanism of action from DrugBank or primary literature
- Independent biological plausibility review of the GDF5/BMP pathway relative to COX inhibition, given the model's own rationale casts doubt on a causal mechanism
- Re-screening for lower-ranked but mechanistically stronger candidates, since all seven predictions in this pack score similarly (L5, Hold) with no differentiating evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

