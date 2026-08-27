---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

> Erdafitinib is a pan-FGFR (FGFR1–4) tyrosine kinase inhibitor publicly known for the treatment of FGFR-altered locally advanced or metastatic urothelial carcinoma; this specific indication is not confirmed in the current Evidence Pack (regulatory and MOA fields are flagged as data gaps).
> The TxGNN model's top prediction is **Pulmonary Hypertension**, but with **0 clinical trials** and **0 publications** currently supporting this direction — and the available mechanistic rationale actually points toward a **safety concern** (FGFR-pathway inhibition has been linked to pulmonary hypertension risk with other kinase inhibitors) rather than a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial carcinoma, FGFR2/3-altered (public knowledge; not confirmed by supplied regulatory/MOA data — see Data Gaps) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on public information, erdafitinib is a pan-FGFR tyrosine kinase inhibitor used in oncology; its known efficacy is in FGFR-altered urothelial carcinoma.

Unlike the typical repurposing case where mechanism supports a new therapeutic use, the rationale attached to this top-ranked prediction is a **caution flag rather than an efficacy hypothesis**. FGF/FGFR signaling plays a role in pulmonary vascular remodeling, and other multi-kinase inhibitors (e.g., dasatinib) are known to induce or worsen pulmonary arterial hypertension. Because erdafitinib acts on the same FGFR axis, the model's association with pulmonary hypertension is mechanistically consistent with a **drug-induced risk signal**, not a proposed treatment application. No clinical trials, ICTRP records, or literature currently exist to support either a therapeutic or an adverse relationship — this remains a pure model output requiring safety-first evaluation before any further action.

The lower-ranked candidates in this pack show more classic repurposing logic (e.g., rheumatoid arthritis via FGFR's role in synovial angiogenesis, or brachydactyly-syndactyly syndrome via FGFR's established role in skeletal development), but all remain at evidence level L4–L5 with no clinical or trial-level corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the pulmonary hypertension indication specifically. One general reference on erdafitinib's kinase-inhibitor class was identified in relation to a lower-ranked candidate (rheumatoid arthritis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Review | Pharmacological Research | Overview of FDA-approved small-molecule kinase inhibitors (2019 cohort), noting erdafitinib among four newly approved agents; does not address pulmonary hypertension or rheumatoid arthritis specifically. |

---

## Finland Market Information

Erdafitinib is **not marketed in Finland** — no marketing authorizations are on record (0 licenses).

---

## Cytotoxicity

Erdafitinib is a targeted anticancer kinase inhibitor (publicly documented as an FGFR-directed therapy for urothelial carcinoma), so this section is included despite the Evidence Pack's DrugBank/toxicity fields being unpopulated.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1–4 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this Evidence Pack — TFDA/EU package insert warnings retrieval is listed as a **Blocking** severity gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pulmonary hypertension) has zero supporting clinical or literature evidence and its own mechanistic rationale reads as a potential safety risk rather than an efficacy signal — this is an L5, S0-stage model output with no independent corroboration. All six predicted indications in this pack sit at L4 or L5, and core safety data (package insert warnings, contraindications, DDI) are unavailable, which blocks even an initial S1 safety review.

**To proceed, the following is needed:**
- TFDA/EU package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action and original indication from DrugBank — currently a High-severity data gap (DG002)
- Targeted literature/pharmacovigilance search specifically on FGFR inhibitors and pulmonary hypertension risk (safety signal, not efficacy) before any further development consideration
- If pursuing lower-ranked candidates (e.g., rheumatoid arthritis, brachydactyly-syndactyly syndrome), preclinical mechanistic studies to move beyond L4/L5 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

