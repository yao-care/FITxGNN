---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Pulmonary Arterial Hypertension (Inferred) to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept is an ActRIIA-Fc ligand-trap biologic whose clinical development has centred on pulmonary arterial hypertension; its original indication and mechanism of action are not yet documented in this evidence pack. The TxGNN model's top-ranked new-indication prediction is **Acute Lymphoblastic Leukemia** (score 99.78%), but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale states no known biological link exists between the drug's pathway and ALL pathogenesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (contextual notes reference pulmonary arterial hypertension; not confirmed via formal license data) |
| Predicted New Indication | Acute Lymphoblastic Leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for sotatercept is not available in this evidence pack (Data Gap DG002, High severity). Based on the mechanistic notes embedded in the underlying evidence records, sotatercept is understood to be an ActRIIA-Fc fusion protein acting as a ligand trap for activin A/B and GDF8/GDF11, inhibiting SMAD2/3 signalling — the same biology it shares with its sister molecule luspatercept. Its clinical development context, as referenced in these records, centres on pulmonary arterial hypertension (PAH), where it is thought to rebalance TGF-β superfamily proliferative/anti-proliferative signalling to reduce vascular remodelling.

For the top-ranked prediction, acute lymphoblastic leukaemia, the model's own repurposing rationale explicitly states there is **no known mechanistic link**: activin/GDF signalling has a role in haematopoietic stem cell differentiation, but no established connection to the oncogenic drivers of ALL (chromosomal translocations, tyrosine kinase activation). No clinical trials, ICTRP records, or PubMed literature support this pairing (0/0/0 hits across all queries). This should be read as a similarity signal from TxGNN's embedding space rather than a biologically grounded hypothesis.

Notably, among the ten TxGNN predictions returned, rank 4 (drug-induced osteoporosis, score 99.65%) carries materially stronger mechanistic plausibility: activin/GDF trapping is known to increase osteoblast activity and suppress osteoclast activity, an effect already documented for luspatercept and the earlier ACE-011 development programme. That prediction is internally flagged as a "Research Question" rather than "Hold" and may merit independent literature follow-up, even though it too currently lacks direct trial or publication evidence. Ranks 6–10 (HER2+ breast carcinoma and a cluster of urothelial carcinomas) show tightly clustered scores with no mechanistic rationale, consistent with a TxGNN disease-embedding cluster artifact rather than a real signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Sotatercept is not currently marketed in Finland; no marketing authorizations are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/Fimea package insert warnings and contraindications are marked as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety pre-assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acute lymphoblastic leukemia) is an L5, model-score-only signal with zero clinical, trial-registry, or literature support, and the evidence pack's own mechanistic analysis finds no plausible biological link. Basic drug-level data (MOA, original indication, safety/label information) are also unresolved, one of which is a Blocking gap.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA/Fimea package insert for warnings and contraindications
- Resolve DG002: confirm mechanism of action via DrugBank API
- Confirm the drug's actual original/approved indication(s), which are currently empty in this dataset
- If pursuing further, redirect research priority toward rank 4 (drug-induced osteoporosis), the only candidate with a defensible mechanistic rationale, rather than the top-scored but mechanistically unsupported ALL prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

