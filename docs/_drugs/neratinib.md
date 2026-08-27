---
layout: default
title: Neratinib
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 4
---

# Neratinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Neratinib: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Neratinib is an irreversible pan-HER (HER1/HER2/HER4) tyrosine-kinase inhibitor established for HER2-positive breast cancer, most notably as extended adjuvant therapy after trastuzumab-based treatment.
> The TxGNN model predicts it may also be effective for **progesterone-receptor positive breast cancer**,
> with **5 clinical trials** and **10 publications** currently supporting this direction.
> Note: Finland market authorization and official original-indication text are not available in the current data — the original-indication statement above is drawn from published literature (ExteNET, NALA trials), not from a licensed package insert.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Finland license records (drug not marketed); literature indicates HER2-positive breast cancer, extended adjuvant and metastatic settings |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data is not available in the current evidence pack. Based on the supporting literature, neratinib is an irreversible tyrosine-kinase inhibitor of HER1, HER2, and HER4, and its clinical activity in HER2-positive breast cancer (including the pivotal ExteNET phase 3 trial) is well established.

Progesterone-receptor (PR) positivity frequently co-occurs with HER2 positivity in the clinically important HR+/HER2+ breast cancer subgroup. In this subgroup, hormone-receptor signaling and HER2 signaling interact and can drive resistance to endocrine therapy alone, providing a mechanistic rationale for combining a pan-HER inhibitor like neratinib with endocrine agents (fulvestrant, aromatase inhibitors) or trastuzumab.

This is why the TxGNN prediction is plausible: it does not represent a leap to an unrelated disease, but an extension within the same tumor biology space where neratinib already has proven activity, targeting a hormone-receptor-defined subgroup of its established indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib plus endocrine therapy with trastuzumab in ER-positive, HER2-positive breast cancer; directly tests the neratinib + endocrine therapy combination relevant to PR+ disease |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Multicenter retrospective study of HER2-low prevalence, clinicopathologic characteristics and treatment patterns in metastatic breast cancer; large real-world sample but non-interventional |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A | Completed | 111 | Retrospective observational study of neratinib as extended adjuvant therapy in early-stage HER2+ breast cancer under the European Early Access Program |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | Withdrawn | 0 | Planned trial of fulvestrant plus neratinib in previously treated HR-positive, HER2-negative metastatic breast cancer; withdrawn, no data available |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Phase 2 | Terminated | 12 | Neratinib targeting EGFR/ERBB2 in HR-positive/HER2-negative, HER2-enriched advanced/metastatic breast cancer; terminated early, small sample |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | The Lancet. Oncology | ExteNET phase 3 trial: 12 months of neratinib after trastuzumab-based adjuvant therapy in early-stage HER2-positive breast cancer |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT | New England Journal of Medicine | I-SPY 2 adaptive phase 2 trial evaluating neratinib added to standard neoadjuvant chemotherapy in high-risk early breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Review | JNCCN | NCCN Guidelines update for breast cancer, covering HER2-directed and endocrine-based regimens |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Review | Clinical Breast Cancer | BCTEG roundtable on clinical developments and practice guidance for HER2-positive breast cancer, including neratinib |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Current treatment trends in HR+/HER2+ breast cancer, discussing hormone plus anti-HER2 combinations without chemotherapy |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Review | Clin Adv Hematol Oncol | Integration of recent data into clinical practice for metastatic breast cancer across receptor subgroups |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohort | Breast Cancer Res Treat | Real-world patterns of adjuvant neratinib use and tolerance in HR+/HER2+ early-stage breast cancer, noting GI-related discontinuation |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohort | Breast Cancer Research | Targetable ERBB2 mutations as an adverse prognostic marker in ER-positive, ERBB2 non-amplified lobular breast carcinoma |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Cohort | Frontiers in Oncology | Case report and literature review on HER2-positive breast cancer with leptomeningeal disease |

## Finland Market Information

Neratinib currently has no marketing authorization on record in Finland (market status: 未上市, 0 authorizations). No dosage form or approved-indication data is available to populate a licensing table.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (irreversible pan-HER tyrosine-kinase inhibitor) |
| Myelosuppression Risk | Low — no myelosuppression signal reported in the available literature; dominant toxicity is gastrointestinal (diarrhea), which drives treatment discontinuation in real-world cohorts |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Liver function tests, diarrhea/GI tolerance, and standard CBC per oncology monitoring practice |
| Handling Protection | As an oral antineoplastic agent, standard institutional cytotoxic/hazardous drug handling precautions should apply pending official package insert confirmation |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted PR+ breast cancer indication sits within neratinib's already-validated HER2-positive breast cancer biology, supported by an L2 evidence level (one completed Phase 2 observational trial plus a recruiting Phase 2 combination trial), but no trial to date is specifically stratified by PR status, so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- TFDA/official package insert warnings and contraindications (currently blocking, DG001)
- Formal DrugBank-sourced mechanism-of-action confirmation (DG002)
- Finland market authorization and licensing status confirmation
- A PR-status-stratified clinical trial or subgroup analysis to directly test the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

