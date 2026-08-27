---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: Evaluation Halted — Critical Data Gaps Identified

## Summary

Aprepitant (DrugBank: DB00673) is an NK1 (neurokinin-1) receptor antagonist approved internationally for prevention of chemotherapy-induced nausea and vomiting (CINV).
This Evidence Pack (v4, 2026-04-20) is **incomplete**: the TxGNN prediction pipeline has returned **no predicted indications**, and two critical data gaps remain unresolved.
No meaningful repurposing evaluation can proceed until these gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NK1 receptor antagonist / antiemetic (CINV prevention) |
| Predicted New Indication | Pending — TxGNN predictions not yet available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Evaluation Is Possible Yet

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002, severity: High). Based on publicly known information, Aprepitant is an NK1 receptor antagonist approved by FDA and EMA for prevention of CINV and postoperative nausea and vomiting (PONV). It is commonly co-administered with corticosteroids and 5-HT₃ antagonists as part of antiemetic prophylaxis regimens.

More critically, **TxGNN has not produced any predicted indications** for Aprepitant in this Evidence Pack (`predicted_indications` array is empty). Without a TxGNN prediction score and a target indication, the core repurposing hypothesis cannot be evaluated.

Two data gaps must be resolved before this candidate can advance:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA package insert warnings / contraindications | **Blocking** | Cannot complete S1 safety screening | Download TFDA insert PDF and parse |
| DG002 | Mechanism of action (MOA) | **High** | Cannot perform mechanism-relevance analysis | Query DrugBank API for DB00673 |

---

## Taiwan Market Information

Aprepitant has **zero** authorized licenses in Taiwan. It is not currently marketed domestically.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN predictions and two unresolved data gaps of Blocking/High severity; a repurposing evaluation report cannot be meaningfully generated at this stage.

**To proceed, the following is needed:**

1. **Run TxGNN prediction pipeline** — generate ranked indication predictions for Aprepitant and populate `predicted_indications`
2. **Resolve DG001** — download and parse the TFDA (or EMA/FDA) package insert PDF to extract key warnings and contraindications
3. **Resolve DG002** — query DrugBank API for Aprepitant's mechanism of action data
4. **Re-generate Evidence Pack** — once all gaps are resolved, produce a v5 Evidence Pack with complete data and resubmit for full report generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

