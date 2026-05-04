---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# ABATACEPT: Drug Repurposing Evaluation Report

## One-Sentence Summary

Abatacept (DrugBank: DB01281) is a biologic agent known internationally for immune modulation, but it currently has **no marketing authorization in Taiwan** and **no original indication data** in this evidence pack. The TxGNN model has **not generated any predicted new indications** for this drug, and critical data gaps remain in mechanism of action and safety information.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | ABATACEPT |
| DrugBank ID | DB01281 |
| Original Indication | No data available (no Taiwan licenses) |
| Predicted New Indication | None (no TxGNN predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; no predictions generated |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Abatacept is widely recognized internationally as a selective T-cell co-stimulation modulator (CTLA-4-Ig fusion protein) that inhibits T-cell activation by binding to CD80/CD86 on antigen-presenting cells. It is approved in many countries for rheumatoid arthritis, juvenile idiopathic arthritis, and psoriatic arthritis; however, none of this information is captured in the current Taiwan regulatory dataset.

Since the TxGNN model has not generated any predicted indications for Abatacept, there is no mechanistic bridging analysis to perform at this time. The absence of predictions may be due to insufficient representation of Abatacept in the knowledge graph, or it may indicate that the model did not identify high-confidence repurposing candidates above its scoring threshold.

## Clinical Trial Evidence

Currently no related clinical trials to report, as no new indications have been predicted by the TxGNN model.

## Literature Evidence

Currently no related literature to report, as no new indications have been predicted by the TxGNN model.

## Taiwan Market Information

Abatacept currently holds **no marketing authorization (許可證)** in Taiwan. No license records were returned from the TFDA query (queried 2026-03-29).

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, drug-drug interactions) returned as data gaps in this evidence pack. The DDI query returned no results. Complete safety data should be obtained from international sources (e.g., FDA label, EMA SmPC) or the DrugBank full profile before any clinical evaluation proceeds.

## Data Gaps Summary

The following critical data gaps were identified and must be resolved before advancing this candidate:

| Gap ID | Category | Item | Severity | Remediation |
|--------|----------|------|----------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Query DrugBank API for detailed MOA |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Abatacept has no TxGNN-predicted new indications in the current analysis, no Taiwan marketing authorization, and multiple blocking data gaps. There is insufficient evidence to justify advancing this candidate through the repurposing pipeline at this time.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: Obtain TFDA package insert warnings and contraindications, or equivalent safety data from international regulatory sources (FDA/EMA)
- Resolve **DG002 (High)**: Retrieve detailed mechanism of action from DrugBank API to enable knowledge graph enrichment
- Re-run TxGNN prediction after knowledge graph is updated with complete Abatacept pharmacological data
- If international indications (e.g., rheumatoid arthritis, JIA, psoriatic arthritis) are confirmed, populate `original_indications` and re-evaluate for repurposing opportunities
- Confirm whether Abatacept's absence from the Taiwan market is a regulatory gap or a strategic decision, as this affects the feasibility of any repurposing pathway in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

