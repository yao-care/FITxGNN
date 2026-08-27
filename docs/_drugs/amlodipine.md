---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

Using the provided Evidence Pack (v4, multi-indication candidate for DB00381 / Amlodipine), here is the evaluation report. Note: because this pack contains 10 ranked predicted indications rather than one, I've selected the **best-evidenced candidate (Intracerebral Hemorrhage, L2)** as the headline indication for the title/Quick Overview (per the template's `predicted_indications[0]` convention, adapted to the strongest-evidence entry since rank-1 by TxGNN score, "brain stem infarction," has zero supporting evidence), and added an overview table covering all 10 candidates for transparency.

---

# Amlodipine: From Hypertension to Intracerebral Hemorrhage (Secondary Prevention)

## One-Sentence Summary

> Amlodipine is a long-acting dihydropyridine calcium channel blocker originally used to treat hypertension and chronic stable angina.
> The TxGNN model predicts it may have a role in secondary prevention of **Intracerebral Hemorrhage (ICH)** via intensive blood-pressure control,
> with **6 clinical trials** (including one completed Phase 3 RCT with 1,671 patients) and **8 publications** currently supporting this direction.
> Nine additional candidate indications were also predicted for amlodipine in this run; all but one have weak or no supporting evidence (see overview table below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (well-established clinical indication for amlodipine; no Finland-specific approved-indication text is available because the drug is **not marketed** in this dataset) |
| Predicted New Indication | Intracerebral Hemorrhage (blood-pressure control for secondary prevention) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L2 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All Predicted Indications Overview

The TxGNN run for amlodipine returned 10 ranked candidates. TxGNN score is not a proxy for evidence quality — the top-ranked candidate by score ("brain stem infarction") has no clinical or literature support, while a lower-ranked candidate (Intracerebral Hemorrhage) has the strongest real-world evidence.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Brain stem infarction | 99.94% | L5 | Hold |
| 2 | Pulmonary hypertension, unclear multifactorial mechanism | 99.91% | L5 | Hold |
| 3 | Pulmonary hypertension owing to lung disease/hypoxia | 99.91% | L5 | Hold |
| 4 | Malignant renovascular hypertension | 99.90% | L4 | Research Question |
| 5 | Malignant hypertensive renal disease | 99.90% | L5 | Hold |
| 6 | Cerebral artery occlusion | 99.89% | L3 | Research Question |
| 7 | Braddock syndrome | 99.88% | L5 | Hold |
| 8 | MRI defined brain infarct | 99.86% | L4 | Hold |
| 9 | ABri amyloidosis | 99.84% | L5 | Hold |
| **10** | **Intracerebral hemorrhage** | **99.79%** | **L2** | **Proceed with Guardrails** |

**Note on the weak candidates (ranks 1, 2, 3, 5, 7, 9):** these have no clinical trials and either no literature or only keyword-level (non-drug-specific) literature hits. Several are biologically implausible on mechanistic grounds — for example, calcium channel blockers are generally **not** recommended in hypoxia-driven (Group 3) pulmonary hypertension because they can blunt hypoxic pulmonary vasoconstriction and worsen V/Q mismatch, and rare genetic syndromes (Braddock syndrome, ABri amyloidosis) have no known mechanistic link to CCB pharmacology. These are treated as embedding-similarity noise rather than genuine repurposing signals.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank for this record (flagged as a High-severity data gap, DG002). Based on well-established pharmacological knowledge, amlodipine is a long-acting **dihydropyridine calcium channel blocker (CCB)**, which lowers blood pressure through vascular smooth muscle relaxation and reduction of systemic vascular resistance. Its efficacy in hypertension is well proven and forms the basis for its use in numerous fixed-dose combination antihypertensive regimens.

Hypertension is the single most important modifiable risk factor for both the occurrence and recurrence of intracerebral hemorrhage. Intensive, sustained blood-pressure control after an ICH event is a guideline-endorsed secondary-prevention strategy, and fixed low-dose combination "triple pill" regimens used in this context (e.g., the TRIDENT trial) commonly include a CCB component such as amlodipine. This provides a direct mechanistic rationale for the TxGNN prediction: the drug is not proposed as a treatment for the acute hemorrhage itself, but as a chronic BP-lowering agent to prevent recurrent hemorrhagic and cardiovascular events in ICH survivors.

The main evidentiary gap is that no trial to date has isolated amlodipine's individual contribution within these combination regimens — the supporting RCT (TRIDENT) evaluated a triple-pill strategy, not amlodipine monotherapy, so causal attribution to amlodipine specifically remains indirect.

---

## Clinical Trial Evidence

*(Primary indication: Intracerebral Hemorrhage)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial: fixed low-dose "Triple Pill" (BP-lowering combination, commonly including a CCB) vs. standard care for reducing recurrent stroke after ICH — the largest and most directly relevant trial for this indication. |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | Recruiting | 140 | TRICH score-guided triple antihypertensive therapy for BP control after ICH; ongoing, no results yet. |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | Large BP-intervention trial in Type 2 diabetics; ICH-relevant but not ICH-specific — indirect evidence. |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | ARB monotherapy vs. ARB + CCB combination for cardiovascular event reduction in elderly Japanese hypertensives; indirect evidence. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; terminated with only 1 participant, negligible statistical power. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study; terminated with only 4 participants, negligible statistical power. |

**Secondary candidate — Cerebral Artery Occlusion (L3, Research Question):** 5 trials identified, all indirect (BP-strategy or statin/CEA trials not specific to amlodipine); most relevant is [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) (STEP trial, n=8,000, systolic BP intervention in elderly hypertensives, status unknown).

---

## Literature Evidence

*(Primary indication: Intracerebral Hemorrhage)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT | Hypertension Research | CASE-J trial rationale — compares ARB vs. CCB-based regimens for cardiovascular event reduction in high-risk hypertensives. |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Review (Tier 1) | Int J Stroke | Rationale and design of the TRIDENT trial — triple-pill BP-lowering strategy for recurrent ICH prevention. |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Review | Neurological Sciences | Evaluates β-blocker (atenolol) role in acute ICH outcome; relevant to antihypertensive strategy discussion in ICH but not amlodipine-specific. |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Classic review of calcium antagonists' antihypertensive mechanism, including use in severe hypertension. |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Cohort (animal) | Biol Pharm Bull | Dihydropyridine CCB (benidipine) improves cerebral blood flow autoregulation in hypertensive rats — supportive mechanistic class evidence. |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with hemorrhagic stroke — safety signal, not efficacy evidence. |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Case Report | Curr Drug Saf | Tizanidine-induced hypotension in a stroke patient on antihypertensives; not amlodipine-specific. |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Case Report | BMJ Case Rep | PRES following rapid antihypertensive withdrawal post-bariatric surgery in a patient with prior ICH history; illustrates BP-management complexity, not direct efficacy evidence. |

**Secondary candidate — Cerebral Artery Occlusion (L3):** 5 preclinical (animal model) papers show amlodipine ± atorvastatin reduces infarct volume via antiapoptotic/antioxidant mechanisms after transient MCAO (e.g., [PMID 21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/), [PMID 17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/)) — mechanistically encouraging but no human trial data exists for this specific indication.

---

## Finland Market Information

Amlodipine is currently recorded as **not marketed (未上市)** in this dataset, with **0 marketing authorizations** on file. No product-level licensing data (authorization number, product name, dosage form, approved indication text) is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data were queried but returned as data gaps — TFDA package-insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) that must be resolved before this candidate can proceed to an S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Intracerebral Hemorrhage specifically) / **Hold** (for all other 9 candidate indications)

**Rationale:**
- The Intracerebral Hemorrhage candidate is supported by one completed Phase 3 RCT (TRIDENT, n=1,671) and a recruiting dedicated follow-on trial (TRICH), giving it genuine L2 evidence and a plausible, guideline-consistent mechanism (secondary BP control post-ICH). However, no trial has isolated amlodipine's individual effect from the combination "triple pill," so guardrails (monitoring, no monotherapy label claim) are required.
- The remaining 9 candidates lack drug-specific clinical evidence — most are either pure TxGNN score artifacts (L5, no trials/literature) or supported only by indirect/preclinical data (L3–L4), and are correctly held pending stronger evidence.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/regulatory package-insert warnings and contraindications) — currently a **Blocking** gap preventing any S1 safety evaluation.
- Resolve DG002 (formal DrugBank MOA record) to strengthen the mechanistic-link write-up.
- A trial or subgroup analysis isolating amlodipine's specific contribution within triple-pill regimens for ICH secondary prevention.
- Confirm actual Finland/Taiwan regulatory and marketing status, since the current record shows 0 authorizations, which conflicts with amlodipine's well-known global availability — this should be verified rather than assumed to be a true data gap versus a query/indexing error.
- For the Research Question-tier candidates (malignant renovascular hypertension, cerebral artery occlusion), a targeted literature/trial search using amlodipine-specific terms (current literature was largely non-specific or animal-only) before any further prioritization.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

