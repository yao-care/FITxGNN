---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant is the intravenous prodrug of aprepitant, an NK1 (Substance P) receptor antagonist established for preventing chemotherapy-induced nausea and vomiting (CINV). The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this ranking is currently supported by **no clinical trials and no literature** — it is a pure model-score prediction, and the evidence pack's own mechanistic review flags the biological link as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV) prevention (inferred from supporting trial/literature context; not present in structured `original_indications` field) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record (flagged as a High-severity data gap). Based on information embedded elsewhere in the evidence pack, fosaprepitant is the phosphorylated prodrug of aprepitant, and its established pharmacology is NK1 (Substance P) receptor antagonism, used clinically as an antiemetic in combination with 5-HT3 antagonists and dexamethasone for CINV prevention.

NSIAD is a distinct clinical entity caused by gain-of-function mutations in the AVPR2 (vasopressin V2) receptor, producing a water-retention/hyponatremia phenotype independent of vasopressin levels. There is no established pharmacological crosstalk between NK1/Substance P signaling and the AVPR2 pathway that drives NSIAD.

Consequently, the model's own repurposing rationale for this pairing explicitly characterizes the mechanistic link as weak ("與AVPR2功能增益型突變...無已知交互作用，機轉關聯薄弱"), and recommends this candidate be excluded from the priority research queue. The 99.92% TxGNN score should be read as a graph-embedding similarity signal only, not as biological plausibility — it is not corroborated by any trial or publication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Fosaprepitant is not currently marketed in Finland (market status: Not Marketed; total registered authorizations: 0). No product-level licensing data is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (NSIAD) has no supporting clinical trials or literature and its own mechanistic rationale describes the biological link as weak, so it does not meet the threshold to advance past model screening (S0). This is compounded by a Blocking-severity data gap (Fimea/TFDA-equivalent package insert not yet retrieved), which prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- Retrieve and parse the official package insert (labeling, warnings, contraindications) — currently a Blocking gap
- Obtain structured mechanism-of-action data from DrugBank to properly assess mechanistic plausibility
- If pursuing repurposing research on this drug, consider prioritizing rank 7 (retinitis, L4 — supported by a preclinical mechanistic study showing fosaprepitant blocks NK1/Substance P-driven ocular inflammation) over the current top-ranked NSIAD candidate, which lacks any corroborating evidence
- Independently re-verify the 3 clinical trials surfaced for "multiple endocrine neoplasia" (rank 5): all three are CINV antiemetic-support studies in patients with germ-cell/hematologic malignancies, not treatment trials for MEN — this pairing appears to be a drug/comorbidity false match rather than genuine evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

