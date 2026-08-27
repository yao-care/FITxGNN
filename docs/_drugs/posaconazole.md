---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 1
---

# Posaconazole
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

# Posaconazole: From Invasive Fungal Infection Prophylaxis to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal historically used for the prevention and treatment of invasive fungal infections such as aspergillosis and mucormycosis in high-risk immunocompromised patients. The TxGNN model predicts it may also be effective for **Pneumocystosis (Pneumocystis pneumonia)**, but currently only **2 clinical trials** and **5 publications** are available, and none directly test posaconazole against this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infection prophylaxis/treatment (e.g., aspergillosis, mucormycosis) — official Finland labeling text is not available since the product is not currently marketed |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Posaconazole is a triazole antifungal. Its mechanism of action is inhibition of fungal CYP51 (14-α-demethylase), which blocks ergosterol synthesis — an essential component of the fungal cell membrane. Clinically, it is currently used mainly for the prevention and treatment of invasive aspergillosis and mucormycosis in high-risk populations such as patients with hematologic malignancy or those undergoing transplantation.

*Pneumocystis jirovecii*, however, is an atypical fungus with a distinct membrane sterol composition — it contains relatively little ergosterol and relies more on other sterols. As a result, the direct antifungal activity of triazoles against *Pneumocystis* is mechanistically plausible but weakly and inconsistently supported in the literature; trimethoprim-sulfamethoxazole (TMP-SMX) remains the standard of care for this organism.

Because of this, the link between posaconazole and pneumocystosis should be treated as an indirect, mechanism-driven hypothesis rather than a clinically validated one. This is consistent with the evidence pack's own scoring: an L4 evidence level and an "S0 / Research Question" decision stage, meaning the prediction currently rests on mechanistic reasoning rather than confirmed clinical benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Evaluated IV rezafungin (an echinocandin, not posaconazole) versus standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic HSCT recipients; relevant only as background context for antifungal prophylaxis, not direct evidence for posaconazole in pneumocystosis. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens (PTCy-based) after mismatched unrelated donor transplant; does not name posaconazole or pneumocystosis as a primary endpoint — any antifungal prophylaxis arm is incidental, not a direct test of this indication. |

Neither trial directly tests posaconazole for pneumocystosis; both are graded "C" relevance (indirect background evidence only).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet Infectious Diseases | UK best-practice update on diagnosis of serious fungal disease; covers diagnostic methods broadly, not posaconazole efficacy in pneumocystosis specifically. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review/Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 Chinese clinical practice guideline for invasive pulmonary fungal disease diagnosis and management. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective review of infectious complications (including fungal) in acute GVHD after liver transplantation; provides epidemiologic context, not direct posaconazole–pneumocystosis data. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and Pneumocystis pneumonia; notes posaconazole's established role in reducing invasive candidiasis via mould-active prophylaxis, but does not report direct anti-Pneumocystis efficacy. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK) | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal/antitubercular agents; pharmacokinetic context only, no efficacy data for pneumocystosis. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack itself scores this prediction as L4 ("Research Question," decision stage S0) — a mechanistic hypothesis with no clinical trial or literature directly testing posaconazole in pneumocystosis, and *Pneumocystis*'s atypical sterol biology makes triazole efficacy uncertain. Combined with a Blocking data gap on TFDA/Fimea safety labeling and the product currently not being marketed in Finland, there is not yet a basis to proceed.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism-of-action documentation (DrugBank MOA) — currently a High-severity gap
- Direct preclinical or clinical evidence of posaconazole activity against *Pneumocystis jirovecii*
- Drug-drug interaction (DDI) data, currently unavailable ("not_found")
- Confirmation of original approved indication text once market/licensing data becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

