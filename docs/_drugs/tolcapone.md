---
layout: default
title: Tolcapone
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Tolcapone is a COMT (catechol-O-methyltransferase) inhibitor originally developed as an adjunct therapy to levodopa/carbidopa in Parkinson's disease. The TxGNN model's top-ranked prediction for this drug is **Rasmussen Subacute Encephalitis** (score 99.93%), but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack explicitly notes no known mechanistic relationship between COMT inhibition and this disease's autoimmune pathology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, adjunct to levodopa/carbidopa (based on known drug class; not present in this evidence pack's Taiwan regulatory data) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.93% (rank 1033 in full prediction list) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacological class information, tolcapone is a peripheral and central COMT inhibitor that reduces the metabolic breakdown of levodopa and dopamine, and its efficacy as adjunct therapy in Parkinson's disease is well established.

For the top-ranked predicted indication, Rasmussen subacute encephalitis, the evidence pack's own mechanistic assessment is negative: this is an autoimmune encephalitis with intractable epilepsy, driven by T-cell-mediated neuronal destruction, and there is no known link to COMT inhibition or catecholamine metabolism. No clinical trials, ICTRP records, or PubMed literature were found connecting tolcapone to this disease. This prediction should be treated as a network-topology signal from the TxGNN model only, not as a mechanistically grounded hypothesis.

It is worth noting that other candidates in this evidence pack carry stronger rationale even though ranked lower by score: **Lewy body dementia** (rank 6) has supporting preclinical/mechanistic literature on catecholamine-metabolite-driven α-synuclein pathology, and **juvenile parkinsonism (paralysis agitans, juvenile, of Hunt)** (rank 10) is mechanistically direct, since tolcapone's drug class is already used in classic parkinsonism. Neither reached the primary index position (rank 1) used for this report's structured fields, but both warrant separate, prioritized evaluation (see Next Steps).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA package insert warnings/contraindications for tolcapone were not retrievable in this data pull and are flagged as a Blocking data gap (DG001) — this prevents a formal S1 safety pre-assessment. Tolcapone carries well-known hepatotoxicity concerns in its approved indication that should be independently verified against the official label before any further evaluation.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen subacute encephalitis) has no clinical, literature, or mechanistic support beyond the raw TxGNN score, and mandatory safety data (TFDA label warnings/contraindications) is missing and blocking, so this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action data from DrugBank — currently High priority gap (DG002)
- If pursuing this drug further, re-scope the evaluation toward better-evidenced candidates in the same prediction set — specifically Lewy body dementia (rank 6, L4, S1 "Research Question") and juvenile parkinsonism (rank 10, S1 "Research Question") — rather than the top-scored but mechanistically unsupported rank 1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

