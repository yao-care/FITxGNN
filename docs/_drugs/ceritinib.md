---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is a second-generation ALK tyrosine kinase inhibitor whose approved use — based on the trial and review literature returned in this evidence pack — is ALK-rearranged non-small cell lung cancer (NSCLC); the drug's own structured original-indication field is empty in this pack (data gap). The TxGNN model's top prediction for this drug is **Gingival Fibromatosis**, but this prediction has **zero clinical trials and zero literature** support and no known mechanistic link to the ALK pathway — it is a model-score-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive (ALK-rearranged) non-small cell lung cancer — inferred from literature within this evidence pack (e.g., ASCEND-4, "Ceritinib: first global approval"); not available from the structured `taiwan_regulatory`/`original_indications` fields (data gap) |
| Predicted New Indication | Gingival Fibromatosis (Fibromatosis, Gingival) |
| TxGNN Prediction Score | 99.86% (rank 2020 among all candidates) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured `original_moa` field (data gap, DG002). Based on the literature captured elsewhere in this evidence pack, ceritinib is a second-generation, orally bioavailable small-molecule inhibitor of anaplastic lymphoma kinase (ALK), developed for tumours driven by ALK gene rearrangements, most notably ALK-rearranged NSCLC (PMID 24980964, 27738095, 28126333).

Gingival fibromatosis is a benign, typically hereditary or drug-induced (e.g., phenytoin, cyclosporine, calcium-channel blockers) overgrowth of gingival connective tissue. There is no established biological pathway connecting ALK receptor tyrosine kinase signalling to gingival fibrous overgrowth, and no fibroblast-proliferation or connective-tissue mechanism is referenced anywhere in the evidence supplied.

Consistent with this, the evidence pack's own rationale for this candidate states directly: there are no clinical trials, no literature, and no known mechanistic association between the ALK pathway and gingival fibromatosis — this is purely a TxGNN prediction score with no corroborating evidence of any kind.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Ceritinib is currently **not marketed in Taiwan** — 0 authorizations are on record, and the `licenses` array is empty, so no authorization number, product name, dosage form, or approved-indication text can be extracted from this evidence pack.

## Cytotoxicity

Ceritinib is an antineoplastic agent (ALK/ROS1 tyrosine kinase inhibitor used in NSCLC per the literature evidence above), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (second-generation ALK tyrosine kinase inhibitor; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Not specifically reported in the supplied evidence; as a class, ALK inhibitors typically carry lower myelosuppressive risk than conventional cytotoxic chemotherapy — please refer to the package insert for haematological toxicity grading |
| Emetogenicity Classification | Moderate — GI toxicity is reported in the evidence (ASCEND-8 subgroup analysis, PMID 35344649, found reduced GI toxicity with a modified with-food dosing regimen, implying baseline GI toxicity is clinically relevant) |
| Monitoring Items | ECG/QTc interval (PMID 26008987, 29413968), liver function, GI symptoms (nausea, diarrhoea), thromboembolic events (PMID 39349372), and pulmonary/hypersensitivity symptoms (PMID 31280988 — case of diffuse infiltrative lung disease, pericarditis, and pleural effusion with ceritinib hypersensitivity) |
| Handling Protection | Not specified in the evidence pack. As an oral small-molecule targeted agent, follow institutional oral-oncolytic handling protocols pending confirmation from the TFDA package insert (see blocking data gap below) |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack; the TFDA package insert has not yet been retrieved.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, gingival fibromatosis, has no clinical trial or literature support and no plausible mechanistic link to ALK inhibition — it is a pure model-score artifact (L5, decision stage S0). None of the other 9 candidates in this batch fare better: the two with any literature (lung benign neoplasm, lung germ cell tumor, both L4) are explicitly flagged in their own rationale as ontology-driven mismatches (evidence concerns malignant NSCLC or glioblastoma/CNS metastasis, not the benign entities predicted), and the remaining 7 have no evidence at all.

**To proceed, the following is needed:**
- TFDA package insert retrieval and parsing for warnings/contraindications (blocking gap DG001)
- DrugBank MOA confirmation (DG002)
- If pursuing repurposing further, prioritize mechanistically plausible, evidence-searchable candidates (e.g., ALK-rearranged tumour subtypes) over the current top-ranked prediction
- No further development recommended for gingival fibromatosis or any of the other 9 predicted indications in this batch given the absence of supporting evidence and mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

