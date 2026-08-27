---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 6
---

# Evolocumab
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

# Evolocumab: From Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9-inhibiting monoclonal antibody used to lower LDL cholesterol in hypercholesterolemia/dyslipidemia. The TxGNN model's top prediction suggests possible relevance to **symptomatic hemophilia in female carriers**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis flags it as a likely graph-topology artifact rather than a genuine biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Finland market status is "not marketed," so no approved-indication text exists in the license registry. (General MOA context from the evidence pack: lipid metabolism / LDL-C lowering.) |
| Predicted New Indication | Symptomatic Form of Hemophilia in Female Carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is not available in this evidence pack. Based on the rationale text attached to the ranked predictions, evolocumab is an anti-PCSK9 monoclonal antibody that inhibits PCSK9-mediated degradation of the LDL receptor, thereby increasing LDL-C clearance — i.e., it acts on the lipid-metabolism / LDL-receptor pathway.

Symptomatic hemophilia in female carriers is a coagulation-factor disorder (Factor VIII/IX deficiency linked to X-chromosome carrier status), which operates through an entirely different biological axis than LDL receptor regulation. The evidence pack's own repurposing rationale explicitly states there is **no known mechanistic link** between PCSK9 inhibition and coagulation factor VIII/IX expression, and suggests the high TxGNN score likely reflects the graph model's proximity to a "rare hereditary disease" node cluster rather than a real pharmacological relationship.

This pattern repeats across all six ranked predictions in this pack (familial ApoC-II deficiency, thrombocytopenic purpura, factor XI deficiency, hemophilia A with vascular abnormality, and the non-specific ontology node "disease of catalytic activity") — each rationale independently concludes the mechanistic basis is weak or absent, and none currently have any clinical trial or literature support. This is a low-confidence prediction set that requires substantial additional evidence before any repurposing action is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

No marketing authorizations are on file — evolocumab is currently **not marketed** in Finland (0 licenses registered), so no approved-indication text is available for comparison.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable in this evidence pack — TFDA/Fimea package-insert retrieval is flagged as a **blocking** data gap in `meta.data_gaps` (DG001).)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications sit at evidence level L5 (model prediction only) with zero supporting clinical trials or literature, and the pack's own mechanistic-link analysis assesses the top candidates as probable graph-topology artifacts rather than genuine pharmacological relationships. Combined with the drug's unlicensed status in Finland, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature — currently a high-severity gap (DG002)
- Independent mechanistic or preclinical evidence connecting PCSK9 inhibition to coagulation-factor or hematologic pathways, beyond TxGNN embedding proximity
- Ongoing monitoring for any new clinical trial or publication signal on this drug–disease pair, given the current complete absence of real-world evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

