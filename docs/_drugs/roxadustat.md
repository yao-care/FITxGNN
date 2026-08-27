---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 4
---

# Roxadustat
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

# Roxadustat: From Anemia of Chronic Kidney Disease to Dry Eye Syndrome

## One-Sentence Summary

Roxadustat is a HIF-PH (hypoxia-inducible factor prolyl hydroxylase) inhibitor globally approved for anemia associated with chronic kidney disease. The TxGNN model predicts it may also be effective for **dry eye syndrome**, but this direction is currently supported by only **1 clinical trial** and **no publications**, so the evidence base is still very early.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (no local licenses on file); globally, roxadustat is approved for anaemia associated with chronic kidney disease |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 (single observational study, no completed RCT) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, roxadustat is a HIF-PH inhibitor used for anemia associated with chronic kidney disease (CKD), and mechanistically may be applicable to dry eye syndrome.

Renal anemia and dry eye syndrome are not obviously linked at first glance, but the one identified clinical trial (NCT06287879) offers a plausible bridge: it examines meibomian gland structure and function specifically in **renal anemia patients treated with erythropoietin or roxadustat** who present with dry eye symptoms. This suggests a possible connection between chronic anemia/hypoxia physiology (or its treatment) and ocular surface / meibomian gland health, which may be what the TxGNN model is picking up on.

However, this trial is observational and descriptive (it characterizes meibomian gland findings in an existing patient population) rather than an interventional study testing roxadustat's therapeutic effect on dry eye. The mechanistic pathway from HIF stabilization to ocular surface benefit has not been established, so the prediction should be treated as hypothesis-generating rather than confirmed.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | NA | Unknown | 50 | Observational study characterizing meibomian gland function and morphology in renal anemia patients (treated with EPO or roxadustat) presenting with dry eye symptoms |

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Roxadustat is not currently marketed in Finland — no marketing authorizations are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the dry eye syndrome indication rests on a single observational trial of unknown status with no supporting literature, and the drug is not yet marketed in Finland. Critically, TFDA/Fimea package insert warnings and contraindications are flagged as a **Blocking** data gap, which prevents even an initial safety (S1) assessment.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — Blocking gap
- Confirmed mechanism of action (MOA) documentation from DrugBank
- Drug-drug interaction (DDI) data (currently not found)
- Follow-up on NCT06287879 to determine its completion status and results
- At least one interventional/controlled study directly testing roxadustat for dry eye syndrome before advancing beyond hypothesis stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

