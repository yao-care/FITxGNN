---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
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

# Hydroxocobalamin: From Vitamin B12 Deficiency / Cyanide Poisoning to Esophageal Varices without Bleeding

## One-Sentence Summary

Hydroxocobalamin is clinically known for treating vitamin B12 deficiency and as an antidote for cyanide poisoning, though this specific approved-indication data was not captured in the current evidence pack. The TxGNN model predicts it may be effective for **Esophageal Varices (without bleeding)** — and, at an identical score, for esophageal varices *with* bleeding — but currently **zero clinical trials** and **zero publications** support either direction, and no plausible pharmacological mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency; cyanide poisoning antidote (from known drug class information — not confirmed via a Finnish regulatory source in this evidence pack) |
| Predicted New Indication | Esophageal Varices without Bleeding (a second, identically-scored prediction exists for esophageal varices *with* bleeding) |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for hydroxocobalamin in this evidence pack (flagged as a High-severity data gap). Based on known clinical use, hydroxocobalamin acts as a vitamin B12 precursor for deficiency replacement and, at high doses, as a cyanide antidote (it binds cyanide ions to form cyanocobalamin, which is renally excreted).

Neither of these established mechanisms offers a pharmacological rationale for a role in esophageal varices, which are a manifestation of portal hypertension typically managed with agents that modulate splanchnic blood flow or portal pressure (e.g., octreotide, terlipressin, vasopressin, non-selective beta-blockers). There is no known hemodynamic, vasoactive, or vascular-remodeling effect of hydroxocobalamin that would connect it to this indication.

Given this, the TxGNN score of 99.23% should be interpreted strictly as a knowledge-graph correlation, not as evidence of biological plausibility. With no clinical trials, no literature, and no identifiable mechanistic link, this prediction currently lacks a testable scientific hypothesis and sits at the lowest confidence tier (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Hydroxocobalamin is not currently marketed in Finland (0 authorizations on record), so no product/authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a raw TxGNN model score, with no clinical trials, no literature, and no identifiable mechanistic rationale connecting hydroxocobalamin to esophageal varices. This is an L5 / S0 candidate and does not meet the bar to advance to safety or clinical evaluation.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (currently blocking — safety profile cannot be assessed)
- Confirmed mechanism of action (DrugBank query)
- A plausible biological hypothesis linking hydroxocobalamin to portal hypertension/variceal pathophysiology before further evidence search is warranted
- Ongoing monitoring for any new trials or literature on this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

