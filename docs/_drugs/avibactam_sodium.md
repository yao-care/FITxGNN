---
layout: default
title: Avibactam Sodium
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 0
---

# Avibactam Sodium
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

# Avibactam Sodium: Repurposing Evaluation Inconclusive — No TxGNN Predictions Available

## One-Sentence Summary

Avibactam Sodium is a non-β-lactam β-lactamase inhibitor, used in combination with ceftazidime to treat serious gram-negative bacterial infections. The TxGNN model did not generate any repurposing predictions for this compound in the current evidence pack, and no Finland regulatory authorizations are on file. A formal repurposing evaluation cannot be conducted at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (combination partner of ceftazidime; evidence from external domain knowledge — not present in evidence pack) |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no predictions generated |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction is Available

Avibactam Sodium is a β-lactamase inhibitor without intrinsic antibacterial activity. Its sole mechanism of action is irreversible, covalent binding to serine β-lactamases (class A, C, and some class D enzymes), thereby shielding its combination partner (ceftazidime) from enzymatic inactivation. This highly specific, adjunctive mechanistic role — rather than a direct receptor-mediated or pathway-level effect — may limit TxGNN's ability to identify disease-graph associations for the compound as a standalone node.

Additionally, the evidence pack confirms no DrugBank ID was resolved (`drugbank_id: null`) and no original indications were populated. The absence of a mapped knowledge graph node is the most likely technical reason no predictions were returned.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack contains no TxGNN repurposing predictions, no Finland regulatory authorizations, and no safety data. There is no evidentiary basis on which to proceed with a repurposing evaluation.

**To proceed, the following is needed:**

- **Resolve DrugBank ID**: Confirm whether Avibactam Sodium has a DrugBank entry (it may be listed under the combination product Ceftazidime-Avibactam, DB09050) and re-map the knowledge graph node.
- **Clarify evaluation scope**: Determine whether the evaluation target is Avibactam Sodium as a standalone compound or the Ceftazidime-Avibactam combination — TxGNN predictions will differ significantly between the two.
- **Re-run TxGNN pipeline**: Once the node is correctly mapped, rerun prediction to obtain scored indication candidates.
- **Retrieve package insert**: Obtain warnings, contraindications, and MOA from the official Finnish/EMA-approved SmPC (Zavicefta).
- **Populate original indications**: Register the approved indications (complicated UTI, complicated IAI, hospital-acquired/ventilator-associated pneumonia) in the evidence pack before re-evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

