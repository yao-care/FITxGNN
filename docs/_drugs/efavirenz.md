---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) whose established pharmacological class targets HIV-1 infection in humans. The TxGNN model predicts a possible application to **Simian Immunodeficiency Virus (SIV) Infection**, but the supporting evidence — 1 clinical trial (withdrawn, low relevance) and 16 publications — largely describes efavirenz being used as a research tool in an engineered SIV/HIV-1 chimeric virus model (RT-SHIV) rather than demonstrating native efficacy against wild-type SIV. Current evidence is preliminary and requires careful reinterpretation before advancing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented (efavirenz is not marketed in Finland; no license text available). Its established pharmacological class is NNRTI antiretroviral therapy for HIV-1 infection |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for efavirenz is not available in this evidence pack. Based on the information that is available (from the repurposing rationale), efavirenz is known to act as an NNRTI, binding a non-nucleoside pocket on the HIV-1 reverse transcriptase (RT) enzyme to block viral replication.

The predicted link to SIV infection, however, needs careful interpretation. Wild-type SIV reverse transcriptase differs substantially from HIV-1 RT, and NNRTIs such as efavirenz are generally **not effective against native SIV**. The clinical and preclinical evidence collected here almost entirely concerns "RT-SHIV" — a laboratory-engineered chimeric virus in which SIV's own RT gene has been replaced with HIV-1's RT gene, specifically so that researchers can study HIV-1 NNRTI drugs (including efavirenz) and resistance dynamics in a nonhuman-primate (macaque) model. In other words, this evidence supports **"efavirenz used as a tool to study an engineered HIV-1-RT-carrying virus in animals,"** not **"efavirenz has native antiviral activity against SIV."** This distinction is central to interpreting the TxGNN score and should not be conflated with a genuine new indication.

For context, TxGNN also flagged two additional low-confidence candidates for efavirenz in this run: feline acquired immunodeficiency syndrome (FIV; Evidence Level L5, based on an in vitro structural comparison study showing likely low cross-species affinity) and an ultra-rare genetic neurodevelopmental disorder (Evidence Level L5, no clinical or literature evidence at all). Both were scored "Hold" and are not carried further in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Studied HIV/SIV viral decay kinetics with the integrase inhibitor **raltegravir**, not efavirenz; trial was withdrawn with zero enrollment. Relevance graded "C" (low) — flagged as a likely search-mapping artifact rather than direct efavirenz evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal Study | Antimicrob Agents Chemother | First demonstration of efavirenz antiviral activity in rhesus macaques infected with RT-SHIV (SIV/HIV-1 RT chimera) |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal Study | J Virology | HAART regimen (efavirenz 200 mg + lamivudine + tenofovir) suppressed RT-SHIV viral load in rhesus macaques |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal Study | Retrovirology | Short-course efavirenz monotherapy followed by combination ART studied in RT-SHIV-infected pigtail macaques; tracked resistant subpopulation dynamics |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Preclinical/Virology | J Virology | Genetic diversity of RT-SHIV persists in macaques despite ART, including efavirenz monotherapy phases |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal Study | Antimicrob Agents Chemother | Enhanced 4–5 drug HAART regimens improved RT-SHIV viral decay kinetics in rhesus macaques |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Preclinical/Virology | J Virology | Characterized viral sanctuary sites during HAART in the RT-SHIV nonhuman primate AIDS model |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Preclinical/Virology | PLoS One | Viral decay kinetics characterized in HAART-treated RT-SHIV rhesus macaque AIDS model |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro | J Virology | In vitro characterization of the SIV-HIV RT-SHIV chimera developed to study NNRTI antiviral resistance in pigtail macaques |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Preclinical/Virology | J Virology | Ultrasensitive allele-specific PCR detected rare pre-existing drug-resistant RT-SHIV variants in macaques |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | In vitro/Imaging | Antimicrob Agents Chemother | Mass spectrometry imaging mapped distribution of 6 antiretrovirals (including efavirenz-class agents) relative to RT-SHIV RNA and fibrosis in macaque spleens |

*Note: All ten publications concern the RT-SHIV engineered chimeric virus model used for HIV-1 drug research in nonhuman primates, not native SIV disease.*

---

## Finland Market Information

Efavirenz is currently **not marketed in Finland** — no marketing authorizations are on record (`total_licenses: 0`), so no product/license table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial identified is irrelevant (wrong drug, withdrawn, zero enrollment), and the literature base — while numerous (10+ publications) — almost entirely describes efavirenz's use as a research reagent in an artificially engineered RT-SHIV virus rather than evidence of activity against native SIV. Combined with a **Blocking**-severity data gap on TFDA package insert/safety data (DG001), the candidate cannot yet advance to the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation via DrugBank (DG002)
- Clarification of whether "SIV infection" represents a genuine translatable indication or solely reflects RT-SHIV research-tool overlap with efavirenz's existing HIV-1 indication
- If veterinary application (FIV) is of interest, dedicated species-specific pharmacokinetic and RT-binding affinity data, given the current L5 evidence level and low predicted cross-species activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

