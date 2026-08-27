---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Pertuzumab is an anti-HER2 monoclonal antibody originally developed and approved for HER2-positive breast cancer, typically given in combination with trastuzumab and a taxane.
The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**,
with **10 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (established indication used with trastuzumab; no Finland licence currently on file) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, pertuzumab is an anti-HER2 monoclonal antibody that inhibits HER2/HER3 heterodimerization, used together with trastuzumab as standard therapy for HER2-positive breast cancer.

Progesterone-receptor status frequently co-occurs with HER2 positivity — the HER2+/hormone-receptor-positive (HR+) subtype is a well-recognized clinical entity representing roughly half of all HER2-overexpressing breast cancers. The predicted "new" indication is therefore best understood as a hormone-receptor-defined stratum of pertuzumab's existing approved population, not a wholly independent drug–disease association.

This is why the evidence base is unusually strong for a "predicted" indication: multiple completed Phase 3 trials (e.g. IMpassion050, the Asia-Pacific pertuzumab neoadjuvant trial, and several pertuzumab-biosimilar equivalence trials) already enrolled HER2+/HR-defined populations, and de-escalation studies (WSG-ADAPT, WSG-TP-II, PERTAIN) specifically examine how hormone-receptor status modifies response to dual HER2 blockade — directly supporting the mechanistic plausibility of extending use into the PR-positive stratum.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | QL1209 (pertuzumab biosimilar) + trastuzumab + docetaxel vs. reference pertuzumab regimen in HER2+/ER-PR- early or locally advanced breast cancer |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | BCD-178 vs. Perjeta as neoadjuvant therapy for HER2-positive breast cancer, ER/PR-negative population |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab preoperative therapy; explores impact of HER2 heterogeneity on treatment response |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant study comparing Herceptin/docetaxel/pertuzumab combinations on pathological complete response |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective study of HER2-low prevalence, treatment patterns and outcomes in metastatic breast cancer |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Neoadjuvant weekly paclitaxel response-rate study in Nigerian women with breast cancer (withdrawn, no data) |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | Chemotherapy-free neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab in HR+ (ER+/PR+), HER2+ localized breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs. placebo added to neoadjuvant chemo + trastuzumab + pertuzumab in early HER2+ breast cancer |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | Lapatinib + trastuzumab ± endocrine therapy, 12 vs. 24 weeks, in HER2-overexpressing breast cancer |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: de-escalation of adjuvant chemotherapy after pCR with neoadjuvant chemo + dual HER2 blockade, HR-negative/node-negative population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (biosimilar equivalence) | British Journal of Cancer | QL1209 pertuzumab biosimilar equivalent to reference pertuzumab + trastuzumab + docetaxel in HER2+/ER-PR- breast cancer |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II: endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (5-year follow-up) | Lancet Oncology | NeoSphere 5-year PFS/DFS/safety analysis of neoadjuvant pertuzumab + trastuzumab in HER2+ breast cancer |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase II) | Journal of Clinical Oncology | PERTAIN: trastuzumab + aromatase inhibitor ± pertuzumab in HER2+/HR+ metastatic breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline/Review (ASCO) | Journal of Clinical Oncology | Updated ASCO guideline for systemic therapy in HER2-positive advanced breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase II trial | Annals of Oncology | WSG-ADAPT HER2+/HR- final analysis: 12-week dual blockade ± paclitaxel, predictive markers |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | Review (trial rationale) | Future Oncology | DECRESCENDO: rationale for de-escalating chemotherapy in HR-negative, HER2-positive, node-negative early breast cancer |
| [33902424](https://pubmed.ncbi.nlm.nih.gov/33902424/) | 2022 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | Overview of immunotherapy options for breast cancer, including trastuzumab/pertuzumab context |
| [32905036](https://pubmed.ncbi.nlm.nih.gov/32905036/) | 2020 | Review | Cureus | Literature review of therapeutic strategies for HER2-positive metastatic breast cancer |
| [29291541](https://pubmed.ncbi.nlm.nih.gov/29291541/) | 2018 | Case report | International Journal of Surgery Case Reports | HER2-positive mucinous breast carcinoma case, notes on hormone receptor co-expression |

---

## Finland Market Information

Pertuzumab currently has no marketing authorization on file in Finland (market status: not marketed; 0 authorizations recorded).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low as monotherapy; risk in practice is largely driven by concurrent chemotherapy partners (e.g. docetaxel, paclitaxel) used in combination regimens |
| Emetogenicity Classification | Minimal to low as monotherapy; combination regimens follow the emetogenicity of the concurrent chemotherapy backbone |
| Monitoring Items | Please refer to the package insert warnings and precautions; anti-HER2 antibody therapy generally requires cardiac function (LVEF) monitoring and infusion-reaction observation |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted PR-positive breast cancer indication is supported by an L1 evidence level, including multiple completed Phase 3 trials, but it substantially overlaps with pertuzumab's existing approved HER2-positive use rather than representing a novel drug–disease relationship. The drug is not currently marketed in Finland and no local safety data are available, so guardrails are needed before any local development or off-label use decision.

**To proceed, the following is needed:**
- Fimea/TFDA package insert data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank or product labeling
- Assessment of the regulatory pathway required for Finland market entry, given current "not marketed" status
- Formal drug-drug interaction (DDI) review, since the current query returned no data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

