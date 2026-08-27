---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 3
---

# Bictegravir
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

# Bictegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome (FIV)

## One-Sentence Summary

Bictegravir has no formally recorded original indication in this evidence pack (Finland/Fimea licensing data is empty, and the official MOA field is a data gap), but literature cited within this pack identifies it as an HIV-1 integrase strand transfer inhibitor (INSTI). The TxGNN model's top prediction (rank 1) is **Feline Acquired Immunodeficiency Syndrome (FIV)**, a veterinary indication with a **99.82%** prediction score but **zero clinical trials and zero publications** supporting it — evidence level **L5 (model prediction only)**. A secondary prediction, SIV infection (rank 2), has stronger mechanistic and literature support but is also not a human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this dataset (no Fimea license records); literature evidence (PMID 32506843) identifies bictegravir as an HIV-1 integrase strand transfer inhibitor (INSTI) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) — a veterinary, non-human indication |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, literature evidence surfaced under the SIV prediction (rank 2) independently confirms that bictegravir is a second-generation integrase strand transfer inhibitor (INSTI) used to treat people living with HIV-1, with a high genetic barrier to resistance.

The rank-1 prediction links bictegravir to FIV on the basis that both HIV and FIV are lentiviruses. However, per the pack's own mechanistic assessment, FIV's integrase sequence is considerably less homologous to HIV than SIV's is, and there is no clinical trial or literature evidence of bictegravir activity against FIV integrase specifically. The assessment characterizes this as a topological artifact of the knowledge graph (integrase inhibitor ↔ lentivirus disease proximity) rather than a substantiated pharmacological signal. It is also a veterinary indication, outside the scope of human drug repurposing.

By contrast, the rank-2 prediction (SIV infection) is mechanistically closer — SIV and HIV-1 integrases are highly homologous — and is supported by in vitro/animal-model literature showing direct bictegravir antiviral activity against SIV, including resistant strains. Even so, SIV infection is a non-human (primate) disease with translational research value only, not a human clinical indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: the rank-1 FIV prediction has no supporting trials or literature. The rank-2 SIV prediction is supported by 3 publications — PMID [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/), [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/), [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) — but these describe a primate/animal-model disease, not a human indication, so they are not tabulated as clinical evidence here.)*

---

## Safety Considerations

Please refer to the package insert for safety information.

*(The TFDA/Fimea package insert warnings and contraindications are a Blocking data gap in this pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (FIV) is a veterinary indication with no clinical or literature evidence (L5) and is assessed within the pack itself as a likely false-positive driven by knowledge-graph topology rather than true pharmacological similarity. The next candidate (SIV infection) has stronger mechanistic and preclinical support (L4) but remains a non-human indication with no path to a human clinical trial. None of the three predicted indications in this pack represent an actionable human repurposing target.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the official TFDA/Fimea package insert (warnings, contraindications, DDI) — required before any S1 safety review can proceed.
- Resolve DG002 (High): obtain confirmed mechanism-of-action data from DrugBank to properly assess mechanistic plausibility of any future candidate indication.
- Establish bictegravir's original approved human indication and licensing status, since no license records exist in this dataset.
- If pursuing this drug class further, prioritize disease candidates with confirmed human clinical relevance rather than the veterinary/primate indications currently predicted.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

