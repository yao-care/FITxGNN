---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From No Registered Indication (Not Marketed) to Skin Cancer (Basal Cell Carcinoma)

## One-Sentence Summary

Vismodegib (DrugBank DB08828) is currently **not marketed** in this jurisdiction and has no registered original indication on file. Among the 10 TxGNN-predicted indications in this evidence pack, the only one with substantive supporting data is **Skin Cancer (Basal Cell Carcinoma)**, backed by **23 clinical trials** and **20 publications**, and it corresponds to vismodegib's globally established use as the first-in-class oral Hedgehog-pathway inhibitor. The model's single highest-scoring candidate (medulloblastoma with extensive nodularity, 99.93%) shares the same mechanism but currently has zero retrievable trials or literature, so it is flagged separately below as an unvalidated research question rather than the primary subject of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorizations on file (untuk market: 未上市) |
| Predicted New Indication | Skin Cancer (Basal Cell Carcinoma) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, the formal DrugBank-sourced mechanism-of-action field is flagged as a data gap (DG002, High severity, pending DrugBank API query). Based on the literature evidence retrieved in this pack, however, vismodegib (GDC-0449) is well characterized as the first-in-class, orally bioavailable small-molecule antagonist of the Hedgehog (Hh) signaling pathway. It binds Smoothened (SMO), a seven-transmembrane receptor, blocking downstream activation of GLI transcription factors and suppressing pathway-driven proliferation (PMID 22679179, 22653209, 24756807).

The mechanistic fit to skin cancer is direct rather than inferred: basal cell carcinoma is primarily driven by aberrant Hedgehog signaling, and genomic profiling shows roughly 85% of BCCs carry activating mutations in this pathway (PTCH1 ~73%, SMO ~20%, SUFU ~8%; PMID 26950094). Vismodegib was in fact the first Hedgehog-pathway inhibitor approved (FDA, 2012) specifically for locally advanced and metastatic BCC, and it remains referenced across current European and US treatment guidelines (PMID 37604067, 31288208, 29331385). In this evidence pack, "skin cancer" is therefore best understood not as a novel repurposing hypothesis but as a re-confirmation of vismodegib's canonical, mechanistically validated indication in a market where the product is not yet registered.

Separately, the model's top-ranked candidate overall, medulloblastoma with extensive nodularity (TxGNN score 99.93%), reflects the same SMO/Hedgehog mechanism (SHH-activated molecular subgroup of medulloblastoma) and is biologically plausible, but no clinical trials or literature were retrieved for it in this data pull — it is scored L5/S0 ("Research Question") and requires a dedicated literature search on vismodegib in pediatric/recurrent SHH-medulloblastoma before it can be evaluated further.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01367665](https://clinicaltrials.gov/study/NCT01367665) | Phase 2 | Completed | 1232 | STEVIE study — large single-arm, open-label safety/efficacy trial of vismodegib 150 mg/day in locally advanced/metastatic BCC; primary supportive safety dataset behind approval |
| [NCT00607724](https://clinicaltrials.gov/study/NCT00607724) | Phase 1 | Completed | 68 | First-in-human study of GDC-0449 (vismodegib) in refractory advanced/metastatic solid tumors; established dose and safety basis |
| [NCT01815840](https://clinicaltrials.gov/study/NCT01815840) | Phase 2 | Completed | 229 | Randomized, double-blind comparison of two vismodegib dosing regimens (intermittent vs. induction+intermittent) in multiple BCC |
| [NCT01835626](https://clinicaltrials.gov/study/NCT01835626) | Phase 2 | Completed | 24 | Vismodegib combined with radiation therapy in locally advanced head/neck BCC |
| [NCT03035188](https://clinicaltrials.gov/study/NCT03035188) | Phase 2 | Completed | 40 | Neoadjuvant vismodegib in large/recurrent resectable BCC, aimed at scar/tissue-sparing surgery |
| [NCT01631331](https://clinicaltrials.gov/study/NCT01631331) | Early Phase 1 | Completed | 15 | Pilot study of vismodegib as pre-surgical adjuvant in sporadic BCC |
| [NCT01543581](https://clinicaltrials.gov/study/NCT01543581) | Phase 2 | Completed | 3 | Placebo-controlled, double-blind trial of vismodegib prior to Mohs micrographic surgery |
| [NCT06357988](https://clinicaltrials.gov/study/NCT06357988) | Phase 2 | Active, not recruiting | 35 | NCI-MATCH subprotocol T — vismodegib in non-BCC tumors with SMO/PTCH1 mutations (basket trial, mechanism-extension use) |
| [NCT05651828](https://clinicaltrials.gov/study/NCT05651828) | Early Phase 1 | Recruiting | 34 | Adaptive/personalized intermittent dosing schedules vs. fixed regimens in advanced BCC |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A (registry) | Recruiting | 80 | Netherlands prospective registration study comparing vismodegib and sonidegib in advanced/multiple BCC |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Review/Guideline | European Journal of Cancer | Updated European consensus guideline (EADO/ESTRO) on BCC diagnosis and treatment, including Hedgehog inhibitor use |
| [34000246](https://pubmed.ncbi.nlm.nih.gov/34000246/) | 2021 | RCT/Cohort | Lancet Oncology | Phase 2 trial of cemiplimab after Hedgehog-inhibitor (incl. vismodegib) failure in locally advanced BCC |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Review/Guideline | European Journal of Cancer | European consensus-based interdisciplinary BCC treatment guidelines |
| [29331385](https://pubmed.ncbi.nlm.nih.gov/29331385/) | 2018 | Review/Guideline | J Am Acad Dermatol | AAD guidelines of care for BCC management |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Review | Int J Mol Sci | Comprehensive review of BCC biology and molecular features |
| [26950094](https://pubmed.ncbi.nlm.nih.gov/26950094/) | 2016 | Cohort/Genomic | Nature Genetics | Genomic profiling of 293 BCCs: 85% carry Hedgehog pathway mutations (PTCH1/SMO/SUFU) |
| [27436804](https://pubmed.ncbi.nlm.nih.gov/27436804/) | 2016 | Review | Actas Dermo-Sifiliográficas | Review of resistance mechanisms to nonsurgical BCC treatments including vismodegib |
| [24756807](https://pubmed.ncbi.nlm.nih.gov/24756807/) | 2014 | Review | Recent Results Cancer Res | MOA review: vismodegib binds SMO, inhibits aberrant Hh pathway activation; notes relevance beyond BCC (medulloblastoma, GI, brain, lung, breast, prostate) |
| [22679179](https://pubmed.ncbi.nlm.nih.gov/22679179/) | 2012 | Review | Clin Cancer Res | Approval-era review of vismodegib pharmacology and Phase 2 basis for FDA approval |
| [22653209](https://pubmed.ncbi.nlm.nih.gov/22653209/) | 2012 | Review | Nature Reviews Drug Discovery | Drug profile at initial FDA approval, MOA and development summary |

---

## Finland Market Information

Vismodegib currently has no marketing authorizations on file in this market (market status: 未上市 / Not Marketed; 0 licenses recorded).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / Smoothened inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vismodegib's mechanistic and clinical link to skin cancer (BCC) is well established internationally (large Phase 2 safety cohort of 1,232 patients, multiple completed trials, and current treatment guidelines), but the drug has no registration or marketing history in this jurisdiction, so local regulatory and safety data must be established before advancing.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking) — required before any S1 safety assessment can proceed
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Local drug-drug interaction (DDI) data — current query returned no results
- Formal regulatory pathway assessment given zero current market authorizations
- Independent literature/trial search for the top-ranked but currently unevidenced candidate (medulloblastoma with extensive nodularity) before it can be scored beyond L5/Research Question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

