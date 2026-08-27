---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 1
---

# Mometasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Mometasone: From Topical/Nasal Corticosteroid Use to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is a high-potency corticosteroid, commonly used topically and intranasally for inflammatory skin and airway conditions (specific approved indication text is not present in this dataset). The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma**, but this is currently supported only by **0 clinical trials** and **2 case-report-level publications**, with no mometasone-specific efficacy data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in dataset (mometasone is a topical/nasal corticosteroid class drug; typical uses are dermatitis/eczema and allergic rhinitis) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mometasone is not available. Based on known pharmacological information, mometasone is part of the high-potency corticosteroid class, and its anti-inflammatory/immunosuppressive efficacy in skin- and mucosa-related inflammatory conditions is well established.

Mechanistically, corticosteroids suppress cutaneous lymphocyte infiltration and reduce local cytokine release, which is the pharmacological basis for using topical steroids as skin-directed therapy in early-stage cutaneous T-cell lymphoma (CTCL)/mycosis fungoides. However, this is a **class effect** shared by all topical corticosteroids, not evidence specific to mometasone.

The TxGNN score of 99.36% likely reflects structural and mechanistic similarity inference within the corticosteroid class rather than direct clinical evidence for mometasone in CTCL. Both retrieved publications describe mometasone only as a background/failed treatment in case reports of related lymphoproliferative skin conditions (pseudolymphoma, mycosis fungoides), not as a studied intervention with efficacy outcomes — so the prediction should be treated as a research hypothesis rather than a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University Medical Center) | Case of refractory cutaneous pseudolymphoma (T-cell lymphoproliferative process mimicking CTCL); mometasone and tacrolimus were tried but unsuccessful before switching to tapinarof |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | Pediatric case of CD8+CD56+ cytotoxic mycosis fungoides (a primary cutaneous T-cell lymphoma subtype); mometasone mentioned in the clinical context of the disease, not as a proven therapeutic |

---

## Finland Market Information

Mometasone currently has no marketing authorization in Finland (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to two case reports in which mometasone appears only as a background or failed treatment, with no clinical trials, no drug-specific efficacy data, and a blocking data gap on TFDA/package-insert safety information — this falls short of what is needed even for a preliminary safety review (S1).

**To proceed, the following is needed:**
- TFDA/manufacturer package insert with warnings and contraindications (currently blocking S1 safety review)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Confirmed original approved indication(s) for mometasone
- Clinical or preclinical studies evaluating mometasone specifically (not corticosteroids as a class) in CTCL/mycosis fungoides
- Drug interaction (DDI) data, currently unavailable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

