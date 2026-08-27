---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab (anti-IgE monoclonal antibody) has established use in moderate-to-severe allergic asthma and chronic spontaneous urticaria, based on the trial and literature evidence contained in this pack (formal Finland licensing records show **0 authorizations** — a data gap, not a pharmacological fact, as the evidence itself notes). The TxGNN model predicts potential efficacy in **Bronchitis**, supported by **2 clinical trials** and **8 publications** — but evidence review shows these actually enrolled allergic-asthma / eosinophilic-bronchitis-with-asthma / CSU populations rather than classic bronchitis, pointing to a likely disease-label mismatch that warrants caution before acting on this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe allergic asthma / chronic spontaneous urticaria (per literature evidence in this pack; no Finland license record on file) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank/TFDA sources (Data Gap DG002). Based on information recurring throughout this pack's own trial and literature records, Omalizumab is a recombinant humanized monoclonal antibody that binds free IgE and blocks its interaction with the high-affinity IgE receptor (FcεRI) on mast cells, basophils, and dendritic cells, thereby reducing IgE-mediated allergic inflammation. Its efficacy in moderate-to-severe persistent allergic asthma and chronic spontaneous urticaria is repeatedly documented across trials cited in this pack (e.g., NCT00046748, n=484; NCT01202903, n=616), and mechanistically the drug is expected to be relevant to other IgE/type-2-inflammation-driven airway conditions.

The link to "Bronchitis" specifically is weaker than the TxGNN score (99.9992%) suggests. Both supporting trials are, on closer inspection, studies of adjacent but distinct populations: NCT02477332 is a Phase 2b dose-finding trial of QGE031 (a related anti-IgE biologic, not omalizumab) in Chronic Spontaneous Urticaria, not bronchitis; NCT02049294 is a small (n=11) steroid-sparing trial in patients with **asthma and eosinophilic bronchitis**, not classic infectious/chronic bronchitis. The pack's own repurposing rationale flags this directly: the trial populations represent "類緣疾病外推" (extrapolation from a related disease), and the IgE-mediated mechanism has no established direct support for typical (non-eosinophilic, non-atopic) bronchitis. This is most plausibly a TxGNN ontology-adjacency artifact (bronchitis sharing embedding space with asthma/airway inflammation terms) rather than a validated new indication.

Notably, rank 3 in this same evidence pack — "obstructive lung disease" (TxGNN score 99.97%, evidence level **L1**, decision stage **S3**, recommendation **Proceed with Guardrails**) — is a substantially stronger repurposing signal for the identical drug, backed by multiple completed Phase 3 RCTs (e.g., NCT00046748 n=484, NCT01202903 n=616) directly targeting allergic asthma, which is IgE's core validated indication. This may be a more actionable candidate than the rank-1 "Bronchitis" label reviewed here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Phase 2b dose-finding study of QGE031 (anti-IgE, related to omalizumab) as add-on therapy in Chronic Spontaneous Urticaria — not a bronchitis trial; included here as cross-disease extrapolation (Relevance Grade B). |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Double-blind, placebo-controlled trial testing whether add-on Omalizumab allows prednisone dose reduction in patients with asthma and eosinophilic bronchitis; very small sample, steroid-sparing endpoint rather than direct bronchitis efficacy (Relevance Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Safety study | Current medical research and opinion | Pooled safety analysis of omalizumab in children with IgE-mediated allergic asthma; not bronchitis-specific. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical reviews in allergy & immunology | Review of omalizumab's approval and postapproval experience in moderate-to-severe persistent asthma; demonstrates decreased airway inflammation via IgE/FcεRI reduction. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | Journal of investigational allergology & clinical immunology | Rare case of plastic bronchitis following bronchial thermoplasty; tangential to omalizumab efficacy. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | pending | Postepy dermatologii i alergologii | Omalizumab in older patients with severe allergic asthma–COPD overlap; suggests possible benefit in the ACO phenotype. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | pending | Expert opinion on pharmacotherapy | Discusses treatment challenges in smoking-induced airway disease (chronic bronchitis, emphysema, ACO) among asthma patients, noting these patients are typically excluded from trials. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | pending | Masui (Japanese journal of anesthesiology) | Japanese perioperative management guideline for bronchial asthma/chronic bronchitis; lists omalizumab as an option per JGL2012 for severe allergic asthma. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | pending | Revue des maladies respiratoires | French expert review on definitions and management of adult asthma exacerbations; general context, not bronchitis-specific. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | pending | Allergologia et immunopathologia | General review of monoclonal antibodies in pediatrics, including omalizumab for allergic disease. |

---

## Finland Market Information

Omalizumab currently has no marketing authorization on record in Finland (0 licenses; market status: 未上市/Not marketed). No product, dosage form, or approved-indication data is available from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 predicted indication ("Bronchitis") is not well supported by its own cited evidence — both trials actually studied allergic asthma/CSU or eosinophilic-bronchitis-with-asthma populations, with small samples and B/C relevance grades, consistent with a TxGNN disease-embedding adjacency artifact rather than a validated mechanistic link to classic bronchitis. Formal safety and Finland licensing data are also entirely absent (Blocking Data Gap DG001), so the candidate cannot pass an S1 safety screen even before efficacy is considered.

**To proceed, the following is needed:**
- TFDA/Finland package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed DrugBank mechanism of action data (DG002)
- Disease-ontology clarification on whether "Bronchitis" here specifically means eosinophilic bronchitis (a recognized asthma-overlap phenotype) vs. classic infectious/chronic bronchitis
- Dedicated trials or literature in a confirmed, non-atopic bronchitis population before advancing beyond Research Question stage
- For comparison: this same evidence pack shows "obstructive lung disease" (rank 3, evidence level L1, "Proceed with Guardrails") as a substantially better-supported repurposing candidate for this drug and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

