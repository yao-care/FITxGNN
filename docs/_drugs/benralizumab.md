---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab: From Severe Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Benralizumab is a monoclonal antibody whose established use is severe eosinophilic asthma, where it depletes eosinophils through an anti-IL-5Rα/ADCC mechanism. The TxGNN model predicts a possible role in **Thrombocytopenia Due to Immune Destruction (Immune Thrombocytopenia, ITP)**, but this pairing is currently supported by **zero clinical trials** and **zero publications** — it is a pure model-generated hypothesis with an explicitly weak mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe eosinophilic asthma (inferred from supporting trial context in the evidence pack; not confirmed via local license data, as the drug is unmarketed in this market) |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction (ITP) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for benralizumab is not available in the structured record for this market. Based on the supporting evidence collected, benralizumab is an anti-IL-5Rα monoclonal antibody that clears eosinophils via antibody-dependent cell-mediated cytotoxicity (ADCC), acting primarily on the Type 2 inflammation pathway relevant to eosinophilic asthma.

Immune Thrombocytopenia (ITP), by contrast, is driven by autoantibody-mediated destruction of platelets by macrophages and the spleen — a mechanism centered on humoral autoimmunity and reticuloendothelial clearance, not eosinophil biology. The connection proposed by the model is only an indirect hypothesis: eosinophils have been observed to play a bystander role in some autoimmune conditions, but there is no established causal or mechanistic pathway linking IL-5Rα-mediated eosinophil depletion to platelet-sparing or ITP remission.

In short, this is a case where the TxGNN similarity score is high, but the underlying biology does not currently provide a credible causal story, and no trial or case evidence has yet been generated to test the hypothesis directly.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Benralizumab is not currently marketed in Finland — there are no marketing authorizations on file (total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Local warning, contraindication, and drug-interaction data could not be retrieved — this is logged as a Blocking data gap (DG001) that prevents a formal S1 safety pre-assessment.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction sits at the lowest evidence tier (L5) — no clinical trials, no literature, and only a self-described "weak, indirect" mechanistic hypothesis support it. Combined with missing local safety/label data (Blocking gap DG001) and missing MOA confirmation (DG002), there is currently no basis to advance this candidate beyond model output.

**To proceed, the following is needed:**
- TFDA/local package insert (warnings, contraindications) to clear the Blocking gap before any S1 safety review
- Confirmed mechanism-of-action data from DrugBank or primary literature
- Preclinical or translational evidence connecting IL-5Rα/eosinophil depletion to platelet autoimmunity, before committing to trial design
- Continued surveillance for case reports or investigator-initiated studies, since none currently exist

**Portfolio note:** Among the five indications TxGNN predicted for benralizumab, dermatitis (rank 2) has materially more evidence — 6 trials and 20 publications — but that evidence is largely negative (the Phase 2 HILLIER RCT, NCT04605094, was terminated, and PMID 37178404 reports "lack of effect" in atopic dermatitis). That candidate warrants its own separate evaluation rather than being folded into this one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

