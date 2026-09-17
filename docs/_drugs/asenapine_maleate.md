---
layout: default
title: Asenapine Maleate
parent: Pelkkä mallin ennuste (L5)
nav_order: 43
evidence_level: L5
indication_count: 0
---

# Asenapine Maleate
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **0** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# ASENAPINE MALEATE: Evaluation Pending — Critical Data Gaps

## One-Sentence Summary

Asenapine maleate was queried against the Taiwan TFDA database with no approved registrations found in Taiwan.
No TxGNN repurposing predictions are available in the current Evidence Pack, and **critical data gaps** in the mechanism of action and safety information prevent a complete evaluation.
The DrugBank and TFDA package insert queries each returned one record, but the data has not yet been integrated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication found in Taiwan |
| Predicted New Indication | Not available — TxGNN prediction not generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Insufficient data |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN prediction data is present in the current Evidence Pack, so no mechanistic reasoning can be offered at this stage.

The mechanism of action has not been retrieved despite DrugBank returning one record (query log ID 3, run 2026-03-29). Similarly, the TFDA package insert query returned one record (query log ID 4, same date), which should contain original indication and safety information. Neither dataset has been parsed into the Evidence Pack fields — these two sources together would be sufficient to unlock the next evaluation step.

Until those records are integrated, any mechanistic or clinical justification for repurposing would be speculative and cannot be included in this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN predictions, no original indication, no mechanism of action, and no safety data — the minimum inputs required for a repurposing evaluation are not met.

**To proceed, the following is needed:**

- Parse and integrate the DrugBank record already retrieved (query log ID 3) to populate MOA, drug categories, and toxicity data
- Parse and integrate the TFDA package insert record already retrieved (query log ID 4) to populate original indication and safety warnings
- Re-run TxGNN prediction pipeline for ASENAPINE MALEATE to generate candidate indications with scores
- After predictions are available, re-run the evidence collection step (clinical trials + literature) for the top-ranked indication
- Rebuild the Evidence Pack and regenerate this report
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

