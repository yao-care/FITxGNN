---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma to Pregerminal Center CLL/SLL

## One-Sentence Summary

Ofatumumab is a fully human anti-CD20 monoclonal antibody originally approved (as Arzerra) for chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL). The TxGNN model's top-ranked prediction points to **pregerminal center CLL/SLL** — a specific IGHV-unmutated molecular subtype of the same disease — with a prediction score of **99.77%**, but currently **0 clinical trials** and **0 publications** directly support this subtype-specific extrapolation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic lymphocytic leukemia (CLL) / small lymphocytic lymphoma (SLL) — the drug's original core indication (as Arzerra); no formal Finland license text is available in current data |
| Predicted New Indication | Pregerminal center CLL/SLL (IGHV-unmutated molecular subtype) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ofatumumab is a fully human IgG1κ monoclonal antibody targeting CD20, in the same drug class as rituximab and obinutuzumab. Its efficacy in chronic lymphocytic leukemia/small lymphocytic lymphoma has been proven and forms its original approved indication.

"Pregerminal center CLL/SLL" is not a distinct disease but a molecular subtype of CLL/SLL, characterized by an unmutated IGHV gene status (pre-germinal center origin), which is typically associated with a more aggressive clinical course. Tumor cells in this subtype continue to express CD20, so ofatumumab's core cytotoxic mechanism — complement-dependent cytotoxicity (CDC) and antibody-dependent cell-mediated cytotoxicity (ADCC) against CD20+ B cells — remains mechanistically applicable.

However, this prediction is an **indirect extrapolation** from the drug's main CLL/SLL evidence base rather than a subtype-specific finding: no clinical trial or publication in this evidence pack specifically enrolled or analyzed IGHV-unmutated/pre-germinal center CLL/SLL patients as a defined subgroup for ofatumumab treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Ofatumumab is an antineoplastic biologic (anti-CD20 monoclonal antibody used in CD20+ B-cell malignancies including CLL/SLL and follicular lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD20 monoclonal antibody), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Literature (PMID [26566719](https://pubmed.ncbi.nlm.nih.gov/26566719/)) describes a "favorable toxicity profile" in CLL patients, but no quantified hematologic toxicity data is available in the current dataset |
| Emetogenicity Classification | Low (monoclonal antibodies are generally minimally emetogenic; infusion-related reactions are the more prominent acute toxicity for this class) |
| Monitoring Items | CBC with differential, infusion-related reaction monitoring, hepatitis B screening (class recommendation for anti-CD20 agents), immunoglobulin levels |
| Handling Protection | Standard biologic infusion handling precautions; not subject to cytotoxic chemotherapy handling regulations, as it is a monoclonal antibody rather than a cytotoxic small molecule |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this specific molecular subtype is high, but it is supported by zero direct clinical trials or publications — the mechanistic rationale is entirely extrapolated from ofatumumab's broader CLL/SLL evidence base rather than subtype-specific data. This does not meet the bar to advance beyond S1 (Research Question).

**To proceed, the following is needed:**
- Subtype-specific clinical trial or literature evidence for IGHV-unmutated/pre-germinal center CLL/SLL
- TFDA/Fimea package insert warnings and contraindications (currently a Blocking data gap, DG001) — required before any S1 safety screening
- Confirmed mechanism-of-action data from DrugBank (High-severity data gap, DG002)
- Finland regulatory/market status update, given the drug is currently not marketed there

**Note for context:** within this same evidence pack, other TxGNN-predicted indications for ofatumumab carry substantially stronger evidence — chronic lymphocytic leukemia/small lymphocytic lymphoma overall (rank 5, L1, "Proceed with Guardrails," including completed Phase 3 trials) and follicular lymphoma (rank 3, L2, multiple completed Phase 2/3 trials). Those candidates may warrant separate, higher-priority evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

