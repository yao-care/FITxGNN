---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 3
---

# Tacrolimus
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

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a topical calcineurin inhibitor best known for treating atopic dermatitis (eczema) under products such as Protopic.
The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
with **2 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (topical calcineurin inhibitor) — no formal indication text on file for this dataset |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, tacrolimus is a calcineurin inhibitor originally developed as a topical immunomodulator (Protopic ointment) for atopic dermatitis; it suppresses T-cell activation and downstream inflammatory cytokine release without the skin-atrophy risk associated with long-term topical corticosteroid use.

Seborrheic dermatitis and atopic dermatitis are both chronic, relapsing inflammatory skin conditions driven by T-cell/cytokine-mediated inflammation, and seborrheic dermatitis additionally involves *Malassezia*-associated impairment of skin barrier permeability. Because calcineurin inhibition dampens the shared inflammatory cascade, tacrolimus's established anti-inflammatory activity in atopic dermatitis is mechanistically plausible for seborrheic dermatitis as well.

This mechanistic rationale is reinforced by real clinical use: tacrolimus ointment has repeatedly been trialed specifically for facial seborrheic dermatitis maintenance therapy (steroid-sparing, safe for chronic facial application), which is exactly the use case supported by the Phase 3 and Phase 4 trial evidence below.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Maintenance treatment with tacrolimus ointment (Protopic) for severe facial seborrheic dermatitis in adults, aiming to prolong remission and reduce topical steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once/twice-weekly 0.1% tacrolimus ointment to maintain remission and reduce exacerbation in adult facial seborrheic dermatitis |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | RCT | Annals of Dermatology | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment reduces flare-ups similar to intermittent TCI use in atopic dermatitis |
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter double-blind RCT: tacrolimus 0.1% vs ciclopiroxolamine 1% for maintenance therapy of severe facial seborrheic dermatitis |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | RCT | J Am Acad Dermatol | Single-blind RCT comparing hydrocortisone 1% ointment vs tacrolimus 0.1% ointment for facial seborrheic dermatitis in adults |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical Trial | Annals of Parasitology | Compared sertaconazole 2% cream vs tacrolimus 0.03% cream efficacy in seborrheic dermatitis treatment |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, TCIs) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Review of topical calcineurin inhibitors' pathophysiology, safety, and efficacy as a corticosteroid-sparing option in seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis pathophysiology and therapeutic horizons, including calcineurin inhibitors |
| [15663338](https://pubmed.ncbi.nlm.nih.gov/15663338/) | 2004 | Review | Am J Clin Dermatol | Review of antifungal agents' role in seborrheic dermatitis, providing treatment-landscape context for calcineurin inhibitor use |
| [28685715](https://pubmed.ncbi.nlm.nih.gov/28685715/) | 2017 | Cohort | Chinese Medical Journal | Found high *Staphylococcus epidermidis* colonization and impaired skin barrier permeability in facial seborrheic dermatitis, supporting the barrier/inflammation rationale for TCI therapy |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label Pilot | J Am Acad Dermatol | Open-label pilot study: 0.1% tacrolimus cleared seborrheic dermatitis completely in 61% of 18 patients within 28 days |

## Finland Market Information

Tacrolimus currently has no marketing authorization on file in this dataset (market status: Not Marketed, 0 authorizations). No product/authorization details are available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. No structured safety warnings, contraindications, or drug interaction data are currently available for this candidate (TFDA/Fimea package insert data is flagged as a blocking data gap).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed trials (one Phase 3, one Phase 4) plus multiple RCTs and reviews directly support tacrolimus ointment for facial seborrheic dermatitis maintenance therapy, giving an L1 evidence level. However, the drug is not currently marketed in this jurisdiction and formal safety/label data is missing, so guardrails are warranted before advancing.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-priority gap, DG002)
- Confirmation of local marketing/regulatory pathway status before any repurposing submission
- Drug-drug interaction (DDI) data, currently unavailable (query returned not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

