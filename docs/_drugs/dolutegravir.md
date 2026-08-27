---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Dolutegravir is an antiretroviral integrase strand transfer inhibitor established for treating HIV-1 infection. TxGNN predicts a strong association with **Simian Immunodeficiency Virus (SIV) Infection**, but the supporting evidence (1 clinical trial, 16 publications) is almost entirely preclinical macaque research rather than new human clinical evidence, since SIV is a non-human primate disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (established antiretroviral use; not confirmed via Taiwan license text — data gap DG001/DG002) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on established pharmacological knowledge, dolutegravir is an integrase strand transfer inhibitor (INSTI); its efficacy against HIV-1 has been proven, and the same enzymatic target (retroviral integrase) is shared with SIV, which mechanistically explains the model's high confidence score.

SIV is the simian counterpart of HIV and is the standard non-human primate (NHP) model used to study HIV pathogenesis, latency, and antiretroviral drug resistance. Dolutegravir has already been extensively tested in SIV-infected macaques — not as a new indication under development, but as a research tool to characterize resistance mutations and treatment strategies that inform human HIV-1 care.

Because of this, the TxGNN prediction largely reflects an existing, well-documented research use of dolutegravir in animal models rather than a genuinely novel human therapeutic indication — SIV infection itself does not occur in humans and cannot be an approvable clinical indication. The same pattern appears in the model's next-ranked prediction (feline immunodeficiency-associated disease, rank 2), which is similarly an animal-model analog of HIV rather than a new human use case. A third prediction (a rare neurodevelopmental disorder, rank 3) had no supporting evidence at all and was already flagged for Hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Evaluates vedolizumab combined with antiretroviral therapy (ART) for virological remission in HIV-infected subjects; dolutegravir is not the primary study drug (likely part of background ART), so relevance to a specific SIV indication is limited. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Preclinical | J Virology | Dolutegravir monotherapy in SIV-infected macaques selects multiple resistance mutation patterns with variable virological outcomes. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Preclinical | J Virology | Characterizes INSTI drug-resistance profiles in SIVmac239, supporting SIV as a valid model for HIV integrase inhibitor research. |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Preclinical | Antimicrob Agents Chemother | Uses simian-tropic HIV to study integrase inhibitor drug resistance mechanisms. |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Preclinical | J Virology | HIV-1 integrase resistance mutations introduced into SIVmac239 alter susceptibility to INSTIs including dolutegravir. |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Preclinical | Antimicrob Agents Chemother | Evaluates bictegravir and cabotegravir activity against INSTI-resistant SIVmac239 and HIV-1, contextualizing dolutegravir cross-resistance. |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Review | FEBS Journal | Reviews HIV/SIV intasome crystal structures explaining INSTI (including dolutegravir) binding and resistance escape mechanisms. |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Preclinical | Pharmaceutics | Pharmacokinetic validation of long-term antiretroviral treatment (incl. dolutegravir) in SIV-infected non-human primates. |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Preclinical | Front Immunol | Assesses brain white-matter/free-water changes in rhesus macaques after initiating emtricitabine + tenofovir + dolutegravir treatment. |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Preclinical | Clin Infect Dis | Dolutegravir and raltegravir show proadipogenic/profibrotic effects and induce insulin resistance in human/simian adipose tissue models. |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical | AIDS Res Hum Retroviruses | Evaluates coformulated injectable combination ART regimens in SIV-infected rhesus macaques. |

## Finland/Taiwan Market Information

Currently not marketed in Taiwan — no authorization records available (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted "new indication" (SIV infection) is a non-human primate disease, not an approvable human indication — the underlying evidence is preclinical macaque resistance/PK research that already supports dolutegravir's known HIV-1 mechanism, not a novel human therapeutic opportunity. Combined with the complete absence of TFDA safety documentation (Blocking data gap), this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap
- Confirmed mechanism of action and original indication documentation via DrugBank API
- Re-evaluation of TxGNN predictions restricted to clinically meaningful human indications, since the top-ranked candidates (SIV, feline immunodeficiency-associated disease) are animal-disease analogs of dolutegravir's existing HIV-1 use rather than genuine repurposing targets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

