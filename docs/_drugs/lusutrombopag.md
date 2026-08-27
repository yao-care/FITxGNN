---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: From Chronic Liver Disease-Associated Thrombocytopenia to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Lusutrombopag is an oral TPO receptor agonist originally used to raise platelet counts before scheduled invasive procedures in patients with chronic liver disease. The TxGNN model predicts it may be relevant to **Hereditary Thrombocytopenia with Normal Platelets**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Preoperative thrombocytopenia in chronic liver disease patients (per evidence-pack rationale text; not independently confirmed by a formal indication record) |
| Predicted New Indication | Hereditary Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.995% (rank 88 overall) |
| Evidence Level | L5 (model prediction only) |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in the structured record (DG002). Based on the information available in the evidence pack, lusutrombopag is an oral TPO receptor agonist (TPO-RA) that stimulates megakaryocyte proliferation and differentiation to increase platelet production; its approved use is for thrombocytopenia prior to invasive procedures in chronic liver disease.

Hereditary thrombocytopenia with normal platelets is a disorder of platelet production regulation rather than a platelet functional defect, so directionally the TPO-RA mechanism (increasing platelet output) is biologically plausible for this indication. However, this link is inferred purely from TxGNN embedding similarity — there is no clinical trial, registry, or published case evidence connecting lusutrombopag to this condition to date.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Lusutrombopag is not currently marketed in Finland — no marketing authorizations are on record, so no product/dosage-form/indication information is available.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA package insert warnings/contraindications data is currently a **blocking data gap (DG001)** — a formal S1 safety screening cannot be completed until this is resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is itself scored as a "Research Question" (S0), with no clinical trial or literature support, and the drug's safety data (TFDA insert) is a blocking gap that prevents even a preliminary safety screen. The other 9 predicted indications in this evidence pack (rank 2–10, including two ALS-spectrum diseases likely reflecting embedding-level false positives) were independently assessed as Hold, reinforcing that this candidate is not yet actionable.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (resolves DG001 — required before any safety screening)
- Confirmed mechanism of action detail (resolves DG002)
- Preclinical or mechanistic evidence directly linking TPO-RA pathway activity to hereditary thrombocytopenia with normal platelets
- Ongoing literature/trial monitoring, since current PubMed/ClinicalTrials.gov/ICTRP searches all returned zero results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

