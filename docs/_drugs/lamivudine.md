---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lamivudine: TxGNN Multi-Indication Screen — No Actionable Repurposing Candidate Identified

## One-Sentence Summary

Lamivudine (DB00709) is a well-established nucleoside reverse transcriptase inhibitor (NRTI) used against HIV-1 and chronic hepatitis B; the Evidence Pack does not record its original indication text due to a data gap. TxGNN returned **5 top-ranked predicted indications** (score ≈ 99.1–99.9%), but on evidence review **none qualify as an actionable human repurposing candidate** — the top signal is a veterinary disease (cats), the second is an animal-model-only condition (non-human primates), and the remaining three lack usable or correctly matched evidence. All five candidates carry a **Hold** recommendation.

---

## Quick Overview

*(Values below reflect the top-ranked candidate, predicted_indications[0]; see "All Predicted Indications" for the full set.)*

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license on file (`total_licenses = 0`); Lamivudine is widely known as an antiretroviral for HIV-1 infection and chronic hepatitis B, but this is general background, not Evidence Pack data |
| Predicted New Indication (Rank 1) | Feline acquired immunodeficiency syndrome (cat FIV) — **not a human indication** |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (per Evidence Pack scoring; literature is veterinary cohort/preclinical, not human) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

### All Predicted Indications (Ranked)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Issue |
|------|---------|------------|-----------------|-----------------|-----------|
| 1 | Feline acquired immunodeficiency syndrome | 99.93% | L4 | Hold | Veterinary disease (cats); attached clinical trials are human HIV/dolutegravir studies, unrelated to FIV (relevance grade C) |
| 2 | Simian immunodeficiency virus infection | 99.93% | L5 | Hold | Non-human primate model only; no clinical trials; 20 literature items are all animal/mechanistic studies |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, decreased cortical white matter | 99.93% | L5 | Hold | Zero clinical trials or literature; no known mechanistic link to an NRTI |
| 4 | Obsolete familial combined hyperlipidemia | 99.63% | L5 | Hold | Disease term flagged "obsolete" in ontology; no mechanistic rationale (antiretroviral vs. lipid metabolism); no evidence |
| 5 | Chronic hepatitis C virus infection | 99.11% | L4 | Hold | Likely ontology mislabel — all 16 attached trials and most literature concern chronic **hepatitis B**, not HCV; Lamivudine has no known activity against HCV's RNA-dependent RNA polymerase |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field: Data Gap). Based on known information, Lamivudine is a cytidine nucleoside analogue (NRTI) that, after intracellular phosphorylation, inhibits retroviral reverse transcriptase. Its efficacy against HIV-1 and hepatitis B virus (both of which depend on reverse transcription) is well established in humans.

For **Rank 1 (feline FIV)** and **Rank 2 (simian SIV)**, the mechanistic logic is genuine at the biology level — FIV and SIV are lentiviruses closely related to HIV, and reverse-transcriptase inhibition is a shared vulnerability (the M184V resistance mutation reported in SIV models mirrors the same mutation seen in HIV-1 under lamivudine therapy, per the literature evidence). However, these are **veterinary and non-human-primate disease models**, not human indications, so they do not constitute valid targets for a human drug-repurposing pipeline regardless of mechanistic plausibility.

For **Rank 5 (chronic HCV)**, the mechanistic rationale does *not* hold: HCV is a *Flaviviridae* RNA virus that replicates via the NS5B RNA-dependent RNA polymerase, not reverse transcription, so Lamivudine has no established antiviral activity against it. Critically, essentially all of the attached clinical trial and literature evidence for this candidate actually describes **chronic hepatitis B** (entecavir/adefovir/tenofovir/peginterferon vs. lamivudine trials), suggesting a disease-ontology labeling error in the underlying prediction rather than a genuine HCV signal. Ranks 3 and 4 have no supporting evidence of any kind and, in the case of Rank 4, reference an ontology term explicitly marked "obsolete."

---

## Clinical Trial Evidence

*(Drawn from predicted_indications[0] — feline FIV. All 5 trials are human HIV studies with dolutegravir/abacavir/lamivudine regimens and are graded "C" relevance — i.e., not actually about the predicted indication.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Dolutegravir + abacavir/lamivudine CNS/plasma PK study in ART-naive HIV-1 patients — human trial, unrelated to FIV |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla in ART-naive HIV-1 patients — human trial, unrelated to FIV |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dolutegravir dose-selection with abacavir/lamivudine or tenofovir/emtricitabine in HIV-1 patients — human trial, unrelated to FIV |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Darunavir + lamivudine vs. darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in HIV-1 patients — human trial, unrelated to FIV |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. raltegravir, both with dual NRTI backbone, in HIV-1 patients — human trial, unrelated to FIV |

**Note:** No clinical trials exist for Lamivudine in any of the 5 predicted indications as actually defined (FIV, SIV, the neurodevelopmental disorder, or obsolete hyperlipidemia). The 16 trials attached to Rank 5 (chronic HCV) are also mismatched — they are chronic hepatitis B trials — and are omitted here to avoid restating irrelevant data.

---

## Literature Evidence

*(Drawn from predicted_indications[0] — feline FIV; these are the only literature items directly on-topic for their stated indication.)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Cohort | Veterinary Immunology and Immunopathology | AZT/3TC combination showed additive-to-synergistic anti-FIV activity in primary PBMCs, but efficacy diminished in chronically infected cells |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohort | Journal of Feline Medicine and Surgery | Long-term antiretroviral therapy (AZT-based) evaluated in FIV-infected cats over 5–6 years |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohort | Viruses | ZDV+3TC vs. other regimens compared in naturally FIV-infected cats; viral load and CD4+/CD8+ ratios followed over one year |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Cohort | Antiviral Research | ZDV+3TC+ABC combination suppressed FIV replication in vitro; FIV proposed as an HIV animal model |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro/Preclinical | American Journal of Veterinary Research | Characterized 3TC-resistant FIV pol gene mutants in vitro |

**Note:** All 5 items are veterinary (feline) studies — none constitute human clinical evidence. Literature for Rank 2 (SIV, 20 items) and further items for Rank 5 (HCV/HBV mismatch, 20 items) exist in the Evidence Pack but are animal-model or wrong-disease studies and are not reproduced here to avoid misrepresenting them as support for a human indication.

---

## Taiwan Market Information

Lamivudine is currently **not marketed in Taiwan** (`market_status: 未上市`), with **0 authorizations** on file. No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this Evidence Pack — TFDA package insert retrieval is flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the 5 TxGNN-predicted indications is currently actionable for human drug repurposing: Rank 1 and Rank 2 are non-human disease models (feline FIV, simian SIV) with only animal evidence; Rank 3 and Rank 4 have no supporting evidence at all (Rank 4's disease term is even flagged as ontologically obsolete); and Rank 5 (chronic hepatitis C) is very likely a disease-ontology mismatch, since its clinical trial and literature evidence overwhelmingly concern chronic hepatitis B, a mechanistically plausible indication for an NRTI, rather than HCV.

**To proceed, the following is needed:**
- TFDA package insert retrieval (DG001, Blocking) to establish a baseline safety profile before any S1 evaluation
- DrugBank MOA/category data (DG002) to properly assess mechanistic plausibility
- Verification/correction of the disease-ontology mapping for Rank 5 — if the intended target is chronic hepatitis B rather than hepatitis C, that candidate should be re-scored and re-evaluated as a distinct, evidence-rich signal
- Re-scoping the predicted-indication set to exclude non-human disease terms (FIV, SIV) from the human repurposing pipeline at the model/filtering stage
- No further action recommended on Ranks 3 and 4 given the complete absence of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

