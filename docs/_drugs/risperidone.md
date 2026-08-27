---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Risperidone: From Schizophrenia to Major Affective Disorder

## One-Sentence Summary

Risperidone is a second-generation antipsychotic established for schizophrenia, and — per the rationale annotations in this evidence pack — also for bipolar mania and irritability associated with autistic disorder. Among six TxGNN-predicted indications in this pack, **Major Affective Disorder** is the only one reaching robust evidence (L1), supported by **37 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs on bipolar maintenance and antidepressant augmentation.

> Note: This evidence pack contains 6 TxGNN-predicted indications ranked by raw model score. The top three by score (gaze palsy with progressive scoliosis, Asperger susceptibility, amelocerebrohypohidrotic syndrome) are explicitly flagged in the data as lacking any biological plausibility or supporting evidence ("prediction noise", L5/Hold). This report focuses on **Major Affective Disorder**, which — despite a lower raw TxGNN rank (8680 vs. 3022) — is the only candidate with L1-level clinical evidence and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; also established for bipolar mania and irritability associated with autistic disorder (per evidence-pack rationale; not itemized in license data) |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.11% (rank 8680) |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for risperidone is not available in this evidence pack (DG002, High severity gap). Based on the mechanistic rationale recorded alongside the predictions, risperidone is a second-generation (atypical) antipsychotic acting primarily as a D2 and 5-HT2A receptor antagonist.

This mechanism is already clinically validated in mood disorders: risperidone (including its long-acting injectable formulation) is an established monotherapy and adjunctive therapy for bipolar I disorder mania, and is used off-label/evidence-supported as an augmentation agent to SSRIs/antidepressants in treatment-resistant major depressive disorder. "Major Affective Disorder" as a disease category spans both bipolar and unipolar mood disorders, so the mechanistic link to risperidone's established D2/5-HT2A antagonism is direct rather than speculative — unlike the top-scored but evidence-free candidates in this pack.

The supporting evidence base includes several completed Phase 3, placebo-controlled RCTs (bipolar mania/maintenance, TRD augmentation) plus multiple systematic reviews and network meta-analyses on antipsychotic augmentation in TRD, which together justify the L1 evidence classification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | TEAM study: lithium vs. valproate vs. risperidone in children/adolescents with bipolar disorder or mania symptoms |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Phase 4 | Terminated | 45 | ECT + risperidone vs. ECT alone for treatment-resistant depression |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Phase 4 | Completed | 60 | Double-blind, placebo-controlled risperidone monotherapy in bipolar disorder with comorbid anxiety |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Risperidone LAI monotherapy vs. placebo for prevention of mood episodes in bipolar I disorder |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Double-blind, placebo-controlled risperidone monotherapy in bipolar disorder with panic/GAD comorbidity |
| [NCT05473741](https://clinicaltrials.gov/study/NCT05473741) | N/A | Completed | 51 | Prospective cohort on breakthrough psychotic/mood symptoms during LAI antipsychotic maintenance |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind adjunctive risperidone vs. placebo in MDD with suboptimal antidepressant response |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Efficacy/safety/maintenance of risperidone augmentation of SSRI in treatment-resistant unipolar depression |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Risperidone vs. divalproex in pediatric bipolar disorder with MRI circuitry assessment |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Completed | 46 | Placebo-controlled trial of valproate and risperidone in young children (ages 3-7) with bipolar disorder |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | Randomized trial of risperidone augmentation for treatment-refractory major depressive disorder |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review/NMA | J Affective Disorders | Network meta-analysis comparing augmentation agents (incl. antipsychotics) for treatment-resistant depression |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review/Meta-analysis | J Psychopharmacology | Augmentation/combination treatments for early-stage treatment-resistant depression |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Review/Meta-analysis | J Psychopharmacology | Efficacy/tolerability of antidepressant + second-generation antipsychotic combinations vs. esketamine vs. lithium |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Review/Meta-analysis | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (monotherapy and adjunctive) in adult MDD |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Population-based Study | J Clinical Psychiatry | Nationwide effectiveness study of SGA augmentation (aripiprazole, olanzapine, quetiapine, risperidone) in MDD |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Review | Cochrane Database Syst Rev | Second-generation antipsychotics for major depressive disorder and dysthymia |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Review | Annals of Pharmacotherapy | Efficacy and safety of risperidone augmentation for treatment-resistant MDD |
| [7545159](https://pubmed.ncbi.nlm.nih.gov/7545159/) | 1995 | Open-label/Case series | J Clinical Psychiatry | Early report on risperidone's potential in affective illness and OCD |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | Efficacy/tolerability of antidepressant + atypical antipsychotic augmentation (17 trials, 3807 patients) in MDD |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(DG001 — TFDA/local package insert warnings and contraindications — is flagged as a Blocking data gap and must be resolved before any S1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Major Affective Disorder is the only predicted indication in this pack reaching L1 evidence, backed by multiple completed Phase 3 RCTs (bipolar maintenance, TRD augmentation) and several systematic reviews/meta-analyses confirming risperidone's established, clinically-validated role in mood disorder management. However, this represents an evidence-supported expansion within risperidone's known psychiatric use pattern rather than a novel mechanism-driven repurposing, and critical safety/regulatory data remain unresolved.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (DG001, Blocking — resolve via TFDA package insert PDF)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Local market/registration status confirmation (currently 0 licenses on file — verify if this reflects an actual regulatory gap)
- Formal DDI review (current query returned "not_found")
- Manual review of the 27 additional "pending"-graded trials in this dataset for relevance classification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

