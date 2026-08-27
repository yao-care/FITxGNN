---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Galcanezumab: From Migraine Prevention to Heparin Cofactor II Deficiency

## One-Sentence Summary

Galcanezumab is a humanized monoclonal antibody targeting CGRP (calcitonin gene-related peptide), clinically known for migraine and cluster headache prevention. The TxGNN model predicts possible efficacy in **Heparin Cofactor II Deficiency**, a rare hereditary coagulation disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis finds no known biological link between the two conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine / cluster headache prevention (from known drug class context; formal indication text not available in this evidence pack) |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap). Based on the mechanistic rationale included in this evidence pack, galcanezumab is a CGRP-targeting monoclonal antibody: it binds free CGRP and blocks downstream signaling (vasodilation, trigeminovascular sensitization), a pathway relevant to migraine and cluster headache, not to coagulation.

The three TxGNN-predicted indications for this drug — heparin cofactor II deficiency, antithrombin deficiency type 2, and factor V excess with spontaneous thrombosis — are all hereditary coagulation/serpin disorders. According to the evidence pack's own mechanistic analysis, there is **no established biological pathway** connecting CGRP signaling to thrombin inhibition, serpin structure/function, or coagulation factor expression. No published literature or clinical trial evidence supports any pharmacological interaction between galcanezumab and these disease mechanisms.

In short, this prediction reflects a purely statistical association from the TxGNN knowledge-graph embedding (score 99.50%, rank 5461), with no corroborating mechanistic, preclinical, or clinical evidence. The same conclusion applies to the second- and third-ranked candidates (antithrombin deficiency type 2, factor V excess), both scored similarly (~99.4%) and equally unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are flagged as a Blocking data gap — required before any Stage 1 safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is at Evidence Level L5 — model output only, with zero clinical trials, zero literature, and no biologically plausible mechanism linking a CGRP-targeting antibody to hereditary coagulation disorders. The drug is also not currently marketed in Taiwan, and core safety data (warnings, contraindications, DDI) are entirely unavailable.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking gap
- Confirmed DrugBank mechanism of action data
- Preclinical or mechanistic studies establishing any plausible link between CGRP pathway modulation and coagulation/serpin function
- Ongoing monitoring for any future clinical trials or case reports in this disease area before re-evaluating beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

