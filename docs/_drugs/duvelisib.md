---
layout: default
title: Duvelisib
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

# Duvelisib: From Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma to Hodgkin's Lymphoma

## One-Sentence Summary

Duvelisib is a PI3Kδ/γ dual inhibitor whose only confirmed use (per the literature in this evidence pack) is relapsed/refractory chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) and follicular lymphoma; it is **not marketed in Finland**.
The TxGNN model's top-ranked prediction is **Hodgkin's Lymphoma**, with **11 clinical trials** and **16 publications** retrieved for this pairing — but on inspection, every one of them actually studies **Non-Hodgkin lymphoma** subtypes, not true Hodgkin's lymphoma. This is flagged in the evidence pack itself as a likely disease-ontology mismatch, not a genuine mechanistic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory CLL/SLL and follicular lymphoma (per literature; not a Fimea-approved indication — drug is unmarketed in Finland) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (drug.original_moa = Data Gap). Based on the literature retrieved in this evidence pack, duvelisib is described as an oral dual inhibitor of phosphoinositide-3-kinase (PI3K)-δ and PI3K-γ, blocking B-cell receptor signaling and tumor-microenvironment survival cues in lymphoid malignancies. It received its first global approval (outside Finland/Taiwan) for CLL/SLL, and later follicular lymphoma.

**Important caveat:** the repurposing rationale explicitly attached to this candidate states that of the 11 trials and 16 papers surfaced for "Hodgkin's Lymphoma," none actually studies classical Hodgkin's lymphoma (Reed-Sternberg cell biology, NF-κB/EBV-driven pathogenesis). All of them study indolent/aggressive **Non-Hodgkin lymphoma** (follicular lymphoma, CLL/SLL, mantle cell lymphoma, peripheral T-cell lymphoma). This pattern is consistent with a knowledge-graph disease-naming collision ("Hodgkin's" vs. "Non-Hodgkin's") rather than a real mechanistic link between PI3Kδ/γ inhibition and Hodgkin's lymphoma biology. The evidence below should be read with that mismatch in mind — it supports duvelisib's role in B/T-cell NHL, not HL.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | YY-20394 (a duvelisib analog) monotherapy in relapsed/refractory **follicular Non-Hodgkin lymphoma** failing ≥2 prior therapies |
| [NCT05923502](https://clinicaltrials.gov/study/NCT05923502) | N/A | Not yet recruiting | 200 | Real-world, non-interventional study of duvelisib capsules in **Non-Hodgkin lymphoma (NHL)** |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | CHO(E)P vs. CC-486-CHO(E)P vs. duvelisib-CHO(E)P in untreated CD30-negative **peripheral T-cell lymphoma** (relevance grade C — not HL) |
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Completed | 129 | Duvelisib monotherapy in rituximab-refractory **indolent Non-Hodgkin lymphoma** (FL, MZL, SLL) (relevance grade C — distinct disease entity from HL) |
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Compared two intermittent dosing schedules of duvelisib in **indolent NHL** (relevance grade C — not HL) |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, not recruiting | 42 | Duvelisib after CAR T-cell therapy to improve CAR T persistence via PI3K inhibition, in lymphoid malignancies |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Withdrawn | 0 | Duvelisib + acalabrutinib in relapsed/refractory **indolent NHL** (DUAL trial) |
| [NCT02640833](https://clinicaltrials.gov/study/NCT02640833) | Phase 1 | Withdrawn | 0 | Duvelisib + venetoclax in relapsed/refractory CLL, SLL, or indolent/aggressive **NHL** |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Duvelisib + BMS-986345 combination, safety/tolerability in lymphoid malignancy |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Completed | 48 | IPI-145 (duvelisib) + rituximab or bendamustine/rituximab in lymphoma or CLL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic Review/Meta-analysis | Frontiers in Immunology | Safety and efficacy of duvelisib across relapsed/refractory lymphoid neoplasms |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Preclinical | Scientific Reports | PI3Kγ/δ expression drives mantle cell lymphoma proliferation/migration, supporting duvelisib efficacy in MCL |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Review | The Lancet Oncology | Duvelisib in indolent Non-Hodgkin lymphoma |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | Am J Health-Syst Pharm | Summary of approved targeted therapies for B- and T-cell lymphomas |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Clinical (Phase 1) | Am J Hematology | Duvelisib + rituximab or bendamustine/rituximab in NHL/CLL patients |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | Novel therapy approaches, including PI3K inhibitors, in follicular lymphoma |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Curr Treat Options Oncol | PI3K inhibitors as targeted therapy in lymphoma, incl. duvelisib |
| [39836493](https://pubmed.ncbi.nlm.nih.gov/39836493/) | 2025 | Preclinical/Mechanistic | Advanced Science | TTK as a novel drug target in T-cell lymphoma (mechanistic, not duvelisib-specific) |
| [27872741](https://pubmed.ncbi.nlm.nih.gov/27872741/) | 2016 | Review | Mediterr J Hematol Infect Dis | Novel drugs, incl. PI3K inhibitors, in follicular lymphoma |
| [32658557](https://pubmed.ncbi.nlm.nih.gov/32658557/) | 2020 | Review | Future Oncology | Role of PI3K inhibitors (copanlisib class) in Non-Hodgkin lymphoma |

## Finland Market Information

No Finland market authorization records exist for duvelisib — `taiwan_regulatory.market_status` = 未上市 (not marketed), 0 authorizations on file.

## Cytotoxicity

Duvelisib is an antineoplastic agent (targeted kinase inhibitor used for hematologic malignancies).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ/γ dual inhibitor), not a conventional cytotoxic chemotherapy — per literature (PMID 38423708, 30430368) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

*Note: this evidence pack flags a Blocking data gap (DG001) — TFDA/package-insert warnings and contraindications could not be retrieved, which by itself prevents entry into the S1 safety pre-assessment stage regardless of efficacy evidence.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence base for "Hodgkin's Lymphoma" is built entirely on Non-Hodgkin lymphoma trials/literature — a likely disease-ontology naming collision rather than a genuine mechanistic signal, so the L4/Hold call from the evidence pack stands.
- A Blocking data gap (DG001: TFDA package insert / warnings and contraindications) independently prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- Resolve the Hodgkin's vs. Non-Hodgkin's lymphoma entity mapping before any further evaluation of this candidate
- Retrieve TFDA/manufacturer package insert (warnings, contraindications, DDI) — DG001
- Retrieve confirmed mechanism of action from DrugBank — DG002
- If re-scoping to Non-Hodgkin lymphoma subtypes is warranted, note that "B-cell neoplasm" (rank 9 in this evidence pack) already carries L1 evidence (Phase 3 DUO trial) — but that reflects duvelisib's existing approved indication (CLL/SLL, FL), not a novel repurposing opportunity, and should be evaluated as a market-access question rather than a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

