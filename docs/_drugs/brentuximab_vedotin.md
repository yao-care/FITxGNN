---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From CD30-Positive Classical Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

> Brentuximab vedotin (BV) is an anti-CD30 antibody-drug conjugate internationally approved for CD30-positive classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma, but it is **not currently marketed in Taiwan**.
> The TxGNN model predicts it may also be effective for **Follicular Lymphoma**,
> with **6 clinical trials** and **20 publications** currently supporting this direction — though most trials are small, terminated/withdrawn, or still recruiting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this dataset (`original_indications` is empty); BV is internationally approved for CD30-positive classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma, per contextual evidence in this pack |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is a data gap). Based on the clinical trial and literature evidence collected, brentuximab vedotin is an antibody-drug conjugate combining an anti-CD30 monoclonal antibody with the cytotoxic payload monomethyl auristatin E (MMAE). It binds CD30-expressing cells and delivers the microtubule-disrupting agent intracellularly, and its efficacy in CD30-positive lymphomas has been well established internationally.

Classic follicular lymphoma (FL), however, is not a canonical CD30-high tumor — CD30 expression in FL is typically low or heterogeneous, and is more reliably found in transformed or large-cell-component subsets. The repurposing rationale in this pack explicitly notes that the mechanistic link is only moderate and would require CD30 immunohistochemistry stratification to be clinically meaningful.

This is reflected in the trial landscape: several BV+rituximab/bendamustine combination studies were designed for CD30-positive B-cell lymphomas broadly (including relapsed/refractory FL as one eligible histology), but key trials were terminated or withdrawn before generating conclusive efficacy data. The one FL-specific trial (NCT04587687) is still recruiting with a small planned enrollment (n=23). Overall, the biological rationale is plausible for a CD30-selected FL subpopulation, but direct, mature evidence in unselected FL is currently limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized, open-label trial of rituximab + bendamustine ± BV for relapsed/refractory CD30-positive DLBCL after second-line failure; terminated without full efficacy readout |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Risk-stratified sequential rituximab + BV (± bendamustine) for newly diagnosed CD20+/CD30+ post-transplant lymphoproliferative disorders; withdrawn before enrollment |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | BV + pembrolizumab for recurrent systemic peripheral T-cell lymphoma; withdrawn, no enrollment |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | BV + bendamustine + rituximab for CD30-positive relapsed/refractory B-cell NHL; withdrawn, no enrollment |
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | Single-arm study of BV + bendamustine specifically in relapsed/refractory follicular lymphoma; ongoing, no results yet |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline therapy for CD30+ and/or EBV+ lymphomas; terminated, limited to CD30-positive subset |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia research reports | Reviews immunotherapy (including monoclonal antibody-based approaches) across indolent NHL subtypes including follicular lymphoma |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case report | The Gulf journal of oncology | Grade I follicular lymphoma transforming to CD30+/ALK1- anaplastic large cell lymphoma, achieving complete response to BV plus high-dose methotrexate |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | Pending classification | Hematological oncology | Overview of evolving PTCL treatment landscape, including BV-based regimens, across more than 30 disease subtypes |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Pending classification | Blood | Current/upcoming treatment approaches for common nodal PTCL subtypes, including BV combined with CHP for CD30-positive disease |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Pending classification | Blood advances | LYSA phase 2 study of BV + gemcitabine (with BV maintenance) in relapsed/refractory PTCL with ≥5% CD30 expression |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Pending classification | Hematology ASH Education Program | Discusses incorporating BV and novel agents into PTCL management |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Pending classification | European journal of haematology | BV added to ifosfamide/carboplatin/etoposide (ICE) regimen in relapsed/refractory PTCL |
| [28340875](https://pubmed.ncbi.nlm.nih.gov/28340875/) | 2017 | Pending classification | Hematology/oncology clinics of North America | Review of angioimmunoblastic T-cell lymphoma treatment landscape |
| [41409526](https://pubmed.ncbi.nlm.nih.gov/41409526/) | 2025 | Pending classification | Skin appendage disorders | Case of extensive alopecia mucinosa/follicular mucinosis responding to BV |
| [37262395](https://pubmed.ncbi.nlm.nih.gov/37262395/) | 2023 | Pending classification | ASCO Educational Book | Frontline management overview of nodal PTCL subtypes |

*Note: most of the literature evidence retrieved for this indication concerns CD30-positive T-cell lymphomas (PTCL) rather than follicular lymphoma specifically, reflecting the indirect/mechanistic nature of this signal.*

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (anti-CD30 monoclonal antibody linked to the microtubule-disrupting cytotoxic payload MMAE) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L3 (observational/indirect), and the only trial specifically designed for follicular lymphoma (NCT04587687) is small (n=23) and still recruiting with no results yet; other supporting trials were terminated or withdrawn, and most supportive literature addresses CD30-positive T-cell lymphomas rather than FL directly. Combined with the absence of TFDA safety data and the drug's non-marketed status in Taiwan, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism-of-action data from DrugBank (currently a High-severity data gap)
- CD30 immunohistochemistry stratification data in follicular lymphoma to establish which patient subset the mechanistic rationale actually applies to
- Mature results from NCT04587687 (BV + bendamustine in relapsed/refractory FL)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

