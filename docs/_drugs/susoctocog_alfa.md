---
layout: default
title: Susoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog Alfa: From Acquired Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Susoctocog alfa is a recombinant, B-domain deleted, porcine sequence Factor VIII (FVIII) product, best documented in the literature for treating bleeding episodes in **acquired hemophilia A (AHA)**. The TxGNN model's top-ranked prediction for this drug is **primary release disorder of platelets**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the underlying rationale explicitly notes the mechanism does not align with FVIII replacement therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acquired Hemophilia A / bleeding episodes (per literature; not confirmed in Finnish regulatory records) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for susoctocog alfa is not available in the structured drug record. Based on the surrounding literature, susoctocog alfa (recombinant porcine FVIII, marketed elsewhere as Obizur) is used to replace Factor VIII activity in patients whose endogenous FVIII is neutralized by autoantibodies (acquired hemophilia A), restoring the intrinsic coagulation pathway to control bleeding.

Primary release disorder of platelets, however, is a disease of impaired platelet granule secretion — patients have normal platelet counts and normal coagulation factor levels, but platelets fail to release their granule contents (ADP, serotonin, etc.) needed to amplify aggregation. This is mechanistically distinct from FVIII deficiency or FVIII autoantibody neutralization.

The evidence pack's own repurposing rationale for this candidate states this directly: there is no clear physiological link between exogenous FVIII replacement and correcting a platelet granule release defect. The high TxGNN score therefore reflects a graph-based similarity signal (both diseases fall under a broad "bleeding disorder" neighborhood) rather than a validated pharmacological mechanism, and it is not corroborated by any clinical trial or published case evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Susoctocog alfa is not currently marketed in Finland — the regulatory record shows 0 authorizations, so no product/dosage-form details are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Fimea/TFDA package insert warnings, contraindications, and DDI data are flagged as blocking data gaps (DG001) in the evidence pack and have not yet been retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, this candidate has no clinical trial or literature support, and the evidence pack's own mechanistic assessment concludes there is no credible biological link between FVIII replacement and correcting a platelet granule release defect. This does not meet the bar to advance past model-only prediction (L5).

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for susoctocog alfa (DG002)
- Fimea/TFDA package insert — warnings, contraindications, and DDI data (DG001)
- Any preclinical or translational evidence connecting FVIII activity to platelet granule secretion pathways, if this indication is to be pursued further
- Note: the same evidence pack shows stronger, more mechanistically coherent support for FVIII-pathway-adjacent indications (e.g., "hemophilia" and "acquired coagulation factor deficiency," ranks 4–5, which reference the drug's existing AHA evidence base) — these may warrant a separate evaluation rather than being treated as novel repurposing candidates, since they largely overlap with the drug's known use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

