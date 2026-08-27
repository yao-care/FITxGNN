---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: Type 1 Diabetes Mellitus — Existing Indication, Not a New Repurposing Signal

## One-Sentence Summary

Insulin aspart (DrugBank ID DB01306) is a rapid-acting insulin analog; this evidence pack has no record of its original indication or MOA (data gap). TxGNN's top-ranked prediction, **Type 1 Diabetes Mellitus**, is supported by **50 clinical trials** and **20 publications** — but this volume of evidence reflects insulin aspart's already-established standard-of-care role in T1DM, not a genuine new-use discovery.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (`original_indications` is empty) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological classification, insulin aspart is a rapid-acting recombinant human insulin analog, engineered for faster subcutaneous absorption than regular human insulin; its role is direct replacement of endogenous insulin to control blood glucose.

Critically, the evidence pack's own analysis flags an important caveat: Type 1 Diabetes Mellitus is not really a *novel* predicted indication for insulin aspart — it is the drug's actual, long-standing, guideline-standard indication. The fact that `original_indications` is empty and `market_status` shows "Not Marketed" in Finland appears to reflect gaps in the underlying regulatory database rather than clinical reality, since insulin aspart products (e.g., NovoRapid/NovoLog, Fiasp) are widely used for T1DM glycemic control internationally.

Mechanistically, T1DM is caused by autoimmune destruction of pancreatic beta cells and absolute insulin deficiency — exogenous rapid-acting insulin is the definitive replacement therapy. This is why the model surfaces such a high score and a large body of directly relevant trials and literature: TxGNN has essentially rediscovered an existing, proven treatment relationship rather than identifying a new therapeutic hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | Terminated | 596 | Direct comparison of inhaled mealtime insulin vs. subcutaneous insulin aspart (+ insulin detemir) in T1DM over 104 weeks |
| [NCT02546401](https://clinicaltrials.gov/study/NCT02546401) | Phase 3 | Completed | 22 | Tested pre- vs. post-meal bolus timing of insulin aspart via insulin pump in T1DM patients |
| [NCT05413369](https://clinicaltrials.gov/study/NCT05413369) | Phase 3 | Completed | 582 | Large multicenter trial comparing iGlarLixi to IDegAsp (insulin degludec/aspart) in diabetes inadequately controlled on oral agents |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Phase 3 | Completed | 26 | Dapagliflozin add-on to liraglutide and insulin in T1DM; insulin (incl. aspart) as background therapy |
| [NCT03800875](https://clinicaltrials.gov/study/NCT03800875) | Phase 2 | Completed | 24 | Dual-hormone (insulin-pramlintide) closed-loop delivery without carbohydrate counting in T1DM adults |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | Safety comparison of HMR1964 vs. insulin aspart via continuous subcutaneous insulin infusion in T1DM |
| [NCT01513590](https://clinicaltrials.gov/study/NCT01513590) | Phase 3 | Completed | 394 | 26-week trial comparing insulin degludec/aspart (IDegAsp) vs. biphasic insulin aspart 30, both with metformin |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Insulin detemir vs. NPH insulin, both combined with mealtime insulin aspart, in children/adolescents with T1DM |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Insulin detemir vs. NPH insulin combined with insulin aspart bolus in pregnant women with T1DM |
| [NCT00082407](https://clinicaltrials.gov/study/NCT00082407) | Phase 3 | Completed | 505 | Exenatide vs. twice-daily biphasic insulin aspart in diabetes on sulfonylurea/metformin |

*40 additional trials were returned but are not shown; most involve insulin aspart as background/comparator therapy in device or combination studies.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT (systematic review-based) | Diabetes & Metabolism | Efficacy/safety comparison of rapid-acting insulin aspart vs. regular human insulin in T1DM/T2DM |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT (Phase 3a) | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily degludec in basal-bolus regimen for T1DM |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT trial: insulin degludec vs. detemir, both with insulin aspart, in pregnant women with T1DM |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes & Endocrinology | Management of T1DM in pregnancy — lifestyle, pharmacological treatment, glycaemic targets |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Type 1 Diabetes overview — autoimmune beta-cell destruction, epidemiology, complications |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treatments in Endocrinology | Spotlight on insulin aspart in T1DM/T2DM — lower HbA1c and improved postprandial control vs. regular insulin |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Insulin aspart review of use in T1DM/T2DM management |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Biphasic insulin aspart 30 for treatment of T1DM |
| [35746893](https://pubmed.ncbi.nlm.nih.gov/35746893/) | 2023 | Meta-analysis | Diabetes & Metabolism Journal | Fast-acting aspart vs. aspart via insulin pump in T1DM |
| [31345519](https://pubmed.ncbi.nlm.nih.gov/31345519/) | 2019 | Review | Endocrinology and Metabolism Clinics of North America | Type 1 diabetes in pregnancy — glycemic control challenges and technology advances |

*10 additional publications were returned but are not shown.*

## Finland Market Information

Insulin aspart currently shows **no marketing authorization records** in this evidence pack (`market_status`: Not Marketed, `total_licenses`: 0). Given insulin aspart's broad clinical use and trial base shown above, this likely reflects a gap in the underlying regulatory database rather than actual market absence, and should be re-verified against Fimea's official registry.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The scale of Phase 3 trial and literature evidence (L1) confirms insulin aspart's efficacy for T1DM, but this is because T1DM is already its standard indication — not a genuine repurposing discovery. This candidate should be handled as a data-quality correction, not a novel opportunity, before any downstream action is taken.
- Separately, two other TxGNN signals for this drug (drug-induced localized lipodystrophy, centrifugal lipodystrophy) appear to have reversed causality — insulin injection is a known *cause* of localized lipodystrophy, not a treatment for it — and should be flagged as safety review items rather than repurposing candidates.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings and contraindications) — currently a blocking data gap (DG001)
- DrugBank-sourced mechanism of action confirmation (DG002)
- Correction of `original_indications` and `market_status` fields in the source database to reflect insulin aspart's actual approved indication and Finland marketing status
- Re-classification of this candidate in the pipeline from "predicted new indication" to "existing indication — database gap"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

