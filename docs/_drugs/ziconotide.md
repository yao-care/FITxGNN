---
layout: default
title: Ziconotide
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Ziconotide
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

# Ziconotide: From Severe Chronic Pain to Migraine Disorder

## One-Sentence Summary

> Ziconotide is an N-type calcium channel blocker originally used as intrathecal therapy for severe chronic pain refractory to other treatments (not present as structured data in this evidence pack, sourced from general drug knowledge). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this is currently supported by only **0 clinical trials** and **1 case-report publication**, so the evidence base is very thin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe chronic pain requiring intrathecal analgesia *(not recorded in evidence pack — general drug knowledge; original_indications field is empty)* |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (original_moa: Data Gap). Based on the repurposing rationale supplied for this prediction, Ziconotide selectively blocks N-type (Cav2.2) voltage-gated calcium channels, inhibiting presynaptic release of neurotransmitters including glutamate and CGRP-related pathways.

Migraine pathophysiology is linked to abnormal neurotransmitter release in the trigeminovascular system, and familial hemiplegic migraine is genetically associated with mutations in P/Q-type (CACNA1A) calcium channels. This gives calcium-channel modulation general mechanistic plausibility in migraine.

However, the channel subtype Ziconotide targets (N-type) differs from the subtype genetically linked to migraine (P/Q-type), so this mechanistic extrapolation should be treated cautiously. Supporting evidence is limited to a single 2015 case report of chronic migraine resolution with intrathecal ziconotide — informative as a signal, but far from confirmatory.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Case Report | Journal of Pain Research | Single case of chronic migraine headache resolution following intrathecal ziconotide, framed around its N-type calcium channel blockade for chronic severe pain without tolerance/dependence issues seen with opioids |

---

## Taiwan Market Information

Ziconotide is currently **not marketed in Taiwan** (0 authorizations on record), so no product/license table is available.

---

## Safety Considerations

Safety data (key warnings, contraindications, drug–drug interactions) is entirely unavailable in this evidence pack — the TFDA package insert warnings/contraindications item is flagged as a **Blocking** data gap (DG001), which prevents entry into formal S1 safety pre-assessment.

> Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (migraine disorder) has only a single case report and zero clinical trials, and the mechanistic link relies on a calcium-channel subtype (N-type) that differs from the one genetically implicated in migraine (P/Q-type). Safety data is completely unavailable (Blocking gap), and the drug is not marketed in Taiwan — none of the criteria for "Go" or "Proceed with Guardrails" are met.

**To proceed, the following is needed:**
- TFDA package insert with warnings/contraindications (DG001, Blocking)
- Verified mechanism of action data via DrugBank API (DG002)
- Prospective or at least observational clinical data specifically evaluating ziconotide in migraine, given the N-type vs. P/Q-type channel mismatch noted above
- Confirmation of intrathecal route feasibility/acceptability for a migraine population, since Ziconotide's approved route is highly invasive relative to standard migraine therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

