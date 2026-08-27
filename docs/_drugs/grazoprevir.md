---
layout: default
title: Grazoprevir
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Grazoprevir
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

# Grazoprevir: From Chronic Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Grazoprevir is an HCV NS3/4A protease inhibitor, marketed as a component of the elbasvir/grazoprevir combination (Zepatier) for chronic hepatitis C genotype 1/4/6.
The TxGNN model predicts it may be effective for **HIV infectious disease**, with **14 clinical trials** and **20 publications** nominally linked to this pairing —
however, on inspection, all of this evidence treats **hepatitis C** in HIV/HCV co-infected patients rather than HIV itself, so the mechanistic basis for this prediction is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus (HCV) genotype 1, 4, 6 infection (as elbasvir/grazoprevir combination) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% (rank 3470) |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for grazoprevir is not available (Data Gap). Based on known information from the linked literature, grazoprevir is the NS3/4A protease-inhibitor component of the elbasvir/grazoprevir fixed-dose combination (Zepatier), and its efficacy against chronic HCV genotype 1, 4, and 6 infection is well established through multiple Phase 2/3 trials.

The predicted link to HIV infectious disease is mechanistically implausible. Grazoprevir's target — the HCV NS3/4A serine protease — has no structural or functional homology to the enzymes HIV depends on for replication (HIV protease, reverse transcriptase, integrase), and none of the 14 linked trials or 20 publications report any direct antiviral activity against HIV.

Nearly all the supporting evidence instead comes from studies of **HCV treatment in HIV/HCV co-infected populations** (e.g., the pivotal C-EDGE CO-INFECTION and C-WORTHY trials), where the efficacy endpoint is HCV sustained virologic response (SVR), not HIV viral suppression or any HIV-related clinical outcome. The most plausible explanation is that TxGNN's knowledge graph picked up a strong "HCV–HIV co-infection" co-occurrence signal and mistook it for a therapeutic signal against HIV itself. Several trials in the evidence set are explicitly graded "C" (contradictory/tangential) for this reason.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Completed | 218 | GZR 100mg + EBR 50mg in HCV GT1/4/6 co-infected with HIV; primary endpoint SVR12 for **HCV**, not HIV |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Completed | 159 | GZR+EBR in HCV GT1/4/6 with inherited blood disorders, with/without HIV co-infection; HCV SVR endpoint |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Completed | 150 | Treat-counsel-cure strategy for HCV in HIV-positive MSM (Swiss HCVree Trial); validates an HCV care pathway, not HIV efficacy |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | GZR+EBR for acute HCV genotype 1/4 in HIV-positive patients (DAHHS-2, Dutch cohort); HCV cure endpoint |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication, comparing HIV/HCV co-infected vs HIV mono-infected controls |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Completed | 40 | GZR+EBR efficacy/tolerability in PWID and MSM with genotype 1 HCV and HIV co-infection; HCV endpoint |
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Unknown | 62 | 8 vs 12 weeks GZR/EBR for early chronic HCV GT1/4 in HIV co-infected patients; HCV SVR and tolerability |
| [NCT03037151](https://clinicaltrials.gov/study/NCT03037151) | Phase 4 | Unknown | 100 | Safety and fibrosis improvement with GZR+EBR in compensated cirrhotic HCV GT1/6 patients with/without HIV |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Unknown | 1000 | Real-life efficacy/tolerability of DAA-based regimens (incl. GZR) in HIV/HCV co-infected patients (HEPAVIR cohort); HCV endpoint |
| [NCT03407703](https://clinicaltrials.gov/study/NCT03407703) | N/A | Unknown | 50 | Impact of 12 weeks EBR+GZR (Zepatier) on kidney function in HCV GT1/4 patients with/without HIV |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | Open-label trial (C-EDGE CO-INFECTION) | The Lancet HIV | Non-randomised trial of grazoprevir+elbasvir in HCV/HIV co-infected patients; assessed HCV efficacy, safety and tolerability — endpoint is HCV SVR, not an HIV outcome |
| [25467560](https://pubmed.ncbi.nlm.nih.gov/25467560/) | 2015 | RCT, Phase 2 (C-WORTHY) | The Lancet | 8 vs 12 weeks grazoprevir+elbasvir ± ribavirin in HCV GT1 mono-infected and HIV/HCV co-infected patients; HCV SVR endpoint |
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Systematic review / Network meta-analysis | J Gastroenterol Hepatol | Compares efficacy/safety of DAA regimens (incl. grazoprevir/elbasvir) for HCV/HIV co-infection; outcome is HCV cure, not HIV suppression |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | PK/DDI study | Antimicrob Agents Chemother | Pharmacokinetic interactions between elbasvir/grazoprevir and HIV protease inhibitors (ritonavir, atazanavir, lopinavir, darunavir) |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | PK/DDI study | J Antimicrob Chemother | Drug interaction potential between elbasvir/grazoprevir and HIV integrase inhibitors (raltegravir, dolutegravir) |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Review | Expert Opin Drug Metab Toxicol | Drug-drug interactions between DAAs and antiretrovirals when treating hepatitis C in HIV-infected patients |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Review | Expert Rev Clin Pharmacol | Mechanism of action, PK/PD, clinical use, safety and efficacy of elbasvir/grazoprevir for chronic HCV GT1/4 |
| [26849059](https://pubmed.ncbi.nlm.nih.gov/26849059/) | 2016 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics and pharmacokinetics of elbasvir and grazoprevir in HCV treatment |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Review | Drugs | Review of elbasvir/grazoprevir fixed-dose combination for chronic HCV genotypes 1 and 4 |
| [28947524](https://pubmed.ncbi.nlm.nih.gov/28947524/) | 2017 | Review | Am J Health-Syst Pharm | Chemistry, pharmacology, PK/PD, efficacy, safety and dosing of elbasvir/grazoprevir for HCV |

## Finland Market Information

Grazoprevir currently has **no marketing authorization in Finland** (market status: 未上市 / Not Marketed; 0 authorizations on record). No product-level licensing data is available for this report.

## Safety Considerations

Please refer to the package insert for safety information. The TFDA/Fimea package insert data required to assess warnings and contraindications is currently unavailable (data gap DG001, marked Blocking), which prevents a full S1 safety evaluation for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted grazoprevir–HIV link lacks mechanistic plausibility (HCV NS3/4A protease inhibition has no known relevance to HIV replication), and all cited clinical and literature evidence measures HCV treatment outcomes in HIV/HCV co-infected populations rather than any direct anti-HIV effect. This pattern strongly suggests the TxGNN prediction reflects a knowledge-graph co-occurrence artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data to resolve the blocking safety data gap (DG001)
- Confirmed mechanism-of-action data for grazoprevir (DG002)
- In vitro or preclinical evidence of any direct anti-HIV activity, if this signal is to be pursued further
- Otherwise, this candidate should be deprioritized in favor of predicted indications with stronger mechanistic and evidentiary support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

