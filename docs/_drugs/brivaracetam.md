---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: From Focal-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Brivaracetam (BRV) is a high-affinity SV2A ligand used as adjunctive and monotherapy treatment for focal-onset epilepsy. TxGNN predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex epilepsy subtype), with a **99.51% prediction score**, but this direction is currently supported only by mechanistic and general-epilepsy literature (**19 publications**) — no disease-specific clinical trials exist yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal-onset (partial-onset) seizures in epilepsy — adjunctive and monotherapy (per literature evidence; no formal regulatory license record in this pack) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (data pack labels this a "Research Question", decision stage S1) |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data (DrugBank field) is not available for this candidate. However, the supporting literature consistently describes brivaracetam as a high-affinity, highly selective ligand for synaptic vesicle protein 2A (SV2A) — the same target as levetiracetam, but bound with 15- to 30-fold greater affinity and faster brain penetration (PMID 38811492, PMID 40568060). SV2A modulates presynaptic neurotransmitter vesicle release, and by binding this target BRV reduces neuronal hyperexcitability broadly across seizure types.

Visual (photosensitive) epilepsy is a reflex epilepsy subtype in which seizures are triggered by intermittent photic stimulation (IPS), producing an epileptiform EEG response (photoparoxysmal response, PPR). Because SV2A modulation is a broad-spectrum antiseizure mechanism rather than one specific to a single trigger type, it is mechanistically plausible that BRV's efficacy could extend from general focal-onset epilepsy to this photosensitive subtype.

This is not purely speculative: the literature includes a validated proof-of-concept surrogate — the human phase IIa "photosensitivity model." A randomized, double-blind, crossover trial (PMID 32949370, tier 1) directly compared BRV against levetiracetam on speed of PPR elimination in photosensitive epilepsy patients, and earlier work (PMID 17785672) established BRV's activity in this same model. These studies support biological plausibility, but they used an EEG surrogate endpoint in general photosensitive-epilepsy patients rather than a clinical trial specifically diagnosing and treating "visual epilepsy" as a distinct indication — hence the L3 (mechanism/model-based) evidence rating rather than a higher tier.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic Review/Meta-analysis | Frontiers in Neurology | Safety and efficacy of BRV in children with epilepsy |
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | Phase III RCT | Epilepsia Open | Adjunctive BRV efficacy, safety, and tolerability in adult Asian patients with uncontrolled focal-onset seizures |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Narrative Review | Advances in Therapy | Preclinical profile and clinical benefits of BRV; 15–30× higher SV2A affinity than levetiracetam |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Review | Journal of Epilepsy Research | Pharmacology, clinical efficacy, and safety of BRV across age groups, adjunctive and monotherapy use |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Review | Expert Review of Neurotherapeutics | BRV efficacy and safety in focal epilepsy; comparison with levetiracetam |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled Safety Analysis | Epilepsy & Behavior | In-depth pooled safety/tolerability analysis of adjunctive BRV across trials |
| [40069539](https://pubmed.ncbi.nlm.nih.gov/40069539/) | 2025 | Network Study | Neurology and Therapy | Effectiveness of BRV in people with epilepsy and intellectual disability (BRIVAFIRST network) |
| [32157673](https://pubmed.ncbi.nlm.nih.gov/32157673/) | 2021 | Observational | Acta Neurologica Belgica | Efficacy and tolerability of BRV in patients with intellectual disability and epilepsy |
| [38205459](https://pubmed.ncbi.nlm.nih.gov/38205459/) | 2023 | Prospective Non-Interventional Study | Cureus | Real-world efficacy and safety of BRV via selective SV2A binding |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review (general MOA) | Neuropharmacology | Mechanisms of action of currently used antiseizure drugs, including SV2A-targeting agents |

---

## Finland Market Information

Brivaracetam currently has **no marketing authorizations** on record in this data pack (market status: Not Marketed, 0 authorizations). No product/dosage-form information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a strong TxGNN score and plausible SV2A mechanism, reinforced by validated photosensitivity-model surrogate data, but there are no clinical trials or literature diagnosing and treating "visual epilepsy" as a distinct indication — this keeps the evidence at L3 / decision stage S1 ("Research Question").

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety pre-assessment)
- Structured DrugBank MOA confirmation
- A disease-specific clinical study (or registry) enrolling patients with photosensitive/visual epilepsy, not just general focal-onset epilepsy

**Note:** Within this same evidence pack, the rank-2 candidate **status epilepticus** (score 99.40%) has materially stronger support — an L2 evidence level with 2 clinical trials (including a completed, high-relevance IV brivaracetam vs. levetiracetam pediatric trial) and a "Proceed with Guardrails" recommendation. If prioritizing near-term repurposing value, that indication warrants separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

