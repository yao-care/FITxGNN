---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

Using the txgnn-pipeline domain context (老藥新用 evidence-pack → report), I'll generate the report directly per the v5 prompt template. This is a content-authoring task with a fully-specified format already in the prompt — no additional skill invocation changes the output, so I'm proceeding straight to the report.

One important note before the report: this Evidence Pack bundles **three** TxGNN predictions for Emtricitabine, and none of them is a clean, validated new *human* indication — rank 1 (feline AIDS) and rank 3 (a rare genetic neurodevelopmental disorder) are species/ontology-mismatch artifacts explicitly flagged as such in the pack's own `repurposing_rationale`, and rank 2 (SIV infection) is preclinical evidence that actually underlies the *already-approved* Truvada PrEP indication rather than a novel signal. I built the primary report around rank 1 (as the template specifies using `predicted_indications[0]`), but added a clearly-labeled supplementary section covering ranks 2–3 so this context isn't lost — omitting it would be misleading given the "multi" nature of this candidate pack.

---

# Emtricitabine: From HIV-1 Infection Treatment to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Emtricitabine is a cytidine-analogue NRTI used clinically as a component of HIV-1 antiretroviral regimens (e.g., Truvada, Atripla), as evidenced throughout this pack's own clinical trial and literature records.
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)**, with **4 clinical trials** and **1 publication** retrieved —
> however, this signal is a **species/ontology mismatch** (a veterinary indication, not a human repurposing opportunity) and should not be actioned as-is.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Not populated in structured fields (`original_indications` and `original_moa` are data gaps)*. Based on clinical trial/literature text within this pack, Emtricitabine is used as a component of antiretroviral therapy for **HIV-1 infection** (e.g., Truvada, Atripla) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Emtricitabine is not available in this pack (`original_moa: [Data Gap]`). Based on information embedded in the clinical trial and literature records themselves, Emtricitabine is a cytidine nucleoside analogue reverse transcriptase inhibitor (NRTI) used as part of combination antiretroviral regimens (co-formulated with tenofovir ± other agents, e.g., Truvada, Atripla) for treatment and prevention of HIV-1 infection in humans.

The TxGNN model's rank-1 prediction — Feline Immunodeficiency Virus (FIV) infection — is mechanistically plausible at a very abstract level: FIV, like HIV, is a lentivirus that depends on reverse transcriptase for replication, so an RT inhibitor could in principle act on both. However, this is **not a valid human drug-repurposing signal**. FIV is a *veterinary* disease entity in cats, and pharmacokinetics, dosing, and toxicity profiles differ substantially between species. The pack's own `repurposing_rationale` explicitly states this "不屬於藥物再利用（human drug repurposing）範疇" (does not fall within the scope of human drug repurposing). The high TxGNN score here most likely reflects a knowledge-graph entity/embedding similarity between FIV and HIV nodes rather than a genuine new human therapeutic opportunity.

Because of this, the retrieved clinical trials below are all human HIV-1 trials that happen to reference Emtricitabine-containing regimens — they are **not evidence for the FIV indication itself**, and each has been graded "C" (low relevance / entity mismatch) by the source evidence pipeline.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + Abacavir/Lamivudine vs. Atripla (Efavirenz/Emtricitabine/Tenofovir) in ART-naive HIV-1 adults. Human trial; **Grade C — species/entity mismatch with FIV** |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of Dolutegravir + Abacavir/Lamivudine or Tenofovir/Emtricitabine in ART-naive HIV-1 adults. **Grade C — mismatch** |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted Darunavir + Lamivudine vs. Darunavir + Emtricitabine/Tenofovir or Lamivudine/Tenofovir in naive HIV-1 patients. **Grade C — mismatch** |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. Raltegravir, both with dual NRTI backbone (incl. Emtricitabine/Tenofovir), in ART-naive HIV-1 adults. **Grade C — mismatch** |

*All four trials are human HIV-1 studies; none evaluate the FIV/feline indication directly.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal Cohort/Review (Tier 3) | Viruses | Combination antiretroviral therapy (Dolutegravir + Tenofovir + Emtricitabine) evaluated for pharmacokinetics and clinical outcomes in FIV-infected domestic cats; no definitive therapy currently exists for FIV. |

---

## Finland Market Information

No marketing authorization records are present for Emtricitabine in this evidence pack (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`). There is currently no Finnish product/licence data to summarize.

---

## Additional Predicted Signals in This Evidence Pack (Supplementary)

This candidate bundle (`TW-DB00879-multi`) contains two further TxGNN predictions worth surfacing for completeness, since they materially change the interpretation of the overall candidate:

### Rank 2 — Simian Immunodeficiency Virus (SIV) Infection
TxGNN score 99.92% (rank 1108) · Evidence Level **L2** · Recommendation: **Research Question**

This is the strongest-evidence signal in the pack (2 clinical trials, 20 publications), but the rationale clarifies it is **not a novel indication** — it represents the non-human-primate (macaque) preclinical model data that historically supported Emtricitabine/Tenofovir's (Truvada) already-approved human PrEP indication, rather than a new therapeutic direction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | HIV decay-kinetics study (Raltegravir); referenced SIV decay comparisons in macaques. Grade C — withdrawn/species mismatch. |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + ART for HIV virological remission; human trial, not SIV. Grade C — mismatch. |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Review | Pharmacotherapy | Overview of systemic PrEP for HIV prevention. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Cohort (NHP preclinical) | J Infect Dis | Oral Emtricitabine + Tenofovir alafenamide protects macaques from rectal SHIV infection. |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Cohort (NHP preclinical) | J Infect Dis | Emtricitabine/Tenofovir DF prevents tenofovir-resistant (K65R) SHIV transmission in macaques. |
| [32128569](https://pubmed.ncbi.nlm.nih.gov/32128569/) | 2020 | Cohort (NHP preclinical) | J Infect Dis | Long-acting Cabotegravir vs. oral Emtricitabine/Tenofovir DF against penile SHIV exposure in macaques. |
| [19656878](https://pubmed.ncbi.nlm.nih.gov/19656878/) | 2009 | Cohort (NHP preclinical) | J Virol | Topical tenofovir ± Emtricitabine gel fully protects macaques from repeated vaginal SHIV exposure. |
| [21632769](https://pubmed.ncbi.nlm.nih.gov/21632769/) | 2011 | Cohort (NHP preclinical) | J Virol | Intermittent Truvada prophylaxis protects against emtricitabine-resistant (M184V) SHIV rectal transmission. |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Cohort (NHP preclinical) | J Infect Dis | Vaginal Emtricitabine/Tenofovir gel protects against repeated rectal SHIV exposure in macaques. |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Cohort (NHP preclinical) | J Infect Dis | Oral Tenofovir alafenamide/Emtricitabine vs. TAF alone against vaginal SHIV infection in macaques. |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Cohort (NHP preclinical) | AIDS Res Hum Retroviruses | HIV VLP vaccine + partial oral PrEP prevents SHIV infection and primes immunity in macaques. |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Cohort (NHP preclinical) | J Infect Dis | Emtricitabine/Tenofovir DF prevents vaginal SHIV in macaques co-infected with C. trachomatis/T. vaginalis. |

*(10 of 20 total publications shown, prioritized by relevance to Emtricitabine-specific PrEP efficacy; the remaining 10 are largely SIV pathogenesis/resistance mechanism studies with only peripheral drug relevance.)*

### Rank 3 — Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter
TxGNN score 99.92% (rank 1168) · Evidence Level **L5** · Recommendation: **Hold**

Currently no related clinical trials registered. Currently no related literature available. The pack's own rationale states there is no known biological link between an antiviral RT inhibitor and this genetic neurodevelopmental disorder's causal mechanism (neuronal migration/myelination gene defects) — this is most likely a knowledge-graph co-occurrence artifact rather than a real pharmacological signal.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All structured safety fields — key warnings, contraindications, and drug-drug interactions — are unpopulated data gaps in this pack; notably, `DG001` flags missing TFDA/regulatory package-insert warnings as a **Blocking** gap that must be resolved before any safety-stage (S1) evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the three TxGNN predictions in this pack constitutes a validated, actionable *new human* indication: the rank-1 signal (FIV) is a species-mismatched veterinary entity, the rank-2 signal (SIV) is preclinical evidence underlying an indication (PrEP) Emtricitabine-containing products already have, not a novel one, and the rank-3 signal has no clinical trials, no literature, and no plausible mechanistic link. Combined with a Blocking safety data gap (no TFDA/package-insert warnings or contraindications) and no Finland market presence, this candidate does not meet the bar to proceed past S0/S1.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): obtain TFDA package insert warnings/contraindications before any S1 safety evaluation
- Resolve **DG002** (High): confirm Emtricitabine's mechanism of action via DrugBank API query
- Clarify with the prediction pipeline whether species-mismatched disease entities (feline/simian) should be filtered from the human-indication candidate pool before ranking/scoring
- If a genuine new human indication is still sought for Emtricitabine, treat rank 2 (SIV) only as confirmatory background for the existing PrEP indication — not as a new candidate — and deprioritize ranks 1 and 3 as invalid signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

