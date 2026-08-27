---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 1
---

# Ketoconazole
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

# Ketoconazole: From Fungal Infections to Acne

## One-Sentence Summary

Ketoconazole is an imidazole-class antifungal agent, originally developed and marketed for the treatment of fungal infections. The TxGNN model predicts it may be effective for **Acne (Acne Vulgaris)**, with **1 clinical trial** and **15 publications** currently identified, though most of this evidence remains mechanistic, in vitro, or drawn from tangential indications rather than confirmatory acne trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (imidazole antifungal agent; specific licensed indication text not available in current dataset) |
| Predicted New Indication | Acne (Acne Vulgaris) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ketoconazole is an imidazole antifungal agent that inhibits fungal cytochrome P450-dependent 14α-demethylase, disrupting ergosterol synthesis in fungal cell membranes; its efficacy in fungal infections is well established, and mechanistically it may be applicable to acne through a distinct, non-antifungal pathway.

Acne vulgaris pathophysiology involves *Cutibacterium acnes* (formerly *Propionibacterium acnes*), a bacterium whose secreted lipase breaks down sebum triglycerides into free fatty acids that trigger follicular inflammation. In vitro evidence (PMID 28111792) demonstrates that ketoconazole directly inhibits this *C. acnes* lipase activity and also suppresses bacterial growth, offering a mechanistic link to acne that is independent of its antifungal properties. This is reinforced by a related in vitro study (PMID 20045949) showing azole antifungals have activity against *P. acnes* isolates from acne patients.

A secondary, weaker rationale comes from ketoconazole's anti-androgenic activity, which has been studied in the context of Cushing's syndrome (via levoketoconazole) and could theoretically reduce sebum production. However, this evidence is derived from a different patient population and indication, not from acne trials directly, so it should be considered supportive rather than confirmatory.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Phase NA | Active, not recruiting | 52 | Randomized comparison of topical ketoconazole 2% cream vs. topical adapalene 2% cream in mild comedonal and papulopustular acne, assessing whether ketoconazole is a viable alternative to retinoids with fewer side effects; results not yet published. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Mechanistic/In vitro | Microbiology and Immunology | Ketoconazole inhibits *P. acnes* lipase activity, a key enzyme in acne-related inflammation; proposed as a potential alternative acne treatment. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biological & Pharmaceutical Bulletin | Azole antifungals, including ketoconazole, show in vitro activity against *P. acnes* isolated from acne vulgaris patients. |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology (Basel) | Overview of systemic acne treatments; contextualizes antimicrobial approaches for papulopustular acne amid rising antibiotic resistance. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical/diagnostic study | Clinical and Experimental Dermatology | Pityrosporum (Malassezia) folliculitis is frequently misdiagnosed as acne vulgaris, highlighting a differential diagnosis relevant to antifungal therapy. |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Archives of Dermatology | Neonatal Malassezia furfur pustulosis associated with papulopustular facial eruptions resembling neonatal acne. |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | The Keio Journal of Medicine | Reviews Pityrosporum ovale-associated skin diseases, including folliculitis often confused with acne. |
| [23600337](https://pubmed.ncbi.nlm.nih.gov/23600337/) | 2013 | Review | FP Essentials | Reviews common infant skin rashes including neonatal and infantile acne. |
| [39622522](https://pubmed.ncbi.nlm.nih.gov/39622522/) | 2024 | Formulary survey | Southern Medical Journal | Analyzes dermatologic diagnosis and medication distribution patterns, including acne management, at a free clinic. |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Review | Pharmaceuticals (Basel) | Reviews adapalene, the comparator drug in NCT07237763, and its established role as first-line acne therapy. |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | BMJ Clinical Evidence | Reviews PCOS, noting acne as an associated hyperandrogenic symptom; not directly about ketoconazole treatment. |

## Finland Market Information

Ketoconazole is currently not marketed in Finland — no marketing authorization records are available in this dataset (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for ketoconazole in acne currently rests on in vitro/mechanistic studies and a single small, non-phased, still-ongoing trial (L3) — there is no completed RCT directly evaluating ketoconazole for acne. Critical safety data (warnings, contraindications, drug interactions) are entirely unavailable, which blocks even a preliminary safety assessment.

**To proceed, the following is needed:**
- Package insert warnings/contraindications and DDI data (currently a blocking data gap)
- Confirmed mechanism-of-action documentation from DrugBank
- Completed results from NCT07237763 (expected completion 2025-12)
- Additional RCT-level evidence directly evaluating ketoconazole (not levoketoconazole or Cushing's-population data) in acne vulgaris
- Formal DDI review, given known CYP3A4 interaction potential of imidazole antifungals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

