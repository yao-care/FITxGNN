---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim is a thrombopoietin (TPO) receptor agonist internationally used to treat chronic immune thrombocytopenia (ITP); detailed original-indication and MOA data were not captured in this evidence pack, and the drug is not currently marketed in Finland.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, with **1 clinical trial** and **2 publications** currently associated with this direction — none of which directly test romiplostim in this specific disease.
Evidence quality is preclinical/mechanistic (L4); this remains a research question rather than an actionable repurposing candidate at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no licenses on file); internationally approved for chronic Immune Thrombocytopenia (ITP) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known information, romiplostim is a thrombopoietin receptor (MPL) agonist that binds and activates the TPO receptor on megakaryocyte progenitors, stimulating megakaryocyte proliferation and platelet production/release — this is the mechanistic basis of its established efficacy in chronic ITP.

Primary release disorder of platelets refers to defective release of platelets from megakaryocytes into circulation. Since romiplostim's core pharmacology is to stimulate megakaryocytopoiesis and platelet release, there is a plausible mechanistic direction between the two conditions.

However, the supporting evidence currently on file does not test this hypothesis directly: the single clinical trial identified (NCT03820960) is an observational study of thrombosis risk factors in ITP patients, not an interventional trial of romiplostim, and both literature citations are reviews of megakaryocytopoiesis/ITP autoantibody biology rather than romiplostim efficacy studies. As the rationale notes, the underlying mechanism (TPO receptor agonism to boost platelet generation) is directionally consistent, but the cited evidence describes autoantibody-mediated inhibition of proplatelet formation in ITP — a related but distinct clinical entity from primary release disorder of platelets itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Observational study of thrombosis risk factors in immune thrombocytopenia (ITP) patients; does not evaluate romiplostim treatment. Population-overlap relevance only (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Reviews megakaryocytopoiesis and thrombopoiesis biology, including TPO's role as the primary growth factor for the megakaryocyte lineage. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Review | Haematologica | Shows antiplatelet autoantibodies in primary ITP inhibit proplatelet formation by megakaryocytes and impair platelet production in vitro. |

---

## Finland Market Information

Currently no marketing authorization on file — romiplostim is not marketed in Finland (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were queried but not returned — flagged as a Blocking-severity data gap requiring retrieval of the TFDA/Fimea package insert.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a mechanistic rationale (TPO-receptor agonism → megakaryocyte stimulation) and indirect evidence — one observational trial that does not test romiplostim, plus two review articles on related ITP biology. No trial or publication directly evaluates romiplostim in "primary release disorder of platelets," placing this at evidence level L4 / decision stage S1 (Research Question).

**To proceed, the following is needed:**
- Original indication and mechanism-of-action data from DrugBank/Fimea package insert (currently marked as data gaps)
- Fimea/TFDA-equivalent package insert warnings and contraindications (Blocking gap — required before any safety pre-assessment)
- A direct interventional study (preclinical or clinical) of romiplostim specifically in primary release disorder of platelets, rather than general ITP populations
- Reassessment of other TxGNN-predicted indications in this pack with stronger direct evidence — notably "platelet-type bleeding disorder" (rank 8), which has a completed Phase 3 RCT (NCT03362177) and evidence level L2, and may warrant separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

