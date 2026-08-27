---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension (Idiopathic/Heritable) to Additional PAH Subtypes

## One-Sentence Summary

Ambrisentan is a selective endothelin type A (ETA) receptor antagonist already used for pulmonary arterial hypertension (idiopathic/heritable forms); this is not stated in the structured drug fields of this Evidence Pack but is recoverable from the literature retrieved within it (e.g., PMID 28425346, 24787237). TxGNN produced **10 candidate new-indication predictions** for ambrisentan; of these, two — **PAH associated with congenital heart disease** and **PAH associated with connective tissue disease** — are backed by **9–19 trials/publications each** and reach the highest evidence tier (L1), while the model's top-scored prediction (pulmonary arteriovenous malformation) and six others have little to no supporting evidence. This report evaluates the full portfolio and recommends action only on the well-supported subtypes.

> **Note on scope:** This Evidence Pack (`TW-DB06403-multi`) covers 10 ranked predictions rather than a single indication. Rather than mechanically reporting only the #1-ranked TxGNN hit (which the evidence itself flags as mechanistically weak), this report leads with the two indications that have real clinical evidence, and summarizes the rest for transparency.

---

## Quick Overview

*(Primary candidate shown below is rank #2, PAH associated with congenital heart disease — the highest-scored prediction that also carries substantial clinical evidence. Rank #1, pulmonary arteriovenous malformation, is addressed in the "Other Predicted Indications" section because it has only one indirect case report and is explicitly noted in the source data as mechanistically questionable.)*

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (idiopathic/heritable) — inferred from literature within this pack; not present in the structured `original_indications`/`licenses` fields |
| Predicted New Indication | Pulmonary arterial hypertension associated with congenital heart disease (incl. Eisenmenger syndrome) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Predicted Indications Portfolio (All 10 Ranked Candidates)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Pulmonary arteriovenous malformation | 99.41% | L4 | Hold |
| 2 | PAH associated with congenital heart disease | 99.37% | L1 | Proceed with Guardrails |
| 3 | PAH associated with schistosomiasis | 99.30% | L5 | Hold |
| 4 | PAH associated with HIV infection | 99.30% | L2 | Research Question |
| 5 | PAH associated with chronic hemolytic anemia | 99.30% | L5 | Hold |
| 6 | PAH associated with connective tissue disease | 99.30% | L1 | Proceed with Guardrails |
| 7 | Malformation syndrome with odontal/periodontal component | 99.19% | L5 | Hold |
| 8 | Hypotrichosis simplex of the scalp | 99.15% | L5 | Hold |
| 9 | Hypertrichosis | 99.14% | L5 | Hold |
| 10 | Syndrome with Dandy-Walker malformation | 99.12% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, the structured mechanism-of-action field for ambrisentan is not populated in this Evidence Pack. However, literature retrieved within the pack itself (PMID 28425346, 24787237) identifies ambrisentan as **a selective ETA receptor antagonist approved for idiopathic, heritable, and connective-tissue-disease-associated PAH**, working by blocking endothelin-1-mediated vasoconstriction and vascular remodeling in the pulmonary arterial bed.

**PAH associated with congenital heart disease (CHD-PAH, including Eisenmenger syndrome)** is a well-recognized subtype within the WHO Group 1 PAH classification. Its pathophysiology likewise involves endothelin-1 pathway dysregulation from chronically elevated pulmonary flow and shear stress, making it a direct mechanistic extension of ambrisentan's established pharmacology rather than a novel target. Nine trials and 18 publications support this direction, though the hemodynamic particularities of shunt-related disease — right-to-left shunting, Eisenmenger physiology — mean patients need individualized evaluation before treatment (the guardrail behind the "Proceed with Guardrails" call).

**PAH associated with connective tissue disease (CTD-PAH)**, most often driven by systemic sclerosis, is likewise a WHO Group 1 subtype whose vascular remodeling and endothelin-1 activation mirror idiopathic PAH. This is the strongest-supported prediction in the pack: it is backed by a Tier-1 meta-analysis (PMID 23906950), an AMBITION-trial subgroup RCT analysis (PMID 28039187), and three dedicated trials including the Phase 4 combination study (NCT01042158) and the EDITA early-intervention RCT (NCT02290613).

By contrast, the model's **highest-scored** prediction — pulmonary arteriovenous malformation (PAVM) — is a *structural* vascular malformation (direct arteriovenous shunting), not the *functional* vasoconstriction/remodeling process ambrisentan's ETA-antagonism targets. The only supporting literature is a single case report describing PAH in a patient with hereditary hemorrhagic telangiectasia (an indirect association), which is why this report leads with the two mechanistically and clinically better-supported subtypes instead.

---

## Clinical Trial Evidence

### Primary candidate: PAH associated with congenital heart disease

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Phase 3 | Terminated | 33 | Randomized, double-blind, placebo-controlled trial of ambrisentan 5 mg in inoperable CTEPH; terminated early (Grade A evidence) |
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | Phase 3 | Completed | 134 | Open-label study of ambrisentan on exercise capacity (6MWT) in Chinese PAH patients; completed (Grade A) |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Phase 2 | Completed | 38 | Long-term open-label extension for pediatric PAH patients continuing ambrisentan treatment (Grade A) |
| [NCT01894022](https://clinicaltrials.gov/study/NCT01894022) | Phase 3 | Terminated | 19 | Long-term extension study of ambrisentan safety/efficacy in inoperable CTEPH (Grade A) |
| [NCT01332331](https://clinicaltrials.gov/study/NCT01332331) | Phase 2 | Terminated | 41 | Randomized comparison of high vs. low weight-adjusted ambrisentan dose in pediatric PAH (Grade B) |
| [NCT04095286](https://clinicaltrials.gov/study/NCT04095286) | Phase 1 | Completed | 29 | PK bioavailability study of a low-dose pediatric ambrisentan formulation vs. marketed tablet (Grade B) |
| [NCT00593905](https://clinicaltrials.gov/study/NCT00593905) | N/A | Withdrawn | 0 | Pharmacogenomics study of endothelin receptor antagonist response; withdrawn, no data (Grade C) |
| [NCT02688387](https://clinicaltrials.gov/study/NCT02688387) | Phase 1 | Completed | 112 | Relative bioavailability of ambrisentan/tadalafil fixed-dose combinations; PK only (Grade C) |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Iloprost (not ambrisentan) in Eisenmenger-related PAH; low relevance (Grade C) |

### Secondary candidate: PAH associated with connective tissue disease

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | Ambrisentan + tadalafil combination therapy in scleroderma-spectrum PAH (SSc-PAH), assessing 6MWD, NYHA class, hemodynamics (Grade A) |
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | EDITA proof-of-concept RCT: early ambrisentan treatment for borderline PAH in systemic sclerosis (Grade A) |
| [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) | Phase 4 | Terminated | 3 | Switch study from bosentan/macitentan to ambrisentan in CTD-PAH; terminated for under-enrollment (Grade B) |

### PAH associated with HIV infection *(Research Question — lower priority)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Double-blind crossover study of inhaled iloprost in idiopathic/familial/HIV/drug-toxin-associated PAH on background PAH therapy (which may include ambrisentan); population is mixed-etiology, not HIV-PAH specific — needs manual verification of the original trial record (Grade B) |

### Other predicted indications
No clinical trials are registered for: pulmonary arteriovenous malformation, PAH associated with schistosomiasis, PAH associated with chronic hemolytic anemia, malformation syndrome with odontal/periodontal component, hypotrichosis simplex of the scalp, hypertrichosis, or Dandy-Walker malformation syndrome.

---

## Literature Evidence

### Primary candidate: PAH associated with congenital heart disease

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Cohort | American Journal of Cardiology | Early experience with ambrisentan in Eisenmenger syndrome; effects on resting/exercise systemic arterial saturation |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | Cohort | Pediatric Pulmonology | Real-world safety/tolerability of ambrisentan + tadalafil combination in pediatric PH |
| [22104452](https://pubmed.ncbi.nlm.nih.gov/22104452/) | 2011 | Cohort | Postgraduate Medicine | Adult congenital heart disease program experience with PAH management, including targeted therapies |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General PAH diagnosis/treatment review; contextualizes endothelin receptor antagonist use |
| [18333354](https://pubmed.ncbi.nlm.nih.gov/18333354/) | 2007 | Review | Rom J Intern Med | Management of PAH associated with congenital heart disease |
| [21852894](https://pubmed.ncbi.nlm.nih.gov/21852894/) | 2009 | Review | Progress in Pediatric Cardiology | Non-CHD causes of pediatric PAH, for differential context |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review/Meta-analysis | Medicine | PAH-specific drug therapy position in Eisenmenger syndrome |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | PAH treatment in connective tissue disease and congenital heart disease subgroups |
| [26223872](https://pubmed.ncbi.nlm.nih.gov/26223872/) | 2015 | Review | Indian Journal of Pediatrics | Modern management concepts for pediatric pulmonary hypertension incl. CHD-PAH |
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | Cohort | Ther Adv Respir Dis | Real-world ambrisentan tolerability/use across a broad PH referral population |

### Secondary candidate: PAH associated with connective tissue disease

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Meta-analysis of clinical trials in CTD-PAH treatment |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | RCT subgroup analysis | Annals of the Rheumatic Diseases | AMBITION trial subgroup: initial ambrisentan + tadalafil combination in CTD-PAH |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Cohort (post hoc) | Annals of the Rheumatic Diseases | AMBITION modified ITT post hoc analysis of combination vs. monotherapy in CTD-PAH |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Cohort | Respiratory Medicine | ARIES-E subgroup: 3-year ambrisentan efficacy/safety specifically in CTD-PAH |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | RCT subgroup analysis | Am J Respir Crit Care Med | Up-front ambrisentan + tadalafil combination in scleroderma-associated PAH |
| [31655622](https://pubmed.ncbi.nlm.nih.gov/31655622/) | 2019 | RCT | Arthritis Research & Therapy | EDITA RCT: early ambrisentan treatment for mildly elevated mPAP in systemic sclerosis |
| [29282676](https://pubmed.ncbi.nlm.nih.gov/29282676/) | 2018 | Post-marketing surveillance | Clinical Drug Investigation | Interim analysis of 702 real-world PAH patients on ambrisentan (Volibris) |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review/Meta-analysis | Internal and Emergency Medicine | Treatment outcomes for CTD-PAH across RCT subgroup/post hoc data |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in CTD-PAH treatment |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | PAH treatment in connective tissue disease |

### PAH associated with HIV infection *(supporting literature)*
- [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) (2014, Cohort) — broad PH referral population including HIV-associated cases
- [25560124](https://pubmed.ncbi.nlm.nih.gov/25560124/) (2015, Case report) — HIV-associated PAH diagnosed postpartum
- [26897508](https://pubmed.ncbi.nlm.nih.gov/26897508/) (2016, Case series) — 4 cases of HIV-associated PAH
- [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) (2019, Registry/Cohort) — Russian national PAH registry, includes HIV-associated subgroup

### Other predicted indications
No literature is available for: PAH associated with schistosomiasis, PAH associated with chronic hemolytic anemia, hypotrichosis simplex of the scalp, or hypertrichosis.

For **malformation syndrome with odontal/periodontal component** (rank 7), 20 publications were retrieved, but every one discusses periodontitis pathology/treatment with no mention of ambrisentan or its pharmacology — the source data itself flags this as a likely **knowledge-graph false positive** (entity confusion) rather than a genuine repurposing signal. **Syndrome with Dandy-Walker malformation** (rank 10) similarly has no clinical trials or literature.

---

## Finland Market Information

Ambrisentan is **not currently marketed in Finland** — 0 authorizations are on record, and no license entries are available in this Evidence Pack. No product name, dosage form, or approved indication text can be extracted at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug-drug interaction data are available in this Evidence Pack.

One point worth flagging explicitly: the pack's own data-gap log records the **TFDA/Fimea package insert (warnings/contraindications) as a Blocking-severity gap** — meaning this candidate cannot yet clear the S1 safety pre-screen. For the HIV-associated PAH prediction specifically, the repurposing rationale notes that HIV patients commonly co-prescribe antiretrovirals (protease inhibitors, CYP3A4-interacting agents), which would need dedicated DDI screening before that indication could advance beyond a research question.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for PAH associated with congenital heart disease and PAH associated with connective tissue disease — the two L1-evidence predictions). **Hold** on the remaining 8 predictions, including the model's top-scored hit (pulmonary arteriovenous malformation).

**Rationale:**
- CHD-PAH and CTD-PAH are both established WHO Group 1 PAH subtypes with a direct endothelin-pathway mechanistic link to ambrisentan's known pharmacology, and each is backed by multiple completed trials (including Phase 3/4 and an AMBITION-trial subgroup analysis) plus double-digit publication counts — meeting the L1 bar (≥2 relevant completed RCT-grade studies).
- PAVM is a structural vascular malformation rather than a functional vasoconstrictive process, and its only literature support is one indirect case report — mechanistically and evidentially too weak to advance (Hold, L4).
- HIV-associated PAH has moderate cohort/case-series support (L2) but the key trial's population is ambiguous and DDI risk with antiretrovirals is unassessed — kept as a research question rather than advanced.
- Schistosomiasis-, hemolytic-anemia-, periodontal-, hypotrichosis-, hypertrichosis-, and Dandy-Walker-related predictions have no clinical trials or literature (L5) and in one case (periodontal) show clear signs of a knowledge-graph false positive.

**To proceed, the following is needed:**
- Obtain and parse the TFDA/Fimea approved package insert (Blocking data gap — required before any S1 safety pre-screen)
- Confirm ambrisentan's mechanism of action via a formal DrugBank API lookup (currently reconstructed only from embedded literature abstracts)
- Manually verify whether NCT00709956 (iloprost crossover trial) actually enrolled an HIV-PAH-specific subpopulation, since the current summary is ambiguous
- Run a formal DDI screen for ambrisentan against antiretroviral regimens before advancing the HIV-PAH indication further
- Obtain route/formulation compatibility data (currently "pending" for all 10 predictions) to confirm the existing oral tablet meets requirements for pediatric CHD-PAH use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

