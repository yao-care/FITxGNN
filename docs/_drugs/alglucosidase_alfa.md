---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase Alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is a recombinant human acid α-glucosidase (rhGAA) enzyme replacement therapy, best known for treating Pompe disease (glycogen storage disease type II). The TxGNN model predicts it may be effective for **Adult Polyglucosan Body Disease**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug is not marketed in Finland.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pompe disease (acid α-glucosidase deficiency / glycogen storage disease type II) — *not present in this Evidence Pack's Finland licensing data, since the product is unmarketed there* |
| Predicted New Indication | Adult Polyglucosan Body Disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on known information, Alglucosidase alfa is a recombinant human acid α-glucosidase (rhGAA) enzyme replacement therapy; its efficacy in Pompe disease has been proven, and mechanistically it may be applicable to other disorders of glycogen metabolism that share an overlapping enzymatic pathway.

However, the mechanistic rationale supplied for this specific prediction is cautious rather than supportive. Adult polyglucosan body disease is primarily caused by deficiency of **GBE1** (glycogen branching enzyme), not GAA — only a minority of reported cases show overlap with GAA mutations. The core pathology in this disease is *structurally abnormal* glycogen (polyglucosan) accumulation due to a branching defect, not simply a shortfall of enzyme activity. There is no established mechanistic evidence that GAA enzyme replacement therapy can clear this structurally abnormal glycogen. The rationale explicitly notes that the high TxGNN score likely reflects the knowledge graph's clustering of "glycogen metabolism disease" nodes near one another, rather than a direct pharmacological correspondence.

This caution extends to the rest of the top-10 predicted list: ranks 2–3 (GSD IV subtypes) share the same GBE1-vs-GAA mismatch, while ranks 4–10 (congenital entropion/ectropion, Horner syndrome, ptosis syndromes, congenital eye/muscle disorders) have no known mechanistic link to lysosomal glycogen metabolism at all and are explicitly flagged in the source data as likely graph-proximity noise from shared "congenital/rare disease" annotations. None of the ten predictions currently have any corroborating clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Alglucosidase alfa is currently **not marketed** in Finland — the Evidence Pack lists 0 authorizations and no license records, so no product/authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug–drug interaction data are all recorded as data gaps in this Evidence Pack. Notably, TFDA/Fimea package insert warnings and contraindications are flagged as a Blocking data gap — DG001 — which by itself prevents this candidate from entering the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — a model prediction with zero corroborating clinical trials or literature. The proposed mechanistic link is weak: the target disease's primary causal enzyme (GBE1) differs from Alglucosidase alfa's target (GAA), and the score pattern across the full top-10 list suggests disease-category clustering in the knowledge graph rather than genuine pharmacological signal. In addition, a Blocking data gap (missing TFDA/Fimea package insert data) independently prevents progression to safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/Fimea official package insert (warnings, contraindications) — resolves Blocking gap DG001
- Confirmed mechanism-of-action documentation from DrugBank — resolves High-severity gap DG002
- Case-level or preclinical evidence specifically for patients with overlapping GAA mutations in adult polyglucosan body disease, rather than reliance on disease-category similarity
- Reassessment of whether GBE1-directed (rather than GAA-directed) therapeutic strategies are more appropriate targets for this indication
- Clarification of any regulatory pathway or market intent for Finland, given the drug is currently unmarketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

