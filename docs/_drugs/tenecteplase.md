---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From Acute STEMI to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Tenecteplase (DB00031) is an established fibrin-specific thrombolytic used for acute ST-elevation myocardial infarction (STEMI). The TxGNN model's top prediction is efficacy in **Posteroinferior Myocardial Infarction**, an anatomical STEMI subtype, but this specific candidate currently has **0 clinical trials** and **0 dedicated publications** — the supporting evidence is indirect, extrapolated from tenecteplase's already-proven STEMI mechanism rather than subtype-specific data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute ST-elevation myocardial infarction (STEMI) — thrombolytic therapy *(inferred from repurposing rationale; not separately captured in this evidence pack — see Data Gap DG002)* |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Finland/Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, tenecteplase is a recombinant, fibrin-specific tissue plasminogen activator (tPA variant) belonging to the thrombolytic/fibrinolytic drug class; its efficacy in acute STEMI thrombolysis is well established, and mechanistically this action may extend to anatomical subtypes of the same disease process.

Posteroinferior myocardial infarction is not a distinct disease but an anatomical location descriptor of STEMI. The underlying pathology — acute coronary thrombotic occlusion — is identical to the drug's original indication, so the biological rationale for repurposing is strong. However, no clinical trial or literature record in this evidence pack specifically evaluates tenecteplase in posteroinferior (or posterolateral, rank 2) MI; both share the same TxGNN score (99.87%) and are best read as the model recognizing "STEMI" broadly rather than subtype-specific efficacy signals.

Within this same candidate set, two other predictions are worth noting for context: septal myocardial infarction (rank 3) has literature, but it concerns pulmonary embolism cases misdiagnosed as septal MI rather than direct efficacy data; and coronary stenosis (rank 5) has meaningfully stronger evidence — a completed Phase 2 RCT plus supporting cohort literature on low-dose intracoronary tenecteplase as PCI adjunct therapy — making it a more mature candidate than the top-ranked prediction reviewed here.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Tenecteplase is not currently marketed in Taiwan; there are no approved product licenses on record (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link to posteroinferior MI is biologically plausible (same STEMI pathology, established thrombolytic mechanism), but no subtype-specific clinical trial or literature evidence exists in this evidence pack — this is a hypothesis-generating signal, not an actionable indication.

**To proceed, the following is needed:**
- Subtype-specific clinical or observational data for posteroinferior MI (not just general STEMI evidence)
- TFDA package insert / warnings and contraindications data (Data Gap DG001, currently Blocking)
- Confirmed mechanism of action detail from DrugBank (Data Gap DG002)
- Consider prioritizing **coronary stenosis** (rank 5) instead — it already has a completed Phase 2 RCT (NCT00604695) and supporting cohort literature, placing it at a more advanced evidence stage (L2/S2) than this top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

