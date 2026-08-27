---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Remdesivir is a nucleotide prodrug originally developed and used for COVID-19 (SARS-CoV-2 infection), with additional trial history in Ebola virus disease.
> The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**, with a **99.50% prediction score**,
> but currently **0 clinical trials** and **0 publications** support this direction — the evidence pack itself flags the prediction as a likely knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COVID-19 / Ebola virus disease (inferred from clinical trial evidence in this pack; not separately confirmed via `drug.original_indications`, which is empty) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% (rank #5453) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for remdesivir is not available in the structured `original_moa` field (flagged as a High-severity data gap, DG002). However, the evidence pack's own rationale fields describe remdesivir as an adenosine nucleotide prodrug that targets viral RNA-dependent RNA polymerase (RdRp), causing delayed chain termination — effective against RNA viruses such as Ebola virus and SARS-CoV-2.

Multiple Endocrine Neoplasia (MEN) is a hereditary tumour syndrome driven by germline mutations in genes such as *RET* and *MEN1*, with pathophysiology centered on endocrine cell proliferation — a mechanism with no known connection to viral RdRp inhibition. The evidence pack's own repurposing rationale for this top-ranked prediction explicitly states: *"無已知機轉關聯...高分應屬圖嵌入雜訊"* ("no known mechanistic link... the high score is likely graph-embedding noise").

Consistent with this, no clinical trials, ICTRP records, or PubMed literature were retrieved for the remdesivir–MEN pairing (query IDs 5–7 in the query log all returned zero results). This prediction should be treated as an unverified computational signal rather than a mechanistically or clinically supported hypothesis. For context, the pack's second-ranked prediction (HIV infection, score 99.32%) does have 23 trials and 20 publications, but review of those records shows they are overwhelmingly COVID-19/Ebola trials mismatched to the "HIV" disease label, and the pack's own mechanistic assessment likewise finds no basis for antiretroviral activity — reinforcing that none of the top-ranked TxGNN predictions in this pack currently have credible supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Remdesivir is not currently marketed in Finland (0 marketing authorizations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are a Blocking-severity data gap (DG001) that must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Multiple Endocrine Neoplasia) has zero supporting clinical trials or literature, and the evidence pack's own mechanistic analysis concludes there is no biological plausibility — the prediction is most likely a knowledge-graph artifact. Combined with the absence of any Finland market presence and a Blocking-severity gap in safety/label data, this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/Fimea-equivalent package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity gap (DG002)
- Any preclinical or mechanistic evidence linking RdRp-targeting nucleotide analogs to MEN-related pathways (*RET*, *MEN1*) before this candidate can be reconsidered
- If pursuing other TxGNN-ranked candidates instead (e.g., HIV infection), a re-screen of the retrieved trials/literature is needed, since current records appear to be COVID-19/Ebola studies mismatched to the disease label rather than genuine HIV-specific evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

