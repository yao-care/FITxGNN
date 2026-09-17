---
layout: default
title: Baricitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 62
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# BARICITINIB: Drug Repurposing Evaluation — Data Collection Incomplete

## One-Sentence Summary

BARICITINIB is a JAK1/JAK2 inhibitor approved in multiple countries for rheumatoid arthritis and other inflammatory conditions.
The current Evidence Pack does not contain TxGNN prediction results for new indications, and the drug holds **no marketing authorization in Finland**.
A complete repurposing evaluation cannot be conducted until the blocking data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | No TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model output absent |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Full Prediction Analysis Cannot Proceed

Two blocking data gaps prevent a standard evaluation:

**DG001 (Blocking):** Package insert warnings and contraindications have not been parsed. Without this, the mandatory S1 safety pre-screening cannot be completed, and any repurposing candidate assessment would be unsafe to advance.

**DG002 (High):** Mechanism of action data from DrugBank has not been retrieved. Without MOA, it is impossible to explain why BARICITINIB's pharmacology might transfer to a new indication — a core requirement of the evaluation framework.

In addition, the `predicted_indications` field returned an empty array, meaning TxGNN has either not yet been run for this drug or produced no ranked candidates. All downstream sections (clinical trial evidence, literature evidence, predicted indication overview) depend on this output and cannot be populated.

---

## Finland Market Information

BARICITINIB currently holds **no marketing authorization** in Finland. No registered products, dosage forms, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — TxGNN predictions are absent and a Blocking-severity data gap (DG001) prevents safety pre-screening. Advancing this candidate without resolving these gaps would be methodologically unsound.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download and parse the BARICITINIB package insert PDF from the TFDA website to extract warnings and contraindications; this unlocks the S1 safety gate
- **[High — DG002]** Query the DrugBank API for BARICITINIB (DB11817) to retrieve MOA, drug categories, and toxicity data
- **[Required]** Run the TxGNN model for DB11817 to generate ranked predicted indications; without `predicted_indications`, no repurposing target can be evaluated
- **[Required]** Re-run the evidence collection pipeline (clinical trials, literature) once a predicted indication is confirmed
- **[Optional]** Verify Finland EMA/Fimec authorization status via the national medicines database for any recent approvals not captured in this query cycle
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

