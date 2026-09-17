---
layout: default
title: Apalutamide
parent: Pelkkä mallin ennuste (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
---

# Apalutamide
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

# Apalutamide: Repurposing Evaluation — No Predictions Available

## Summary

Apalutamide (DB11901) is a drug currently not approved in Finland. The TxGNN model returned **no predicted new indications** for this candidate in the current dataset. Critical data items — including original indications, mechanism of action, and safety information — are also absent, making a complete repurposing evaluation impossible at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Finland Market Information

Apalutamide has no registered authorizations in Finland. No license records, approved dosage forms, or approved indications are available in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no candidate indications for Apalutamide, and the absence of original indication data, mechanism of action, and safety information means there is no basis for a repurposing evaluation at this time.

**To proceed, the following is needed:**

- **TxGNN prediction**: Re-run the prediction pipeline with Apalutamide's DrugBank graph embeddings to determine whether a candidate indication score can be generated
- **Mechanism of action**: Query the DrugBank API (DB11901) to retrieve pharmacological class, target, and MOA
- **Original indications**: Parse the TFDA package insert PDF (already located per query log) to extract approved indications and safety warnings
- **Finland regulatory check**: Verify Fimea database directly to confirm current approval and market status
- **Safety data**: Extract key warnings, contraindications, and drug interactions from the package insert before proceeding to safety screen
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

