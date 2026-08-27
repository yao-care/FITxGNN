---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog used to manage diabetes mellitus.
The TxGNN model's top-ranked prediction for this drug is **Autoimmune Oophoritis**,
but this candidate is currently supported by **0 clinical trials** and **0 publications**,
and the model's own rationale flags it as a likely indirect graph association rather than a genuine mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (glycemic control) — based on general drug identity; no Finland license text is available in this evidence pack |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned no MOA text for this drug). Based on general pharmacological knowledge, insulin lispro is a recombinant rapid-acting insulin analog (reversed Lys-Pro at positions B28–B29) that binds the insulin receptor to lower blood glucose; it is used in the management of type 1 and type 2 diabetes mellitus.

For the top-ranked prediction, **autoimmune oophoritis**, the evidence pack's own mechanistic assessment is explicit: there is no known pathophysiological connection between insulin and autoimmune oophoritis. The prediction most likely reflects the drug and disease being indirectly clustered under a shared "autoimmune disease" node in the knowledge graph, rather than any causal or therapeutic mechanism. No preclinical, case-level, or clinical evidence currently supports insulin as a treatment for this condition.

Because the mechanistic rationale is absent and no supporting studies exist, this candidate does not currently meet the bar for further evaluation despite its high TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Insulin lispro has no registered authorizations in Finland in this evidence pack (`market_status: 未上市`, `total_licenses: 0`); no product/dosage-form/indication records are available.

## Other Candidate Indications in This Evidence Pack

This evidence pack (`TW-DB00046-multi`) evaluated 9 TxGNN-predicted indications for insulin lispro. Only one — ranked lower by score — currently has literature support:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|------------|-----------------|-----------------|------------------|------|
| 1 | Autoimmune oophoritis | 99.78% | L5 | S0 | Hold | No known mechanistic link |
| 2 | Thiamine-responsive dysfunction syndrome | 99.37% | L5 | S0 | Hold | Diabetes component only; thiamine is first-line, not insulin |
| 3 | Classic stiff person syndrome | 99.36% | L5 | S0 | Hold | Comorbidity via anti-GAD65, not a treatment target |
| 4 | Focal stiff limb syndrome | 99.36% | L5 | S0 | Hold | Same anti-GAD65 comorbidity confound |
| 5 | Opsismodysplasia | 99.34% | L5 | S0 | Hold | No known pathway overlap |
| 6 | Drug-induced localized lipodystrophy | 99.09% | L4 | S0 | Hold | **Reverse causality** — insulin injection is a known cause of this condition |
| 7 | Pancreatic agenesis | 99.09% | L3 | S1 | Research Question | Insulin (incl. lispro) is already standard-of-care for PNDM due to pancreatic agenesis — extension of existing practice, not a novel repurposing signal |
| 8 | Centrifugal lipodystrophy | 99.04% | L5 | S0 | Hold | Same reverse-causality confound as #6 |
| 9 | Pressure-induced localized lipoatrophy | 99.03% | L5 | S0 | Hold | Same reverse-causality confound as #6 |

Three of the nine candidates (#6, #8, #9) are likely artifacts of insulin injection being a **cause** of localized lipodystrophy/lipoatrophy, not a treatment for it, and should be deprioritized rather than pursued. Candidate #7 (pancreatic agenesis) has the most substantive support in this pack but represents confirmation of existing clinical practice rather than a new repurposing opportunity.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (autoimmune oophoritis) has no supporting clinical trials, no literature, and no plausible mechanistic link per the evidence pack's own analysis — it most likely reflects an indirect knowledge-graph association rather than a genuine therapeutic signal. This does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a **Blocking** data gap (DG001), required before any S1 safety screening
- DrugBank mechanism-of-action data — currently a **High**-priority gap (DG002), needed to properly assess mechanistic plausibility
- A specific preclinical or case-level rationale connecting insulin signaling to autoimmune oophorits pathophysiology, if this candidate is to be pursued further
- If interest continues in this evidence pack, consider re-scoping evaluation toward candidate #7 (pancreatic agenesis), which has actual literature support, though it reflects standard-of-care confirmation rather than novel repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

