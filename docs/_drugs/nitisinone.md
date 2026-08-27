---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

Using the report template above (this is a direct content-generation task from the given Evidence Pack — no coding/skill workflow needed).

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone (NTBC) is an HPPD inhibitor used as the standard treatment for hereditary tyrosinemia type 1 (HT-1).
The TxGNN model predicts it may also be effective for **Renal Tubular Acidosis**,
with **0 clinical trials** and **2 publications** currently supporting this direction — evidence is preliminary and limited to HT-1-associated cases.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (HT-1) — noted in repurposing rationale; not confirmed via a structured MOA/indication field (data gap) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not confirmed in a structured field (DrugBank MOA lookup is flagged as a data gap). Based on known pharmacology, nitisinone is an HPPD (4-hydroxyphenylpyruvate dioxygenase) inhibitor and is the standard treatment for hereditary tyrosinemia type 1 (HT-1), a rare inherited disorder of tyrosine metabolism.

Renal tubular dysfunction — which can present as proximal renal tubular acidosis or Fanconi syndrome — is a well-recognized complication of untreated HT-1, caused by accumulation of the toxic metabolite succinylacetone. Published cohort data show that nitisinone therapy improves renal tubular function in HT-1 patients, which is mechanistically consistent with the TxGNN prediction.

Importantly, this evidence supports nitisinone's benefit for renal tubular acidosis **secondary to HT-1**, not renal tubular acidosis of general or unrelated etiology. Any downstream indication should be scoped specifically to "HT-1-associated" renal tubular dysfunction rather than a broad renal tubular acidosis label.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort | Molecular Genetics and Metabolism | Describes early effect of NTBC on renal tubular dysfunction in HT-1 patients; renal tubular disease is a recognized HT-1 complication that has been poorly studied prior to this work |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case Series | Indian Journal of Gastroenterology | Case series of 4 children with tyrosinemia treated with NTBC; 3 patients maintained normal liver function and undetectable urine succinylacetone with no renal tubular complications on long-term NTBC therapy |

## Finland Market Information

Nitisinone is currently **not marketed** in Finland (0 authorizations on record), so no marketing-authorization details are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic plausibility is strong (HT-1-associated renal tubular dysfunction is a well-documented complication that improves with NTBC), but supporting evidence is limited to one cohort study and one case series — no RCTs or registered clinical trials exist for this specific indication, and the drug is not currently marketed in Finland.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a blocking data gap
- Structured DrugBank MOA confirmation
- Drug-drug interaction data (current DDI query returned no results)
- Clarification that the target indication is scoped to HT-1-associated renal tubular acidosis, not general-etiology cases
- Finland marketing authorization / import pathway assessment given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

