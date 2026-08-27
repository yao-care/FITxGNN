---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 1
---

# Trabectedin
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

# Trabectedin: From Soft Tissue Sarcoma to Female Breast Carcinoma

## One-Sentence Summary

> Trabectedin is a marine-derived DNA-binding alkylator, established in Europe for soft tissue sarcoma and (in combination with pegylated liposomal doxorubicin) platinum-sensitive ovarian cancer.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> with **2 clinical trials** and **20 publications** currently retrieved, though most literature addresses breast cancer only indirectly (BRCA-related mechanism, preclinical work, or combination regimens).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma / ovarian cancer (per literature evidence; no formal approved-indication text on file — data gap) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source database (data gap). Based on the literature retrieved in this evidence pack, trabectedin is a tetrahydroisoquinoline alkaloid originally derived from the marine tunicate *Ecteinascidia turbinata*. It binds the DNA minor groove, inhibits transcription-coupled nucleotide excision repair (TC-NER), and interferes with transcription-factor binding (e.g., NF-Y), conferring selective cytotoxicity against tumor cells with BRCA1/2 or other DNA-repair deficiencies. It also acts on the tumor microenvironment by depleting tumor-associated macrophages/myeloid cells.

Trabectedin's established indications — soft tissue sarcoma and platinum-sensitive ovarian cancer — both frequently involve homologous-recombination/DNA-repair pathway alterations, the same biological axis implicated in a meaningful subset of breast cancers (particularly germline BRCA1/2-mutated and triple-negative disease). This shared vulnerability is the mechanistic bridge for the predicted extension to breast carcinoma.

Consistent with this rationale, in vitro studies in this evidence pack show trabectedin induces apoptosis in both HER2-/ER+ (MCF-7) and HER2+/ER- (MDA-MB-453) breast cancer cell lines, exerts anti-angiogenic effects on breast cancer cells, and — in combination with IL-12 — enhances NK-cell-mediated antitumor immunity in triple-negative breast cancer models. Several completed Phase 1/2 clinical studies have also tested trabectedin directly in advanced/metastatic breast cancer, including BRCA1/2-mutated subgroups, giving the prediction more than purely computational support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, placebo-controlled study of trabectedin's effect on QT/QTc interval in patients with advanced solid tumor malignancies (cardiac safety pharmacology, not breast-cancer-specific efficacy) |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance therapy after response to trabectedin + pegylated liposomal doxorubicin in recurrent ovarian carcinoma; trabectedin used as induction regimen, not as the primary study drug |

Note: neither retrieved trial directly evaluates trabectedin efficacy in a breast cancer population; efficacy signals in breast cancer come primarily from the literature below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2 Clinical Trial (single-agent) | Clinical Breast Cancer | Multicenter randomized Phase 2 study of trabectedin monotherapy in advanced breast cancer post-anthracycline/taxane, comparing two administration regimens |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 Clinical Trial | Clinical Breast Cancer | Phase 2 study of trabectedin 1.3 mg/m² q3w in HR+/HER2- advanced breast cancer, stratified by XPG mRNA expression as a predictive biomarker |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 Clinical Trial | Annals of Oncology | First-in-class international Phase 2 trial of trabectedin in germline BRCA1/2-mutated metastatic breast cancer |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Phase 3 exploratory biomarker analysis | Annals of Oncology | Exploratory analysis of the Phase 3 OVA-301 trial showing BRCA1/XPG mutation status predicts response to trabectedin + PLD (ovarian cancer, BRCA biology relevant to breast) |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opinion on Investigational Drugs | Overview of trabectedin's mechanism and rationale for use in breast cancer via tumor-associated macrophage modulation |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treatment Reviews | Trabectedin as a chemotherapy option in BRCA-deficient tumors, including breast cancer |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 (combination) | European Journal of Cancer | Phase 1 pharmacokinetic study of trabectedin + doxorubicin in soft tissue sarcoma and advanced breast cancer (9 breast cancer patients) |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunology Research | Trabectedin depletes MDSCs and enhances IL-12-driven NK-cell antitumor activity in triple-negative breast cancer models |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicology Letters | Trabectedin induces apoptosis via distinct pathways in MCF-7 (HER2-/ER+) and MDA-MB-453 (HER2+/ER-) breast cancer cell lines |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | European Cytokine Network | Trabectedin shows anti-angiogenic effects on HUVECs and breast cancer cell lines in vitro |

---

## Market Information

Trabectedin currently has **no market authorization on file** (0 licenses, market status: Not Marketed). No product/dosage-form records are available to summarize.

---

## Cytotoxicity

Trabectedin is a cytotoxic antineoplastic agent (DNA minor-groove-binding alkylator), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (marine-derived tetrahydroisoquinoline alkylator) |
| Myelosuppression Risk | High — literature in this evidence pack reports grade 3–4 neutropenia in ~50% and thrombocytopenia in ~20% of patients; hepatic toxicity also commonly noted |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests, renal function |
| Handling Protection | Cytotoxic drug handling precautions apply (standard for DNA-alkylating chemotherapy agents) |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in the evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (DG001: no TFDA/local package insert data) means the candidate cannot yet enter the S1 safety pre-assessment, and the drug is not marketed locally (0 authorizations).
- Efficacy evidence specific to breast carcinoma is real but preliminary — several completed Phase 1/2 studies (including a BRCA1/2-mutated subgroup) plus supportive preclinical mechanism data, but no completed Phase 3 confirmatory trial and no directly relevant registered clinical trial in this pack targets breast cancer as primary endpoint. This is consistent with the pack's own scoring of Evidence Level L2 / Decision Stage S2 ("Research Question").

**To proceed, the following is needed:**
- TFDA/local regulatory package insert (warnings, contraindications, DDI) to clear the Blocking gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- A completed randomized trial with breast carcinoma (ideally BRCA1/2-mutated or HR+/HER2- subgroup) as the primary study population
- A local market-entry or import pathway assessment, given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

