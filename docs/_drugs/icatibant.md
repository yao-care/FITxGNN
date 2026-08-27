---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 7
---

# Icatibant
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

# Icatibant: From Hereditary Angioedema (HAE) to C1 Inhibitor Deficiency

## One-Sentence Summary

> Icatibant (DrugBank DB06196) is a bradykinin B2 receptor antagonist already used globally (brand name Firazyr) for acute attacks of hereditary angioedema (HAE) caused by C1 inhibitor deficiency, though it is currently **not marketed in Finland**.
> The TxGNN model predicts it is effective for **C1 inhibitor deficiency**, the very condition underlying HAE, with **23 clinical trials** and **20 publications** currently supporting this direction.
> This is less a novel repurposing signal than a confirmation of icatibant's already-established global indication — the open question here is Finland market entry and local safety documentation, not efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Angioedema (HAE) due to C1 inhibitor deficiency *(inferred from clinical trial/literature evidence; no formal license text on file for Finland)* |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available directly from DrugBank for this pack (data gap DG002). However, the literature evidence collected here documents icatibant as a **selective bradykinin B2 receptor antagonist**: it competitively blocks bradykinin from binding its B2 receptor, preventing the vascular permeability increase and edema formation that bradykinin otherwise triggers (PMID 34965883, PMID 24925394).

C1 inhibitor (C1-INH) normally restrains the kallikrein-kinin cascade; when it is deficient or dysfunctional (hereditary or acquired), uncontrolled bradykinin generation drives the swelling attacks that define hereditary and acquired angioedema. Icatibant does not correct the enzyme deficiency itself, but blocks the final common downstream effector (the B2 receptor), which is why it is already the standard on-demand treatment for HAE attacks in multiple markets (Japan, UK, Spain, Taiwan, China, per the trial and registry evidence in this pack).

Because "C1 inhibitor deficiency" is the pathophysiological label for the same disease process icatibant already treats clinically, the TxGNN prediction should be read as the model correctly recovering an existing, well-validated indication rather than surfacing a genuinely new therapeutic hypothesis. The practical question for this jurisdiction is therefore registration and local labeling, not proof of concept.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | Randomized, double-blind, placebo-controlled trial of subcutaneous icatibant for acute HAE attacks |
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Randomized, double-blind, placebo-controlled trial of subcutaneous icatibant for cutaneous/abdominal HAE attacks |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | Randomized, double-blind head-to-head trial: icatibant vs. oral tranexamic acid for HAE |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS) — large multinational prospective registry of real-world safety/outcomes |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label study of self-administered subcutaneous icatibant for HAE attacks |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A | Completed | 179 | FIRAZYR post-marketing drug-use survey in Japan |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | Pharmacokinetics, tolerability and safety of single-dose icatibant in pediatric/adolescent HAE patients |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Completed | 8 | Open-label efficacy, PK and safety study of icatibant in Japanese HAE patients |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Completed | 5 | Safety/efficacy of icatibant injection (Icanticure®) in bradykinin-induced angioedema, Taiwan NHI-reimbursed setting |
| [NCT05489640](https://clinicaltrials.gov/study/NCT05489640) | N/A | Completed | 85 | Real-world UK homecare self-administration study — treatment patterns and patient-reported outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Disease burden of C1-INH-deficiency HAE in the Asia-Pacific region |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | Retrospective study | JACI In Practice | Bicenter review of diagnosis, course and therapy of acquired C1-INH deficiency |
| [37146882](https://pubmed.ncbi.nlm.nih.gov/37146882/) | 2023 | Observational survey | JACI In Practice | National UK survey of HAE and acquired C1 inhibitor deficiency demographics |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective study | J Clin Pharmacol | Real-life off-label prescribing patterns of C1-INH concentrates and icatibant |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registry analysis | Clin Exp Allergy | Icatibant and C1-inhibitor use in treatment of laryngeal HAE attacks |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Registry (IOS) | Allergy Asthma Clin Immunol | Real-world icatibant treatment outcomes in Spanish HAE-1/2 patients |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Overview of current and emerging HAE therapies including icatibant |
| [33472202](https://pubmed.ncbi.nlm.nih.gov/33472202/) | 2021 | Nationwide retrospective study | Int Arch Allergy Immunol | Occurrence, features and management of acquired C1-INH deficiency in the Czech Republic |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Clinical recommendations | Rev Med Interne | CREAK diagnosis/treatment recommendations for acquired C1-INH-deficiency angioedema |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case series | J Clin Immunol | Icatibant and recombinant C1 inhibitor use for HAE attacks during pregnancy |

---

## Finland Market Information

Icatibant currently holds **no marketing authorization in Finland** (`market_status: 未上市`, `total_licenses: 0`). No product-level licensing data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: no Finland-specific package insert, key warnings, contraindications, or DDI data are currently on file — see DG001/DG002 below. Prescribing information from jurisdictions where icatibant/Firazyr is already approved, e.g. the EU SmPC, should be reviewed as an interim reference.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence is strong and consistent — three completed Phase 3 RCTs plus a large multinational real-world registry (IOS, n=1761) already support icatibant for HAE/C1 inhibitor deficiency (Evidence Level L1). The blocker is not clinical evidence but local regulatory readiness: icatibant is not yet marketed in Finland, and the Finland-specific package insert/safety data is a **Blocking** data gap (DG001) that must be resolved before a formal S1 safety review can proceed.

**To proceed, the following is needed:**
- Obtain the Fimea-approved package insert (warnings and contraindications) — Blocking gap, DG001
- Confirm mechanism of action and drug classification directly via DrugBank API — DG002
- Complete a formal drug-drug interaction (DDI) review (current automated query returned "not found")
- Assess the Finland regulatory pathway (e.g., mutual recognition/decentralized procedure) given icatibant is already approved elsewhere in the EU and Asia-Pacific for this same indication

*Note: Ranks 2–7 in this evidence pack (serpinopathy, pseudo-von Willebrand disease, primary platelet release disorder, immune-mediated necrotizing myopathy, antisynthetase syndrome, Glanzmann thrombasthenia) all scored L5/S0/Hold — no clinical trials, no literature, and weak-to-absent mechanistic links per the model's own rationale — and are not recommended for further evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

