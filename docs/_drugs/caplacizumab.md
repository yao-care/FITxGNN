---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: From Not-Yet-Marketed to Thrombotic Thrombocytopenic Purpura (TTP)

## One-Sentence Summary

Caplacizumab (DrugBank DB06081) is not currently marketed in this jurisdiction (0 authorizations on file), so no locally-documented original indication exists in this dataset. Among the 10 candidate indications TxGNN generated, **Thrombotic Thrombocytopenic Purpura (TTP)** is the only one with substantive supporting evidence — **14 clinical trials** and **20 publications**, including the pivotal TITAN and HERCULES RCTs that underpin the drug's approval elsewhere. Note this is effectively a **market-access gap**, not classical repurposing: caplacizumab's globally-approved indication is TTP itself, and the evidence pack flags this explicitly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — drug not yet marketed in this jurisdiction (0 licenses on file) |
| Predicted New Indication | Thrombotic Thrombocytopenic Purpura (TTP) |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L1 |
| Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action field is not populated in this dataset for caplacizumab, but the repurposing rationale attached to the TTP candidate supplies sufficient mechanistic detail: caplacizumab is an anti-von Willebrand factor (vWF) A1-domain humanized nanobody that blocks the interaction between vWF multimers and platelet GPIbα.

In immune-mediated TTP, autoantibody-driven ADAMTS13 deficiency allows uncontrolled accumulation of ultra-large vWF multimers, which drive pathological platelet adhesion, microthrombosis, thrombocytopenia, and organ ischemia. By blocking the vWF–GPIbα axis directly, caplacizumab interrupts the proximate step in this pathology — the mechanism maps onto the disease process essentially 1:1, rather than by analogy.

This is why the evidence pack itself flags TTP as an unusual "prediction": caplacizumab (Cablivi) is already approved for TTP in multiple countries. Its appearance here as a "predicted indication" reflects a **local data/licensing gap** (未上市) rather than a genuine mechanistic hypothesis requiring validation — the underlying clinical evidence base is mature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Completed | 145 | HERCULES — pivotal double-blind, placebo-controlled RCT establishing caplacizumab's efficacy in faster platelet count normalization and prevention of microvascular thrombosis in aTTP |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Completed | 75 | TITAN — single-blind, placebo-controlled RCT; first evidence anti-vWF nanobody shortens time to platelet response as adjunct to plasma exchange |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Completed | 51 | Single-arm study of caplacizumab + immunosuppression **without** first-line plasma exchange; supports remission without daily TPE |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Completed | 21 | Japanese population trial confirming efficacy/safety consistency across ethnic groups, including recurrence prevention |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Completed | 104 | Post-HERCULES long-term follow-up; evaluates safety/efficacy of repeated caplacizumab use |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A | Completed | 223 | Real-world observational study characterizing platelet-count dynamics under caplacizumab, decoupled from ADAMTS13 activity |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A | Recruiting | 131 | Multicenter non-inferiority study of immunosuppression + caplacizumab + plasma infusion **without** therapeutic plasma exchange |
| [NCT06376786](https://clinicaltrials.gov/study/NCT06376786) | N/A | Recruiting | 132 | Italian iTTP prospective registry — natural history and long-term real-world outcomes |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | N/A | Recruiting | 350 | REACT-2020 (Germany) — national observational study confirming real-world efficacy and prescribing patterns |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Phase 2 | Terminated | 58 | Personalized caplacizumab dosing regimen guided by ADAMTS13 activity monitoring |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | RCT | NEJM | HERCULES primary publication — caplacizumab inhibits vWF-platelet interaction, reduces time to platelet response |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | RCT | NEJM | TITAN primary publication — establishes proof-of-concept efficacy of anti-vWF nanobody in aTTP |
| [36053773](https://pubmed.ncbi.nlm.nih.gov/36053773/) | 2023 | Systematic Review/Meta-analysis | Blood Advances | Adding caplacizumab to standard of care — pooled RCT and real-world observational data |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Systematic Review/Meta-analysis | Expert Review of Hematology | Efficacy and safety synthesis across populations |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Guideline | J Thromb Haemost | 2025 focused update of ISTH TTP management guidelines |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Guideline | J Thromb Haemost | ISTH guidelines for treatment of TTP |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Guideline | J Thromb Haemost | ISTH guidelines for diagnosis of TTP |
| [34266669](https://pubmed.ncbi.nlm.nih.gov/34266669/) | 2022 | Guideline | Medicina Clínica | Spanish diagnosis/treatment recommendations for TTP |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Review | JAMA | Comprehensive review of immune TTP diagnosis and management |
| [36890095](https://pubmed.ncbi.nlm.nih.gov/36890095/) | 2023 | Review | Transfus Apher Sci | Individualized treatment approach to TTP in the caplacizumab era |

---

## Market Information

This drug is **not currently marketed** in this jurisdiction — no product authorizations, dosage forms, or approved indication text are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other TxGNN-Flagged Candidates (Not Recommended)

For completeness: this evidence pack scored caplacizumab against 9 additional platelet/bleeding-disorder nodes (primary release disorder of platelets, pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen-receptor bleeding diathesis, constitutional thrombocytopenia, FNAIT, hemophilia, platelet-type bleeding disorder). All carry **L4–L5 evidence, decision stage S0/S1, and a Hold or Research Question recommendation** — either no clinical/literature evidence exists, or the disease mechanism runs counter to caplacizumab's anti-adhesive action (several are bleeding disorders where blocking vWF–GPIbα could *worsen* hemorrhagic risk). None are addressed further here.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical evidence for caplacizumab in TTP is mature (two pivotal RCTs, multiple Phase 2/3 confirmatory trials, and real-world registries across 1,500+ patients), so this is not an open efficacy question — it is a local registration/market-access gap.

**To proceed, the following is needed:**
- Local regulatory dossier / TFDA package insert (warnings, contraindications) — currently unavailable and blocking a full safety review
- Structured mechanism-of-action documentation from DrugBank
- Drug-drug interaction data (currently not found)
- Local licensing/market-authorization application status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

