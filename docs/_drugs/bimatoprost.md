---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

Using the evidence pack as given. One note up front: I did **not** follow `predicted_indications[0]` mechanically. Rank 1 ("malformation syndrome with odontal/periodontal component") has 0 clinical trials and 20 completely unrelated periodontitis papers that never mention bimatoprost — the evidence pack's own rationale field calls this "literature noise, not evidence." Ranks 2–7 and 10 are similarly unsupported (several are even mechanistically backwards, e.g. predicting a hair-growth drug for a *hypertrichosis* syndrome). The only candidate in this pack with real trial and literature support is rank 8, **alopecia** (L2, "Proceed with Guardrails"), so the report is built around that.

---

# Bimatoprost: From Glaucoma to Alopecia

## One-Sentence Summary

> Bimatoprost is a synthetic prostamide F2α analog originally approved (per literature evidence in this pack) for glaucoma/ocular hypertension and, as an ophthalmic solution, for eyelash hypotrichosis (Latisse™).
> The TxGNN model predicts it may also be effective for **Alopecia** (androgenetic alopecia, alopecia areata, and related hair-loss conditions),
> with **11 clinical trials** and **20 publications** currently supporting this direction.
>
> Note: TxGNN's single highest-scoring prediction in this evidence pack (a periodontal malformation syndrome) and several others (Dandy-Walker syndrome, hair-shaft abnormality, hypertrichosis, pulmonary AV malformation) have no supporting evidence and in some cases are mechanistically implausible or backwards — they are excluded from this report and flagged "Hold" in the source data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (ophthalmic); eyelash hypotrichosis (per literature evidence — not confirmed via Finland regulatory data, as the product is not marketed there) |
| Predicted New Indication | Alopecia (androgenetic alopecia / alopecia areata) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank MOA data is not available for bimatoprost in this evidence pack (flagged as a High-severity data gap). However, the clinical trial and literature evidence themselves describe bimatoprost as a synthetic **prostamide F2α analog**. In ophthalmology it lowers intraocular pressure by increasing aqueous humor outflow; as a well-documented side effect, it also prolongs the hair follicle anagen (growth) phase, which is the basis for its FDA-approved use (Latisse™) in treating eyelash hypotrichosis.

This anagen-prolongation mechanism is not specific to eyelashes — hair follicle biology is broadly shared across eyelash, eyebrow, and scalp follicles. Multiple sponsor-run trials (Allergan) directly tested this hypothesis by applying bimatoprost topically to the scalp in androgenetic alopecia (AGA) and female pattern hair loss, and to eyebrows/eyelashes after chemotherapy-induced loss. A related, weaker-evidence entry in the same pack ("genetic alopecia," L4, case-report level) supports the same mechanistic direction.

In short, the prediction is reasonable because it is not a novel hypothesis inferred purely from the TxGNN graph — it is a mechanism that has already been prospectively tested in multiple completed Phase 1/2 trials, including two placebo/active-comparator RCTs with >300 participants each (against minoxidil).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | RCT of 3 bimatoprost doses vs. vehicle and OTC minoxidil 2% in women with female pattern hair loss |
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | RCT of 3 bimatoprost doses vs. vehicle and OTC minoxidil 5% in men with androgenic alopecia |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in men with androgenic alopecia (AGA) |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Effect of bimatoprost 0.03% ophthalmic solution on androgen-dependent scalp hair follicles |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability and pharmacokinetics of new topical bimatoprost formulations in alopecia patients |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Scalp pharmacokinetics and tolerability of two bimatoprost formulations after 14 days topical application in AGA |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Safety/efficacy of bimatoprost 0.03% for eyelash loss or hypotrichosis in children |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | Combined CO2 fractional laser + bimatoprost 0.03% in alopecia areata |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Latanoprost vs. bimatoprost ophthalmic solutions for eyelash regrowth in alopecia areata |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose-escalation safety/tolerability/PK study of topical bimatoprost in men with AGA (terminated, incomplete) |

*(One additional trial, NCT00999557, was withdrawn with 0 enrollment and is omitted as uninformative.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Systematic Review / Network Meta-analysis | J Dermatolog Treat | Compares relative efficacy of non-surgical AGA monotherapies in men and women |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Guideline | J Dermatol | Japanese clinical guideline for diagnosis and treatment of male/female pattern hair loss |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | Reviews bimatoprost for eyelash, eyebrow and scalp alopecia; notes FDA approval for eyelash hypotrichosis |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | Clinical Study | Arch Dermatol Res | CO2 fractional laser + bimatoprost combination enhances hair regrowth in alopecia areata |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective Open-Label Study | Dermatol Ther | Topical bimatoprost for eyelash loss in alopecia totalis/universalis; 16/1x responders |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Non-randomized Open-Label Clinical Trial | Indian Dermatol Online J | Bimatoprost vs. clobetasol propionate in scalp alopecia areata |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | Review | Curr Oncol | Reviews chemotherapy-induced alopecia treatments including prostaglandin analogs |
| [32642317](https://pubmed.ncbi.nlm.nih.gov/32642317/) | 2020 | Review | Dermatol Pract Concept | Prevention and treatment options for chemotherapy-induced alopecia |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Preclinical/Formulation | Drug Deliv | Enhanced-penetration topical bimatoprost formulation shows in vivo hair regrowth efficacy in androgenic alopecia |
| [38577618](https://pubmed.ncbi.nlm.nih.gov/38577618/) | 2024 | Preclinical/Formulation | Int J Pharm X | Nanogel delivery system improves cutaneous bimatoprost deposition and hair regrowth in androgenic alopecia |

## Finland Market Information

Bimatoprost is not currently marketed in Finland — no marketing authorizations are recorded (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information (no structured warnings, contraindications, or DDI data are available in this evidence pack; the TFDA/Fimea package insert lookup is flagged as a **Blocking** data gap). For context, the literature evidence in this pack (e.g. PMID 29854658) notes that prostaglandin-analog eye drops of this class are associated with eyelid pigmentation and localized hypertrichosis as known class effects — this is cited from the literature evidence, not from a validated safety data source, and should not substitute for the formal package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 2 RCTs (two with >300 participants, one against active minoxidil comparators) directly support bimatoprost's efficacy on scalp/eyebrow hair growth, consistent with its already-validated anagen-prolongation mechanism (FDA-approved for eyelash hypotrichosis). However, no completed Phase 3 trial exists, one AGA dose-escalation trial was terminated early, and the product is not currently marketed in Finland, so safety and regulatory data are incomplete.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action documentation
- A completed Phase 3 confirmatory trial in the target alopecia population before any indication filing
- Drug-drug interaction data (current query status: not found)
- A defined regulatory pathway/strategy for Finland market entry given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

