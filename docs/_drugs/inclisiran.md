---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From Unspecified Original Indication to Potassium Deficiency Disease

## One-Sentence Summary

Inclisiran's original approved indication and formal mechanism-of-action are not documented in this evidence pack (flagged as blocking/high-severity data gaps). The TxGNN model's top prediction is **Potassium Deficiency Disease**, but this is a pure model artifact — **0 clinical trials** and **0 publications** support it, and the model itself flags no known mechanistic link between the drug's pathway and potassium homeostasis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty in this evidence pack |
| Predicted New Indication | Potassium Deficiency Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data at the drug-profile level is marked as a data gap (DG002, High severity). However, the evidence pack's own per-indication rationale text (attached to the rank-8 "aortic malformation" entry) describes Inclisiran as a small interfering RNA (siRNA) that targets PCSK9 mRNA in the liver, blocking PCSK9 synthesis and increasing hepatic LDL-receptor recycling to lower LDL-cholesterol — i.e., a lipid-metabolism pathway drug, consistent with the two real trials surfaced in that entry (NCT06597006, NCT06597019), which actually study pediatric familial hypercholesterolemia rather than the labeled disease.

For the top-ranked prediction, Potassium Deficiency Disease, the evidence pack explicitly states there is no known mechanistic connection between the PCSK9/LDL pathway and potassium homeostasis. The 99.93% score is a high-confidence output of the graph model but is not backed by any trial, case report, or mechanistic literature — a pattern consistent with a scoring artifact rather than a biologically grounded hypothesis.

This pattern repeats across all ten ranked predictions: none have literature or trials that directly and validly connect Inclisiran to the predicted disease. Rank 8 ("aortic malformation") returned two trial hits, but the evidence pack's own verification found these to be ontology-mapping errors (the trials study HoFH/HeFH, not aortic malformation). Rank 7 ("migraine with or without aura, susceptibility to") returned 20 PubMed hits, but all concern epilepsy/migraine shared genetics (e.g., SCN1A, MTHFR) with no mention of Inclisiran, PCSK9, or lipid pathways.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-ranked predictions sit at Evidence Level L5 (model score only). The top prediction has an explicitly acknowledged absence of mechanistic plausibility, and the one place real trial data appeared elsewhere in the list (rank 8) turned out to be a disease-label mapping error unrelated to the predicted condition. There is no basis to advance any candidate past S0.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (DG001, Blocking) — required before any S1 safety screening
- Confirmed original indication and MOA from DrugBank (DG002)
- Disease-specific trial or literature evidence for any of the ranked predictions, obtained through corrected disease-ontology mapping (the aortic-malformation mismatch suggests other labels in this batch may also be mismapped)
- Re-run TxGNN evidence retrieval once ontology mapping is validated, before re-evaluating any candidate in this set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

