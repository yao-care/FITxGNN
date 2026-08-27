---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to ALA Dehydratase Deficiency Porphyria

## One-Sentence Summary

Givosiran is a hepatic-targeted siRNA therapeutic originally used to prevent attacks in Acute Hepatic Porphyria (AHP), primarily in Acute Intermittent Porphyria (AIP), by silencing ALAS1 in the heme biosynthesis pathway. The TxGNN model additionally predicts efficacy for **ALA Dehydratase Deficiency Porphyria (ALADP)** — the rarest AHP subtype — supported by **8 publications** (including a pivotal Phase 3 RCT and one case report), though **no dedicated clinical trials** currently exist for this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Hepatic Porphyria (documented in evidence-pack literature, e.g. PMID 36028858, 35734365) |
| Predicted New Indication | ALA Dehydratase Deficiency Porphyria (ALADP) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: This drug has 10 TxGNN-predicted indications in total. Nine of them (rank 1–8, 10) are model-prediction-only (L5, no supporting evidence) with recommendation "Hold" and are not discussed further in this report. This report focuses on rank 9 — the only candidate with an actionable evidence level.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (`original_moa: [Data Gap]`). Based on known information from the evidence-pack literature, Givosiran is a small interfering RNA (siRNA) that silences hepatic ALAS1 (5-aminolevulinic acid synthase 1), the rate-limiting enzyme of the heme biosynthesis pathway. Its efficacy in Acute Hepatic Porphyria has been demonstrated in the Phase 3 ENVISION trial (PMID 36028858) and subsequent cohort studies (PMID 35067977, 40312531).

ALA Dehydratase Deficiency Porphyria (ALADP) is caused by a deficiency in ALA dehydratase, the enzyme immediately **downstream** of ALAS1 in the same heme biosynthesis pathway. Because ALAS1 inhibition reduces production of the neurotoxic precursors ALA and PBG regardless of which downstream enzyme is deficient, there is a plausible mechanistic rationale for givosiran's applicability to ALADP — this is explicitly noted in the pack's own rationale ("抑制 ALAS1 仍可降低 ALA 堆積，機轉關聯強").

However, this mechanistic plausibility is tempered by conflicting real-world evidence: a published case report (PMID 35991568) documented a **lack of clinical response** to givosiran in a confirmed ALADP patient, despite biochemical rationale. ALADP's pathophysiology also involves erythropoietic contributions not fully captured by the hepatic-ALAS1 model used in AIP, which may explain heterogeneous response. Given the extreme rarity of ALADP (fewer than 10 cases reported worldwide), no dedicated RCTs exist, and current support relies on class-level AHP trial data plus a single, discordant case report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | RCT (Phase 3, post hoc) | Orphanet Journal of Rare Diseases | ENVISION trial post hoc analysis: givosiran reduces AHP disease burden and attack rates; pivotal efficacy evidence for the AHP drug class (not ALADP-specific) |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Cohort | Journal of Internal Medicine | RNAi therapy with givosiran significantly reduces attack rates in acute intermittent porphyria |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Cohort | Scientific Reports | Expanded-access study in 10 Japanese AHP patients on monthly SC givosiran 2.5 mg/kg; supports efficacy/safety in a real-world Asian cohort |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Review | Revista clinica espanola | Therapeutic approach to acute hepatic porphyria crises; identifies ALA dehydratase deficiency as one of four AHP subtypes sharing the ALAS1-driven mechanism |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review | Drug Design, Development and Therapy | Overview of givosiran's design, development, and place in therapy for adults with AHP |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | RNA interference therapy in AHP; confirms ALAS1 induction as the shared upstream driver across AHP subtypes |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK/PD | CPT: Pharmacometrics & Systems Pharmacology | PK/PD model of urinary ALA reduction after givosiran across pooled Phase I–III trial data |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Case Report | Frontiers in Genetics | **Directly relevant to ALADP**: reports lack of clinical response to givosiran in a confirmed ALAD porphyria patient, despite biochemical rationale — key contradicting signal |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale (ALAS1 acting upstream of ALA dehydratase in the same heme biosynthesis pathway) is well supported by AHP-class RCT and cohort evidence, but the only ALADP-specific data point — a case report — showed lack of response, and no dedicated trials exist for this ultra-rare subtype. Evidence is directionally supportive but not yet sufficient for unconditional advancement.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (currently Blocking data gap, DG001)
- Confirmed DrugBank mechanism of action detail (currently High-severity data gap, DG002)
- Additional ALADP case series or registry data to reconcile the conflicting case report
- Drug interaction (DDI) profile (currently `not_found`)
- Regulatory pathway assessment, given the drug is not currently marketed in Finland (0 authorizations)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

