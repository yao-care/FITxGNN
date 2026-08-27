---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Bipolar Depression to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone is a second-generation antipsychotic with FDA-approved indications for schizophrenia and bipolar I depression (monotherapy or adjunctive to lithium/valproate). The TxGNN model predicts it may also be effective for **Manic Bipolar Affective Disorder**, with **15 clinical trials** and **19 publications** identified, though the strongest direct evidence covers bipolar depression and maintenance therapy rather than acute mania itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; Bipolar I depression (monotherapy or adjunctive to lithium/valproate) — per FDA label; no Finland regulatory record available |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed TFDA-formatted mechanism of action documentation is not currently available (data gap, DG002). Based on known pharmacological information, Lurasidone acts as a D2/5-HT2A/5-HT7 receptor antagonist with 5-HT1A partial agonist activity — the standard second-generation antipsychotic receptor profile used across the bipolar disorder treatment spectrum.

Lurasidone's approved efficacy in bipolar I depression (as monotherapy and as adjunctive therapy to lithium or valproate for maintenance/recurrence prevention) establishes a strong pharmacological rationale for use across other phases of bipolar disorder, including mania, since both mood states fall within the same underlying disease and are commonly managed with the same antipsychotic class.

However, this extrapolation should be applied cautiously: the one trial designed specifically to test lurasidone in acute mania (NCT01932541, pediatric/adolescent mania) was withdrawn with zero enrollment, meaning there is currently no completed dedicated efficacy trial for the manic pole itself. The bulk of the strong (Grade A) evidence instead supports bipolar depression treatment and long-term maintenance/relapse prevention, which is an adjacent but distinct clinical use case from acute mania.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Lurasidone adjunctive to lithium or divalproex vs. placebo for recurrence prevention in Bipolar I Disorder (PREVAIL 2); direct support for long-term efficacy |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety study of lurasidone (SM-13496) in Bipolar I Disorder |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label extension evaluating long-term safety/tolerability of flexibly dosed lurasidone in pediatric subjects |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2726 | SMART pragmatic trial comparing four treatments (including lurasidone) for bipolar depression |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | Randomized, double-blind, placebo-controlled study of lurasidone (SM-13496) for Bipolar I Depression |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | Open-label extension evaluating longer-term safety/effectiveness of lurasidone adjunctive to lithium/divalproex |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | Efficacy and safety of lurasidone in children/adolescents with Bipolar I Depression |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | Lurasidone adjunctive therapy for cognitive functioning in euthymic Bipolar I/II patients (ELICE-BD) |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | Completed | 53 | Randomized open-label study of cognitive changes in euthymic bipolar patients treated with lurasidone vs. treatment as usual |
| [NCT02974010](https://clinicaltrials.gov/study/NCT02974010) | Phase 2 | Completed | 22 | Sequential therapy (ketamine/NRX-100 followed by d-cycloserine + lurasidone/NRX-101) for acute suicidal ideation in bipolar depression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Meta-analysis (Tier 1) | BMJ Mental Health | Dose-response meta-analysis of lurasidone efficacy and acceptability specifically in bipolar depression |
| [31957501](https://pubmed.ncbi.nlm.nih.gov/31957501/) | 2020 | Review | Expert Opin Pharmacother | Evaluates lurasidone in bipolar disorder; explicitly notes lurasidone has not been directly studied in mania/bipolar psychosis |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Guideline (Tier 1) | Bipolar Disorders | CANMAT/ISBD 2018 bipolar disorder management guidelines |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Guideline (Tier 1) | Bipolar Disorders | CANMAT/ISBD recommendations for bipolar disorder with mixed presentations |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Network meta-analysis (Tier 1) | Lancet Psychiatry | Comparative efficacy/tolerability of pharmacological interventions for acute bipolar depression |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review (Tier 2) | JAMA | Overview of diagnosis and treatment of bipolar disorder |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Network meta-analysis (Tier 2) | Molecular Psychiatry | Mood stabilizers and/or antipsychotics for bipolar disorder maintenance phase |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Editorial | American Journal of Psychiatry | Commentary on lurasidone and bipolar disorder |
| [36472471](https://pubmed.ncbi.nlm.nih.gov/36472471/) | 2022 | Review (Tier 2) | J Child Adolesc Psychopharmacol | Psychopharmacological treatment algorithms for manic/mixed and depressed episodes in pediatric bipolar disorder |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Reviews antipsychotics used as antidepressants, notes lurasidone's approval for bipolar depression |

---

## Finland Market Information

No marketing authorizations are currently registered in Finland (0 licenses; market status: Not Marketed). No authorization number, product name, or approved indication text is available from the regulatory data source.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications and DDI data are currently unavailable — flagged as a Blocking data gap, DG001, preventing full S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (L1 evidence) support lurasidone's efficacy across the bipolar disorder spectrum, particularly bipolar depression and long-term maintenance/relapse prevention. However, no completed trial has directly tested lurasidone in acute mania — the one mania-specific trial was withdrawn — so the "manic bipolar affective disorder" prediction should be treated as an extrapolation within the same disease rather than a directly proven indication.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Formal mechanism of action documentation from DrugBank (DG002)
- A dedicated placebo-controlled efficacy trial (or post-hoc analysis) specifically in acute mania, since current evidence concentrates on the depressive/maintenance phase
- Confirmation of Finland market entry plans, given zero current marketing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

