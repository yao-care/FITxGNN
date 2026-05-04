---
layout: default
title: Abaloparatide
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 4
---

# Abaloparatide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# ABALOPARATIDE: Drug Repurposing Evaluation Report

## One-Sentence Summary

Abaloparatide (DrugBank: DB05084) is a synthetic peptide analog of parathyroid hormone-related protein (PTHrP), known internationally for the treatment of osteoporosis in postmenopausal women at high risk of fracture. Currently, **no new indications have been predicted by the TxGNN model**, and the drug is **not marketed in Taiwan** with **zero active licenses**. Insufficient data is available to support a repurposing assessment at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Abaloparatide |
| DrugBank ID | DB05084 |
| Original Indication | Not recorded in Taiwan (no TFDA licenses found) |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — Model prediction not yet generated |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, Abaloparatide is a synthetic analog of human parathyroid hormone-related protein (PTHrP(1-34)). It acts as a selective activator of the PTH1 receptor signaling pathway, preferentially stimulating the RG conformation of the receptor, which promotes bone formation over bone resorption. It was approved by the U.S. FDA in 2017 under the brand name **Tymlos** for the treatment of postmenopausal osteoporosis in women at high risk of fracture.

However, as the TxGNN model has **not generated any predicted indications** for Abaloparatide, there is currently no new disease target to evaluate for mechanistic plausibility. This may be due to limited representation of the drug or its targets within the knowledge graph used by TxGNN. Until predictions become available, no mechanistic bridging analysis can be performed.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indications exist for Abaloparatide, therefore no targeted clinical trial search was conducted for repurposing candidates.

---

## Literature Evidence

Currently no TxGNN-predicted indications exist for Abaloparatide, therefore no targeted literature search was conducted for repurposing candidates.

---

## Taiwan Market Information

Abaloparatide has **no active TFDA licenses** in Taiwan. The drug is currently classified as **not marketed (未上市)** in this jurisdiction.

| Item | Status |
|------|------|
| TFDA Licenses | None found |
| Market Status | Not marketed |
| Dosage Forms Available | None in Taiwan |

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> TFDA package insert warnings, contraindications, and drug-drug interaction data were not available for Abaloparatide in Taiwan. No drug-drug interactions were found in the queried databases. For prescribing information, consult the originator's labeling (e.g., U.S. FDA-approved Tymlos prescribing information).

---

## Data Gaps

The following critical data gaps were identified during evidence pack assembly:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter Stage 1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Impacts mechanism-relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Abaloparatide currently has no TxGNN-predicted new indications, is not marketed in Taiwan (zero TFDA licenses), and has multiple blocking-level data gaps (package insert warnings, MOA). There is insufficient evidence to proceed with any repurposing evaluation at this time.

**To proceed, the following is needed:**
- **TxGNN prediction results** — Re-run the model or verify that the drug and its target nodes are properly represented in the knowledge graph
- **Mechanism of action data** (DG002) — Query DrugBank API to retrieve full MOA and target information for Abaloparatide
- **TFDA regulatory pathway assessment** — Determine if Abaloparatide is under review or if an import pathway exists for Taiwan
- **Safety profile completion** (DG001) — Obtain warnings and contraindications from the originator's prescribing information (e.g., U.S. FDA label notes a boxed warning regarding osteosarcoma risk observed in animal studies)
- **Re-evaluate** once TxGNN predictions and data gaps are resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

