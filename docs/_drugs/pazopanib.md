---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

Using the drug-repurposing report template directly (no specialized skill matches this content-generation task — it's a straightforward structured-writing job with the full spec already given in the prompt). One note before the report: this Evidence Pack is unusual in that it contains **10 predicted indications** for Pazopanib rather than one, and `original_indications`/`original_moa`/Finland licensing are all empty (candidate is not yet marketed in Finland). I've adapted the template to surface the strongest candidate as the headline while still faithfully reporting the other nine, rather than mechanically reporting only `predicted_indications[0]` (Xp11.2-translocation RCC), which has **zero** supporting trials or literature — reporting it alone would understate what the pack actually shows (Dermatofibrosarcoma Protuberans has the only "Proceed with Guardrails" call, backed by a dedicated multicenter Phase 2 trial).

---

# Pazopanib: From Renal Cell Carcinoma / Soft Tissue Sarcoma to Dermatofibrosarcoma Protuberans (and Other Rare Tumor Indications)

## One-Sentence Summary

Pazopanib is an oral multi-target tyrosine kinase inhibitor (VEGFR-1/2/3, PDGFR-α/β, c-Kit) whose established oncology use — referenced throughout this evidence pack's trial context — is advanced renal cell carcinoma and non-adipocytic soft tissue sarcoma. Across **10 TxGNN-predicted indications** evaluated here, the strongest signal is **Dermatofibrosarcoma Protuberans (DFSP)**, supported by a dedicated multicenter **Phase 2 trial** (published, PMID 32956651) plus a second Phase 2a trial and case-level evidence; several other candidates (unclassified RCC, liposarcoma, fibroblastic neoplasm/desmoid-SFT) show moderate real-world and Phase 2 signal, while the remaining candidates are model-prediction-only with no supporting studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (Finland: unmarketed, 0 licenses on file). Trial context within the pack points to advanced/metastatic renal cell carcinoma and non-adipocytic soft tissue sarcoma as the established indications elsewhere. |
| Predicted New Indication (headline) | Dermatofibrosarcoma Protuberans (rank 10 of 10 by TxGNN score, but strongest evidence tier) |
| TxGNN Prediction Score | 99.29% (0.9929) |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (for DFSP specifically — see per-indication breakdown below) |

**All 10 predicted indications at a glance:**

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | RCC with Xp11.2/TFE3 fusion | 99.63% | L5 | S0 | Hold |
| 2 | RCC associated with neuroblastoma | 99.63% | L5 | S0 | Hold |
| 3 | Unclassified renal cell carcinoma | 99.63% | L2 | S2 | Research Question |
| 4 | Liposarcoma | 99.59% | L2 | S2 | Research Question |
| 5 | Childhood kidney cell carcinoma | 99.54% | L4 | S0 | Hold |
| 6 | Ovarian myxoid liposarcoma | 99.51% | L5 | S0 | Hold |
| 7 | Heart fibrosarcoma | 99.37% | L4 | S0 | Hold |
| 8 | Fibroblastic neoplasm | 99.35% | L2 | S2 | Research Question |
| 9 | Kidney fibrosarcoma | 99.33% | L5 | S0 | Hold |
| 10 | Dermatofibrosarcoma protuberans | 99.29% | L2 | **S3** | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in the trial and rationale records, Pazopanib is consistently described as a **multi-target tyrosine kinase inhibitor** acting on VEGFR-1/2/3, PDGFR-α/β, and c-Kit, with its established efficacy built on anti-angiogenic and anti-PDGFR activity in vascular- and PDGFR-driven tumors (renal cell carcinoma and non-adipocytic soft tissue sarcoma).

**Dermatofibrosarcoma Protuberans (headline indication)** is driven by the *COL1A1-PDGFB* fusion gene, which constitutively activates PDGFR signaling — the same pathway pazopanib inhibits, and the same logic that already supports imatinib's approved use in DFSP. This is a direct, mechanistically tight rationale rather than a broad tumor-type analogy, and it is the only indication in this pack with a purpose-built, published multicenter Phase 2 trial.

Several of the other candidates share a common thread: PDGFR- or VEGF-pathway-dependent mesenchymal tumors (liposarcoma, fibroblastic neoplasm/desmoid tumors and solitary fibrous tumor, non-clear-cell/unclassified RCC). These represent a coherent "class effect" hypothesis — pazopanib's known anti-angiogenic/anti-PDGFR activity extending across histologically related but formally distinct tumor types — and are backed by real-world cohorts and, in some cases, single-arm Phase 2 trials, but lack confirmatory randomized Phase 3 data. By contrast, the remaining candidates (Xp11.2/TFE3-fusion RCC, RCC associated with neuroblastoma, childhood kidney cell carcinoma, ovarian myxoid liposarcoma, heart fibrosarcoma, kidney fibrosarcoma) are extremely rare pathological entities with no direct trials or literature; two of them (childhood kidney cell carcinoma, heart fibrosarcoma) appear to reflect **ontology/label mismatches** — their only linked trials concern adult metastatic RCC and generic non-rhabdomyosarcoma soft tissue sarcoma populations, not the specific rare entity named.

---

## Clinical Trial Evidence — Dermatofibrosarcoma Protuberans

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | Phase 2a | Terminated | 23 | Multicenter trial of pazopanib in unresectable, locally advanced/metastatic DFSP, based on PDGF pathway activation via the COL1A1-PDGFB fusion gene; terminated early but provides direct prospective data. |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Preoperative chemoradiation ± pazopanib in non-rhabdomyosarcoma soft tissue sarcoma (NRSTS); may include DFSP cases but not subtype-specific. |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Risk-adapted maintenance pazopanib + dose-escalated radiation ± selinexor in NRSTS; broad population, not DFSP-specific. |
| [NCT02601209](https://clinicaltrials.gov/study/NCT02601209) | Phase 1/2 | Terminated | 151 | Sapanisertib (TAK-228) vs. pazopanib in locally advanced/metastatic sarcoma; terminated, low direct relevance to DFSP. |

---

## Literature Evidence — Dermatofibrosarcoma Protuberans

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | 2021 | Multicenter Phase 2 trial | J Invest Dermatol | Dedicated Phase 2 study of pazopanib in unresectable DFSP; evaluates efficacy/safety in a population where imatinib (also PDGFR-targeted) has established 36–80% response rates. |
| [37610680](https://pubmed.ncbi.nlm.nih.gov/37610680/) | 2023 | Translational (PDX/cell line) | Human Cell | Multi-omic profiling of imatinib-resistant DFSP with fibrosarcomatous transformation; relevant to sequencing pazopanib after imatinib failure. |
| [34066400](https://pubmed.ncbi.nlm.nih.gov/34066400/) | 2021 | Cohort | Cancers | Long-term outcomes of neoadjuvant TKI (imatinib or pazopanib) followed by surgery in locally advanced DFSP (n=27, 9 with fibrosarcomatous transformation). |
| [28515919](https://pubmed.ncbi.nlm.nih.gov/28515919/) | 2017 | Translational/pathology | Mol Clin Oncol | PD-L1 expression associated with fibrosarcomatous transformation of DFSP; case-level molecular context. |
| [27988943](https://pubmed.ncbi.nlm.nih.gov/27988943/) | 2017 | Case report | J Dermatol | Partial response to pazopanib in metastatic fibrosarcomatous DFSP without genetic translocation, refractory to prior chemotherapy regimens. |
| [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/) | 2016 | Review | Cancer | General chemotherapy review for soft tissue sarcoma, contextualizing pazopanib's place among treatment options. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | Emerging therapies for adult soft tissue sarcoma, including pazopanib. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Histological-subtype-based medical treatment of soft tissue sarcomas. |
| [22510939](https://pubmed.ncbi.nlm.nih.gov/22510939/) | 2012 | Review | Curr Opin Oncol | Review of PDGFR-inhibitor clinical trial results specifically in DFSP. |
| [37592448](https://pubmed.ncbi.nlm.nih.gov/37592448/) | 2023 | Functional/fusion-gene screen | Cancer Sci | Screen of 59 sarcoma fusion genes identifying pazopanib as a potential inhibitor of the COL1A1-PDGFB fusion gene specifically. |

---

## Additional Predicted Indications with Research-Level Evidence (L2, "Research Question")

These three candidates did not reach the "Proceed with Guardrails" bar but have meaningfully more than model-prediction-only support and may warrant monitoring or future re-evaluation.

### Liposarcoma (TxGNN score 99.59%)

Rationale caveat: pazopanib's approved soft tissue sarcoma indication (PALETTE trial) explicitly **excludes** adipocytic sarcomas, so this is a "reversal of an exclusion" hypothesis specifically requiring independent validation — not a simple label extension.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable/metastatic liposarcoma — direct, subtype-specific. |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 (randomized, double-blind) | Completed | 54 | Gemcitabine ± pazopanib in refractory soft tissue sarcoma — direct comparison including liposarcoma patients. |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Phase 3 | Active, not recruiting | 333 | INT230-6 (intratumoral) vs. US standard of care in liposarcoma/UPS/leiomyosarcoma — background reference only (non-pazopanib arm). |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Pazopanib neoadjuvant trial in NRSTS, may include liposarcoma subtypes. |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib activity/tolerability in advanced/metastatic liposarcoma after relapse. |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 trial report | Expert Opin Investig Drugs | Pazopanib in advanced intermediate/high-grade liposarcoma. |
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | Prospective Phase 2 | Cancer | Prospective Phase 2 study of pazopanib in advanced intermediate/high-grade liposarcoma. |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | Randomized Phase 2 (PAPAGEMO) | JAMA Oncol | Pazopanib ± gemcitabine in anthracycline/ifosfamide-refractory soft tissue sarcoma. |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | Preclinical (xenograft) | Transl Oncol | Pazopanib suppresses tumor growth via anti-angiogenesis in dedifferentiated liposarcoma xenograft models. |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Case report (PDOX model) | Tissue Cell | PDGFRA-amplified pleomorphic liposarcoma regressed by pazopanib in a patient-derived orthotopic xenograft. |

### Unclassified Renal Cell Carcinoma (TxGNN score 99.63%)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Completed | 544 | Sorafenib→pazopanib vs. pazopanib→sorafenib sequencing in advanced/metastatic RCC (sorafenib-led trial; indirect reference only). |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 single-arm trial | Cancer Res Treat | Direct Phase 2 evaluation of pazopanib in metastatic non-clear-cell RCC. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective multicenter (PANORAMA) | Clin Genitourin Cancer | First-line pazopanib in non-clear-cell RCC, Italian multicenter cohort. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Outcomes of metastatic non-clear-cell RCC patients treated with pazopanib. |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world cohort | Ecancermedicalscience | Sunitinib vs. pazopanib interchangeability in non-clear-cell/sarcomatoid mRCC. |

### Fibroblastic Neoplasm (desmoid tumor / solitary fibrous tumor spectrum, TxGNN score 99.35%)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) | Phase 2 | Completed | 96 | Single-agent pazopanib in solitary fibrous tumor and extraskeletal myxoid chondrosarcoma — direct, subtype-specific. |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Pazopanib neoadjuvant NRSTS trial, may include fibroblastic subtypes. |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30578023](https://pubmed.ncbi.nlm.nih.gov/30578023/) | 2019 | Multicentre single-arm Phase 2 | Lancet Oncol | Pazopanib for advanced malignant/dedifferentiated solitary fibrous tumor. |
| [25269954](https://pubmed.ncbi.nlm.nih.gov/25269954/) | 2014 | Preclinical + clinical case evidence | Eur J Cancer | Preclinical and clinical activity of pazopanib in solitary fibrous tumor. |
| [38759389](https://pubmed.ncbi.nlm.nih.gov/38759389/) | 2024 | Real-world multicenter cohort (CanSaRCC) | Eur J Cancer | Pazopanib and sorafenib real-world experience in desmoid tumors. |
| [29384266](https://pubmed.ncbi.nlm.nih.gov/29384266/) | 2018 | Cohort (AYA patients) | Pediatr Blood Cancer | Pazopanib therapy for desmoid tumors in adolescent/young adult patients. |
| [29614488](https://pubmed.ncbi.nlm.nih.gov/29614488/) | 2018 | Retrospective cohort | Oncology | Efficacy/safety of pazopanib for recurrent/metastatic solitary fibrous tumor. |

---

## Low-Evidence Indications (L4–L5, "Hold")

The remaining six candidates have no subtype-specific trials or literature, or only indirect/mismatched trial linkage. They are not recommended for further action at this time.

| Disease | Evidence Level | Key Issue |
|---------|------------------|-----------|
| RCC with Xp11.2/TFE3 fusion | L5 | No trials/literature; MiT-family translocation RCC typically shows poor response to VEGF-TKIs in general literature. |
| RCC associated with neuroblastoma | L5 | Extremely rare secondary malignancy entity; no direct evidence, pure class-analogy reasoning. |
| Childhood kidney cell carcinoma | L4 | Only linked trial (NCT01575548) is an adult metastatic RCC Phase 3 registration trial — likely an ontology/label mapping error; no pediatric safety/PK data. |
| Ovarian myxoid liposarcoma | L5 | Myxoid liposarcoma is characteristically an extremity tumor; ovarian primary site is an extremely rare presentation with no direct evidence. |
| Heart fibrosarcoma | L4 | Linked trials are generic NRSTS studies (one terminated); no cardiac-site-specific data; anti-angiogenic cardiotoxicity risk adds complexity. |
| Kidney fibrosarcoma | L5 | No trials/literature; extremely rare entity, pure class-analogy reasoning. |

---

## Finland Market Information

Pazopanib does not currently hold a marketing authorization in Finland (0 licenses on file; market status: not marketed). No product/dosage-form table is available from this evidence pack.

---

## Cytotoxicity

Pazopanib is an antineoplastic agent per its use in this evidence pack (renal cell carcinoma, soft tissue sarcoma, and the sarcoma-family indications evaluated above), but it is a **targeted small-molecule kinase inhibitor**, not a conventional cytotoxic chemotherapy agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-target tyrosine kinase inhibitor (VEGFR-1/2/3, PDGFR-α/β, c-Kit) |
| Myelosuppression Risk | Not specified in this evidence pack (DrugBank toxicity data not available). As monotherapy, generally lower myelosuppressive burden than conventional cytotoxics; risk increases materially in combination regimens seen in the trial evidence above (e.g., gemcitabine + pazopanib). Please refer to the package insert for confirmed hematologic toxicity data. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this evidence pack — notably DG001, a **Blocking**-severity gap for TFDA/Fimea package-insert warnings and contraindications, which currently prevents this candidate from entering the S1 safety pre-screen stage.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (candidate-level, driven by Dermatofibrosarcoma Protuberans; other indications carry differentiated, lower-tier recommendations — see summary table above)

**Rationale:**
- Dermatofibrosarcoma Protuberans has a mechanistically direct rationale (COL1A1-PDGFB fusion → PDGFR dependence) and a dedicated, published multicenter Phase 2 trial (PMID 32956651) plus a second prospective Phase 2a trial — the only indication in this pack reaching decision stage S3.
- Liposarcoma, unclassified RCC, and fibroblastic neoplasm/desmoid-SFT show real Phase 2 and real-world cohort signal (L2) but lack confirmatory Phase 3 data and, in liposarcoma's case, actively contradict pazopanib's current approved-indication exclusion — these remain open research questions rather than actionable candidates.
- The remaining six candidates (Xp11.2/TFE3-fusion RCC, RCC with neuroblastoma, childhood kidney cell carcinoma, ovarian myxoid liposarcoma, heart fibrosarcoma, kidney fibrosarcoma) have no direct supporting evidence and, in two cases, show signs of disease-ontology mapping errors; they should be held pending re-verification of the TxGNN disease labels against source ontologies.

**To proceed, the following is needed:**
- **Blocking:** Obtain the TFDA/Fimea package insert (warnings, contraindications) — this evidence pack cannot complete the S1 safety pre-screen without it (DG001).
- **High priority:** Confirm mechanism of action via DrugBank API to validate the mechanistic-link reasoning used throughout this report (DG002).
- Re-verify disease ontology mapping for "childhood kidney cell carcinoma" and "heart fibrosarcoma," where the only linked trials describe unrelated adult/generic populations.
- Complete route-of-administration compatibility checks (all `route_compatibility.status` fields are currently "pending" in this pack) before any go-forward indication proceeds past S3.
- For DFSP specifically: obtain post-2021 follow-up data or additional trial results, since the pivotal Phase 2 trial (PMID 32956651) and the earlier Phase 2a trial (NCT01059656, terminated) remain the only subtype-specific prospective evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

