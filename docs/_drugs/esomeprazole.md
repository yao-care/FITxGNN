---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 3
---

# Esomeprazole
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

# Esomeprazole: From Acid-Related Gastrointestinal Disorders to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI), the S-isomer of omeprazole, established for treating acid-related gastrointestinal disorders such as peptic ulcer, H. pylori infection, GERD, and NSAID-induced GI lesions. The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, but this direction is currently supported only by **1 general review article** and **no disease-specific clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no market authorization or approved indication text on file for this registry |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate is not available (Data Gap). Based on the supporting literature in this evidence pack, esomeprazole belongs to the proton pump inhibitor (PPI) class, which irreversibly inhibits the H+/K+-ATPase on gastric parietal cells to suppress acid secretion; its efficacy in acid-related disorders (peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions, Zollinger-Ellison syndrome) is well established.

However, the mechanistic link to duodenogastric reflux is explicitly assessed as weak in this evidence pack. Duodenogastric reflux is primarily caused by bile and pancreatic enzyme reflux into the stomach — a non-acidic/alkaline injury mechanism. Esomeprazole only suppresses gastric acid secretion and has no direct pharmacological action on bile reflux itself; it can at most indirectly alleviate the acidic component of mucosal damage in mixed-type reflux. The high TxGNN score should therefore be interpreted as an indirect inference from the drug's broader acid-suppression profile, not evidence of a direct therapeutic target.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General update on PPI clinical use (peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions, Zollinger-Ellison syndrome); not specific to duodenogastric reflux |

## Finland Market Information

No market authorization on file — this drug is currently not marketed under this registry (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but the mechanistic link to duodenogastric reflux is indirect (acid suppression vs. bile-driven injury), and the evidence base consists of a single general PPI review with no disease-specific clinical trials — evidence level L4 does not meet the threshold to advance.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (currently Data Gap, blocking S1 safety pre-assessment)
- TFDA/regulatory package insert (warnings, contraindications, DDI)
- Preclinical or mechanistic studies specifically addressing bile/alkaline reflux modulation
- Disease-specific clinical evidence for duodenogastric reflux before re-scoring

**Note on other candidates in this evidence pack:** Rank 3 ("duodenal ulcer") shows much stronger evidence (L1, 50 trials, 20 publications) but its own rationale flags that this is esomeprazole's well-established, already-approved PPI indication rather than a genuine repurposing candidate — the empty `original_indications` field is itself a data gap, not evidence of novelty. Rank 2 ("duodenal obstruction") has no supporting trials or literature and reflects a mechanistic mismatch (structural obstruction vs. pharmacological acid suppression); it should remain on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

