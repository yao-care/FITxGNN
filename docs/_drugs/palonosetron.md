---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 5
---

# Palonosetron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Palonosetron: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

> Palonosetron is a second-generation 5-HT3 receptor antagonist antiemetic, established for chemotherapy-induced nausea and vomiting (CINV) — this original-use context is general pharmacological knowledge and is **not** confirmed by the evidence pack itself, which contains no sourced original-indication text.
> The TxGNN model predicts possible effectiveness for **Migraine Disorder** (score **99.74%**), but the only supporting literature currently on file is a single case report titled *"Palonosetron-induced migraine-type headache"* — i.e., a report of the drug **causing** migraine-like symptoms, not treating them — and **no clinical trials** are registered for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (no `original_indications` or Finland license text on file); generally known as an antiemetic for CINV, but unverified against this data source |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, palonosetron is a highly selective 5-HT3 receptor antagonist, clinically established for preventing chemotherapy-induced nausea and vomiting.

The mechanistic case for migraine, however, is weak and arguably contradictory rather than supportive. The pharmacological standard of care for migraine — triptans — acts on 5-HT1B/1D receptors, a distinct serotonin receptor subtype with no established positive interaction with 5-HT3 antagonism. There is no established mechanism by which 5-HT3 blockade would relieve migraine.

More importantly, the single piece of literature evidence attached to this prediction is a case report describing palonosetron *inducing* migraine-type headache as an **adverse reaction**, not evidence of therapeutic benefit. This means the available real-world signal for this drug–disease pair points in the opposite direction from what the TxGNN score would suggest. The prediction should be read as a graph-based statistical association rather than a mechanistically or clinically supported hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report | Canadian Journal of Anaesthesia | Describes a case of palonosetron **inducing** migraine-type headache — an adverse-event report, not evidence of efficacy against migraine |

---

## Finland Market Information

Palonosetron is currently **not marketed** in Finland (0 authorizations on file); no product license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data are available in the current evidence pack — TFDA/product-label safety data is flagged as a **Blocking** data gap (DG001), meaning safety cannot yet be assessed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the migraine indication consists of a single case report of an **adverse effect** (drug-induced migraine-type headache), not a treatment signal, and no clinical trials exist. The proposed mechanism also lacks a positive pharmacological rationale (5-HT3 antagonism vs. the triptan/5-HT1B/1D pathway actually used in migraine). All five TxGNN-predicted indications for this candidate carry a "Hold" recommendation, and the two lower-ranked skin conditions (atrophoderma vermiculata, ulerythema ophryogenesis) have no literature or trial support at all.

**To proceed, the following is needed:**
- TFDA/Finland package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action and verified original indication, sourced rather than inferred from general knowledge (DG002)
- Independent evaluation of whether the "palonosetron-induced migraine" case report represents a class-level 5-HT3-antagonist safety signal, which would argue **against** rather than for this repurposing direction
- Any additional clinical or preclinical data establishing a positive (not merely correlative) mechanistic link to migraine before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

