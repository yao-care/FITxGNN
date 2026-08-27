---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# ETRAVIRINE: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Etravirine is a second-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) originally developed for HIV-1 infection treatment. The TxGNN model's top prediction is **Simian Immunodeficiency Virus (SIV) infection**, but this is currently supported only by **0 clinical trials** and **1 preclinical/in-vitro publication**, and the evidence pack itself flags the mechanistic rationale as weak and directionally uncertain.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (per repurposing rationale notes in the evidence pack; no formal Finland license record exists) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (MOA is flagged as a data gap, DG002). Based on known information, etravirine belongs to the NNRTI class and is well established for HIV-1 treatment by binding the reverse transcriptase (RT) enzyme's non-nucleoside binding pocket to block viral replication.

SIV and HIV-1 are both lentiviruses with structurally related reverse transcriptases, which is presumably why the TxGNN embedding model links them. However, the evidence pack's own rationale explicitly cautions that SIV reverse transcriptase differs meaningfully from HIV-1 RT within the NNRTI binding pocket sequence, and that most NNRTIs — including etravirine — show markedly reduced activity against SIV compared to HIV-1. This means the mechanistic extrapolation underlying this prediction is weak and its directionality is uncertain, rather than a confirmed cross-species mechanism.

Supporting this caution, the only literature retrieved for this indication is a single 2015 in vitro/preclinical nanoparticle drug-delivery paper that does not directly test etravirine activity against SIV. No clinical trials, ICTRP records, or dedicated antiviral-activity studies against SIV exist. Overall, this prediction should be read as a model-generated hypothesis requiring wet-lab confirmation, not an evidence-backed repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical (in vitro) | Molecular Pharmaceutics | Nanocarrier-based combination delivery of antiretroviral drugs (including NNRTIs) evaluated for synergistic inhibition of cell-free and cell-cell HIV transmission; does not directly test SIV activity. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) rests on a single indirect preclinical paper with no dedicated antiviral evidence against SIV, and the evidence pack itself flags the RT-sequence mechanistic link as weak and directionally uncertain (L4, S0). Critical drug-level data — TFDA/Fimea package insert warnings and contraindications (blocking, DG001) and detailed MOA (DG002) — are also missing, so this candidate cannot yet clear a basic safety pre-screen.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- In vitro or in vivo antiviral activity data for etravirine specifically against SIV reverse transcriptase
- Data-quality cleanup of the linked evidence set: several trials attached to lower-ranked predictions (e.g., rank 4, "congenital HIV") actually study other ARV agents (cabotegravir, rilpivirine, fosdevirine, darunavir) rather than etravirine itself, and one trial (NCT04273165, etravirine in Friedreich Ataxia) appears misclassified under an unrelated neurodevelopmental disorder prediction (rank 3) — these should be corrected before further scoring
- Note: ranks 4–5 ("congenital HIV," "AIDS related complex") largely restate etravirine's existing approved HIV-1 mechanism rather than representing a novel repurposing signal; ranks 6–10 have no supporting evidence (L5) and should remain Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

