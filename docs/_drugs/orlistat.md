---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

> Orlistat is a lipase inhibitor whose established clinical role is in weight management (obesity); however, the structured "original indication" field in this evidence pack is empty (data gap).
> The TxGNN model predicts a possible link to **Hypervitaminosis**, but this is currently supported by **0 clinical trials** and **0 publications** — prediction score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in evidence pack (flagged as data gap, DG002); commonly known clinically as obesity/weight management (gastric & pancreatic lipase inhibitor) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack's structured `original_moa` field (data gap DG002). However, the repurposing rationale supplied alongside the prediction describes the relevant pharmacology: Orlistat inhibits gastric and pancreatic lipase, blocking triglyceride hydrolysis and reducing intestinal fat absorption by roughly 30%.

This same lipase-inhibition mechanism also reduces intestinal absorption of the fat-soluble vitamins (A, D, E, K). That provides a theoretical, indirect rationale for using orlistat to lower circulating levels in cases of fat-soluble vitamin excess — such as hypervitaminosis A.

This link should be treated as inferential rather than mechanistically targeted: orlistat was not designed against hypervitaminosis pathology, and because both the original-indication field and the formal MOA field are data gaps, the pathway cannot be fully verified against source documentation at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Orlistat is not currently marketed in Finland — no marketing authorizations are on record (total_licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is model-generated only (L5), with no clinical trials or literature identified for hypervitaminosis. Critically, TFDA warning/contraindication data is missing and flagged as a **Blocking** gap (DG001) — the candidate cannot proceed to S1 safety initial review without it.

**To proceed, the following is needed:**
- TFDA package insert data — warnings and contraindications (DG001, Blocking; source: TFDA official site)
- Confirmed original indication and mechanism-of-action data via DrugBank (DG002, High)
- Preclinical or observational evidence directly linking lipase inhibition to fat-soluble vitamin clearance in hypervitaminosis
- Ongoing monitoring for new clinical trials or publications on this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

