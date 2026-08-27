---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: From Anti-PD-1 Cancer Immunotherapy to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab is a PD-1 immune checkpoint inhibitor whose established use — per the literature captured across this evidence pack — is in advanced malignancies such as non-small cell lung cancer, melanoma, and other solid tumors. TxGNN's top-ranked prediction for this drug is **Gingival Fibromatosis**, a benign fibroproliferative condition, but this signal is currently supported by **0 clinical trials** and **0 publications**, with the model's own mechanistic annotation noting no known biological pathway connecting PD-1 blockade to this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented via Finland regulatory data (no marketing authorization on file); literature evidence in this pack characterizes pembrolizumab as an anti-PD-1 antibody used in advanced NSCLC, melanoma, and other solid tumors |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.40% (rank 6326 of all candidates) |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action record for pembrolizumab is currently a data gap in this evidence pack (flagged as a High-severity gap, DG002). Based on the literature evidence gathered elsewhere in this pack, pembrolizumab is a humanized monoclonal IgG4 antibody that blocks the PD-1/PD-L1 checkpoint, restoring T-cell–mediated anti-tumor immune activity — a mechanism validated across numerous Phase 3 trials in NSCLC (KEYNOTE-024, KEYNOTE-010) and other cancers.

Gingival fibromatosis, however, is a benign disorder driven by fibroblast proliferation and excess collagen deposition in gingival tissue — it is not a malignancy and has no described dependence on tumor immune evasion or PD-1/PD-L1 signaling. The evidence pack's own mechanistic annotation for this candidate states there is no known pathway overlap between checkpoint blockade and this condition, and the TxGNN score is not corroborated by any registered trial or publication.

Taken together, this ranks as a **model-generated signal without biological or empirical support**, most plausibly reflecting network-level prediction noise rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Pembrolizumab is **not marketed in Finland** — the evidence pack lists 0 authorizations, so no product/authorization table can be generated.

---

## Cytotoxicity

Pembrolizumab is an antineoplastic agent (immune checkpoint inhibitor), based on the extensive oncology literature attached to other candidates in this evidence pack (e.g., KEYNOTE-024, KEYNOTE-010 in NSCLC).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a monoclonal antibody biologic, standard cytotoxic drug handling protocols (spill/PPE for small-molecule chemotherapy) do not directly apply; follow institutional biologic-handling and infusion-monitoring procedures per package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Gingival Fibromatosis) has no supporting clinical trials or literature (L5 — model prediction only), and the pack's own rationale identifies no plausible mechanistic link between PD-1 blockade and this benign condition. Combined with the unresolved Blocking-severity safety data gap (DG001: TFDA label/warnings) and High-severity MOA gap (DG002), this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/Finland package insert warnings and contraindications) before any safety pre-assessment
- Resolve DG002 (formal DrugBank MOA record) to support mechanistic review
- If repurposing pembrolizumab remains of interest, redirect evaluation toward the two candidates in this batch with actual signal — **lung hilum carcinoma** (rank 4, L4, decision stage S1, "Research Question," though one supporting case report shows a hyperprogression signal requiring caution) and **lung germ cell tumor** (rank 8, L3, S1, "Research Question," 50 trials/20 publications, though none disease-specific) — rather than this rank-1 candidate
- Independent review of the TxGNN batch output is advisable, since several of the top-10 ranked candidates in this evidence pack were flagged by the model's own annotations as mechanistically implausible or as label/evidence mismatches
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

