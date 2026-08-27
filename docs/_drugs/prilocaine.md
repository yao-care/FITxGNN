---
layout: default
title: Prilocaine
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaine: From Local Anesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Prilocaine is an amide-type local anesthetic (best known as a component of EMLA cream, used together with lidocaine for topical/regional analgesia). The TxGNN model's top-ranked prediction for this drug is **Papillary Conjunctivitis**, but currently **0 clinical trials** and **0 publications** support this specific link — the prediction is model-score only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Finland; no approved indication text on file. Known use (per literature in this evidence pack) is topical/regional local anesthesia. |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for prilocaine is not available in this evidence pack. Based on known information, prilocaine is a sodium-channel-blocking amide local anesthetic (frequently combined with lidocaine in EMLA cream), and its efficacy for producing local/topical analgesia is well established across the literature captured for this drug's other candidate indications.

Papillary conjunctivitis, however, is a hypersensitivity/mechanical-irritation condition of the conjunctiva, driven by allergic or foreign-body inflammatory pathways — not by nociceptive nerve conduction. No mechanistic pathway currently links sodium-channel blockade to this disease process.

The evidence pack's own analysis is explicit on this point: no clinical trials or publications connect prilocaine to papillary conjunctivitis, and the reviewers judged there to be no plausible mechanistic overlap. The high TxGNN score therefore reflects the model's embedding-space output alone, not any corroborating biological or clinical rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.78%), there is no clinical trial, literature, or mechanistic evidence connecting prilocaine to papillary conjunctivitis, and the underlying disease pathology does not align with the drug's known pharmacology. This candidate does not currently meet the bar for further investment.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action (MOA) data for prilocaine
- Preclinical or in-vitro rationale specifically linking local anesthetic activity to conjunctival hypersensitivity pathways
- TFDA/Fimea package insert data (warnings, contraindications) — currently a blocking data gap
- Consider redirecting evaluation effort toward this drug's better-evidenced candidates in the same evidence pack — notably **neuralgia** (L2, 12 trials, 20 publications, "Proceed with Guardrails") and **migraine disorder** (L3, 4 trials, "Research Question") — which have substantially stronger mechanistic and clinical support than papillary conjunctivitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

