---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

Using no additional skill — this is a direct document-generation task following the fully-specified template already provided in the prompt; I'll produce the report directly per the Evidence Pack.

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), a class of drugs whose established use is treating hypertension. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the signal rests on the model's mechanistic score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class; the drug is not marketed in Finland, so no approved-label indication text is available) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack (MOA field is a data gap). Based on known drug class information, irbesartan is an AT1 receptor antagonist (ARB) that inhibits the renin-angiotensin-aldosterone system (RAAS) to lower blood pressure — this is stated directly in the model's own repurposing rationale for this candidate.

The mechanistic logic connecting ARB pharmacology to malignant renovascular hypertension is genuinely double-edged, not a simple positive signal. On one hand, RAAS blockade is the standard pharmacological approach to severe hypertension. On the other, malignant renovascular hypertension frequently involves unilateral or bilateral renal artery stenosis, and ARBs dilate the efferent arteriole and reduce intraglomerular pressure — a well-known mechanism that can precipitate acute kidney injury specifically in bilateral renal artery stenosis. The same caveat applies to the closely related rank-2 candidate (malignant hypertensive renal disease), where renal function is often already compromised and ARB initiation requires close monitoring of creatinine and potassium.

The other two candidates in this pack (pulmonary hypertension due to lung disease/hypoxia, and pulmonary hypertension with unclear multifactorial mechanism — WHO Groups 3 and 5) are mechanistically weaker: these conditions are driven primarily by hypoxic pulmonary vasoconstriction and vascular remodeling rather than systemic RAAS activation, so ARB relevance is limited. Critically, the 20 literature records retrieved for the Group 3 candidate are all basic hypoxia biology, neurodegeneration, or oncology-hypoxia mechanism papers — none address irbesartan or ARBs in pulmonary hypertension, so they do not constitute supporting clinical evidence despite appearing in the search results.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other TxGNN-Predicted Indications (Ranks 2–4)

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|-----------------|------|
| 2 | Malignant hypertensive renal disease | 99.31% | L5 | Same mechanistic caveat as Rank 1 (pre-existing renal impairment); no trials or literature |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.25% | L5 | 20 literature hits, all unrelated hypoxia-biology/oncology papers — no ARB-specific clinical evidence |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.25% | L5 | No mechanistic pathway clearly linked to ARB activity; no trials or literature |

All four candidates are scored L5 (model prediction only) with a Hold recommendation at decision stage S0.

## Finland Market Information

Irbesartan currently has **no marketing authorization in Finland** (market status: Not marketed; 0 licenses on file). No approved indication text is available from this jurisdiction.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all unavailable in this Evidence Pack — the DDI query also returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No candidate indication in this pack has clinical trial or literature support, and the top-ranked candidate carries a known mechanistic risk (potential acute kidney injury in bilateral renal artery stenosis) rather than a clean positive signal. Compounding this, the missing TFDA/Fimea package-insert safety data (contraindications and warnings) is flagged as a **Blocking** gap that by itself prevents this candidate from entering S1 safety review.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (Blocking gap — required before any S1 safety evaluation)
- Detailed mechanism-of-action data to properly assess mechanistic fit for renal-hypertension indications
- Clinical or real-world evidence specifically evaluating ARB use in malignant renovascular hypertension / malignant hypertensive renal disease, including renal-artery-stenosis screening protocols
- Route and dosage-form compatibility data, since Finland has no existing marketing authorization to reference
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

