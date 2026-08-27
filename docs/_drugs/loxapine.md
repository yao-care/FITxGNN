---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Loxapine
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

# Loxapine: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Loxapine is a first-generation (typical) antipsychotic historically used for **schizophrenia**; it is not currently marketed in Finland and has no Fimea license on file. The TxGNN model predicts it may also be effective for **Manic Bipolar Affective Disorder**, and this is not a purely speculative prediction — an inhaled formulation of loxapine (Adasuve) is already approved in the US/EU for acute agitation in bipolar I disorder. **20 publications**, including a systematic review/meta-analysis and Phase III RCT reports, currently support this direction, though no trials are registered in the structured clinical-trials feed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per literature; no Finland regulatory license on file — drug is unmarketed) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this candidate. Based on known pharmacology, Loxapine is a dibenzoxazepine-class first-generation antipsychotic acting primarily via D2 dopamine and 5-HT2A serotonin receptor antagonism, with additional sedating (antihistaminic) properties. Its efficacy in schizophrenia, particularly for psychotic and agitated symptoms, has been established through decades of clinical use.

Manic episodes in bipolar disorder and acute psychotic exacerbations in schizophrenia share substantial symptomatic and neurochemical overlap — both frequently present with agitation, hyperarousal, and impaired reality testing that respond to D2/5-HT2A blockade. This is not a purely mechanistic extrapolation: an inhaled powder formulation of loxapine (Adasuve®, using the Staccato® delivery system) has already been approved in the United States and European Union specifically for the acute treatment of agitation associated with **both** schizophrenia and bipolar I disorder, reaching peak plasma concentrations within minutes. Two Phase III randomized, double-blind, placebo-controlled trials (registered as NCT00628589 and NCT00721955, referenced within the literature evidence below) enrolled agitated patients with bipolar I disorder specifically, and demonstrated efficacy using the PANSS-Excited Component scale.

Given this existing regulatory precedent for the agitation/mania indication in bipolar disorder, the TxGNN prediction is well-supported by real-world clinical development rather than being an unvalidated model artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the structured trials feed. (Note: the literature evidence below references two Phase III RCTs — NCT00628589 and NCT00721955 — and the PLACID trial, but these were not returned by the structured ClinicalTrials.gov/ICTRP query for this candidate.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review & Meta-analysis | Human Psychopharmacology | Systematic review of short-term pharmacological interventions for agitation associated with schizophrenia or bipolar disorder. |
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | RCT | European Neuropsychopharmacology | PLACID study: assessor-blind, parallel-group RCT (23 centres, 4 countries) comparing inhaled loxapine vs IM aripiprazole in acutely agitated schizophrenia/bipolar I patients. |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | RCT (post-hoc analysis) | BJPsych Open | PANSS-EC responder analysis of two Phase III RCTs (NCT00628589, NCT00721955) in 344 schizophrenia and 314 bipolar I agitated patients. |
| [28376877](https://pubmed.ncbi.nlm.nih.gov/28376877/) | 2017 | RCT (study design) | BMC Psychiatry | Rationale and design of the PLACID RCT comparing inhaled loxapine vs IM aripiprazole for acute agitation in schizophrenia/bipolar disorder. |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | Review (RCT effect sizes) | International Journal of Clinical Practice | Analysis of effect sizes from 2 Phase III RCTs of inhaled loxapine in schizophrenia/bipolar agitation. |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review | CNS Drugs | Review of inhaled loxapine powder (Adasuve) approval and use in acute agitation in bipolar disorder/schizophrenia. |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Expert Review/Commentary | Drugs in R&D | Expert review of inhaled loxapine for acute agitation management in bipolar disorder and schizophrenia. |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatric Disease and Treatment | Safety, efficacy, and patient acceptability of inhaled loxapine for acute agitation in schizophrenia/bipolar I disorder. |
| [28208695](https://pubmed.ncbi.nlm.nih.gov/28208695/) | 2017 | Clinical Review | International Journal of Molecular Sciences | Clinical review of inhaled loxapine's role in treating acute agitation in psychiatric disorders. |
| [27121764](https://pubmed.ncbi.nlm.nih.gov/27121764/) | 2016 | Review (drug profile) | Current Medical Research and Opinion | Review of inhaled loxapine for urgent treatment of acute agitation in schizophrenia/bipolar disorder. |

---

## Finland Market Information

Loxapine is currently **not marketed** in Finland — no Fimea marketing authorizations are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-interaction data were returned for this candidate; a Fimea package-insert review is required before any S1 safety assessment can proceed — see Data Gap DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Loxapine's applicability to acute agitation in bipolar mania is corroborated by an existing approved indication (inhaled loxapine/Adasuve, US/EU) and by two Phase III RCTs plus a systematic review — this is meaningfully stronger than a pure model prediction (L2). However, no Finland licensing, package-insert safety data, or DrugBank MOA record currently exist, so the candidate cannot yet clear a formal S1 safety gate.

**To proceed, the following is needed:**
- Fimea/TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- DrugBank-confirmed mechanism of action — currently a High-severity data gap (DG002)
- Confirmation of route compatibility (oral vs. inhaled loxapine) against the RCT evidence base, since the strongest supporting trials used the inhaled Adasuve formulation
- Drug-drug interaction data (current DDI query returned no results)

**Note on other predicted indications:** Nine additional TxGNN-predicted indications (ranks 2–10, e.g., retinal dystrophy, hydranencephaly, X-linked myopia variants, Charcot-Marie-Tooth type 1G) were also screened. All were rated **L5 / Hold** — no clinical trials, no relevant literature, and no plausible mechanistic link to loxapine's D2/5-HT2A pharmacology. These appear to be TxGNN link-prediction noise rather than genuine repurposing signals and are not recommended for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

