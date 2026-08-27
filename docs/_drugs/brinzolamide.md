---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 1
---

# Brinzolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Brinzolamide: From Elevated Intraocular Pressure to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a topical carbonic anhydrase (CA-II) inhibitor pharmacologically used to lower intraocular pressure (IOP) in glaucoma-spectrum conditions.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
but this prediction is currently **model-only**, with **0 clinical trials** and **0 publications** supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on record (no approved licenses in dataset); based on known pharmacology, used to reduce intraocular pressure in ocular hypertension/glaucoma |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% (rank 5640) |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is formally marked as a data gap in this record. However, the underlying repurposing rationale identifies brinzolamide as a topical carbonic anhydrase (CA-II) inhibitor: it inhibits carbonic anhydrase in the ciliary body epithelium, reducing aqueous humor production and thereby lowering intraocular pressure (IOP).

Primary hereditary glaucoma and the conditions brinzolamide is pharmacologically associated with (ocular hypertension and open-angle glaucoma) share the same core pathological feature — elevated IOP. This gives the TxGNN prediction a plausible mechanistic basis: any glaucoma subtype driven by elevated IOP, including hereditary/congenital forms, is theoretically responsive to aqueous humor suppression.

That said, mechanistic plausibility alone does not establish clinical evidence. Primary hereditary glaucoma often presents in pediatric or congenital contexts with distinct pathophysiology (e.g., anatomical outflow abnormalities), efficacy, dosing, and safety profile (including systemic absorption risk in children) that cannot be assumed from adult ocular hypertension data. No clinical trials or literature specific to this indication currently exist to confirm the link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Brinzolamide currently holds no marketing authorization in Finland (0 licenses on record); market status is "not marketed."

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert warnings and contraindications, and drug interaction data, are flagged as a Blocking data gap (DG001) — this must be resolved before any S1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on mechanistic plausibility alone (L5, model-only), with no clinical trials, literature, or safety data (package insert) available for primary hereditary glaucoma specifically. A Blocking data gap on TFDA/Fimea package insert safety information (DG001) also prevents any S1 safety evaluation at this stage.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) to resolve Blocking gap DG001
- Confirmed mechanism of action documentation from DrugBank (High-priority gap DG002)
- Preclinical or clinical evidence specific to primary hereditary glaucoma, particularly in pediatric/congenital populations
- Drug-drug interaction data
- Route/dosage-form compatibility assessment for the ophthalmic route in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

