---
layout: default
title: Azathioprine
parent: Pelkkä mallin ennuste (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Azathioprine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Azathioprine: Evaluation Report — Insufficient Data for Repurposing Assessment

## One-Sentence Summary

Azathioprine (DB00993) is a candidate submitted for TxGNN drug repurposing evaluation. However, this Evidence Pack contains **no predicted new indications**, **no mechanism of action data**, and **no safety information**, making a complete repurposing assessment impossible at this stage. A data remediation effort is required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No predictions available |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Finland Market Information

Azathioprine currently holds **no marketing authorizations** in Finland according to the data queried on 2026-03-29. No product listings, dosage forms, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Azathioprine is missing all three elements required for a repurposing evaluation: TxGNN predictions, mechanism of action data, and safety/contraindication information. No recommendation for or against repurposing can be issued until these gaps are resolved.

**To proceed, the following is needed:**

- **\[Blocking\] Predicted Indications**: The `predicted_indications` array is empty. Re-run the TxGNN pipeline for DB00993 to generate candidate indications with scores, supporting clinical trials, and literature.
- **\[Blocking\] Safety Data (DG001)**: Key warnings and contraindications were not retrieved. Download and parse the package insert PDF from the relevant regulatory authority to enable the S1 safety pre-screening step.
- **\[High\] Mechanism of Action (DG002)**: MOA data is absent. Query the DrugBank API for DB00993 to populate `original_moa`, which is required for the mechanistic rationale section of the evaluation.
- **\[Recommended\] Original Indications**: The `original_indications` field is empty. Populate this from DrugBank or the package insert to enable the "From X to Y" repurposing narrative.

Once the above data gaps are resolved and the Evidence Pack is regenerated at v5 or later, a full evaluation report can be produced.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

