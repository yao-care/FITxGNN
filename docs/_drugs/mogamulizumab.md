---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mogamulizumab: From Adult T-Cell Leukemia/Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab is an anti-CCR4 monoclonal antibody currently used for adult T-cell leukemia/lymphoma and mycosis fungoides/Sézary syndrome (per the evidence pack's mechanistic rationale; not independently confirmed via Finland licensing data).
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, but this ranking is based **purely on the model's score** — **0 clinical trials** and **0 publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adult T-cell leukemia/lymphoma; Mycosis fungoides/Sézary syndrome (per repurposing rationale text; no structured license record available) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (marked as a data gap). Based on the repurposing rationale provided, mogamulizumab is an anti-CCR4 monoclonal antibody, and its efficacy in adult T-cell leukemia/lymphoma and mycosis fungoides/Sézary syndrome has been established. CCR4 is expressed on regulatory T cells (Tregs), and mogamulizumab's mechanism involves depleting CCR4-positive Tregs to enhance anti-tumor immunity.

The theoretical link to prostatic urethra urothelial carcinoma rests on the observation that CCR4-positive Treg infiltration has been described in some urothelial tumor microenvironments — depleting these Tregs could, in principle, relieve local immunosuppression and enhance anti-tumor immune response. However, this connection is a mechanistic hypothesis derived solely from the TxGNN embedding space; it is not supported by any preclinical, translational, or clinical data specific to urothelial carcinoma.

Given the complete absence of clinical trials or literature (see below), this prediction should be treated as a hypothesis-generating signal rather than an actionable repurposing candidate at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Mogamulizumab is not currently marketed in Finland (0 authorizations on record), so no product/license details are available.

## Cytotoxicity

Mogamulizumab is an antineoplastic agent (indicated for T-cell leukemia/lymphoma).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CCR4 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Retrieval of the Finland package insert / warning label (a blocking data gap, DG001) has not yet been completed, so no safety review (S1 stage) can be performed until this is resolved.*

## Additional Candidates Identified by TxGNN

The model flagged six further low-confidence candidates in the same score band (99.15–99.42%), all similarly lacking clinical or literature support and all scored L5/Hold: kidney pelvis sarcomatoid transitional cell carcinoma, infiltrating bladder urothelial carcinoma (sarcomatoid variant), renal pelvis papillary urothelial carcinoma, human herpesvirus 8-related tumor, ectomesenchymoma, and malignant cutaneous granular cell skin tumor. None currently warrant individual evaluation beyond the top-ranked candidate above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature evidence for any of the seven predicted indications, and the mechanistic rationale is theoretical only. In addition, the Finland package insert/warning data (blocking gap) has not been retrieved, so the candidate cannot yet even enter safety pre-screening (S1).

**To proceed, the following is needed:**
- Finland (Fimea) package insert warnings/contraindications (DG001, blocking)
- Confirmed mechanism of action detail from DrugBank or primary literature (DG002)
- Preclinical or translational evidence for CCR4/Treg involvement specifically in urothelial carcinoma
- Any emerging clinical trial or case report data before this candidate is reconsidered beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

