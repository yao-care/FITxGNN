---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# Peginterferon Alfa-2a: From Chronic Hepatitis C to Chronic Hepatitis B

## One-Sentence Summary

> Peginterferon alfa-2a (DrugBank DB00008, brand name Pegasys) is a pegylated interferon originally developed for chronic hepatitis C treatment.
> The TxGNN model predicts it may also be effective for **Chronic Hepatitis B (hepatitis B virus infection)**,
> with **50 clinical trials** and **20 publications** currently supporting this direction — the strongest evidence base among all ten candidate indications in this evidence pack.
> Notably, the accompanying rationale indicates this is not a purely novel signal: Peginterferon alfa-2a is already an internationally approved therapy for chronic hepatitis B, so TxGNN has effectively re-identified a known, clinically validated indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C *(well-established public drug information; not recorded in the structured evidence pack — see Data Gap DG002)* |
| Predicted New Indication | Hepatitis B Virus Infection (Chronic Hepatitis B) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack (Data Gap DG002, High severity). Based on generally known pharmacological information, Peginterferon alfa-2a is a pegylated form of recombinant interferon alfa-2a. It combines **direct antiviral activity** (induction of interferon-stimulated genes that suppress viral replication) with **immune-modulatory effects** (activation of NK cells and promotion of a Th1-skewed immune response that drives HBeAg seroconversion). According to the repurposing rationale supplied with this candidate: *"Peginterferon alfa-2a has a dual mechanism — direct antiviral suppression of HBV replication plus immune modulation — which is the core pharmacological basis for HBV treatment. This is an already-approved indication of the drug, not a purely novel prediction."*

Chronic hepatitis B and chronic hepatitis C are both hepatotropic viral infections that share overlapping treatment paradigms built around interferon-based antiviral/immunomodulatory therapy. This mechanistic overlap explains why a model trained largely on the drug's hepatitis C evidence base would also surface hepatitis B with very high confidence.

Consistent with this, Peginterferon alfa-2a (Pegasys) is approved for chronic hepatitis B in multiple markets worldwide, and the clinical trial record below shows a mature, decades-long body of Phase 3/4 evidence in HBeAg-positive and HBeAg-negative chronic hepatitis B populations — reinforcing that the TxGNN signal reflects genuine, clinically confirmed pharmacology rather than a speculative repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01011738](https://clinicaltrials.gov/study/NCT01011738) | N/A (Observational) | Completed | 1,842 | Large multicenter cohort evaluating on-treatment predictors of response to Pegasys in HBeAg-positive and HBeAg-negative CHB; also assessed efficacy and safety. |
| [NCT00435825](https://clinicaltrials.gov/study/NCT00435825) | Phase 4 | Completed | 551 | 4-arm RCT comparing PEGASYS 90 vs. 180 mcg for 24 vs. 48 weeks; evaluated HBeAg seroconversion and safety in HBeAg-positive CHB. |
| [NCT02604823](https://clinicaltrials.gov/study/NCT02604823) | Phase 4 | Completed | 307 | Efficacy and safety of Pegasys in treatment-naive, interferon- or lamivudine-pretreated HBeAg-positive CHB patients (48-week treatment + 24-week follow-up). |
| [NCT01086085](https://clinicaltrials.gov/study/NCT01086085) | Phase 4 | Completed | 265 | Response-guided treatment study — rapid responders completed 48 weeks total; slow responders randomized to extended Pegasys monotherapy or Pegasys + adefovir. |
| [NCT02822547](https://clinicaltrials.gov/study/NCT02822547) | Phase 4 | Unknown | 253 | Korean study identifying eligible subjects for a response-guided stopping rule for Pegasys therapy in CHB. |
| [NCT00940485](https://clinicaltrials.gov/study/NCT00940485) | Phase 4 | Completed | 200 | Compared combination vs. sequential Pegasys + entecavir therapy in HBeAg-positive CHB patients pretreated with entecavir. |
| [NCT02908763](https://clinicaltrials.gov/study/NCT02908763) | Phase 4 | Unknown | 200 | Investigated ability of peginterferon alpha to achieve HBsAg loss/seroconversion in low-replicative CHB with low HBsAg levels. |
| [NCT00973219](https://clinicaltrials.gov/study/NCT00973219) | N/A | Completed | 151 | RCT of Peg-IFN + adefovir vs. Peg-IFN + tenofovir vs. no treatment in HBeAg-negative CHB with low viral load. |
| [NCT01706575](https://clinicaltrials.gov/study/NCT01706575) | Phase 2b | Completed | 76 | Open-label study adding Pegasys to nucleos(t)ide analogue therapy in HBeAg-negative genotype D CHB with stable HBV DNA suppression; evaluated HBsAg decline. |
| [NCT00436163](https://clinicaltrials.gov/study/NCT00436163) | Phase 4 | Completed | 39 | Baltic post-marketing program evaluating efficacy/safety of Pegasys 180 mcg weekly in treatment-naive HBeAg-positive and -negative CHB. |

*Note: 50 trials were retrieved in total for this indication; the 10 most directly relevant, HBV-specific trials are shown above.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | The New England Journal of Medicine | Landmark trial comparing Peg-IFN alfa-2a alone, Peg-IFN alfa-2a + lamivudine, and lamivudine alone in HBeAg-positive CHB — established the efficacy and safety basis for Peg-IFN alfa-2a in CHB. |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review / IPD Meta-analysis | Antiviral Therapy | Individual-participant-data meta-analysis identifying the most appropriate Peg-IFN alfa-2a stopping rules in chronic hepatitis B. |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT (Pediatric) | Hepatology | Entecavir + Peg-IFN alfa-2a combination in immune-tolerant, HBeAg-positive children with CHB. |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir + Peg-IFN alfa-2a combination in immune-tolerant adults with HBeAg-positive CHB. |
| [18220290](https://pubmed.ncbi.nlm.nih.gov/18220290/) | 2008 | Phase III Registration Trial Analysis | Hepatology | Analysis from a large 271-patient Phase III trial evaluating quantitative HBeAg and HBV DNA as outcome predictors during Peg-IFN alfa-2a therapy. |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | General review of chronic HBV infection covering epidemiology, natural history, and treatment options including Peg-IFN. |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | RCT | Virology Journal | Double-blind trial investigating long-term effects of Peg-IFN alfa-2a therapy in Japanese CHB patients. |
| [33339708](https://pubmed.ncbi.nlm.nih.gov/33339708/) | 2021 | Cohort | Journal of the Formosan Medical Association | Study of virological/immunological predictors of long-term outcomes after Peg-IFN alfa-2a therapy for HBeAg-negative CHB. |
| [31064399](https://pubmed.ncbi.nlm.nih.gov/31064399/) | 2019 | Cohort | Virology Journal | Serum HBV RNA levels evaluated as a predictor of HBeAg seroconversion during Peg-IFN alfa-2a treatment. |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nature Reviews Gastroenterology & Hepatology | Review of hepatitis B therapy goals (viral suppression, HBeAg seroconversion, HBsAg loss) and treatment response monitoring. |

*Note: 20 publications were retrieved in total for this indication; the 10 most relevant (prioritizing RCTs and systematic reviews) are shown above.*

---

## Finland Market Information

This drug is currently **not marketed in Finland** — the evidence pack records **0 authorizations** and no license entries. No dosage form, product name, or approved-indication text is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured safety data (key warnings, contraindications, or drug-drug interactions) was retrievable for this candidate in the current evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA/local package insert warnings and contraindications) that must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The predicted indication (chronic hepatitis B) is supported by the highest evidence tier in this pack (L1), including a landmark NEJM RCT, multiple Phase 3/4 studies, and a 1,842-patient observational cohort — and per the repurposing rationale, this is already a clinically established, approved use of the drug rather than a speculative new signal.
- However, the drug currently has **zero market authorizations in Finland**, and **critical safety documentation (package insert warnings/contraindications) is completely missing (Blocking Data Gap DG001)**, which prevents this candidate from clearing the initial safety screening stage (S1) in this jurisdiction.

**To proceed, the following is needed:**
- Obtain the official Finland/EU Summary of Product Characteristics (SmPC) or equivalent package insert to resolve DG001 (Blocking) before any safety evaluation.
- Obtain formal mechanism-of-action documentation from DrugBank or the manufacturer to resolve DG002 (High) and support a rigorous mechanistic-plausibility assessment.
- Confirm drug-drug interaction (DDI) data, since the current DDI query returned no results.
- Clarify the regulatory pathway for market authorization in Finland, given the drug is not currently registered there despite established international approval for this indication.

*Note: Nine additional candidate indications (ranks 2–10) were also evaluated in this evidence pack — including hepatitis E and hepatitis A virus infection, animal viral hepatitis, and several cardiac conditions — but all scored L3–L5 with weak, indirect, or apparently mismatched evidence (several appear to be ontology-mapping artifacts, e.g., "heart neoplasm" trials that are actually polycythemia vera studies). These are recommended for **Hold** or, at most, **Research Question** status and are not detailed further in this report, which focuses on the top-ranked, well-supported candidate.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

