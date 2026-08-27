---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

Using the drug-repurposing evaluation report template directly on the supplied Evidence Pack (rank-1 predicted indication = *visual epilepsy*, TxGNN score 99.98%).

# Levetiracetam: From Epilepsy to Visual (Photosensitive) Epilepsy

## One-Sentence Summary

Levetiracetam is an established second-generation antiepileptic drug (AED), most widely used for partial-onset and generalized seizures. TxGNN predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex seizure subtype), a direction currently supported by **9 clinical trials** and **20 publications**, though none targets this specific reflex subtype directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — adjunctive/monotherapy for partial-onset seizures, and adjunctive treatment of myoclonic seizures in juvenile myoclonic epilepsy and primary generalized tonic-clonic seizures (per literature evidence; no Finland license text available) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for levetiracetam in this evidence pack. Based on known pharmacology (also reflected in this pack's own repurposing rationale fields), levetiracetam binds to synaptic vesicle protein 2A (SV2A), modulating neurotransmitter release and reducing pathological neuronal hypersynchronization — the mechanism underlying its broad-spectrum antiseizure effect.

Visual epilepsy is a reflex/photosensitive subtype within the idiopathic generalized epilepsy (IGE) spectrum — the same disease family as levetiracetam's original indication. A network meta-analysis in this pack (PMID 37378757) confirms antiseizure medication efficacy across IGE broadly, and a related meta-analysis (PMID 40450767) supports levetiracetam specifically for myoclonic seizures in IGE, a closely related reflex-adjacent phenotype.

Mechanistically, SV2A-mediated suppression of hypersynchronized cortical discharge is plausible for stimulus-triggered (visual) seizure activity, and this is indirectly supported by trials using visual stimulation paradigms — e.g., NCT04277936 and NCT04559529, which used visual scene-processing fMRI tasks to test whether levetiracetam reduces hippocampal hyperexcitability. However, no trial in this dataset directly enrolls or measures "visual epilepsy" as a defined endpoint, so this remains an extrapolation from broader IGE/reflex-epilepsy efficacy data rather than direct proof.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Levetiracetam evaluated as alternative to phenobarbital for neonatal seizures; not visual-epilepsy specific |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam for migraine prophylaxis with/without visual aura |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Tests whether levetiracetam reduces hippocampal hyperactivity via visual scene-processing fMRI task in psychosis |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Prophylactic levetiracetam to prevent seizures after intracerebral haemorrhage; different patient population |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of levetiracetam and other AEDs as first bitherapy in focal epilepsy |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | RCT of cognitive/neuropsychological effects of adjunctive levetiracetam in children with refractory partial seizures |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | fMRI study of levetiracetam's effect on hippocampal hyperactivity via visual scene-processing task in psychotic disorders |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1649 | MAST trial: AED duration/choice (including levetiracetam) for seizure prevention after traumatic brain injury |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | Gene therapy trial for Canavan disease; levetiracetam not the primary intervention, tangential relevance only |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Spotlight review confirming levetiracetam's approved indications: partial-onset seizures, and adjunctive therapy for myoclonic/GTC seizures in JME |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network Meta-analysis | J Neurol | Compares ASM efficacy/safety across idiopathic generalized epilepsies — the disease family containing visual/photosensitive epilepsy |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review | Epilepsy Behav | Levetiracetam efficacy for myoclonic seizures in IGE, a reflex-adjacent phenotype relevant to visual epilepsy |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | NEJM | General review on initial management of seizure in adults |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT | Lancet Neurol | PEACH trial: prophylactic levetiracetam vs placebo for seizure prevention after intracerebral haemorrhage |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guideline | Neurocrit Care | Clinical practice guideline on seizure prophylaxis (incl. levetiracetam) after moderate-severe TBI |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocrit Care | Levetiracetam for seizure prophylaxis in neurocritical care (ICH, TBI, SAH, post-neurosurgery) |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arq Neuropsiquiatr | Review of status epilepticus diagnosis, monitoring and treatment |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | — | Future Oncol | Levetiracetam and valproic acid as first-line antiseizure medications in glioma-related epilepsy |

## Finland Market Information

Levetiracetam is currently **not marketed in Finland** in this dataset (0 authorizations on record; Fimea query returned no results). No product-level licensing data is available.

## Safety Considerations

Please refer to the package insert for safety information. (No structured safety data — key warnings, contraindications, or DDI records — is currently available for levetiracetam in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Visual epilepsy is mechanistically plausible as an extension of levetiracetam's established IGE/reflex-epilepsy activity, but no trial or publication in this dataset directly targets this reflex subtype — evidence is indirect (L4, mechanism/adjacent-phenotype only). Critically, a **Blocking**-severity data gap (missing TFDA/Fimea package insert) currently prevents even an initial safety (S1) assessment, independent of the efficacy evidence level.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — blocking gap, required before any S1 safety review
- DrugBank-sourced mechanism of action confirmation (SV2A binding, pharmacokinetics)
- A dedicated study or registry cohort specifically enrolling patients with visual/photosensitive-triggered seizures
- Finland-specific licensing/market authorization data, since the drug is currently unmarketed there

*Note: within this evidence pack, a lower-ranked candidate — status epilepticus (rank 9, L1 evidence, "Proceed with Guardrails") — has substantially stronger direct trial support (e.g., ESETT, PEACH) and may warrant separate, higher-priority evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

