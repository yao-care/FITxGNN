---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is a second-generation tyrosine kinase inhibitor established for chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL). The TxGNN model's top prediction is that it may also be effective in **Ewing Sarcoma**, with **3 clinical trials** and **9 publications** currently identified, though the mechanistic rationale (SRC/FAK pathway inhibition) is stronger than the clinical evidence, which remains largely preclinical and non-disease-specific.

> **Note on model validation:** TxGNN's rank-2 prediction for dasatinib is "myeloid leukemia" — which is not a new indication but dasatinib's *original*, already-approved use (confirmed by the DASISION trial, PMID 27217448, in this same evidence pack). This is a useful sanity check: the model correctly recovers a known true positive, which lends some circumstantial credibility to its ranking of Ewing sarcoma, but does not substitute for disease-specific validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukemia (CML) / Ph+ ALL *(not present in the Taiwan/Finland regulatory dataset — drug is unmarketed there; based on globally established approved indications, corroborated by literature evidence in this pack)* |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% (rank 1502) |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap, High severity). Based on known information, dasatinib is a multi-target kinase inhibitor originally developed for BCR-ABL–driven leukemias, and its efficacy in chronic myeloid leukemia and Ph+ ALL is well established and mechanistically may extend beyond hematologic malignancy given its activity against SRC-family kinases, c-KIT, and PDGFR-β.

Ewing sarcoma is biologically distinct from CML — it is a bone/soft-tissue sarcoma of neuroectodermal origin driven by the EWSR1-FLI1 fusion oncogene, not by BCR-ABL. There is therefore no shared disease lineage with dasatinib's original indication; the rationale instead rests entirely on a shared downstream molecular target rather than a shared tumor origin.

Mechanistically, Ewing sarcoma cell invasion and metastasis are highly dependent on SRC/FAK signaling. Dasatinib, as a potent SRC-family kinase inhibitor, has been shown in vitro to suppress migration/invasion and induce apoptosis in Ewing sarcoma cell lines. However, this is an indirect mechanistic link (inhibiting a downstream signaling node) rather than a direct hit on the disease's driver oncogene, and single-agent dasatinib has previously underperformed in a Phase 2 basket trial for sarcomas including Ewing sarcoma — suggesting any future clinical benefit would likely require combination strategies rather than monotherapy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib combined with ifosfamide, carboplatin, and etoposide in Ewing sarcoma and related tumors; trial terminated, and the small sample size (n=7) sharply limits any conclusions. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Basket trial of single-agent dasatinib across advanced sarcomas (response rate, 6-month PFS); Ewing sarcoma was one of several subtypes enrolled, not a dedicated disease-specific design — subgroup results for Ewing sarcoma specifically were not reported here. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | Trial of B7-H3 CAR-T cell therapy (not dasatinib) in pediatric/young-adult relapsed/refractory solid tumors; overlaps only in disease population, not in study drug. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Curr Treat Options Oncol | Review of systemic therapy for chondrosarcoma; tangential to Ewing sarcoma, likely surfaced via cross-sarcoma search overlap. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Reviews the role of Src signaling across sarcoma biology, supporting Src as a plausible therapeutic target class. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical (in vitro) | Cancer Research | Dasatinib inhibits migration/invasion across diverse sarcoma cell lines and induces apoptosis in Src-dependent bone sarcoma cells. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclinical | Sarcoma | Studies FAK-Src complex targeting in DSRCT, Ewing sarcoma, and rhabdomyosarcoma; notes single-agent dasatinib previously failed in a Phase 2 trial for these subtypes, motivating combination approaches. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical (in vitro) | Oncology Reports | Dasatinib shows antiproliferative and antimigratory activity in neuroblastoma and Ewing sarcoma cell lines, linked to c-KIT/PDGFR inhibition. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate to drive invadopodia formation and metastatic invasion in Ewing sarcoma. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical (in vitro) | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia activation and cell migration in Ewing sarcoma. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical (different agent: plerixafor) | Cell Commun Signal | CXCR4 antagonist plerixafor (not dasatinib) promotes Ewing sarcoma proliferation via receptor tyrosine kinase signaling; included through disease-overlap search, not a dasatinib study. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Case report | Case Reports in Oncology | Describes a rare chromosomal abnormality in CML blast crisis; not related to Ewing sarcoma — likely a search mismatch. |

## Cytotoxicity

Dasatinib is an antineoplastic agent (tyrosine kinase inhibitor class), so this section applies. Note: TFDA/regulatory label data for dasatinib is a **Blocking** data gap in this evidence pack (no package insert available), so the items below draw on the drug class and on safety signals present in this evidence pack's literature rather than an official label — they should not substitute for label review.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — second-generation multi-target tyrosine kinase inhibitor (BCR-ABL, SRC-family, c-KIT, PDGFR-β) |
| Myelosuppression Risk | Moderate–High — cytopenias (including thrombocytopenia) are a recognized class effect of dasatinib and other BCR-ABL TKIs (e.g., a dedicated trial investigated IL-11 for TKI-associated thrombocytopenia, NCT00493181); routine hematologic monitoring is warranted |
| Emetogenicity Classification | Low (oral targeted therapy, not conventional cytotoxic chemotherapy) |
| Monitoring Items | CBC with differential, liver function, and pulmonary/pleural status — literature in this evidence pack documents dasatinib-associated pleural effusion/chylothorax and interstitial pneumonitis as class-relevant adverse events |
| Handling Protection | Oral hazardous/antineoplastic agent — institutional hazardous drug handling precautions apply; formal TFDA label warnings are pending (Blocking data gap) |

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings, contraindications, and drug-drug interaction data are currently unavailable (Blocking data gap — DG001), so no structured safety data from this evidence pack can be cited here.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (SRC/FAK-pathway dependence in Ewing sarcoma) is plausible, but clinical support is weak — the only disease-related trial with meaningful enrollment (NCT00464620) is a non-disease-specific sarcoma basket trial, and the one Ewing-sarcoma–focused trial was terminated at n=7. Combined with a Blocking data gap on TFDA safety/label information (which prevents even an initial S1 safety assessment) and the drug being unmarketed in Finland, there is insufficient basis to proceed at this time.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications, DDI) to clear the Blocking safety gap
- Confirmed mechanism-of-action data from DrugBank
- Ewing-sarcoma-specific subgroup results from NCT00464620 (the completed Phase 2 basket trial)
- Any updated combination-therapy trial data, since single-agent dasatinib has previously underperformed in sarcoma trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

