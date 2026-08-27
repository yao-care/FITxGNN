---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 5
---

# Sacubitril
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

# Sacubitril: From Heart Failure (Sacubitril/Valsartan Combination) to Diabetic Nephropathy

> **Scoping note:** The evidence pack lists 5 TxGNN-predicted indications. Ranks #1 (brain small vessel disease/ocular anomalies), #2 (HANAC syndrome), #4 (rheumatoid arthritis) and #5 (hemoglobinopathy) each have **zero clinical trials**, and where literature exists (rank #1, 19 papers) none of it mentions sacubitril — the evidence pack's own rationale flags these as likely TxGNN false positives with no mechanistic support. Rank #3, **Diabetic Nephropathy**, is the only candidate with actual clinical trials and mechanistically relevant literature, so this report focuses on it.

## One-Sentence Summary

Sacubitril is the neprilysin-inhibitor component of the heart failure combination sacubitril/valsartan (LCZ696/Entresto); sacubitril itself has no marketing authorization on record in this evidence pack and its standalone mechanism-of-action data has not yet been catalogued. The TxGNN model predicts the sacubitril/valsartan combination may also benefit **Diabetic Nephropathy**, with **2 clinical trials** (including 1 not-yet-recruiting Phase 4 RCT) and **17 publications** — largely preclinical and mechanistic — currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure with reduced ejection fraction, as part of the sacubitril/valsartan combination (no sacubitril monotherapy indication on record) |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for sacubitril itself is not available in this evidence pack. Based on known information, sacubitril is the neprilysin-inhibitor component of sacubitril/valsartan (LCZ696), whose efficacy in heart failure with reduced ejection fraction (HFrEF) is well established; mechanistically, this combination may also be applicable to diabetic nephropathy.

Neprilysin inhibition raises circulating natriuretic peptide (ANP/BNP) activity, which is theorized to reduce glomerular intracapillary pressure and exert anti-fibrotic and antioxidant effects; combined with valsartan's angiotensin-receptor blockade, this gives a plausible dual mechanism against diabetic kidney injury. Several rodent models (db/db mice, Zucker Obese rats, streptozotocin-diabetic rats) support reduced glomerulosclerosis, oxidative stress and NLRP3 inflammasome activity under sacubitril/valsartan treatment.

An important caveat: **every piece of clinical and preclinical evidence below concerns the sacubitril/valsartan combination, not sacubitril as a single agent.** Since sacubitril has no monotherapy indication or market presence on record here, any repurposing pathway for diabetic nephropathy would necessarily follow the already-marketed combination product, not sacubitril alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not yet recruiting | 297 | Randomized, multicenter study (2:1 allocation) comparing sacubitril/valsartan vs. valsartan over 12 weeks in patients with essential hypertension and type 2 diabetic nephropathy; primary outcome tracks renal function change. No results yet available. |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Retrospective, non-interventional real-world EMR study of HFrEF patients on sacubitril/valsartan in India; documents prescribing/demographic patterns, not a diabetic-nephropathy-specific endpoint. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | RCT secondary analysis | The Lancet Diabetes & Endocrinology | Secondary analysis of the PARADIGM-HF trial assessing neprilysin inhibition's effect on renal function decline in patients with type 2 diabetes and chronic heart failure. |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical (combination therapy study) | International Immunopharmacology | 112 hypertensive diabetic nephropathy patients randomized to nifedipine + valsartan vs. nifedipine + sacubitril/valsartan; evaluates renal function outcomes. |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical imaging study | Diabetes, Metabolic Syndrome and Obesity | BOLD-MRI study evaluating sacubitril/valsartan's renal protective effects in type 2 diabetic nephropathy patients. |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Update on pillars of diabetic kidney disease therapy, situating RAAS/neprilysin-pathway agents within current management. |
| [34441977](https://pubmed.ncbi.nlm.nih.gov/34441977/) | 2021 | Review | Journal of Clinical Medicine | Reviews the diabetes–heart failure–diabetic nephropathy relationship and relevant pharmacotherapies. |
| [34734359](https://pubmed.ncbi.nlm.nih.gov/34734359/) | 2023 | Review | Heart Failure Reviews | Reviews disease-modifying drugs, including sacubitril/valsartan, in diabetic HFrEF patients. |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Review | Current Hypertension Reports | Reviews newer blood-pressure-lowering drugs developed for diabetic kidney disease and heart failure, including their mechanisms. |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Revue Médicale Suisse | Discusses the potential role of sacubitril/valsartan in type 2 diabetes, including glycemic and renal protective signals. |
| [35975848](https://pubmed.ncbi.nlm.nih.gov/35975848/) | 2023 | Review | Current Diabetes Reviews | Clinical review of existing and novel combination therapies for diabetic cardiorenal complications. |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Animal (preclinical, rat model) | Diabetes, Metabolic Syndrome and Obesity | Rat model of early diabetic nephropathy showing sacubitril/valsartan slows progression via NLRP3 inflammasome inhibition. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Evidence for diabetic nephropathy currently consists of a secondary RCT analysis (PARADIGM-HF), one small combination-therapy clinical study, one imaging study, and multiple preclinical/review sources — but no completed trial with diabetic nephropathy as a primary endpoint, and the sole purpose-built Phase 4 RCT (NCT06501651) has not yet started recruiting. All evidence pertains to the sacubitril/valsartan combination, while sacubitril itself remains unmarketed in this jurisdiction with no MOA data on file.

**To proceed, the following is needed:**
- Results from NCT06501651 (Phase 4 Hyper-Save Study) once recruitment completes
- Sacubitril mechanism-of-action data (currently a High-severity data gap, DG002)
- TFDA/regulatory package-insert warnings and contraindications (currently a Blocking data gap, DG001, required before any S1 safety pre-assessment)
- Clarification of regulatory pathway: repurposing would apply to the marketed sacubitril/valsartan combination, not sacubitril monotherapy — combination-product regulatory status should be separately confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

