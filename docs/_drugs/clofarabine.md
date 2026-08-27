---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a second-generation purine nucleoside analog originally developed and FDA-approved for relapsed/refractory acute lymphoblastic leukemia (ALL) in pediatric patients (this approval history is documented within the trial records in this evidence pack, as Taiwan/Finland regulatory licensing data is unavailable). The TxGNN model predicts it may also be effective for **Myeloid Leukemia**, with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory acute lymphoblastic leukemia (ALL) in pediatric patients (FDA-approved; per clinical trial records — no Finland/Taiwan regulatory license on file) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed regulatory-grade mechanism of action data is not yet available (DrugBank query pending confirmation). Based on the mechanistic rationale captured in this evidence pack, clofarabine is a second-generation purine (deoxyadenosine) nucleoside analog that inhibits DNA polymerase α/ε and ribonucleotide reductase, depleting the intracellular deoxynucleotide pool and triggering the mitochondrial apoptosis pathway. This gives it direct cytotoxic activity against rapidly dividing cells — a mechanism well suited to hematologic malignancies with high proliferative fractions.

Clofarabine's original approved indication, pediatric relapsed/refractory ALL, and the predicted new indication, myeloid leukemia (AML/CML), are both hematologic malignancies driven by highly proliferative blast populations in the bone marrow. Because the drug's antileukemic mechanism is not lineage-restricted (it targets DNA synthesis machinery common to both lymphoid and myeloid blasts), extensive off-label and investigational use in adult and pediatric AML has already accumulated over two decades, including single-agent Phase II studies and multiple combination regimens (clofarabine + cytarabine, + idarubicin, + busulfan-based transplant conditioning). This existing body of AML-directed research is the mechanistic and clinical bridge supporting the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01423175](https://clinicaltrials.gov/study/NCT01423175) | Phase 2 | Unknown | 60 | Randomized comparison of ClAraC (clofarabine + Ara-C) vs. FLAMSA conditioning in high-risk AML/advanced MDS prior to allogeneic SCT |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | Completed | 65 | Decitabine followed by clofarabine + idarubicin + cytarabine (CIA) in acute leukemia; dose-finding and disease control |
| [NCT00044889](https://clinicaltrials.gov/study/NCT00044889) | Phase 2 | Completed | 40 | Single-arm, open-label clofarabine monotherapy in adult refractory/relapsed AML |
| [NCT00852709](https://clinicaltrials.gov/study/NCT00852709) | Phase 1 | Terminated | 35 | Dose-escalation of clofarabine followed by fractionated cyclophosphamide in relapsed/refractory pediatric acute leukemias |
| [NCT00908167](https://clinicaltrials.gov/study/NCT00908167) | Phase 1 | Completed | 44 | Sorafenib sequenced with cytarabine and clofarabine in relapsed/refractory AML, APL, ALL and infantile leukemia |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Large treatment-development program for older AML/high-risk MDS patients, incorporating clofarabine-containing arms |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | Completed | 735 | Randomized CLARA (clofarabine/intermediate-dose cytarabine) vs. high-dose cytarabine as AML consolidation in younger patients |
| [NCT02665065](https://clinicaltrials.gov/study/NCT02665065) | Phase 3 | Active, not recruiting | 153 | Iomab-B plus reduced-intensity conditioning (clofarabine-containing regimens common in this population) vs. conventional care in relapsed/refractory AML |
| [NCT00373529](https://clinicaltrials.gov/study/NCT00373529) | Phase 2 | Completed | 116 | Single-agent clofarabine in previously untreated older AML patients unlikely to benefit from intensive induction |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine-based salvage therapy in relapsed/refractory AML as a bridge to allogeneic HCT |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | Phase III RCT | J Clin Oncol | AML08 multicenter randomized trial: clofarabine can replace anthracyclines/etoposide in remission induction for childhood AML |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 Cohort | Cancer Medicine | Clofarabine + cytarabine + mitoxantrone (CLAM) in refractory/relapsed AML: high response rates, effective bridge to allo-HCT |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort | Transplant Cell Ther | Clofarabine + busulfan myeloablative conditioning for allogeneic HCT in active myeloid malignancies |
| [27621503](https://pubmed.ncbi.nlm.nih.gov/27621503/) | 2015 | Review/Cohort | Hospital Pharmacy | Practical review of clofarabine + cytarabine regimen preparation and administration for AML |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Review | Lancet Oncology | Summary of clofarabine and cytarabine combination data in AML |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Role of clofarabine in adult AML across monotherapy and combination strategies |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | Clofarabine's mechanism (ribonucleotide reductase/DNA polymerase inhibition) and role in AML |
| [23526416](https://pubmed.ncbi.nlm.nih.gov/23526416/) | 2013 | Review | Am J Hematol | AML risk-stratification and management update, contextualizing nucleoside-analog therapy |
| [18433953](https://pubmed.ncbi.nlm.nih.gov/18433953/) | 2008 | Review | Blood Reviews | Conventional and novel treatment approaches for AML in the elderly |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Review | Leukemia & Lymphoma | "Clofarabine: past, present, and future" — mechanism and development history in leukemia |

---

## Finland Market Information

Clofarabine is currently **not marketed in Finland** (0 marketing authorizations on file). No product listings are available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | High — nucleoside analogs that inhibit DNA synthesis are expected to cause profound myelosuppression (neutropenia, thrombocytopenia, anemia); drug-specific incidence figures are pending package-insert confirmation |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, signs of infection |
| Handling Protection | Must follow institutional cytotoxic drug handling and disposal regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — TFDA package insert retrieval is a blocking data gap for this candidate.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clofarabine's mechanism of action against high-proliferation blast cells, combined with a substantial body of Phase I–III clinical evidence in AML (including a randomized Phase III pediatric trial and a large randomized Phase II consolidation study), supports an L2 evidence level for the myeloid leukemia indication. However, the drug is not currently marketed in Finland and core safety documentation is missing.

**To proceed, the following is needed:**
- TFDA/EMA package insert with warnings, precautions, and contraindications (blocking gap — DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Formal drug-drug interaction (DDI) review, currently unresolved (query status: not found)
- Route-of-administration compatibility assessment between required IV administration and any future local formulation
- Regulatory pathway evaluation given the current "not marketed" status in Finland
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

