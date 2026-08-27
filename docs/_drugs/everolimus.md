---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Unspecified Original Indication to Liposarcoma

## One-Sentence Summary

The evidence pack does not document Everolimus's original approved indication or mechanism of action (both flagged as data gaps), and the drug is currently not marketed in Finland. The TxGNN model predicts potential efficacy for **Liposarcoma**, supported by **1 clinical trial** and **5 publications**, though the strongest direct evidence so far comes from a combination regimen (everolimus + ribociclib) rather than everolimus monotherapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for everolimus is not available in this evidence pack (data gap DG002), and no original indication is documented. The supporting literature and trial records, however, consistently identify everolimus as an **mTOR (mechanistic target of rapamycin) inhibitor** — this is stated directly within the evidence pack's own repurposing rationale (e.g., for renal cell carcinoma: "Everolimus 為 mTOR 抑制劑").

The mechanistic case for liposarcoma rests on documented **Akt-mTOR and MAPK pathway activation** in dedifferentiated liposarcoma tumor specimens (PMID 26518767), providing a biological basis for mTOR-directed therapy in this tumor type. This is reinforced by an active Phase 2 trial (NCT03114527) combining everolimus with the CDK4/6 inhibitor ribociclib in dedifferentiated liposarcoma and leiomyosarcoma, built on preclinical evidence of synergistic growth inhibition when CDK4 and mTOR are co-inhibited (PMID 37967116).

Importantly, all current clinical evidence for this indication involves everolimus **as part of a combination regimen**, not as monotherapy — there is no everolimus single-agent trial or publication for liposarcoma in this evidence pack, which limits the strength of the causal link between everolimus itself and clinical benefit in this tumor type.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Evaluates ribociclib + everolimus combination in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) after ≥1 prior systemic therapy, assessing anti-tumor activity of the doublet; everolimus dosed at 2.5–5 mg/day alongside ribociclib 300 mg/day (3 weeks on/1 week off). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT | Clinical Cancer Research | Reports the SAR-096 Phase 2 trial of ribociclib + everolimus in DDL/LMS; CDK4/6 and mTOR co-inhibition showed synergistic growth inhibition in preclinical tumor models, motivating the combination trial. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Review of sarcoma patient-derived orthotopic xenograft (PDOX) models identifying effective CDK-inhibitor-based combination therapies, supporting the CDK/mTOR pathway-targeting rationale in sarcomas. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Review | Tumour Biology | Demonstrates Akt-mTOR and MAPK pathway activation in dedifferentiated liposarcoma specimens (99 cases); in vitro mTOR inhibition showed antitumor effect. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Review | Anticancer Research | Preclinical evaluation of eribulin combined with mechanistically distinct anticancer agents, including activity in liposarcoma models; not everolimus-specific. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Review | Oncogene | Identifies XPO1 inhibitor selinexor as disrupting the core transcriptional regulatory circuitry of dedifferentiated liposarcoma; a distinct, non-mTOR therapeutic vulnerability. |

---

## Finland Market Information

Everolimus currently has **no marketing authorizations on file** for Finland (market status: Not Marketed, 0 licenses recorded). No product-level licensing data is available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are available in this evidence pack (Fimea/TFDA package insert data is a blocking gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The liposarcoma prediction (L2, decision stage S2) is supported by only one ongoing, non-completed combination trial and mechanistic/preclinical literature — there is no everolimus monotherapy evidence in this tumor type. Combined with a blocking gap in safety/label data (DG001), the evidence base is not yet sufficient to advance beyond a research question.

**To proceed, the following is needed:**
- Fimea/TFDA package insert (warnings, contraindications, DDI) — required before any S1 safety pre-assessment
- Confirmed original indication and mechanism of action data for everolimus (DG002)
- Maturation/results of NCT03114527 (estimated completion 2025-12)
- Evidence distinguishing everolimus's independent contribution from the ribociclib combination effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

