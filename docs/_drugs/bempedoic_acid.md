---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Bempedoic acid is an ATP-citrate lyase (ACLY) inhibitor used to lower LDL-cholesterol. TxGNN's top-ranked predictions (hyperthyroidism, thyroid hormone resistance, two cattle diseases, CMV infection) are flagged in the evidence pack itself as likely false positives or model noise with no supporting literature — one is even a data-pairing error citing a paper about an unrelated drug. The only prediction with real supporting evidence is **Homozygous Familial Hypercholesterolemia (HoFH)** (rank 6), backed by **1 real-world cohort study** and **16 additional publications**, with a coherent mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Finland licensing data (drug not yet marketed); pharmacologically an LDL-C–lowering agent (ACLY inhibitor) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% (rank 5650 of full candidate list) |
| Evidence Level | L3 (real-world cohort study) |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on TxGNN ranking:** Ranks 1–5, 7, and 10 (hyperthyroidism, thyroid hormone receptor-β resistance, malignant catarrh, infectious bovine rhinotracheitis, CMV infection, hyperthyroxinemia, pregnancy-associated osteoporosis) all scored *higher* than HoFH but carry **no supporting clinical or literature evidence** — two are veterinary/cattle diseases, and the one literature hit (PMID 40549098) discusses a different drug (tiratricol) entirely. These are treated as model noise and excluded from further evaluation. Rank 6 (HoFH) is the only candidate with real, verifiable evidence and is the subject of this report.

---

## Why is This Prediction Reasonable?

Bempedoic acid is an ATP-citrate lyase (ACLY) inhibitor that acts upstream of HMG-CoA reductase in the cholesterol biosynthesis pathway. It is a prodrug requiring liver-specific activation by ACSVL1, which limits off-target effects to hepatic tissue. By inhibiting ACLY, it reduces hepatic cholesterol synthesis and upregulates LDL receptor (LDLR) expression, producing an LDL-C-lowering effect that is additive to statins and PCSK9 inhibitors.

HoFH is caused by biallelic loss-of-function mutations in the LDLR gene, leading to extreme, treatment-resistant LDL-C elevations from birth. Because bempedoic acid's LDL-C-lowering mechanism partly depends on LDLR upregulation, its efficacy in HoFH is mechanistically plausible but genotype-dependent: patients with residual LDLR function ("receptor-defective") are expected to respond better than those with a complete null/null genotype, a pattern also seen with statins in this population.

This mechanistic overlap — both the original indication (general/heterozygous hypercholesterolemia) and the predicted indication (HoFH) converge on the same LDL-C-lowering pathway — is the basis for the TxGNN signal, and is now supported by an initial real-world cohort study (PMID 41274797) evaluating bempedoic acid specifically in HoFH patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Cohort (Real-world) | Journal of Clinical Lipidology | Real-world evaluation of bempedoic acid efficacy and tolerability specifically in HoFH patients |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Expert Consensus | Journal of Clinical Lipidology | National Lipid Association update on FH management, reviewing current diagnostic and therapeutic advances |
| [41694628](https://pubmed.ncbi.nlm.nih.gov/41694628/) | 2026 | Case Report/Review | Clinical Case Reports | Case of catastrophic HoFH progression after interrupted follow-up, illustrating consequences of inadequate LDL-C control |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Experimental and Molecular Pathology | Reviews innovative therapies for HoFH, including LDLR-independent approaches |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol (JACC Focus Seminar) | Discusses bempedoic acid alongside inclisiran and PCSK9 inhibitors as emerging LDL-C/ApoB-lowering therapies |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiology in Review | Positions bempedoic acid among add-on lipid-lowering options for familial hypercholesterolemia |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atherosclerosis and Thrombosis | Reviews advancements in HoFH treatment, contextualizing non-statin options |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Preclinical | Arterioscler Thromb Vasc Biol | Bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR+/- and LDLR-/- miniature pigs, a direct model of the HoFH mechanism |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Preventive Cardiology | Reviews the importance of sustained LDL-C lowering across the ASCVD risk continuum |
| [32243228](https://pubmed.ncbi.nlm.nih.gov/32243228/) | 2020 | Review | Postgraduate Medicine | Reviews emerging LDL-C-lowering agents including bempedoic acid |

---

## Finland Market Information

Bempedoic acid is not currently marketed in Finland — no marketing authorizations are on record (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bempedoic acid's LDL-C-lowering mechanism (ACLY inhibition → LDLR upregulation) is directly relevant to HoFH pathophysiology, and an initial real-world cohort study now supports this use, but efficacy is expected to be genotype-dependent (limited in null/null LDLR patients) and no randomized controlled trial data yet exist specifically for HoFH.

**To proceed, the following is needed:**
- TFDA/Finnish package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed original indication and approved labeling (drug not yet marketed in Finland)
- Genotype-stratified efficacy data (receptor-defective vs. null/null) from the cited real-world cohort or future prospective trials
- Drug-drug interaction data, particularly with statins and PCSK9 inhibitors commonly co-administered in HoFH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

