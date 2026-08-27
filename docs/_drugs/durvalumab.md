---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: An Anti-PD-L1 Checkpoint Inhibitor — Predicted New Indication: Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 monoclonal antibody (immune checkpoint inhibitor); this evidence pack does not document its original approved indication or detailed mechanism of action data, and the drug is currently not marketed in Finland.
The TxGNN model's top-ranked prediction is **Prostatic Urethra Urothelial Carcinoma** (score 99.98%), but this specific prediction is currently supported by **no clinical trials and no literature** — it is a model-only hypothesis.
Note: among the 10 candidates in this pack, two other urothelial/gynecologic-carcinoma indications (ranks 3 and 6) do have supporting trial and/or literature evidence — see the Conclusion for details.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty; Finland has 0 licenses on file) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for durvalumab in this evidence pack (flagged as a High-severity data gap). Based on information present in the supporting rationale fields, durvalumab is an **anti-PD-L1 monoclonal antibody** that works by blocking the PD-1/PD-L1 checkpoint pathway, restoring T-cell mediated anti-tumor immune activity — a mechanism already established as a therapeutic strategy across several urothelial and immunogenic tumor types represented elsewhere in this same prediction set.

Prostatic urethra urothelial carcinoma shares tissue origin with bladder and renal pelvis urothelial carcinoma — both part of the broader urothelial carcinoma family. The rationale for this specific prediction is a mechanistic extrapolation: because PD-L1 checkpoint blockade has known biological relevance in urothelial carcinoma generally, the model infers the same may hold for the prostatic urethra subtype.

However, this extrapolation is **not yet backed by any disease-specific trial or publication** — no clinicaltrials.gov, ICTRP, or PubMed record was found for durvalumab in prostatic urethra urothelial carcinoma specifically (query log IDs 5–7, all zero results). The mechanistic plausibility is inherited from the urothelial-carcinoma class as a whole rather than from direct evidence in this exact histologic subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Durvalumab currently has no marketing authorization on file in Finland (`market_status`: 未上市, `total_licenses`: 0). No product/dosage-form information is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 immune checkpoint inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (prostatic urethra urothelial carcinoma) has evidence level L5 — a TxGNN model score with zero corroborating clinical trials or literature. In addition, package insert warnings/contraindications for durvalumab are flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from entering the S1 safety pre-assessment stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) to clear the Blocking data gap (DG001) and enable S1 safety pre-assessment
- Confirmed mechanism of action and original approved indication documentation (DG002)
- Disease-specific preclinical or early clinical data for prostatic urethra urothelial carcinoma, since current support is mechanistic extrapolation only

**Note for prioritization:** two other candidates in this same prediction set have materially stronger evidence and may warrant separate evaluation ahead of this one:
- **Infiltrating bladder urothelial carcinoma, sarcomatoid variant** (rank 3, L3, decision stage S1) — a Phase 2 trial (NCT03912818, terminated, n=7) graded "A" for disease-specificity, plus a supporting Phase 1 trial (NCT02812420).
- **Endocervical carcinoma** (rank 6, L2, decision stage S2) — two trials (NCT04065269 Phase 2 ongoing n=174; NCT03452332 Phase 1 completed n=20) and one supporting review (PMID 37467967).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

