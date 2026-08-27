---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
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

# Insulin Degludec: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec is an ultra-long-acting basal insulin analog with an established global indication of diabetes mellitus (type 1 and type 2). The TxGNN model flags **Type 1 Diabetes Mellitus** as its top-ranked predicted indication, and the evidence base — **50 clinical trials** and **20 publications** — confirms this is not a novel repurposing signal but the drug's own core, label indication in a market (Finland) where it is not currently marketed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (type 1 and type 2) — established global label use; no Finland-specific license record exists in this Evidence Pack |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin degludec is an ultra-long-acting basal insulin analog that acts directly on the insulin receptor, replacing the endogenous insulin that patients with type 1 diabetes lose to autoimmune β-cell destruction. Its multihexamer subcutaneous depot slowly and continuously releases monomeric insulin, giving a flat, ultra-long action profile with lower day-to-day variability than first-generation basal insulins (glargine, detemir).

Because this mechanism is direct replacement therapy rather than an indirect or inferred pathway, the TxGNN prediction of "type 1 diabetes mellitus" is not really a repurposing hypothesis — it is the drug's own established, on-label indication, already approved for T1DM in numerous markets worldwide (e.g., as Tresiba). The "Not Marketed" status recorded for this evaluation should be read as **this drug not yet having Finland market authorization**, not as an unvalidated new-use signal. Practically, this candidate should be tracked as a **market-access case** (bringing an already-proven therapy to a new market) rather than a traditional evidence-generation repurposing case.

The five other TxGNN-predicted indications for this drug (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, and two stiff-person-syndrome variants) all score highly on the model but have zero supporting trials or literature and were placed on **Hold** — their similarity to T1DM in the underlying knowledge graph (shared autoimmune or endocrine nodes) does not reflect an actual pharmacological rationale for insulin degludec.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00992537](https://clinicaltrials.gov/study/NCT00992537) | Phase 1 | Completed | 27 | Head-to-head PK/PD comparison of IDegAsp (NN5401), insulin degludec (NN1250), and insulin aspart in T1D |
| [NCT05413369](https://clinicaltrials.gov/study/NCT05413369) | Phase 3 | Completed | 582 | iGlarLixi vs. IDegAsp in Chinese T2DM inadequately controlled on oral agents |
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2 — randomized double-blind crossover comparing degludec vs. glargine safety/efficacy, with/without OADs |
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Weekly insulin efsitora alfa vs. degludec in T1D on multiple daily injections |
| [NCT05243628](https://clinicaltrials.gov/study/NCT05243628) | Phase 4 | Completed | 33 | Afrezza inhaled mealtime insulin + automated insulin pump or degludec in adult T1D |
| [NCT02536859](https://clinicaltrials.gov/study/NCT02536859) | Phase 1 | Completed | 60 | Steady-state PK/PD crossover, degludec vs. glargine U300, in T1D |
| [NCT05767255](https://clinicaltrials.gov/study/NCT05767255) | Phase 3 | Unknown | 66 | Hypoglycemia risk during inpatient-to-outpatient transition, basal-bolus vs. degludec/liraglutide |
| [NCT01959529](https://clinicaltrials.gov/study/NCT01959529) | Phase 3 | Completed | 7,637 | DEVOTE — cardiovascular safety of degludec vs. glargine in T2D patients at high CV risk |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | Completed | 1,108 | Faster-acting insulin aspart vs. NovoRapid, both combined with degludec, in adult T1D |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1,392 | PRONTO-T1D — LY900014 vs. insulin lispro, combined with glargine or degludec, in adult T1D |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial — degludec vs. detemir (both + aspart) in pregnant women with T1D, non-inferiority design |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6 — weekly insulin icodec vs. daily degludec in a basal-bolus regimen for T1D |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5 — weekly insulin efsitora alfa vs. daily degludec, phase 3 non-inferiority in T1D |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Review/Meta-analysis | Clinical Therapeutics | Systematic review/meta-analysis of degludec efficacy and tolerability vs. other long-acting basal insulins in T1D and T2D |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg — randomized crossover, degludec vs. glargine U100 in T1D prone to nocturnal severe hypoglycemia |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX — single-center RCT comparing degludec 100 IU/mL vs. glargine 300 IU/mL efficacy/safety in T1D |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP — open-label randomized crossover, basal degludec vs. aspart via pump in T1D |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1 — randomized crossover comparing glargine U300 vs. degludec around spontaneous exercise in T1D |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Current status of degludec in T1D and T2D based on randomized and observational trials |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Management of T1D in pregnancy, including basal insulin choice and glycemic targets |

---

## Finland Market Information

No marketing authorizations are on file for insulin degludec in Finland (`market_status: 未上市` / Not Marketed; `total_licenses: 0`). Fimea product-level license data (product name, dosage form, approved indication text) has not yet been retrieved for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured Fimea/TFDA warnings, contraindications, or drug-interaction data are currently available for insulin degludec in this Evidence Pack (this is flagged as a **Blocking** data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin degludec's efficacy and safety in type 1 diabetes are supported by an extensive, mature evidence base — including multiple completed Phase 3 RCTs (SWITCH 2, DEVOTE, PRONTO-T1D, QWINT-5, ONWARDS 6) and systematic reviews — meeting L1 evidence criteria. However, this is not a novel repurposing signal: it is the drug's own core indication, currently unregistered in Finland, and the Blocking safety data gap (no Fimea package-insert warnings/contraindications) must be closed before any S1 safety review can proceed.

**To proceed, the following is needed:**
- Fimea package-insert data (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Formal DrugBank-sourced mechanism-of-action documentation (DG002)
- Confirmation of the appropriate regulatory pathway for Finland market entry (likely standard marketing-authorization/mutual-recognition route, not an experimental repurposing pathway, given this is an established global indication)
- Note: the five other TxGNN-predicted indications for this drug (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, classic and focal stiff-person/stiff-limb syndrome) have no supporting trials or literature and remain on **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

