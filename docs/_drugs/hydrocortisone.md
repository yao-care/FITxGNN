---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a corticosteroid (glucocorticoid) historically used across a broad range of anti-inflammatory, immunosuppressive, and hormone-replacement indications. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **4 clinical trials** and **20 publications** currently supporting this direction — including a completed Phase 3 RCT directly comparing hydrocortisone against another topical steroid in this exact indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory data provided; hydrocortisone is broadly used as a systemic/topical corticosteroid for anti-inflammatory and adrenal hormone-replacement therapy |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for hydrocortisone is not available in this evidence pack. Based on known pharmacology, hydrocortisone is a glucocorticoid receptor agonist; its anti-inflammatory and immunosuppressive efficacy in a wide range of inflammatory and autoimmune conditions is well established.

Alopecia areata is understood as an autoimmune process in which T-cells attack the hair follicle, triggering non-scarring hair loss. Suppressing this local inflammatory/immune attack via topical or intralesional corticosteroid administration is already a recognized, long-standing treatment approach for alopecia areata — meaning this prediction reflects an **established clinical use** rather than a wholly novel repurposing hypothesis. The TxGNN prediction is therefore corroborated both by mechanistic plausibility and by decades of documented clinical practice using hydrocortisone specifically (intracutaneous/intradermal injection and topical cream) for this condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomized controlled trial in children comparing Clobetasol Propionate 0.05% Cream vs. Hydrocortisone 1% Cream for alopecia areata; direct head-to-head evidence for hydrocortisone in this indication |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Evaluated adrenal function effects of intralesional Triamcinolone (a related corticosteroid) in alopecia areata patients — mechanistically relevant but not hydrocortisone itself |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Not Yet Recruiting | 72 | Four-arm dose-response study of hair growth products vs. placebo in androgenic alopecia (different alopecia subtype); no results available yet |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Studied abnormal steroid metabolome and bone effects in mild autonomous cortisol secretion; low relevance — not an alopecia areata treatment trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Randomized clinical trial: clobetasol propionate 0.05% vs. hydrocortisone 1% for alopecia areata in children |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Review/Meta-analysis | Journal of Cosmetic Dermatology | Systematic review/meta-analysis of fractional laser (alone or combined) for alopecia areata |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Cohort/Clinical | Clinical and Experimental Dermatology | Retrospective analysis: topical corticosteroid under occlusion for severe pediatric alopecia areata (including totalis/universalis) |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | Early case series treating alopecia areata, partialis, and totalis with cortisone, hydrocortisone, prednisone, and prednisolone |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | JEADV | Reviews the hypothesis of HPA-axis hyperactivity and cortisol production in alopecia areata patients |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | Journal of the American Academy of Dermatology | Four cases of congenital alopecia areata treated with minoxidil and topical steroid therapy |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case report | Der Hautarzt | Hair regrowth in alopecia areata and areata maligna following intracutaneous hydrocortisone injection |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Case report | Vestnik Dermatologii i Venerologii | Treatment of alopecia areata and total alopecia with intracutaneous hydrocortisone injections |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Case report | Actas Dermo-Sifiliográficas | Treatment of alopecia areata with intradermal hydrocortisone injections |
| [5696522](https://pubmed.ncbi.nlm.nih.gov/5696522/) | 1968 | Case report | British Journal of Dermatology | Scalp blood vessel changes in alopecia areata patients before and after corticosteroid therapy |

## Finland Market Information

No marketing authorization is currently registered for hydrocortisone in Finland (market status: **Not Marketed**, 0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT and decades of historical clinical literature directly support hydrocortisone's use in alopecia areata, and the underlying immunosuppressive mechanism is well established. However, the drug currently has no marketing authorization in Finland and key safety/MOA fields are unfilled, so full sign-off is not yet warranted.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently blocking (DG001)
- Detailed mechanism of action data from DrugBank (DG002)
- Confirmation of Finland regulatory pathway given current "Not Marketed" status
- Additional confirmatory RCT data beyond the single completed Phase 3 trial
- Drug interaction (DDI) data, currently unavailable (query returned not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

