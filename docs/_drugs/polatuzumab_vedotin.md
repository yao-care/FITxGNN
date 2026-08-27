---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Polatuzumab Vedotin: From B-Cell Lymphoma (DLBCL) to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) whose known drug class targets B-cell lymphomas such as DLBCL; confirmed original-indication and regulatory data for this evidence pack are not yet available. The TxGNN model predicts possible efficacy for **HER2-Positive Breast Carcinoma**, with a prediction score of **99.34%**, but **zero clinical trials** and **zero publications** currently support this direction — this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (no license/indication text available); drug class background points to B-cell lymphomas (e.g., DLBCL) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for polatuzumab vedotin is not available in this evidence pack. Based on the repurposing rationale provided, the drug is a CD79b-targeted antibody-drug conjugate (ADC) — CD79b is a component of the B-cell receptor complex, with expression physiologically restricted to the B-lymphocyte lineage (normal B cells and B-cell lymphomas such as DLBCL).

HER2-positive breast carcinoma, by contrast, is an epithelial-derived tumor driven by HER2/ERBB2 gene amplification and downstream PI3K/MAPK signaling — a pathway with no known intersection with CD79b/B-cell receptor signaling. There is no literature reporting CD79b expression in breast cancer cells.

The TxGNN score of 0.9934 reflects a graph neural network link-prediction output, which may capture a co-occurrence pattern between "cancer" and "ADC drug" node categories in the knowledge graph rather than genuine molecular mechanistic evidence. Combined with the absence of original MOA data, this prediction currently lacks a verifiable biological basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Polatuzumab vedotin currently holds no marketing authorizations in Finland (0 licenses on record; market status: Not Marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC), per repurposing rationale (anti-CD79b ADC) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no supporting clinical trials or publications, and the drug's known mechanism (CD79b/B-cell receptor signaling) has no established link to HER2-driven breast carcinoma biology. This is an L5, model-prediction-only signal with an unfavorable mechanistic rationale, which does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed original indication and formal MOA documentation via DrugBank/regulatory source (DG002)
- Drug interaction (DDI) data — current query returned not_found
- Any emergent preclinical or clinical evidence specifically linking CD79b/ADC mechanism to HER2-positive breast carcinoma before reconsidering this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

