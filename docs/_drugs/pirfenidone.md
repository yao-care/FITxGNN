---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an oral antifibrotic agent whose established use is idiopathic pulmonary fibrosis (IPF), acting via inhibition of TGF-β1, PDGF, and collagen synthesis pathways.
The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**, with a prediction score of **99.71%**, but currently **0 clinical trials** and **0 publications** directly support this specific pairing — the signal is model-only at this stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF) — not confirmed via Finland licensing data (drug is unmarketed there); inferred from literature within this evidence pack |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking gap DG002). Based on known information, pirfenidone is an antifibrotic small molecule reported to inhibit TGF-β1, platelet-derived growth factor, and epidermal/fibroblast growth factor signaling, reducing fibroblast proliferation and collagen deposition — the mechanism underlying its efficacy in idiopathic pulmonary fibrosis.

Extracutaneous mastocytoma is a mast cell neoplastic process, biologically distinct from the fibrotic pathology pirfenidone targets. There is no established mechanistic bridge between anti-TGF-β/anti-fibrotic activity and mast cell proliferation control. The TxGNN score most likely reflects an indirect knowledge-graph association (e.g., shared inflammatory or fibrosis-adjacent pathways) rather than a direct causal mechanism, and no clinical, preclinical, or case-level evidence currently exists to support or refute this pairing.

Notably, other lower-ranked predictions in this evidence pack for structurally related "fibroblastic neoplasm" indications carry an important caution: literature evidence includes case reports of tumor progression (undifferentiated pleomorphic sarcoma, aggravated dermatofibromas) following pirfenidone exposure. This raises the possibility that pirfenidone's effect on neoplastic (as opposed to benign) fibrous/connective tissue proliferation could be direction-uncertain — a consideration that should be carried into evaluation of any tumor-related repurposing candidate, including mast cell neoplasms.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Pirfenidone is currently **not marketed in Finland** (0 authorizations on record). No product licenses, dosage forms, or approved-indication text are available for this drug in the Fimea dataset.

## Safety Considerations

- **Data Gaps**: TFDA/Fimea package insert warnings, contraindications, and DDI data are not currently available for pirfenidone (blocking gap DG001) — a formal safety review cannot proceed until this is resolved.
- **Emerging Literature Signal (context, not indication-specific)**: Case reports elsewhere in the evidence pack (PMID [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/): undifferentiated pleomorphic sarcoma after pirfenidone use; PMID [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/): aggravation of eruptive dermatofibromas) suggest a possible tumor-promoting risk in fibrous/connective-tissue neoplastic contexts. This is not proven causality, but it is a relevant flag when evaluating pirfenidone against any neoplastic indication, including mastocytoma.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The extracutaneous mastocytoma prediction is supported only by a TxGNN model score, with no clinical trials, no literature, and no mechanistic rationale connecting pirfenidone's antifibrotic activity to mast cell tumor biology (L5, S0). Combined with an unresolved blocking safety data gap and a literature signal elsewhere in this drug's profile suggesting possible tumor-promoting risk in neoplastic fibrous tissue, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications, DDI) to clear the blocking safety gap (DG001)
- Confirmed mechanism of action data (DG002) to assess biological plausibility against mast cell pathways
- Preclinical or in vitro evidence specifically evaluating pirfenidone in mast cell proliferative disease
- Targeted investigation of the tumor-progression signal seen in other fibroblastic neoplasm case reports, to rule out a class-level promotive risk before pursuing any oncologic repurposing indication for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

