---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Epinephrine: From Anaphylaxis to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is classically used as an emergency treatment for anaphylaxis, cardiac arrest, and acute bronchospasm. The TxGNN model predicts it may also be broadly effective for **Obstructive Lung Disease**, a prediction already substantially supported by **50 clinical trials** and **20 publications** — several of which directly test inhaled or nebulized epinephrine in asthma and bronchiolitis. However, epinephrine currently holds **no marketing authorization in Finland**, and a Blocking-severity data gap in TFDA/Fimea package-insert warnings means the candidate cannot yet enter formal (S1) safety screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Finland regulatory data (0 licenses, unmarketed); epinephrine's well-established classic uses are anaphylaxis, cardiac arrest, and acute bronchospasm/asthma |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (conditional on resolving safety data gap) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available from DrugBank for this candidate (flagged as data gap **DG002**, High severity). Based on well-established pharmacology, however, epinephrine is a **nonselective α/β-adrenergic receptor agonist**. Its β2-receptor activity produces bronchial smooth-muscle relaxation (bronchodilation), while its α1-receptor activity reduces airway mucosal vascular congestion and edema — both actions directly counteract the airflow limitation that defines obstructive lung disease.

Critically, this is not a purely theoretical extrapolation: epinephrine already has a documented history of use in acute bronchospasm and asthma. The historical over-the-counter inhaler Primatene Mist, its investigational HFA reformulation (E004), and nebulized "racemic epinephrine"/adrenaline are all epinephrine-based products that have been directly studied in asthma and infant bronchiolitis — both recognized subtypes of obstructive lung disease. This is reflected in the trial evidence below, where multiple studies test epinephrine formulations head-to-head against albuterol, hypertonic saline, and placebo in exactly this disease space.

Because the mechanistic pathway is pharmacologically well characterized and the "new" indication substantially overlaps with epinephrine's existing off-label/legacy respiratory use, this candidate reaches a relatively mature decision stage (S3) with an L1 evidence level, despite the drug lacking a current Finland indication record.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | Completed | 373 | 12-week efficacy/safety of Epinephrine HFA Inhalation Aerosol MDI vs. placebo-HFA and marketed Primatene® Mist (CFC epinephrine inhaler) in adolescents/adults with asthma. |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | Nebulized 3% hypertonic saline vs. normal saline, both with epinephrine, in RSV-positive hospitalized infants with bronchiolitis. |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Combined nebulized adrenaline + oral betamethasone tested as an alternative to reduce hospitalization for acute bronchiolitis in pediatric emergency departments. |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Phase 2 | Completed | 18 | Cross-over safety/efficacy study of intranasal epinephrine (ARS-1) vs. albuterol as a needleless route for refractory asthma symptom management. |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Crossover PK comparison of inhaled Primatene Mist (epinephrine) vs. IM epinephrine injection vs. inhaled ProAir (albuterol) in healthy adults. |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | NA | Completed | 60 | RCT comparing nebulized 3% hypertonic saline vs. nebulized adrenaline for bronchiolitis, including response in initial non-responders. |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Deuterium-labeled PK study of epinephrine HFA-MDI (E004) inhalation aerosol distinguishing exogenous from endogenous epinephrine. |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | NA | Unknown | 600 | RCT comparing epinephrine and albuterol, the two most commonly used bronchodilators, in bronchiolitis. |
| [NCT01737892](https://clinicaltrials.gov/study/NCT01737892) | Phase 1/2 | Terminated | 21 | Follow-up PK/safety study of epinephrine HFA-MDI (E004) using deuterium-labeled epinephrine in healthy volunteers. |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Home oxygen therapy vs. standard nebulized therapy (0.1% epinephrine + bromhexine or hypertonic saline) in ambulatory infant bronchiolitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Review | The Cochrane Database of Systematic Reviews | "Epinephrine for bronchiolitis" — systematic review of bronchodilator use; effectiveness remains uncertain despite common practice. |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Review | The Cochrane Database of Systematic Reviews | Earlier Cochrane review version; bronchodilators show modest short-term benefit in mild-to-moderate bronchiolitis. |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Review of Respiratory Medicine | Reviews the role of racemic epinephrine, corticosteroids, hypertonic saline, and high-flow oxygen in pediatric bronchiolitis therapy. |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort | Scandinavian Journal of Clinical and Laboratory Investigation | Elevated plasma noradrenaline in chronic obstructive lung disease patients, correlated with hemodynamics and blood-gas abnormalities. |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | Overview of bronchiolitis epidemiology and treatment as the most common infant lower respiratory tract infection. |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | Earlier edition of the same bronchiolitis clinical-evidence review. |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Pending classification | Clinical Pharmacology and Therapeutics | "Bronchodilator effects of terbutaline and epinephrine in obstructive lung disease" — direct historical comparison of epinephrine's bronchodilator effect. |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Pending classification | Annals of Allergy | "Nebulized bronchodilators in obstructive lung disease II" — early evaluation of nebulized bronchodilator therapy including epinephrine. |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review | Journal of Allergy and Clinical Immunology | Review of childhood asthma pathophysiology, characterizing asthma as an obstructive airway disease. |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Other | The Medical Letter on Drugs and Therapeutics | Coverage of the OTC return of Primatene Mist (epinephrine inhaler) for asthma symptom relief. |

---

## Finland Market Information

Epinephrine currently holds **no marketing authorization on file in Finland** (0 licenses; market status: 未上市 / Not Marketed). No product name, dosage form, or approved-indication text is available from the regulatory data source for this candidate.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-drug interactions) is currently available for this candidate — the DDI query returned `not_found` with zero interactions on record. Please refer to the package insert for safety information.

**Note on safety data status:** This is flagged in the evidence pack as a **Blocking**-severity gap (DG001) — the absence of TFDA/Fimea package-insert warnings and contraindications means this candidate **cannot yet proceed to the S1 safety initial evaluation stage**, independent of how strong the efficacy/mechanistic evidence is for the predicted indication. Remediation requires downloading and parsing the official package insert PDF from the relevant regulatory source.

---

## Other TxGNN-Predicted Indications (Not Prioritized)

The evidence pack scored three additional candidate indications for epinephrine, none of which are recommended to advance at this time:

| Rank | Indication | Score | Evidence Level | Recommendation | Note |
|------|-----------|-------|----------------|-----------------|------|
| 2 | Food-Dependent Exercise-Induced Anaphylaxis (FDEIA) | 99.57% | L3 | Proceed with Guardrails | Strong mechanistic rationale (epinephrine is standard anaphylaxis rescue therapy) but no clinical trials — 20 review/case-level publications only; represents an indication-label extension rather than new pharmacology. |
| 3 | Rienhoff Syndrome | 99.57% | L5 | **Hold** | No clinical trials, no literature, no mechanistic link to adrenergic pharmacology (a rare LTBP3-related connective tissue disorder). Likely model noise/false positive from sparse rare-disease training data — not a meaningful signal. |
| 4 | Respiratory Malformation | 99.56% | L4 | **Hold** | Evidence retrieved is mismatched to the disease label — trials and literature relate to functional respiratory emergencies (cardiac arrest resuscitation, croup/upper-airway obstruction) rather than structural airway malformation. Requires disease-label clarification before further evaluation. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Conditional on Safety Data)**

**Rationale:**
The top-ranked prediction — epinephrine for obstructive lung disease — is supported by an L1 evidence level, including a completed Phase 3 RCT (NCT01357642, N=373) and a substantial, epinephrine-specific trial record spanning both asthma and bronchiolitis. This is less a novel prediction than a data-driven reconfirmation of epinephrine's existing legacy respiratory use. However, the candidate cannot move past initial safety screening until the Blocking-severity package-insert data gap (DG001) is resolved, and Finland market status (unmarketed, 0 licenses) still needs a defined regulatory pathway.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings and contraindications) — Blocking gap (DG001), required before S1 safety evaluation
- Confirmed DrugBank mechanism-of-action record — High-priority gap (DG002), to support mechanistic-link analysis
- A defined Finland regulatory/registration pathway, given the drug is currently unmarketed with zero licenses
- A completed drug-drug interaction (DDI) query, since the current query returned no results
- Route-compatibility confirmation (available vs. required administration routes), currently marked "pending" in the evidence pack
- Disease-label verification for "respiratory malformation" (rank 4), where retrieved evidence does not match the stated indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

