---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 0
---

# Anifrolumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Anifrolumab: From Systemic Lupus Erythematosus — No TxGNN Repurposing Predictions Available

## One-Sentence Summary

Anifrolumab is a human monoclonal antibody targeting the type I interferon receptor (IFNAR1), approved in the US and EU for moderate-to-severe systemic lupus erythematosus (SLE).
The current Evidence Pack contains **no TxGNN-predicted indications** — the prediction pipeline has not yet generated output for this candidate.
This report documents available background data and identifies the critical gaps that must be resolved before a formal repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic Lupus Erythematosus (SLE), moderate-to-severe — based on global approval records |
| Predicted New Indication | Not available — TxGNN predictions not yet generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Prediction stage not yet reached |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Drug Background

> Currently, detailed mechanism of action data is not available in this Evidence Pack (DG002). Based on known global pharmaceutical information, the following background is provided for reference.

Anifrolumab (brand name: SAPHNELO) is a fully human IgG1κ monoclonal antibody that binds to subunit 1 of the type I interferon receptor (IFNAR1), thereby blocking the downstream signaling of all type I interferons — including IFN-α, IFN-β, and IFN-ω. Type I interferon overactivation is a well-established pathogenic driver in SLE, with elevated IFN gene expression signatures observed in approximately 60–80% of SLE patients.

Clinical efficacy was demonstrated in two Phase 3 trials (TULIP-1 and TULIP-2), leading to FDA approval in July 2021 and EMA approval in February 2022. The drug is not currently approved or marketed in Taiwan.

Because type I interferon dysregulation is mechanistically implicated in a broad spectrum of autoimmune and inflammatory conditions — including Sjögren's syndrome, inflammatory myopathies (dermatomyositis), systemic sclerosis, and ANCA-associated vasculitis — anifrolumab holds biological plausibility as a repurposing candidate across interferonopathies. However, no ranked TxGNN predictions are available in this Evidence Pack to formally evaluate this.

---

## Clinical Trial Evidence

Currently no predicted indication is available — clinical trial evidence table cannot be generated. Once TxGNN predictions are produced, trials will be retrieved and tabulated for the top-ranked indication.

---

## Literature Evidence

Currently no predicted indication is available — literature evidence table cannot be generated. Once TxGNN predictions are produced, relevant publications will be retrieved and tabulated.

---

## Taiwan Market Information

No product authorizations are registered for Anifrolumab with the TFDA. The drug is not marketed in Taiwan. A total of **0** licenses were found in the regulatory query conducted on 2026-03-29.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert data (warnings and contraindications) was flagged as a **Blocking** data gap (DG001). Safety data could not be retrieved in this Evidence Pack cycle, preventing completion of the S1 safety triage. DDI query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted indications, and a Blocking data gap in TFDA safety data prevents the S1 safety triage from being completed. No meaningful repurposing evaluation can proceed until both issues are resolved.

**To proceed, the following is needed:**

- **[Critical]** Re-run TxGNN prediction pipeline for `DB11976` (ANIFROLUMAB) to generate ranked new indication predictions
- **[Blocking]** Download and parse TFDA package insert PDF to retrieve warnings and contraindications (DG001), enabling S1 safety triage
- **[High]** Query DrugBank API to retrieve confirmed MOA data (DG002) for mechanism-linkage analysis
- **[Informational]** Confirm whether a Taiwan licensing pathway is being considered, or whether the regulatory strategy relies on cross-referencing existing FDA/EMA approvals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

