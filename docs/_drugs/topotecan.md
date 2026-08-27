---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Ovarian/Cervical Cancer and SCLC to Female Breast Carcinoma

## One-Sentence Summary

Topotecan is a topoisomerase I inhibitor with established efficacy in ovarian cancer, cervical cancer, and small-cell lung cancer. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **5 clinical trials** and **20 publications** currently identified in support of this direction, though most are small, combination-therapy, or terminated studies rather than confirmatory Phase 3 evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug unmarketed in Finland); mechanistic rationale cites established use in ovarian cancer, cervical cancer, and small-cell lung cancer (SCLC) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (drug-level MOA field is flagged as a High-severity data gap). Based on the supporting rationale within this pack, topotecan is a topoisomerase I inhibitor that stabilizes the Topo1–DNA cleavage complex, causing replication-fork collapse and double-strand DNA breaks, producing cytotoxicity in highly proliferative cancer cells.

This mechanism is already clinically validated in ovarian cancer, cervical cancer, and small-cell lung cancer — all solid tumours with proliferation biology comparable to breast carcinoma. Topotecan's CNS penetration further supports a plausible role in breast cancer with brain metastases, a well-recognized clinical challenge.

However, breast carcinoma is not an approved indication for topotecan. The supporting evidence is a mix of small Phase II trials, terminated studies, and combination regimens rather than confirmatory large-scale RCTs, so mechanistic plausibility currently outweighs direct clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | High-dose TIME regimen (topotecan + ifosfamide/mesna + etoposide) followed by autologous stem cell rescue in metastatic breast cancer; study terminated. |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's-choice single-agent chemotherapy in platinum-sensitive relapsed gBRCA-mutated ovarian cancer; topotecan's specific role as a comparator arm could not be confirmed from the available summary. |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib vs. standard-of-care chemotherapy in platinum-resistant ovarian/peritoneal/fallopian cancer; topotecan-specific arm relevance unclear from summary. |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with multiple standard chemotherapy/immunotherapy regimens in advanced malignancies; topotecan appears only as one of several comparator combinations. |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-based high-throughput drug-screen assay to select chemotherapy in refractory solid tumours; exploratory, not a direct efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II Clinical Trial | American Journal of Clinical Oncology | CALGB Phase II trial of single-agent topotecan in 47 evaluable patients with previously treated advanced breast cancer. |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Cohort/Pilot | Onkologie | Pilot study of topotecan as primary chemotherapy for symptomatic brain metastases in metastatic breast cancer. |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II Clinical Trial | British Journal of Cancer | Continuous infusional topotecan in chemo-naïve advanced breast cancer and NSCLC; no evidence of increased efficacy over standard dosing. |
| [21514634](https://pubmed.ncbi.nlm.nih.gov/21514634/) | 2011 | RCT (Phase II, ovarian) | Gynecologic Oncology | Phase II trial of lapatinib + topotecan targeting BCRP/P-gp-mediated topotecan resistance in platinum-refractory ovarian/peritoneal carcinoma; mechanistic relevance to breast cancer resistance biology. |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical/Mechanistic | International Journal of Biological Macromolecules | TFDP1 identified as a therapeutic target for topotecan in triple-negative breast cancer (TNBC) via senescence suppression. |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-geburtshilfliche Rundschau | Review of new cytotoxic agents (including topotecan) in breast carcinoma therapy. |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan + pazopanib combination shows potent efficacy in preclinical models of primary/metastatic triple-negative breast cancer. |
| [27444351](https://pubmed.ncbi.nlm.nih.gov/27444351/) | 2016 | Preclinical | Phytomedicine | MHP-1 restores topotecan sensitivity and inhibits metastasis via EMT/TGF-β signaling regulation in breast cancer cells. |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacological Research | Daidzein enhances topotecan's anticancer effect and reverses BCRP-mediated drug resistance in breast cancer. |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical/Mechanistic | Cancer Research | CRISPR screen identifies topoisomerase I inhibition as inducing synthetic-lethal R-loop accumulation in MYC-driven breast cancer. |

---

## Finland Market Information

Topotecan is not currently marketed in Finland — no marketing authorizations are on file in this evidence pack (`total_licenses = 0`).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor / camptothecin derivative class) |
| Myelosuppression Risk | High — literature on topotecan in related indications reports myelosuppression as the dose-limiting toxicity (e.g., median nadir leukocyte count 1.75 cells/mm³, neutrophil count 1.55 cells/mm³, platelet count 20,500 cells/mm³) |
| Emetogenicity Classification | Low to moderate (consistent with camptothecin-class agents) |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Requires handling per institutional cytotoxic drug handling protocols (PPE, closed-system transfer where available) |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available for topotecan in this evidence pack (TFDA package insert retrieval is flagged as a Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Topotecan's topoisomerase I inhibition mechanism is well-validated in related solid tumours, and multiple small Phase II trials and a growing body of preclinical/mechanistic literature (including TNBC-specific targets) support biological plausibility in breast carcinoma. However, direct clinical evidence remains limited to older, small, or terminated trials rather than confirmatory large RCTs, and breast carcinoma is not an approved indication.

**To proceed, the following is needed:**
- TFDA/Finland package insert data (warnings, contraindications, DDI) — currently a Blocking gap
- Confirmed mechanism of action documentation from DrugBank
- Clarification of topotecan's actual study-arm role in NCT02282020 and NCT04739800 (both appear olaparib-centric)
- Updated search for any completed Phase II/III breast cancer trials post-2020

*Note: This evidence pack also flags a secondary, lower-confidence signal for adult germ cell tumor (Evidence Level L2, Decision Stage "Research Question"), based largely on pediatric neuroblastoma and retinoblastoma data rather than adult germ cell tumors directly; this was not evaluated in the current report and would require separate assessment.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

