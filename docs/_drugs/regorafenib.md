---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 8
---

# Regorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Regorafenib: From Colorectal Cancer/GIST/Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor originally approved for metastatic colorectal cancer, gastrointestinal stromal tumour (GIST), and hepatocellular carcinoma. The TxGNN model ranks **Liposarcoma** as its top predicted new indication (score 99.76%), but the **2 dedicated clinical trials** and **9 publications** currently available actually report that regorafenib **failed to show efficacy specifically in liposarcoma**, even though it worked in other soft tissue sarcoma subtypes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer, GIST, hepatocellular carcinoma (established global approvals cited in literature; no Finland-specific label text available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Regorafenib is an oral multi-kinase inhibitor targeting VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, and RAF-1/BRAF. This anti-angiogenic and anti-stromal mechanism is biologically plausible for soft tissue sarcomas, which are typically highly vascularized tumours, and overlaps with pazopanib, a multi-kinase inhibitor already approved for non-adipocytic soft tissue sarcoma.

However, the mechanistic plausibility does not hold up in the liposarcoma-specific data. The REGOSARC trial (NCT01900743) enrolled a dedicated liposarcoma cohort and its published results (PMID 29902612) state explicitly that regorafenib demonstrated efficacy in leiomyosarcoma, synovial sarcoma, and other non-adipocytic sarcomas **but not in liposarcoma**. The SARC024 liposarcoma cohort (NCT02048371, reported in PMID 32701199) independently confirmed this: results "do not support the routine use of regorafenib in this patient population." In other words, two separate Phase 2 trials specifically designed to test this hypothesis returned negative results for liposarcoma, even though the drug's general kinase-inhibition rationale looks sound on paper.

This is a case where the TxGNN network-based score (99.76%, rank 3120) and the raw evidence-level metric (L2, based on trial count/phase) do not capture treatment failure — both qualifying trials were completed and well-designed, but their outcome was negative for this specific tumour subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC trial; randomized, placebo-controlled study across 5 sarcoma cohorts including a dedicated Liposarcoma cohort (Cohort A), in patients previously treated with anthracycline-based chemotherapy |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 basket study of oral regorafenib across selected sarcoma subtypes, including a liposarcoma-specific cohort |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncology | REGOSARC primary results: regorafenib efficacy/safety assessed across STS subtypes in patients previously treated with anthracycline |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort: results confirm prior data and **do not support routine use of regorafenib** in treatment-refractory liposarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | Updated REGOSARC analysis with cross-over data: efficacy shown in leiomyosarcoma/synovial/other non-adipocytic sarcoma **but not liposarcoma** |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT (post-hoc) | Cancer | Q-TWiST analysis of REGOSARC trial (NCT01900743): quality-adjusted PFS benefit in doxorubicin-pretreated advanced non-adipocytic sarcoma |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial Protocol | BMC Cancer | REGOSARC study protocol; rationale based on angiogenesis signaling in sarcoma biology |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Overview of regorafenib's evolving role across STS subtypes including liposarcoma |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Review of maintenance therapy strategies after first-line treatment for advanced STS |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | RCT (different drug, anlotinib — indirect) | Anti-Cancer Drugs | Retrospective study of anlotinib in WDLS/DDLS; notes regorafenib/pazopanib as approved TKIs in non-adipocytic STS only |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Cohort (different drug, pazopanib — indirect) | Rare Tumors | Case report providing rationale for adding a Ewing sarcoma arm to SARC024 |

---

## Finland Market Information

Regorafenib currently has no marketing authorization on record in Finland (0 authorizations; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, RAF-1/BRAF) |
| Myelosuppression Risk | Low — literature on regorafenib and related TKIs highlights hand-foot skin reaction, hypertension, hepatotoxicity, and proteinuria as the dominant toxicities rather than bone marrow suppression |
| Emetogenicity Classification | Low (typical of small-molecule multi-kinase inhibitors) |
| Monitoring Items | Blood pressure, liver function tests, renal function/proteinuria, CBC, skin examination for hand-foot skin reaction |
| Handling Protection | Standard oral oncolytic handling precautions apply; not a conventional cytotoxic agent requiring cytotoxic-drug reconstitution/handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/Fimea package insert warnings and contraindications are flagged as a Blocking data gap and are not yet available for this candidate.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN ranks liposarcoma as the top predicted indication with a high score, the two dedicated Phase 2 trials that directly tested this hypothesis (REGOSARC and SARC024) both reported that regorafenib **failed to demonstrate efficacy specifically in liposarcoma**, even while showing benefit in other non-adipocytic soft tissue sarcoma subtypes. Evidence quantity (L2) is not evidence of benefit here — the qualifying data are negative.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed DrugBank mechanism of action record (currently a data gap, DG002)
- If this indication is to be reconsidered, a mechanistic explanation for why liposarcoma specifically does not respond, and whether a biomarker-selected subpopulation might still benefit
- Given the negative liposarcoma signal, evaluate whether **clear cell renal carcinoma** (rank 3, L2, "Proceed with Guardrails," with a positive single-arm Phase 2 trial in RCC) is a more promising candidate from this same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

