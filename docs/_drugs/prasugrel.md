---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Antiplatelet Therapy (ACS/PCI) to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine-class P2Y12 receptor antagonist established as antiplatelet therapy following acute coronary syndrome and percutaneous coronary intervention (per the literature context in this evidence pack). The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but currently only **2 clinical trials** and **2 publications** are on file, and none directly test prasugrel in this indication — the signal remains at the mechanistic-hypothesis stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Finland licenses on file); literature context points to antiplatelet use in ACS/PCI |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for prasugrel. Based on known information within this evidence pack, prasugrel is a thienopyridine-class P2Y12 receptor antagonist (antiplatelet drug) in the same family as clopidogrel; its efficacy in acute coronary syndrome/PCI settings is well established in the literature, and mechanistically this class may be applicable to other vascular/thrombotic conditions.

The proposed link to pulmonary hypertension rests on a single hypothesis: in chronic thromboembolic pulmonary hypertension (CTEPH), a subtype of pulmonary hypertension, anticoagulant therapy is standard adjunctive care, so an antiplatelet agent might plausibly play an analogous thrombo-preventive role. However, this is a class-level, indirect inference — no direct evidence currently supports prasugrel's use for pulmonary hypertension itself.

Both retrieved clinical trials were graded **relevance C** (low relevance) by the evidence review: one is an observational NOAC-management study in elderly atrial fibrillation patients, the other a retrospective eligibility analysis for cancer-associated thrombosis. Neither involves prasugrel or pulmonary hypertension directly. Similarly, the two literature items provide only background context (a COVID-19 comorbidity registry, and a clopidogrel/prasugrel adherence study in ACS/PCI patients) rather than direct evidence for this indication. This is why the evidence level is capped at L4 (mechanism-level reasoning only) despite the high TxGNN score.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational cross-sectional study of NOAC management in elderly non-valvular AF patients in Spain; no direct link to prasugrel or pulmonary hypertension (relevance grade C — background noise) |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on eligibility for the CARAVAGGIO cancer-associated thrombosis trial; no direct link to prasugrel or pulmonary hypertension (relevance grade C — background noise) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Evaluates factors associated with clopidogrel/prasugrel use and adherence after PCI in ACS patients — confirms prasugrel's established antiplatelet role in ACS, but not related to pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort/Observational | Kardiologiia | ACTIV SARS-CoV-2 registry analysis of background comorbidity therapy on COVID-19 outcomes; not specific to prasugrel or pulmonary hypertension |

## Finland Market Information

Prasugrel currently has no marketing authorizations on file in Finland (0 authorizations; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available evidence — two clinical trials (both graded low relevance) and two publications (neither addressing prasugrel in pulmonary hypertension) — does not support a direct or even strong indirect signal. The proposed mechanism (antiplatelet effect analogous to anticoagulation in CTEPH) is plausible but unverified, and core drug data (MOA, package insert warnings/contraindications) are also missing.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (blocking gap: warnings/contraindications, DG001)
- DrugBank mechanism of action data (DG002)
- Preclinical or mechanistic studies evaluating P2Y12 inhibition specifically in pulmonary vascular remodeling or CTEPH
- Dedicated clinical trials or case series testing prasugrel in pulmonary hypertension populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

