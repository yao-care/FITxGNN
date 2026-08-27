---
layout: default
title: Vortioxetine
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 5
---

# Vortioxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Vortioxetine: From Major Depressive Disorder to Neurotic Disorder

## One-Sentence Summary

Vortioxetine is a multimodal serotonergic antidepressant originally developed and used for **Major Depressive Disorder (MDD)**. The TxGNN model's top-ranked prediction suggests possible efficacy in **Neurotic Disorder** — a broad, heterogeneous ICD-9 category covering anxiety, dissociative, and somatoform conditions — but this is currently supported by only **1 indirect clinical trial** and **1 review-level publication**, making the evidence base thin relative to the model's high confidence score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — per literature evidence; no Finland license record available (drug not marketed) |
| Predicted New Indication | Neurotic Disorder |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for vortioxetine is flagged as a data gap in this evidence pack (DG002, High severity). Based on information available in the associated literature (e.g., PMID 25016186, PMID 29189941), vortioxetine is known to act as a serotonin (5-HT) transporter (SERT) inhibitor combined with 5-HT3, 5-HT7, and 5-HT1D receptor antagonism, 5-HT1B partial agonism, and 5-HT1A agonism — a "multimodal" profile that increases serotonergic, noradrenergic, dopaminergic, and cholinergic neurotransmission. Its efficacy in MDD has been well established through multiple Phase 3 registration trials and network meta-analyses.

"Neurotic disorder" is a broad, now largely retired ICD-9 classification that encompasses anxiety, dissociative, and somatoform symptom clusters rather than a single well-defined disease entity. Since anxiety commonly co-occurs with depression, and vortioxetine's serotonergic multimodal mechanism has a theoretical rationale for anxiety-comorbid depression, the biological plausibility for this link is not unreasonable.

However, the model's own rationale flags an important caveat: current evidence for "neurotic disorder" is only indirect (a general-population real-world antidepressant cohort study and a case-report-style review focused on a narrower, related term — "neurotic depression") and does not specifically validate this broad diagnostic category. Notably, this same evidence pack contains two closely related, more specific candidate terms — **melancholia** and **neurotic depression** — each supported by Phase 3 RCT-level evidence (evidence level L1) and multiple network meta-analyses, including the well-known Cipriani et al. 21-antidepressant comparison (PMID 29477251). Those candidates represent substantially stronger, more actionable repurposing signals than the top-ranked "neurotic disorder" prediction evaluated here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Completed | 370,212 | Real-world retrospective cohort using nationwide claims data comparing medication utilization patterns and adverse-outcome risk across commonly used antidepressants; population is general depression patients, not specifically defined as "neurotic disorder" — relevance graded C (indirect). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review (case report) | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Case report on "neurotic depression" treatment approaches, noting the benefit of combining antidepressants with cognitive behavioral therapy; addresses a narrower diagnosis than the broader "neurotic disorder" category. |

## Finland Market Information

Vortioxetine currently has **no marketing authorization in Finland** (0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (TFDA/Fimea package insert review is flagged as a **Blocking** data gap, DG001).

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN score for "neurotic disorder" is high, but supporting evidence is limited to one indirect real-world cohort study and one review discussing a related but narrower diagnosis. No study directly evaluates vortioxetine in a population specifically diagnosed with the broad "neurotic disorder" category, so this remains a hypothesis-generating signal rather than an actionable repurposing case.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank — currently a High-severity data gap (DG002)
- A study or trial specifically targeting the "neurotic disorder" diagnostic category (anxiety/dissociative/somatoform spectrum), rather than proxy terms like general antidepressant cohorts
- Consider prioritizing the related, better-supported candidates in this same evidence pack — **melancholia** and **neurotic depression** — both rated L1 evidence with Phase 3 RCT support and recommended as "Proceed with Guardrails"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

