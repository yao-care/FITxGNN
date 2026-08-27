---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Laronidase: Evaluation Incomplete — No Repurposing Prediction Available

## One-Sentence Summary

Laronidase (DrugBank: DB00090) is a recombinant enzyme replacement therapy whose original indication data is absent from this Evidence Pack.
The TxGNN model has **not generated any predicted new indications** for this compound, and two blocking data gaps — mechanism of action and safety information — prevent a complete repurposing evaluation.
No supporting clinical trials or publications are available at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | None — no predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No actual studies, prediction data absent |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indications are currently available for Laronidase. Without a target indication, it is not possible to construct a mechanistic rationale for repurposing, or to assess whether the drug's mode of action is transferable to a new disease context.

Mechanism of action data (DG002) has been flagged as a High-severity data gap. Although Laronidase is generally understood to function as a recombinant form of alpha-L-iduronidase — an enzyme involved in glycosaminoglycan catabolism — this information has not been formally populated in the Evidence Pack and therefore cannot be cited as the basis for any prediction.

Original indication data is also absent (`original_indications: []`). Combined with the missing MOA, the foundational inputs required by the repurposing evaluation framework are not yet in place. This report will be updated once data gaps are resolved and TxGNN predictions are available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Laronidase is not currently marketed in Finland. No marketing authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is structurally incomplete — TxGNN has not generated any predicted indications for Laronidase, and two data gaps (DG001, DG002) are blocking the minimum required inputs for safety and mechanistic evaluation.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain Finnish prescribing information (warnings, contraindications) via package insert PDF from the regulatory authority's website
- **Resolve DG002 (High):** Populate mechanism of action by querying the DrugBank API for DB00090
- **Populate `original_indications`:** Known indication (Mucopolysaccharidosis type I / Hurler syndrome) should be extracted from DrugBank and entered into the Evidence Pack
- **Re-run TxGNN prediction pipeline:** Laronidase does not appear in the current predicted indications output — verify whether the compound was included in the input drug list and re-execute if necessary
- **Re-run evidence collection:** Once predictions are available, trigger the clinical trial and literature retrieval pipeline for the top-ranked predicted indication

---

> ⚠️ **Note:** This report reflects the state of the Evidence Pack as of 2026-04-20. All sections will be revised once data gaps DG001 and DG002 are resolved and TxGNN predictions are generated. Results are for research purposes only and do not constitute medical advice.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

