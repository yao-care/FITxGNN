---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tenofovir Disoproxil: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor whose established use — referenced within this evidence pack's own literature (the iPrEx study, PMID 20874040) — is HIV pre-exposure prophylaxis and treatment.
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, a disease of non-human primates rather than a human indication, supported by **2 clinical trials** and **20 publications**, most of which are macaque/animal-model studies.
> Given the non-human nature of the top prediction and multiple blocking data gaps, this candidate is **not currently actionable** for human repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication text on file for Finland; the drug's already-approved human use (HIV infection/PrEP) is inferred only from context within the supplied literature, not from `taiwan_regulatory` |
| Predicted New Indication | Simian Immunodeficiency Virus Infection *(non-human primate disease — not a human indication)* |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the context available in this evidence pack, tenofovir disoproxil is the oral prodrug of tenofovir (PMPA), a nucleotide analog reverse transcriptase inhibitor. Its supplied repurposing rationale notes that the only human RCT-grade literature in this pack (PMID 20874040, the iPrEx pre-exposure prophylaxis study) actually evaluates tenofovir's **already-approved** use in human HIV prevention — not a novel indication.

Mechanistically, tenofovir's antiretroviral activity against HIV reverse transcriptase is directly analogous to its activity against SIV reverse transcriptase in macaques, since SIV and HIV are closely related lentiviruses. This explains the very high TxGNN score. However, **SIV infection is a disease of non-human primates used as a laboratory model for HIV research — it is not a human diagnosis**, so this prediction does not represent a genuine new human indication; it reflects the model correctly clustering tenofovir with lentivirus-related disease labels in its knowledge graph, several of which happen to be animal disease ontology terms.

The pack's next three ranked candidates reinforce this pattern rather than offsetting it: rank 2 ("feline acquired immunodeficiency syndrome") is a veterinary disease in cats; rank 3 (a rare neurodevelopmental disorder) has zero supporting evidence and no plausible mechanistic link to an antiviral NRTI; and rank 4 ("obsolete familial combined hyperlipidemia") is flagged in its own disease label as an obsolete ontology term with only indirect, non-mechanistic literature support. All four received a "Hold" recommendation in the source scoring.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Studied HIV/SIV viral decay kinetics with raltegravir (an integrase inhibitor, not tenofovir); trial was withdrawn with zero enrollment. Low relevance (Grade C) — different drug, no actual SIV patients. |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Evaluated vedolizumab combined with antiretroviral therapy for HIV virologic remission in treatment-naïve human subjects; tenofovir was not the primary intervention, and the study population was human HIV, not SIV. Low relevance (Grade C). |

*Note: both trials were flagged as low relevance (Grade C) by the source evidence pack — neither directly tests tenofovir disoproxil against SIV infection.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT (human) | Pharmacotherapy | Reviews systemic HIV pre-exposure prophylaxis (PrEP) in humans — this is tenofovir's established use, not a novel SIV indication; disease-label mismatch noted in source rationale. |
| [14557287](https://pubmed.ncbi.nlm.nih.gov/14557287/) | 2003 | Review | Clinical Microbiology Reviews | Reviews clinical potential of acyclic nucleoside phosphonates (cidofovir, adefovir, tenofovir) against DNA viruses and retroviruses, including SIV models. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal study (macaque) | J Infect Dis | Oral tenofovir alafenamide + emtricitabine protected macaques from rectal SHIV infection (PrEP model). |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Animal study (macaque) | JCI Insight | Hypo-osmolar rectal tenofovir douche formulation prevented SHIV acquisition in macaques. |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal study (infant macaque) | J Acquir Immune Defic Syndr | Oral tenofovir DF and topical tenofovir GS-7340 protected infant macaques against repeated oral SIV challenge (pediatric transmission model). |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal study (macaque) | J Infect Dis | Tenofovir DF chemoprophylaxis gave partial protection against SHIV infection under multiple viral challenges. |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Animal study (macaque) | J Virol | Vaginal tenofovir gel provided durable protection against SHIV infection in macaques, correlated with tissue drug levels. |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study (macaque) | J Infect Dis | Emtricitabine/tenofovir DF prevented vaginal SHIV infection in macaques co-infected with Chlamydia and Trichomonas. |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal study (macaque) | J Infect Dis | Tenofovir alafenamide/elvitegravir vaginal inserts gave extended post-exposure protection against SHIV in macaques. |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study (macaque) | J Infect Dis | Emtricitabine/tenofovir DF prevented transmission of a tenofovir-resistant (K65R) SHIV strain in macaques. |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Natural history (African green monkey) | J Virol | Characterized SIVagm viral dynamics under tenofovir/emtricitabine treatment in a natural-host, non-progressor monkey species. |

*10 additional PMIDs in the source pack (e.g., 41959211, 14963139, 20497048) remain unclassified ("pending" study type) and were not prioritized here.*

---

## Finland Market Information

Not applicable — TENOFOVIR DISOPROXIL currently has **0 marketing authorizations** on file for Finland (`market_status: 未上市`). No product/dosage form/indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields in the evidence pack — key warnings, contraindications, and DDI query — are data gaps; TFDA/Fimea package insert warnings are flagged as a **Blocking**-severity gap (DG001) that must be resolved before any S1 safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (SIV infection) is a non-human primate disease model, not a human indication that can be pursued through a repurposing pathway; ranks 2–4 are similarly non-actionable (veterinary disease, obsolete ontology term, or zero evidence). All four candidates carry a source-assigned "Hold" recommendation.
- Two Blocking/High-severity data gaps remain open: TFDA/Fimea package insert warnings and contraindications (Blocking — blocks S1 safety review), and confirmed mechanism of action (High).

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/Fimea package insert warnings/contraindications) before any safety-stage review can begin
- Resolve DG002 (confirmed MOA via DrugBank) to properly assess mechanistic relevance
- Re-run TxGNN disease matching with a human-only disease ontology filter to exclude animal-model and obsolete disease labels from candidate ranking
- If a genuine human indication is desired, source additional predicted candidates beyond the current top 4, since none of them are currently viable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

