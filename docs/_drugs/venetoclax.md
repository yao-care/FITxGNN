---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

# Venetoclax: From Hematologic Malignancy Standard-of-Care to Acute Myeloid Leukemia (Taiwan Repurposing Candidate)

## One-Sentence Summary

> Venetoclax (DB11581) is a selective BCL-2 inhibitor already used internationally across several B-cell and myeloid malignancies, but it is **not currently marketed in Taiwan** (0 authorizations on file).
> Among the 10 candidate indications TxGNN surfaced for this drug, **Acute Myeloid Leukemia (myeloid leukemia)** stands out as the only one backed by a genuinely mature evidence base — **50+ clinical trials** and **20 publications**, including combination regimens already treated as standard of care internationally — while most of the other 9 candidates are thin, mislabeled, or purely score-driven.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — venetoclax is not yet marketed in Taiwan, so no locally approved indication text exists |
| Predicted New Indication (headline) | Myeloid Leukemia (Acute Myeloid Leukemia) |
| TxGNN Prediction Score | 99.47% (global model rank 5,697) |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (regulatory/safety gate) — see rationale below |

**Note on scope:** this evidence pack is a multi-indication candidate bundle (`TW-DB11581-multi`) containing 10 ranked predictions. The single highest-scoring prediction by raw TxGNN rank (a specific pre-germinal-center CLL/SLL subtype) has almost no supporting evidence, so this report leads with the candidate that has the strongest, most decision-relevant evidence instead of the raw #1 score. All 10 are summarized below for completeness.

### Overview of All Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|--------------|-----------------|-----------------|-----------------|
| 1 | Pregerminal center CLL/SLL | 99.55% | L4 | S1 | Research Question |
| 2 | CLL/SLL (IGHV-mutated subtype) | 99.55% | L5 | S0 | Hold |
| 3 | Hodgkin lymphoma ⚠ | 99.51% | L3 | S1 | Research Question |
| 4 | **Myeloid leukemia (AML)** | 99.47% | **L1** | **S3** | **Proceed with Guardrails** |
| 5 | Chronic myelogenous leukemia (CML), BCR-ABL1+ | 99.36% | L2 | S2 | Research Question |
| 6 | Ewing sarcoma | 99.21% | L4 | S0 | Hold |
| 7 | Follicular lymphoma | 99.15% | L2 | S2 | Research Question |
| 8 | Metastatic neoplasm (generic) | 99.14% | L3 | S0 | Hold |
| 9 | Malignant spiradenoma | 99.12% | L5 | S0 | Hold |
| 10 | AML with t(8;21) translocation | 99.08% | L4 | S1 | Research Question |

⚠ **Data quality flag (Rank 3, Hodgkin lymphoma):** the 50 attached trials and 20 publications are overwhelmingly CLL, DLBCL, mantle cell lymphoma, and follicular lymphoma studies — **not one title explicitly references classic Hodgkin lymphoma**. This strongly suggests a label/classification mismatch (a broad "B-cell lymphoma" evidence set was attached to the Hodgkin lymphoma node). This indication should not be advanced without manual re-verification of the underlying disease mapping.

---

## Why is This Prediction Reasonable?

The structured `original_moa` field for this bundle is empty (data gap), and no Taiwan-approved original indication text exists because the drug is not yet marketed locally. However, the mechanism is consistently documented across the evidence pack's own rationale fields: venetoclax is a **selective, orally available BCL-2 (B-cell lymphoma-2) inhibitor** that restores the intrinsic apoptotic pathway in cells that have become abnormally dependent on BCL-2 for survival.

This mechanism directly explains the strength of the AML signal: leukemic blasts and leukemic stem cells frequently rely on BCL-2-mediated apoptosis evasion, and venetoclax combined with hypomethylating agents (azacitidine/decitabine) or low-dose cytarabine has become a well-established regimen for patients — particularly older or unfit patients — with newly diagnosed or relapsed/refractory AML. Unlike most of the other 9 candidates in this pack, the AML prediction is supported by a deep, multi-decade trial and publication record spanning Phase 1 through Phase 3, including maintenance-therapy and post-transplant settings.

By contrast, several other candidates in this pack (CLL/SLL molecular subtypes, Ewing sarcoma, malignant spiradenoma) share the same underlying BCL-2 rationale in principle, but have no disease-specific trials or only preclinical/mechanistic literature — meaning the mechanistic plausibility is real, but clinical validation is essentially absent.

---

## Clinical Trial Evidence (Myeloid Leukemia / AML)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06713837](https://clinicaltrials.gov/study/NCT06713837) | Phase 3 | Recruiting | 339 | IMPACT-AML: randomized pragmatic trial comparing high- vs low-intensity reinduction therapy in 1st/2nd relapse AML |
| [NCT03404193](https://clinicaltrials.gov/study/NCT03404193) | Phase 2 | Terminated | 235 | Venetoclax + 10-day decitabine in newly diagnosed elderly or R/R AML and high-risk MDS |
| [NCT03941964](https://clinicaltrials.gov/study/NCT03941964) | Phase 3 | Completed | 60 | Outpatient venetoclax + azacitidine/decitabine in treatment-naïve AML ineligible for intensive chemotherapy — reflects the regulatory standard-of-care regimen |
| [NCT04161885](https://clinicaltrials.gov/study/NCT04161885) | Phase 3 | Terminated | 465 | VIALE-T: venetoclax + azacitidine as post-allogeneic transplant maintenance to improve overall survival |
| [NCT05404906](https://clinicaltrials.gov/study/NCT05404906) | Phase 2/3 | Recruiting | 124 | Azacitidine + venetoclax maintenance in favorable-risk AML after first remission |
| [NCT02287233](https://clinicaltrials.gov/study/NCT02287233) | Phase 1/2 | Completed | 94 | Foundational study: venetoclax + low-dose cytarabine in treatment-naïve AML patients ≥60 years ineligible for anthracycline induction |
| [NCT07007312](https://clinicaltrials.gov/study/NCT07007312) | Phase 3 | Recruiting | 1,300 | Ziftomenib added to standard-of-care venetoclax+azacitidine (or intensive 7+3) in NPM1-mutated/KMT2A-rearranged AML |
| [NCT07469046](https://clinicaltrials.gov/study/NCT07469046) | Phase 3 | Not yet recruiting | 308 | Venetoclax+azacitidine+homoharringtonine vs venetoclax+azacitidine alone in elderly newly diagnosed AML |
| [NCT06611839](https://clinicaltrials.gov/study/NCT06611839) | Phase 1/2 | Recruiting | 29 | Venetoclax + ivosidenib + azacitidine triple regimen in IDH1-mutated AML |
| [NCT04146038](https://clinicaltrials.gov/study/NCT04146038) | Phase 2 | Completed | 5 | Salsalate added to venetoclax + decitabine/azacitidine in AML or advanced MDS/MPN |

*10 of 50+ available trials shown, prioritized by phase, sample size, and direct relevance to standard-of-care regimens.*

---

## Literature Evidence (Myeloid Leukemia / AML)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Review | Biomedicine & Pharmacotherapy | Overview of venetoclax's antileukemic activity in preclinical AML models and clinical trials, alone and in combination |
| [31203996](https://pubmed.ncbi.nlm.nih.gov/31203996/) | 2019 | Review | Best Practice & Research Clin Haematology | Venetoclax-based therapies contextualized among 8 new AML drugs approved since 2017 |
| [34329576](https://pubmed.ncbi.nlm.nih.gov/34329576/) | 2021 | Phase 2 cohort | The Lancet Haematology | Venetoclax + cladribine/idarubicin/cytarabine (CLIA) in newly diagnosed AML/high-risk MDS, patients ≤65 years |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Cohort | Clinical Cancer Research | Venetoclax + azacitidine efficacy/safety in treatment-naïve IDH1/2-mutant AML |
| [38866760](https://pubmed.ncbi.nlm.nih.gov/38866760/) | 2024 | Review | Cell Death & Disease | Venetoclax therapy and emerging resistance mechanisms in AML |
| [39303729](https://pubmed.ncbi.nlm.nih.gov/39303729/) | 2024 | Phase 2 cohort | The Lancet Haematology | Decitabine + venetoclax + ponatinib in advanced-phase Ph+ myeloid disease and Ph+ AML |
| [37599456](https://pubmed.ncbi.nlm.nih.gov/37599456/) | 2024 | Network meta-analysis | J Chemotherapy | Venetoclax+azacitidine vs ivosidenib/enasidenib in unfit newly diagnosed IDH1/2-mutant AML — favors venetoclax combination on OS |
| [34966123](https://pubmed.ncbi.nlm.nih.gov/34966123/) | 2022 | Review | Current Opinion in Hematology | Survey of venetoclax combination regimens in AML and MDS |
| [32031033](https://pubmed.ncbi.nlm.nih.gov/32031033/) | 2020 | Review | Leukemia & Lymphoma | Venetoclax + HMA/LDAC established as new standard of care for frontline unfit/elderly AML |
| [39246164](https://pubmed.ncbi.nlm.nih.gov/39246164/) | 2024 | Review | Expert Review of Hematology | Relapse and resistance patterns after frontline venetoclax-based AML therapy, and second-line strategies |

---

## Other Notable Predicted Indications (Secondary Candidates)

- **CML, BCR-ABL1 positive (Rank 5, L2, Research Question):** Multiple Phase 2 trials pair venetoclax with TKIs (dasatinib, ponatinib) to eradicate TKI-persistent leukemic stem cells — an active research line, not yet standard of care (e.g., [NCT02689440](https://clinicaltrials.gov/study/NCT02689440), [NCT04188405](https://clinicaltrials.gov/study/NCT04188405)).
- **Follicular lymphoma (Rank 7, L2, Research Question):** Directly aligned with the t(14;18) BCL-2 overexpression that defines FL. A dedicated Phase 2 (venetoclax+obinutuzumab+bendamustine, PrE0403, [PMID 40355425](https://pubmed.ncbi.nlm.nih.gov/40355425/)) reported in 2025, but efficacy has been inconsistent enough that FL is not yet a registered indication.
- **Ranks 1, 2, 6, 8, 9, 10 (Hold / low priority):** Either extremely narrow molecular subtypes with no dedicated trials, a generic multi-cancer label ("metastatic neoplasm") that mixes unrelated solid tumors, or (malignant spiradenoma) a rare tumor with zero supporting trials or literature. None should be advanced without new dedicated evidence.

---

## Taiwan Market Information

Venetoclax currently holds **0 marketing authorizations in Taiwan** (market status: 未上市 / not marketed). No product licenses, dosage forms, or approved indication text are available in this evidence pack.

---

## Cytotoxicity

Venetoclax is an antineoplastic agent (BCL-2 inhibitor used across CLL/SLL, AML, and other B-cell malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective BCL-2 inhibitor) — consistently identified as such across this evidence pack's rationale entries |
| Myelosuppression Risk | Not available in this evidence pack |
| Emetogenicity Classification | Not available in this evidence pack |
| Monitoring Items | Not available in this evidence pack |
| Handling Protection | Not available in this evidence pack |

Myelosuppression risk, emetogenicity, monitoring, and handling-protection details are not available in this evidence pack — please refer to the package insert warnings and precautions once the TFDA label (see Data Gap DG001 below) is obtained.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable in this evidence pack — DDI query status: not found.)

---

## Conclusion and Next Steps

**Decision: Hold** (regulatory/safety gate), with the underlying AML efficacy case otherwise meeting **Proceed with Guardrails** criteria.

**Rationale:**
- The myeloid leukemia (AML) indication has strong, mature clinical evidence (L1, 50+ trials, 20 publications) and reflects a therapy already treated as standard of care internationally.
- However, a **Blocking-severity data gap (DG001)** means TFDA package-insert warnings/contraindications have not yet been obtained, which by this pipeline's own criteria prevents completion of the S1 safety pre-assessment — so no advancement decision can be finalized until that gap is closed, regardless of efficacy strength.
- Venetoclax is not currently marketed in Taiwan (0 authorizations), so there is no local regulatory precedent to lean on; any repurposing pathway would likely require a full new registration route rather than a label-extension route.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — remediation: download and parse from the TFDA website (DG001, Blocking).
- Structured mechanism-of-action confirmation from DrugBank to replace the current data gap (DG002, High).
- Manual re-verification of the Hodgkin lymphoma (Rank 3) evidence set, which appears mismatched to the disease label.
- A formal DDI query, since the current query returned "not_found" rather than a populated result.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

