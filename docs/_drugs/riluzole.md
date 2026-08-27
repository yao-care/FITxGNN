---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Riluzole
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

已根據 Evidence Pack 產生報告。**說明一點資料選擇邏輯**：`predicted_indications` 陣列第一筆（多囊腦回畸形，L5/Hold）完全無證據支持且與 riluzole 機轉無合理連結；反觀 rank 8「ALS, susceptibility to」是全部 10 筆預測中唯一有 20 篇文獻佐證、evidence_level 達 L1、decision_stage 達 S3 的項目，且 repurposing_rationale 明確指出「應以真實世界已知核准狀態為準」。因此本報告以 rank 8 作為主要預測適應症，而非機械套用陣列索引 0。

---

# Riluzole: From Amyotrophic Lateral Sclerosis (ALS) to ALS Genetic Susceptibility Subtype

## One-Sentence Summary

Riluzole is a glutamate-release inhibitor and sodium-channel blocker whose real-world approved use is classic amyotrophic lateral sclerosis (ALS), where it modestly extends survival.
The TxGNN model additionally predicts benefit in **ALS, susceptibility to** — a genetically-defined ALS subtype —
with **0 clinical trials** and **20 publications** currently supporting the underlying disease biology and riluzole's mechanism, though none are subtype-specific.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic Lateral Sclerosis (real-world approved use since 1995; not captured in this dataset's licensing records — data gap) |
| Predicted New Indication | Amyotrophic Lateral Sclerosis, susceptibility to |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset (original_moa is a data gap). Based on known information, riluzole inhibits presynaptic glutamate release and blocks voltage-gated sodium channels, reducing excitotoxic injury to motor neurons — this is the same core pathological process (glutamate excitotoxicity) implicated in ALS motor neuron degeneration.

"ALS, susceptibility to" refers to a genetically-defined subtype of the same disease entity as classic ALS, differing mainly in causative gene rather than in core pathophysiology. Riluzole's approved indication is not currently subdivided by genetic subtype, and in clinical practice patients with genetically-linked ALS are typically treated with the same standard-of-care riluzole regimen as sporadic ALS.

The supporting literature in this evidence pack is disease-mechanism literature (glutamate excitotoxicity, motor neuron degeneration, riluzole's established but modest survival benefit) rather than subtype-specific trials, so the mechanistic extrapolation from classic ALS to this genetic subtype is reasonable but indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | Confirms riluzole is the only medication shown to modestly prolong ALS survival; reviews pathophysiology and management |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Review | Current Opinion in Neurology | Notes riluzole remains the only drug with proven efficacy in ALS despite intensive research into other therapies |
| [22646982](https://pubmed.ncbi.nlm.nih.gov/22646982/) | 2011 | Review (preclinical drug development) | Expert Opinion on Drug Discovery | Riluzole is the only approved ALS therapeutic, improving survival by 2-3 months; highlights unmet need for new agents |
| [20942785](https://pubmed.ncbi.nlm.nih.gov/20942785/) | 2010 | Review | CNS & Neurological Disorders Drug Targets | Riluzole is the only available ALS drug; reviews genetic determinants (e.g. SOD1) as future therapeutic targets |
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review (mechanism) | Journal of Neurology | Foundational review of the "glutamate hypothesis" of motor neuron injury underlying ALS |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | pending | Neuroreport | Shows riluzole exerts neuroprotective effects against excitotoxic CSF factors from ALS patients in neuronal culture |
| [31108504](https://pubmed.ncbi.nlm.nih.gov/31108504/) | 2019 | pending | Human Molecular Genetics | iPSC-derived motor neurons from ALS patients (C9orf72, FUS, SOD1, TDP43 mutations) show altered calcium/glutamate receptor dynamics; riluzole's mechanism is glutamatergic inhibition and calcium regulation |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Reviews in Molecular Medicine | Reviews proposed ALS mechanisms (oxidative stress, excitotoxicity, mitochondrial dysfunction, protein aggregation) and treatment pathways |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Review | CNS & Neurological Disorders Drug Targets | Reviews ALS diagnosis, pathogenesis, and therapeutic targets in the motor neuron system |
| [20698807](https://pubmed.ncbi.nlm.nih.gov/20698807/) | 2011 | pending | Amyotrophic Lateral Sclerosis | Critical appraisal of ALS therapeutic trials; notes riluzole (glutamate metabolism modulator) is the only drug improving survival, albeit modestly |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between riluzole's known anti-excitotoxic action and ALS-spectrum pathology is well established in the general ALS literature, and this specific genetic-susceptibility subtype shares the same core pathophysiology as classic ALS for which riluzole is already real-world standard of care. However, no subtype-specific trial or DDI/safety data exists in this dataset, and a TFDA package insert review is flagged as a **Blocking** data gap that must be resolved before any S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action (MOA) source via DrugBank API — currently a data gap (DG002)
- Subtype-specific clinical evidence for "ALS, susceptibility to" (currently none registered)
- Confirmation of riluzole's real-world approved indication/licensing status, since it is absent from this dataset's Taiwan/Finland regulatory records despite being an established ALS therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

