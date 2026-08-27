---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: From [Original Indication Not on File] to Strongyloidiasis (Flagged as a Safety Signal, Not a Confirmed Opportunity)

## One-Sentence Summary

Brodalumab is an anti-IL-17RA monoclonal antibody; the Evidence Pack contains no populated `original_indications` field, so its originally approved use cannot be sourced from this dataset. The TxGNN model's top-ranked "new indication," **Strongyloidiasis**, is supported by **0 clinical trials** and **0 publications**, and the model's own repurposing rationale states this association is *mechanistically inverted* — IL-17 signaling is protective against intestinal helminth infection, so blocking IL-17RA would be expected to **worsen**, not treat, strongyloidiasis. This candidate should be read as a possible pharmacovigilance signal, not a repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (`original_indications` empty, `original_moa` = Data Gap; drug is not marketed in Finland) |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for brodalumab is not available in this Evidence Pack (`original_moa` = Data Gap). Based on information embedded in the repurposing rationale fields, brodalumab is described as an anti-IL-17RA monoclonal antibody, i.e., a full blocker of IL-17 receptor signaling — the same class as secukinumab and ixekizumab, which target IL-17-driven inflammatory diseases such as plaque psoriasis and psoriatic arthritis.

For the top-ranked prediction, **strongyloidiasis**, the mechanistic direction runs the opposite way from a therapeutic hypothesis. IL-17 is a key host-defense cytokine against extracellular parasites, including *Strongyloides stercoralis*. Blocking IL-17RA would be expected to impair anti-helminth immunity and could plausibly *increase* the risk of infection or hyperinfection syndrome in susceptible patients — a known class-level concern for IL-17 inhibitors — rather than provide a treatment benefit. The Evidence Pack's own rationale explicitly flags this as "likely a reverse or confounded association in the TxGNN knowledge graph" rather than a genuine treatment signal, and no clinical trials, ICTRP records, or literature exist to counter that interpretation.

The remaining candidates in the top-10 list follow a similar pattern: most are rare ophthalmic/optic-nerve conditions (e.g., von Hippel anomaly, optic perineuritis, episcleritis subtypes) with no clinical or literature evidence (L5), and several carry the same directional caution — IL-17 inhibitors as a class have documented case reports of triggering or worsening demyelinating/optic neuritis-type events, making those associations candidate safety signals rather than repurposing opportunities. Rank 2, "eye disease," has one linked trial and one publication, but the trial is a general immune-mediated skin disease registry (SKINERGY) unrelated to ophthalmology, and the literature is a general IL-17-blockade review — neither constitutes disease-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Brodalumab has 0 registered authorizations and is not currently marketed in Finland (`total_licenses: 0`, `licenses: []`). No product-level authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: this Evidence Pack flags TFDA label warnings/contraindications as a **Blocking** data gap (DG001) — safety pre-assessment (S1) cannot proceed until the package insert is retrieved and parsed. Drug interaction lookup also returned no results (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (strongyloidiasis) has no supporting clinical or literature evidence (L5) and its own mechanistic rationale points in the opposite direction — toward a safety risk rather than a therapeutic benefit. No candidate in the top 10 reaches an evidence level beyond L4, and the one candidate with any linked evidence ("eye disease," L4) is not disease-specific and appears to reflect a database mapping mismatch.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/Fimea package insert to close the Blocking safety data gap (DG001) before any S1 assessment
- Obtain verified mechanism-of-action data from DrugBank (DG002) to properly evaluate mechanistic plausibility
- If "eye disease" is pursued further, first narrow it to a specific IL-17-linked ocular diagnosis (e.g., uveitis) and re-query trials/literature against that specific term
- Route the strongyloidiasis association to pharmacovigilance/signal-detection review rather than the repurposing pipeline, given its mechanistically inverted direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

