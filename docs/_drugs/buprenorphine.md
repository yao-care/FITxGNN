---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 6
---

# Buprenorphine
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

# Buprenorphine: From Opioid Dependence to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial opioid receptor agonist established for opioid dependence and pain management. The TxGNN model predicts a possible link to **Acute Intermittent Porphyria (AIP)**, but this is currently supported by only **0 clinical trials** and **1 case report**, and that single report describes buprenorphine being chosen for its favorable safety profile during anesthesia in an AIP patient — not evidence that it treats AIP itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid dependence / analgesia (general established use; no Finland-specific approved indication text available — drug is not marketed in Finland) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a data gap). Based on general pharmacological knowledge, buprenorphine is a partial μ-opioid receptor agonist / κ-antagonist used for opioid dependence and pain control; it is not established as a disease-modifying agent for porphyric conditions.

The single supporting publication (a 1993 Japanese anesthesiology case report) does not evaluate buprenorphine as a treatment for acute intermittent porphyria. Instead, it describes an anesthetic management decision: buprenorphine was selected as a comparatively "porphyrinogenic-safe" opioid for a patient with suspected AIP undergoing unrelated cancer surgery, because opioids metabolized outside the hepatic cytochrome pathways implicated in porphyric attacks are conventionally preferred in this setting.

Given this, the TxGNN prediction likely reflects a co-occurrence pattern — buprenorphine appearing on lists of "AIP-safe" perioperative drugs — rather than a genuine treatment-efficacy signal. There is no mechanistic rationale connecting opioid receptor activity to heme biosynthesis pathway modulation, which is the actual driver of AIP pathophysiology. This assessment is consistent with the lower-ranked predictions in this evidence pack (lingual-facial-buccal dyskinesia, chronic tic disorder, etc.), which similarly show literature describing incidental buprenorphine use in unrelated contexts rather than therapeutic evidence for those conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui (The Japanese Journal of Anesthesiology) | Anesthetic management case of a patient with suspected acute intermittent porphyria undergoing gynecologic cancer surgery; buprenorphine was among agents used as part of a porphyria-safe anesthetic regimen. Not a treatment-efficacy study for AIP. |

---

## Finland Market Information

Buprenorphine is not currently marketed in Finland; no marketing authorizations are on record in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Fimea package insert warnings and contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any Stage 1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acute Intermittent Porphyria) rests on a single 1993 case report describing a safety-motivated drug choice, not therapeutic evidence — evidence level L4 with zero clinical trials. All other predicted indications in this pack score even lower (L4–L5) and their supporting literature is explicitly assessed as incidental or noise-driven co-occurrence rather than mechanistic support.

**To proceed, the following is needed:**
- DrugBank MOA data to properly evaluate mechanistic plausibility (DG002)
- TFDA/Fimea package insert warnings and contraindications — currently a Blocking gap (DG001)
- Dedicated preclinical or mechanistic studies linking opioid receptor activity to heme biosynthesis/porphyria pathophysiology
- Any prospective clinical data (even observational) specifically evaluating buprenorphine as an AIP treatment, rather than as an incidental anesthetic choice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

