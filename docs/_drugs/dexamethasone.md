---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Corticosteroid Anti-Inflammatory Therapy to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid with broad anti-inflammatory and immunosuppressive use; this Evidence Pack does not contain specific original-indication or regulatory label data for the drug. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **1 relevant RCT** and **9 additional supporting publications** (mostly cohort/case-series data on oral "mini-pulse" corticosteroid therapy) currently backing this direction; no clinical trial registered on ClinicalTrials.gov directly evaluates this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (Evidence Pack contains no original indication or license text; dexamethasone is broadly known as a synthetic corticosteroid used across inflammatory/immune-mediated conditions) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack. Based on known pharmacology, dexamethasone is a high-potency synthetic glucocorticoid; its anti-inflammatory and immunosuppressive efficacy is well established across corticosteroid-responsive conditions, and mechanistically this profile plausibly extends to alopecia areata.

Alopecia areata (AA) is a T-cell-mediated autoimmune disease in which cytotoxic T lymphocytes attack hair follicles that normally sit in an "immune-privileged" state. Dexamethasone acts through the glucocorticoid receptor to suppress T-cell activation and local inflammatory cytokine release — a mechanism directly relevant to halting the autoimmune attack driving AA.

This is not a novel hypothesis generated purely from embedding similarity: oral dexamethasone "mini-pulse" (Oral Mini-Pulse, OMP) therapy has been used in dermatology practice for over two decades as a treatment for moderate-to-severe AA, particularly in pediatric populations and in patients ineligible for newer JAK-inhibitor therapy. This existing real-world clinical practice pattern reinforces the biological plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

The ClinicalTrials.gov query matched 14 registered trials containing "dexamethasone," but none directly evaluate dexamethasone for alopecia areata — all are unrelated regimens (e.g., multiple myeloma combination therapy, oncology supportive care, mesothelioma) rated low-relevance ("C") or off-topic by the relevance classifier.

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomized open-label trial in 30 children with severe AA comparing low-dose dexamethasone oral mini-pulse vs. DPCP contact sensitization |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / Network Meta-analysis | Archives of Dermatological Research | Compares systemic steroids, JAK inhibitors, and contact immunotherapy for severe AA; no single treatment shown clearly superior |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Literature review of pulse-dose corticosteroid dosing regimens and side effects for pediatric AA |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world evidence on effectiveness/safety of dexamethasone mini-pulse therapy and factors associated with response in AA |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Retrospective Cohort (Multicentric) | Dermatologic Therapy | Oral dexamethasone mini-pulse therapy for moderate-to-severe AA, including totalis/universalis subtypes |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Case Series (long-term follow-up) | Dermatologic Therapy | 65 children/adolescents with severe AA treated with monthly oral dexamethasone pulses plus topical corticosteroid, median 96-month follow-up |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Case Series | Dermatologic Therapy | 73 pediatric patients with severe AA; comparison of 1-day vs 3-day IV dexamethasone pulse regimens plus topical clobetasol |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Clinical Study | Dermatology (Basel) | Compares efficacy, relapse rate, and side effects among three systemic corticosteroid regimens for extensive AA |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Clinical Study | The Journal of Dermatology | Twice-weekly 5 mg oral dexamethasone pulse in 30 patients with widespread AA; reports complete regrowth outcomes |
| [17656876](https://pubmed.ncbi.nlm.nih.gov/17656876/) | 2002 | Clinical Review | Indian Journal of Dermatology, Venereology and Leprology | Discussion of dexamethasone pulse therapy utility and risk/benefit in extensive AA |

---

## Finland Market Information

Dexamethasone is currently **not marketed** in Finland per this Evidence Pack, with 0 registered authorizations and no license records available.

---

## Safety Considerations

Please refer to the package insert for safety information. This Evidence Pack contains no populated key warnings, contraindications, or drug interaction data (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between glucocorticoid immunosuppression and AA's T-cell-mediated pathology is well established, and one RCT plus multiple cohort/case-series studies support real-world use of dexamethasone oral pulse therapy in AA. However, no registered clinical trial directly evaluates this indication, and product-level regulatory/safety data are entirely absent, so full-scale progression is not yet warranted.

**To proceed, the following is needed:**
- Official package insert / regulatory label data (contraindications, warnings) — flagged as a **Blocking** data gap; required before any S1 safety pre-assessment
- Documented mechanism of action (MOA) from DrugBank or equivalent source — flagged as a **High** severity data gap
- Confirmation of Finland market/licensing status, since the drug currently shows 0 authorizations
- A prospective or registry-based trial specifically designed to evaluate dexamethasone (or OMP regimens) in AA, since existing evidence is exclusively retrospective/observational
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

