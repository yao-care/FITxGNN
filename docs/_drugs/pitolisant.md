---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 3
---

# Pitolisant
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

# Pitolisant: From Narcolepsy to Insomnia

## One-Sentence Summary

Pitolisant is a histamine H3 receptor inverse agonist originally developed and internationally approved for excessive daytime sleepiness in narcolepsy (with or without cataplexy) and residual sleepiness in OSA — it is not currently marketed in this jurisdiction. The TxGNN model predicts it may be effective for **Insomnia**, but this prediction is mechanistically counter-intuitive (a wake-promoting drug for a sleep-inducing indication) and is supported only by **1 withdrawn, zero-enrollment trial** and **8 publications**, none of which directly studied insomnia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy with/without cataplexy, excessive daytime sleepiness in OSA (per international literature; no local registration data exists) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed official mechanism of action data is not available (flagged as a High-severity data gap). Based on the literature collected in this evidence pack, pitolisant is a selective histamine H3 receptor inverse agonist/antagonist. By blocking H3 autoreceptors, it increases histamine, norepinephrine, and acetylcholine release in the brain, producing a wake-promoting effect. This mechanism underlies its approved use for excessive daytime sleepiness in narcolepsy and its investigational use for residual sleepiness in CPAP-treated OSA patients.

This mechanistic direction runs **counter to** the proposed new indication. A drug designed to increase wakefulness is pharmacologically more likely to induce or worsen insomnia than to treat it — indeed, insomnia is a known adverse effect of H3 receptor antagonism in clinical use. The single registered trial in this evidence pack (NCT02800083) was not actually an insomnia trial; it targeted alcohol use disorder, was withdrawn, and enrolled zero patients, so it provides no usable signal for sleep-related endpoints. None of the 8 supporting publications studied pitolisant for insomnia — they cover narcolepsy pharmacology, OSA-related daytime sleepiness, and general H3 receptor biology.

The TxGNN score most likely reflects a semantic proximity between "sleep disorder" concepts in the model's embedding space (narcolepsy, OSA, insomnia are all sleep-related nodes) rather than a genuine therapeutic relationship. This prediction should be treated as a candidate requiring mechanistic reassessment, not a validated repurposing lead.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Designed to evaluate pitolisant for alcohol use disorder (reduction in heavy drinking days), with secondary endpoints touching on mental health/sleep improvement. Trial was withdrawn with zero enrollment, so no efficacy or safety data were generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet. Neurology | Phase 3 trial confirming safety/efficacy of pitolisant in pediatric narcolepsy with/without cataplexy — not an insomnia study. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant reduced residual excessive daytime sleepiness in CPAP-adherent OSA patients — a wake-promoting effect, opposite direction to insomnia treatment. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Pitolisant improved daytime sleepiness in OSA patients refusing CPAP — again a wake-promoting outcome. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de neurología | Real-world "WAKE study" on pitolisant effectiveness/safety in treatment-refractory type 1 narcolepsy. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | General review of brain histamine receptors (H1–H4) in health and disease; no insomnia-specific data. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Review of pitolisant's development and therapeutic role in narcolepsy. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Reviews histaminergic system changes in neuropsychiatric disorders; notes pitolisant is used for narcolepsy sleepiness, contrasted with H1-antagonist doxepin used for insomnia. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | Early report on pitolisant as a stimulant alternative for refractory sleepiness in narcolepsy-cataplexy. |

None of the eight publications evaluate pitolisant as a treatment for insomnia; several explicitly document its wake-promoting profile.

---

## Other Predicted Indications (Lower Priority, Not Detailed Above)

- **ADHD** (score 99.36%, Evidence Level L5): Plausible mechanistic rationale via H3-receptor-mediated cortical arousal/cognition pathways, but **zero registered clinical trials** and 7 supporting papers are all general H3-receptor pharmacology reviews with no direct ADHD trial data. Recommendation: Hold.
- **Faciodigitogenital syndrome (Aarskog-Scott syndrome)** (score 99.29%, Evidence Level L5): No identifiable biological link — this is an FGD1 gene mutation-driven X-linked developmental disorder unrelated to histamine H3 signaling. Zero trials, zero literature. Assessed as likely model noise from sparse rare-disease ontology embeddings. Recommendation: Hold.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (insomnia) is mechanistically implausible given pitolisant's wake-promoting pharmacology, and its only associated trial was withdrawn with zero enrollment. The two lower-ranked predictions (ADHD, faciodigitogenital syndrome) have even weaker evidentiary support (L5 — model prediction only, no clinical or, in the case of faciodigitogenital syndrome, mechanistic support). None of the three candidates meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently a Blocking data gap — cannot complete S1 safety screening without it)
- Confirmed DrugBank mechanism of action record (currently a High-severity data gap)
- If insomnia remains of interest, a mechanistic explanation for how an H3 inverse agonist could treat rather than induce insomnia, ideally with new preclinical or clinical data, before further evaluation
- DDI dataset (current query returned no results) before any safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

