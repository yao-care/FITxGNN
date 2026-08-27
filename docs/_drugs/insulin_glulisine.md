---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine is a rapid-acting insulin analogue used broadly for glycemic control in diabetes mellitus. The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus**, with **50 clinical trials** and **19 publications** currently supporting this direction — however, this predicted "new" indication substantially overlaps with insulin glulisine's already-established clinical use, so it should be read as evidence-strength validation rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available regulatory data (Finland: not marketed, no license record); insulin glulisine is generally indicated for prandial glycemic control in diabetes mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glulisine is a rapid-acting human insulin analogue that binds the insulin receptor to directly restore insulin signaling and lower blood glucose — this is the core pharmacological action shared by all insulin products, not a novel mechanism being newly applied.

Because insulin replacement is the standard-of-care treatment for absolute insulin deficiency, and Type 1 Diabetes Mellitus is defined by autoimmune destruction of pancreatic beta cells leading to exactly that deficiency, the mechanistic link between the drug and the predicted indication is direct and expected rather than exploratory.

**Important caveat:** the evidence pack's own repurposing rationale flags this explicitly — insulin glulisine already carries labeled use in T1DM in most markets, so this candidate does not represent genuine "old drug, new use" repurposing. The very strong TxGNN score and large trial/literature base reflect the drug's well-established role in T1DM management, not a newly discovered therapeutic application. This candidate is best interpreted as a model-validation/positive-control case rather than a pipeline opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Phase 4 | Completed | 289 | Demonstrated superiority of insulin glulisine over aspart and lispro via CSII pump regarding unexplained hyperglycemia/infusion set occlusion in T1DM |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | Multinational comparison of glulisine (HMR1964) vs aspart via CSII pump; safety endpoints (occlusions, HbA1c, hypoglycemia) in T1DM |
| [NCT00115570](https://clinicaltrials.gov/study/NCT00115570) | Phase 3 | Completed | 572 | 26-week trial: glulisine as safe and effective as lispro in children/adolescents with T1DM |
| [NCT00545337](https://clinicaltrials.gov/study/NCT00545337) | Phase 3 | Completed | 60 | 26-week international trial evaluating glulisine + glargine efficacy (HbA1c) and safety in T1DM |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | 28-week non-inferiority trial: HMR1964 (glulisine) vs lispro in T1DM |
| [NCT00397553](https://clinicaltrials.gov/study/NCT00397553) | Phase 3 | Completed | 104 | Local efficacy/safety data for glulisine + glargine basal insulin therapy in T1DM |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Completed | 206 | Basal-bolus therapy (glargine + glulisine) in previously uncontrolled T1DM patients; HbA1c change at 24 weeks |
| [NCT00539448](https://clinicaltrises.gov/study/NCT00539448) | Phase 4 | Completed | 98 | Open-label multicenter study of glargine + glulisine efficacy and dosing in T1DM |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Efficacy, safety, and patient satisfaction of glulisine + glargine in T1DM |
| [NCT00925977](https://clinicaltrials.gov/study/NCT00925977) | N/A | Terminated | 44 | Crossover comparison of treatment satisfaction: glargine + glulisine vs NPH + glulisine in newly diagnosed pediatric T1DM (study terminated) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Multinational randomized parallel-group trial (n=683) comparing efficacy/safety of glulisine vs lispro in adults with T1DM |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Randomized 3-way crossover trial: glulisine vs aspart vs lispro via CSII in T1DM |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | 26-week pediatric trial showing comparable efficacy/safety of glulisine and lispro in basal-bolus regimens |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | RCT | Diabetes Obes Metab | Glulisine vs lispro efficacy/safety in Japanese T1DM patients using glargine as basal insulin |
| [41366610](https://pubmed.ncbi.nlm.nih.gov/41366610/) | 2026 | RCT | Diabetes Obes Metab | Phase III randomized trial: biosimilar insulin glulisine (T-Glu) vs originator (R-Glu) — immunogenicity, efficacy, safety in T1DM |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Cohort | Pediatr Int | 1-year CSII use of glulisine in 20 children with T1DM; significant improvement in post-meal glucose |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of insulin glulisine's role in diabetes management, including T1DM |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK/PD Study | Diabetes Care | Pharmacokinetics and prandial glucose control of glulisine vs regular human insulin in pediatric T1DM |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Review | Clin Pharmacokinet | Clinical pharmacokinetics/pharmacodynamics review of insulin glulisine |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Review | Drugs | Review of glulisine's glycemic control efficacy vs regular human insulin in T1DM/T2DM |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1: multiple completed Phase 3 RCTs directly studying insulin glulisine in T1DM), but the predicted indication substantially overlaps with the drug's already-established clinical use rather than representing a novel repurposing opportunity — guardrails are needed to confirm this is treated as a formal-registration/validation case, not a new therapeutic hypothesis.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings, contraindications, and drug interaction data (currently blocking safety pre-screening — DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Verification of whether "predicted new indication" reflects a true evidence gap in Finland (0 licenses, not marketed) or simply an unregistered existing-use product, to route this correctly as a market-entry case rather than a repurposing case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

