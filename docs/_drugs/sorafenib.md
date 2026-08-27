---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Renal Cell Carcinoma/Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-kinase inhibitor originally established for renal cell carcinoma, hepatocellular carcinoma, and differentiated thyroid carcinoma. The TxGNN model predicts it may be effective for **Liposarcoma**, with **2 clinical trials** (1 sorafenib-direct) and **8 publications** currently supporting this direction, alongside nine other candidate indications of varying evidence strength (including a stronger L1/Phase 3-backed signal for unclassified renal cell carcinoma).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma / Hepatocellular carcinoma / Differentiated thyroid carcinoma (established global indications; no Fimea license record found in this dataset) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for sorafenib is not available in the structured field of this evidence pack. Based on well-established pharmacology, sorafenib is a multi-target oral kinase inhibitor that blocks RAF (including wild-type and mutant BRAF), and receptor tyrosine kinases involved in angiogenesis and tumor proliferation — VEGFR-1/2/3, PDGFR-β, FLT3, and c-KIT. This dual RAF/MEK/ERK-pathway and anti-angiogenic activity underlies its proven efficacy in renal cell carcinoma and hepatocellular carcinoma.

Soft tissue sarcomas, including liposarcoma, frequently show activation of the RAS/RAF/MEK/ERK signaling axis and are strongly dependent on tumor neovascularization — the same biological features sorafenib was designed to target. Preclinical work in dedifferentiated liposarcoma xenografts links PTEN down-regulation to a malignant, angiogenesis-dependent phenotype and to sensitivity to PI3K/RAF-pathway inhibition (PMID 23416162), providing a mechanistic bridge from sorafenib's known targets to this tumor type.

This plausibility is reinforced by clinical precedent: sorafenib's anti-angiogenic mechanism is already validated in a closely related, VEGF-driven solid tumor (renal cell carcinoma, see the separately evaluated "unclassified renal cell carcinoma" candidate, which reached L1/S3 evidence with a completed Phase 3 trial of 544 patients). The completed Phase 2 trial in advanced soft tissue sarcoma (NCT00217620, n=51) offers direct, disease-specific supporting evidence, though it has not yet been followed by a confirmatory Phase 3 study specific to liposarcoma.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY 43-9006) tested directly in advanced soft tissue sarcomas, including liposarcoma subtype; rationale based on blocking tumor-growth enzymes and tumor blood supply. Graded A (direct, same-drug evidence). |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol studying **regorafenib** (not sorafenib) across sarcoma subtypes, citing sorafenib's activity in soft tissue sarcoma as rationale. Graded C — different drug, low direct relevance to sorafenib. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | RCT (Phase 2, SWOG S0505) | Cancer | Phase 2 intergroup trial of sorafenib in advanced soft tissue sarcoma, evaluating its multitargeted kinase inhibition (RAF, VEGFR1-3, PDGFR-β, FLT3, c-KIT) in a population with limited therapeutic options. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven review of soft tissue sarcoma treatment; notes trabectedin's high activity specifically in liposarcoma and outlines targeted-therapy rationale by subtype. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Subtype-based review of soft tissue sarcoma pharmacotherapy, covering targeted agents alongside conventional cytotoxics. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Reviews patient-derived orthotopic xenograft (PDOX) models identifying effective combination therapies (e.g., with CDK inhibitor palbociclib) for sarcomas. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Annals of Surgical Oncology | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma, based on preclinical synergy between anti-angiogenic therapy and radiotherapy. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibits growth and MAPK signaling in malignant peripheral nerve sheath tumor and dedifferentiated liposarcoma (LS141, DDLS) cell lines, both Ras/Raf pathway-activated tumor types. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (xenograft) | American Journal of Pathology | Novel dedifferentiated liposarcoma xenograft models show PTEN down-regulation as a malignant signature, linking response to PI3K-pathway (and by extension RAF-pathway) inhibition. |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | Response to **trabectedin** (not sorafenib) in a synovial sarcoma patient with lung metastases; low direct relevance to sorafenib. |

## Cytotoxicity

Sorafenib is an antineoplastic agent (multi-kinase inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: RAF/MEK/ERK pathway + VEGFR/PDGFR anti-angiogenic activity) |
| Myelosuppression Risk | No myelosuppression data supplied in this evidence pack. As a class, targeted kinase inhibitors like sorafenib are typically associated with non-hematologic toxicities (hand-foot skin reaction, hypertension, diarrhea) rather than significant bone marrow suppression — please refer to the package insert for confirmed hematologic risk. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure, liver function tests, skin/dermatologic assessment, CBC |
| Handling Protection | Oral formulation — follow institutional hazardous/antineoplastic drug handling policy for oral kinase inhibitors |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial (NCT00217620) directly tests sorafenib in advanced soft tissue sarcoma including liposarcoma, supported by preclinical mechanistic evidence (PTEN/RAF pathway) and a coherent biological rationale, but no confirmatory Phase 3 data exists specific to liposarcoma — consistent with the L2/S2 evidence rating.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings, contraindications, and DDI data (currently blocking — DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A confirmatory Phase 2/3 trial or expanded case series specific to liposarcoma (current direct evidence is a single completed Phase 2 study)
- Formal safety monitoring plan given the complete absence of hematologic/toxicity data in this pack
- Note: among the 10 candidates evaluated for sorafenib, "unclassified renal cell carcinoma" carries markedly stronger evidence (L1, completed Phase 3, n=544) and may warrant separate, higher-priority evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

