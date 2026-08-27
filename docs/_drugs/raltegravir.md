---
layout: default
title: Raltegravir
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

Using the evidence pack as given — no skill needed here, this is a direct report-generation task per the system prompt's own spec.

# Raltegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Raltegravir is an HIV-1 integrase strand-transfer inhibitor, originally used to treat HIV-1 infection in humans (its formal indication record and DrugBank MOA entry are currently data gaps, but this pharmacological class is confirmed within the evidence pack's own mechanistic notes). The TxGNN model predicts possible efficacy against **Feline Acquired Immunodeficiency Syndrome (FIV / feline AIDS)**, but this direction is currently supported by only **2 clinical trials — both of which turn out to be unrelated human HIV-1 studies, not feline data** — and **0 dedicated publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection *(inferred from confirmed pharmacological class — integrase strand-transfer inhibitor; formal indication list and DrugBank MOA record are open data gaps, see below)* |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.78% (rank 2784 of model output) |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for raltegravir is formally a data gap (DG002), but the evidence pack's own repurposing rationale confirms raltegravir's known pharmacology: it is an **HIV-1 integrase strand-transfer inhibitor**, blocking the enzyme responsible for integrating retroviral DNA into the host genome.

FIV (Feline Immunodeficiency Virus) and HIV both belong to the *Lentivirus* genus, and their integrase enzymes are theorized to be structurally conserved, giving a plausible cross-species mechanistic rationale for raltegravir's activity against FIV. However, **no feline-specific pharmacological, pharmacokinetic, or clinical data exist in this evidence pack** — the two clinical trials retrieved (NCT01231516, NCT01227824) are both human HIV-1 trials comparing raltegravir to dolutegravir, incorrectly linked to this indication by the knowledge graph (disease-entity mismatch, graded "C" relevance in both cases). No supporting literature was found either.

Notably, a closely related predicted indication in this same evidence pack — **Simian Immunodeficiency Virus (SIV) infection** — is backed by much stronger evidence: 19 publications, including direct animal-model efficacy data (e.g., PMID 20233398, raltegravir tested in SIVmac251-infected macaques). Because SIV and FIV share the same lentiviral integrase-conservation logic, this related finding lends indirect biological plausibility to the FIV hypothesis, even though it does not substitute for feline-specific data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Human HIV-1 trial: dolutegravir vs. raltegravir (integrase-inhibitor-naïve, ART-experienced adults). **Not a feline/FIV study — flagged as disease-entity mismatch (relevance grade C).** |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Human HIV-1 trial: dolutegravir vs. raltegravir in treatment-naïve adults. **Not a feline/FIV study — flagged as disease-entity mismatch (relevance grade C).** |

Neither trial provides usable evidence for the FIV indication; both were retrieved due to a knowledge-graph linkage error rather than genuine relevance.

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Raltegravir currently has no marketing authorization on file in Finland (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA package insert retrieval is an open Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (FIV) sits at evidence level L4 with no genuine clinical trial or literature support — the only trials retrieved are irrelevant human HIV-1 studies. While the lentivirus/integrase mechanistic rationale is plausible and indirectly reinforced by stronger SIV-infection evidence elsewhere in this pack, there is currently no feline-specific data to justify advancing past a research hypothesis.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): TFDA/Finland package insert — warnings and contraindications
- Resolve DG002: Confirmed DrugBank mechanism-of-action record
- Direct feline pharmacokinetic, dosing, and safety data (no veterinary studies currently exist in this pack)
- Correction of the clinical-trial knowledge-graph linkage that mismatched human HIV-1 trials to this feline indication
- Consider prioritizing the better-supported related prediction — **Simian Immunodeficiency Virus Infection** (L3, "Research Question", 19 publications including direct animal efficacy data) — as a nearer-term research pathway before pursuing FIV directly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

