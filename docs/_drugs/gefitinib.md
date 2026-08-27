---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival (Predicted)

## One-Sentence Summary

Gefitinib (Iressa) is globally known as a first-generation EGFR tyrosine kinase inhibitor used to treat non-small cell lung cancer (NSCLC), but this evidence pack does not itself document that original indication — a data gap flagged internally as inconsistent with real-world approval status. The TxGNN model's top-ranked prediction is **Fibromatosis, Gingival**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the pack's own mechanistic review found no plausible biological link between EGFR signaling and gingival fibromatosis pathogenesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (real-world: NSCLC — flagged internally as data gap, see DG002) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gefitinib is not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge — and corroborated by literature retrieved elsewhere in this pack (e.g. PMID 24794908, PMID 12841190) — gefitinib is a reversible, small-molecule inhibitor of the epidermal growth factor receptor (EGFR) tyrosine kinase, established worldwide as a treatment for EGFR-mutation-positive non-small cell lung cancer. This original indication is nonetheless not captured in the structured `original_indications` field of this pack, a discrepancy the pack's own rank-5 rationale explicitly flags as needing manual verification.

The top-ranked predicted indication, gingival fibromatosis, is a benign gingival overgrowth most commonly linked to SOS1/REST gene mutations or induced by drugs such as cyclosporine, phenytoin, or calcium-channel blockers. The evidence pack's own mechanistic assessment concludes there is no known overlap between EGFR signaling and gingival fibromatosis pathogenesis, and no clinical trial or literature evidence (0/0) was retrieved to support the link — this prediction appears to be a model score artifact rather than a substantiated hypothesis.

Among the ten predictions reviewed, rank #5 (lung hilum carcinoma) and rank #9 (pulmonary sulcus neoplasm) — both anatomical subtypes of NSCLC — carry meaningfully stronger mechanistic grounding, since gefitinib's EGFR-TKI activity is directly relevant to NSCLC biology. These should be treated as the more credible research questions arising from this evidence pack, rather than the top-ranked but mechanistically unsupported gingival fibromatosis prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Gefitinib is currently **not marketed in Finland** (market status: 未上市) and has **0 recorded marketing authorizations** in this evidence pack. No authorization records are available to tabulate.

---

## Cytotoxicity

Gefitinib is an antineoplastic agent (literature within this pack directly documents its use "for the treatment of chemoresistant non-small cell lung cancer patients," PMID 24794908), classified pharmacologically as a targeted small-molecule kinase inhibitor rather than conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low — as a targeted EGFR-TKI, gefitinib is not directly cytotoxic to bone marrow, unlike conventional chemotherapy agents |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (hepatotoxicity risk), pulmonary status (interstitial lung disease — PMID 20942679, 20949670), ECG/QTc (PMID 34474028, 37258113), skin toxicity (acneiform eruption — PMID 18931563), baseline CBC |
| Handling Protection | Oral hazardous-drug handling precautions recommended (avoid tablet crushing, use gloves) even though IV cytotoxic-handling protocols do not apply; confirm against official package insert once available |

Note: this table is derived from literature retrieved elsewhere in this pack, not from a structured DrugBank toxicity field. Please cross-check against the official package insert once DG001 is resolved.

---

## Safety Considerations

Please refer to the package insert for safety information.

**⚠ Note:** Key warnings, contraindications, and DDI data are all recorded as data gaps in this pack. The missing TFDA/Fimea package insert (DG001) is flagged as **Blocking** severity — it prevents any S1 safety pre-assessment and must be resolved before further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (fibromatosis, gingival) has zero clinical trial or literature support and no plausible mechanistic link per the pack's own assessment (evidence level L5). Combined with the Blocking data gap in package-insert safety data (DG001), there is no basis to advance this candidate beyond the model-prediction stage.

**To proceed, the following is needed:**
- Fimea/TFDA-approved package insert (resolves DG001 — currently Blocking)
- Confirmed original indication and mechanism-of-action data for gefitinib (resolves DG002)
- Re-validation of the TxGNN output against gefitinib's known NSCLC indication space, to distinguish genuine signal from embedding noise
- If pursuing lung-cancer-adjacent candidates instead, targeted clinical trial/literature searches on EGFR-mutation status in lung hilum carcinoma (rank #5) and pulmonary sulcus neoplasm (rank #9), which show stronger mechanistic plausibility than the current top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

