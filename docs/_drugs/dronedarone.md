---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation/Atrial Flutter to Stroke

## One-Sentence Summary

Dronedarone is a Class III antiarrhythmic agent originally used to treat atrial fibrillation and atrial flutter. The TxGNN model predicts it may also reduce the risk of **stroke**, with **19 clinical trials** and **20 publications** currently available as supporting context — though only a subset directly studies dronedarone itself. The drug is currently **not marketed in Taiwan**, and key safety documentation (TFDA package insert, DDI data) is still missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial Fibrillation / Atrial Flutter |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not yet available in this evidence pack (DrugBank MOA field is a data gap). Based on the clinical evidence collected, dronedarone is a non-iodinated, multichannel-blocking Class III antiarrhythmic (a structural analogue of amiodarone) used to maintain sinus rhythm in patients with atrial fibrillation or atrial flutter.

Atrial fibrillation itself is a major, well-established risk factor for ischemic stroke — the arrhythmia promotes atrial stasis and thrombus formation, particularly in the left atrial appendage. By restoring and maintaining sinus rhythm ("rhythm control"), dronedarone may indirectly reduce thromboembolic events. This link is not a novel discovery: it was already flagged as a secondary/post-hoc finding in the pivotal Phase 3 **ATHENA trial**, where dronedarone reduced first cardiovascular hospitalization or death, with post-hoc analyses (PMID 22149318, 20396635) suggesting a reduction in stroke incidence specifically. One mechanistic study (PMID 28992468) further suggests dronedarone may have direct anticoagulant/antiplatelet effects independent of its antiarrhythmic action, offering a possible pharmacological explanation beyond rhythm control alone.

Importantly, this mechanistic link is indirect (via arrhythmia control) rather than a direct antithrombotic mechanism, and dronedarone carries a black-box warning for use in permanent AF and heart failure populations (per PALLAS trial findings, PMID 22082198) — meaning the therapeutic window for this repurposing hypothesis is narrower than for its original indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1,015 | International observational cohort directly comparing dronedarone's real-world effectiveness vs. other antiarrhythmic agents in AF |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A | Completed | 87,810 | Systematic literature review/network meta-analysis of Multaq® (dronedarone) vs. sotalol safety in AF, including stroke risk |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs. usual care in first-detected AF, evaluating improved outcomes including thromboembolic events |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | RCT assessing dronedarone 400mg BID for preventing stroke, systemic embolism, MI, or CV death in permanent AF with risk factors (PALLAS trial) |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | EDORA trial: dronedarone vs. placebo post-ablation for AF recurrence and atrial fibrosis progression |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST trial: early structured rhythm control (incl. antiarrhythmics) vs. usual care to prevent AF-related complications, including stroke |
| [NCT02618577](https://clinicaltrials.gov/study/NCT02618577) | Phase 3 | Terminated | 2,608 | NOAH-AFNET trial: NOAC (edoxaban) vs. current therapy for stroke prevention in atrial high-rate episodes (drug class differs from dronedarone) |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1,898 | Multicenter prospective study of dronedarone's efficacy, safety, and quality-of-life impact for early rhythm control in AF |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs. dronedarone for maintenance of sinus rhythm post-cardioversion |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational study describing NOAC management for stroke prevention in elderly NVAF patients in Spain (indirect, non-dronedarone) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | New England Journal of Medicine | Tested whether dronedarone reduces major vascular events in high-risk permanent AF; trial was stopped early for safety concerns |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT sub-analysis | Clinical Research in Cardiology | Long-term safety/efficacy of amiodarone and dronedarone for early rhythm control in the EAST-AFNET 4 trial |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc RCT analysis (ATHENA) | European Journal of Heart Failure | Dronedarone reduces CV events in AF/AFL patients with concomitant HFpEF/HFmrEF |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Retrospective cohort | Circulation: Arrhythmia and Electrophysiology | Head-to-head comparison of dronedarone vs. sotalol effectiveness and safety in AF-naive veterans |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Retrospective cohort | Journal of Atrial Fibrillation | Real-world risk of CV events, stroke, CHF, interstitial lung disease, and liver injury: dronedarone vs. amiodarone and other antiarrhythmics |
| [33888353](https://pubmed.ncbi.nlm.nih.gov/33888353/) | 2021 | Real-world cohort | Clinical Therapeutics | Evaluated digitalis intoxication risk with concomitant dronedarone + digoxin use |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic/basic science | Atherosclerosis | Dronedarone exerts anticoagulant and antiplatelet effects independent of its antiarrhythmic action |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vascular Health and Risk Management | Overview of dronedarone approval and efficacy; post-hoc ATHENA analysis suggests decreased stroke risk |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Review | Current Cardiology Reviews | Stroke prevention in atrial fibrillation: concepts and controversies |
| [24469871](https://pubmed.ncbi.nlm.nih.gov/24469871/) | 2013 | Review | Cardiology Journal | Efficacy and tolerability of dronedarone for AF patients in clinical practice |

---

## Taiwan Market Information

Dronedarone currently holds **no TFDA marketing authorization** and is **not marketed** in Taiwan (0 licenses on record). No product/dosage-form data is available for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug-drug interaction data are currently on file for dronedarone in this evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA package insert), meaning a formal S1 safety pre-assessment cannot yet be completed.

Note from the literature evidence above: dronedarone carries a known black-box warning for use in **permanent AF** and **heart failure** (PALLAS trial, PMID 22082198), and has documented pharmacokinetic interaction risk with digoxin via P-glycoprotein inhibition (PMID 33888353). These should be prioritized once formal TFDA labeling data is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple trials and post-hoc analyses (ATHENA, EAST-AFNET 4) support an indirect stroke-risk-reduction signal via AF rhythm control, but this evidence is largely secondary/post-hoc rather than a dedicated stroke-endpoint trial, and the PALLAS trial shows a narrow safety margin in permanent AF populations — consistent with the L2 evidence level and guarded recommendation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a **Blocking** data gap
- Detailed mechanism of action data from DrugBank
- Formal drug-drug interaction (DDI) data, particularly for digoxin and P-glycoprotein/CYP3A4 substrates
- Assessment of Taiwan market access pathway, since dronedarone is not currently marketed locally
- A dedicated safety monitoring plan given the black-box warning in permanent AF/heart failure populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

