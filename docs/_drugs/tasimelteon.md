---
layout: default
title: Tasimelteon
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: From Circadian Rhythm Sleep-Wake Regulation to Insomnia

## One-Sentence Summary

Tasimelteon (DB09071) is a melatonin MT1/MT2 receptor agonist; this evidence pack scored it against 10 TxGNN-predicted indications, and **Insomnia** is the only one that reached actionable evidence (evidence level L1, decision stage S3), while the other 9 — including the highest raw TxGNN score (bilateral parasagittal parieto-occipital polymicrogyria) — remain at Hold with no clinical trials or literature support. For insomnia specifically, **4 clinical trials** (including one completed Phase 3 RCT, n=322) and **6 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this data pack (drug not currently marketed in Finland; no license record to source an approved indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

DrugBank's mechanism-of-action field is empty in this data pack, but the literature evidence collected alongside it is consistent: tasimelteon is a non-selective **MT1/MT2 melatonin receptor agonist** that acts on the suprachiasmatic nucleus (SCN), the brain's circadian pacemaker, to phase-shift circadian rhythms and promote sleep onset (PMID 19579175, 24228714, 25207602).

No formal "original indication" is captured in this pack's regulatory data — the drug has no marketing authorization on file in Finland. However, the trial evidence itself points to insomnia as part of tasimelteon's original clinical development scope: the drug's development code, VEC-162, was studied in a completed Phase 3, double-blind, placebo-controlled trial specifically for **primary insomnia** (NCT00548340, 2007–2008). This suggests the TxGNN prediction is not identifying a novel repurposing signal so much as recovering a well-established, mechanistically direct use of the compound.

Because MT1/MT2 agonism directly targets sleep-onset physiology, the mechanistic rationale for insomnia is strong and requires no cross-indication extrapolation — unlike most of the other 9 candidates in this pack (e.g., ALS, polymicrogyria, skeletal dysplasia), which have no identifiable pathophysiological link to melatonergic signaling and no supporting evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Randomized, double-blind, placebo-controlled 5-week trial of VEC-162 (tasimelteon) 20 mg/day and 50 mg/day for primary insomnia efficacy and safety |
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Multicenter, double-blind, randomized trial of tasimelteon vs. placebo in pediatric insomnia disorder; ongoing, completion expected 2028-01 |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Proof-of-concept study of tasimelteon vs. placebo in travelers with jet lag disorder (circadian-related sleep disturbance, not classic insomnia) |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Open-label pilot assessing 20 mg tasimelteon on dream enactment and insomnia symptoms (ISI, PSQI, ESS) in REM Behavior Disorder patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | International Journal of Molecular Sciences | Reviews therapeutic effects of melatonin receptor agonists (including tasimelteon) on insomnia and comorbid disorders |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | Journal of Medicinal Chemistry | Characterizes tasimelteon as a high-affinity non-selective MT1/MT2 agonist; reviews ligands and therapeutic potential |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatric Disease and Treatment | Discusses synthetic melatoninergic agonists as an approach to insomnia management |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Current Drug Safety | Discusses melatonin and tasimelteon in the context of Alzheimer's disease-associated insomnia |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Therapeutic Advances in Neurological Disorders | Reviews melatonin analogs for sleep disturbance and neuroprotection in Parkinson's disease |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinology Letters | Reviews melatonin's role in chronobiology of sleep and cytoprotection in obesity |

---

## Finland Market Information

Tasimelteon is not currently marketed in Finland — no marketing authorizations are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3, placebo-controlled RCT (n=322) directly supports efficacy for primary insomnia, reinforced by a consistent literature base on the MT1/MT2 mechanism and an actively recruiting pediatric Phase 3 trial. However, no Finnish/EU safety labeling (warnings, contraindications, DDI) or confirmed original indication is available in this data pack, so full risk assessment cannot yet proceed to S1 safety clearance.

**To proceed, the following is needed:**
- Package insert / label data (warnings, contraindications, DDI) — currently marked as a Blocking data gap (DG001)
- Confirmed original approved indication and regulatory history for tasimelteon
- Formal DrugBank mechanism-of-action record to replace the literature-derived MOA used here
- Results of the ongoing pediatric Phase 3 trial (NCT06953869, expected completion 2028-01)
- Note: the other 9 TxGNN-predicted indications in this pack (including the top-scored polymicrogyria prediction) have no clinical trial or literature support and remain at Hold — no further action recommended on those without new evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

