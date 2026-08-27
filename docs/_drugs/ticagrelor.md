---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is a reversible P2Y12 receptor antagonist used as an antiplatelet agent to reduce thrombotic cardiovascular events (no official original-indication or MOA record was returned from the source registries for this candidate — this is based on generally known drug information, not the Evidence Pack). The TxGNN model predicts it may be effective for **Intracranial Arteriosclerosis**, with **11 clinical trials** and **3 publications** currently supporting this direction, though none of the trials has yet reported completed pivotal results specific to this indication. This Evidence Pack also flags TFDA/Fimea package insert data as a **blocking gap**, so no safety pre-screen can be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (general knowledge fallback — no Finland/Fimea license record available) |
| Predicted New Indication | Intracranial Arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on generally known information, ticagrelor is a reversible, direct-acting oral P2Y12 receptor antagonist that inhibits ADP-induced platelet activation and aggregation — the standard antiplatelet mechanism used to prevent atherothrombotic events in acute coronary syndrome, post-PCI stenting, and prior myocardial infarction.

Intracranial arteriosclerosis (intracranial atherosclerotic disease, ICAD) shares the same underlying pathology as coronary atherosclerosis: plaque build-up in the arterial wall leading to thrombus formation and downstream ischemic events (stroke rather than myocardial infarction). Since antiplatelet therapy is the pathophysiological countermeasure to arterial (not venous) thrombosis regardless of vascular bed, extending a P2Y12 inhibitor from coronary to cerebrovascular arteries is mechanistically coherent.

This is reflected in the evidence: the CAPTIVA trial (NCT05047172, Phase 3, ongoing) is directly testing ticagrelor (alone or combined with rivaroxaban) against clopidogrel for symptomatic intracranial arteriosclerotic stenosis, and the DREAM-PRIDE trial (NCT04948749, recruiting) is evaluating intracranial stenting plus aggressive antiplatelet management for the same population. However, both are still active/recruiting rather than completed with reported outcomes, which is why the evidence level is capped at L2 rather than L1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1,683 | CAPTIVA: tests whether rivaroxaban, ticagrelor, or both are superior to clopidogrel for lowering 1-year ischemic stroke/ICH/vascular death in intracranial vascular atherostenosis. |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recruiting | 792 | DREAM-PRIDE: drug-eluting stent + aggressive medical treatment vs. standard medical treatment alone to prevent 1-year stroke recurrence in symptomatic intracranial atherosclerotic disease. |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | EVOLVE Short DAPT: assessed safety of 3-month DAPT in high-bleeding-risk PCI patients with the SYNERGY stent system. |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13,885 | EUCLID: compared ticagrelor vs. clopidogrel on CV death/MI/ischemic stroke in peripheral artery disease — supportive but indirect atherosclerosis-population evidence. |
| [NCT06857045](https://clinicaltrials.gov/study/NCT06857045) | N/A | Withdrawn | 0 | 3- vs 6-month DAPT after implantation of the NOVA intracranial sirolimus-eluting stent system. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot RCT comparing genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic intracranial atherosclerotic disease (ICAD). |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Unknown | 2,171 | Anticoagulation alone vs. anticoagulation + antiplatelet in acute ischemic stroke with concomitant atrial fibrillation and extracranial/intracranial artery stenosis. |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS: ticagrelor + aspirin (1 month) then ticagrelor monotherapy vs. standard DAPT strategy after stent implantation. |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not yet recruiting | 1,700 | SOLOPCI: very short DAPT followed by P2Y12 monotherapy vs. standard DAPT duration in elderly post-PCI patients. |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2,036 | Low-dose (45mg BID) vs. standard-dose (90mg BID) ticagrelor after drug-eluting stent implantation for unstable angina. |

*(1 additional lower-relevance trial, NCT07354828 — a generic DAPT quality-control-indicator study not specific to intracranial arteriosclerosis — was excluded to keep the table to the 10 most relevant trials.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT | International Journal of Stroke | Design/early progress of the CAPTIVA trial testing whether dual antithrombotic combinations (incl. ticagrelor) outperform clopidogrel+aspirin for symptomatic intracranial atherosclerotic stenosis. |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of Neurointerventional Surgery | Reports experience with ticagrelor 60mg BID + aspirin vs. standard aspirin/clopidogrel for DAPT in neurointerventional (intracranial stenting) procedures. |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis, summarizing current knowledge gaps and highlights in the field. |

---

## Finland Market Information

Ticagrelor is currently **not marketed** in Finland under this Evidence Pack's regulatory query (market_status: 未上市, total authorizations: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: this Evidence Pack flags a **Blocking** data gap (DG001 — TFDA/Fimea package insert warnings and contraindications not retrieved), which means the S1 safety preliminary evaluation cannot be completed at this stage. A separate drug interaction database query also returned no results (query_status: not_found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Safety data (package insert warnings, contraindications, drug-drug interactions) is entirely missing, which is a Blocking-severity gap that prevents even a preliminary (S1) safety evaluation.
- The top-ranked predicted indication (intracranial arteriosclerosis) has only L2 evidence — mechanistically plausible and actively being tested (CAPTIVA, DREAM-PRIDE), but no completed indication-specific pivotal trial has yet reported results.
- Ticagrelor is not currently marketed in Finland, so there is no existing local regulatory foothold to leverage for a label-extension pathway.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications, DDI) to complete the S1 safety pre-screen
- Detailed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Completed results from the CAPTIVA trial (NCT05047172) and DREAM-PRIDE trial (NCT04948749)
- A Finland-specific regulatory pathway assessment, given the drug currently has zero local marketing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

