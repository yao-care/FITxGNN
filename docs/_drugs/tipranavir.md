---
layout: default
title: Tipranavir
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Tipranavir (DB00932) is a non-peptidic HIV-1 protease inhibitor; this evidence pack does not carry a documented original indication or MOA (both flagged as data gaps), but the drug is broadly known as an antiretroviral for treatment-experienced HIV-1 infection.
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)**, scored at **99.99%**,
> but there are **0 clinical trials** and **0 publications** supporting this specific link, and the evidence pack itself notes that FIV protease differs structurally enough from HIV-1 protease that cross-inhibition is biologically unlikely — this is best read as a TxGNN embedding artifact, not a credible repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (drug-level `original_indications`/`original_moa` are data gaps); publicly known pharmacology: HIV-1 infection, treatment-experienced adults |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tipranavir is marked as a data gap at the drug level in this evidence pack (DG002, High severity). Based on the mechanistic notes attached to the lower-ranked candidates in this same pack, tipranavir is a non-peptidic HIV-1 protease inhibitor that blocks viral replication by inhibiting protease-mediated cleavage of Gag-Pol polyproteins — but this is external/general knowledge, not something this dataset's drug-level fields actually support.

For the rank-1 prediction, FIV and HIV are both lentiviruses, which is presumably what drives the TxGNN embedding similarity. However, the evidence pack's own rationale explicitly flags that FIV protease and HIV-1 protease differ substantially in structure, and HIV protease inhibitors generally lack cross-species inhibitory activity against FIV protease. Combined with zero clinical trials, zero literature, and an evidence level of L5 (model prediction only), this specific top-ranked link should be treated as a low-confidence, likely spurious association rather than a genuine repurposing candidate.

Two lower-ranked candidates in this pack are mechanistically more coherent — "AIDS related complex" (rank 5) and "congenital human immunodeficiency virus" (rank 6) — since both sit within the HIV disease spectrum where protease inhibitors are an established drug class. Even so, the 9 trials retrieved for congenital HIV were graded "C" relevance because none actually studied tipranavir (they studied cabotegravir, dolutegravir, or general antiretroviral pharmacokinetics), so tipranavir-specific clinical evidence remains absent from this dataset for those indications too.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Tipranavir has 0 registered marketing authorizations in Finland (market status: 未上市 / not marketed), so no product-level table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack; DG001 — TFDA/Fimea package insert — is flagged as a **Blocking** gap that prevents S1 safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (FIV, 99.99% score) has no supporting trials or literature, and the pack's own mechanistic review flags it as a likely cross-species embedding artifact rather than a real pharmacological link — evidence level L5 does not clear even preliminary screening.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the TFDA/Fimea package insert to establish warnings/contraindications before any S1 safety evaluation.
- Resolve DG002 (High): confirm tipranavir's MOA via DrugBank API to properly assess mechanistic linkage.
- If pursuing HIV-spectrum indications instead of FIV, source tipranavir-specific trials/literature for "AIDS related complex" and "congenital HIV" (rank 5–6) — the trials currently attached to congenital HIV all involve other agents (cabotegravir, dolutegravir), not tipranavir itself.
- Treat rank 4 ("familial combined hyperlipidemia") as a candidate to exclude rather than pursue — the pack notes this likely reflects tipranavir's known dyslipidemia adverse-effect signal being mislearned as an indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

