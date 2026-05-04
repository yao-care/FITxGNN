---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase Alfa: Evaluation Pending — Insufficient Evidence Pack Data

## One-Sentence Summary

Asfotase alfa is a recombinant tissue-nonspecific alkaline phosphatase (TNSALP) enzyme replacement therapy, approved internationally for hypophosphatasia (HPP) — a rare, life-threatening inherited metabolic bone disorder.
The current Evidence Pack contains **no TxGNN-predicted repurposing indications**, and two critical data gaps (mechanism of action and safety warnings) remain unresolved.
A full repurposing evaluation **cannot proceed** until these gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypophosphatasia (HPP) — perinatal/infantile/juvenile-onset (international approval; absent from Taiwan regulatory records) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | N/A — no TxGNN predictions present |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Are No Predictions Available?

Asfotase alfa is a large-molecule recombinant enzyme replacement therapy — a class that differs substantially from the small-molecule drugs on which TxGNN knowledge graph embeddings are primarily trained.

Three factors likely explain the absence of predictions:

1. **Biologic / ERT class**: Enzyme replacement therapies act by directly replenishing a deficient endogenous enzyme (TNSALP). Their mechanism is substrate-specific, leaving limited scope for cross-indication repurposing compared to receptor-targeting small molecules. The TxGNN model may not have sufficient graph edges for this compound to generate repurposing hypotheses.

2. **Ultra-rare disease signal**: HPP has an estimated prevalence of approximately 1 in 300,000. Knowledge graph training data for this drug is sparse, reducing the model's ability to infer novel indication links through disease-disease or gene-disease co-occurrence pathways.

3. **MOA data gap**: The Evidence Pack carries no mechanism of action entry for DB09105 (flagged as DG002, severity: High). Without an MOA node in the knowledge graph, mechanistic similarity analysis cannot be performed, and the repurposing engine has no anchor from which to project candidate indications.

Until TxGNN returns prediction candidates for this compound, no repurposing recommendation can be made.

---

## Taiwan Market Information

Asfotase alfa is **not currently approved or marketed in Taiwan**.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No authorizations on record |

---

## Safety Considerations

Please refer to the package insert for safety information.

All safety fields in the current Evidence Pack are unresolved data gaps: key warnings (DG001, severity: Blocking), contraindications (DG001, severity: Blocking), and drug interaction data are unavailable. No safety assessment can be performed at this stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for asfotase alfa is critically incomplete — no TxGNN predictions, no Taiwan regulatory records, and no usable safety data are present. The compound cannot be evaluated for repurposing potential until the blocking data gaps are resolved.

**To proceed, the following is needed:**

- **Confirm TxGNN pipeline coverage**: Verify whether DB09105 was included in the prediction run. Biologics and enzyme replacement therapies may require a dedicated graph augmentation step or exclusion flag to be documented.
- **Retrieve MOA from DrugBank** (DG002): Query DrugBank API for the mechanism of action entry for DB09105. This is required for all downstream mechanistic analysis.
- **Parse Taiwan package insert from TFDA** (DG001, Blocking): Download and extract the 仿單 PDF to obtain official warnings, contraindications, and precautions before any clinical safety evaluation.
- **Verify international approval status**: Asfotase alfa holds FDA and EMA approvals for HPP. Confirm whether Finland's Fimea has granted equivalent authorization, as this would establish a baseline regulatory precedent for any new indication filing.
- **Assess rare disease framework applicability**: HPP carries orphan drug designation in multiple jurisdictions. Any repurposing candidate should be assessed within the rare disease regulatory pathway, which may affect evidence thresholds and approval timelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

