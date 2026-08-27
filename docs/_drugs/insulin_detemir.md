---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir is a long-acting basal insulin analogue with an established history of use in insulin-dependent diabetes mellitus. The TxGNN model's top prediction is **Type 1 Diabetes Mellitus** — but this is not a genuinely novel indication, since it falls within the drug's already-approved use. It is nonetheless the best-evidenced candidate in this pack, supported by **50 clinical trials** and **19 publications**, several of them completed Phase 3 RCTs directly comparing insulin detemir to NPH insulin in T1DM.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (Type 1 and Type 2), long-acting basal insulin therapy |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for insulin detemir was not available in the source evidence pack (DrugBank MOA field is flagged as a data gap). Based on established pharmacological knowledge, insulin detemir is a long-acting basal insulin analogue that reversibly binds circulating albumin via a C14 fatty-acid side chain, which slows its absorption and produces a smooth, prolonged (up to 24-hour) glucose-lowering effect through direct activation of the insulin receptor.

Unlike a typical repurposing candidate, the top prediction here — type 1 diabetes mellitus — is not a novel indication. Insulin detemir (Levemir) already has a decades-long clinical history in T1DM, and the underlying rationale explicitly notes that this represents the drug's original, already-approved indication rather than a new hypothesis. In T1DM, autoimmune destruction of pancreatic β-cells causes an absolute deficiency of endogenous insulin, so exogenous basal insulin replacement is a direct, mechanism-based causal treatment rather than a speculative association.

This candidate is surfaced here because it is, by a wide margin, the best-evidenced prediction in the pack. The next nine ranked indications — autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, the stiff-person-syndrome spectrum, pancreatic agenesis, and three lipodystrophy/lipoatrophy phenotypes — all sit at Evidence Level L5 with zero supporting trials or literature. Several of the lipodystrophy predictions in particular likely reflect a **reversed causal direction** in the knowledge graph (insulin injection as a known *cause* of localized lipoatrophy, not a treatment for it), and should not be advanced without independent mechanistic validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00655200](https://clinicaltrials.gov/study/NCT00655200) | N/A (Observational) | Completed | 2286 | Safety and tolerability of Levemir® FlexPen® (insulin detemir) in Filipino patients with Type 1 and Type 2 diabetes. |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Multinational RCT comparing insulin detemir vs. NPH insulin (both with insulin aspart bolus) in pregnant women with T1DM. |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Compares insulin detemir vs. NPH insulin (with aspart) in children and adolescents with T1DM. |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | Six-month efficacy/safety comparison of insulin detemir (2400 nmol/mL formulation) vs. NPH insulin in a basal-bolus regimen for T1DM. |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Multinational RCT comparing insulin detemir + aspart vs. NPH + human soluble insulin on glycaemic control in T1DM. |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Efficacy/safety of insulin degludec/aspart once daily vs. insulin detemir once/twice daily plus mealtime aspart in children/adolescents with T1DM. |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | Completed | 520 | Compares once-daily vs. twice-daily insulin detemir in a basal-bolus regimen with aspart for T1DM, evaluating HbA1c reduction and hypoglycaemia risk. |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Efficacy and safety of insulin detemir + aspart vs. NPH + aspart in adults with T1DM. |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Phase 3 | Completed | 26 | Dapagliflozin added to liraglutide and insulin (detemir as background basal insulin) in T1DM; evaluates glycaemic variability and insulin dose reduction. |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | Terminated | 596 | 104-week trial comparing inhaled mealtime insulin vs. subcutaneous insulin aspart, both combined with insulin detemir, in T1DM. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT trial: insulin degludec non-inferior to insulin detemir (both + aspart) in pregnant women with T1DM. |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review / Network Meta-analysis | Value in Health | Compares relative efficacy and safety of basal insulin regimens, including detemir, in adults with T1DM. |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review / Meta-analysis | Polskie Archiwum Medycyny Wewnetrznej | Insulin detemir vs. NPH insulin in T1DM — glycaemic control outcomes not uniformly confirmed across studies. |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Reviews (ultra-)long-acting insulin analogues, including detemir, for people with T1DM. |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vascular Health and Risk Management | Update on T1DM/T2DM treatment focused on insulin detemir; lower hypoglycaemia rates vs. NPH insulin. |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vascular Health and Risk Management | Reviews insulin detemir's unique albumin-binding mechanism and reduced hypoglycaemia risk in T1DM/T2DM. |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Review of insulin detemir's pharmacology and clinical use in T1DM and T2DM management. |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Spotlight review on insulin detemir's predictable, protracted glucose-lowering effect in T1DM/T2DM. |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatric Drugs | Reviews insulin analogue preparations, including detemir, in children/adolescents with T1DM. |
| [30666772](https://pubmed.ncbi.nlm.nih.gov/30666772/) | 2019 | Analysis of RCT data | Pediatric Diabetes | Compares hyperglycaemia/ketosis rates between degludec-based treatment and insulin detemir in pediatric T1DM across two RCTs. |

---

## Finland Market Information

Insulin detemir currently holds **no marketing authorization in Finland** — the evidence pack records 0 licenses and a market status of "Not marketed." No Finland-specific product, dosage form, or approved-indication text is available for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The T1DM indication reaches Evidence Level L1, backed by multiple completed Phase 3 RCTs and systematic reviews directly evaluating insulin detemir. However, this validates an existing, already-approved indication rather than establishing a new one, and the drug currently has zero marketing authorizations in Finland, with a Blocking-severity gap in local package-insert safety data (warnings/contraindications).

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Structured DrugBank mechanism-of-action data (DG002, High severity)
- Confirmation of regulatory/reimbursement pathway for market entry in Finland (currently 0 authorizations)
- Since this is not a novel indication, reclassify this candidate as "existing indication confirmation" rather than a repurposing opportunity in the pipeline
- Ranks 2–10 (all L5, Hold) should be deprioritized pending real trial or literature evidence; the lipodystrophy-related predictions in particular warrant a knowledge-graph causal-direction review before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

