---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 2
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a neuraminidase inhibitor used against influenza A and B infection. The TxGNN model's top prediction suggests possible efficacy for **Pyelonephritis**, but this pairing currently has **0 clinical trials** and **0 supporting publications** — the model's own rationale flags it as likely graph noise rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza A/B (inferred from the pharmacological classification described in the supporting literature within this evidence pack — no Fimea-approved indication text is available; see Market Status) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (data gap, high severity). Based on the pharmacological classification captured in the accompanying literature, zanamivir is a neuraminidase inhibitor that blocks release of influenza A/B virus particles from infected host cells — a narrowly targeted antiviral mechanism, not a broad-spectrum one.

Pyelonephritis is a bacterial upper urinary tract infection. There is no established pathway linking viral neuraminidase inhibition — or any host sialidase-mediated process — to bacterial pyelonephritis pathogenesis. The TxGNN score of 99.84% reflects graph-embedding similarity only; it is not accompanied by a single clinical trial or publication.

The model's own repurposing rationale for this pair explicitly states the connection is unsupported and likely represents knowledge-graph noise/a false positive rather than a plausible biological signal. Given the complete absence of corroborating evidence and the clear mechanistic mismatch, this pairing does not currently meet the bar for further mechanistic investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Zanamivir currently holds no marketing authorization in Finland (market status: 未上市 / Not marketed). No license records exist to list.

---

## Additional Predicted Indication (Rank 2): Disorder of Tyrosine Metabolism

For completeness, a second candidate was returned by the model:

| Item | Content |
|------|------|
| TxGNN Prediction Score | 99.02% (rank 9324) |
| Evidence Level | L5 |
| Recommended Decision | Hold |

Three PubMed records were returned by the automated search, but none actually concern tyrosine metabolism disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23675925](https://pubmed.ncbi.nlm.nih.gov/23675925/) | 2013 | Review | Infectious Disorders Drug Targets | Oseltamivir resistance surveillance (H275Y neuraminidase mutation) — not related to tyrosine metabolism |
| [25727669](https://pubmed.ncbi.nlm.nih.gov/25727669/) | 2015 | Methodology | J Mol Recognit | SPR assay for neuraminidase inhibition sensitivity (zanamivir/oseltamivir vs. H274Y mutant) — assay development, not disease-relevant |
| [21367898](https://pubmed.ncbi.nlm.nih.gov/21367898/) | 2011 | Basic virology | J Virology | N294S neuraminidase mutation and H5N1 pathogenicity — unrelated to tyrosine metabolism |

These were most likely matched through incidental term overlap (e.g., "tyrosine" appearing in neuraminidase mutation nomenclature such as H274Y/N294S) rather than genuine disease relevance. No known pathway connects viral neuraminidase inhibition to endogenous tyrosine-metabolizing enzymes (e.g., FAH, TAT, HPD). This candidate should also be held.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both candidate indications are graded L5 (model prediction only), with zero supporting clinical trials and no genuinely relevant literature — the model's own mechanistic rationale identifies both pairings as likely false positives rather than credible repurposing signals.

**To proceed, the following is needed:**
- Retrieve TFDA/Fimea package insert warnings and contraindications (currently a **blocking** data gap)
- Obtain confirmed mechanism-of-action data from DrugBank (high-severity data gap)
- Identify any literature or preclinical studies that specifically link zanamivir to pyelonephritis or tyrosine-metabolism pathways — none currently exist
- If no genuine supporting evidence emerges, deprioritize this candidate pair in favor of higher-evidence-level TxGNN predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

