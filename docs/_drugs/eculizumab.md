---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Paroxysmal Nocturnal Hemoglobinuria to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor whose established use is in complement-mediated disorders such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS). The TxGNN model predicts it may be effective for **Cyclic Hematopoiesis**, but this ranking is driven purely by embedding similarity — **0 clinical trials** and **0 publications** support this specific pairing, and the underlying disease biology (ELANE-driven neutrophil cycling) has no known connection to the complement pathway.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complement-mediated disorders (PNH, atypical HUS) — inferred from literature captured in this evidence pack; not separately confirmed via structured drug record |
| Predicted New Indication | Cyclic Hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action data for eculizumab is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in the supporting literature and rationale records, eculizumab is a humanized monoclonal antibody that binds complement protein C5, blocking its cleavage into C5a and C5b-9, thereby preventing terminal complement (membrane attack complex) activation. This mechanism underlies its established efficacy in complement-driven hematologic disease (PNH, aHUS) and, per the qualitative literature captured here, in other complement-associated conditions such as thrombotic microangiopathies and CD59-deficiency syndromes.

Cyclic hematopoiesis, however, is a periodic disorder of granulocyte production caused by ELANE (neutrophil elastase) mutations, affecting myeloid progenitor differentiation and survival — a pathway with no established link to terminal complement activation. The repurposing rationale attached to this candidate explicitly states there is no known mechanism by which C5 blockade would correct an ELANE-driven cycling defect, and this ranking derives entirely from TxGNN's learned embedding similarity between diseases, not from any shared pathophysiology.

Given this mechanistic disconnect and the complete absence of clinical or literature evidence, this prediction should be read as a hypothesis-generating signal only, not as a clinically supported repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

No marketing authorization records are available for this market — eculizumab is currently **not marketed** in this region (0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert data has not yet been obtained — flagged as a Blocking data gap, DG001, required before any Stage 1 safety assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN embedding similarity (L5, S0) with zero clinical trials and zero literature evidence, and the repurposing rationale itself identifies no plausible mechanistic link between complement C5 inhibition and ELANE-driven cyclic hematopoiesis. Note that 9 additional TxGNN-predicted indications for this candidate (all congenital neutropenia/immunodeficiency syndromes) were reviewed alongside this one and show the same pattern — high similarity scores but no mechanistic, trial, or genuinely on-topic literature support.

**To proceed, the following is needed:**
- TFDA/local regulatory package insert (warnings, contraindications) — currently a blocking gap
- Confirmed mechanism-of-action documentation from DrugBank or primary literature
- Preclinical or mechanistic studies directly linking complement pathway activity to ELANE-mediated neutrophil cycling, if such a link is ever established
- Re-screening of literature search terms, since prior queries for related candidates (e.g., rank 4 and rank 10) returned matches driven by keyword overlap rather than disease-specific relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

