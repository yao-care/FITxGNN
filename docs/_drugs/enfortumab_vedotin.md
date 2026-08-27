---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Enfortumab Vedotin: From Urothelial (Bladder) Cancer to Leprosy

## One-Sentence Summary

Enfortumab vedotin is a Nectin‑4 targeted antibody‑drug conjugate (ADC) carrying the microtubule‑inhibitor payload MMAE, developed and used in the treatment of advanced urothelial (bladder) cancer — though this original indication is **not directly recorded** in the current evidence pack (`original_indications` is empty; only inferred from associated literature context). The TxGNN model's top-ranked new prediction, **Leprosy**, has a very high similarity score but **zero supporting clinical trials or literature**, and the evidence pack's own mechanistic review explicitly concludes there is **no plausible biological link** between the drug's mechanism and *Mycobacterium leprae* infection. This candidate should be treated as a model-only signal, not a validated repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (`original_indications` empty); literature context (PMID 41341429) associates enfortumab vedotin ADCs with **bladder/urothelial cancer** — unconfirmed, pending DrugBank/label verification |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Finland Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (Data Gap DG002, High severity). Based on information embedded elsewhere in this evidence pack, enfortumab vedotin is described as a **Nectin‑4 targeted antibody‑drug conjugate**, whose payload MMAE (monomethyl auristatin E) is a microtubule inhibitor that acts on cancer cell mitosis — consistent with its known role as an ADC used in oncology.

For the top-ranked prediction, **leprosy**, the evidence pack's own repurposing rationale explicitly states there is **no reasonable mechanistic link**: leprosy is driven by *Mycobacterium leprae* infection and its associated immune/neural pathology, which has no known intersection with Nectin‑4 expression or microtubule-targeted cytotoxicity. The rationale itself notes the high TxGNN score more likely reflects an indirect node connection within the knowledge graph rather than a genuine biological mechanism.

This concern is reinforced by the quality of the broader prediction batch: of the nine ranked indications returned, **all nine are rated L5/S0/Hold**, two (rank 8 "infectious bovine rhinotracheitis" and rank 9 "malignant catarrh") are **veterinary diseases in cattle/ruminants**, explicitly flagged in the evidence pack as likely species-confusion artifacts in the knowledge graph, and one (rank 4, candidiasis) is supported only by a pharmacovigilance study describing candidiasis as an **adverse safety signal** of ADC-induced immunosuppression, not a treatment indication. Taken together, this pattern suggests the current prediction set for this drug reflects graph-level noise more than credible pharmacological hypotheses, and none of the top candidates — including leprosy — currently rises above a speculative, model-only signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: literature evidence exists elsewhere in this dataset for a different candidate indication — rank 4, "candidiasis," PMID 41341429 — but this concerns an ADC-class safety signal, not leprosy, and is discussed under Safety Considerations below.)*

---

## Finland Market Information

No marketing authorization currently registered in Finland (`total_licenses: 0`). Enfortumab vedotin is not currently marketed in this jurisdiction.

---

## Cytotoxicity

Enfortumab vedotin is an antibody-drug conjugate with a cytotoxic microtubule-inhibitor payload, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Antibody-Drug Conjugate) delivering a conventional cytotoxic payload (MMAE, microtubule/mitosis inhibitor of the auristatin class) |
| Myelosuppression Risk | Not formally quantified in this evidence pack. A related pharmacovigilance literature signal (PMID 41341429, rank-4 candidiasis rationale) associates ADC therapy with neutropenia/immunosuppression manifesting as opportunistic infection — please refer to the package insert for confirmed data |
| Emetogenicity Classification | Not available in evidence pack — please refer to the package insert |
| Monitoring Items | CBC with differential (particularly neutrophil count), signs/symptoms of infection, liver and renal function |
| Handling Protection | Cytotoxic drug handling precautions should apply given the MMAE payload; confirm specific protocol against the package insert |

---

## Safety Considerations

Formal package insert data (key warnings, contraindications, DDI) is a **Blocking** data gap (DG001) — TFDA/manufacturer labeling has not yet been retrieved, so a full safety review cannot be completed at this time. Drug interaction screening also returned no results (`ddi.query_status: not_found`), which reflects absence from the queried database rather than a confirmed absence of interactions.

One relevant signal was identified in adjacent literature: a 2025 real-world FAERS pharmacovigilance study of ADCs in bladder cancer (PMID 41341429) reports safety signals including opportunistic infections such as candidiasis, plausibly related to ADC-induced immunosuppression or neutropenia. This should be treated as a risk to monitor, not a treatment indication.

Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no supporting clinical trials or literature, is explicitly assessed by the evidence pack's own mechanistic analysis as lacking a plausible biological rationale, and sits within a prediction batch where all nine ranked indications are L5/Hold — two of which appear to be veterinary-disease artifacts. Combined with a Blocking-severity gap in package insert/safety data (DG001) and the drug's non-marketed status in Finland, there is currently no basis to advance this candidate beyond model screening.

**To proceed, the following is needed:**
- TFDA/EMA package insert data (warnings, contraindications, DDI) — DG001, Blocking
- Confirmed mechanism of action and original indication via DrugBank/regulatory label — DG002, High
- Preclinical or biological plausibility data specifically linking Nectin‑4/MMAE activity to *M. leprae* infection or leprosy pathophysiology, if this hypothesis is to be pursued further
- A data-quality review of the broader TxGNN prediction batch for this drug, given the presence of veterinary-disease entries (ranks 8–9) suggesting possible knowledge-graph node confusion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

