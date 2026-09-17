---
layout: default
title: Lacosamide
parent: Kohtalainen näyttö (L3-L4)
nav_order: 210
evidence_level: L3
indication_count: 10
---

# Lacosamide
{: .fs-9 }

Näytön taso: **L3** | Ennustetut käyttöaiheet: **10** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Lacosamide: From Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is an antiepileptic drug (AED), acting as a sodium-channel modulator used for partial-onset seizures. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but the strongest current evidence (1 recruiting Phase 3 trial and multiple retrospective/case reports) addresses bipolar **depressive**, not manic, episodes — a polarity mismatch that limits confidence in this specific prediction.

*Note: `original_indications` and `original_moa` were not populated in the evidence pack (data gap DG002). "Epilepsy (partial-onset seizures)" is inferred from the supporting literature/trial descriptions (e.g., "FDA-approved for treating partial seizures," "adjunctive treatment for partial epilepsy"), not from a formal indication field.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset seizures) — inferred from literature, not a formal labeled field |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.96% (rank 711) |
| Evidence Level | L3 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question (Hold pending confirmatory data) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, lacosamide selectively enhances slow inactivation of voltage-gated sodium channels — a mechanism pharmacologically related to established mood stabilizers such as lamotrigine, which is used clinically for bipolar disorder. This shared class-level mechanism is the biological rationale behind the TxGNN prediction.

However, the relationship between the original indication (epilepsy) and the predicted new indication (bipolar **mania**) is indirect. Existing clinical and case-level evidence on lacosamide in bipolar disorder consistently centers on **depressive** and mixed/anxious symptoms — e.g., open-label improvement of depressive symptoms, and the only ongoing Phase 3 trial (NCT07412132) specifically targets major depressive episodes in Bipolar I/II. No trial or publication in this evidence pack directly demonstrates antimanic efficacy, so the mechanistic story (sodium-channel stabilization → mood stabilization) is plausible but has not been shown to extend to the manic pole specifically.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Evaluates lacosamide as augmentation therapy for **major depressive episodes** in Bipolar I/II (not mania); based on prior observational/open-label signals of mood improvement in epilepsy and bipolar patients. Polarity mismatch with the "manic" prediction — no results yet. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide vs. other AEDs in bipolar disorder patients without epilepsy — first dedicated look at lacosamide in BD. |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot | J Clin Psychopharmacol | 12-week open-label pilot showing efficacy/safety signal specifically in **bipolar depression**. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective multicenter | Epilepsy Behav | Lacosamide associated with improved depression/anxiety symptoms in focal epilepsy patients — precursor signal for psychiatric use. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Mood stabilization achieved with lacosamide in a patient with comorbid mood disorder, PTSD, and fronto-temporal epilepsy. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report (adverse event) | Indian J Psychol Med | Neutropenia precipitated by lacosamide in a patient with bipolar disorder and comorbid epilepsy — safety signal. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case report | Cureus | Complex case of Bipolar I disorder with multiple comorbidities including seizure-like activity; illustrative rather than efficacy evidence. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | Notes AEDs, including lacosamide's class, are used off-label in bipolar disorder management. |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Adv Drug Deliv Rev | Background on lacosamide's chemical/pharmacokinetic properties among newer AEDs. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chem Neurosci | Discusses CRMP2 as a druggable target relevant to lacosamide's mechanism of action. |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | Mechanistic | PNAS | Cryo-EM structural mechanism of Nav channel inhibition by lamotrigine, a related mood-stabilizing AED — supports the shared-mechanism rationale. |

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and DDI data were not available in this evidence pack — DG001, classified as Blocking, prevents a full S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Research Question (Hold pending confirmatory data)**

**Rationale:**
The mechanistic rationale (sodium-channel slow-inactivation, class analogy to lamotrigine) is plausible, but all available clinical evidence for lacosamide in bipolar disorder addresses the **depressive** pole (open-label pilot, retrospective cohort, one recruiting Phase 3 trial), not the **manic** pole predicted here — a direct polarity mismatch flagged in the evidence pack's own relevance grading (Grade B). No completed trial or literature currently supports antimanic efficacy.

**To proceed, the following is needed:**
- TFDA/EMA package insert data to close the Blocking safety gap (DG001) before any S1 progression
- Formal MOA documentation (DG002) to substantiate the sodium-channel-to-mood-stabilization mechanistic link
- Results from NCT07412132 (depressive-episode trial) once available, to gauge translatability to manic presentations
- Consider re-scoping the candidate indication toward "bipolar depression" specifically, where evidence is materially stronger than for "manic bipolar affective disorder"
- Note: within this same evidence pack, **migraine disorder** (rank 5) shows substantially stronger evidence (L1, head-to-head Phase 3 RCTs vs. propranolol, decision stage S3, "Proceed with Guardrails") and may warrant separate, higher-priority evaluation
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

