---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic established in indications such as cystic fibrosis pulmonary infection and complicated urinary tract infection (per mechanistic notes in this evidence pack); it is not currently marketed in Finland and no original-indication registry data is available. The TxGNN model predicts it may be effective for **Exposure Keratitis**, with **2 clinical trials** (both low direct relevance) and **7 publications** currently associated with this direction, none of which use tobramycin as the primary study intervention.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (Finland: not marketed, 0 licenses on record; `original_indications` field empty) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on information embedded in the evidence pack's rationale notes, tobramycin is an aminoglycoside antibiotic that binds the bacterial 30S ribosome to inhibit protein synthesis, giving it bactericidal activity against common Gram-negative and Gram-positive pathogens (notably *Pseudomonas aeruginosa* and *Staphylococcus aureus*); it is already established for infections such as CF pulmonary infection and complicated UTI.

Exposure keratitis results from incomplete eyelid closure, leaving the cornea chronically exposed and at elevated risk of secondary bacterial infection. Mechanistically, tobramycin's antibacterial spectrum against the pathogens most likely to cause secondary corneal infection provides a plausible rationale for use as a prophylactic/adjunct topical agent — this is consistent with tobramycin's long-standing off-label use as a topical ophthalmic antibiotic.

However, the evidence pack explicitly cautions that aminoglycosides carry known corneal epithelial toxicity (see PMID 2707046, an in vitro study of tobramycin among other aminoglycosides), and notes that **no trial in this dataset uses tobramycin as the actual intervention** for exposure keratitis. The prediction should therefore be read as mechanistically plausible but currently unsupported by drug-specific clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Evaluates platelet-rich fibrin (PRF) membrane across four ophthalmic conditions (macular hole, pterygium, corneal ulcer, post-trabeculectomy). Tobramycin is not the study intervention (relevance grade C). |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compares treatment modalities for dendritic corneal ulcer, primarily herpes simplex virus keratitis; tobramycin is not the primary intervention (relevance grade C). |

*Note: Neither trial directly evaluates tobramycin for exposure keratitis; both were graded "C" relevance in the source evidence.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Cohort/Lab comparison | Nippon Ganka Gakkai Zasshi | Compared MIC and post-antibiotic effect of antibiotic eye drops (including tobramycin) against isolates from Japan's National Surveillance of Infectious Keratitis. |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro | Current Eye Research | In vitro corneal epithelial cytotoxicity study of aminoglycosides (neomycin, gentamicin, **tobramycin**, amikacin) in rabbit corneal cell culture — informs known toxicity risk. |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis caused by multi-drug-resistant *Shewanella algae* without marine exposure. |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | *Bacillus cereus* keratitis associated with contact lens wear. |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy. |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Case series (veterinary) | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis seroprevalence and treatment outcomes — different pathogen class, low direct relevance. |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report (unrelated pathology) | Yan Ke Xue Bao | Paracentral corneal dellen as a sign of Graves ophthalmopathy — unrelated to infectious keratitis. |

## Finland Market Information

Tobramycin currently has no marketing authorization on record in Finland (market status: Not Marketed; total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/Fimea package-insert warnings and contraindications are flagged in this evidence pack as a **Blocking** data gap — see Conclusion below — and drug interaction lookup returned no data.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for tobramycin in exposure keratitis is mechanism-level only (L4) — no clinical trial or publication in this dataset uses tobramycin as the actual intervention for this indication, and a known aminoglycoside corneal-toxicity signal (PMID 2707046) warrants caution. Separately, the package-insert safety review cannot proceed at all: the missing TFDA/Fimea label data is a Blocking-severity gap in this evidence pack.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — required before any S1 safety screening can occur
- Confirmed DrugBank mechanism-of-action data for tobramycin
- A tobramycin-specific preclinical or clinical study in exposure keratitis, given the current lack of drug-specific evidence and the known corneal epithelial toxicity signal from aminoglycosides
- Clarification of tobramycin's original approved indication(s), since no data exists in Finland's registry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

