---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 9
---

# Deferiprone
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

# Deferiprone: From Iron Overload (Thalassemia) to Hepatic Porphyria

## One-Sentence Summary

Deferiprone is an oral iron chelator whose established clinical role — noted in the evidence pack's own rationale — is managing chronic iron overload from long-term transfusion (e.g., thalassemia major). The TxGNN model predicts it may be effective for **Hepatic Porphyria**, but this direction is currently supported only by **2 preclinical/animal publications** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron overload (chronic, transfusion-related — per evidence pack rationale; not marketed locally, so no formal approved-indication text is available) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the information present in this evidence pack, deferiprone is an oral iron-chelating agent, and its rationale entries indicate proven efficacy in reducing iron-catalyzed oxidative damage in transfusion-dependent iron overload states.

Mechanistically, hepatic porphyria and iron overload intersect through iron-driven oxidative stress: excess free iron catalyzes Fenton-type reactions that worsen porphyrin accumulation and associated hemolysis. Two preclinical studies in the evidence pack support this link — one showing iron chelation rescues hemolytic anemia and skin photosensitivity in a congenital erythropoietic porphyria model (PMID 32678895), and another showing an oral iron chelator (deferiprone) reduces uroporphyrin accumulation in a murine model of porphyria cutanea tarda (PMID 17854053).

However, both supporting studies are animal/preclinical in nature, with no human clinical trial or observational data identified. The mechanistic plausibility is reasonable, but translation to human hepatic porphyria remains unconfirmed.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preclinical/Animal | Blood | Iron chelation rescued hemolytic anemia and skin photosensitivity in a congenital erythropoietic porphyria (CEP) model, linked to reduced porphyrin isomer I overload |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Preclinical/Animal (murine) | Hepatology (Baltimore, Md.) | Oral iron chelator (deferiprone/L1) reduced hepatic uroporphyrin accumulation in Hfe(-/-) mice, comparable to iron-deficient diet approach for porphyria cutanea tarda |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the hepatic porphyria indication is limited to two preclinical/animal studies (L4) with no clinical trials or human data; the drug is also not currently marketed locally, and core safety documentation (TFDA warnings/contraindications, MOA) is flagged as a blocking data gap in this evidence pack.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (DG002)
- TFDA/local package insert data on warnings and contraindications before any S1 safety evaluation (DG001)
- Human clinical evidence (case series, observational, or trial data) in hepatic porphyria patients before advancing beyond a research-question stage
- Note: within this same evidence pack, beta-thalassemia with other manifestations (rank 8, L3, "Proceed with Guardrails") has materially stronger literature support and may be a more actionable near-term candidate than hepatic porphyria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

