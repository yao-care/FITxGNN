---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 2
---

# Ponatinib
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

# Ponatinib: From Chronic Myeloid Leukemia to Gingival Fibromatosis

## One-Sentence Summary

Ponatinib is a multi-target tyrosine kinase inhibitor best known for treating chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL). The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukemia (CML) / Ph+ acute lymphoblastic leukemia (general drug knowledge; not confirmed by a local license record) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in this evidence pack). Based on known information, ponatinib is a third-generation, multi-target tyrosine kinase inhibitor (BCR-ABL, including the T315I-resistant mutant, plus VEGFR, FGFR, PDGFR and SRC-family kinases), and its efficacy in CML/Ph+ ALL has been proven; mechanistically, some of these same kinases (notably PDGFR and related fibro-proliferative pathways) are implicated in fibrotic gum overgrowth, which is the theoretical basis TxGNN's knowledge graph likely relied on.

Chronic myeloid leukemia and gingival fibromatosis are biologically unrelated conditions — one is a hematologic malignancy driven by the BCR-ABL fusion kinase, the other is a benign, often hereditary, fibroblast-proliferative disorder of the gums. The mechanistic bridge is therefore indirect: it depends on ponatinib's off-target inhibition of PDGFR/kinase pathways that also drive fibroblast proliferation and extracellular matrix deposition, rather than on any shared disease biology with CML. Given that this prediction has zero clinical trial or literature support, it should be treated as a hypothesis generated purely from the model's learned associations rather than an evidence-backed signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Ponatinib currently holds no marketing authorizations in this jurisdiction (status: **Not marketed**, 0 licenses on record), so no approved indication text is available for comparison.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: BCR-ABL, VEGFR, FGFR, PDGFR, SRC-family) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Note: Rank 2 Predicted Indication

A second predicted indication, **liposarcoma**, scored nearly as high (99.00%, TxGNN rank 9484) and — unlike gingival fibromatosis — has one supporting preclinical publication: [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) (2017, *Journal of Hematology & Oncology*), a kinase-profiling/RNAi drug-screening study identifying druggable kinase targets in liposarcoma. This is preclinical, not clinical, evidence, but it gives liposarcoma a stronger (though still early) evidentiary basis than the top-ranked indication and may warrant separate follow-up.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (gingival fibromatosis) has no clinical trial or literature support — only a model score — placing it at Evidence Level L5. Combined with a Blocking data gap on package insert/safety data (DG001) and the drug not being marketed in this jurisdiction, there is insufficient basis to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications, DDIs) — currently a Blocking gap
- Confirmed mechanism of action from DrugBank — currently a High-severity gap
- Targeted literature/preclinical search specific to gingival fibromatosis to test the mechanistic hypothesis
- Consider parallel evaluation of the liposarcoma signal (rank 2), which has at least one supporting preclinical publication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

