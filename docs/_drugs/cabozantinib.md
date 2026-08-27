---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-target tyrosine kinase inhibitor (MET/VEGFR1-3/RET/AXL/KIT) already approved internationally for renal cell carcinoma and other cancers, though it is not yet marketed in Taiwan. The TxGNN model predicts potential efficacy in **Liposarcoma**, currently supported by **1 clinical trial** and **1 publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (and other internationally approved oncology indications; not yet licensed in Taiwan) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Cabozantinib is a multi-target tyrosine kinase inhibitor that blocks MET, VEGFR1-3, RET, AXL and KIT, thereby suppressing tumour angiogenesis and invasive signalling. This mechanism underlies its established efficacy in renal cell carcinoma, where VEGF/MET-driven vascular signalling is a key oncogenic driver.

Soft tissue sarcomas, including liposarcoma, are also highly dependent on tumour angiogenesis for growth. TxGNN's prediction is mechanistically plausible because cabozantinib's VEGFR2 inhibition can block the vascular supply these tumours rely on, and a subset of liposarcomas has been reported to show upregulated MET expression — providing a secondary mechanistic rationale.

That said, liposarcoma is not a core indication in cabozantinib's original development programme, and current evidence comes from a broader soft-tissue-sarcoma trial rather than a liposarcoma-specific study, so the mechanistic link remains supportive rather than confirmatory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomized trial comparing ipilimumab + nivolumab alone vs. combined with cabozantinib in advanced soft tissue sarcoma; liposarcoma is among the eligible subtypes but not the sole focus, and results are not yet mature |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 | American Journal of Clinical Oncology | Neoadjuvant cabozantinib combined with radiation therapy in extremity soft tissue sarcomas; establishes safety of the combination (prior concern was fistula/perforation risk with concurrent RT), supporting activity across multiple STS subtypes |

---

## Taiwan Market Information

Cabozantinib currently holds **no marketing authorizations in Taiwan** (0 licenses on record; market status: 未上市). No product name, dosage form, or approved indication text is available from Taiwan regulatory data at this time.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: MET/VEGFR1-3/RET/AXL/KIT) |
| Myelosuppression Risk | Low to moderate — typical for VEGFR-targeted TKIs rather than classic cytotoxic chemotherapy; drug-specific haematologic toxicity data not yet available (see safety data gap below) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure, liver and renal function, urinalysis (proteinuria), wound healing status, CBC |
| Handling Protection | Oral targeted agent — standard institutional precautions for oral antineoplastic handling apply; drug-specific TFDA handling requirements are not yet confirmed |

---

## Safety Considerations

Detailed key warnings, contraindications, and drug interaction data are not yet available from TFDA sources (blocking data gap — see Conclusion). Based on the drug class and evidence referenced elsewhere in this evaluation, known class-level concerns for cabozantinib include hypertension, bleeding risk, and impaired wound healing, which should be verified against the official package insert once available.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Evidence for the liposarcoma indication currently consists of one ongoing, not-yet-mature Phase 2 trial (broader soft-tissue-sarcoma population, not liposarcoma-specific) and one Phase 1 safety study — corresponding to evidence level L2 and decision stage S1. This is preliminary rather than actionable evidence, and a blocking safety gap prevents a full initial safety assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking, required before any S1 safety evaluation (DG001)
- Confirmed mechanism-of-action data from DrugBank to strengthen the mechanistic rationale (DG002)
- Mature, subtype-specific results from NCT05836571 or a liposarcoma-focused trial
- Clarification of Taiwan regulatory/licensing pathway, since cabozantinib is not currently marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

