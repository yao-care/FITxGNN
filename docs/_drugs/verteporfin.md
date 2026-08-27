---
layout: default
title: Verteporfin
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 1
---

# Verteporfin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Verteporfin: From Photodynamic Therapy for Neovascular AMD to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Verteporfin (DrugBank DB00460) is a benzoporphyrin-derivative photosensitizer established in photodynamic therapy for choroidal neovascularization. The TxGNN model predicts it may be relevant to **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no independent evidence yet.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Photodynamic therapy for choroidal neovascularization (e.g. age-related macular degeneration) — based on established pharmacological knowledge; not present in this evidence pack, which has no `original_indications` data |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% (global rank 5558) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as data gap **DG002**, High severity). Based on established pharmacological knowledge, verteporfin accumulates preferentially in proliferating/neovascular tissue and, once activated by non-thermal red light, generates reactive oxygen species that selectively damage the target endothelium — its established clinical role is ophthalmic photodynamic therapy.

The predicted indication — a nuclear-DNA-related mitochondrial OXPHOS disorder — has no obvious mechanistic overlap with this photoactivation pathway. TxGNN's score reflects a knowledge-graph association rather than a validated pharmacological link, and the pack's own `repurposing_rationale` fields (`mechanistic_link`, `similarity_to_original`) are both marked **pending**, meaning expert mechanistic review has not yet been done.

Because the original indication itself is also missing from this evidence pack (empty `original_indications`), the comparison between original and predicted indications cannot be substantiated from the data provided. This prediction should be treated as hypothesis-generating only, pending mechanistic review and confirmation of TFDA/regulatory labeling (data gap **DG001**, Blocking severity).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Verteporfin is not marketed in Taiwan (market status: 未上市), with 0 active authorizations recorded — no license table available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with no clinical trials, no literature, and no mechanistic analysis completed, combined with a Blocking data gap on TFDA labeling. There is currently insufficient evidence to proceed even under guardrails.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap DG001
- Verified mechanism of action (DrugBank/primary literature) — High gap DG002
- Confirmed original indication data (currently empty in this pack)
- Completion of `mechanistic_link` and `similarity_to_original` rationale analysis
- Ongoing monitoring for emerging clinical trials or literature on this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

