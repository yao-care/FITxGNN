---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

> Daptomycin is a cyclic lipopeptide antibiotic originally used to treat serious Gram-positive bacterial infections (complicated skin/skin-structure infections, *S. aureus* bacteraemia, right-sided infective endocarditis).
> The TxGNN model predicts it may be effective for **Osteoarthritis**, with **0 clinical trials** and **10 publications** currently associated with this signal — however, closer review shows the literature actually concerns treatment of *prosthetic joint/osteoarticular infections* in patients who happen to have osteoarthritis, not treatment of osteoarthritis itself. This appears to be a keyword-confusion artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (complicated skin/skin-structure infections, *S. aureus* bacteraemia, right-sided infective endocarditis) — Finland-specific label text unavailable (drug not marketed there) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on generally known pharmacology (and consistent with statements found within the literature retrieved for this pack, e.g. PMID 39571268), daptomycin is a calcium-dependent cyclic lipopeptide that disrupts the cell membrane of Gram-positive bacteria, causing rapid depolarization and cell death. It is not known to have a specific mechanistic link to degenerative joint disease.

The high TxGNN score for osteoarthritis does **not** appear to reflect a genuine pharmacological relationship. All ten retrieved publications describe daptomycin's use in treating **prosthetic joint infections (PJI)** or other **osteoarticular infections** — serious complications that can occur *after* joint replacement surgery, which patients often undergo *because of* osteoarthritis. In other words, the literature co-occurrence is driven by shared vocabulary ("joint," "osteoarticular," patients with an OA history) rather than any evidence that daptomycin treats osteoarthritis itself. None of the studies test daptomycin as a disease-modifying or symptomatic therapy for OA.

For context, the model's second-ranked prediction — **rheumatoid arthritis** (score 99.84%, rank 2176) — is supported by more mechanistically direct, if still early-stage, evidence: two 2025 preclinical studies (PMID 39571268, PMID 40923559) report that daptomycin and its lipopeptide derivatives suppress inflammatory cytokines and NF-κB signalling in a collagen-induced arthritis mouse model, suggesting a possible independent anti-inflammatory activity distinct from its antibacterial action. This is not yet human evidence, but it is a more biologically plausible lead than the osteoarthritis signal and may warrant separate tracking.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | International Orthopaedics | High-dose daptomycin + rifampicin for Gram-positive osteoarticular infections — evaluated safety/efficacy of the combination, not OA treatment |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Daptomycin for knee/hip periprosthetic joint infections (PJI) |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone/joint and implant-associated Gram-positive infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs. standard therapy for osteoarticular infections associated with *S. aureus* bacteraemia |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry/Cohort | Medicina Clínica | EU-CORE registry: daptomycin use experience across Spanish hospitals for Gram-positive infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Cohort/Survey | Int J Antimicrob Agents | Survey of current PJI management practices among infectious disease physicians |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In-vitro susceptibility | Journal of Antibiotics | *S. aureus*/*S. epidermidis* susceptibility testing in PJI isolates |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Microbiologic survey | Surgical Infections | 10-year evolution of Staphylococcal susceptibility profiles in osteoarticular infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | Case Reports in Orthopedics | *Corynebacterium striatum* septic arthritis in a patient originally referred for total knee arthroplasty for OA |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | ASM Case Reports | *Corynebacterium propinquum* septic arthritis, first synovial fluid isolation in a native joint |

**Note:** None of these publications studies daptomycin as a treatment for osteoarthritis itself — all concern management of bacterial infections in or around joints (often in OA patients post-arthroplasty).

---

## Finland Market Information

Daptomycin is not marketed in Finland — no marketing authorizations are currently registered for this product in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Additional literature-derived safety signal (not from the structured safety dataset, but surfaced during evidence review):** one case report (PMID [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/), 2023) describes daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis, consistent with daptomycin's known association with creatine kinase elevation/myopathy. This is a recognized class effect worth flagging for any future clinical use, independent of the repurposing question.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis signal is not supported by genuine mechanistic or clinical evidence — all ten retrieved publications concern treatment of bacterial osteoarticular/prosthetic joint infections, not osteoarthritis itself, and appear to be a keyword co-occurrence artifact rather than a real repurposing opportunity (evidence level L4, decision stage S0, per source scoring).

**To proceed, the following is needed:**
- Confirm whether TxGNN's osteoarthritis prediction should be deprioritized/excluded given the confounded evidence base
- If pursuing a joint-related signal at all, redirect attention to **rheumatoid arthritis** (rank 2), where 2025 preclinical data (PMID 39571268, PMID 40923559) show a plausible independent anti-inflammatory mechanism — though this still requires human-stage validation before advancing past S1
- Daptomycin's mechanism of action (MOA) data and TFDA/EMA label warnings and contraindications (currently marked Blocking/High severity data gaps) must be obtained before any safety pre-assessment (S1) can proceed
- Given the drug is not marketed in Finland, market-access and regulatory pathway feasibility would also need to be assessed separately
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

