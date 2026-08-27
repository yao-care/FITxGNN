---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibric acid derivative (PPAR-α agonist) with an established, well-documented use in hyperlipidemia and mixed dyslipidemia. The TxGNN model's top-ranked prediction is **Homozygous Familial Hypercholesterolemia (HoFH)**, but this signal is currently supported by only **1 loosely related clinical trial** (testing a different drug) and **11 publications**, none of which directly test fenofibrate in HoFH.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack's regulatory fields; fenofibrate's known original use is hyperlipidemia / mixed dyslipidemia (fibrate class), corroborated by the rank-2 prediction rationale |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for fenofibrate (flagged as a High-severity data gap, DG002). Based on known pharmacological class information, fenofibrate is a fibric acid derivative and PPAR-α agonist that activates lipoprotein lipase and lowers apoC-III, reducing triglycerides and raising HDL-C. Its efficacy in hyperlipidemia and mixed (type IIb/III/IV/V) hyperlipoproteinemia is well established — this is directly supported within this same evidence pack by the rank-2 prediction ("hyperlipoproteinemia"), which reaches Evidence Level L1 with multiple completed Phase 3 RCTs.

HoFH, however, is a distinct clinical entity: it is caused by near-complete loss of LDL-receptor function, leading to markedly elevated LDL-C that is largely independent of the triglyceride/HDL-focused PPAR-α pathway fenofibrate acts on. The relationship between fenofibrate's proven original use (TG-lowering in dyslipidemia) and this new predicted indication is therefore indirect at best.

The repurposing rationale captured in the evidence pack states this explicitly: "fenofibrate's PPAR-α/TG pathway has no direct relationship to the pathogenic mechanism of HoFH; clinically it is not part of mainstream HoFH therapy" (mainstream options being statins, PCSK9 inhibitors, lomitapide, or LDL apheresis). Consistent with this, the single retrieved clinical trial (NCT03510715) tests alirocumab, not fenofibrate, in HoFH patients — it overlaps only in target population, not in drug. This prediction should therefore be read as a TxGNN model signal awaiting direct mechanistic or clinical validation, not as an evidence-backed repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (PCSK9 inhibitor), not fenofibrate, in children/adolescents with HoFH on background therapy — relevance limited to population overlap only (grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Clinical | Pharmacological Research Communications | Fenofibrate 300 mg/day in type II hyperlipoproteinemia (22 patients); one HoFH patient showed the greatest fall in total and LDL cholesterol among all subjects |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK Study | Pharmacotherapy | Characterized pharmacokinetic interactions of lomitapide (an approved HoFH drug) with fenofibrate and other lipid-lowering agents |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Case series | Internal Medicine Journal | Liver transplantation for HoFH; discusses standard/emerging lipid-lowering therapies as inadequate alone for severe LDL-C elevation |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | States fenofibrate's most definite indication is monotherapy for fasting triglyceride >500 mg/dL to reduce pancreatitis risk, with modest cardiovascular benefit |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management and cardiovascular disease prevention guideline |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the NY Academy of Sciences | Reviews pharmacologic/surgical treatment options for dyslipidemic children with familial hypercholesterolemia, including fenofibrate among several agents |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Reviews dyslipidemia management in pregnancy; general context, not fenofibrate/HoFH-specific |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews LDL-C reduction via statins and PCSK9 inhibitors; general background, no fenofibrate/HoFH data |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe as a cholesterol absorption inhibitor; general background only |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Reviews atorvastatin pharmacology and therapeutic potential; general background only |

---

## Finland Market Information

Fenofibrate currently holds **0 marketing authorizations** in Finland and is not on the market (`market_status: 未上市`). No product/license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available at the time of this evaluation (DG001, Blocking severity — TFDA/label warning data could not be retrieved, which also blocks progression to the S1 safety-review stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (HoFH) lacks a direct mechanistic link — fenofibrate's PPAR-α/triglyceride pathway does not address the LDL-receptor defect underlying HoFH — and no clinical trial has tested fenofibrate specifically in this population.
- A Blocking-severity data gap (missing TFDA/label safety data) prevents this candidate from advancing to the S1 safety pre-assessment stage regardless of efficacy signal.

**To proceed, the following is needed:**
- Retrieve and parse the official package insert (warnings, contraindications, DDI) to resolve DG001 before any S1 safety evaluation
- Obtain confirmed mechanism-of-action data (DG002) to properly assess mechanistic plausibility for HoFH
- Consider evaluating the rank-2 candidate ("hyperlipoproteinemia," L1 evidence, 34 clinical trials) instead, or as an interim path, since it reflects fenofibrate's already-established use rather than a novel, mechanistically unsupported indication
- If HoFH remains of interest, seek preclinical or mechanistic studies directly testing fenofibrate (or fenofibrate + statin/PCSK9i combination) in LDL-receptor-deficient models before further clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

