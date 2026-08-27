---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 1
---

# Decitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Decitabine: From Myelodysplastic Syndrome to Refractory Cytopenia of Childhood

> **Note on original indication**: The evidence pack contains no `original_indications`, `original_moa`, or Finland licensing data for decitabine (drug not marketed in Finland, 0 authorizations). The original-indication context below (MDS/AML, DNA hypomethylating agent) reflects decitabine's well-established international drug identity, not a sourced field from this evidence pack — flagged here for transparency rather than presented as verified data.

## One-Sentence Summary

Decitabine is a DNA hypomethylating agent internationally used for myelodysplastic syndrome (MDS) and acute myeloid leukemia in adults, but it is not currently marketed in Finland and no TFDA/local package-insert safety data is available. The TxGNN model predicts it may be effective for **Refractory Cytopenia of Childhood** (a pediatric MDS subtype), with a TxGNN score of **99.03%**, currently supported by **0 clinical trials** and **1 publication**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in evidence pack (no licenses on file); decitabine is internationally known as an MDS/AML hypomethylating agent |
| Predicted New Indication | Refractory Cytopenia of Childhood |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 (single retrospective observational study, no RCTs) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as data gap DG002). Based on generally known pharmacology, decitabine is a DNA methyltransferase inhibitor (hypomethylating agent) whose efficacy in adult myelodysplastic syndrome and AML is well established internationally, though this has not been independently confirmed via the sourced evidence pack for this drug.

Refractory cytopenia of childhood is classified as a pediatric subtype of myelodysplastic syndrome, sharing the same underlying clonal bone marrow pathology as adult MDS. Mechanistically, a hypomethylating agent effective in adult MDS would be expected to have biological plausibility in a pediatric MDS variant, which is consistent with the direction of the TxGNN prediction.

This mechanistic plausibility is further supported by the one available literature record: a single-center retrospective study of decitabine combined with a minimally myelosuppressive regimen, used as a bridge to allogeneic HSCT in pediatric MDS patients — a clinical population that overlaps with refractory cytopenia of childhood.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Retrospective cohort study | BMC Pediatrics | Single-center 10-year experience using decitabine combined with a minimally myelosuppressive regimen (DAC + MMR) as a bridge to allogeneic HSCT in pediatric MDS; reports on outcomes of this approach prior to transplant. |

## Finland Market Information

Decitabine is not currently marketed in Finland; no authorization records are available.

## Cytotoxicity

Decitabine is an antineoplastic agent (DNA hypomethylating agent / antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (hypomethylating agent / antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/local package insert data is currently unavailable — flagged as a **Blocking** data gap, DG001, which prevents completion of the S1 safety pre-assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is supported by only a single observational (non-RCT) publication and zero registered clinical trials for this specific indication, and a Blocking safety data gap (no package-insert warnings/contraindications) currently prevents even an initial safety assessment.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (resolves DG001, Blocking)
- Verified mechanism of action data from DrugBank (resolves DG002)
- Confirmation of decitabine's original approved indication(s) and licensing status from a sourced regulatory database
- Any additional clinical trials or controlled studies specifically evaluating decitabine in refractory cytopenia of childhood / pediatric MDS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

