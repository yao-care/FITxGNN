---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 8
---

# Fluticasone Furoate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Fluticasone Furoate: From Allergic Airway Inflammation to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate is an inhaled/intranasal corticosteroid whose original indication data is not documented in this evidence pack, though its pharmacological class is established for allergic airway inflammation. The TxGNN model predicts it may be effective for **Atopic Eczema**, with **13 clinical trials** and **2 publications** currently supporting this direction — though most direct trial evidence comes from the propionate ester rather than furoate specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug class: inhaled/intranasal corticosteroid) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fluticasone furoate is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, fluticasone furoate is a trifluorinated synthetic corticosteroid and part of the inhaled/intranasal corticosteroid (ICS) class — its role in suppressing airway and mucosal inflammation via glucocorticoid receptor-mediated cytokine suppression is well established in allergic respiratory disease (supported within this evidence pack by literature such as PMID 21977941, which describes it as "a novel long-acting inhaled corticosteroid").

Atopic eczema and allergic airway disease share a common Th2-driven inflammatory pathway, and topical corticosteroids are a standard-of-care class-effect treatment for atopic dermatitis. The bulk of direct clinical evidence in this pack, however, comes from **fluticasone propionate** (a related but distinct ester) rather than furoate — meaning the mechanistic rationale is sound, but cross-ester extrapolation (propionate → furoate) should be treated as an assumption requiring confirmation, particularly given differences in skin penetration and potency between the two esters.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of Cutivate (fluticasone propionate) lotion 0.05% and its effect on the HPA axis in pediatric atopic dermatitis |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Randomized comparative study of intermittent fluticasone propionate 0.05% cream to reduce relapse risk in stabilized atopic dermatitis |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | RCT of twice-weekly fluticasone propionate maintenance therapy to reduce relapse in mild/moderate pediatric AD |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Randomized double-blind comparison of tacrolimus 0.03% vs. fluticasone 0.005% ointment in children with moderate-to-severe AD |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | SEAL study: proactive skin barrier care plus fluticasone propionate cream to prevent AD progression and food allergy in infants |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | NA | Completed | 98 | Oral probiotic supplementation in children with AD (low mechanistic relevance to fluticasone) |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Combined pimecrolimus (Elidel) and fluticasone (Cutivate) cream in patients with severe AD lesions |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Randomized double-blind comparison of tacrolimus 0.1% vs. fluticasone 0.005% ointment in adults with facial AD |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Pilot RCT comparing EpiCeram device vs. fluticasone propionate 0.05% in pediatric AD |
| [NCT07537751](https://clinicaltrials.gov/study/NCT07537751) | NA | Completed | 40 | RCT comparing topical crisaborole 2% vs. fluticasone propionate 0.05% in mild-to-moderate pediatric AD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews intranasal corticosteroid use across allergic conditions including atopic dermatitis, focusing on HPA axis suppression risk |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case Report | Indian J Otolaryngol Head Neck Surg | Case study on allergen immunotherapy in an autoimmune-terrain patient, noting extended application to atopic dermatitis |

---

## Finland Market Information

Fluticasone furoate is currently **not marketed** in Finland — no marketing authorizations are on record in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fluticasone (propionate) has multiple Phase 3/4 trials with grade-A relevance directly supporting efficacy in atopic dermatitis, giving an L1 evidence level. However, the drug is not currently marketed in Finland, direct evidence for the furoate ester (vs. propionate) is limited, and a Blocking-severity data gap on the Finnish/TFDA package insert (warnings and contraindications) prevents a safety initial assessment (S1) — so this cannot yet advance to unconditional Go.

**To proceed, the following is needed:**
- Finnish/TFDA package insert — warnings, contraindications (Blocking gap, required before S1 safety evaluation)
- Fluticasone furoate-specific mechanism of action data (High-priority gap)
- Direct efficacy/safety data for the furoate ester in atopic dermatitis, to confirm cross-ester extrapolation from propionate-based trials
- Route/formulation feasibility assessment (topical dermatologic formulation vs. currently available nasal/inhaled forms)
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

