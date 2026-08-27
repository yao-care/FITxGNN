---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

Using judgment as domain expert: the raw top-ranked TxGNN hit (`acromesomelic dysplasia, Hunter-Thompson type`, score 99.99%) has **zero evidence** and its own rationale text flags it as a likely false positive. The only candidate that clears an actual evidence bar (L2, real RCT literature, "Proceed with Guardrails") is **ankylosing spondylitis** (rank 5). Building the headline report around a biologically implausible top-score hit would be misleading, so the report below leads with the evidence-supported candidate and explains that deviation explicitly.

---

# Diflunisal: From NSAID Pain/Inflammation Use to Ankylosing Spondylitis

## One-Sentence Summary

> Diflunisal is a salicylic-acid-derivative NSAID historically used for pain and inflammatory musculoskeletal conditions.
> While TxGNN's single highest-scoring hit (a rare skeletal dysplasia) has no supporting evidence and is flagged as a likely false positive, its 5th-ranked prediction — **Ankylosing Spondylitis** — is backed by a direct head-to-head randomized trial and **7 supporting publications**, making it the more credible repurposing candidate from this evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in source data (drug class known: salicylate NSAID for pain/inflammation) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.98% (rank 373 by raw score; promoted to lead candidate based on evidence) |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (pending resolution of blocking safety data gap) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for diflunisal is not available in this evidence pack (Data Gap, High severity). Based on known drug-class information, diflunisal is a salicylic acid derivative NSAID; like other members of this class it inhibits cyclo-oxygenase (COX-1/COX-2), reducing prostaglandin synthesis and producing analgesic and anti-inflammatory effects.

Ankylosing spondylitis (AS) is a chronic inflammatory spondyloarthropathy in which NSAIDs are a well-established first-line symptomatic therapy. The mechanistic link is therefore direct rather than speculative: COX inhibition reduces the prostaglandin-mediated inflammation underlying AS symptoms, the same pathway targeted by diclofenac, naproxen, and pirprofen — all of which have documented efficacy in AS per the supporting literature below.

Notably, this is not a purely analogical (same-class) inference. One publication (PMID 3524970) is a direct, drug-specific randomized double-blind trial of diflunisal in AS patients, which is stronger support than typical repurposing hypotheses built only on class effects.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | RCT | Clinical Rheumatology | 12-week double-blind RCT (n=38) directly comparing diflunisal 500mg BID vs. phenylbutazone 200mg BID in AS; both effective, diflunisal had faster, more pronounced early analgesic onset, benefit maintained through 36-week open extension |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review (same-class: diclofenac) | Clinical Pharmacy | Reviews diclofenac pharmacology/efficacy across rheumatic conditions including AS, supporting class-level NSAID rationale |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Review (same-class: diclofenac) | Drugs | Diclofenac efficacy review covering rheumatoid arthritis, degenerative joint disease, and ankylosing spondylitis |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review (same-class: naproxen) | Drugs | Naproxen efficacy/tolerability review in rheumatic disease, supportive of NSAID class effect in spondyloarthropathies |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Review (same-class: pirprofen) | Drugs | Pirprofen reviewed as alternative NSAID therapy in rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Cohort | Annals of the Rheumatic Diseases | 48-week study of serum IgA vs. disease activity in AS patients on phenylbutazone or diflunisal; IgA correlated with chest expansion/lumbar flexion, not a direct efficacy trial |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Cohort | Journal of Rheumatology | Pulmonary function study in AS patients treated with diflunisal or phenylbutazone; assesses restrictive lung impairment vs. disease activity, not a primary efficacy endpoint |

**Limitation:** The only diflunisal-specific efficacy trial (PMID 3524970) is small (n=38, male only), over 35 years old, and compared against phenylbutazone — a comparator now withdrawn or heavily restricted in most markets due to toxicity — rather than placebo or a current standard of care.

## Finland Market Information

No market authorization records found — diflunisal is currently not marketed in Finland (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information. Note: collection of TFDA/local package-insert warnings and contraindications is an open **Blocking** data gap (DG001) — this candidate cannot complete a full S1 safety pre-assessment until that source is retrieved.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A direct, drug-specific randomized trial plus consistent same-class NSAID evidence support diflunisal's mechanistic and clinical plausibility in ankylosing spondylitis (L2, S2). However, the evidence base is old, small, and uses an outdated comparator, and a Blocking safety data gap (package insert / contraindications) remains unresolved, so this cannot yet advance to a Go decision.

**To proceed, the following is needed:**
- Retrieve TFDA/local package insert (warnings, contraindications) to close Blocking data gap DG001
- Obtain formal MOA documentation (DrugBank) to close High-severity gap DG002
- Assess feasibility of a modern-comparator (vs. placebo or current standard-of-care NSAID) trial or real-world evidence, given the existing trial's age and outdated comparator
- Clarify original indication history, since `original_indications` is empty in current source data

*Note: The top TxGNN-ranked prediction (acromesomelic dysplasia, Hunter-Thompson type, 99.99%) and 7 of the other top-10 predictions were excluded from this report — each has no clinical trial or literature support and their own mechanistic rationale explicitly notes no biological plausibility to diflunisal's NSAID mechanism (likely model noise/false positives).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

