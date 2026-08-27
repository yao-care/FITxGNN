---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 3
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutant AML (External Reference) to Bulbar Polio — A Low-Confidence TxGNN Signal

## One-Sentence Summary

Ivosidenib (DB14568) has no original-indication or Finnish licensing record in this evidence pack; based on external background knowledge it is a targeted inhibitor of mutant IDH1, used in IDH1-mutant acute myeloid leukemia (AML) — this is not sourced from the dataset itself. The TxGNN model's top-ranked prediction, **Bulbar Polio**, has **0 clinical trials** and **0 publications**, and the rationale field explicitly flags it as having no plausible mechanistic link — most likely model noise. Two lower-ranked but mechanistically more coherent signals — **treatment-related AML/MDS** (alkylating-agent- and radiation-related) — remain at "Research Question" status pending dedicated evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no `original_indications`, no Finnish licenses); externally known as IDH1-mutant AML |
| Predicted New Indication | Bulbar Polio (rank 1) |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no studies) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on externally known information, ivosidenib is a targeted small-molecule inhibitor of mutant IDH1, an enzyme implicated in AML — this is background context, not data drawn from the dataset.

For the top-ranked prediction, **bulbar polio**, the rationale field in the evidence pack itself states there is **no identifiable mechanistic connection**: bulbar polio is an acute neurological disease caused by poliovirus infection of brainstem motor neurons, with no known pathological relationship to IDH1 metabolic-enzyme inhibition. With zero clinical trials, zero literature, and no mechanistic rationale, this signal is best interpreted as model noise or an atypical association rather than a genuine repurposing hypothesis.

By contrast, the two lower-ranked predictions — treatment-related AML/MDS following alkylating agents or radiation therapy — are mechanistically more coherent: both are recognized subtypes of the broader AML/MDS disease category, and a subset of cases can carry IDH1 R132 mutations, which would overlap with ivosidenib's known mechanism. However, the evidence pack contains no subtype-specific trials, literature, or IDH1-mutation-prevalence data for these subtypes, so this remains an indirect, unconfirmed inference (see below).

---

## Additional Predicted Indications (Lower Rank, Higher Mechanistic Plausibility)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 2 | AML/MDS related to alkylating agent | 99.26% | L4 | S1 | Research Question |
| 3 | AML/MDS related to radiation | 99.26% | L4 | S1 | Research Question |

Both are treatment-related AML/MDS subtypes with a plausible (though unconfirmed) overlap with ivosidenib's known IDH1-mutant AML mechanism. No clinical trials or literature specific to these subtypes were found in the queried sources (ClinicalTrials.gov, ICTRP, PubMed — all returned 0 results).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three TxGNN-predicted indications (bulbar polio; treatment-related AML/MDS – alkylating agent; treatment-related AML/MDS – radiation).

## Literature Evidence

Currently no related literature available for any of the three TxGNN-predicted indications.

## Finland Market Information

Ivosidenib is currently **not marketed in Finland**. No marketing authorizations are on file (0 licenses).

---

## Cytotoxicity

Ivosidenib's predicted and externally known indications are oncologic/hematologic (AML/MDS), so this section is included for completeness. Classification below is based on the drug's known identity as an IDH1 inhibitor (external reference); specific toxicity data are not present in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 enzyme inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (bulbar polio) has no supporting clinical trials, no literature, and no plausible mechanistic link — the evidence pack's own rationale identifies it as likely model noise. The two mechanistically more plausible predictions (treatment-related AML/MDS) remain at an early "Research Question" stage with no dedicated supporting evidence.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (blocking gap, DG001)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- If pursuing the treatment-related AML/MDS signals: subtype-specific IDH1 mutation prevalence data and dedicated clinical trial or case-series evidence
- DDI data source resolution (current query returned "not found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

