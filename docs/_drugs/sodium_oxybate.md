---
layout: default
title: Sodium Oxybate
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 6
---

# Sodium Oxybate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Sodium Oxybate: From Narcolepsy with Cataplexy to Insomnia

## One-Sentence Summary

Sodium oxybate (Xyrem) is a GABA-B/GHB receptor agonist established for narcolepsy with cataplexy in the EU/US. The TxGNN model predicts it may also be effective for **Insomnia**, with **13 clinical trials** and **13 publications** currently identified, though the drug is not marketed in Finland and carries controlled-substance (Schedule III) risk.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy with cataplexy (per international literature; not derivable from Finland licensing data — drug not marketed) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism of action data is currently a data gap (DG002). Based on the mechanistic rationale available in the evidence pack, sodium oxybate (the sodium salt of gamma-hydroxybutyrate, GHB) acts as a GABA-B/GHB receptor agonist that induces and consolidates slow-wave sleep (SWS). This effect has been clinically validated in narcolepsy, where it improves sleep consolidation and reduces cataplexy attacks.

Narcolepsy and insomnia are both primary sleep-architecture disorders, so the pharmacological logic — enhancing SWS to improve sleep continuity — is mechanistically transferable. Directly supporting this, a completed Phase 2 randomized, double-blind, placebo-controlled trial (NCT00383643) compared sodium oxybate against zolpidem (Ambien) specifically in chronic insomnia patients, which is the strongest available evidence for this candidate.

However, the mechanism is not insomnia-specific: it is a generalized CNS/sleep-architecture effect rather than a targeted insomnia pathway, and several of the identified trials in related sleep-disturbance populations (PTSD, chronic fatigue syndrome) were withdrawn or terminated, suggesting practical or tolerability barriers to broader use. The drug's Schedule III controlled status, dependence/abuse potential, and respiratory depression risk (noted in the repurposing rationale) also temper enthusiasm for a mechanism that is otherwise plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00383643](https://clinicaltrials.gov/study/NCT00383643) | Phase 2 | Completed | 48 | Randomized, double-blind, double-dummy, placebo-controlled trial comparing sodium oxybate (Xyrem) vs. zolpidem (Ambien) for chronic insomnia — the most directly relevant and strongest trial for this indication |
| [NCT02637648](https://clinicaltrials.gov/study/NCT02637648) | Phase 3 | Unknown | 60 | Sodium oxybate for headache and sleep disturbance prophylaxis in cluster headache; sleep quality was a secondary outcome, status unknown |
| [NCT00330291](https://clinicaltrials.gov/study/NCT00330291) | Phase 2 | Withdrawn | 0 | Planned trial of Xyrem for treatment-refractory insomnia due to PTSD; withdrawn with no enrollment |
| [NCT00641186](https://clinicaltrials.gov/study/NCT00641186) | Phase 2 | Completed | 30 | Open-label trial of Xyrem for excessive daytime sleepiness and nocturnal sleep disturbance in mild-to-moderate Parkinson's disease |
| [NCT04803786](https://clinicaltrials.gov/study/NCT04803786) | N/A | Completed | 110 | Observational study (TENOR) on real-world dosing/transition experience of narcolepsy patients switching from Xyrem to Xywav |
| [NCT04508166](https://clinicaltrials.gov/study/NCT04508166) | N/A | Completed | 27 | Healthy-volunteer study testing whether deep-sleep enhancement (including a GHB-class agent) reduces post-traumatic intrusive memories |
| [NCT00594256](https://clinicaltrials.gov/study/NCT00594256) | Phase 2 | Completed | 8 | Open-label pilot of adjunctive Xyrem for persistent schizophrenia symptoms and associated sleep disturbance |
| [NCT01584934](https://clinicaltrials.gov/study/NCT01584934) | Phase 4 | Withdrawn | 0 | Planned double-blind, randomized crossover trial of sodium oxybate for chronic fatigue syndrome-related sleep disturbance; withdrawn |
| [NCT07077278](https://clinicaltrials.gov/study/NCT07077278) | Phase 4 | Not yet recruiting | 25 | Randomized withdrawal study of low-sodium oxybate for autonomic symptoms in idiopathic hypersomnia patients with POTS |
| [NCT03626727](https://clinicaltrials.gov/study/NCT03626727) | Early Phase 1 | Withdrawn | 0 | Planned open-label trial of Xyrem for post-traumatic narcolepsy and hypersomnia in TBI patients; withdrawn |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40120323](https://pubmed.ncbi.nlm.nih.gov/40120323/) | 2025 | Cohort | J Clin Neurosci | Propensity-matched cohort characterizing treatment patterns of patients on immediate-release sodium oxybate for narcolepsy |
| [18852348](https://pubmed.ncbi.nlm.nih.gov/18852348/) | 2008 | Cohort | Archives of Neurology | Open-label polysomnographic study of sodium oxybate for excessive daytime sleepiness in Parkinson disease |
| [11174231](https://pubmed.ncbi.nlm.nih.gov/11174231/) | 2001 | Review | Annals of Emergency Medicine | Describes GHB (gamma-hydroxybutyrate) withdrawal syndrome — relevant safety signal for dependence risk |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | Expert Opin Emerging Drugs | Review of emerging narcolepsy treatments including sodium oxybate's role in nocturnal sleep disruption |
| [26171909](https://pubmed.ncbi.nlm.nih.gov/26171909/) | 2015 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of opioid/hypnotic/sedating medication effects on sleep-disordered breathing, relevant to CNS depressant risk |
| [31526967](https://pubmed.ncbi.nlm.nih.gov/31526967/) | 2019 | Case report | Sleep Medicine | Sodium oxybate used to manage severe sleep deprivation in a child with EBV encephalitis affecting the sleep-wake regulation system |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Revue Neurologique | Review of narcolepsy with cataplexy, including sleep-maintenance insomnia as a disease feature |
| [21815499](https://pubmed.ncbi.nlm.nih.gov/21815499/) | 2011 | Review | Revue Medicale Suisse | Review of the bidirectional relationship between chronic pain and sleep disorder, discussing hypnotic approaches |
| [37590830](https://pubmed.ncbi.nlm.nih.gov/37590830/) | 2023 | Review | Continuum (Minneap Minn) | Comprehensive review of pediatric sleep disorders including insomnia and narcolepsy |
| [20082966](https://pubmed.ncbi.nlm.nih.gov/20082966/) | 2009 | Review | Parkinsonism Relat Disord | Review of sleepiness and sleep disturbance in Parkinson's disease |

---

## Finland Market Information

Sodium oxybate currently has no marketing authorizations recorded for Finland (0 licenses; market status: not marketed).

---

## Safety Considerations

Official Fimea package insert warnings and contraindications are currently unavailable (Blocking data gap, DG001) — this prevents a formal S1 safety evaluation. Based on information present elsewhere in the evidence pack (mechanistic rationale and literature), the following risks are relevant and should be verified once the package insert is obtained:

- **Controlled substance risk**: Sodium oxybate (GHB) is a Schedule III controlled substance with known dependence, abuse, and diversion potential (supported by literature on GHB withdrawal syndrome and tolerability/abuse liability).
- **CNS/respiratory depression**: Additive sedative and respiratory depression risk when combined with alcohol or other CNS depressants.
- **Movement/sleep side effects**: Case literature associates sodium oxybate with induction or worsening of restless legs syndrome/periodic limb movements in narcolepsy patients — a paradoxical sleep-disruption effect worth monitoring if repurposed for insomnia.

Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia signal has meaningful supporting evidence (L2: one completed Phase 2 RCT directly comparing sodium oxybate to zolpidem in chronic insomnia), but a Blocking data gap on Fimea warnings/contraindications (DG001) prevents the required S1 safety evaluation, and the drug's controlled-substance/abuse-risk profile combined with its unmarketed status in Finland warrants caution before advancing.

**To proceed, the following is needed:**
- Fimea package insert (warnings, contraindications, controlled-substance scheduling in Finland) — DG001
- DrugBank mechanism of action detail — DG002
- Formal drug-drug interaction (DDI) database query (current query returned no results)
- Assessment of controlled-substance import/prescribing feasibility for an unmarketed product in Finland
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

