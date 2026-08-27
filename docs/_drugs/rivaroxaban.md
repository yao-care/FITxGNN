---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation Therapy to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct Factor Xa inhibitor anticoagulant, generally used for prevention and treatment of thromboembolic conditions (e.g., venous thromboembolism, stroke prevention in atrial fibrillation); no structured original-indication data is present in this dataset. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **4 publications** currently identified — none of which directly test rivaroxaban as an RA therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (drug not marketed in Finland; known generally as an anticoagulant/Factor Xa inhibitor) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, rivaroxaban is a direct Factor Xa inhibitor used to prevent and treat thromboembolic disease; it has no established mechanistic action on inflammatory or immune pathways.

Rheumatoid arthritis (RA) is a chronic inflammatory disease, and elevated inflammatory activity is known to increase venous thromboembolism (VTE) risk. In clinical practice, RA patients may receive rivaroxaban to manage a co-occurring VTE or atrial fibrillation event — that is, treatment of a *complication* of RA, not RA itself.

There is no evidence that Factor Xa inhibition acts on RA's core inflammatory pathways (e.g., TNF-α, IL-6). The high TxGNN score most likely reflects an indirect knowledge-graph association driven by RA–VTE comorbidity co-occurrence rather than a genuine therapeutic mechanism, and should be interpreted with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Compares medication adherence between rivaroxaban and apixaban in non-valvular atrial fibrillation patients; not RA-specific. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of lower-extremity VTE diagnosis and treatment; does not address RA. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de medecine interne | Discusses thrombin generation assay for assessing hypercoagulability in autoimmune disease (e.g., antiphospholipid syndrome); RA relevance is indirect. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case Report | Cureus | Case of an 88-year-old woman with RA (on oral steroids) and atrial fibrillation who had recurrent thromboembolic events despite anticoagulation — illustrates RA as a comorbidity in anticoagulated patients, not RA treatment. |

## Finland Market Information

Rivaroxaban is currently not marketed in Finland (0 authorizations on record); no license data is available.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/Fimea package insert warnings and contraindications are a blocking data gap for this candidate — see Next Steps.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, there is no clinical trial evidence and no mechanistic support for rivaroxaban treating RA itself — the identified literature reflects RA-as-comorbidity in anticoagulated patients rather than RA-directed efficacy. Combined with the absence of safety/regulatory data, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a blocking gap preventing initial safety assessment
- DrugBank-sourced mechanism of action data
- RA-specific mechanistic or preclinical studies (e.g., effect of Factor Xa inhibition on synovial inflammation) to distinguish a true signal from comorbidity-driven graph noise

**Other candidates from this evidence pack** (gout, HIV infectious disease, brachydactyly-syndactyly syndrome) were also evaluated and all received a **Hold** recommendation, with weaker or no mechanistic rationale than rheumatoid arthritis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

