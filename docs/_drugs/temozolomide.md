---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the report structure to generate this directly from the Evidence Pack data (no ambiguity in schema — proceeding without other skills, as this is a single-shot content generation task using the fully-specified template already provided).

# Temozolomide: From Malignant Glioma Chemotherapy to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent already established worldwide as the backbone of malignant glioma treatment. The TxGNN model predicts it is effective for **Adult Astrocytic Tumour**, a disease category that substantially overlaps with its existing standard-of-care use, and this direction is supported by **2 registered clinical trials** (including 1 completed Phase 3 RCT, n=500) and **20 publications**, several of which are landmark practice-defining trials (e.g., the original Stupp regimen study).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in local licensing data (0 authorizations on file); evidence-pack mechanistic analysis identifies malignant glioma / anaplastic astrocytoma chemotherapy (Stupp regimen) as temozolomide's established global use |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Finland Market Status | ✗ 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide is an oral imidazotetrazine alkylating prodrug. It undergoes spontaneous, non-enzymatic hydrolysis to MTIC, which methylates DNA at the O6 and N7 positions of guanine. This methylation triggers a futile mismatch-repair (MMR) cycle that ultimately drives apoptosis in tumor cells. Its high lipophilicity allows it to cross the blood–brain barrier, and MGMT (O6-methylguanine-DNA methyltransferase) promoter methylation status is the key biomarker predicting treatment response.

Because astrocytic tumors (including glioblastoma and anaplastic astrocytoma) arise from the same glial cell lineage that temozolomide was developed to target, the mechanistic fit is direct rather than inferred by analogy — unlike typical drug-repurposing candidates where the original and new indications are pharmacologically distant.

**Important caveat:** the evidence pack's own rationale explicitly notes that this is "the current standard of care (Stupp regimen), not strictly repurposing in the narrow sense, but an extension of evidence for an already-established indication." In other words, TxGNN has correctly rediscovered temozolomide's known primary use rather than surfaced a genuinely novel therapeutic hypothesis. This strengthens confidence in the model's signal quality but reduces its value as a *new* opportunity — the practical question here is regulatory/market entry, not proof of efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Head-to-head RCT comparing temozolomide alone vs. procarbazine/lomustine/vincristine (PCV) in recurrent WHO Grade III/IV astrocytic tumors — direct efficacy evidence for this indication (relevance grade A). |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of cabozantinib (XL184) combined with temozolomide + radiotherapy as first-line treatment in glioblastoma; temozolomide is a combination-arm component, providing supportive safety/PK data rather than standalone efficacy (relevance grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark EORTC-NCIC trial establishing radiotherapy + concomitant/adjuvant temozolomide (the "Stupp regimen") as standard of care for newly diagnosed glioblastoma. |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (long-term follow-up) | Lancet Oncol | 5-year follow-up of the EORTC-NCIC trial confirming durable survival benefit of RT + temozolomide over RT alone. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Randomized trial adding bevacizumab to RT + temozolomide in newly diagnosed glioblastoma; no overall survival benefit shown. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 Phase 3 trial: lomustine-temozolomide combination improved OS vs. temozolomide alone in MGMT-methylated glioblastoma. |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Randomized trial showing Tumor-Treating Fields plus maintenance temozolomide improves survival vs. temozolomide alone. |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 Phase 3 trial: dose-dense temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG Oncology BN007 Phase II/III trial of dual immune checkpoint blockade in MGMT-unmethylated newly diagnosed glioblastoma. |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Cohort/Trial | J Neurooncol | Exploratory cohort of radiotherapy + temozolomide specifically in anaplastic astrocytic gliomas. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Comprehensive review of glioblastoma and other primary adult brain malignancies, including temozolomide-based standard of care. |
| [29075865](https://pubmed.ncbi.nlm.nih.gov/29075865/) | 2017 | Review | Curr Oncol Rep | Review of glioblastoma treatment considerations specific to older adults. |

---

## Finland Market Information

No marketing authorization is currently on file — market status is **未上市 (Not marketed)**, with 0 registered licenses in the reviewed regulatory data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic chemotherapy agent — standard cytotoxic/hazardous drug handling protocols apply; specific label-based precautions pending TFDA package insert retrieval |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1) — a completed Phase 3 head-to-head RCT (n=500) plus multiple landmark Phase 3 trials in the literature support temozolomide's efficacy across astrocytic tumor subtypes. However, the drug is not currently marketed locally (0 licenses), and two data gaps are flagged as Blocking/High severity: (DG001) TFDA/local package insert warnings and contraindications, and (DG002) a formal MOA/indication registry entry. Note also that this "prediction" largely reconfirms temozolomide's already-established global standard-of-care role rather than surfacing a genuinely novel indication — the open question is local regulatory pathway, not efficacy.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/Fimea package insert for warnings, contraindications, and dosing (closes DG001, Blocking)
- Confirm formal original MOA/indication registry entry via DrugBank or equivalent (closes DG002, High)
- Obtain drug-drug interaction data (current query status: not found)
- Assess local market-entry pathway given current unmarketed status and 0 authorizations

**Lower-confidence secondary signal (not pursued further here):** TxGNN also flagged *cauda equina neoplasm* (rank 2, score 99.30%) as a candidate indication. Evidence is weak — Evidence Level L4, no clinical trials, only 2 case-report/case-series-tier publications, one of which is unrelated to tumor treatment. Recommendation for this candidate is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

