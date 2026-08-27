---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Ocular Hypertension/Glaucoma to Vascular Disease

## One-Sentence Summary

> Travoprost is a prostaglandin F2α analogue (FP receptor agonist) used to lower intraocular pressure in open-angle glaucoma and ocular hypertension.
> The TxGNN model's single highest-scoring prediction (**visceral calciphylaxis**, score 99.9998%) has **zero supporting trials or literature** and is flagged as pure graph-proximity inference.
> Among the 10 candidate indications in this pack, only **Vascular Disease** reached the "Research Question" stage, supported by **15 clinical trials** and **20 publications** — though all are drawn from the drug's original glaucoma indication and describe vascular *side effects* rather than a tested vascular *treatment* effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (inferred from trial evidence and rationale text; no formal indication record in this pack) |
| Predicted New Indication | Vascular Disease |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold — Research Question (hypothesis-generating, not yet a Go candidate) |

---

## Why is This Prediction Reasonable?

Currently, a formal mechanism-of-action record is not available for this drug (flagged in the evidence pack as a High-severity data gap). Based on information embedded in the evidence's own rationale text, travoprost is an FP-receptor prostaglandin agonist whose approved effect is intraocular pressure reduction via increased uveoscleral outflow. FP receptors are also expressed on vascular smooth muscle, which is the theoretical bridge TxGNN appears to be using to connect travoprost to the broad "vascular disease" category.

In practice, this link is indirect. The supporting trials do not test travoprost as a treatment for any systemic vascular condition — they document a related but distinct phenomenon: prostaglandin-analogue eye drops cause **conjunctival hyperemia** (local vasodilation) as a side effect, and one small study (NCT00308945, n=20) directly measured drug-induced changes in retinal vascular diameter and choroidal blood flow. This establishes that travoprost has *measurable vasoactive effects*, but not that modulating those effects treats "vascular disease" as a therapeutic indication.

Given this, the TxGNN score most plausibly reflects graph proximity between "travoprost" and vascular *side-effect* nodes, rather than a validated treatment relationship. This is why the evidence level is capped at L4 (mechanistic/pharmacodynamic signal only) and the decision stage remains "Research Question" rather than moving toward a Go recommendation.

---

## Other TxGNN-Predicted Indications (Screened, No Evidence Support)

For transparency, the remaining 9 ranked candidates in this evidence pack were also queried against ClinicalTrials.gov, ICTRP, and PubMed. All returned no hits except one (case-report level only), and all are held at decision stage S0:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Visceral calciphylaxis | 99.9998% | L5 | Hold — no mechanistic or evidentiary link |
| 2 | Venous thoracic outlet syndrome | 99.9998% | L5 | Hold — no evidence |
| 3 | Arterial thoracic outlet syndrome | 99.9998% | L5 | Hold — no evidence |
| 4 | Neurogenic thoracic outlet syndrome | 99.9997% | L5 | Hold — no evidence |
| 6 | Angiodysplasia of stomach | 99.9997% | L5 | Hold — no evidence |
| 7 | Blue toe syndrome | 99.9997% | L5 | Hold — no evidence |
| 8 | Lymphangiectasis | 99.9997% | L5 | Hold — no evidence |
| 9 | Idiopathic spontaneous coronary artery dissection | 99.9997% | L5 | Hold — no evidence; population should avoid unvalidated cardiovascular intervention |
| 10 | Hemangioendothelioma | 99.9997% | L4 | Hold — 2 case reports show travoprost **inducing** uveal effusion in patients with vascular anomalies (Sturge-Weber-Krabbe syndrome); this is a risk signal, not supporting evidence |

---

## Clinical Trial Evidence

Evidence below is drawn from `predicted_indications` → Vascular Disease (the only candidate with registered trials). All trials were conducted in the drug's original glaucoma/ocular hypertension population; none tests a systemic vascular disease endpoint directly.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02136589](https://clinicaltrials.gov/study/NCT02136589) | Phase 4 | Completed | 40 | Evaluated whether NSAID pretreatment affects travoprost-induced conjunctival hyperemia and IOP reduction — direct vascular mechanism study (Grade B) |
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Phase 4 | Completed | 20 | Compared travoprost vs. latanoprost effects on retinal vascular diameter and choroidal blood flow — only trial measuring vascular physiology parameters (Grade B) |
| [NCT00293787](https://clinicaltrials.gov/study/NCT00293787) | Phase 3 | Completed | 156 | Safety/efficacy of glaucoma therapy in open-angle glaucoma/ocular hypertension (original indication) |
| [NCT00293761](https://clinicaltrials.gov/study/NCT00293761) | Phase 3 | Completed | 109 | Safety/efficacy of glaucoma therapy in open-angle glaucoma/ocular hypertension (original indication) |
| [NCT00799682](https://clinicaltrials.gov/study/NCT00799682) | Phase 4 | Completed | 56 | Ocular surface signs/symptoms: Xalatan vs. Travatan Z in dry-eye glaucoma patients |
| [NCT00760539](https://clinicaltrials.gov/study/NCT00760539) | Phase 3 | Completed | 87 | Travoprost/timolol BAC-free vs. standard formulation in open-angle glaucoma |
| [NCT01253902](https://clinicaltrials.gov/study/NCT01253902) | Phase 4 | Completed | 164 | Ocular surface tolerability comparison across prostaglandin analogues |
| [NCT00347126](https://clinicaltrials.gov/study/NCT00347126) | N/A | Completed | 372 | Efficacy/safety of systematic switch from latanoprost to travoprost |
| [NCT00047554](https://clinicaltrials.gov/study/NCT00047554) | N/A | Terminated | 336 | Five-year safety study of iris pigmentation changes with travoprost |
| [NCT00672997](https://clinicaltrials.gov/study/NCT00672997) | Phase 3 | Completed | 301 | Travoprost/timolol BAC-free vs. standard formulation, US arm of NCT00760539 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18497524](https://pubmed.ncbi.nlm.nih.gov/18497524/) | 2008 | RCT | Ophthalmologica | Compared ocular surface side effects (hyperemia, tearing) of travoprost vs. bimatoprost over 6 months |
| [12614748](https://pubmed.ncbi.nlm.nih.gov/12614748/) | 2003 | RCT | Am J Ophthalmol | Conjunctival hyperemia after short-term dosing with latanoprost, bimatoprost, and travoprost |
| [24070367](https://pubmed.ncbi.nlm.nih.gov/24070367/) | 2013 | RCT | J Ocul Pharmacol Ther | Bimatoprost 0.01% vs. travoprost/timolol in IOP control after latanoprost/timolol failure |
| [40718639](https://pubmed.ncbi.nlm.nih.gov/40718639/) | 2025 | Review | Int J Nanomedicine | Nanomedicine-based ophthalmic drug delivery systems for ocular disease |
| [31335731](https://pubmed.ncbi.nlm.nih.gov/31335731/) | 2019 | Review | Medicine | Systematic evaluation of travoprost efficacy in glaucoma |
| [25867658](https://pubmed.ncbi.nlm.nih.gov/25867658/) | 2015 | Review | Curr Med Res Opin | Meta-analysis of prostaglandin-timolol fixed combination efficacy/tolerability |
| [22167538](https://pubmed.ncbi.nlm.nih.gov/22167538/) | 2012 | Review | Eur J Ophthalmol | Meta-analysis of prostaglandin-timolol fixed combinations' IOP-lowering effect |
| [21878000](https://pubmed.ncbi.nlm.nih.gov/21878000/) | 2011 | Review | Curr Med Res Opin | Balancing efficacy and tolerability of prostaglandin analogues in POAG |
| [35524840](https://pubmed.ncbi.nlm.nih.gov/35524840/) | 2022 | Review | Adv Ther | VISIONARY study subanalysis: switching to preservative-free tafluprost/timolol |
| [17535371](https://pubmed.ncbi.nlm.nih.gov/17535371/) | 2007 | Review | Clin Exp Optom | General review of ocular therapeutics |

---

## Taiwan Market Information

Travoprost is currently **not marketed in Taiwan** — the evidence pack records 0 active authorizations and no license entries, so no product/dosage-form table can be produced.

---

## Safety Considerations

No package-insert warnings, contraindications, or drug-drug interaction data are available for travoprost in this evidence pack (the TFDA package insert lookup is flagged as a **Blocking** data gap, and the DDI query returned no results).

> Please refer to the package insert for safety information.

**Related safety signal (not a formal warning, but real literature data):** two case reports (PMID 19107053, PMID 21524602) describe travoprost inducing uveal effusion in glaucoma patients with pre-existing vascular anomalies (Sturge-Weber-Krabbe syndrome). This suggests caution in any patient population with underlying vascular malformations, and is directionally opposite to a therapeutic vascular-disease use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN model's top-ranked prediction (visceral calciphylaxis) has no clinical, literature, or mechanistic support and should not be advanced.
- The only candidate with real supporting data — Vascular Disease — is backed solely by pharmacodynamic/safety observations (hyperemia, retinal blood flow changes) from the drug's original glaucoma trials, not by any trial testing a vascular-disease treatment endpoint. This is hypothesis-generating (L4), not decision-ready.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently a Blocking gap preventing any S1 safety screen
- Formal mechanism-of-action documentation from DrugBank
- A dedicated preclinical or translational study directly testing FP-receptor modulation in a defined vascular disease model, since existing evidence only documents vascular *side effects* of ocular dosing
- Confirmation of Taiwan regulatory pathway, given the drug is currently unmarketed with zero local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

