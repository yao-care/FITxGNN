---
layout: default
title: Axicabtagene Ciloleucel
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 0
---

# Axicabtagene Ciloleucel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Axicabtagene Ciloleucel: Repurposing Evaluation — Insufficient Evidence Pack

## One-Sentence Summary

Axicabtagene ciloleucel (DB13915) is a CD19-directed CAR-T cell immunotherapy; however, the current Evidence Pack contains no original indication records, no TxGNN-predicted indications, and no mechanism-of-action data.
Without a predicted new indication, a standard repurposing evaluation **cannot be completed at this time**.
The recommended action is to remediate all Blocking/High-severity data gaps before re-running the pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no predictions generated) |
| Finland Market Status | Not marketed (0 authorisations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The `predicted_indications` array in the Evidence Pack is empty. This typically occurs for one of two reasons:

1. **Model scope**: The TxGNN knowledge graph may not include the DrugBank node for `DB13915` (axicabtagene ciloleucel) because CAR-T cell therapies are living-cell products whose graph representation differs from small-molecule drugs.
2. **Pipeline gap**: The prediction step may not have been executed, or the disease-mapping step (KG → MeSH/ICD) produced no matched candidates above threshold.

Currently, detailed mechanism-of-action data is also unavailable. Based on known information, axicabtagene ciloleucel belongs to the CD19-targeting CAR-T cell therapy class; its efficacy in relapsed/refractory large B-cell lymphoma has been established in registrational trials, and mechanistically its approach could in principle extend to other CD19-expressing haematological malignancies — but **this cannot be formally evaluated without Evidence Pack data**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Finland Market Information

No marketing authorisations on file for axicabtagene ciloleucel in this Evidence Pack.

---

## Cytotoxicity

Axicabtagene ciloleucel is an antineoplastic cellular product (CAR-T immunotherapy targeting CD19). The following is noted from the DrugBank record retrieved in this run; detailed package-insert toxicity data was not parsed into the Evidence Pack.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Cellular immunotherapy (CAR-T; not conventional cytotoxic) |
| Myelosuppression Risk | High — cytokine release syndrome and haematological toxicity are class effects of CAR-T therapies |
| Emetogenicity Classification | Low (primary toxicity is CRS/neurotoxicity, not emetogenicity) |
| Monitoring Items | CBC with differential, liver function, renal function, neurological status, ferritin, CRP (CRS monitoring) |
| Handling Protection | Must follow guidelines for handling of genetically modified cellular products; standard cytotoxic handling precautions apply |

> **Note:** The above is based on CAR-T class knowledge. Please refer to the full package insert (Yescarta® SmPC) for product-specific warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no predicted indications, no original indication records, and no mechanism-of-action data; a drug repurposing evaluation cannot be meaningfully completed or scored without these inputs.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve TFDA (or EMA/FDA) package insert PDF and parse warnings, contraindications, and approved indications
- **[DG002 — High]** Query DrugBank API for MOA, pharmacology, and drug categories for `DB13915`
- **Re-run TxGNN pipeline** after confirming that the `DB13915` node is present in the knowledge graph and that the prediction + disease-mapping steps complete successfully
- **Verify KG node type**: Confirm whether axicabtagene ciloleucel is modelled as a small-molecule node or a biologic/cell-therapy node in the TxGNN graph, as this affects prediction coverage
- Once predictions are available, re-generate this Evidence Pack (v5+) and re-run the evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

