---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 3
---

# Temsirolimus
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

# Temsirolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Temsirolimus (Torisel) is an mTOR inhibitor originally approved for renal cell carcinoma. The TxGNN model predicts it may be effective for **Liposarcoma**, with **5 clinical trials** (two using temsirolimus itself) and **1 literature review** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (per repurposing rationale; no local license record — see Market Status) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The `original_moa` field for temsirolimus is flagged as a data gap in this evidence pack (DG002 — High severity). However, the repurposing rationale attached to the prediction supplies mechanistic detail: temsirolimus is a prodrug of sirolimus, and after CYP3A4-mediated metabolic activation it binds FKBP12 to inhibit mTORC1, blocking the PI3K/AKT/mTOR signaling pathway.

Liposarcoma — particularly the dedifferentiated subtype — frequently shows activation of this same pathway along with MDM2/CDK4 co-amplification, giving a clear mechanistic rationale for extending temsirolimus beyond its approved indication of renal cell carcinoma, another tumor type driven by mTOR pathway dysregulation.

This mechanistic continuity is reinforced by direct clinical evidence: temsirolimus itself (as Torisel) has already been tested in combination regimens for advanced soft-tissue and bone sarcomas, including liposarcoma subtypes, and other mTOR-pathway inhibitors (sirolimus, ridaforolimus, everolimus) have been studied in the same disease space, forming a broader class-level evidence base.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) + liposomal doxorubicin in recurrent sarcoma (incl. liposarcoma); dose-finding and efficacy assessment. Direct evidence for temsirolimus. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Temsirolimus + cixutumumab in pediatric recurrent/refractory sarcoma. Direct evidence for temsirolimus, but population limited to pediatrics. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma. Same-class (mTOR inhibitor) evidence. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (another mTOR inhibitor) in advanced sarcoma; large sample size, same-class evidence. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (mTOR inhibitor) in advanced dedifferentiated liposarcoma and leiomyosarcoma. Same-class evidence, ongoing. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Review of targeted treatments for rare connective tissue tumors and sarcomas, classifying molecular subgroups relevant to targeted therapy selection. |

## Finland Market Information

Temsirolimus is not currently marketed in Finland — 0 authorizations are on record in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (Local package insert warnings/contraindications and DDI data are not yet available — flagged as a **Blocking** data gap, DG001.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temsirolimus itself has completed Phase 1/2 clinical evidence in sarcoma (including liposarcoma), reinforced by a coherent mTOR-pathway mechanistic rationale and supportive same-class trial data. However, the drug is not currently marketed in Finland and key safety/regulatory data are missing, so guardrails are needed before advancing further.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (Blocking gap, DG001)
- Detailed mechanism of action documentation from DrugBank (High-priority gap, DG002)
- Local market authorization or import pathway assessment, since the product is not currently marketed
- Drug-drug interaction data (none found in current query)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

