---
layout: default
title: Regadenoson
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 4
---

# Regadenoson
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

# Regadenoson: From Cardiac Stress Test Agent to Anaphylaxis

## One-Sentence Summary

> Regadenoson is a selective adenosine A2A receptor agonist used clinically as a pharmacologic cardiac stress agent for myocardial perfusion imaging, not as a disease-treating drug.
> The TxGNN model predicts it may be effective for **Anaphylaxis**, with a score of **99.85%**,
> but this is supported by only **1 loosely related clinical trial** and **0 publications** — and the mechanistic evidence points the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharmacologic cardiac stress agent (myocardial perfusion imaging) — not formally structured in source data; no Finland-approved indication text available |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap in the structured record, but the evidence pack's own mechanistic analysis identifies regadenoson as a selective adenosine A2A receptor agonist, used clinically to pharmacologically simulate exercise stress during cardiac perfusion imaging in patients who cannot exercise adequately.

The predicted link to anaphylaxis does **not** follow a plausible treatment mechanism. Adenosine A2A receptor activation is mechanistically associated with mast cell degranulation and vasodilation — this is precisely why regadenoson's own label already carries a known risk of anaphylactoid/hypersensitivity reactions (flushing, dyspnea, hypotension) as an **adverse effect**, not a therapeutic one. The single clinical trial retrieved for this indication (NCT06854458) confirms this pattern: it is a cardiac stress-MRI perfusion study where regadenoson is used as the stress-inducing agent, and anaphylaxis appears only as a monitored adverse event, not a treatment endpoint (relevance grade **C**).

This concern is reinforced by the broader prediction set: of the top 4 TxGNN candidates for this drug, three (anaphylaxis, food-dependent exercise-induced anaphylaxis, pseudoallergy) are all hypersensitivity/mast-cell-mediated conditions. This clustering strongly suggests the knowledge graph has encoded a drug→adverse-event relationship as a drug→indication relationship — i.e., a likely **direction-inverted signal** rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | N/A | Recruiting | 1000 | Multicenter stress cardiac MRI perfusion imaging study; regadenoson used as the pharmacologic stress agent. Anaphylaxis is not a treatment target — at most a monitored adverse event. Relevance graded **C** (low relevance to the treatment hypothesis). |

*No clinical trials were found for the other predicted indications (food-dependent exercise-induced anaphylaxis, esotropia, pseudoallergy).*

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Regadenoson is not currently marketed in Finland (0 authorizations on record); no product/license data is available.

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, DDI) are not populated in the source data. However, the evidence pack's mechanistic rationale flags that regadenoson has a **known risk of anaphylactoid/hypersensitivity reactions** (flushing, dyspnea, hypotension) as part of its established adverse-effect profile — directly relevant given that this is also the predicted "new indication." Full labeling data (TFDA/package insert warnings and contraindications) is currently a **blocking data gap** and has not yet been retrieved.

Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) — the one retrieved clinical trial does not actually support treating anaphylaxis with regadenoson, and no literature exists. More importantly, the mechanistic pattern (adenosine A2A agonism triggering mast-cell-mediated reactions) and the clustering of hypersensitivity-related predictions across this drug's top candidates both suggest this is a safety signal misclassified as a treatment signal, not a genuine repurposing hypothesis.

**To proceed, the following is needed:**
- Retrieve TFDA/package insert warnings and contraindications (currently a blocking gap for S1 safety evaluation)
- Confirm mechanism-of-action data via DrugBank to formally rule in/out the signal-inversion hypothesis
- If pursued further, obtain preclinical or mechanistic studies that directly link A2A receptor agonism to an anti-anaphylactic (rather than pro-anaphylactic) effect before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

