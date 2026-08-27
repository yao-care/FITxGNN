---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 6
---

# Etanercept
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a TNF-α receptor fusion protein originally developed for rheumatoid arthritis and related inflammatory joint diseases.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, but the **6 clinical trials** and **20 publications** currently available include a direct negative trial and multiple reports of etanercept-induced (paradoxical) vasculitis, making the supporting evidence contradictory rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (based on known global approval history; structured original-indication data not available in this pack) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record. Based on known information, etanercept is a soluble p75 TNF-receptor–Fc fusion protein that binds and neutralizes TNF-α, thereby blocking a key pro-inflammatory cytokine implicated in rheumatoid arthritis and related autoimmune conditions. Its efficacy in rheumatoid arthritis has been proven in multiple pivotal trials, and mechanistically this TNF blockade could plausibly extend to other TNF-driven inflammatory conditions.

Rheumatoid vasculitis (RV) is recognized in the literature as one of the most severe extra-articular manifestations of rheumatoid arthritis (PMID 33058033), which gives the RA→RV pairing biological plausibility — both conditions share an underlying inflammatory, TNF-associated pathophysiology, and RV typically arises in patients with long-standing, severe RA.

However, the mechanism does not translate cleanly into supportive evidence. The only trial directly testing etanercept in an ANCA-associated vasculitis population (NCT00001901, Wegener's granulomatosis) was a negative/inconclusive study associated with safety concerns (the WGET research), not a positive efficacy signal. Compounding this, multiple case reports and case series describe etanercept **inducing** cutaneous or renal vasculitis as a paradoxical adverse event (e.g., PMID 31632872, 15853915, 12209493, 15801034), and a dedicated cohort study (PMID 28123776) quantifies TNF-inhibitor–associated risk of vasculitis-like events. This is a mechanistically coherent but evidentially contradictory signal — the drug's TNF blockade could theoretically help RV, but the accumulated clinical experience leans toward risk rather than benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 1/2 | Completed | 60 | Direct trial of etanercept in Wegener's granulomatosis (ANCA-associated vasculitis) — the only study testing the drug in a true vasculitis population; part of the WGET research and known to be a negative/safety-concern trial, not supportive of efficacy |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large real-world study on risk of developing additional immune-mediated inflammatory diseases in patients on biologics/immunosuppressants; indirect safety-relevant data only |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational registry of tocilizumab (not etanercept) in RA patients with inadequate response to DMARDs/biologics; general RA context, not vasculitis-specific |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world treatment-pathway comparison of etanercept vs. non-biologic therapy in moderate RA; not vasculitis-specific |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biologic DMARD treatment patterns in Chinese RA patients; not vasculitis-specific |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Evaluates perioperative immunosuppressant (including etanercept) management around shoulder arthroplasty in rheumatology patients; not vasculitis-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic review | Clinical Rheumatology | Systematic review of biological therapy use in rheumatoid vasculitis, a severe extra-articular RA manifestation |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology Dialysis Transplantation | Reviews the rationale and evidence for TNF-α blockade in ANCA-associated vasculitis and glomerulonephritis |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort (BSRBR-RA) | RMD Open | Quantifies drug-specific risk of lupus- and vasculitis-like events in RA patients treated with TNF inhibitors, including etanercept |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review/safety analysis | The Journal of Rheumatology | Analyzes the relationship between TNF-α blockade and risk of vasculitis |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case report | The Journal of Rheumatology | Reports proliferative lupus nephritis and leukocytoclastic vasculitis developing during etanercept treatment |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case report | Case Reports in Medicine | Large-vessel vasculitis occurring in an RA patient under anti-TNF therapy |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case series | Scandinavian Journal of Immunology | Immunologic mechanisms of cutaneous vasculitis associated with both etanercept and infliximab |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case report | Arthritis and Rheumatism | Accelerated nodulosis and vasculitis following etanercept therapy for RA (reverse/paradoxical signal) |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Case report | Cureus | Etanercept-associated nephropathy |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case report | Rheumatology (Oxford) | Etanercept and infliximab associated with cutaneous vasculitis |

---

## Finland Market Information

Etanercept is currently **not marketed in Taiwan** — no product authorizations are on file (0 licenses), so no license table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings and contraindications data is a currently unresolved data gap — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct clinical trial in a vasculitis population (NCT00001901, Wegener's granulomatosis) was negative/inconclusive with safety concerns, and multiple case reports describe etanercept as a potential **cause** of cutaneous or renal vasculitis rather than a treatment — this is contradictory, not supportive, evidence for the rheumatoid vasculitis indication.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap; required before any S1 safety screening)
- Confirmed mechanism of action documentation from DrugBank
- A dedicated, adequately powered trial or controlled observational study in rheumatoid vasculitis patients that directly weighs the paradoxical vasculitis risk signal against any therapeutic benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

