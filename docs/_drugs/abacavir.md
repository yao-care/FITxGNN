---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# ABACAVIR: Antiretroviral Agent — Drug Repurposing Evaluation

## One-Sentence Summary

Abacavir is a nucleoside analogue reverse transcriptase inhibitor (NRTI) used in the treatment of HIV infection. The TxGNN model has **not generated any predicted new indications** for this drug at the current data cutoff, and **no clinical trials or literature** supporting repurposing directions are available in this evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection (known from drug class; no Taiwan label available) |
| Predicted New Indication | — None predicted |
| TxGNN Prediction Score | — N/A |
| Evidence Level | L5 (No predictions or supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

There is currently **no TxGNN prediction** available for Abacavir. The model did not return any candidate new indications, so a mechanistic plausibility assessment cannot be performed at this time.

For reference, Abacavir is a carbocyclic synthetic nucleoside analogue. It is intracellularly converted to its active metabolite, carbovir triphosphate (CBV-TP), which competitively inhibits HIV-1 reverse transcriptase and terminates viral DNA chain elongation. However, detailed mechanism of action data was not included in this evidence pack (marked as a data gap).

Without a predicted indication, there is no basis to evaluate whether Abacavir's mechanism could be leveraged for a novel therapeutic use.

## Clinical Trial Evidence

Currently no related clinical trials registered for any repurposing indication.

## Literature Evidence

Currently no related literature available for any repurposing indication.

## Taiwan Market Information

Abacavir currently holds **no marketing authorizations** in Taiwan (TFDA). No licensed products were identified during the query (2026-03-29).

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack. These represent **blocking data gaps** that must be resolved before any safety evaluation can proceed.

## Data Gaps Identified

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Impacts mechanistic relevance analysis | Query DrugBank API |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has not generated any predicted new indications for Abacavir. Combined with the absence of Taiwan marketing authorization, missing safety data (blocking-level gap), and no supporting clinical or literature evidence, there is insufficient basis to advance this candidate through the repurposing pipeline.

**To proceed, the following is needed:**
- Re-run TxGNN prediction pipeline to confirm absence of candidate indications (or update to a newer model version)
- Resolve DG001: Obtain TFDA package insert warnings and contraindications (blocking for safety assessment)
- Resolve DG002: Retrieve detailed mechanism of action data from DrugBank API
- If a future prediction is generated, gather clinical trial and literature evidence for the predicted indication
- Assess Taiwan regulatory pathway feasibility given the drug's current unlicensed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

