---
layout: default
title: Nelarabine
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 1
---

# Nelarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Nelarabine: From T-cell Acute Lymphoblastic Leukemia/Lymphoma to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine (DrugBank DB01280) is a purine nucleoside analogue prodrug internationally approved for T-cell acute lymphoblastic leukemia and T-cell lymphoblastic lymphoma; it is not currently marketed in Finland.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, with a prediction score of **99.43%**, but **no supporting clinical trials or literature** have been identified to date.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell acute lymphoblastic leukemia (T-ALL) / T-cell lymphoblastic lymphoma (T-LBL) — per known international approval; not present in Finland licensing records |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on known pharmacological information, nelarabine is a prodrug of ara-G (9-β-D-arabinofuranosylguanine), a deoxyguanosine analogue. It is dephosphorylated to ara-G, taken up preferentially by T-lymphoblasts, and phosphorylated intracellularly to the active triphosphate ara-GTP, which is incorporated into DNA and inhibits DNA synthesis, leading to selective T-cell death. It belongs to the purine nucleoside analogue (antimetabolite) class, and its efficacy in T-cell malignancies has been established through international approval.

Mechanistically, purine nucleoside analogues as a class are already clinically validated in autoimmune neurology: cladribine, a related purine analogue, is an approved disease-modifying therapy for relapsing-remitting multiple sclerosis precisely because of its selective depletion of circulating lymphocytes. Given nelarabine's comparable lymphocyte-selective cytotoxic mechanism, a repurposing hypothesis toward an immune-mediated, lymphocyte-driven disease such as RRMS is biologically plausible. However, this rationale is currently mechanistic/analogical only — it is not yet supported by any disease-specific trial or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Nelarabine currently has no marketing authorization in Finland (0 licenses on record); no product/dosage form data is available for this candidate.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine nucleoside analogue / antimetabolite) |
| Myelosuppression Risk | High — known class effect of purine analogues (neutropenia, thrombocytopenia, anemia commonly reported in published prescribing information) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential, neurological examination (peripheral and central neurotoxicity is a recognized class concern), renal and hepatic function |
| Handling Protection | Yes — standard cytotoxic drug handling precautions apply |

*Note: TFDA package insert data is a Blocking data gap; the above reflects general knowledge of the drug class, not verified local labeling. Confirm against official prescribing information before clinical use.*

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5 evidence) — no clinical trials, ICTRP registrations, or literature support this indication, and the drug is not currently marketed in Finland. The mechanistic rationale is analogical (based on a related drug class), not direct evidence.

**To proceed, the following is needed:**
- TFDA package insert / official prescribing information (currently Blocking gap)
- Confirmed DrugBank MOA data
- Any preclinical or case-level evidence linking nelarabine to demyelinating/autoimmune disease
- Formal safety profile: contraindications, key warnings, DDI data
- Periodic re-query of clinicaltrials.gov, ICTRP, and PubMed as this is a novel, unstudied indication pairing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

