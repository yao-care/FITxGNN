---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

Oteracil is a non-cytotoxic modulating component of the S-1 combination (tegafur/gimeracil/oteracil), historically used alongside tegafur-based regimens in gastric and gastrointestinal cancers. The TxGNN model predicts it may be effective for **Colonic Neoplasm**, with **8 clinical trials** and **20 publications** currently supporting this direction, including three completed Phase 3 RCTs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (as a component of the S-1 combination) — specific Fimea/TFDA label text not available |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for oteracil itself is not available. Based on known information, oteracil is part of the S-1 oral fluoropyrimidine combination (tegafur + gimeracil + oteracil). Within this combination, oteracil acts by inhibiting orotate phosphoribosyltransferase (OPRT) in the gastrointestinal tract, which reduces local phosphorylation of 5-FU generated from tegafur and thereby lowers GI toxicity — it does not itself exert direct antitumor activity.

Gastric cancer and colonic neoplasm are both gastrointestinal malignancies that share the same underlying pharmacological target: the fluoropyrimidine (5-FU) pathway delivered via tegafur. Because S-1 has already been established and, in several countries, approved for colorectal cancer in addition to gastric cancer, the mechanistic rationale for extending oteracil-containing regimens to colonic neoplasm is well supported.

The strength of this prediction rests specifically on the S-1 combination's extensive clinical development in colorectal cancer (ACTS-CC, ACTS-RC, SALTO trials), rather than on any independent activity of oteracil. This distinguishes it from several lower-ranked predictions in this evidence pack (e.g., benign or vascular colonic lesions), which lack any plausible cytotoxic mechanism and appear to be anatomical-proximity artifacts of the TxGNN embedding rather than genuine pharmacological signals.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+Leucovorin vs. TS-1 (S-1) as adjuvant treatment for Stage III colon cancer, with gene-expression predictive factor analysis |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO study: S-1 vs. Capecitabine as first-line treatment for metastatic colorectal cancer, ± bevacizumab |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (oxaliplatin + S-1) vs. XELOX as adjuvant chemotherapy for Stage III colorectal cancer |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib combined with S-1 (tegafur/gimeracil/oteracil) as third-line treatment for advanced metastatic CRC |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 for metastatic colorectal cancer that failed standard chemotherapy; primary endpoint mPFS |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after irinotecan/oxaliplatin failure |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL regimen) for untreated metastatic colorectal cancer |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1/capecitabine + oxaliplatin vs. cardiac microvascular safety in metastatic GI adenocarcinoma (safety-focused, not efficacy) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02: S-1 + oxaliplatin (SOX) superior to UFT/LV as adjuvant therapy in high-risk Stage III colon cancer |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Annals of Oncology | ACTS-RC (JFMC35-C1): S-1 vs. UFT as adjuvant chemotherapy for Stage II/III rectal cancer |
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT | Annals of Oncology | ACTS-CC trial: S-1 non-inferior to UFT/LV as adjuvant chemotherapy for Stage III colon cancer |
| [26036466](https://pubmed.ncbi.nlm.nih.gov/26036466/) | 2015 | RCT | BMC Cancer | Randomized Phase II study comparing S-1 dosing schedules after resection of colorectal cancer |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | Clinical Study | Int J Clin Oncol | KSCC1303: S-1 + oxaliplatin (C-SOX) for Stage III colon cancer, final 3-year disease-free survival analysis |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | Asian consensus guidelines for management of metastatic colorectal cancer |
| [10897209](https://pubmed.ncbi.nlm.nih.gov/10897209/) | 2000 | Review | Gan To Kagaku Ryoho | Foundational review of S-1's biochemical modulation concept, including oteracil's role in reducing GI toxicity |
| [17496461](https://pubmed.ncbi.nlm.nih.gov/17496461/) | 2007 | Review | Gan To Kagaku Ryoho | Status of adjuvant chemotherapy for colorectal cancer in Japan |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | Clinical Study | Br J Cancer | ACTS-CC trial planned safety analysis of UFT/LV vs. S-1 as adjuvant therapy for Stage III colon cancer |
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Clinical Study | Zhonghua Zhong Liu Za Zhi | Efficacy and side effects of oxaliplatin + S-1 combination therapy in postoperative colorectal cancer patients |

## Finland Market Information

Oteracil-containing products (S-1 combination) are currently **not marketed in Finland** — no active Fimea marketing authorizations were found (0 licenses on record).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic combination component (fluoropyrimidine-class modulator; oteracil itself has no direct cytotoxic activity — it inhibits GI-tract OPRT to reduce toxicity from tegafur-derived 5-FU) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low to moderate (based on fluoropyrimidine class, consistent with the S-1 combination) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes |
| Handling Protection | As a component of an antineoplastic combination product, cytotoxic drug handling regulations apply |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs (ACTS-CC, ACTS-RC, SALTO) and multiple Phase 2 studies consistently support the efficacy of S-1 (containing oteracil) in colorectal cancer, giving this prediction L1 evidence strength. However, the product is not currently marketed in Finland and key safety/MOA data remain unavailable, so guardrails are warranted before any regulatory or clinical advancement.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications, drug interactions) — currently a Blocking data gap
- Detailed mechanism of action documentation for oteracil specifically (DrugBank query pending)
- Finland-specific regulatory pathway assessment, given current "not marketed" status
- Confirmation of DDI profile (current query returned "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

