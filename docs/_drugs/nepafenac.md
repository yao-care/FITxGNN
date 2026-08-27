---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Cataract Surgery-Related Ocular Inflammation to Eye Disease (Broader Predicted Indication)

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID prodrug; this evidence pack does not carry a formally documented original indication (data gap), but the underlying trial and literature record shows extensive, longstanding use for inflammation/pain prevention after cataract surgery and for diabetic macular edema risk reduction. TxGNN's top prediction is the broad category **eye disease**, supported by **41 clinical trials** and **20 publications** already in this pack — meaning the "new indication" signal largely reconfirms the drug's known ocular use rather than pointing to a genuinely novel disease area.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this evidence pack (data gap, see DG002). Trial/literature evidence within this pack indicates established use for cataract surgery-related ocular inflammation, pain, and macular edema prevention. |
| Predicted New Indication | Eye disease (broad ocular category) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not present in the structured `drug.original_moa` field (data gap DG002). However, the clinical evidence collected in this pack is itself informative: nepafenac is a prodrug that, once instilled topically, is converted intraocularly to amfenac, which inhibits COX-1 and COX-2 to reduce prostaglandin synthesis. This is the pharmacological basis for its established role in preventing and treating ocular inflammation and pain after cataract surgery, and in reducing the risk of postoperative macular edema in diabetic patients.

Because "eye disease" is a broad category rather than a specific new condition, this prediction largely overlaps with nepafenac's known clinical use rather than identifying an unmet, previously untested indication. The `original_indications` field being empty appears to be a data-capture gap rather than an absence of clinical basis — the pack's own trial set (41 studies, several large Phase 3 pivotal trials with n>800–2,000) already documents this activity. Genuinely novel signals in this pack are weaker: candidates such as optic papillitis (rank 2) and vitreous detachment (rank 10) have plausible mechanistic rationale (anti-inflammatory/COX-inhibition effects on retinal or optic nerve inflammation) but only sparse, indirect, or preclinical support (L3–L4), and several lower-ranked predictions (hypotrichosis, seborrheic keratosis, congenital syndromes) have no clinical or mechanistic link at all and are best treated as model noise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once-daily superior to vehicle for clinical outcomes in diabetic subjects after cataract surgery |
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Large pivotal trial assessing nepafenac 0.3% for prevention/treatment of postoperative ocular inflammation and pain after cataract extraction |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for prevention/treatment of postoperative inflammation and pain |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Bioequivalence study of generic vs Ilevro (nepafenac 0.3%) for postoperative pain/inflammation |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Phase 4 | Completed | 126 | Head-to-head comparison of nepafenac (Nevanac) vs other NSAID eye drops on PGE2 inhibition post-phacoemulsification |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | Terminated | 175 | Evaluated nepafenac (Nevanac) for macular edema incidence/severity reduction in diabetic retinopathy after cataract surgery |
| [NCT00494494](https://clinicaltrials.gov/study/NCT00494494) | Phase 4 | Completed | 82 | Nepafenac 0.1% effect on preventing postoperative cystoid macular edema after uncomplicated cataract surgery |
| [NCT02515045](https://clinicaltrials.gov/study/NCT02515045) | Phase 4 | Completed | 59 | Compared injectable dropless prophylaxis vs standard topical regimen (including nepafenac) after phacoemulsification |
| [NCT03851172](https://clinicaltrials.gov/study/NCT03851172) | Phase 2 | Unknown | 75 | Nepafenac vs ketorolac for preventing intraoperative miosis during cataract surgery |
| [NCT00801905](https://clinicaltrials.gov/study/NCT00801905) | Phase 2 | Terminated | 50 | Topical nepafenac for preventing/treating macular thickening related to pan-retinal photocoagulation in diabetic retinopathy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Compared 0.1% nepafenac vs 1% prednisolone acetate for postoperative inflammation control after micro-incisional cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology. Glaucoma | Compared 0.1% nepafenac vs 1% prednisolone acetate for inflammation control after laser peripheral iridotomy |
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review/Meta-analysis | Eur J Ophthalmol | Nepafenac's role in preventing macular swelling and improving visual outcome after cataract surgery |
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 Study | J Cataract Refract Surg | Once-daily nepafenac 0.3% to prevent/treat ocular inflammation and pain after cataract surgery |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Cohort/Comparative | Acta Ophthalmol | Clinical efficacy and tolerability of nepafenac vs preservative-free diclofenac after cataract surgery |
| [29199864](https://pubmed.ncbi.nlm.nih.gov/29199864/) | 2018 | Safety/Efficacy Study | Curr Eye Res | Intracameral nepafenac safety and efficacy in inhibiting prostaglandin synthesis during phacoemulsification |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | PK/Distribution Study | Exp Eye Res | Distribution of topical nepafenac and its active metabolite amfenac to the posterior segment of the eye |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | Comparative Study | J Cataract Refract Surg | Prophylactic nepafenac and ketorolac vs placebo in preventing postoperative macular edema |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | Comparative Study | Int J Ophthalmol | Efficacy/safety comparison of bromfenac, nepafenac, and diclofenac for cystoid macular edema prevention |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic agents and therapeutic medications (including NSAIDs) for non-infectious corneal injury |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal TFDA/Fimea warnings, contraindications, and drug-drug interaction data were not retrievable at the time of this pack's generation (data gap DG001, classified as **Blocking** — this prevents a formal S1 safety pre-assessment).

---

## Other TxGNN-Predicted Indications (Screening Notes)

Ranks 2–10 were also screened but are not the focus of this report given weaker or absent evidence:

| Rank | Disease | Score | Evidence Level | Recommendation |
|------|---------|-------|-----------------|-----------------|
| 2 | Optic papillitis | 99.84% | L4 | Hold |
| 3 | Hypotrichosis simplex of the scalp | 99.84% | L5 | Hold |
| 4 | Seborrheic keratosis | 99.83% | L5 | Hold |
| 5 | von Hippel anomaly | 99.82% | L5 | Hold |
| 6 | Congenital hypotrichosis milia | 99.82% | L5 | Hold |
| 7 | McPherson Robertson Cammarano syndrome | 99.82% | L5 | Hold |
| 8 | Lagophthalmos | 99.81% | L5 | Hold |
| 9 | Vulvar inverted follicular keratosis | 99.81% | L5 | Hold |
| 10 | Vitreous detachment | 99.81% | L3 | Research Question |

Ranks 3, 4, 6, 7, 8, and 9 have no supporting clinical trials or literature and no plausible mechanistic link to nepafenac's COX-inhibition activity — these likely reflect model noise. Vitreous detachment (rank 10) has one completed Phase 4 trial on vitreous inflammatory biomarkers and warrants a research question rather than immediate dismissal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction ("eye disease") is backed by L1-level evidence (multiple completed Phase 3 RCTs), but it substantially overlaps with nepafenac's already-established ophthalmic anti-inflammatory use rather than representing a distinct novel indication — so this should be treated as evidence consolidation, not new-indication discovery. A blocking safety data gap (DG001) also prevents formal risk sign-off.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) to close the blocking safety gap (DG001)
- Confirmed original indication and MOA documentation from DrugBank/regulatory sources to properly scope what counts as "new" vs. already-approved use (DG002)
- If pursuing rank 10 (vitreous detachment) as a genuine research question, targeted literature/trial search specific to vitreous detachment rather than secondary post-surgical vitreous inflammation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

