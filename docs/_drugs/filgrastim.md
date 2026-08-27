---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia/Stem Cell Mobilization to Primary Release Disorder of Platelets

## One-Sentence Summary

> Filgrastim (recombinant human G-CSF) is a hematopoietic growth factor whose established clinical use is treating chemotherapy-induced neutropenia and mobilizing peripheral blood stem cells before collection.
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but the supporting evidence is weak: of **14 clinical trials** surfaced, most are graded as *not directly relevant* (off-target stem cell transplant studies), and only **1 publication** (an observational cohort study, relevance still pending review) touches the topic.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neutropenia (chemotherapy-induced) / Peripheral blood stem cell mobilization — *based on the drug's known G-CSF mechanism described in the evidence pack's rationale field; not an officially approved Taiwan indication (see Market Status)* |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% (rank 48) |
| Evidence Level | L4 (mechanistic/indirect only — no clinical trial or study directly targets this indication) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Filgrastim is recombinant human granulocyte colony-stimulating factor (G-CSF). It acts on granulocyte precursor cells to promote proliferation and differentiation, and it mobilizes hematopoietic stem cells from the bone marrow into peripheral blood — the basis for its established uses in neutropenia management and stem cell collection prior to transplantation.

Primary release disorder of platelets (a δ-storage pool disease affecting platelet granule release) has no established pharmacological link to G-CSF signaling. The evidence pack's own mechanistic assessment is explicit on this point: there is "no known direct pharmacological mechanism" connecting filgrastim to platelet granule release function. The single related publication describes an *indirect observation* — that G-CSF mobilization in healthy stem cell donors preferentially affects lymphocyte subsets — which is not a treatment mechanism study for platelet release disorders.

In short, the high TxGNN score appears to be driven by semantic/graph clustering around "hematopoietic" and "hemorrhagic disorder" concepts rather than a validated pharmacological pathway. This is consistent with the model's other top candidates for filgrastim (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, and others), all of which the evidence pack itself flags as having **no mechanistic overlap** with G-CSF signaling and **no supporting trial or literature evidence** (Evidence Level L5, Hold recommendation for every one of them).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor stem cell transplant for hematologic malignancies — *not relevant* (grade C: population and endpoint are hematologic cancer, not platelet release disorder) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic stem cell transplant in pediatric sarcomas — *not relevant* (grade C) |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant for myeloid leukemia — *not relevant* (grade C) |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity stem cell transplant for GATA2 mutation patients — relevance not yet graded |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs unselected autologous transplant in lymphoma — *not relevant* (grade C) |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Post-transplant cyclophosphamide dosing for GVHD prophylaxis — *not relevant* (grade C) |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved unrelated donor bone marrow transplant — relevance not yet graded |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Autologous stem cell transplant for severe lupus (SLE) — relevance not yet graded |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile for COVID-19 cytokine release syndrome — relevance not yet graded |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Post-transplant cyclophosphamide GVHD prophylaxis platform trial — relevance not yet graded |

*Note: 4 additional trials were returned but omitted for brevity; none were graded as directly relevant to this indication. Across all 14 trials retrieved, none study filgrastim as a treatment for a platelet release disorder — all involve hematopoietic stem cell transplantation for unrelated hematologic malignancies or autoimmune disease.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort/Observational | Frontiers in Immunology | G-CSF mobilization in healthy stem cell donors preferentially mobilizes lymphocyte subsets; an indirect immunological observation, not a study of platelet release function or treatment efficacy (relevance grading still pending) |

---

## Taiwan Market Information

Filgrastim is **not currently marketed in Taiwan** — no authorization records are available in the evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this evidence pack — including a Blocking-severity gap on the TFDA package insert, which prevents a preliminary safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between G-CSF signaling and platelet release/granule disorders is unestablished — the evidence pack's own rationale states there is no known direct pharmacology connecting the two. No clinical trial or publication actually studies filgrastim for this indication; the trials retrieved are almost entirely off-target hematopoietic stem cell transplant studies, and the single literature hit is an indirect observational finding. This same weak-evidence pattern (Evidence Level L5, Hold) applies to all nine other TxGNN-predicted indications for filgrastim in this pack (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, C1 inhibitor deficiency, and others), none of which have any supporting trial or literature evidence at all.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking data gap — required before any S1 safety review can begin)
- Mechanism of action documentation (High-severity data gap — needed to properly evaluate mechanistic plausibility)
- A dedicated preclinical or mechanistic study directly linking G-CSF/granulocyte pathways to platelet granule release function
- If pursued, a hematology/coagulation specialist review of biological plausibility before any trial design work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

