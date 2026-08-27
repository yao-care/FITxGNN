---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 4
---

# Ezetimibe
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor originally developed to lower LDL cholesterol in hypercholesterolemia, used alone or combined with a statin.
The TxGNN model predicts it may also be effective for **Hyperlipoproteinemia**, a prediction supported by **50 clinical trials** (19 disease-matched via PubMed search) and **19 publications**, including multiple completed Phase 3 RCTs.
Because hyperlipoproteinemia sits within the drug's already-established pharmacology, this reads less as a novel mechanistic leap and more as a formal extension of existing use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia (LDL-C/total cholesterol lowering, alone or with a statin) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured DrugBank mechanism-of-action record is not available for this drug in the Evidence Pack (Data Gap DG002). Based on the repurposing rationale attached to this candidate: ezetimibe selectively inhibits the NPC1L1 transporter at the intestinal brush border, blocking absorption of dietary and biliary cholesterol (and plant sterols). This reduces chylomicron-cholesterol delivery to the liver, which compensatorily upregulates hepatic LDL receptors and lowers LDL-C and other apoB-containing lipoproteins.

Hyperlipoproteinemia is the broader clinical category that encompasses elevated LDL-C and mixed lipid disorders — essentially the pathophysiology ezetimibe's core mechanism already targets. This is not a mechanistic extrapolation into a new disease area; it is the drug's on-label pharmacological action being formally mapped onto a related diagnostic category.

The clinical trial record reinforces this: ezetimibe has been studied as monotherapy, in fixed-dose combinations with statins/fenofibrate/bempedoic acid, and as an active comparator arm in numerous Phase 3 trials for mixed hyperlipidemia and hypercholesterolemia, giving this prediction unusually strong real-world clinical support for a TxGNN-derived candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate coadministration evaluated for cholesterol-lowering effect in mixed hyperlipidemia (high cholesterol + high triglycerides) |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Phase 3 | Completed | 615 | Evolocumab vs. placebo and ezetimibe (active comparator) on LDL-C change in low-Framingham-risk hypercholesterolemic adults |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib 10mg/ezetimibe 10mg fixed-dose combination on top of maximally tolerated therapy in HeFH/ASCVD patients |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | IVUS-measured coronary plaque regression comparing cholesterol absorption inhibitor (ezetimibe) vs. synthesis inhibitor |
| [NCT04433533](https://clinicaltrials.gov/study/NCT04433533) | Phase 4 | Unknown | 200 | Rosuvastatin/ezetimibe combination vs. rosuvastatin monotherapy in Korean patients with LV diastolic dysfunction and hyperlipidemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate and ezetimibe coadministration for cholesterol-lowering safety/efficacy in mixed hyperlipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Companion Phase 3 study of fenofibrate/ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Completed | 181 | Fenofibrate vs. ezetimibe vs. combination in Type IIb dyslipidemia with metabolic syndrome features |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10mg add-on to atorvastatin or simvastatin in homozygous familial hypercholesterolemia |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completed | 1794 | 52-week Japanese post-marketing surveillance of Zetia (ezetimibe) mono/combination therapy safety and efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM Phase 3 RCT: obicetrapib/ezetimibe fixed-dose combination significantly reduces LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide RCT in heterozygous FH, a population historically treated with ezetimibe-based regimens |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Pathophysiology, diagnosis and treatment of postprandial hyperlipidemia and its link to atherosclerosis |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Review of current drugs targeting hyperlipidemia and ASCVD prevention |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors for patients not achieving LDL-C goals on statins/ezetimibe |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C/apoB-lowering therapies, positioning ezetimibe within the treatment landscape |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circulation Research | Overview of cholesterol-lowering agents including ezetimibe and PCSK9 inhibitors |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Familial hypercholesterolemia management, citing statins, ezetimibe, and LDL apheresis as core therapies |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug and Therapeutics Bulletin | Update on ezetimibe's LDL/total cholesterol-lowering effect alone or combined with statins |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Editorial | New England Journal of Medicine | Editorial commentary on cholesterol lowering and ezetimibe |

---

## Finland Market Information

Ezetimibe is currently **not marketed in Finland** according to this Evidence Pack — 0 marketing authorizations are on file (`taiwan_regulatory.total_licenses = 0`, `market_status = 未上市`). No Fimea license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (The Evidence Pack's key warnings, contraindications, and DDI lookup are all unpopulated — DG001, "TFDA/Fimea package insert warnings and contraindications," is flagged as a **Blocking** data gap that must be resolved before a full safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is strongly supported — evidence level L1, with multiple completed Phase 3 RCTs directly evaluating ezetimibe (alone or in fixed-dose combination) in hyperlipoproteinemia/mixed hyperlipidemia populations, and the mechanism is ezetimibe's already-established pharmacology rather than a novel hypothesis. However, the drug is not currently marketed in Finland and local safety/label data is entirely absent, so guardrails are required before any local development or communication.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently Blocking (DG001)
- Structured DrugBank MOA record to formally close DG002
- Finland-specific regulatory pathway assessment given current "not marketed" status (0 authorizations)
- Drug-drug interaction data (current DDI query returned `not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

