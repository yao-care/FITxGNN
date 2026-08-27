---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myeloid Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a classic bifunctional alkylating agent, historically developed for chronic myeloid leukemia and now used mainly as a myeloablative conditioning agent before allogeneic hematopoietic stem cell transplantation (allo-HSCT). The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, with **50 clinical trials** and **20 publications** currently supporting this direction, including completed Phase 3 randomized trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukemia / myeloablative conditioning agent (based on general pharmacological knowledge — not captured in the current Finland regulatory dataset, which contains no license records) |
| Predicted New Indication | Myelodysplastic Syndrome |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack (MOA field marked as a data gap). Based on well-established pharmacology, busulfan is a bifunctional alkylating agent that cross-links DNA, producing profound, dose-dependent myeloablation. Its established modern clinical role is as a component of **myeloablative/reduced-intensity conditioning regimens** (typically combined with fludarabine or cyclophosphamide) given immediately before allo-HSCT.

MDS is a clonal hematopoietic stem cell disorder for which allo-HSCT remains the only potentially curative treatment in higher-risk disease. To perform allo-HSCT, the recipient's abnormal marrow must first be ablated to allow donor stem cells to engraft — this is exactly the role busulfan-based conditioning already plays in routine clinical practice for MDS. As the repurposing rationale notes, this is not a novel biological hypothesis so much as a confirmation of an already-standard clinical pathway: busulfan-based conditioning (Bu/Flu, Bu/Cy, timed-sequential busulfan, etc.) is widely used pre-transplant for MDS patients, which explains both the very high TxGNN score and the unusually deep clinical trial/literature base for this pairing.

The mechanistic link is therefore strong and directly supported by decades of transplant literature, rather than purely computational inference — multiple Phase 3 randomized trials directly compare busulfan-based conditioning regimens in MDS/AML populations undergoing allo-HSCT.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00416598](https://clinicaltrials.gov/study/NCT00416598) | Phase 2 | Completed | 546 | Maintenance decitabine after busulfan-containing induction/intensification in AML/MDS; large completed study, grade A relevance |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax + timed-sequential busulfan/cladribine/fludarabine conditioning directly in AML and MDS patients |
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Phase 2 | Recruiting | 220 | Randomized comparison of bendamustine vs. ruxolitinib added to fludarabine/busulfan conditioning in haploidentical HSCT |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Phase 2 | Active, not recruiting | 204 | Timed-sequential busulfan plus post-transplant cyclophosphamide conditioning for blood cancers including MDS |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Large treatment-development program for older AML/high-risk MDS patients, including busulfan-based regimens |
| [NCT00002989](https://clinicaltrials.gov/study/NCT00002989) | Phase 3 | Unknown | 207 | Randomized Phase 3 trial intensifying the conditioning regimen for allo-HSCT in leukemia/MDS with high relapse risk |
| [NCT03779854](https://clinicaltrials.gov/study/NCT03779854) | Phase 2 | Recruiting | 68 | Multicenter randomized trial of naïve T-cell depletion for chronic GVHD prevention post-transplant |
| [NCT01861106](https://clinicaltrials.gov/study/NCT01861106) | Phase 2 | Recruiting | 144 | Allo-HSCT for GATA2 deficiency/MonoMAC syndrome, a condition that frequently progresses to MDS |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Completed | 120 | Busulfan, etoposide and cyclophosphamide conditioning for MDS/MPD patients aged 51–60 |
| [NCT01622556](https://clinicaltrials.gov/study/NCT01622556) | Phase 2 | Terminated | 6 | Reduced-intensity busulfan/TBI/thymoglobulin conditioning with cord blood transplant; small, terminated, limited value |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (Phase 3) | The Lancet Haematology | Randomized non-inferiority trial: treosulfan vs. busulfan/fludarabine conditioning in older AML/MDS patients undergoing allo-HSCT |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (Phase 3) | J Clin Oncol | Randomized trial comparing myeloablative vs. reduced-intensity busulfan-based conditioning for AML/MDS |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (Phase 3) | The Lancet Haematology | Open-label multicenter randomized trial: G-CSF+decitabine+busulfan/cyclophosphamide vs. busulfan/cyclophosphamide alone to reduce relapse in MDS/secondary AML |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Cohort | American Journal of Hematology | Final analysis: treosulfan improves outcomes vs. reduced-intensity busulfan in older AML/MDS allo-HSCT patients |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic Review / Meta-analysis | Frontiers in Oncology | Long-term outcomes of treosulfan- vs. busulfan-based conditioning in MDS/AML before HSCT |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Cohort | Transplantation and Cellular Therapy | Propensity-matched retrospective comparison of treosulfan- vs. busulfan-based conditioning in MDS (n=138) |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | Contemporary review of allogeneic HSCT for MDS and myelofibrosis, covering conditioning strategy |
| [38176654](https://pubmed.ncbi.nlm.nih.gov/38176654/) | 2024 | Retrospective cohort | Transplantation and Cellular Therapy | Long-term complications after treosulfan- vs. busulfan-based conditioning in pediatric acute leukemia/MDS |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Cohort | Transplantation and Cellular Therapy | Myeloablative busulfan + fludarabine with in vivo T-cell depletion shown safe and effective for AML/MDS |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Propensity-matched cohort | Bone Marrow Transplantation | Fludarabine/busulfan vs. busulfan/cyclophosphamide myeloablative conditioning for MDS, nationwide Japanese registry |

---

## Finland Market Information

Busulfan currently holds **no marketing authorization records in the evidence pack for Finland** (market status: Not marketed; 0 authorizations on file). No product-level licensing data is available for evaluation.

---

## Cytotoxicity

Busulfan is a well-established cytotoxic alkylating agent used in high-dose myeloablative regimens; it qualifies as antineoplastic/cytotoxic based on drug class (alkylating agent) and its role in myeloablative chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent; myeloablative conditioning agent) |
| Myelosuppression Risk | High — myeloablation is the intended therapeutic effect; profound, prolonged pancytopenia is expected by design, particularly at HSCT-conditioning doses |
| Emetogenicity Classification | High (especially at high-dose IV conditioning regimens) |
| Monitoring Items | CBC with differential, hepatic function (veno-occlusive disease/sinusoidal obstruction syndrome risk), pulmonary function ("busulfan lung"/pulmonary fibrosis), seizure precautions at high dose, and therapeutic drug monitoring (busulfan plasma levels) where used for conditioning |
| Handling Protection | Cytotoxic drug handling precautions required (PPE, closed-system transfer devices per institutional cytotoxic handling protocols) |

One identified publication ([PMID 37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/)) specifically evaluates busulfan's association with secondary malignancy risk, relevant to long-term safety monitoring in non-malignant or curative-intent transplant settings.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in the evidence pack (DDI query returned no results), and this is flagged as a **Blocking** data gap (DG001) that must be resolved before any S1 safety assessment.

---

## Other Predicted Indications (Lower Priority)

This evidence pack also scored busulfan against 9 additional candidate indications, all ranked below MDS and mechanistically related to it as a broader hematologic-malignancy/bone-marrow-failure cluster, except two flagged as likely graph artifacts:

| Rank | Indication | Evidence Level | Recommendation |
|------|-----------|----------------|-----------------|
| 2 | Refractory cytopenia of childhood | L2 | Research Question |
| 3 | Unclassified myelodysplastic syndrome | L3 | Research Question |
| 4 | Partial deletion of chromosome 5q (5q- syndrome) | L5 | Hold |
| 5 | Aregenerative anemia (aplastic anemia) | L2 | Proceed with Guardrails |
| 6 | Severe congenital hypochromic anemia w/ ringed sideroblasts | L5 | Hold |
| 7 | HIV infectious disease | L3 | Research Question |
| 8 | Neurodevelopmental disorder (ataxic gait/absent speech) | L5 | Hold — likely graph noise |
| 9 | Seborrheic keratosis | L5 | Hold — likely false positive |
| 10 | Feline acquired immunodeficiency syndrome | L5 | Hold — non-human species, should be excluded from evaluation |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Myelodysplastic syndrome has the strongest evidence base of all predicted indications (L1: multiple completed Phase 3 RCTs directly comparing busulfan-based conditioning regimens in this population), and busulfan-based conditioning is already an established standard of care ahead of allo-HSCT for MDS. However, busulfan is currently unmarketed in Finland and critical safety documentation (TFDA/Fimea label warnings and contraindications) is missing, so guardrails are required before proceeding.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain official Finnish/EU package insert warnings and contraindications
- Resolve high-priority data gap DG002: confirm detailed mechanism of action from DrugBank or product label
- Confirm whether any Finland/EU marketing authorization exists for busulfan under any brand (e.g., Busilvex) despite the "not marketed" status shown here
- Establish a drug-drug interaction profile (current DDI query returned no data)
- Develop a monitoring and cytotoxic-handling protocol specific to conditioning-dose use in MDS transplant candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

