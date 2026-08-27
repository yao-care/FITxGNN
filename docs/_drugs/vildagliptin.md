---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Vildagliptin is a DPP-4 (dipeptidyl peptidase-4) inhibitor established for the treatment of type 2 diabetes mellitus. The TxGNN model's top-ranked prediction for this drug is **Classic Stiff Person Syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-generated hypothesis with no corroborating clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (per supporting literature; no formal Finland label text on file) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for vildagliptin is not available in this evidence pack. Based on information contained in the supporting literature collected for other candidate indications, vildagliptin belongs to the DPP-4 inhibitor class: it blocks degradation of the incretin hormones GLP-1 and GIP, thereby enhancing glucose-dependent insulin secretion and suppressing glucagon release. Its efficacy in type 2 diabetes has been established through extensive clinical use.

Classic Stiff Person Syndrome is a rare autoimmune central nervous system disorder, most commonly associated with anti-GAD65 antibodies, that causes progressive muscle rigidity and spasms. Per the evidence pack's own repurposing rationale, there is **no known mechanistic link** between DPP-4/incretin-pathway modulation and the autoimmune, GABAergic-neuron-directed pathophysiology underlying this disease.

The very high TxGNN score paired with a complete absence of clinical, preclinical, or mechanistic evidence is consistent with how graph neural network models can surface high-confidence link predictions for rare diseases with sparse knowledge-graph connectivity, independent of established biology. This candidate should be treated strictly as a hypothesis-generating signal, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Vildagliptin is not currently marketed in Finland, and no marketing authorizations are on record for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction sits at evidence level L5 with zero clinical trials and zero literature support, and the drug's own repurposing rationale explicitly states there is no known mechanistic connection between DPP-4 inhibition and stiff person syndrome pathophysiology. There is no basis to advance beyond model prediction at this time.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- DrugBank-sourced mechanism of action data — currently a **High**-severity gap (DG002)
- Any preclinical or mechanistic study specifically linking incretin/DPP-4 pathway modulation to GAD65-mediated autoimmune neurological disease, before this candidate can move past S0
- Note: within the same evidence pack, the rank-10 prediction (**Type 1 Diabetes Mellitus**, L2, decision stage S2, 50 trials incl. 1 RCT) has materially stronger support and may warrant separate, prioritized evaluation ahead of this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

