---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide: Repurposing Evaluation — Evidence Pack Incomplete

## One-Sentence Summary

Arsenic Trioxide (DB01169) is a well-established antineoplastic agent; however, this Evidence Pack contains **no TxGNN predicted indications**, and critical data fields — including original indications, mechanism of action, and safety warnings — are either missing or not yet populated.
A full repurposing evaluation cannot be completed at this stage.
The overall evidence level is **L5** and the recommended decision is **Hold** pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in Evidence Pack |
| Predicted New Indication | None — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model data not yet available |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predictions are present in this Evidence Pack (`predicted_indications: []`), so a data-driven repurposing rationale cannot be generated at this time.

Additionally, the mechanism of action is flagged as **Data Gap DG002** (severity: High), which means even a qualitative mechanistic bridge between a source indication and a candidate new indication cannot be constructed. Until DrugBank API data is retrieved and parsed, any mechanistic claim would be speculative.

Currently, detailed mechanism of action data is not available. Based on known pharmacological class, Arsenic Trioxide belongs to the arsenic compound category with established antineoplastic activity; however, this must be formally confirmed via DrugBank (DB01169) before it can be used to support a repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Taiwan Market Information

Arsenic Trioxide is currently **not marketed in Taiwan**. No drug authorizations are on file (total licenses = 0). No license table can be generated.

---

## Cytotoxicity

Arsenic Trioxide belongs to a class of antineoplastic agents (arsenic compounds); a cytotoxicity section is included accordingly.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Arsenic compound |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests, renal function, ECG (QTc interval), serum electrolytes (potassium, magnesium) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Both key warnings (DG001, severity: **Blocking**) and contraindications are listed as data gaps. The TFDA package insert PDF must be retrieved and parsed before any safety screening can proceed. DDI query returned no results (status: `not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is critically incomplete — there are no TxGNN predicted indications, no mechanism of action data, and safety information is blocked pending package insert retrieval. A repurposing evaluation cannot responsibly proceed until these gaps are closed.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve and parse the TFDA package insert PDF to extract warnings and contraindications; this is a prerequisite for the S1 safety screening gate
- **[DG002 — High]** Query DrugBank API (DB01169) to populate mechanism of action, drug categories, and toxicity profile
- **Re-run TxGNN pipeline** after data gaps are resolved to generate `predicted_indications` — without this, no repurposing candidate can be evaluated
- **DDI re-query** once the drug identity and formulation details are confirmed in DrugBank
- **Taiwan market status cross-check** — confirm whether any foreign authorizations (e.g., FDA Trisenox, EMA Trisenox) could support a bridging regulatory strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

