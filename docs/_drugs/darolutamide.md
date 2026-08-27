---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 3
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is an androgen receptor (AR) antagonist established for castration-resistant prostate cancer. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely embedding-similarity artifact rather than a mechanistically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (castration-resistant prostate cancer) — formal indication text not available in this data pull |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High data gap in this pack). Based on known information, darolutamide is a second-generation androgen receptor antagonist used for castration-resistant prostate cancer; its efficacy in that setting is well established, but no MOA data is present here to connect it to lipid metabolism.

Homozygous Familial Hypercholesterolemia is a genetic disorder driven by LDLR/APOB/PCSK9 defects that impair LDL receptor function and cause extreme LDL-C elevation. This is a pathway with no known mechanistic overlap with AR signaling. The evidence pack's own rationale is explicit on this point: it describes the link as having "no direct or known indirect mechanistic relationship" and states this is "a prediction driven purely by the TxGNN score, without any corroborating evidence."

In other words, this candidate should be read as a low-confidence model output rather than a biologically motivated hypothesis. The two other predicted indications in this pack (multiple endocrine neoplasia, HIV infection) show the same pattern — plausible-sounding disease names with no mechanistic or empirical support — which suggests the ranking region these predictions come from (rank ~8,600–9,200) may sit outside TxGNN's high-confidence zone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Darolutamide is not currently marketed in Taiwan (0 authorizations, no license records available in this data pull).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — androgen receptor antagonist (hormonal antineoplastic agent, not conventional cytotoxic chemotherapy) |
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
The predicted indication (HoFH) has no supporting clinical trials or literature and no plausible mechanistic link to darolutamide's known pharmacology — the evidence pack itself characterizes this as a score-only artifact (L5, decision stage S0). The two alternate candidates (multiple endocrine neoplasia, HIV infection) are similarly unsupported, one resting on a single terminated, 2-patient basket trial with no disease-specific relevance.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank — currently a High-severity data gap
- Confirmed original indication text (formal source, not just rationale-embedded mentions)
- Any preclinical or mechanistic rationale connecting AR antagonism to lipid metabolism, before this candidate can be reconsidered above S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

