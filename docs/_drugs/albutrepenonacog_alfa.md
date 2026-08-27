---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog Alfa: From Haemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa is a recombinant Factor IX–albumin fusion protein, originally developed to treat and prevent bleeding in Haemophilia B (congenital Factor IX deficiency). The TxGNN model predicts it may also be effective for **Pseudo-von Willebrand disease**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags the biological rationale as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia B / congenital Factor IX deficiency *(inferred from drug identity — not present in evidence pack; `original_indications` and `taiwan_regulatory.licenses` are both empty)* |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.94% (rank 878 among model predictions) |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known drug classification, albutrepenonacog alfa is a recombinant Factor IX molecule fused to albumin to extend half-life, and its efficacy in Haemophilia B — a **coagulation factor deficiency** affecting the secondary (plasmatic) haemostasis pathway — is well established.

However, the mechanistic plausibility for the top predicted indication is weak. Pseudo-von Willebrand disease is caused by a **gain-of-function mutation in the platelet GPIbα receptor**, which increases its affinity for von Willebrand factor. This is a **platelet receptor defect**, not a clotting factor deficiency — Factor IX supplementation does not correct abnormal receptor-ligand binding, and the evidence pack's own repurposing rationale explicitly characterizes the mechanistic link as sharing only a superficial "bleeding tendency" phenotype rather than a shared pathway.

Notably, the evidence pack surfaces five additional TxGNN-ranked candidates in the same score band (0.9994–0.9928), all of which are **primary haemostasis / platelet disorders** rather than coagulation factor deficiencies: primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome, collagen receptor–related bleeding diathesis, and thrombocytopenia-related bleeding disorder. Each carries the same L5 evidence level and the same internally-documented caveat that Factor IX has no established mechanism to correct platelet-level defects. This consistent pattern suggests the model is clustering diseases by shared "bleeding disorder" phenotype embeddings rather than identifying a genuine, actionable pharmacological pathway — a pattern that warrants caution rather than immediate pursuit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

The drug is currently **not marketed** in Finland (`market_status: 未上市`, `total_licenses: 0`), and no authorization records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and drug-drug interaction data are all marked as data gaps in this evidence pack. TFDA package insert warnings/contraindications are flagged as a **Blocking**-severity gap (DG001), meaning this candidate cannot yet complete an S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a TxGNN model score with no corroborating clinical trials or literature (Evidence Level L5), and the evidence pack's own mechanistic analysis concludes that Factor IX replacement has no established biological pathway to correct the underlying platelet receptor defect in pseudo-von Willebrand disease. Combined with a Blocking-severity gap in TFDA safety/label data, this candidate is not ready to advance past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking S1 safety review
- Confirmed mechanism of action data for albutrepenonacog alfa
- Preclinical or translational studies directly testing Factor IX supplementation in platelet-receptor-defect bleeding disorders, to establish biological plausibility before further investment
- Re-screening of TxGNN output to distinguish genuine mechanistic candidates from phenotype-clustering artifacts (given 6 similarly-scored, similarly-weak platelet-disorder predictions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

