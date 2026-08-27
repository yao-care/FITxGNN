---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Trametinib
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

Using the evidence pack's own annotations to select the reporting focus: TxGNN's #1-ranked hit (choroideremia, 99.31%) is explicitly flagged in its own `repurposing_rationale` as likely model noise (no mechanistic link, zero trials, zero literature, recommendation = Hold). Building the whole report around a self-identified false positive would be misleading, so I'm reporting on the highest-scoring prediction that actually carries mechanistic and evidentiary support: **non-cutaneous melanoma** (rank 2, L1/S3, Proceed with Guardrails).

# Trametinib: From BRAF-Mutant Cutaneous Melanoma to Non-Cutaneous Melanoma

> **Note on model output:** TxGNN's single highest-scoring prediction for trametinib was *choroideremia* (score 99.31%). The evidence pack's own analysis judged this a likely false positive — no mechanistic link to MEK inhibition, no clinical trials, no literature, and a "Hold" recommendation. This report instead covers the next-ranked, evidence-backed prediction: **non-cutaneous melanoma**.

## One-Sentence Summary

Trametinib is a MEK1/2 inhibitor established (in combination with the BRAF inhibitor dabrafenib) for BRAF V600E/K-mutant **cutaneous** melanoma. The TxGNN model additionally predicts activity in **Non-Cutaneous Melanoma** (mucosal, acral, uveal, and ocular/conjunctival subtypes), with **50 clinical trials** identified in the underlying BRAF-mutant melanoma evidence base and **3 supporting case-level publications** specific to non-cutaneous (ocular/mucosal) sites.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BRAF V600E/K-mutant cutaneous melanoma (established combination use with dabrafenib; not derivable from Finland regulatory record, see below) |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L1 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Trametinib is a MEK1/2 inhibitor acting downstream in the RAS-RAF-MEK-ERK signalling pathway. In combination with the BRAF inhibitor dabrafenib, it is an established treatment for BRAF V600E/K mutation-positive melanoma, and this combination has been studied and approved primarily in **cutaneous** melanoma populations.

Non-cutaneous melanoma — encompassing mucosal, acral, uveal, and ocular/conjunctival subtypes — arises from the same melanocyte lineage but carries a lower BRAF V600 mutation prevalence (roughly 15–20% in acral melanoma, versus 50–60% in cutaneous superficial spreading melanoma). Critically, within the BRAF-mutant-positive subgroup of these non-cutaneous subtypes, the driving oncogenic mechanism is identical to cutaneous disease, so MEK inhibition remains mechanistically applicable.

Supporting this, case reports of BRAF-mutant conjunctival and lacrimal sac melanoma (ocular/mucosal, i.e. non-cutaneous) describe clinical responses to combined BRAF/MEK inhibition, and a dedicated Phase 2 trial (NCT02083354) specifically enrolled both acral and cutaneous BRAF V600-mutant melanoma patients under a shared dabrafenib + trametinib regimen. The prediction is therefore best framed as "effective in the BRAF-mutant-positive fraction of non-cutaneous melanoma," not the full non-cutaneous population indiscriminately.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04961619](https://clinicaltrials.gov/study/NCT04961619) | N/A | Completed | 39 | Real-world observational cohort of adjuvant dabrafenib + trametinib in completely resected high-risk Stage III melanoma (Turkey) |
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Phase 3 | Active, not recruiting | 267 | DREAMseq: sequencing of immunotherapy vs. dabrafenib+trametinib in unresectable/metastatic BRAF V600-mutant Stage III-IV melanoma |
| [NCT02645149](https://clinicaltrials.gov/study/NCT02645149) | Phase 2 | Completed | 216 | Molecular profiling with matched targeted therapy in BRAF/NRAS wild-type and mutant advanced/metastatic melanoma |
| [NCT02065063](https://clinicaltrials.gov/study/NCT02065063) | Phase 1 | Completed | 28 | Dose-escalation of trametinib + palbociclib (CDK4/6 inhibitor) in solid tumours including melanoma |
| [NCT01940809](https://clinicaltrials.gov/study/NCT01940809) | Phase 1 | Terminated | 15 | Sequential BRAF-MEK inhibition with CTLA-4/PD-1 blockade, immune biomarker focus, in BRAF-mutant melanoma |
| [NCT03979651](https://clinicaltrials.gov/study/NCT03979651) | N/A | Completed | 29 | Trametinib + hydroxychloroquine (autophagy inhibition) in NRAS-mutant melanoma |
| [NCT04949113](https://clinicaltrials.gov/study/NCT04949113) | Phase 3 | Active, not recruiting | 423 | NADINA: neoadjuvant ipilimumab+nivolumab vs. standard adjuvant nivolumab in Stage III melanoma (dabrafenib+trametinib as reference standard arm) |
| [NCT05668585](https://clinicaltrials.gov/study/NCT05668585) | Phase 1 | Completed | 89 | Safety/tolerability of CFT1946 alone and combined with trametinib in BRAF V600-mutant solid tumours |
| [NCT05275374](https://clinicaltrials.gov/study/NCT05275374) | Phase 1/2 | Not yet recruiting | 221 | XP-102 ± trametinib in BRAF V600-mutant advanced solid tumours (melanoma, colorectal, NSCLC, thyroid) |
| [NCT04547946](https://clinicaltrials.gov/study/NCT04547946) | N/A | Completed | 3 | Quality-of-life assessment of adjuvant dabrafenib+trametinib in melanoma (Portugal, real-world) |

*Note: none of the above trials specifically restrict enrollment to non-cutaneous melanoma subtypes; NCT02083354 (see acral lentiginous melanoma sub-analysis) is the only identified trial explicitly including a non-cutaneous (acral) arm alongside cutaneous melanoma.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27893585](https://pubmed.ncbi.nlm.nih.gov/27893585/) | 2017 | Case Report | Ophthalmic Plastic and Reconstructive Surgery | Conjunctival melanoma harbouring BRAF V600E mutation responsive to systemic BRAF/MEK inhibition |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Case Report | Clinical and Experimental Dermatology | Two cases of BRAF-mutated bulbar conjunctival (epithelioid-type) melanoma; one treated with a BRAF inhibitor for metastatic disease |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Case Report | Journal of Investigative Medicine High Impact Case Reports | Lacrimal sac malignant melanoma case and review of 15 Japanese patients |

## Finland Market Information

Trametinib currently holds **no marketing authorizations on file** (`total_licenses: 0`, `market_status: 未上市`). No dosage form or product-level data is available to summarize.

## Cytotoxicity (Antineoplastic Drug)

Trametinib is antineoplastic (MEK inhibitor used in BRAF-mutant melanoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable at this data cutoff (DDI query status: not found).

**Flag:** the evidence pack records a **Blocking**-severity data gap (DG001) — the TFDA/package-insert warnings and contraindications for trametinib have not yet been retrieved. This blocks completion of the S1 safety pre-assessment stage and should be resolved before any Go decision.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The BRAF-MEK inhibition mechanism is well-validated in BRAF-mutant melanoma broadly (L1 evidence, multiple completed/active Phase 2-3 trials), and case-level evidence supports activity in BRAF-mutant non-cutaneous (ocular/mucosal) melanoma specifically. However, no trial in the evidence base enrolls non-cutaneous melanoma as a primary, subtype-defined population, and BRAF mutation prevalence is markedly lower in non-cutaneous subtypes, so efficacy should be assumed only in BRAF-mutant-positive patients pending dedicated confirmation.

**To proceed, the following is needed:**
- Resolve the Blocking data gap (DG001): TFDA/package-insert warnings, contraindications, and DDI profile
- Confirm mechanism-of-action detail via DrugBank (DG002) to support a fuller mechanistic-relevance assessment
- Subtype-specific (mucosal/acral/uveal) trial data with BRAF-mutation stratification, since current trials pool cutaneous and non-cutaneous patients
- Finland/EU regulatory pathway assessment, given the drug currently holds no local marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

