---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a well-established amide-type local anesthetic, used clinically as a topical/regional anesthetic (including in ophthalmic procedures, per the evidence base reviewed here). The TxGNN model's top-ranked prediction is **Punctate Epithelial Keratoconjunctivitis**, but this specific candidate currently has **zero supporting clinical trials** and **zero supporting literature** — it is a pure model-score signal with no external validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local/regional anesthesia (established pharmacological use; no Finland-specific licensed indication text on file — drug not marketed) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lidocaine in this evidence pack. Based on the supporting materials that *are* present (drawn from other ranked candidates in the same pack), lidocaine is a sodium-channel-blocking local anesthetic with established ophthalmic use as a topical/subconjunctival anesthetic during ocular procedures (e.g., intravitreal injection, pterygium excision, cataract surgery).

For the top-ranked candidate specifically, the evidence pack's own annotation states plainly: *"no clinical trial or literature evidence exists; this is a pure model prediction score."* Punctate epithelial keratoconjunctivitis is a corneal epithelial disorder (commonly viral, toxic, or dry-eye related in etiology), and no mechanistic pathway connecting lidocaine's anesthetic action to treating this condition is documented anywhere in the supplied data.

The only tangential plausibility argument is that lidocaine already has approved-formulation precedent for ocular surface application (ophthalmic gel/drops used peri-procedurally, seen in related candidates below), so a topical route would be technically feasible if a treatment rationale were ever established — but that rationale does not currently exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

No Finland market authorizations on file — lidocaine is not currently marketed in Finland under this evidence pack (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/Fimea package-insert warnings and contraindications are a **Blocking** data gap — DG001 — and have not yet been retrieved.)

## Other Screened Candidates (Ranks 2–10)

For context, nine additional TxGNN-predicted indications were screened alongside the top candidate. Only one showed meaningful (non-score-only) support:

| Rank | Disease | Score | Evidence Level | Stage | Note |
|------|---------|-------|-----------------|-------|------|
| 2 | Papillary conjunctivitis | 99.98% | L5 | S0 | No evidence |
| 3 | Rosacea conjunctivitis | 99.92% | L5 | S0 | No evidence |
| 4 | Exposure keratitis | 99.87% | L5 | S0 | 1 unrelated case-series (methamphetamine keratitis) |
| 5 | Atopic conjunctivitis | 99.86% | L4 | S0 | Indirect mechanistic hint only (nasal anesthesia/lacrimal reflex study) |
| 6 | Conjunctival disorder | 99.84% | L3 | S1 (Research Question) | Best-supported candidate — IV lidocaine literature for SUNCT/SUNA (trigeminal autonomic cephalalgia with conjunctival injection); most of its 18 trials reflect existing surgical-anesthesia use, not a new indication |
| 7 | Nephrotic syndrome | 99.83% | L5 | S0 | Pharmacokinetic/safety literature only, not efficacy |
| 8 | Non-human animal disease | 99.82% | L4 | S0 | Non-human disease label; primate seizure case report (safety signal, not efficacy) |
| 9 | Tinea corporis | 99.82% | L5 | S0 | No mechanistic link to antifungal activity |
| 10 | Steroid-resistant nephrotic syndrome | 99.79% | L5 | S0 | No evidence, no mechanistic hypothesis |

If pursuing this drug further, **rank 6 (conjunctival disorder / SUNCT-SUNA)** is the more defensible research direction, not the top-ranked candidate reported above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (punctate epithelial keratoconjunctivitis) is supported by a TxGNN score alone, with no clinical trials, no literature, and no mechanistic rationale in the evidence pack — this does not meet even the minimum bar for a Research Question stage (S1).

**To proceed, the following is needed:**
- Direct preclinical or mechanistic studies linking lidocaine to punctate epithelial keratoconjunctivitis
- TFDA/Fimea package insert data (warnings, contraindications) — currently Blocking gap (DG001)
- DrugBank mechanism-of-action detail — currently High-severity gap (DG002)
- Consider re-scoping evaluation to rank 6 ("conjunctival disorder," specifically the SUNCT/SUNA signal), which has the only L3/S1-level evidence in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

