---
layout: default
title: Reteplase
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
---

# Reteplase
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

Using the report structure directly (this is a document-generation task with a fully specified template — no additional skill applies).

# Reteplase: From Acute Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Reteplase is a recombinant thrombolytic (plasminogen activator) originally used to restore coronary blood flow in acute myocardial infarction. The TxGNN model's top prediction is **Posteroinferior Myocardial Infarction**, but this is currently supported by **0 clinical trials** and **0 publications** — the score reflects mechanistic overlap with reteplase's existing thrombolytic use, not new clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myocardial infarction (thrombolytic reperfusion therapy) — not separately documented in the Finland regulatory record, since reteplase is not currently marketed there |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (per source scoring); by raw trial/literature count this candidate has zero supporting studies, which would place it at L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A structured mechanism-of-action record is not available for reteplase in this evidence pack. Based on information surfaced elsewhere in the pack, reteplase is a second-generation recombinant tissue-type plasminogen activator (r-PA, compound BM 06.022) that catalyzes conversion of plasminogen to plasmin, dissolving coronary thrombi and restoring perfusion in occluded coronary arteries. This mechanism is the pharmacological basis for its established use in acute myocardial infarction.

"Posteroinferior myocardial infarction" is not a distinct disease — it is an anatomical subtype of acute MI, describing the location of the infarcted myocardium rather than a different pathology. Since reteplase's thrombolytic action restores flow in the infarct-related artery regardless of anatomical territory, it is mechanistically plausible that the drug would work here too — in fact, this subtype likely already falls within reteplase's existing AMI indication rather than representing a genuinely new use.

This is precisely why the evidence pack itself flags the prediction as weak: no clinical trial or publication in this dataset specifically studies posteroinferior MI as a distinct population, so the high TxGNN score is driven by mechanistic/anatomical proximity in the knowledge graph rather than by direct clinical validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Reteplase currently holds no marketing authorization in Finland (0 licenses on record; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. Note that a **blocking data gap** exists: the Fimea/label warnings and contraindications for reteplase have not yet been retrieved, which currently prevents a formal initial safety screening (S1) for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (posteroinferior MI) has no direct clinical trial or literature support and largely overlaps with reteplase's existing general AMI indication rather than representing a novel repurposing opportunity. A blocking safety data gap (regulatory label/warnings) also prevents initial safety screening.

**To proceed, the following is needed:**
- Fimea/TFDA package insert (warnings, contraindications) — currently a blocking gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Clarification on whether "posteroinferior MI" should be evaluated as a distinct repurposing candidate or folded into reteplase's existing AMI indication

**Note on a stronger alternate candidate:** among the 10 predictions in this evidence pack, **coronary stenosis** (rank 5, TxGNN score 99.62%) has materially stronger support — evidence level L3, decision stage S2, 6 literature references (including RCT/cohort data such as the SPEED/GUSTO-4 trial and GUSTO-V outcomes analysis), and a source recommendation of "Proceed with Guardrails." This candidate may warrant prioritization over the top-ranked but evidence-poor posteroinferior MI prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

