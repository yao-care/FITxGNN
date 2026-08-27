---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

> Perampanel is a selective, non-competitive AMPA-receptor antagonist originally developed and marketed worldwide as an adjunctive (and later monotherapy) treatment for partial-onset seizures and primary generalized tonic-clonic seizures.
> The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex seizure subtype),
> with **3 clinical trials** and **20 publications** currently associated with this direction — though none directly enrolled visual-epilepsy patients, so the supporting evidence remains indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial-onset seizures (adjunctive/monotherapy) and primary generalized tonic-clonic seizures (epilepsy), per published literature — no Finland-specific approved indication text on file |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured drug record (`original_moa` = Data Gap). Based on the supporting literature in this evidence pack, perampanel is a first-in-class, selective, non-competitive antagonist of AMPA-type glutamate receptors, which mediate the fast excitatory synaptic transmission that drives cortical hyperexcitability in seizures. It has been approved in over 35 countries as an adjunctive and later monotherapy treatment for focal (partial-onset) seizures and primary generalized tonic-clonic seizures.

Visual epilepsy (photosensitive/visually-induced reflex epilepsy) is a seizure subtype in which flickering light or patterned visual stimuli trigger cortical hypersynchronous discharge, a phenomenon mechanistically tied to excessive AMPA-receptor-mediated excitation in the occipital and adjacent cortex. Because perampanel's broad-spectrum action targets this same excitatory pathway, the TxGNN prediction has plausible mechanistic grounding.

However, this is a rationale by mechanistic extrapolation rather than direct evidence: none of the identified trials or publications specifically enrolled or studied visual/photosensitive epilepsy patients. The clinical trials found relate to perampanel's general safety, pharmacokinetics, and neurophysiological effects (EEG/VEP/SEP/BAEP) in mixed epilepsy populations, and the literature largely covers perampanel's broad-spectrum efficacy in focal and generalized epilepsies rather than reflex seizure subtypes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Tolerability, safety, and pharmacokinetics of perampanel (E2007) in patients with refractory partial or generalised seizures; general epilepsy population, not visual-epilepsy specific (Relevance C) |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Evaluated whether perampanel affects neurophysiology tests including visual evoked potential (VEP), EEG, SEP, and BAEP; assesses testing parameters, not seizure control in visual epilepsy (Relevance C) |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Evaluated perampanel's effects on cognition and EEG in general epilepsy patients receiving adjunctive treatment (Relevance C) |

No trial directly enrolled or tested efficacy in visual/photosensitive epilepsy patients.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review/NMA | Journal of Neurology | Network meta-analysis comparing ASM efficacy/safety for idiopathic generalized epilepsies, a category that includes photosensitive seizure phenotypes |
| [37059702](https://pubmed.ncbi.nlm.nih.gov/37059702/) | 2023 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Reviews perampanel add-on therapy for drug-resistant focal epilepsy |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review/Meta-analysis | Seizure | Pooled RCT data on perampanel efficacy and safety across focal and generalized seizure types |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review/Meta-analysis | Brain & Development | Efficacy, tolerability, and safety of perampanel in children and adolescents with epilepsy |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Systematic Review/NMA | Drugs | Network meta-analysis of third-generation ASMs (including perampanel) as adjunctive treatment for focal-onset seizures |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Cohort/Real-world | Epilepsy & Behavior | Reviews clinical trial and real-world evidence for perampanel monotherapy across FOS and GTCS |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline Review | Neurology | AAN/AES practice guideline update on efficacy/tolerability of new AEDs, including perampanel, for new-onset epilepsy |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opinion on Drug Discovery | History of perampanel's discovery and development as an AMPA-receptor antagonist |
| [26111428](https://pubmed.ncbi.nlm.nih.gov/26111428/) | 2015 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetic/pharmacodynamic evaluation of perampanel for partial-onset seizures |
| [38602656](https://pubmed.ncbi.nlm.nih.gov/38602656/) | 2024 | Preclinical/Mechanism study | Molecular Neurobiology | Investigates perampanel's effect on autophagy-mediated regulation of AMPA-receptor subunit GluA2 and PSD95 in epilepsy — mechanistic support for the AMPA-pathway rationale |

None of the identified publications specifically study visual/photosensitive epilepsy; all pertain to perampanel's general efficacy in focal or generalized epilepsy, or to its underlying AMPA-receptor mechanism.

---

## Finland Market Information

Perampanel is currently **not marketed in Finland** — no product authorizations are on file (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — see Data Gap DG001, which is flagged as Blocking for safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the visual-epilepsy indication is limited to mechanistic plausibility (AMPA-receptor antagonism counteracting light-induced cortical hyperexcitability) supported only by trials and literature on perampanel's general epilepsy efficacy — none address visual/photosensitive epilepsy directly, and the strongest cited trials are graded "C" relevance. This corresponds to evidence level L4 / decision stage S1 ("Research Question"), insufficient to proceed even with guardrails.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Structured mechanism-of-action data from DrugBank (DG002)
- A dedicated trial or case series enrolling patients with visual/photosensitive reflex epilepsy
- For context: among the other TxGNN-predicted indications for perampanel in this evidence pack, **status epilepticus** (rank 10) has materially stronger evidence — an ongoing Phase 3 add-on trial, a Phase 2 prophylaxis trial, and a systematic review — reaching evidence level L3 / "Proceed with Guardrails." This may be a more promising near-term repurposing candidate than visual epilepsy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

