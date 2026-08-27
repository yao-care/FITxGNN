---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Moroctocog Alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant coagulation Factor VIII (FVIII) product; no formal original-indication text is present in this Evidence Pack, but it is a factor-replacement therapy conventionally used for haemophilia A. The TxGNN model predicts it may be effective for **primary release disorder of platelets** (a platelet granule-secretion defect), but this is currently supported only by **7 clinical trials — all graded low-relevance (Grade C)** — and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A *(inferred from drug class; `original_indications` and Finland license text are empty in this pack)* |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is a data gap). Based on known information, moroctocog alfa is a recombinant FVIII replacement product, and its role in restoring clotting-factor activity has been established for haemophilia A.

However, the pack's own mechanistic analysis argues **against** biological plausibility here: primary release disorder of platelets is a defect in platelet granule secretion/activation, not a deficiency in FVIII concentration or activity. Restoring circulating FVIII does not address a platelet degranulation defect, so there is no clear mechanistic bridge between the original and predicted indications.

Consistent with this, the 7 clinical trials retrieved for this indication were all judged **Grade C (low relevance)** on manual review — they largely concern FVIII products in haemophilia A (BIVV001, BAX 855) or unrelated coagulation/hematology research (AML, post-COVID vaccination syndrome, liver failure), and none actually studies platelet release disorders. This pattern looks like a database keyword mismatch rather than genuine supporting evidence, which is why the evidence level is capped at L4 despite the high TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN) prophylaxis/PK in severe haemophilia A ≥12y; **Grade C** — not platelet-disease specific |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | BIVV001 safety/efficacy in paediatric severe haemophilia A <12y; **Grade C** |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | BAX 855 (PEGylated rFVIII) in severe haemophilia A undergoing surgery; **Grade C** |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Coagulation profile observation in newly diagnosed AML; **Grade C** — not interventional, not disease-specific |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Symptom/lab evaluation in post-COVID-19-vaccination syndrome; **Grade C** |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system effect on coagulation in acute-on-chronic liver failure; **Grade C** |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal haemostasis in TIPS-procedure patients; **Grade C** |

*All 7 trials were assessed as low relevance (Grade C) — none directly studies moroctocog alfa in platelet release disorders.*

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Moroctocog alfa is currently not marketed in Finland (0 authorizations); no license data is available in this pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this is currently a Blocking data gap — TFDA/Finland package-insert warnings, contraindications, and DDI data are all unavailable, which prevents a full S1 safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted mechanism (FVIII replacement) does not plausibly address the underlying defect in primary release disorder of platelets (a platelet degranulation disorder), and the only available clinical trial evidence is low-relevance (Grade C) with no supporting literature — evidence level L4 is model/mechanism-only, not indication-specific.
- Among the 8 TxGNN candidates in this pack, rank 4 ("acquired coagulation factor deficiency," L3, decision stage S1) has notably stronger and more mechanistically consistent evidence and may warrant prioritized review instead.

**To proceed, the following is needed:**
- TFDA/Finland package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Mechanism of action (MOA) data from DrugBank — currently a High-severity gap (DG002)
- Platelet-release-disorder-specific clinical or preclinical evidence directly involving moroctocog alfa (not FVIII products generally)
- Re-scoping of trial search terms to exclude the FVIII/haemophilia-A keyword mismatches identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

