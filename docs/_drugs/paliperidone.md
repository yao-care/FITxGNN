---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Paliperidone is an atypical antipsychotic (the active metabolite of risperidone) already established for schizophrenia. The TxGNN model's top-ranked prediction for this drug is **Retinal Dystrophy with or without Extraocular Anomalies**, but this signal is supported by **0 clinical trials** and **15 publications**, none of which mention paliperidone, antipsychotics, or any related pharmacology — the evidence pack itself flags this as a likely knowledge-graph false positive rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per evidence-pack rationale; formal TFDA label text not yet available — see Data Gaps) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not yet available for paliperidone in this evidence pack (blocking data gap DG002). Based on the analysis embedded in this evidence pack, paliperidone acts as a D2/5-HT2A receptor antagonist, a class mechanism shared with other atypical antipsychotics, and its efficacy in schizophrenia is well established clinically.

However, there is **no known or plausible biological link** between this mechanism and retinal dystrophy with extraocular anomalies, which is a congenital/genetic ophthalmologic condition typically driven by developmental gene defects rather than monoamine receptor signaling. All 15 literature items returned for this pairing are ophthalmology or craniofacial-anomaly reviews and case reports — none reference paliperidone, antipsychotics, or any pharmacological intervention at all.

Given the absence of any drug-relevant literature, any clinical trials, and any mechanistic rationale, this candidate should be treated as a probable artifact of TxGNN's knowledge-graph proximity scoring rather than a substantiated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

**Note:** None of the publications below reference paliperidone or antipsychotic pharmacology — they were retrieved based on disease-term proximity only and are included for completeness/transparency.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Overview of orbital infections/cellulitis secondary to sinusitis; not drug-related |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia evaluation; not drug-related |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging differential diagnosis of congenital pediatric ocular pathologies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Review of congenital lens-shape anomalies |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Review of congenital ptosis etiology and management |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler vitreoretinal degeneration syndrome complex |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Review of ophthalmoplegia and congenital cranial dysinnervation disorders |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis/treatment approach for maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Retinal abnormalities associated with congenital fibrosis of extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia with orbital/ocular malformation |

---

## Finland Market Information

Paliperidone is currently **not marketed** in Finland — no product authorizations are on record in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** TFDA package-insert warnings/contraindications and DDI data are marked as a **blocking data gap (DG001)** — this prevents a full S1 safety pre-assessment for this drug regardless of indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction lacks any mechanistic rationale, clinical trial support, or relevant literature — it most likely reflects a TxGNN knowledge-graph artifact rather than a real signal. Separately, a blocking safety data gap (missing TFDA label/DDI data) would prevent progression even if the mechanistic case were stronger.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) and DDI data (DG001, Blocking)
- Confirmed original indication and mechanism of action from DrugBank (DG002, High)
- If further repurposing work on this drug is desired, redirect evaluation toward **treatment-refractory schizophrenia** (rank 10 in this same evidence pack), which has an L2 evidence level, a completed Phase 4 real-world study (NCT01860781), and a directly plausible mechanism — a substantially stronger candidate than the top-ranked prediction above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

