---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From an Undocumented Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel's original approved indication is not captured in this evidence pack (Finland market status: **not marketed**, 0 authorizations on file), so it cannot be stated with certainty here.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, and this direction is already backed by **50 clinical trials** and **20 publications** in the evidence pack — reflecting the fact that paclitaxel is a globally established taxane chemotherapy already used in breast cancer regimens.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap — DrugBank/TFDA records empty) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% (rank #82) |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for paclitaxel is not available in this record (flagged as a High-severity data gap, DG002). Based on the repurposing rationale captured in the evidence pack, paclitaxel is a taxane-class microtubule-stabilizing agent: it inhibits spindle depolymerization, causing mitotic arrest and apoptosis in rapidly dividing cells. This mechanism is well validated clinically in high-proliferation tumors.

Female breast carcinoma is a classic high-mitotic-rate solid tumor, and this microtubule-stabilization mechanism is independent of hormone-receptor or HER2 status — which is consistent with paclitaxel already being one of the most extensively studied cytotoxic backbones in breast cancer regimens worldwide (both as monotherapy and combined with trastuzumab, lapatinib, or platinum agents).

Because original-indication data is missing from this specific record (and the drug shows as not marketed in Finland), this prediction functions less as a novel mechanistic leap and more as **confirmation of an already-established global indication** that happens to be absent from the local regulatory record on file.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | Completed | 444 | Lapatinib + Paclitaxel vs. Placebo + Paclitaxel in ErbB2-amplified metastatic breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Chemotherapy (incl. weekly paclitaxel) ± trastuzumab in node-positive/high-risk HER2-low breast cancer |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2005 | Sequential doxorubicin, paclitaxel, cyclophosphamide vs. concurrent AC→paclitaxel in node-positive stage II/IIIA breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FE75C→docetaxel vs. paclitaxel as adjuvant therapy in node-positive breast cancer |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Phase 3 | Completed | 725 | ABP 980 vs. trastuzumab (both with paclitaxel backbone context) in HER2-positive early breast cancer |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Completed | 280 | FEC-75→paclitaxel+trastuzumab vs. paclitaxel+trastuzumab→FEC-75 in HER2-positive operable breast cancer |
| [NCT00016276](https://clinicaltrials.gov/study/NCT00016276) | Phase 3 | Terminated | 396 | AC±dexrazoxane followed by weekly paclitaxel±trastuzumab in HER2+ stage IIIA–IV breast cancer |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Completed | 200 | Paclitaxel + trastuzumab adjuvant therapy for HER2-overexpressing stage II/IIIA breast cancer |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Terminated | 63 | Paclitaxel + trastuzumab + lapatinib vs. + placebo in ErbB2-overexpressing metastatic breast cancer |
| [NCT04753177](https://clinicaltrials.gov/study/NCT04753177) | Phase 2/3 | Unknown | 120 | Neoadjuvant combined hormone therapy in premenopausal ER+/HER2- locally advanced breast cancer |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort | Cancer | Doxorubicin + paclitaxel efficacy/toxicity in metastatic breast cancer; importance of prior adjuvant anthracycline exposure |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Paclitaxel's mechanistic and clinical effects on breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review of paclitaxel and docetaxel efficacy in breast and ovarian cancer |
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | Randomized trial | Cancer | GONO trial: concomitant vs. sequential epirubicin + paclitaxel as first-line therapy in metastatic breast carcinoma |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclinical | Chemical Biology & Drug Design | Paclitaxel combination therapeutic potential against breast carcinoma with in vivo biomarker identification |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | — | Journal for ImmunoTherapy of Cancer | Paclitaxel's effect on tumor-associated macrophages enhancing PD-1 blockade in TNBC |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | — | BioMed Research International | Real-world efficacy of neoadjuvant epirubicin/cyclophosphamide + weekly paclitaxel/trastuzumab in HER2+ breast carcinoma |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | — | Nature Communications | TEKT4 germline variations associated with breast cancer resistance to paclitaxel |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | — | Molecular Pharmacology | Reversal of stathmin-mediated resistance to paclitaxel and vinblastine in breast carcinoma cells |
| [14508823](https://pubmed.ncbi.nlm.nih.gov/14508823/) | 2003 | — | Cancer | Combined trastuzumab + paclitaxel inhibits ErbB-2-mediated angiogenesis via Akt more effectively than either agent alone |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane class, microtubule-stabilizing agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for female breast carcinoma is strong (L1, 50 trials including multiple completed Phase 3 RCTs with N>400, plus 20 supporting publications), but this specific evidence pack has a **Blocking** data gap on TFDA/Finland package-insert warnings and contraindications (DG001) and a **High**-severity gap on formal MOA documentation (DG002), and the drug is currently recorded as not marketed in Finland.

**To proceed, the following is needed:**
- TFDA/Finland package insert (warnings, contraindications) — required before any S1 safety review can proceed
- Confirmed DrugBank-sourced mechanism-of-action documentation
- Confirmation of Finland marketing authorization status (or a pathway/timeline to market entry)
- Drug interaction (DDI) data, currently returned as "not found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

