---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 chemokine receptor antagonist originally developed to block CCR5-tropic HIV-1 entry into host cells. The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, with a very high similarity score (99.82%), but currently **0 clinical trials** and **0 publications** support this specific direction, and the underlying mechanistic rationale is explicitly assessed as unsubstantiated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (CCR5-tropic strains) — evidence pack contains no `original_indications` entries; based on the drug's known pharmacological classification |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological classification, maraviroc is a CCR5 chemokine receptor antagonist; its established clinical use is blocking CCR5-mediated HIV-1 cell entry.

Multiple Endocrine Neoplasia is a hereditary endocrine tumour syndrome driven by germline mutations in genes such as *RET* and *MEN1*, with no established connection to CCR5 chemokine signalling. The repurposing rationale attached to this prediction states directly that "no known association exists between MEN and the CCR5 chemokine signalling pathway, and the mechanistic basis does not hold" (機轉不成立).

Despite the high TxGNN similarity score, the model's output here should be treated as a statistical association from the knowledge graph rather than a mechanistically grounded hypothesis. No clinical trials, literature, or preclinical data currently support this specific drug-disease pairing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Maraviroc is not currently marketed in Finland (0 authorizations on record), so no product/license table can be produced from this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction carries a high TxGNN score but is assessed at Evidence Level L5 (model prediction only) with zero supporting clinical trials or publications, and the repurposing rationale explicitly states no plausible mechanistic link between CCR5 antagonism and MEN pathogenesis.

**To proceed, the following is needed:**
- Confirmed mechanism of action documentation for maraviroc (currently a blocking/high-severity data gap)
- TFDA/regulatory package insert data covering warnings, contraindications, and DDI (currently a blocking data gap)
- Preclinical or mechanistic studies specifically linking CCR5 signalling to endocrine neoplasia pathways before any further evaluation of this indication

**Note on portfolio prioritization:** Among the 10 TxGNN-predicted indications for maraviroc in this evidence pack, **HER2-positive breast carcinoma** (rank 10, decision stage S1, "Research Question") has the strongest mechanistic support — a published preclinical study (PMID [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/)) shows autocrine CCL5-CCR5 signalling drives trastuzumab resistance via ERK pathway activation, suggesting CCR5 blockade could restore trastuzumab sensitivity. This candidate, rather than MEN, may warrant a dedicated follow-up evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

