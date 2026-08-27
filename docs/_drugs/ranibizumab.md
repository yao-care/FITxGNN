---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

Using the report-writing instructions in the prompt directly (no additional skill applies — this is a templated document-generation task, not code/data/diagram work).

# Ranibizumab: From Neovascular Age-Related Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Ranibizumab is an anti-VEGF monoclonal antibody fragment originally used for neovascular (wet) age-related macular degeneration and related retinal vascular diseases.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> with **6 clinical trials** (including 3 completed Phase 3 RCTs) and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (`original_indications` empty, `original_moa` = Data Gap). Publicly known original indication: neovascular AMD and related retinal vascular disease |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate is not available in the evidence pack (DG002, High severity). Based on known pharmacology, ranibizumab is part of the anti-VEGF (vascular endothelial growth factor inhibitor) class of biologics — a humanized monoclonal antibody Fab fragment that binds and neutralizes VEGF-A. Its efficacy in neovascular retinal disease is well established, and mechanistically it is directly applicable to diabetic retinopathy.

Diabetic retinopathy and the diseases ranibizumab was originally developed for (wet AMD, diabetic macular edema) share a common pathophysiological driver: pathological VEGF-mediated neovascularization and vascular permeability in the retina. Progression to severe nonproliferative and proliferative diabetic retinopathy is closely tied to rising intraocular VEGF levels, which is exactly the target ranibizumab neutralizes.

Notably, the clinical trial and literature evidence retrieved for this candidate is unusually extensive for a "predicted" indication — including multiple completed Phase 3 RCTs and a 2025 JAMA Ophthalmology trial (Pavilion). This suggests TxGNN is here reproducing a mechanistically sound and largely clinically validated relationship rather than a purely novel hypothesis, which strengthens confidence in the prediction even though formal MOA/indication fields are missing from this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | Compared laser alone, laser + triamcinolone, laser + ranibizumab, and ranibizumab alone for diabetic macular edema |
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Completed | 174 | Port Delivery System with ranibizumab vs comparator in diabetic retinopathy without center-involved DME |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | Intravitreal anti-VEGF for prevention of vision-threatening DR in high-risk eyes |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Intravitreous ranibizumab vs sham injection for prevention of high-risk DR |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Intravitreal ranibizumab for macular edema with NPDR; effects on microaneurysm turnover and non-perfused retinal area |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observational study of anti-VEGF therapy (ranibizumab, aflibercept, conbercept) in AMD, PDR, macular edema, and CNV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: Port Delivery System with ranibizumab vs monitoring in NPDR without macular edema |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Meta-Analysis | Ophthalmology Retina | Baseline DR severity and time to DME resolution with ranibizumab across Phase 3 trials |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic Review | Health Technology Assessment | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic Review | Health Technology Assessment | Anti-VEGF vs laser photocoagulation for DR — systematic review and economic analysis |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post-hoc Analysis | Clinical Ophthalmology | Predictors of early DR regression with ranibizumab in RIDE/RISE trials |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Observational Study | JAMA Ophthalmology | Retinal nonperfusion characteristics in severe NPDR and PDR on ultra-widefield angiography |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Overview of ranibizumab for the treatment of diabetic retinopathy |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Review | Journal of Diabetes and its Complications | Advances in the treatment of diabetic retinopathy; VEGF-A as key driver of progression |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Modeling Study | BMJ Open Ophthalmology | Simulation of long-term impact of intravitreal anti-VEGF therapy on severe NPDR |
| [40466685](https://pubmed.ncbi.nlm.nih.gov/40466685/) | 2025 | Clinical Observational Study | Georgian Medical News | Anti-VEGF combined with panretinal photocoagulation in diabetic retinopathy |

---

## Finland Market Information

Ranibizumab is currently **not marketed** in Finland per this evidence pack (`market_status`: 未上市, `total_licenses`: 0). No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: this evidence pack flags a Blocking-severity data gap (DG001) — the TFDA/product-label warnings and contraindications could not be retrieved, which per the internal pipeline definition prevents entry into the S1 safety initial assessment. Drug interaction data query also returned no results (`not_found`).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence is strong (L1: 3 completed Phase 3 RCTs plus extensive supporting literature), and the VEGF-driven mechanistic link between the original indication and severe NPDR is sound.
- However, a Blocking-severity data gap (DG001: missing TFDA package insert / warnings / contraindications) prevents completion of the initial safety assessment, and the drug is not currently marketed in Finland (0 authorizations).

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the S1 safety gate (DG001)
- Formal mechanism of action documentation from DrugBank (DG002)
- Drug interaction (DDI) data, as the current query returned no results
- Regulatory pathway assessment for Finland market entry, given zero existing local authorizations
- Formal classification (study type / tier / relevance) of the currently "pending" clinical trial and literature records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

