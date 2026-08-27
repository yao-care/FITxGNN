---
layout: default
title: Agomelatine
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: From Major Depressive Disorder to Depressive/Neurotic-Spectrum Disorders

## One-Sentence Summary

Agomelatine is a melatonergic antidepressant whose approved use — confirmed only through literature in this evidence pack, since structured DrugBank/Fimea fields are data gaps — is major depressive disorder (MDD) in adults. TxGNN surfaced ten candidate indications for this drug; the five that carry any supporting evidence (agoraphobia, neurotic disorder, melancholia, neurotic depression, dysthymic disorder) all fall inside the depression/neurotic-disorder spectrum and are backed by **0 clinical trials** and **28 unique publications** (mostly class-level antidepressant evidence rather than indication-specific trials). The other five top-ranked predictions — including benign paroxysmal torticollis of infancy and four ultra-rare genetic syndromes — have **zero supporting evidence** and are almost certainly graph-embedding noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (MDD) — inferred from literature in this pack; not confirmed via DrugBank or Fimea structured records (data gap) |
| Predicted New Indication | Melancholia (lead candidate within a 5-indication depressive/neurotic-spectrum cluster — see full ranking below) |
| TxGNN Prediction Score | 99.88% (melancholia, model rank #1740 among all disease pairs; graph rank #4 among this drug's top-10 candidates) |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

### Full Candidate Ranking (all 10 TxGNN predictions)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------------|-----------------|-----------------|-----------------|
| 1 | Benign paroxysmal torticollis of infancy | 99.96% | L5 | S0 | Hold (no biological or literature link) |
| 2 | Agoraphobia | 99.95% | L4 | S0 | Hold |
| 3 | Neurotic disorder | 99.90% | L4 | S0 | Hold |
| 4 | **Melancholia** | 99.88% | L2 | S2 | Research Question |
| 5 | Neurotic depression | 99.88% | L2 | S2 | Research Question |
| 6 | Ohdo syndrome and variants | 99.87% | L5 | S0 | Hold (genetic syndrome, unrelated mechanism) |
| 7 | Dysthymic disorder | 99.86% | L3 | S1 | Research Question |
| 8 | Ligneous conjunctivitis | 99.83% | L5 | S0 | Hold (unrelated mechanism) |
| 9 | Blepharophimosis–intellectual disability syndrome, Ohdo type | 99.82% | L5 | S0 | Hold (genetic syndrome) |
| 10 | Keppen-Lubinsky syndrome | 99.81% | L5 | S0 | Hold (genetic syndrome) |

Only ranks 4, 5, and 7 (melancholia, neurotic depression, dysthymic disorder) — plus, more weakly, ranks 2 and 3 (agoraphobia, neurotic disorder) — have any literature support at all. Ranks 1, 6, 8, 9, and 10 have no clinical trials, no ICTRP records, and no literature hits in this evidence pack; they are treated here as low-confidence model artifacts rather than genuine repurposing signals.

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data from DrugBank is a documented data gap (DG002) in this pack. Based on the literature retrieved, agomelatine is described consistently as a melatonergic MT1/MT2 receptor agonist combined with 5-HT2C (and 5-HT2B) serotonin receptor antagonism — a mechanism that normalizes disrupted circadian rhythms while also enhancing dopamine and noradrenaline release in the prefrontal cortex, distinguishing it from classic monoaminergic antidepressants (PMID 19777735, 23484857, 32568567, 30759026).

Melancholia, neurotic depression, and dysthymic disorder are not truly distinct diseases from a mechanistic standpoint — they are historical or nosological subtypes and near-synonyms sitting within the same depressive-disorder spectrum as agomelatine's own approved indication. Their mechanistic plausibility is therefore high, but this also means the "repurposing" signal here is largely a naming/ontology overlap rather than a genuine extension into an unrelated disease area. Agoraphobia and neurotic disorder are more indirect: they are often comorbid with depression, so a benefit could plausibly arise from agomelatine's antidepressant/anxiolytic-adjacent effect, but neither has literature that studies the drug in that population directly — the single citation for agoraphobia (PMID 21183900) actually studies valdoxan's response predictors in moderate-to-severe depression, not agoraphobia itself.

By contrast, the five rare-disease/genetic-syndrome predictions (benign paroxysmal torticollis of infancy, Ohdo syndrome and its variants, ligneous conjunctivitis, Keppen-Lubinsky syndrome) have no identifiable mechanistic link to melatonergic/serotonergic pharmacology and no supporting literature or trials at all — these are best interpreted as knowledge-graph proximity artifacts rather than credible repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. Across all 10 predicted indications, both ClinicalTrials.gov and ICTRP queries returned zero results (confirmed in the query log for every disease pair tested).

---

## Literature Evidence

The table below consolidates and deduplicates literature across the five evidenced indications (agoraphobia, neurotic disorder, melancholia, neurotic depression, dysthymic disorder), prioritizing meta-analyses/RCT-level and agomelatine-specific evidence, and showing the top 10 of 28 unique publications identified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network Meta-analysis (RCTs) | Lancet | Compares efficacy/acceptability of 21 antidepressants (including agomelatine) for acute MDD treatment; class-level evidence relevant to melancholia/neurotic depression |
| [39684343](https://pubmed.ncbi.nlm.nih.gov/39684343/) | 2024 | Systematic Review/Meta-analysis (agomelatine-specific) | Int J Mol Sci | Efficacy and safety of agomelatine specifically in depressed patients with comorbid diabetes |
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis (placebo-controlled RCTs, class-level) | J Clin Psychiatry | Antidepressant efficacy specifically in dysthymic disorder vs. MDD — most disease-specific evidence in the set |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review/NMA | Molecular Psychiatry | Antidepressant efficacy/safety in the MDD maintenance phase |
| [25911132](https://pubmed.ncbi.nlm.nih.gov/25911132/) | 2015 | Systematic Review (RCT dose-equivalence) | J Affect Disord | Dose-equivalence of antidepressants from randomized trials |
| [32568567](https://pubmed.ncbi.nlm.nih.gov/32568567/) | 2020 | Review (agomelatine-specific) | Expert Opin Drug Discov | Preclinical discovery and development of agomelatine for depression |
| [21183900](https://pubmed.ncbi.nlm.nih.gov/21183900/) | 2010 | Cohort/Observational (post-hoc predictor analysis) | Zh Nevrol Psikhiatr | Clinical predictors of response to valdoxan (agomelatine) in moderate/severe depression — cited as agoraphobia evidence but not disease-specific |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic Review/NMA | Lancet | Cardiometabolic and physiological effects across antidepressants |
| [39072578](https://pubmed.ncbi.nlm.nih.gov/39072578/) | 2024 | Review | Zh Nevrol Psikhiatr | General antidepressant selection guidance, explicitly mentions "neurotic disorder" as a treatment target |
| [23484857](https://pubmed.ncbi.nlm.nih.gov/23484857/) | 2013 | Review | Expert Opin Investig Drugs | Mechanistic review linking melatonin/circadian disruption to depressive disorder |

---

## Finland Market Information

Agomelatine is **not currently marketed in Finland** (0 authorizations recorded). No Fimea license records are available in this evidence pack, so authorization numbers, product names, dosage forms, and approved indication text cannot be presented.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in this evidence pack (key warnings, contraindications, drug interactions) are data gaps — no Fimea/TFDA package insert data was retrievable. Note that this gap (DG001) is flagged as **Blocking** severity in the source data, meaning this candidate cannot yet proceed to a formal S1 safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap (DG001: no Fimea/TFDA package insert or safety data) prevents even an initial S1 safety screen, regardless of how promising the efficacy signal looks.
- The best-supported candidates (melancholia, neurotic depression, dysthymic disorder) reach only L2–L3 evidence and Research Question status — they rely on class-level antidepressant literature rather than indication-specific trials, and largely overlap in nomenclature with agomelatine's existing depression indication rather than representing a genuinely novel disease area.
- Five of the ten top-ranked predictions have no supporting evidence whatsoever and should be deprioritized as likely model noise.

**To proceed, the following is needed:**
- Resolve DG001 (Fimea/TFDA package insert — warnings, contraindications, DDI) before any safety-stage review can begin.
- Resolve DG002 (formal DrugBank mechanism-of-action record) to properly validate the mechanistic rationale currently based only on literature.
- If pursuing the depressive/neurotic-spectrum cluster, clarify with clinical/regulatory experts whether melancholia, neurotic depression, and dysthymic disorder represent a genuinely distinct labeling opportunity versus overlap with the existing MDD indication.
- Drop or deprioritize the five zero-evidence predictions (benign paroxysmal torticollis of infancy, Ohdo syndrome and variants, ligneous conjunctivitis, blepharophimosis–ID syndrome Ohdo type, Keppen-Lubinsky syndrome) pending any future contradicting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

