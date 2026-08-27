---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Amifampridine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

> Amifampridine is a voltage-gated potassium channel blocker whose established pharmacological use is in **Lambert-Eaton Myasthenic Syndrome (LEMS)**, though it currently holds **no marketing authorization in Taiwan**.
> The TxGNN model predicts it may be effective for **Glaucoma** (score 99.71%), with a secondary, lower-confidence signal for **Acute Intermittent Porphyria** (score 99.32%).
> Neither prediction is currently supported by any clinical trials or published literature — this is a **model-prediction-only (L5)** signal, and a **Blocking data gap** on TFDA package-insert safety data prevents any formal safety screening at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lambert-Eaton myasthenic syndrome (LEMS) — noted in the model's mechanistic rationale as the drug's known use; not confirmed via Taiwan license data, since the product is not marketed in Taiwan |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% (rank 3737) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for amifampridine is a confirmed data gap in this evidence pack (DG002, High severity). Based on the model's own mechanistic rationale, amifampridine is known as a voltage-gated potassium channel blocker that acts at the neuromuscular junction to increase acetylcholine release — the basis of its established use in LEMS.

For the top-ranked prediction, **glaucoma**, the pathological core is an imbalance between aqueous humor production and outflow that raises intraocular pressure (IOP). Ion channels — including K⁺ channels — in the ciliary body epithelium do participate in regulating aqueous humor secretion, which is the theoretical basis for the model's link between the two conditions.

However, this connection is stated in the evidence pack itself as a **class-level, indirect analogy only**: there is no ophthalmic pharmacology, preclinical, or clinical evidence showing that amifampridine directly affects IOP or aqueous humor dynamics. Combined with the missing original-MOA data, the mechanistic link should be treated as a purely predictive hypothesis (L5), not a validated pharmacological rationale.

### Secondary Prediction: Acute Intermittent Porphyria (Score 99.32%, Rank 6919)

Acute Intermittent Porphyria (AIP) results from porphobilinogen deaminase deficiency disrupting heme biosynthesis, with acute attacks presenting as neuro-visceral symptoms (abdominal pain, peripheral neuropathy, autonomic dysfunction). The model's rationale draws only a **symptomatic-level analogy**: amifampridine's known neuromuscular-transmission-enhancing effect could theoretically offer symptomatic benefit for AIP-related neuropathy, but this has **no mechanistic connection** to the underlying enzymatic defect in heme synthesis (e.g., no evidence it modulates ALA synthase activity). This link is explicitly the weakest of the two and should be considered a surface-level analogy rather than a pharmacological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for either predicted indication (glaucoma or acute intermittent porphyria).

---

## Literature Evidence

Currently no related literature available for either predicted indication (glaucoma or acute intermittent porphyria).

---

## Taiwan Market Information

Amifampridine currently holds **no marketing authorization in Taiwan** (market status: 未上市, total authorizations: 0). No approved indication text, dosage form, or license data is available for this product in Taiwan.

---

## Safety Considerations

Taiwan/TFDA package-insert data on warnings and contraindications for amifampridine has not yet been obtained (data gap DG001, **Blocking severity**) — this currently prevents the candidate from entering the S1 safety pre-screening stage. Drug-drug interaction data was queried but not found (0 interactions on file).

Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications rest solely on a TxGNN model score (L5, no clinical or literature evidence), and a Blocking-severity data gap on TFDA safety/package-insert information means the candidate cannot yet complete even initial safety screening (S1). The drug also has no existing Taiwan market presence to anchor a regulatory pathway.

**To proceed, the following is needed:**
- TFDA package-insert data (warnings, contraindications) — required to clear the Blocking gap (DG001) before any safety review
- Confirmed mechanism-of-action data from DrugBank or primary pharmacology literature (DG002)
- Preclinical or mechanistic studies specifically testing amifampridine's effect on aqueous humor dynamics / intraocular pressure (for the glaucoma hypothesis)
- Any case reports, preclinical data, or trials addressing amifampridine use in porphyria-related neuropathy (for the AIP hypothesis)
- Validated drug-drug interaction data (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

