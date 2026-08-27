---
layout: default
title: Pegvaliase
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 3
---

# Pegvaliase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pegvaliase: From Phenylketonuria (PKU) to Diabetic Retinopathy (Predicted)

## One-Sentence Summary

Pegvaliase (DrugBank DB12839) is a PEGylated phenylalanine ammonia lyase (PAL) enzyme therapy used to lower blood phenylalanine levels in patients with phenylketonuria (PKU) — this background is inferred from the model's own rationale text, as no formal original-indication or regulatory data is on file. The TxGNN model predicts potential effectiveness for **Diabetic Retinopathy**, with a prediction score of **99.17%**, but currently **zero clinical trials and zero publications** support this direction. This is a model-only (L5) prediction with no biological plausibility established, and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in regulatory data (drug not marketed in Finland); background pharmacology indicates use in PKU-associated hyperphenylalaninemia |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.17% (rank 8141 in model output) |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data is flagged as a data gap in this evidence pack (DG002, High severity). However, the model's own repurposing rationale describes Pegvaliase's known pharmacology: it catabolizes circulating phenylalanine via PAL enzyme activity, and is used to manage hyperphenylalaninemia in PKU patients.

Diabetic retinopathy has a fundamentally different pathophysiology — chronic hyperglycemia driving retinal microvascular basement membrane thickening, pericyte loss, VEGF-driven neovascularization, and vascular leakage. There is no known biochemical or pharmacological intersection between phenylalanine metabolism/PAL enzyme activity and this VEGF/microvascular disease pathway.

Based on the evidence pack's own assessment, the high TxGNN score is most likely a **false positive** arising from indirect knowledge-graph topology — for example, shared nodes such as "metabolic disease" or PKU-associated ocular/neurological complications connecting to diabetes-related eye disease clusters, rather than a genuine shared mechanism. The two related predictions (severe nonproliferative diabetic retinopathy, and diabetic cataract) are sub-classifications or variants of the same diabetic-eye-disease cluster and share this same lack of independent mechanistic support — they appear to be redundant outputs of the same underlying graph artifact rather than three independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Confirmed by direct ClinicalTrials.gov and ICTRP queries for Pegvaliase against diabetic retinopathy, severe NPDR, and diabetic cataract — all returned zero results.)*

---

## Literature Evidence

Currently no related literature available.

*(Confirmed by direct PubMed queries for Pegvaliase against diabetic retinopathy, severe NPDR, and diabetic cataract — all returned zero results.)*

---

## Finland Market Information

Pegvaliase currently holds no marketing authorization in Finland — market status is **Not Marketed**, with 0 authorizations on file. No product, dosage form, or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No key warnings, contraindications, or drug interaction data are currently on file for Pegvaliase in this evidence pack; TFDA package insert data collection (DG001, Blocking severity) is still pending.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by the TxGNN model score (L5), with no clinical trials, no literature, and no established biological mechanism linking PAL enzyme activity to diabetic retinopathy pathophysiology. The evidence pack itself assesses this as a likely knowledge-graph false positive. This does not meet the threshold to advance to safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/EMA package insert data (warnings, contraindications) to close Blocking data gap DG001
- Verified, structured mechanism-of-action data to close High-severity data gap DG002
- Independent biological plausibility review (e.g., any evidence of phenylalanine/PAL pathway involvement in retinal microvascular disease)
- Continued periodic monitoring of ClinicalTrials.gov, ICTRP, and PubMed for emerging evidence, since none currently exists for any of the three related predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

