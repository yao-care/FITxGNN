---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 6
---

# Zidovudine
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

# Zidovudine: From HIV/AIDS Antiretroviral Therapy to Prevention of Congenital HIV Transmission

## One-Sentence Summary

Zidovudine (AZT) is the original nucleoside reverse transcriptase inhibitor (NRTI), long established for treating HIV-1 infection/AIDS. Of six indications TxGNN predicted in this evidence pack, **Congenital Human Immunodeficiency Virus** (perinatal / mother-to-child transmission prevention) is the only candidate with strong, credible support — **33 clinical trials** and **20 publications**, including the landmark ACTG 076/PACTG-derived prophylaxis regimens. This largely reflects zidovudine's already-established PMTCT role rather than a genuinely novel indication; the other five predictions in this batch (feline/simian AIDS animal models, a rare neurodevelopmental disorder, and an obsolete hyperlipidemia ontology term) lack credible human clinical relevance and are not recommended for further evaluation (see "Other Predicted Indications Screened" below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Finland licensing data (drug not marketed there); based on general pharmacological knowledge — HIV-1 infection / AIDS (adult antiretroviral therapy) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus (perinatal/mother-to-child transmission prevention) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this record. Based on well-established pharmacological knowledge, zidovudine is a thymidine nucleoside analogue reverse transcriptase inhibitor (NRTI): it is phosphorylated intracellularly to its active triphosphate form, which is incorporated into nascent viral DNA by HIV-1 reverse transcriptase, causing chain termination and blocking viral replication. Its efficacy in adult HIV-1 infection/AIDS has been established since 1987 (the first antiretroviral drug ever approved).

Mechanistically, the same reverse-transcriptase-blocking action applies directly to interrupting mother-to-child (in-utero, intrapartum, and early neonatal) transmission of HIV-1 — the virus and its reverse transcriptase are identical; only the patient population (pregnant women and neonates) differs. This is reflected in real regulatory history: the landmark ACTG 076/PACTG 076 trial established that zidovudine prophylaxis (given antepartum/intrapartum to the mother and for six weeks to the newborn) reduces perinatal HIV transmission by roughly two-thirds, becoming the founding evidence base for PMTCT programs worldwide.

Because this evidence pack's `original_indications` field is empty (a documented drug-level data gap, DG002), the model's "predicted new indication" substantially overlaps with zidovudine's already-recognized antiretroviral/PMTCT role rather than a true off-label repurposing opportunity. This should be read as a data-completeness artifact rather than a novel scientific hypothesis — the underlying clinical evidence is nonetheless strong.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00386230](https://clinicaltrials.gov/study/NCT00386230) | Phase 3 | Completed | 1,554 | Short-course ZDV regimen non-inferior to long ACTG-076-like regimen for reducing perinatal HIV transmission risk in Thailand |
| [NCT00000751](https://clinicaltrials.gov/study/NCT00000751) | Phase 3 | Completed | 1,600 | Evaluated HIVIG vs IVIG added to intrapartum/neonatal AZT for further reducing maternal-fetal HIV transmission |
| [NCT01061151](https://clinicaltrials.gov/study/NCT01061151) | Phase 3 | Completed | 3,747 | PROMISE study — optimal antiretroviral strategies (incl. AZT-based regimens) for antepartum, intrapartum, and postpartum/breastfeeding MTCT prevention |
| [NCT00164736](https://clinicaltrials.gov/study/NCT00164736) | Phase 3 | Completed | 2,369 | Maternal/infant antiretroviral interventions and nutritional supplementation during breastfeeding to prevent MTCT |
| [NCT00197587](https://clinicaltrials.gov/study/NCT00197587) | N/A | Completed | 1,200 | "Mashi" study — prevention of milk-borne HIV-1C transmission in Botswana |
| [NCT01511237](https://clinicaltrials.gov/study/NCT01511237) | Phase 3 | Completed | 379 | PHPT-5 — perinatal antiretroviral intensification for women with <8 weeks of prior HAART during pregnancy |
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | Completed | 377 | Compared antiretroviral course lengths for infants infected with HIV at birth, in a resource-poor setting |
| [NCT00001007](https://clinicaltrials.gov/study/NCT00001007) | Phase 1 | Completed | 18 | Safety and pharmacokinetics of IV and oral zidovudine in infants with perinatal HIV exposure (age 1 day–3 months) |
| [NCT03642704](https://clinicaltrials.gov/study/NCT03642704) | Phase 4 | Completed | 56 | Strategy evaluation of early HIV diagnosis plus reinforced preventive antiretroviral treatment at birth (Guinea) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7913986](https://pubmed.ncbi.nlm.nih.gov/7913986/) | 1994 | Guideline | MMWR Recomm Rep | US PHS Task Force recommendations for ZDV use to reduce perinatal HIV transmission, based on ACTG 076 results (~2/3 risk reduction) |
| [8879761](https://pubmed.ncbi.nlm.nih.gov/8879761/) | 1996 | Review | Clin Infect Dis | Progress report two years post-ACTG 076: real-world MTCT rates fell substantially when counseling and ZDV therapy were offered |
| [9240849](https://pubmed.ncbi.nlm.nih.gov/9240849/) | 1997 | Cohort | Acta Paediatr Suppl | Timing of perinatal HIV transmission and its implications for designing ZDV-based preventive/therapeutic interventions |
| [12197800](https://pubmed.ncbi.nlm.nih.gov/12197800/) | 2002 | Cohort | Arch Pediatr Adolesc Med | Population-level effectiveness of zidovudine prophylaxis on mother-to-infant HIV-1 transmission, before vs. after its introduction |
| [8419601](https://pubmed.ncbi.nlm.nih.gov/8419601/) | 1993 | Phase I trial | J Pediatr | Safety, tolerability, and pharmacokinetics of IV/oral zidovudine in 32 infants born to HIV-infected mothers |
| [28537936](https://pubmed.ncbi.nlm.nih.gov/28537936/) | 2017 | Cohort/registry | AIDS | Assessed association between zidovudine use in pregnancy and congenital malformations; evidence inconsistent for increased risk |
| [26687320](https://pubmed.ncbi.nlm.nih.gov/26687320/) | 2016 | Registry study | Eur J Obstet Gynecol Reprod Biol | Antiretroviral Pregnancy Registry data on prenatal ZDV exposure and risk of ventricular septal/congenital heart defects |
| [33541012](https://pubmed.ncbi.nlm.nih.gov/33541012/) | 2021 | Systematic review/meta-analysis | Epidemiol Health | Meta-analysis on whether antiretroviral therapy (incl. ZDV) during pregnancy causes congenital malformations |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/non-case study | Eur J Clin Pharmacol | European congenital anomaly registry analysis of antiretroviral drug exposure in pregnancy and malformation risk |
| [2126136](https://pubmed.ncbi.nlm.nih.gov/2126136/) | 1990 | Case report | Pediatr Infect Dis J | Early case report describing zidovudine treatment of an infant with congenital HIV infection |

---

## Finland Market Information

Zidovudine is **not currently marketed in Finland** — the regulatory query returned 0 valid marketing authorizations, so no product name, dosage form, or approved-indication text is available. Any repurposing pathway would require a new marketing authorization application (or import/named-patient route) before local use.

---

## Other Predicted Indications Screened

Five additional TxGNN predictions were reviewed in this evidence pack and are **not recommended for further evaluation**:

| Disease | Score | Evidence Level | Reason for Exclusion |
|---|---|---|---|
| Feline acquired immunodeficiency syndrome | 99.96% | L4 | Cross-species knowledge-graph artifact (feline FIV model); no human clinical relevance |
| Simian immunodeficiency virus infection | 99.96% | L4 | Primate disease model used as an HIV analogue in preclinical research; not a human indication |
| Neurodevelopmental disorder with ataxic gait, absent speech, decreased cortical white matter | 99.96% | L5 | No mechanistic link, no supporting trials or literature; likely embedding-similarity false positive |
| Obsolete familial combined hyperlipidemia | 99.62% | L5 | Ontology term marked "obsolete"; no known lipid-related mechanism, zero evidence |
| AIDS related complex | 99.19% | L1 | Same underlying finding as the reported indication above — reflects AZT's already-established antiretroviral role, not a novel candidate |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (TFDA/Fimea package insert query pending — flagged as a **Blocking** data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical evidence base for zidovudine in preventing congenital/perinatal HIV transmission is strong (L1: 33 trials including multiple large completed Phase 3 studies, plus 20 publications spanning efficacy and pregnancy-safety literature). However, this substantially overlaps with the drug's already-established antiretroviral/PMTCT use rather than representing a genuinely new indication, and two blocking data gaps prevent a full go decision: local (Finland) package-insert safety data and formal MOA documentation are both missing, and the drug is not currently marketed in Finland.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — **Blocking**, required for initial safety screening (S1)
- Formal DrugBank/regulatory-sourced mechanism of action documentation
- Clarification of true original approved indication(s), since `original_indications` is currently empty in source data
- Regulatory pathway assessment for Finland market entry (new MA application or import route), given 0 current licenses
- Confirmation that the "new indication" framing (PMTCT-specific) offers meaningful clinical/regulatory differentiation from AZT's existing antiretroviral use before committing further repurposing resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

