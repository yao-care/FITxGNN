---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Undocumented Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (DrugBank DB01248) is a taxane-class cytotoxic agent; the evidence pack does not carry a documented original indication or Finland/Taiwan license record, but the drug's real-world clinical use context is breast cancer chemotherapy.
The TxGNN model predicts continued/strengthened efficacy for **Female Breast Carcinoma**, with **50 clinical trials** and **20 publications** returned from the literature search supporting this signal.
Because this indication overlaps with docetaxel's already-established real-world use (per the evidence pack's own rationale notes), this is best read as a **confirmatory signal rather than a novel repurposing candidate**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no `original_indications` or license records on file) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Finland/Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a taxane. It stabilizes microtubules and inhibits their depolymerization, which locks rapidly dividing cells in the G2/M phase and drives apoptosis. Since breast cancer cells have a high proliferation rate, this mechanism is directly relevant to the predicted indication.

The evidence pack's own repurposing rationale flags an important caveat: docetaxel (Taxotere) is a **currently approved chemotherapy for breast cancer** in most markets — this is not a typical "old drug, new disease" repurposing case. It appears here only because the `original_indications` field in this evidence pack is empty, so the model/scoring pipeline evaluated it as if breast cancer were an unconfirmed candidate. The very large number of completed Phase 3 trials below (including trials with >2,000–3,000 enrolled patients) reflects this: they are trials establishing/optimizing docetaxel's role in breast cancer treatment, not exploratory repurposing studies.

Because no license or regulatory documentation exists in this pack for the Finland/Taiwan market ("未上市" / Not Marketed, 0 authorizations), the practical next step is regulatory confirmation rather than further mechanistic justification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002544](https://clinicaltrials.gov/study/NCT00002544) | Phase 3 | Completed | 300 | Mitoxantrone ± docetaxel as first-line chemotherapy for metastatic breast cancer with unfavorable prognosis |
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Phase 3 | Completed | 150 | Weekly docetaxel vs. CMF in adjuvant treatment of high-risk breast cancer patients ≥65 or anthracycline-ineligible |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Docetaxel+cyclophosphamide or doxorubicin+cyclophosphamide→paclitaxel, ± trastuzumab, in node-positive/high-risk HER2-low breast cancer |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Phase 3 | Completed | 2611 | Adriamycin/Cytoxan followed by Taxotere ± Xeloda; overall survival in high-risk breast cancer |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2411 | Preoperative AC vs. AC followed by pre- or postoperative docetaxel in operable breast carcinoma |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Neoadjuvant docetaxel, carboplatin, trastuzumab, pertuzumab (TCHP) ± estrogen deprivation in HR+/HER2+ breast cancer |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | TAC (docetaxel/doxorubicin/cyclophosphamide) vs. TCX (docetaxel/cyclophosphamide/capecitabine) as adjuvant therapy in high-risk HER2-negative breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FE75C→docetaxel vs. paclitaxel as adjuvant chemotherapy in node-positive breast cancer |
| [NCT03252431](https://clinicaltrials.gov/study/NCT03252431) | Phase 3 | Completed | 393 | F-627 vs. Neulasta in women with Stage I–III breast cancer receiving myelotoxic (docetaxel-containing) chemotherapy |
| [NCT00003565](https://clinicaltrials.gov/study/NCT00003565) | Phase 2 | Completed | 109 | Population pharmacokinetics of docetaxel in Caucasian and African-American solid tumor patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | Docetaxel+cyclophosphamide (TC) vs. anthracycline-taxane regimens (TaxAC) in early breast cancer (ABC trials pooled analysis) |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review of paclitaxel and docetaxel in breast and ovarian cancer |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Review | The Oncologist | Clinical experience review of docetaxel and paclitaxel in breast cancer treatment |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review (pending classification) | J Clin Oncol | Foundational preclinical/clinical profile review of docetaxel (Taxotere) |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Study (pending classification) | Breast Cancer (Tokyo) | Docetaxel+cyclophosphamide+trastuzumab as neoadjuvant therapy for HER2+ primary breast cancer |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Study (pending classification) | Breast Cancer (Tokyo) | CEF followed by docetaxel as preoperative chemotherapy for early-stage breast carcinoma |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Study (pending classification) | Cancer | Capecitabine + docetaxel + epirubicin (TEX) as first-line therapy for advanced breast carcinoma |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Study (pending classification) | Oncology | Weekly docetaxel + gemcitabine as first-line treatment for metastatic breast cancer |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Study (pending classification) | J Clin Oncol | Dose-dense doxorubicin/docetaxel/G-CSF ± tamoxifen as preoperative therapy for operable breast carcinoma |

---

## Finland/Taiwan Market Information

No authorization records are on file for docetaxel in this evidence pack. Market status is recorded as **Not Marketed**, with **0 total licenses**.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane class, microtubule-stabilizing agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is strong (L1: multiple completed Phase 3 RCTs, including trials with >2,000 patients) and mechanistically coherent, but this indication appears to reflect docetaxel's already-established clinical use for breast cancer rather than a genuinely new repurposing target — and the pack has no Finland/Taiwan regulatory or safety documentation to support an independent evaluation.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed drug interaction (DDI) data — current query returned no results
- Verification of docetaxel's actual original/approved indication(s), since `original_indications` is empty in this pack
- Clarification of local (Taiwan/Finland) market and licensing status before any "new indication" claim is made, since current status is Not Marketed with 0 authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

