---
layout: default
title: Zonisamide
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

Using the evidence-pack rules directly (no skill match for this templated report-writing task).

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

Zonisamide is a broad-spectrum antiepileptic drug (AED), most established as adjunctive/monotherapy for partial-onset seizures. The TxGNN model's top-ranked prediction for this candidate is **Tourette syndrome** (score 99.85%), but this specific prediction is currently supported by **zero clinical trials and zero publications** — it is a pure model output with no confirmatory evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset seizures) — based on known AED classification; no formal Taiwan license text available (drug is unmarketed) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa` is a data gap). Based on known information, zonisamide belongs to the antiepileptic drug (AED) class, and its efficacy in epilepsy is well established clinically and pharmacologically (voltage-gated sodium/T-type calcium channel modulation, among other actions referenced throughout the AED literature in this pack).

The rationale offered for Tourette syndrome is that TxGNN's high score may reflect zonisamide's hypothesized dopaminergic/serotonergic modulatory effects, since Tourette syndrome is theoretically linked to dopamine pathway dysfunction. This is a plausible mechanistic *hypothesis*, not an evidence-backed connection — no clinical trial or published study in this pack tests zonisamide in Tourette syndrome specifically.

Given the complete absence of clinical trials or literature (evidence level L5), this prediction should be treated as a hypothesis-generation signal only, not a basis for clinical or regulatory action.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Zonisamide is not currently marketed in Taiwan (0 authorizations on file; `total_licenses` = 0, no license records available).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in this evidence pack — TFDA package insert retrieval is flagged as a **Blocking** data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests solely on a TxGNN score with no supporting clinical trials, literature, or confirmed mechanism of action — insufficient to justify any further evaluation stage (S0).

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data (DG001/DG002 remediation via DrugBank API)
- At minimum, preclinical or case-level evidence specifically linking zonisamide to Tourette syndrome before advancing past S0

---

**Note on this evidence pack:** This candidate bundle contains 10 TxGNN-predicted indications for zonisamide, several with materially stronger evidence than the top-ranked Tourette syndrome hit — notably **absence epilepsy** (L1, decision stage S3, "Proceed with Guardrails," supported by a 583-patient completed Phase 3 RCT) and **manic bipolar affective disorder** (L2, decision stage S1, "Research Question," supported by a dedicated RCT, PMID 22506436). If a repurposing report is desired for one of those higher-evidence candidates instead, a separate report should be generated using `predicted_indications[6]` (bipolar) or `predicted_indications[7]` (absence epilepsy) as the primary entry. Several other high-score predictions (methemoglobinemia variants) are flagged in the rationale as mechanistically *contradictory* — zonisamide's sulfonamide structure is a known methemoglobinemia risk factor, not a treatment — and should be treated as safety signals, not repurposing opportunities.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

