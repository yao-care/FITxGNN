---
layout: default
title: Axitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: Insufficient Data for Repurposing Analysis

## One-Sentence Summary

Axitinib (Inlyta) is a selective VEGFR-1/2/3 tyrosine kinase inhibitor approved globally for advanced renal cell carcinoma. However, **this Evidence Pack contains no TxGNN-predicted new indications**, and the drug is **not marketed in Finland**, making a full repurposing evaluation impossible at this stage. The current data is insufficient to support any repurposing recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (global approval; not registered in Finland) |
| Predicted New Indication | No predictions available in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — TxGNN output absent |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indications were returned for Axitinib in this Evidence Pack (`predicted_indications: []`). As a result, the mechanistic linkage analysis between the original indication and any new indication cannot be performed.

Based on general pharmacological knowledge, Axitinib is a second-generation selective inhibitor of vascular endothelial growth factor receptors (VEGFR-1, VEGFR-2, VEGFR-3). Its anti-angiogenic mechanism is mechanistically applicable across multiple solid tumour types, and it has been studied in thyroid cancer, hepatocellular carcinoma, and non-small cell lung cancer beyond its approved renal cell carcinoma indication. However, **these observations are not supported by the current Evidence Pack** and cannot form the basis of a formal repurposing recommendation under this evaluation framework.

Detailed MOA data was flagged as a data gap (DG002) in the evidence pack and must be retrieved from DrugBank before mechanism-based analysis can proceed.

---

## Finland Market Information

Axitinib holds **no marketing authorizations in Finland** as of the data cutoff (2026-04-20). No license records are available.

---

## Cytotoxicity

Axitinib is an antineoplastic targeted therapy (VEGFR tyrosine kinase inhibitor). Although cytotoxicity data was not present in this Evidence Pack, the following applies based on its drug class:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective VEGFR tyrosine kinase inhibitor |
| Myelosuppression Risk | Low to moderate (less than conventional cytotoxics; thrombocytopenia and neutropenia reported) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure (hypertension is a class effect), CBC, liver function (ALT/AST), thyroid function, urine protein |
| Handling Protection | Follow institutional cytotoxic drug handling guidelines; oral formulation but classified as hazardous drug |

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) was available in this Evidence Pack. The TFDA package insert query returned a result (query log ID 4), but the content was not parsed into the evidence pack.

> Please refer to the Inlyta (axitinib) Summary of Product Characteristics (SmPC) and local package insert for full safety information, including warnings on hypertension, arterial and venous thromboembolism, haemorrhage, hepatotoxicity, and wound healing complications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Axitinib is structurally incomplete — no TxGNN predictions, no Finland market authorization, no parsed safety data, and no MOA data — making it impossible to perform a repurposing evaluation under the current framework.

**To proceed, the following is needed:**

- **[Critical — DG001]** Parse the TFDA/Fimea package insert PDF to extract key warnings and contraindications; required before any safety review can begin
- **[High — DG002]** Retrieve MOA data from DrugBank API to enable mechanism-based repurposing analysis
- **[Critical]** Investigate why TxGNN returned zero predicted indications for DB06626 — check whether the DrugBank ID is correctly mapped to the knowledge graph node, and re-run prediction pipeline
- **[Required]** Verify Finland (Fimea) registration status independently; if Axitinib is sold under a different brand or via parallel import, licenses may exist under alternate identifiers
- Once TxGNN predictions are available, re-generate this Evidence Pack (v5+) to enable full L1–L5 evidence assessment
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

