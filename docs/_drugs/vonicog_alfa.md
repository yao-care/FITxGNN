---
layout: default
title: Vonicog Alfa
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
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

Using the provided Evidence Pack directly (this is a report-writing task against an explicit template, not a codebase task — no skill applies). One structural note before the report: `predicted_indications[0]` (rank 1, "primary release disorder of platelets") has **zero** clinical/literature evidence, while rank 4 ("hemophilia") is the only candidate with real trial/publication support — and the pack's own rationale text flags that "hemophilia" label as likely a mislabeled reference to the drug's *existing* approved use (Von Willebrand Disease), not a genuine new indication. I built the report around rank 1 per the template's literal instruction, but added a full candidate-comparison table so this isn't buried.

---

# Vonicog Alfa: From Von Willebrand Disease to Primary Release Disorder of Platelets (Predicted)

## One-Sentence Summary

> Vonicog alfa (recombinant von Willebrand factor) is not currently marketed in Finland; its confirmed original-indication and mechanism-of-action data are both flagged as data gaps in this evidence pack.
> The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the model's own mechanistic rationale argues against biological plausibility.
> Across the 10 predicted indications in this pack, only one ("hemophilia", rank 4) has substantial evidence — and it appears to represent an ontology mislabeling of the drug's already-established use in Von Willebrand Disease rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in drug-level data (Blocking gap, DG001/DG002). Trial/literature text within this pack repeatedly references "severe Von Willebrand Disease" as the drug's established use. |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for vonicog alfa in this pack (marked as a High-severity data gap, DG002), and no original indication is recorded at the drug level (Blocking gap, DG001). Based on the evidence embedded elsewhere in this pack (clinical trial and literature abstracts under the "hemophilia" candidate), vonicog alfa is a recombinant von Willebrand factor (rVWF) used to stabilize endogenous Factor VIII and restore platelet adhesion — the standard replacement mechanism for Von Willebrand Disease.

For the top-ranked prediction, **Primary Release Disorder of Platelets**, the model's own rationale argues against mechanistic plausibility: this disease group stems from defects in platelet-internal signal transduction and granule secretion, not the VWF–GPIb adhesion axis that vonicog alfa targets. Supplementing VWF does not correct a release-machinery defect. No clinical trial or literature evidence was found for this pairing (0 hits across ClinicalTrials.gov, ICTRP, and PubMed), and the evidence level is accordingly the lowest tier (L5, model prediction only).

In short: the high TxGNN score reflects statistical pattern-matching in the knowledge graph, not a validated mechanistic or clinical signal for this specific candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Vonicog alfa is not currently marketed in Finland (0 authorizations on record). No license/product information is available in this pack.

---

## Other Predicted Indications (Full Candidate Comparison)

Since this evidence pack evaluates 10 candidate indications for vonicog alfa, the table below gives the full picture beyond the top-ranked candidate:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Trials | Literature | Recommendation |
|------|---------|-------------|-----------------|-----------------|--------|------------|-----------------|
| 1 | Primary release disorder of platelets | 99.98% | L5 | S0 | 0 | 0 | Hold |
| 2 | Glanzmann thrombasthenia | 99.98% | L5 | S0 | 0 | 0 | Hold |
| 3 | Pseudo-von Willebrand disease | 99.97% | L4 | S1 | 0 | 0 | Hold |
| 4 | Hemophilia | 99.95% | L1 | S3 | 4 | 5 | Proceed with Guardrails |
| 5 | Scott syndrome | 99.95% | L5 | S0 | 0 | 0 | Hold |
| 6 | Acquired coagulation factor deficiency | 99.94% | L5 | S0 | 0 | 0 | Hold |
| 7 | Von Willebrand disease, X-linked form | 99.92% | L4 | S0 | 0 | 0 | Hold |
| 8 | Bleeding diathesis due to a collagen receptor defect | 99.92% | L5 | S0 | 0 | 0 | Hold |
| 9 | Hemorrhagic disorder due to a constitutional thrombocytopenia | 99.92% | L5 | S0 | 0 | 0 | Hold |
| 10 | Flood factor deficiency | 99.90% | L5 | S0 | 0 | 0 | Hold |

**Notable flags:**
- **Rank 3 (Pseudo-von Willebrand disease)**: this is a documented *mechanistic contraindication risk*, not a data gap — the disease originates from a platelet GPIbα mutation with abnormally increased VWF affinity, so administering exogenous VWF could theoretically worsen thrombocytopenia by depleting large VWF multimers. Requires safety review before any further evaluation, independent of low evidence volume.
- **Rank 4 (Hemophilia)** is the only candidate with real trial/literature support: 4 Phase 3 trials (2 completed, 1 terminated, 1 recruiting) and 5 publications, all of which are actually about **Von Willebrand Disease** (rVWF prophylaxis, PK/PD vs. plasma-derived VWF, menorrhagia management), not classical Factor VIII/IX-deficient hemophilia A/B. This strongly suggests a knowledge-graph ontology mislabeling (VWD folded into a broader "hemophilia"/bleeding-disorder category) rather than a genuine new-indication signal — vonicog alfa's VWD use is standard of care, not a repurposing candidate.
- **Rank 7 (Von Willebrand disease, X-linked form)** is likely a similar ontology error: VWD is autosomal (chromosome 12), not X-linked; no such classification exists in standard hematology nomenclature.
- **Rank 10 (Flood factor deficiency)** is not a recognized medical term — likely a data extraction/translation error requiring source verification before clinical interpretation.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/Fimea package-insert warnings (DG001) and DDI data (query returned "not_found") are currently unavailable and are flagged as a **Blocking** gap for entering safety pre-assessment (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Primary Release Disorder of Platelets) has no supporting clinical or literature evidence and a mechanistically weak rationale per the model's own analysis. No candidate in this pack currently qualifies for progression on its own merits — the one candidate with strong evidence (rank 4, "hemophilia") most likely reflects the drug's existing approved use (Von Willebrand Disease) rather than a new indication.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/Fimea package insert warnings and contraindications before any S1 safety pre-assessment
- Resolve DG002 (High): obtain confirmed mechanism-of-action and original-indication data from DrugBank/regulatory source
- Disambiguate the "hemophilia" (rank 4) and "Von Willebrand disease, X-linked form" (rank 7) disease-entity labels against standard nomenclature — verify whether these represent real signals or ontology artifacts
- If pursuing rank 3 (Pseudo-VWD), commission a dedicated mechanistic/safety review given the identified contraindication risk
- No further action recommended on ranks 1, 2, 5, 6, 8, 9, 10 without new trial or literature evidence emerging
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

