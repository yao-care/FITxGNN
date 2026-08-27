---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Diseases (PNH/aHUS) to G6PC3-Deficient Congenital Neutropenia

## One-Sentence Summary

Ravulizumab is a long-acting anti-complement C5 monoclonal antibody, with established use in complement-mediated diseases such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS). The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but this is currently a **model prediction only** — no clinical trials or published literature support this direction, and the evidence pack's own mechanistic review flags the biological rationale as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Taiwan regulatory data; per the mechanistic rationale, ravulizumab's established use is in complement-mediated diseases (PNH, aHUS) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% (model rank 731) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ravulizumab is not available in this evidence pack (flagged as a High-severity data gap). Based on known information referenced in the model's own rationale, ravulizumab is a long-acting anti-C5 monoclonal antibody that blocks the terminal complement pathway (membrane attack complex formation); its efficacy in complement-driven diseases such as PNH and aHUS is well established.

G6PC3-deficient congenital neutropenia, however, is caused by glucose-6-phosphatase catalytic subunit 3 deficiency, which increases endoplasmic reticulum stress and apoptosis in neutrophil precursors through a glucose/glycosylation metabolic defect — a pathway that does not intersect with terminal complement activation. The evidence pack explicitly notes there is **no direct mechanistic link** between the two conditions, and characterizes this prediction as a similarity-based extrapolation by TxGNN across a broad "rare hematologic/immune disease" category rather than a validated pathophysiological connection.

Given this, the prediction should be read as a hypothesis-generating signal rather than a mechanistically grounded repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Ravulizumab currently holds no marketing authorization on file for this region (0 licenses; market status: 未上市 / not marketed), so no product-level licensing details are available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack; a TFDA package insert lookup is flagged as a Blocking data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, preclinical, or literature evidence for this indication, and the model's own mechanistic review found no direct pathway linking C5/complement inhibition to G6PC3-deficient neutropenia — the association is a category-level similarity extrapolation, not a validated hypothesis.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action data from DrugBank or primary literature
- Preclinical or mechanistic studies directly testing complement pathway involvement in G6PC3-deficient neutropenia
- Real-world or trial-registry evidence (ClinicalTrials.gov, ICTRP) before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

