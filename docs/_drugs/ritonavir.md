---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using no specific skill — this is a direct report-generation task per the detailed prompt template already provided.

One judgment call before drafting: `predicted_indications[0]` (feline AIDS) is TxGNN's top-ranked hit by array order, but the evidence pack's own `repurposing_rationale` flags it as a likely ontology-mapping artifact (human HIV trial, "grade C" relevance, no cat data) and `predicted_indications[2]` has zero evidence (L5, no mechanistic plausibility). Presenting either as the headline indication would misrepresent the evidence. I'm featuring rank 2 (SIV infection — L3, real mechanistic/experimental support) as the primary candidate and noting why the other two were screened out.

---

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor, used both as a direct antiretroviral and as a pharmacokinetic booster of other protease inhibitors via CYP3A4 inhibition. The TxGNN model's most biologically coherent prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a lentivirus closely related to HIV-1 and a standard primate model for antiretroviral research — supported by **10 relevant publications** including direct in vitro susceptibility data, though **no dedicated clinical trials** currently exist for this indication.

> **Note on model output:** TxGNN also scored two other candidates at similarly high confidence — *feline acquired immunodeficiency syndrome* (rank 1) and a rare neurodevelopmental disorder (rank 3). Both were excluded from this report: the feline AIDS hit is annotated in the evidence itself as a likely disease-name mapping error (its only linked trial is a human HIV study), and the neurodevelopmental disorder has no mechanistic rationale, trials, or literature (L5, prediction-only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (per evidence-pack mechanistic annotation; no formal Finland label text on file) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this evidence pack (flagged as a Blocking-severity data gap). Based on the information that is available, ritonavir is an HIV-1 protease inhibitor that also acts as a CYP3A4 inhibitor, a property exploited to raise the blood levels of co-administered protease inhibitors ("boosting"). Its efficacy against HIV-1 protease is well established.

SIV is a close relative of HIV-1 within the lentivirus genus and is widely used as an animal-model surrogate for HIV-1 in antiretroviral research. The evidence pack's own rationale for this prediction notes that PI-class drugs show cross-reactive inhibitory activity against SIV protease because of structural and substrate-specificity similarity between the two viral proteases — a claim borne out directly in the literature below (e.g., PMID 12709355 measured ritonavir's IC50 against SIV protease in vitro).

Because SIV infection is a research/model-organism condition rather than a target patient population, the practical value of this prediction is primarily as a validated *tool compound* use (confirming PI activity in SIV models for HIV cure/reservoir research) rather than a therapeutic indication in animals or humans — this distinction should guide how "Go/Hold" is interpreted downstream.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro susceptibility | Antimicrob Agents Chemother | Direct head-to-head comparison of PI susceptibility: SIVmac239 inhibited by ritonavir at EC50 ≈13 nM, similar to its potency against HIV-1 (EC50 ≈25 nM) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility | Antiviral Therapy | Evaluated 16 approved anti-HIV-1 drugs against HIV-2, SIV (mac251, B670) and SHIV strains to inform treatment/PEP guidance |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model (macaque) | Journal of Virology | Modeled rapid viral decay kinetics in SIVmac251-infected macaques on a 7-day quadruple antiretroviral regimen |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal model (macaque) | PLoS ONE | Combination ART plus the HDAC inhibitor SAHA tested in SIV-infected Chinese rhesus macaques as a viral-reservoir/cure model |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal model (macaque) | Journal of Virological Methods | Oral HAART including Lopinavir/Ritonavir given to SHIV(89.6P)-infected macaques; assessed impact on CD8+ T-cell subsets |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal model (macaque) | mBio | Found lentivirus (HIV/SIV) persistence in brain tissue despite effective ART, with neuroimmune activation |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal model (macaque) | PLoS Pathogens | Highly intensified multidrug ART tested across a range of viremia levels in SIVmac251-infected rhesus macaques; assessed viral reservoir restriction |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Basic virology | Microbes and Infection | Engineered a chimeric SHIV carrying HIV-1 protease as an in vivo tool for testing protease inhibitor efficacy in macaques |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Basic virology | Journal of Virology | Characterized viral-protease-dependent processing of the HIV-1 Vif protein within virions |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro (unrelated compound) | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative K-12 active against AZT- and ritonavir-resistant HIV-1 strains as well as HIV-2 and SIV |

## Finland Market Information

Ritonavir is not currently marketed in Finland; no marketing authorizations are on file (0 licenses recorded).

## Safety Considerations

Please refer to the package insert for safety information. (Finland-specific warnings, contraindications, and drug-interaction data are recorded as a Blocking-severity data gap and were not retrievable from TFDA sources at this data cutoff.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to in vitro susceptibility assays and animal-model (macaque) studies using ritonavir only as part of combination ART — no study isolates ritonavir's effect or targets SIV infection as a primary clinical endpoint, and no dedicated clinical trials exist. Combined with the absence of Finland market presence and a Blocking-severity gap on core safety documentation, this candidate is not ready to advance past a research question.

**To proceed, the following is needed:**
- Finland-specific package insert / SPC (warnings, contraindications, DDI) — currently Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent (DG002)
- Clarification of therapeutic intent: SIV infection is a research/animal-model condition, not a human or veterinary disease target — next step should define whether this is pursued as a tool-compound validation or reframed toward a clinically relevant lentivirus indication
- Re-query TxGNN/ontology mapping for rank-1 (feline AIDS) to confirm or rule out the suspected disease-name mismatch before considering it further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

