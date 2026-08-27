---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed (DrugBank DB00642) is a multi-targeted antifolate whose core registered use is malignant pleural mesothelioma in combination with cisplatin. The TxGNN model additionally predicts efficacy in **Malignant Peritoneal Mesothelioma**, a related but anatomically distinct mesothelial malignancy, with **11 clinical trials** and **20 publications** currently supporting this direction — though none is yet a completed randomized trial specific to this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant pleural mesothelioma (in combination with cisplatin) — the drug's core registered indication per the underlying evidence base |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is currently a data gap (flagged as DG002, High severity, in the evidence pack). However, the repurposing rationale attached to every predicted indication independently and consistently describes pemetrexed as a **multi-targeted antifolate** that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — key enzymes in de novo purine and pyrimidine biosynthesis. Blocking these pathways starves rapidly dividing tumour cells of nucleotides needed for DNA replication.

Malignant pleural mesothelioma and malignant peritoneal mesothelioma both arise from **mesothelial cells**, sharing histology, immunohistochemical markers, and molecular biology despite originating from different serosal cavities (pleura vs. peritoneum). Because pemetrexed's antifolate mechanism targets a cellular replication pathway rather than a tissue-specific target, the biological rationale for extending its established pleural-mesothelioma activity to the peritoneal counterpart is mechanistically sound.

This is reflected in real-world practice: cisplatin plus pemetrexed is already commonly used off-label as first-line systemic therapy for peritoneal mesothelioma, extrapolated from the pleural mesothelioma standard of care, and several prospective trials (including an ongoing randomized Phase 2, ICARuS II) are now formally testing this regimen in the peritoneal setting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | ICARuS II — randomized trial comparing intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC for malignant peritoneal mesothelioma |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial of carboplatin/pemetrexed/bevacizumab ± atezolizumab in neoadjuvant/palliative treatment of peritoneal mesothelioma |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib mesylate in unresectable/metastatic malignant mesothelioma, including peritoneal disease |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | MESOTIP — PIPAC plus systemic chemotherapy (alternating cisplatin/pemetrexed) vs. systemic chemotherapy alone as first-line treatment |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm study of sintilimab + bevacizumab + pemetrexed/cisplatin in unresectable malignant peritoneal mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Three-cohort trial of talazoparib maintenance following first-line platinum-based chemotherapy in pleural or peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 combined with cisplatin/pemetrexed in advanced solid tumors and pemetrexed/cisplatin-refractory mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 (arginine-depleting enzyme) with pemetrexed/cisplatin in arginine-dependent tumors, including peritoneal mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat with pemetrexed-cisplatin as first-line therapy in malignant mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | ALIMTA (pemetrexed) plus gemcitabine as front-line chemotherapy for malignant pleural or peritoneal mesothelioma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | Journal of Clinical Medicine | Comprehensive review of treatment approaches for malignant peritoneal mesothelioma, including systemic pemetrexed-based chemotherapy |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | Journal of Gastrointestinal Oncology | Diagnosis and management overview of malignant peritoneal mesothelioma |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and Peritoneum | Bidirectional chemotherapy enabling surgery and HIPEC in initially unresectable peritoneal mesothelioma |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Retrospective study | Clinical Medicine Insights. Oncology | Compares first-line pemetrexed-platinum vs. gemcitabine-platinum regimens in malignant peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Japanese Journal of Clinical Oncology | Efficacy and safety of pemetrexed plus cisplatin as first-line chemotherapy in advanced peritoneal mesothelioma |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Review of Anticancer Therapy | First-line pemetrexed plus cisplatin chemotherapy outcomes in peritoneal mesothelioma |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospective study | BMC Cancer | Efficacy of second-line treatment and prognostic factors after first-line pemetrexed/cisplatin in advanced peritoneal mesothelioma |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center retrospective study | Annals of Surgical Oncology | Treatment strategies and outcomes across a multi-center peritoneal mesothelioma population |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | Response to rechallenge with cisplatin and pemetrexed in peritoneal mesothelioma |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Case report | BMJ Case Reports | Nivolumab following pemetrexed-based chemotherapy in peritoneal mesothelioma |

---

## Finland Market Information

Pemetrexed is not currently marketed in Finland — the evidence pack records 0 authorizations on file. No product/dosage-form data is available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine-adjacent multi-targeted antifolate) |
| Myelosuppression Risk | High — antifolate chemotherapeutics of this class are well known to cause neutropenia, thrombocytopenia, and anemia; standard practice mandates folic acid and vitamin B12 supplementation to mitigate this risk. Formal package-insert-level toxicity figures are not available in this evidence pack (see DG001, Blocking) and should be confirmed before clinical use |
| Emetogenicity Classification | Low–moderate as monotherapy; the standard cisplatin-containing combination regimen is highly emetogenic due to the cisplatin component |
| Monitoring Items | CBC with differential, renal function (creatinine clearance), folate/vitamin B12 status, liver function |
| Handling Protection | Requires standard cytotoxic drug handling precautions (PPE, closed-system transfer devices, spill protocols) |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that currently prevents a full S1 safety pre-assessment and must be resolved before clinical guardrails can be finalized.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is strong (shared mesothelial origin with the drug's core pleural mesothelioma indication) and is supported by 11 clinical trials — including two actively recruiting randomized Phase 2 studies (ICARuS II, NCT05001880) — plus 20 publications, several of which report retrospective first-line efficacy of pemetrexed/cisplatin specifically in peritoneal mesothelioma. However, no completed randomized trial with peritoneal mesothelioma as the primary indication yet exists, keeping the evidence level at L3.

**To proceed, the following is needed:**
- TFDA/Finland package insert warnings, contraindications, and DDI data (DG001, Blocking — required for S1 safety clearance)
- Confirmed formal mechanism-of-action documentation from DrugBank (DG002)
- Mature results from the ongoing Phase 2 RCTs (ICARuS II, expected completion 2028; NCT05001880, expected completion 2026)
- A Finland/EU regulatory pathway assessment, since the drug is not currently marketed in Finland
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

