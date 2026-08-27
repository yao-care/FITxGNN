---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# Nevirapine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is an approved HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI). The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome** (FIV infection in cats), but this direction is currently supported by only **1 publication** and **no clinical trials**, and that single study raises caution rather than confirming efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (nevirapine is referenced in the evidence pack as an "approved HIV-1 non-nucleoside reverse transcriptase inhibitor"; a formal indication text/MOA record is not yet on file) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, nevirapine is known to act as an NNRTI that binds the hydrophobic allosteric pocket of HIV-1 reverse transcriptase (RT), a mechanism referenced elsewhere in this same evidence pack.

Feline immunodeficiency virus (FIV) causes an AIDS-like syndrome in cats and, like HIV-1, depends on a reverse transcriptase for replication — the superficial rationale for testing HIV-1 NNRTIs against it. However, the sole supporting publication (PMID 38031646) is a structural/biochemical comparison of NNRTIs against feline vs. human RT, and this type of study is typically conducted precisely *because* the two RTs differ significantly in structure. The evidence therefore points toward **limited or unpredictable cross-species inhibition**, not demonstrated efficacy.

Taken together, the mechanistic plausibility is weak: the link is a shared drug class/target family rather than confirmed cross-species activity, and FIV is a veterinary (non-human) indication that sits outside the typical human drug-repurposing development pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Structural/biochemical comparison study | Journal of Veterinary Science | Compared nevirapine, efavirenz, and rilpivirine biochemically/structurally against feline vs. human RT to assess NNRTI potential for treating FIV-infected cats; no effective FIV treatment currently exists |

## Finland Market Information

Nevirapine is currently not marketed in Finland, and no marketing authorizations are on record.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert data was queried but is currently a Blocking-severity data gap in this evidence pack, preventing a full safety review.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication rests on a single preclinical structural/biochemical comparison study with no clinical trials, and that study itself suggests cross-species RT inhibition may be limited rather than confirming therapeutic benefit. The candidate indication is also a veterinary disease (feline FIV), which falls outside standard human drug-repurposing evaluation.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently a Blocking gap preventing S1 safety evaluation
- Detailed mechanism of action (MOA) data for nevirapine — currently a High-severity gap
- In vivo/in vitro efficacy data specifically demonstrating antiviral activity against FIV (not just structural RT comparison)
- If a human-relevant repurposing signal is desired, note that rank 2 in this evidence pack (simian immunodeficiency virus infection, L3/S1, 17 supporting publications) has a stronger and more direct mechanistic basis, though it also concerns a non-human model rather than a human indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

