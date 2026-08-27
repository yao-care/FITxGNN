---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
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

# Tenofovir Alafenamide: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Tenofovir alafenamide (TAF) is a nucleotide reverse-transcriptase inhibitor prodrug whose established clinical role is HIV-1 treatment and pre-exposure prophylaxis (PrEP); no original-indication record exists in this evidence pack because the drug is **not marketed in Taiwan**. TxGNN's top scored prediction, **Simian Immunodeficiency Virus (SIV) infection**, is supported only by **1 tangentially relevant clinical trial** and **9 non-human-primate (NHP) preclinical publications** — no human efficacy data exist for this specific indication. Two other candidates in this pack (feline AIDS, and a rare neurodevelopmental disorder) carry zero supporting evidence and/or fall outside human-drug repurposing scope, so they are noted but not developed further below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Taiwan licenses on file); TAF is internationally established as an antiretroviral for HIV-1 infection/PrEP |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical/NHP challenge-model evidence only; no completed human RCT or observational study specific to this indication) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for TAF is not available in this evidence pack (flagged as data gap DG002). Based on known pharmacology, TAF is a prodrug that is intracellularly converted to tenofovir diphosphate, which inhibits retroviral reverse transcriptase — the same enzyme class targeted in HIV-1 treatment.

SIV is a lentivirus closely related to HIV-1 and infects non-human primates; because the two viruses share reverse-transcriptase biology, TAF's antiviral mechanism is plausible in the SIV/SHIV (simian-human immunodeficiency virus) macaque model. However, the supporting literature is almost entirely translational research designed to validate TAF as **PrEP/PEP for human HIV prevention** using SIV/SHIV-infected macaques as a surrogate model — it is not evidence that TAF treats SIV infection as a disease in its own right. SIV infection itself is a veterinary/research-model condition, not a human clinical indication, which limits the practical repurposing value of this prediction despite the high TxGNN similarity score.

For context, the other two TxGNN candidates in this pack are weaker still: feline acquired immunodeficiency syndrome is an explicitly veterinary indication outside the company's human-drug repurposing scope, and the rare neurodevelopmental disorder has no clinical, preclinical, or mechanistic support whatsoever (pure embedding-similarity prediction, L5).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Trial of vedolizumab + antiretroviral therapy aiming for virologic remission in HIV-infected subjects; TAF is only incidentally part of background ART, and the trial does not target SIV infection directly (relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical (SHIV remission, macaque) | Nature Communications | Oral emtricitabine/TAF plus long-acting cabotegravir/rilpivirine tested for SHIV remission in macaques |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical (NHP model) | J Infect Dis | TAF/elvitegravir vaginal inserts gave 93–100% protection against repeated SHIV vaginal exposure in macaques |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical (humanized mouse model) | Frontiers in Immunology | Dual-purpose humanized mouse model proposed for testing antiviral strategies against SIV and HIV |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Preclinical (implant device, NHP) | J Antimicrob Chemother | Biodegradable TAF-releasing implant evaluated for sustained vaginal HIV/SHIV protection in macaques |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Preclinical (macaque efficacy) | J Infect Dis | Oral TAF/emtricitabine or TAF alone tested against vaginal SHIV infection in macaques (PrEP model) |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Preclinical (methodology, macaque) | PLoS One | Protocol for daily oral ARV dosing in macaques to improve compliance in SIV/SHIV prevention studies |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical (macaque chemoprophylaxis) | J Infect Dis | Oral TAF/emtricitabine prevented rectal SHIV infection in macaques |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Preclinical (SHIV, macaque) | J Infect Dis | Oral PrEP reduced inflammation and CD4 loss in acute SHIV infection |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Preclinical (infant macaque) | J Acquir Immune Defic Syndr | Oral tenofovir DF and topical GS-7340 (TAF precursor) evaluated against oral SIV challenge in infant macaques |

---

## Taiwan Market Information

Currently no Taiwan marketing authorizations on file (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (No warnings, contraindications, or drug-interaction data were retrievable in this cycle — see data gap DG001, marked Blocking.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence for the top prediction (SIV infection) is preclinical NHP model data supporting TAF as **HIV prevention/PrEP in humans**, not evidence of efficacy for treating SIV infection as a standalone indication; SIV infection is itself an animal/research-model disease rather than a human clinical target. Combined with the absence of TFDA safety/label data (Blocking gap) and MOA data, this candidate set does not currently support progression.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap, required before any S1 safety review
- DrugBank-sourced mechanism-of-action data to properly assess mechanistic fit
- Re-evaluation of whether SIV infection should be reframed as a human indication (e.g., HIV-1 PrEP/treatment) rather than pursued literally, since the current disease label is not a viable human repurposing target
- If pursuing further, deprioritize the feline AIDS (veterinary, out of scope) and neurodevelopmental-disorder (L5, no evidence) candidates from this set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

