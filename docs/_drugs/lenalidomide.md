---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 6
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lenalidomide: From Multiple Myeloma / MDS with del(5q) to Myeloid Leukemia

## One-Sentence Summary

Lenalidomide is a thalidomide-derived immunomodulatory drug (IMiD), established in the treatment of multiple myeloma and transfusion-dependent myelodysplastic syndrome (MDS) with isolated del(5q).
The TxGNN model predicts it may also be effective for **Myeloid Leukemia** (AML/higher-risk MDS spectrum),
with **50 clinical trials** and **20 publications** currently retrieved in support of this direction, though evidence quality is mixed (many trials terminated or of unknown status).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma; MDS with del(5q) (based on well-established drug information — not captured in this evidence pack, see Data Gap DG002) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% (rank 5525) |
| Evidence Level | L2 (1 completed Phase 2 RCT identified; no completed Phase 3 RCT) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as Data Gap DG002, High severity). Based on well-established pharmacological knowledge, lenalidomide is a second-generation IMiD (immunomodulatory imide drug) derived from thalidomide. It acts via cereblon (CRBN)-mediated ubiquitination and degradation of the transcription factors IKZF1/IKZF3, producing direct cytotoxic/anti-proliferative effects on malignant clones as well as immune-stimulatory effects (enhanced T-cell and NK-cell activity). It is already established for multiple myeloma and for red-blood-cell-transfusion-dependent MDS associated with a del(5q) cytogenetic abnormality.

MDS and AML exist on a biological continuum — MDS is a pre-leukemic clonal stem-cell disorder that frequently transforms into AML, and higher-risk MDS/CMML/AML are often studied together in the same trial programs. This is reflected in the evidence pack: the majority of the 50 retrieved trials and several review articles (e.g. PMID 37288607, PMID 24656536) explicitly discuss MDS, AML and CMML as a shared disease spectrum, frequently using lenalidomide in combination with hypomethylating agents (azacitidine) or conventional chemotherapy (cytarabine, idarubicin, mitoxantrone).

Mechanistically, lenalidomide's anti-clonal and immune-potentiating activity in del(5q) MDS plausibly extends to broader myeloid malignancies, particularly AML/MDS carrying chromosome 5 abnormalities or monosomy 5, which is the most consistent efficacy signal across the retrieved trials. However, results in non-del(5q) AML/MDS populations are more heterogeneous, with numerous Phase 1/2 studies terminated early (frequently for toxicity, slow accrual, or lack of efficacy rather than confirmed benefit), and no completed randomized Phase 3 trial confirms efficacy specifically for "myeloid leukemia" as a standalone indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00843882](https://clinicaltrials.gov/study/NCT00843882) | Phase 3 | Active, not recruiting | 247 | Randomized trial of lenalidomide alone vs. + epoetin alfa for major erythroid response in low-/int-1-risk MDS with symptomatic anemia |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | Completed | 120 | Randomized, multicenter maintenance therapy alternating lenalidomide and azacitidine cycles in elderly AML patients in first CR |
| [NCT00065156](https://clinicaltrials.gov/study/NCT00065156) | Phase 2 | Completed | 148 | Pivotal single-arm trial of lenalidomide monotherapy in RBC-transfusion-dependent del(5q) MDS (basis of original regulatory approval) |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2/3 | Active, not recruiting | 282 | Randomized trial: azacitidine ± lenalidomide vs. azacitidine + vorinostat in higher-risk MDS/CMML |
| [NCT02472691](https://clinicaltrials.gov/study/NCT02472691) | Phase 2 | Completed | 50 | Lenalidomide added to azacitidine + donor lymphocyte infusion for MDS/CMML/AML relapse after allo-SCT |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML patients in remission |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Phase 2 | Completed | 48 | Lenalidomide safety/efficacy in untreated AML (≥60y) without 5q abnormalities |
| [NCT02538965](https://clinicaltrials.gov/study/NCT02538965) | Phase 2 | Completed | 17 | Lenalidomide activity/safety/PK in pediatric relapsed/refractory AML |
| [NCT02921802](https://clinicaltrials.gov/study/NCT02921802) | N/A (post-marketing surveillance) | Completed | 4,626 | Large all-case surveillance of Revlimid 5mg capsules real-world safety/efficacy |
| [NCT01016600](https://clinicaltrials.gov/study/NCT01016600) | Phase 1/2 | Completed | 31 | Azacitidine + lenalidomide toxicity and remission rate in AML |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30653424](https://pubmed.ncbi.nlm.nih.gov/30653424/) | 2019 | Prospective clinical trial (JCO) | J Clin Oncol | Combination lenalidomide + azacitidine as salvage therapy for AML/MDS relapse after allo-SCT |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic review & meta-analysis | Hematology (Amsterdam) | Efficacy and adverse events of azacitidine + lenalidomide across AML, MDS and CMML |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Prospective clinical trial (Azalena) | Haematologica | Azacitidine + lenalidomide + DLI for relapsed MDS/AML/CMML after allogeneic transplant |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | American Journal of Hematology | 2023 update on MDS diagnosis, risk-stratification and management |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making and treatment framework for MDS |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Overview of MDS pathophysiology, clinical course and progression to AML |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Review/Editorial | Leukemia | Rationale for combining azacitidine and lenalidomide in MDS/AML |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide as a novel treatment approach in AML |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib clinical trial | J Geriatr Oncol | Safety of lenalidomide as post-remission therapy in older AML patients |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Mechanism study | Cell Mol Biol Lett | KDM5C enhances AML sensitivity to lenalidomide by stabilizing cereblon (CRBN) |

## Taiwan Market Information

Lenalidomide currently has no marketing authorization record in this evidence pack — market status is "未上市" (not marketed) with 0 licenses on file. No authorization number, product name, dosage form, or approved indication text is available for tabulation.

## Cytotoxicity

Lenalidomide's original approved indications (multiple myeloma; MDS/leukemia-spectrum disorders) meet the antineoplastic criteria, so this section applies. Note: no DrugBank toxicity data or TFDA label data is present in this evidence pack (Data Gap DG001, Blocking; DG002, High) — the following reflects well-established pharmacological knowledge, not pack-sourced data, and must be confirmed against the actual package insert once obtained.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/immunomodulatory therapy (IMiD; cereblon-mediated — not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are well documented dose-limiting toxicities requiring dose modification |
| Emetogenicity Classification | Low (typical of IMiDs, in contrast to conventional cytotoxic chemotherapy) |
| Monitoring Items | CBC with differential (weekly during early cycles), renal function (dose adjustment required — renally cleared), VTE risk assessment, pregnancy testing given teratogenicity |
| Handling Protection | Yes — lenalidomide is teratogenic (thalidomide analog); handling and dispensing require controlled-distribution/REMS-equivalent safeguards in addition to standard cytotoxic handling precautions |

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data are available in this evidence pack — the TFDA package insert query (DG001) is flagged as a **Blocking** data gap that must be resolved before a safety initial evaluation (S1) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While TxGNN assigns a high prediction score (99.49%) and a substantial volume of supporting trials (50) and literature (20) exists, the trial evidence is heterogeneous — many studies are Phase 1, terminated, or of unknown status, and no completed randomized Phase 3 trial confirms efficacy specifically for myeloid leukemia. Critically, the safety data gap (DG001, Blocking) prevents completion of even the initial safety evaluation (S1), so a Go or Guardrails decision cannot be responsibly made at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — resolve Blocking gap DG001
- DrugBank/verified mechanism-of-action data — resolve High-severity gap DG002
- Confirmation of original approved indications and licensing status (original_indications field is currently empty)
- Manual review of trial relevance grading (most trials/literature are still marked "pending" relevance in the evidence pack) to distinguish del(5q)-specific signal from general AML/MDS use
- Drug interaction (DDI) data, currently unretrieved ("not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

