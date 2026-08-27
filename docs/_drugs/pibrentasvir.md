---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is an NS5A inhibitor marketed only as part of the glecaprevir/pibrentasvir combination (Maviret/Mavyret) for chronic Hepatitis C virus (HCV) infection. The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection**, with **14 clinical trials** and **20 publications** nominally attached to this candidate — but on inspection, every one of them studies HCV (or HCV co-infection), not HBV. This appears to be a label-confusion artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Finland regulatory data (drug not marketed); per known pharmacology, pibrentasvir is a component of glecaprevir/pibrentasvir, used for chronic Hepatitis C virus (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (as labeled by the evidence pack — see caveat below) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known information, pibrentasvir is part of the glecaprevir/pibrentasvir fixed-dose combination, an NS5A protein inhibitor that binds the highly variable region of HCV NS5A. Its established efficacy is specifically against chronic HCV infection (genotypes 1–6).

The prediction that this profile extends to Hepatitis B does **not** hold up mechanistically. HBV belongs to the Hepadnaviridae family and replicates via reverse transcription and a cccDNA reservoir — a completely different biology from HCV's NS5A-dependent replication complex. There is no known HBV homolog of the HCV NS5A binding site, and no preclinical or clinical data in this evidence pack shows anti-HBV activity for pibrentasvir.

Reviewing the underlying evidence confirms this: all 14 clinical trials and 20 publications linked to this candidate involve HCV (including HCV/HBV or HCV/HIV co-infected populations), with sustained virologic response to HCV (SVR12) as the endpoint — not HBV DNA suppression or HBsAg clearance. Only one publication (PMID 29485084) even mentions HBV, and it addresses HBV *vaccination* after HCV treatment — a co-management topic, not a drug-efficacy signal. This pattern is consistent with a TxGNN embedding-space artifact confusing "viral hepatitis" concepts (HCV vs. HBV) rather than a real pharmacological relationship. The evidence pack's own rationale field reaches the same conclusion.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Completed | 89 | Dose-ranging safety/antiviral activity of ABT-493+ABT-530 in genotype 1 chronic **HCV** — not HBV |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ABT-493/ABT-530 vs. sofosbuvir+daclatasvir in genotype 3 **HCV** (ENDURANCE-3) |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after **HCV** eradication in HIV/HCV co-infected patients |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | G/P efficacy/safety in Japanese adults with chronic **HCV** (CERTAIN-1) |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | G/P ± ribavirin in genotype 1 **HCV** patients previously treated with an NS5A inhibitor + sofosbuvir |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Completed | 100 | G/P in treatment-naïve Brazilian adults with **HCV** genotype 1–6 |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term follow-up of DAA resistance/durability of response in **HCV** patients |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | G/P ± ribavirin in **HCV** patients who failed prior DAA therapy |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | G/P ± ribavirin in **HCV** genotype 1, 4, 5, 6 (SURVEYOR-I) |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Completed | 304 | G/P vs. placebo in genotype 2 **HCV** (ENDURANCE-2) |

*None of the 14 registered trials for this candidate enroll HBV-infected patients or use an HBV endpoint.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | Real-world GLE/PIB effectiveness/safety in **HCV** patients with severe renal impairment (Taiwan) |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Cohort | Semin Liver Dis | Retreatment strategies for **HCV** patients who fail DAA therapy |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Cohort | World J Gastroenterol | Real-world DAA effectiveness in HIV/**HCV** genotype 6 co-infection |
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | Lancet Infect Dis | HBV vaccination strategy after completing **HCV** treatment — a co-management topic, not evidence of anti-HBV drug activity |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Review | Cancers | Hepatocellular carcinoma in chronic kidney disease; general liver-cancer epidemiology, not HBV-specific drug evidence |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Not classified | Lancet Gastroenterol Hepatol | Overview of **HCV** infection in children/adolescents |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Not classified | World J Gastroenterol | Pediatric viral hepatitis management (HBV and HCV); discusses available DAAs for HCV, not HBV activity of pibrentasvir |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Not classified | Eur J Gen Pract | Primary-care overview of chronic **HCV** diagnosis and treatment |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Not classified | AIDS Rev | Conference report covering global HBV and **HCV** burden and elimination roadmap; not a drug-efficacy study |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Not classified | Clin Pharmacokinet | Pharmacokinetic/pharmacodynamic update on **HCV** DAA regimens including glecaprevir/pibrentasvir |

*None of the 20 publications report pibrentasvir activity against HBV.*

## Safety Considerations

Please refer to the package insert for safety information (TFDA/Fimea warnings, contraindications, and drug-interaction data are not available in this evidence pack).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted HBV indication lacks any supporting mechanistic, preclinical, or clinical evidence — all 14 trials and 20 publications attached to this candidate concern HCV, not HBV, and the evidence pack's own rationale identifies this as a likely TxGNN label-confusion artifact between related "viral hepatitis" concepts rather than a real repurposing signal. Pibrentasvir is also not marketed in Finland, and core safety data (TFDA warnings/contraindications) is a Blocking-severity gap that independently prevents any S1 safety evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank to formally rule out (or in) any HBV-relevant activity
- TFDA/Fimea package insert (warnings, contraindications) to close the Blocking data gap
- If this candidate is retained for tracking, a dedicated PubMed/ClinicalTrials.gov search specifically filtered for HBV (not general "viral hepatitis") to confirm the absence of genuine evidence
- Given the consistent false-positive pattern across all 10 predicted indications for this drug (HBV, HIV, HEV, HAV, animal hepatitis, Omsk/Kyasanur fever, SIV, FIV, and an unrelated neurodevelopmental disorder), consider deprioritizing or excluding this drug-candidate pair from further repurposing review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

