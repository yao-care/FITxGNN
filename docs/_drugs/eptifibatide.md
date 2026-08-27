---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

Using the **data-report** discipline (no fabrication, no reformatting/omitting of source data) to build this from the evidence pack as given. Before drafting I want to flag one judgment call I made explicit in the report itself:

**Note on indication selection:** This evidence pack (`candidate_id: TW-DB00063-multi`) lists 10 TxGNN-predicted indications. Rank #1 by raw score (`rheumatoid arthritis`) has **zero** supporting trials/literature (L5/Hold). The indication with actual clinical trial + literature support is **hemoglobinopathy** (rank 7, L2, decision_stage S2) — a completed Phase I/II RCT plus 4 papers, all specifically studying eptifibatide in sickle cell disease. I used **hemoglobinopathy** as the report's headline indication (not literal `predicted_indications[0]`), since a report built on the zero-evidence top-score entry would be empty and non-actionable. I've also added a compact "Other TxGNN Signals" section so the remaining 9 predictions aren't lost.

Also: `original_indications` and `taiwan_regulatory.licenses` are both empty (data gap) — eptifibatide's ACS/unstable-angina use is stated only implicitly, inside the literature abstracts themselves (e.g. PMID 17916103, 24678072), not in a formal indication field. I've flagged this sourcing explicitly rather than presenting it as confirmed regulatory data.

---

# Eptifibatide: From Acute Coronary Syndrome to Hemoglobinopathy (Sickle Cell Disease)

## One-Sentence Summary

Eptifibatide is a GPIIb/IIIa (platelet integrin αIIbβ3) antagonist whose established use — per the literature evidence collected in this pack — is acute coronary syndrome (ACS)/unstable angina; no formal original-indication or MOA field was available in this evidence pack. TxGNN predicts potential efficacy in **hemoglobinopathy (sickle cell disease spectrum)**, currently supported by **1 completed Phase I/II clinical trial** and **4 publications** directly studying eptifibatide in sickle cell disease patients. Evidence is early-stage: the only dedicated trial was terminated with just 13 patients enrolled.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) / Unstable Angina — inferred from literature context only; no formal indication or local license data is available (drug is not marketed in this market) |
| Predicted New Indication | Hemoglobinopathy (Sickle Cell Disease spectrum) |
| TxGNN Prediction Score | 99.98% (0.9998089671134948) |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data (`original_moa`) is a **data gap** in this evidence pack (DG002, High severity). However, the literature evidence gathered under the hemoglobinopathy indication itself consistently and independently confirms the mechanism: eptifibatide is repeatedly described as a **synthetic peptide antagonist of the platelet integrin receptor GPIIb/IIIa (αIIbβ3)**, which blocks fibrinogen-mediated platelet aggregation (e.g., PMID 17916103, PMID 23973010). This receptor blockade is the pharmacological basis for its established use in acute coronary syndromes, where platelet aggregation drives thrombus formation.

Sickle cell disease shares a related — though pathophysiologically distinct — final common pathway: acute painful crises and vaso-occlusive events are increasingly understood to involve **platelet activation and platelet–erythrocyte–endothelial cell interactions**, not just erythrocyte sickling alone (as directly discussed in PMID 17916103 and the in-vitro microfluidic model PMID 22156199). Inhibiting GPIIb/IIIa is therefore mechanistically plausible as a way to reduce microvascular thrombosis and downstream inflammatory signaling during vaso-occlusive crises, and this hypothesis has already been tested — not merely theorized — in a dedicated Phase I/II clinical trial (NCT00834899) and three supporting clinical/translational papers.

It is important to note that this mechanistic link is specific to the broader "hemoglobinopathy/sickle cell disease" cluster. The TxGNN model also separately scored several narrower sickle-cell genotype variants (HbSD, HbS/β-thalassemia, HbSE, HbSC, HPFH-sickle cell) at comparable or higher scores, but **none of these genotype-specific predictions have any direct supporting trial or literature data** — the rationale for those is explicitly described in the evidence pack as an indirect extrapolation from the general sickle cell disease evidence base, not independent confirmation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1, Phase 2 | Terminated | 13 | Randomized, double-blind, placebo-controlled study evaluating the safety of eptifibatide for acute pain episodes in sickle cell disease. Tested the hypothesis that platelet activation and resultant inflammation contribute to sickle cell painful crises. Enrollment stopped early (13 of planned target), limiting statistical power. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase 1 clinical trial | British Journal of Haematology | First-in-disease Phase I study of eptifibatide in 4 sickle cell anaemia patients in steady state; established safety and pharmacodynamic (platelet inhibition) data, drawing an explicit analogy to its established ACS use. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot clinical study | Thrombosis Research | Pilot study evaluating safety and efficacy of eptifibatide during acute painful episodes in sickle cell disease patients. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Clinical trial sub-analysis (inflammatory markers) | American Journal of Hematology | Sub-analysis of eptifibatide's effect on inflammation markers during acute pain episodes in sickle cell disease (likely derived from the same trial population as above). |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In vitro model study | The Journal of Clinical Investigation | Microfluidic "endothelialized" microvasculature model recapitulating microvascular occlusion/thrombosis in hematologic diseases including sickle cell disease; supports the platelet–endothelial mechanistic rationale but is not a clinical study of eptifibatide itself. |

*Note: one additional literature hit was returned under the related "HbSC disease" entry (PMID 24678072) but was explicitly flagged in that entry's own rationale as being about eptifibatide in acute coronary syndrome patients generally, not hemoglobinopathy — it was excluded here as low relevance.*

---

## Finland Market Information

Eptifibatide is **not currently marketed** in this market (`market_status: 未上市`), and there are **0 registered authorizations**. No product name, dosage form, or approved-indication license text is available to tabulate.

---

## Other TxGNN Signals (Lower Evidence, for Completeness)

Since this evidence pack scored 10 candidate indications for eptifibatide, the remaining 9 are summarized here rather than omitted:

| Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Rheumatoid arthritis | 99.99% | L5 | Hold | Top score, but zero trials/literature — pure model prediction |
| Sickle cell–hemoglobin D disease | 99.98% | L4 | Research Question | No direct data; extrapolated from sickle cell disease evidence |
| Sickle cell–β-thalassemia disease | 99.98% | L4 | Research Question | Same extrapolation basis |
| Sickle cell–hemoglobin E disease | 99.98% | L4 | Research Question | Same extrapolation basis |
| HPFH–sickle cell disease | 99.98% | L4 | Research Question | Same extrapolation basis |
| Sickle cell–hemoglobin C disease | 99.98% | L4 | Research Question | Only cited literature (PMID 24678072) is off-target (general ACS population) |
| Female breast carcinoma | 99.97% | L4 | Hold | In vitro/organ-on-chip evidence only (e.g., PMID 25090985); no in vivo or clinical data |
| β-thalassemia with other manifestations | 99.97% | L5 | Hold | No trials/literature; weak mechanistic rationale (no sickling pathology) |
| Partial deletion of chromosome 16p | 99.96% | L5 | Hold | No biological link identified; likely a knowledge-graph co-occurrence artifact |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug–drug interaction data are all recorded as data gaps in this evidence pack — DG001, Blocking severity, "TFDA package insert warnings/contraindications" — and DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for eptifibatide in sickle cell disease/hemoglobinopathy is grounded in an actual dedicated Phase I/II RCT plus three supporting clinical/translational papers (L2 evidence) — clearly the strongest signal in this pack. However, that trial was **terminated early with only 13 of its planned participants enrolled**, and no larger confirmatory trial exists. Combined with a **Blocking** data gap on safety warnings/contraindications (DG001) and a **High**-severity gap on formal mechanism-of-action confirmation (DG002), the evidence is not yet sufficient to proceed to guardrail-based deployment.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank-confirmed mechanism-of-action text (DG002)
- A larger, adequately powered controlled trial in sickle cell disease (the only existing trial, NCT00834899, was terminated at n=13)
- Drug–drug interaction (DDI) data, currently returning no results
- Clarification of whether the narrower sickle-cell genotype predictions (HbSD, HbSC, etc.) warrant separate evaluation, or should remain bundled under the general hemoglobinopathy signal until genotype-specific data becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

