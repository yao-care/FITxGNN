---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 6
---

# Desloratadine
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

Using the evidence pack fields directly (no skill fits this templated report-writing task); drafting the report per the v5 prompt spec.

# Desloratadine: From Allergic Rhinitis/Chronic Urticaria to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation H1-antihistamine commonly used for allergic rhinitis and chronic urticaria. The TxGNN model predicts it may be effective for **Cold Urticaria (Acquired Cold Urticaria, ACU)**, with **3 clinical trials** and **7 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis / chronic urticaria (general second-generation antihistamine use; not documented in the Finland regulatory dataset provided) |
| Predicted New Indication | Cold Urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action data was not retrievable from DrugBank in this evidence pack. Based on known pharmacology, desloratadine is a selective, peripherally-acting second-generation H1-receptor antagonist — the active metabolite of loratadine.

Cold urticaria is triggered by cold-induced degranulation of cutaneous mast cells, with histamine release driving the wheal-and-flare response. Because desloratadine directly blocks the H1 receptor downstream of this histamine release, its established antihistamine activity maps mechanistically onto cold urticaria's pathophysiology, rather than requiring a novel mode of action.

This is reflected in the repurposing rationale supplied with the prediction: H1-antihistamines are already recommended by EAACI/GA²LEN urticaria guidelines as first-line therapy for cold urticaria, and dose-escalation (updosing) strategies with desloratadine specifically have been studied. This gives the TxGNN prediction direct, guideline-consistent mechanistic support rather than a purely inferential link.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center, double-blind, dose-escalating study assessing the desloratadine dose (5/10/20 mg) sufficient to inhibit cold urticaria symptoms. |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg vs. 20 mg desloratadine on experimentally induced cold urticaria lesions (thermography/volumetry); hypothesizes updosing (20 mg) is more effective than standard dose. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Evaluation of the inhibitory effect of 5 antihistamines (including desloratadine) in urticaria; class-comparison evidence rather than desloratadine-specific. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | 5 mg desloratadine for 4 days tested with ice-cube provocation in 12 cold urticaria patients before/after treatment. |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | High-dose desloratadine decreases wheal volume and improves cold provocation thresholds vs. standard dose in ACU patients (randomized, placebo-controlled, crossover). |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized controlled trial of H1-antihistamine dose escalation using critical temperature threshold measurement for cold urticaria. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of chronic urticaria aetiology, management, and current/future treatment options (including antihistamine class). |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of ebastine (a different antihistamine) in allergic rhinitis and chronic idiopathic urticaria; class-level, not desloratadine-specific. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Review/Case series | J Allergy Clin Immunol Pract | Describes food-dependent cold urticaria as a new variant of physical urticaria. |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | First reported case of cold-induced urticaria following black ant bite-induced anaphylaxis. |

## Finland Market Information

Desloratadine is currently **not marketed** in Finland per the available regulatory data, and no marketing authorizations were found (0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cold urticaria is supported by an L1 evidence level, including two completed Phase 4 RCTs specifically dosing desloratadine in ACU patients and three additional published RCTs (Juhlin 2004, Siebenhaar 2009, Magerl 2012) with a mechanism consistent with EAACI/GA²LEN guideline-recommended therapy. However, desloratadine is not currently marketed in Finland and TFDA-equivalent labeling/safety data (warnings, contraindications, DDI) were not retrievable, so guardrails on safety and regulatory pathway are required before advancing.

**To proceed, the following is needed:**
- Official package insert / label warnings and contraindications (currently a Blocking data gap)
- Confirmed drug-drug interaction profile
- Formal mechanism-of-action documentation from DrugBank
- Regulatory pathway assessment for introducing/relabeling desloratadine for cold urticaria in a market where it is not currently authorized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

