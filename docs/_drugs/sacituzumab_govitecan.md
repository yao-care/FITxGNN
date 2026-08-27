---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
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

# Sacituzumab Govitecan: From [Original Indication Not Available] to Drug-Induced Osteoporosis

## One-Sentence Summary

Sacituzumab Govitecan (DB12893) is a Trop-2–targeted antibody-drug conjugate that delivers SN-38 (a topoisomerase I inhibitor and the active metabolite of irinotecan) as systemic cytotoxic chemotherapy; its original indication is not recorded in the current data pack (data gap). TxGNN predicts it may be effective for **drug-induced osteoporosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags the causal direction as likely reversed — cytotoxic chemotherapy is a known cause of bone-density loss, not a treatment for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication text on file (data gap) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (marked as a data gap). Based on the mechanistic rationale included in this evidence pack, Sacituzumab Govitecan is a Trop-2–directed antibody-drug conjugate (ADC) that releases SN-38 intracellularly — a topoisomerase I inhibitor and the active metabolite of irinotecan — functioning as systemic cytotoxic chemotherapy.

There is no known mechanistic pathway by which this cytotoxic payload would *treat* osteoporosis. To the contrary, systemic cytotoxic chemotherapy is a recognized cause of bone-density loss through myelosuppression and secondary gonadal dysfunction. The evidence pack's own analysis concludes that the causal direction implied by this TxGNN prediction is likely inverted — the drug is more plausibly a risk factor for drug-induced osteoporosis than a candidate treatment for it.

Notably, the next three ranked predictions (severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract) follow the same unusual pattern: high TxGNN scores (99.1–99.7%), zero supporting trials or literature, and no plausible mechanistic link to an anti-tumour ADC payload. Combined with the fact that this drug's `original_indications` list and DDI records are both empty, this cluster of predictions is more consistent with a data-sparsity artifact ("cold-start" node in the knowledge graph) than genuine repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Sacituzumab Govitecan is an antineoplastic ADC (Trop-2-targeted delivery of the cytotoxic topoisomerase I inhibitor SN-38), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ADC) delivering a conventional cytotoxic payload (SN-38, topoisomerase I inhibitor) |
| Myelosuppression Risk | Flagged in the evidence pack's mechanistic rationale as an expected class effect of SN-38-based cytotoxic therapy (bone marrow suppression, secondary gonadal dysfunction); no formal toxicity database entry on file — please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a cytotoxic ADC payload, standard cytotoxic drug handling precautions likely apply; confirm via package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications (drug-induced osteoporosis, severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract) sit at L5/S0 with zero clinical trials or literature, and the mechanistic review in this evidence pack indicates the top prediction likely reflects reversed causality rather than a genuine therapeutic signal — this pattern, together with empty original-indication and DDI records, points to knowledge-graph data sparsity rather than a real repurposing opportunity.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action via DrugBank API — currently high priority (DG002)
- Enrichment of the drug's original-indication and DDI records to resolve the apparent knowledge-graph data gap before re-evaluating any TxGNN prediction for this compound
- Independent mechanistic or preclinical evidence for each predicted indication before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

