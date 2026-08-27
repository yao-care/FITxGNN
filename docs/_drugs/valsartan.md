---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker (ARB), originally used to treat hypertension. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but this direction is currently supported by only **1 publication** (which actually studied a different drug, Avosentan) and **no clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class — no Finland-specific license text on file) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Valsartan is an angiotensin II type 1 (AT1) receptor blocker (ARB), whose efficacy in hypertension is well established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Both the original and new indications sit on the same pathophysiological axis: malignant hypertension drives fibrinoid necrosis of the renal microvasculature largely through excessive renin-angiotensin-aldosterone system (RAAS) activation. AT1 blockade is the same mechanism used to control blood pressure in essential hypertension, so extending it to a RAAS-driven renal complication of severe hypertension is mechanistically coherent.

However, the only supporting literature (PMID 24368192) does not study Valsartan — it studies avosentan, an endothelin receptor antagonist, in a transgenic rat model of hypertensive nephropathy. This is class-level/analogous evidence at best, not drug-specific evidence, and should be weighted accordingly.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | RCT (non-Valsartan; avosentan) | Pharmacological Research | In double-transgenic rats overexpressing human renin/angiotensinogen, avosentan (an endothelin receptor antagonist, not Valsartan) protected against hypertensive nephropathy at doses below those causing fluid retention. |

## Finland Market Information

Valsartan is currently not marketed in Finland under this evidence pack — 0 product authorizations on file.

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug interaction data are currently on file; TFDA/Fimea package insert retrieval is flagged as a **Blocking** data gap — see below.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (mechanism/analogous evidence only), there are no clinical trials, and the single literature reference studies a different drug class (endothelin antagonist), not Valsartan itself. Mechanistic plausibility via RAAS inhibition exists but is not yet substantiated by drug-specific data.

**To proceed, the following is needed:**
- Valsartan-specific (not analog-drug) preclinical or clinical studies in hypertensive nephropathy/malignant hypertensive renal disease
- Official mechanism of action (MOA) data from DrugBank
- Package insert-derived warnings/contraindications — this is currently a **Blocking** data gap (DG001) that must be resolved before any S1 safety review
- Note: within this same evidence pack, a lower-ranked candidate — **chronic pulmonary heart disease** (rank 6, score 99.58%) — carries substantially stronger evidence (L1, multiple completed Phase 3/4 RCTs of sacubitril/valsartan in heart failure populations) and may warrant separate, higher-priority evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

