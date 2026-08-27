---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Tegafur
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

# Tegafur: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

Tegafur is an oral fluoropyrimidine, a prodrug of 5-fluorouracil (5-FU), historically used to treat **gastric cancer**. The TxGNN model predicts strong applicability to **Colonic Neoplasm**, a prediction already backed by substantial real-world evidence — **30 registered clinical trials** (including multiple completed Phase 3 RCTs) and **20 peer-reviewed publications**, largely through the UFT (tegafur + uracil) adjuvant regimen.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (based on established pharmacology of tegafur monotherapy; formal Taiwan/Finland license text not available) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap DG002). Based on known pharmacology, tegafur is a prodrug of 5-FU, activated in the liver via CYP2A6, which inhibits thymidylate synthase and blocks DNA synthesis. It is part of the fluoropyrimidine antimetabolite class, both as monotherapy and as a component of the UFT combination (tegafur + uracil, where uracil inhibits dihydropyrimidine dehydrogenase [DPD] to increase 5-FU exposure). Its efficacy in gastric cancer has been well established, and mechanistically it extends directly to colonic neoplasm.

Gastric cancer and colonic neoplasm are both gastrointestinal malignancies that share the same pharmacological vulnerability to fluoropyrimidine-based DNA synthesis inhibition. In practice, the UFT regimen is already a standard postoperative adjuvant chemotherapy for colon cancer in multiple markets (notably Japan), meaning this is less a novel repurposing hypothesis and more a direct evidentiary extension of an already-established clinical use — which is reflected in the unusually large trial and literature base supporting this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1,608 | UFT+leucovorin vs 5-FU+leucovorin, resected stage II/III colon cancer — head-to-head confirmatory trial |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1,535 | UFT+leucovorin vs S-1 (TS-1) as adjuvant treatment for stage III colon cancer |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2,025 | UFT adjuvant chemotherapy vs observation in curatively resected stage II colon cancer |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | UFT postoperative adjuvant chemotherapy vs surgery alone, Dukes C colorectal cancer (NSAS-CC) |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | Unknown | 340 | Comparison of UFT+LV, UFT+LV/UFT, and UFT+LV+PSK/UFT+PSK regimens, stage III colorectal cancer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs capecitabine as first-line therapy in metastatic colorectal cancer |
| [NCT00439517](https://clinicaltrials.gov/study/NCT00439517) | Phase 2 | Completed | 302 | FOLFOX-4+cetuximab vs UFOX (UFT-based)+cetuximab, first-line metastatic colorectal cancer |
| [NCT02887365](https://clinicaltrials.gov/study/NCT02887365) | Phase 4 | Unknown | 300 | Tegafur-uracil as maintenance chemotherapy in stage II MSI-L/MSS colon cancer |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | Completed | 47 | UFT + cetuximab/irinotecan/oxaliplatin, first-line metastatic colorectal cancer |
| [NCT00890188](https://clinicaltrials.gov/study/NCT00890188) | Phase 2 | Unknown | 34 | UFT + thalidomide in advanced colorectal cancer after oxaliplatin-based chemotherapy |

*20 additional trials were retrieved but excluded from this table for brevity (see evidence pack for the complete list of 30).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 trial, updated 5-year survival: S-1+oxaliplatin (SOX) not superior to UFT/LV as adjuvant therapy for high-risk stage III colon cancer |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 phase III trial: SOX vs UFT/LV as postoperative adjuvant chemotherapy, high-risk stage III colon cancer |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT | Medicine | Nationwide Taiwan cohort study and meta-analysis: UFT vs 5-FU as postoperative adjuvant chemotherapy, stage II/III colon cancer |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | RCT of adjuvant immunochemotherapy (OK-432) combined with oral pyrimidines including UFT in colorectal cancer |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | RCT | Am J Clin Oncol | Comparative study of oral tegafur vs IV 5-FU in metastatic colorectal cancer |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT (Phase 3) | Ann Oncol | JFMC33-0502: randomized trial of treatment duration for UFT/LV adjuvant chemotherapy, stage IIB/III colon cancer |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT (Phase 3) | J Clin Oncol | NSABP C-06: oral UFT+LV vs IV 5-FU+LV, stage II/III colon carcinoma |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective study | Int J Clin Oncol | JFMC46-1201 final analysis: UFT/LV adjuvant treatment for high-risk stage II colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | Asian consensus adaptation of international guidelines for metastatic colorectal cancer |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT as postoperative adjuvant chemotherapy for solid tumors: clinical evidence, mechanism of action, and future direction |

*10 additional publications were retrieved but excluded from this table for brevity (see evidence pack for the complete list of 20).*

---

## Finland Market Information

Tegafur currently has **no marketing authorizations registered in Finland** (market status: 未上市 / Not Marketed, 0 licenses on file).

---

## Cytotoxicity

Tegafur is an antineoplastic agent (fluoropyrimidine class, 5-FU prodrug), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium — leukopenia/neutropenia reported across UFT-based regimens; generally milder than IV 5-FU regimens |
| Emetogenicity Classification | Low to moderate (typical of oral fluoropyrimidines) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; DPD/DPYD genotype status prior to initiation (per NCT05266300, DPYD-genotyping is used clinically to guide fluoropyrimidine dosing and avoid severe toxicity) |
| Handling Protection | Yes — must follow cytotoxic drug handling regulations despite oral route of administration |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (evidence level L1) already establish UFT/tegafur-based regimens as effective adjuvant and metastatic-setting therapy for colon cancer, giving this prediction strong external validation rather than being a purely speculative signal. However, Finland-specific regulatory status, formal MOA documentation, and safety/package-insert data remain unavailable, blocking a full safety assessment.

**To proceed, the following is needed:**
- TFDA/Fimea package insert — warnings, precautions, and contraindications (Blocking gap, DG001)
- Formal mechanism of action documentation from DrugBank or equivalent source (DG002)
- Confirmation of Finland market authorization pathway, since the drug is currently unmarketed there
- DDI dataset (current query returned "not_found") and a DPD/DPYD-based dosing safety protocol before clinical use

*Note: Nine other TxGNN-predicted indications for tegafur (e.g., cecum villous adenoma, colon leiomyoma, colonic lymphangioma) were also screened but carry evidence level L4–L5 with no or only tangential clinical/literature support and are recommended for **Hold**, not further evaluation at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

