---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is a dual endothelin receptor antagonist historically used for pulmonary arterial hypertension (PAH) and, per the supporting literature in this evidence pack, systemic sclerosis-related vasculopathy. The TxGNN model's top-ranked prediction is **Rheumatoid Arthritis**, but the supporting evidence is indirect — the only registered trial actually targets Giant Cell Arteritis, not RA — and is currently backed by **1 clinical trial (wrong indication)** and **16 publications**, mostly preclinical/review-level. Note: a lower-ranked candidate (limited systemic sclerosis, rank 3) shows a substantially stronger evidence base and is flagged separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured drug data (Data Gap); literature in this evidence pack consistently describes Bosentan as an endothelin receptor antagonist for pulmonary arterial hypertension |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the literature captured in this evidence pack, Bosentan is a dual ETA/ETB endothelin receptor antagonist whose established clinical use is pulmonary arterial hypertension and, in an off-label/extended context, systemic sclerosis-related vasculopathy.

The rationale for a rheumatoid arthritis link is indirect: two preclinical studies show that endothelin signaling contributes to inflammation in collagen-induced and zymosan-induced arthritis mouse models, and that Bosentan can reduce arthritis severity in these models (PMID 22249931, PMID 18515326). This supports a plausible role for endothelin blockade in joint inflammation generally, but it is a mechanistic inference from animal models of arthritis, not RA-specific clinical or translational data.

Importantly, the single clinical trial associated with this prediction (NCT06957002) is not an RA trial — it studies Bosentan in **Giant Cell Arteritis**, a different rheumatic disease. No RA-specific interventional trial currently exists. Given this gap between the predicted indication and the actual trial population, the evidence level is capped at L4 (mechanism/preclinical only), and this candidate should be treated as an early-stage hypothesis rather than a clinically supported repurposing case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | Randomized, controlled trial of Bosentan + glucocorticoids vs. glucocorticoids alone in **Giant Cell Arteritis** (not RA) — endpoint is failure-free survival at 12 months. Included here because it is the only bosentan trial retrieved under the RA search, but it targets a different disease entity. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Preclinical (collagen-induced arthritis) | Inflammation Research | Bosentan ameliorates collagen-induced arthritis in mice; TNF-α induces endothelin system genes |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Preclinical (zymosan-induced arthritis) | Journal of Leukocyte Biology | Endothelins modulate inflammation in zymosan-induced arthritis via LTB4, TNF-α, CXCL-1; ET-1 elevated in RA synovium |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Preclinical (IL-17, antigen-induced arthritis) | Pain | IL-17, a key RA cytokine, drives joint hypernociception in a mouse arthritis model |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Preclinical (IL-15) | PNAS | IL-15-induced hypernociception (relevant to RA) inhibited by a dual ETA/ETB receptor antagonist |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | Kardiologia Polska | Child with Eisenmenger syndrome and juvenile RA improved clinically on bosentan (given for PAH, not RA) |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Current Opinion in Rheumatology | Overview of rheumatic skin disease pathophysiology and therapy |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in connective tissue disease, including RA |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Diseases Clinics of North America | PAH related to connective tissue disease |
| [18238768](https://pubmed.ncbi.nlm.nih.gov/18238768/) | 2008 | Review | American Journal of Health-System Pharmacy | Drug therapy for systemic sclerosis complications, including endothelin antagonists |
| [21165350](https://pubmed.ncbi.nlm.nih.gov/21165350/) | 2010 | Review | Canadian Respiratory Journal | Treatment of pulmonary hypertension in connective tissue disease with interstitial lung disease |

---

## Finland Market Information

Bosentan is currently **not marketed** in Finland — no product authorizations are on record (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data for Bosentan were not available in this evidence pack — Data Gap DG001, flagged as Blocking, and DG002.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis prediction rests on preclinical arthritis-model mechanism data only; the sole associated clinical trial actually targets Giant Cell Arteritis, not RA, so there is no direct clinical evidence for this specific indication. Combined with the Blocking data gap on TFDA/package-insert safety information, this candidate cannot yet clear even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA package insert / regulatory safety data (contraindications, warnings, DDI) — currently Blocking (DG001)
- Confirmed mechanism of action documentation (DG002)
- An RA-specific interventional trial or translational study, since the only registered trial targets a different disease (GCA)
- Consider re-prioritizing evaluation resources toward **limited systemic sclerosis** (rank 3 in this evidence pack), which shows materially stronger evidence — an SSc-matched observational trial, a systematic review/meta-analysis (PMID 36974107), and mechanistic in vitro data on endothelin-driven fibrosis — and is already scored L2/S3 ("Proceed with Guardrails") rather than L4/Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

