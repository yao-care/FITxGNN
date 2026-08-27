---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Monoclonal Gammopathy (Infection Prophylaxis)

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibiotic originally used to treat bacterial infections. Across 10 TxGNN-predicted indications screened in this evidence pack, most show no supporting clinical or literature evidence (Hold), but the model's prediction for **Monoclonal Gammopathy** — specifically as **infection prophylaxis in newly diagnosed multiple myeloma** — is backed by a completed Phase 3 RCT (TEAMM) and **20 supporting publications**, making it the strongest candidate in this batch.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibiotic); no Taiwan-specific approved indication text on file — drug is currently unmarketed in Taiwan |
| Predicted New Indication | Monoclonal Gammopathy (infection prophylaxis during myeloma treatment) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured DrugBank mechanism-of-action record is not available (data gap). Based on the pharmacology already referenced within this evidence pack's own repurposing rationale, Levofloxacin is a broad-spectrum **fluoroquinolone** that inhibits bacterial DNA gyrase and topoisomerase IV, giving it bactericidal activity against a wide range of gram-negative and gram-positive organisms.

Patients with monoclonal gammopathy (particularly newly diagnosed multiple myeloma) have profound humoral immunodeficiency from suppressed normal immunoglobulin production, compounded by chemotherapy-induced neutropenia. Roughly a quarter of newly diagnosed myeloma patients develop a serious infection within 3 months of diagnosis. Levofloxacin's role here is **infection prophylaxis during the vulnerable induction/transplant period**, not a disease-modifying therapy for the gammopathy itself — the TEAMM trial and subsequent literature support this as a supportive-care intervention rather than a treatment targeting the underlying plasma cell disorder.

This distinction matters for scoping: the mechanistic link is indirect (anti-infective support in an immunocompromised population) rather than a direct antibody/plasma-cell pathway effect, so any recommendation must be framed as "infection prophylaxis in monoclonal gammopathy patients," not "treatment of monoclonal gammopathy."

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no ClinicalTrials.gov or ICTRP records found in this evidence pack for this indication; the pivotal TEAMM trial is documented via literature/HTA report below rather than a registry entry).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT (Phase 3) | Lancet Oncology | TEAMM trial: levofloxacin prophylaxis in newly diagnosed myeloma reduced febrile episodes/infections vs placebo without significantly increasing C. difficile or resistant-organism carriage |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT (HTA monograph) | Health Technol Assess | Full technology assessment report of the TEAMM RCT, evaluating antibiotic prophylaxis to prevent infection in newly diagnosed symptomatic myeloma |
| [25212681](https://pubmed.ncbi.nlm.nih.gov/25212681/) | 2014 | RCT | Int J Hematol | Prophylactic oral levofloxacin reduced severe infections in myeloma patients on bortezomib-based regimens at high risk from lymphocytopenia |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | RCT/Comparative cohort | Biol Blood Marrow Transplant | Levofloxacin prophylaxis before vs after implementation reduced bloodstream infection and fever/neutropenia rates in autologous HSCT for myeloma |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Curr Hematol Malig Rep | Supportive care review in multiple myeloma covering infection prevention among other management domains |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort study | Transpl Infect Dis | Characterizes infectious complications after autologous HSCT in myeloma, comparing outcomes with/without levofloxacin prophylaxis |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Comparative cohort | Clin Transplant | Retrospective comparison of ciprofloxacin vs levofloxacin prophylaxis in autologous HSCT for myeloma; compared breakthrough infection rates |
| [32304873](https://pubmed.ncbi.nlm.nih.gov/32304873/) | 2020 | Retrospective review | Biol Blood Marrow Transplant | Reassesses fluoroquinolone prophylaxis value in autologous stem-cell transplantation, comparing myeloma (prophylaxis) vs lymphoma (no prophylaxis) cohorts |
| [15791505](https://pubmed.ncbi.nlm.nih.gov/15791505/) | 2005 | Cohort study | Clin Infect Dis | Foundational study showing fluoroquinolone prophylaxis reduces infection-related mortality in neutropenic patients with hematologic malignancies |
| [25591868](https://pubmed.ncbi.nlm.nih.gov/25591868/) | 2016 | Case report (safety) | J Oncol Pharm Pract | Reports acute kidney injury from crystal nephropathy in a myeloma patient on concurrent pomalidomide and levofloxacin — relevant safety signal for this population |

---

## Taiwan Market Information

Levofloxacin currently holds **no marketing authorization in Taiwan** (0 licenses on file, market status: 未上市). No product/dosage-form data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured key-warning, contraindication, or drug-interaction data is currently available in this evidence pack — the Taiwan package insert has not yet been retrieved.)

---

## Other Predicted Indications Screened (This Batch)

For transparency, this evidence pack screened 10 TxGNN-predicted indications for levofloxacin. Only two reached an actionable evidence tier; the remaining eight had no clinical trial or literature support and are held.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|-----------------|-----------------|
| 1 | Punctate epithelial keratoconjunctivitis | 99.92% | L4 | Hold (sole literature source describes microsporidial, not bacterial, etiology — mechanistic mismatch) |
| 7 | **Monoclonal gammopathy** (featured above) | 99.81% | L1 | Proceed with Guardrails |
| 9 | Septicemic plague | 99.80% | L2 | Proceed with Guardrails — evidence from FDA Animal Rule primate/rodent efficacy studies; already an approved US indication for plague, though human RCTs are not ethically feasible |
| 5 | Blood group incompatibility | 99.85% | L4 | Hold (only literature is an incidental case report of infection during ABO-incompatible transplant workup, not a causal link) |
| 2 | Hyperamylasemia | 99.90% | L5 | Hold (no evidence) |
| 3 | Polyclonal hyperviscosity syndrome | 99.90% | L5 | Hold (no evidence) |
| 4 | Congenital analbuminemia | 99.89% | L5 | Hold (no mechanistic plausibility) |
| 6 | Premalignant hematological system disease | 99.83% | L5 | Hold (label too nonspecific) |
| 8 | Hematological disease with acquired peripheral neuropathy | 99.80% | L5 | Hold (fluoroquinolones carry a known peripheral neuropathy risk — direction contradicts the prediction) |
| 10 | Congenital hematological disorder | 99.72% | L5 | Hold (label too nonspecific) |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The monoclonal gammopathy prediction is supported by a completed Phase 3 RCT (TEAMM) plus multiple corroborating cohort studies, establishing levofloxacin's value as **infection prophylaxis during myeloma induction/transplant**, not as disease-modifying therapy. This is meaningfully stronger evidence than any other candidate in this batch, but the drug is currently unmarketed in Taiwan and a **Blocking** data gap (DG001: TFDA package insert unavailable) prevents even the initial S1 safety screen from being completed.

**To proceed, the following is needed:**
- Retrieve the Taiwan/TFDA package insert (DG001, Blocking) — required before any S1 safety assessment can proceed
- Obtain a structured DrugBank MOA record (DG002)
- Scope the indication precisely as "infection prophylaxis in monoclonal gammopathy patients undergoing chemotherapy/HSCT," not treatment of the gammopathy itself
- Evaluate the Taiwan registration/import pathway, since the drug currently has zero local marketing authorizations
- Track septicemic plague (L2, US Animal Rule precedent) as a secondary candidate in parallel, given its distinct regulatory pathway and biodefense relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

