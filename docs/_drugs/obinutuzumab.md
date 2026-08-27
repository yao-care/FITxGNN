---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Obinutuzumab: From CD20+ B-Cell Malignancy to Follicular Lymphoma

## One-Sentence Summary

Obinutuzumab is a glycoengineered anti-CD20 monoclonal antibody already used against CD20-positive B-cell blood cancers, including chronic lymphocytic leukemia (CLL). The TxGNN model's top actionable prediction extends this activity to **Follicular Lymphoma (FL)**, a closely related B-cell malignancy, and this direction is backed by **50 clinical trials** (including the pivotal Phase 3 GALLIUM trial) and **20 publications**. The model separately flags two ultra-specific CLL/SLL molecular subtypes with near-identical scores but zero supporting trials or literature in this dataset — likely an ontology-granularity artifact rather than a genuinely unsupported signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Finland (drug is unmarketed there; `taiwan_regulatory.licenses` is empty). Trial records in this evidence pack describe obinutuzumab as already approved elsewhere in combination regimens for CLL and, later, FL. |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on other predictions:** TxGNN also ranked two molecularly-defined CLL/SLL subtypes ("pregerminal center CLL/SLL" and "CLL/SLL with IGHV somatic hypermutation") at essentially the same score (~99.2%), but no clinical trials or literature were retrieved for either — evidence level L5, decision stage S0, recommendation Hold. These are treated here as low-priority signals warranting no independent action until better-resolved disease terms allow evidence linkage.

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for obinutuzumab is flagged as a data gap (DG002, High severity) in this evidence pack. However, the trial and rationale records that were retrieved consistently describe obinutuzumab as a third-generation, glycoengineered type II anti-CD20 IgG1 monoclonal antibody that produces enhanced antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct B-cell killing compared with rituximab.

Follicular lymphoma, like CLL/SLL, is a CD20-positive B-cell malignancy, so the molecular target obinutuzumab engages is directly expressed on the tumor cells in both diseases. This is not a distant repurposing leap across unrelated organ systems — it reflects the drug's existing mechanistic footprint in indolent B-cell lymphoproliferative disease being extended from one CD20+ malignancy to another.

This mechanistic plausibility is strongly corroborated by real-world development: obinutuzumab (via multiple trial records in this pack, e.g. NCT02877550) is already described as approved in combination with chlorambucil for untreated CLL and in combination with bendamustine for FL. The TxGNN prediction for FL therefore aligns with an indication space the drug has already been extensively studied and, in some markets, approved for — which explains the unusually mature L1 evidence base compared to a typical de novo repurposing candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Completed | 1401 | GALLIUM trial: obinutuzumab + chemotherapy vs. rituximab + chemotherapy in untreated advanced indolent NHL, with obinutuzumab or rituximab maintenance in responders — pivotal direct-comparison evidence. |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Completed | 413 | Bendamustine alone vs. bendamustine + obinutuzumab (GA101) in rituximab-refractory indolent NHL, with obinutuzumab maintenance. |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL. |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Safety of obinutuzumab given as a short-duration (90-minute) infusion from cycle 2 onward, combined with chemotherapy, in untreated advanced FL. |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | Completed | 133 | Obinutuzumab + polatuzumab vedotin + venetoclax in relapsed/refractory FL. |
| [NCT02600897](https://clinicaltrials.gov/study/NCT02600897) | Phase 1/2 | Completed | 114 | Obinutuzumab + polatuzumab vedotin + lenalidomide in relapsed/refractory FL. |
| [NCT03113422](https://clinicaltrials.gov/study/NCT03113422) | Phase 2 | Completed | 56 | Venetoclax + obinutuzumab + bendamustine as front-line therapy in high tumor burden FL. |
| [NCT04034056](https://clinicaltrials.gov/study/NCT04034056) | N/A (observational) | Completed | 299 | Non-interventional, retrospective/prospective real-world study of obinutuzumab effectiveness and safety in previously untreated advanced FL. |
| [NCT05783596](https://clinicaltrials.gov/study/NCT05783596) | Phase 2 | Active, not recruiting | 47 | Glofitamab + obinutuzumab for first-line treatment of FL and marginal zone lymphoma. |
| [NCT05058404](https://clinicaltrials.gov/study/NCT05058404) | Phase 3 | Active, not recruiting | 605 | FIL_FOLL19: shortened vs. standard chemo-immunotherapy for initial treatment of high tumor burden FL. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | Primary GALLIUM report: obinutuzumab-based chemoimmunotherapy compared with rituximab-based chemoimmunotherapy in previously untreated advanced FL. |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM sub-analysis showing obinutuzumab significantly prolonged progression-free survival vs. rituximab across CHOP/CVP/bendamustine chemotherapy backbones. |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL. |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT (final analysis) | HemaSphere | Final GALLIUM results confirming durable PFS benefit of obinutuzumab- vs. rituximab-based immunochemotherapy in untreated FL. |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN: obinutuzumab + lenalidomide in relapsed/refractory follicular B-cell lymphoma, single-arm Phase 2. |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Cohort | Haematologica | Phase Ib/II GO29365: polatuzumab vedotin + bendamustine + rituximab or obinutuzumab in relapsed/refractory FL. |
| [40355425](https://pubmed.ncbi.nlm.nih.gov/40355425/) | 2025 | Phase 2 trial | Blood Cancer Journal | PrE0403: intermittent-dose venetoclax added to bendamustine + obinutuzumab as front-line therapy in high-risk FL. |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood and Lymphatic Cancer: Targets and Therapy | Review of obinutuzumab alone and in combination for FL, covering mechanism and combination rationale. |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish Journal of Haematology | Comprehensive review of FL staging, prognosis, and current/emerging treatment options including obinutuzumab-based regimens. |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Review of obinutuzumab in rituximab-refractory/relapsed FL, including GADOLIN trial data. |

## Finland Market Information

Obinutuzumab currently holds no marketing authorization in Finland (`market_status`: not marketed; `total_licenses`: 0). No product, dosage form, or approved-indication data is available to report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — glycoengineered anti-CD20 monoclonal antibody (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — notably DG001, a Blocking-severity gap on TFDA-equivalent label warnings/contraindications.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The follicular lymphoma prediction is supported by L1-level evidence — most notably the completed Phase 3 GALLIUM trial (n=1401) and its final published analysis — and is mechanistically consistent with obinutuzumab's known anti-CD20 activity in CD20+ B-cell malignancies. However, two Blocking/High-severity data gaps (TFDA-equivalent safety labeling, and formal MOA documentation) must be closed before this can advance past initial safety screening.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (DG001, Blocking)
- Formal documented mechanism of action (DG002, High)
- Confirmation of Finland/Taiwan market authorization pathway, since obinutuzumab currently has zero licenses on file
- Route-compatibility and dosing-regimen assessment (currently marked "pending" in the evidence pack)
- Re-query of the two CLL/SLL molecular-subtype predictions under broader/parent disease terms to determine whether the current zero-evidence result is a true gap or an ontology-matching artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

