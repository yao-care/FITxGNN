---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 1
---

# Olaparib
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

Using the drug-repurposing-report format directly (this is a single deterministic formatting task, no ambiguity requiring brainstorming/other skills).

# Olaparib: From Ovarian Cancer to Breast Cancer

## One-Sentence Summary

> Olaparib is an oral PARP1/2 inhibitor originally developed for BRCA-mutated, platinum-sensitive ovarian cancer.
> The TxGNN model predicts it may also be effective for **female breast carcinoma**,
> with **50 clinical trials** and **20 publications** currently supporting this direction, including two pivotal completed Phase 3 RCTs (OlympiAD, OlympiA).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer, BRCA-mutated (per international approval; not confirmed in Finnish labeling — see Data Gap below) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from the drug label is not available (data gap). Based on the evidence pack's repurposing rationale, olaparib is a PARP1/2 (poly ADP-ribose polymerase) inhibitor that acts through **synthetic lethality**: in tumor cells with BRCA1/BRCA2 mutations or other homologous recombination deficiency (HRD), blocking PARP-mediated single-strand DNA repair leads to accumulation of unrepaired double-strand breaks and cell death.

Olaparib's original use was in BRCA-mutated, platinum-sensitive ovarian cancer, where this synthetic-lethality mechanism is well established. BRCA1/2 mutations drive both ovarian and breast cancer through the same defective homologous-recombination-repair biology, so the mechanistic link between the two indications is direct rather than speculative — it is not an analogy across unrelated tumor types but the same molecular vulnerability expressed in a different tissue.

This is reflected in the maturity of the evidence: olaparib is already internationally approved (FDA/EMA) for gBRCA-mutated, HER2-negative breast cancer (both adjuvant and metastatic settings), supported by two independent, completed Phase 3 RCTs — OlympiAD (metastatic setting) and OlympiA (adjuvant, early-stage, high-risk setting). This substantially strengthens confidence in the TxGNN prediction beyond a purely model-driven signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | OlympiAD: olaparib vs. physician's-choice chemotherapy in gBRCA-mutated, HER2-negative metastatic breast cancer — pivotal registration trial |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1/2 | Completed | 25 | Carboplatin-olaparib sequential therapy vs. capecitabine as first-line treatment in BRCA1/2-mutated, HER2-negative advanced breast cancer |
| [NCT03402841](https://clinicaltrials.gov/study/NCT03402841) | Phase 3b | Completed | 279 | Single-arm maintenance olaparib in platinum-sensitive relapsed non-gBRCA ovarian cancer; supportive real-world efficacy/safety data |
| [NCT02503436](https://clinicaltrials.gov/study/NCT02503436) | N/A | Completed | 276 | C-PATROL: prospective non-interventional study collecting real-world effectiveness/safety data in BRCA-mutated ovarian cancer |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | AZD2281 (olaparib) in BRCA-mutated/recurrent ovarian cancer and BRCA-mutated/triple-negative breast cancer; early proof-of-concept for later Phase 3 trials |
| [NCT03162627](https://clinicaltrials.gov/study/NCT03162627) | Phase 1 | Active, not recruiting | 90 | Selumetinib + olaparib combination in Ras-altered/PARP-resistant solid tumors including breast cancer; early dose-finding, not breast-specific |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Active, not recruiting | 185 | ROSY-O rollover study providing continued olaparib access and long-term safety follow-up, not an efficacy endpoint trial |
| [NCT06545942](https://clinicaltrials.gov/study/NCT06545942) | Phase 1 | Active, not recruiting | 220 | MOMA-313 alone or combined with a PARP inhibitor in HRD-positive advanced/metastatic solid tumors |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Phase 2 | Recruiting | 2900 | ComboMATCH: genomically-directed basket trial platform; breast cancer is one of multiple sub-cohorts |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Phase IV trial in Indian patients with platinum-sensitive ovarian cancer and gBRCA1/2-mutated metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib significantly improves invasive disease-free survival in gBRCA1/2-mutated, high-risk early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall survival follow-up confirming durable benefit of adjuvant olaparib in gBRCA1/2-mutated early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib shows antitumor activity in gBRCA-mutated metastatic breast cancer, establishing the pivotal efficacy signal |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final overall survival and tolerability results vs. chemotherapy in gBRCA-mutated HER2-negative metastatic breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD extended follow-up: median OS 19.3 vs. 17.1 months for olaparib vs. chemotherapy, reaffirming safety profile |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT | J Clin Oncol | TBCRC 048 Phase 2: olaparib activity in metastatic breast cancer with somatic BRCA or other HR-related gene mutations beyond germline BRCA |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel increases pathologic complete response in high-risk HER2-negative stage II/III breast cancer |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Phase 2 study | Breast (Edinburgh) | NOBROLA: olaparib monotherapy activity in advanced triple-negative breast cancer with HRD but no germline BRCA1/2 mutation |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Real-world study | Breast Cancer Res Treat | LUCY final analysis: real-world effectiveness and safety of olaparib in gBRCA-mutated, HER2-negative metastatic breast cancer |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved as monotherapy for deleterious/suspected germline BRCA-mutated, HER2-negative breast cancer |

---

## Finland Market Information

Olaparib currently has no marketing authorization on record in Finland (0 authorizations; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor, synthetic lethality mechanism — not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical evidence is strong — two independent, completed Phase 3 RCTs (OlympiAD, OlympiA) support olaparib's efficacy in BRCA-mutated breast cancer, meeting L1 evidence criteria. However, the drug is not currently marketed in Finland, and Blocking/High-severity data gaps (TFDA-equivalent label warnings/contraindications, detailed MOA) prevent a full safety review, so guardrails are required before advancing.

**To proceed, the following is needed:**
- Finnish package insert (warnings, contraindications, DDI) to clear the Blocking data gap (DG001)
- Confirmed original approved indication and detailed MOA from DrugBank (DG002)
- Confirmation of Finland market authorization pathway, since the drug is currently unmarketed
- DDI database query (current status: not_found) to complete the S1 safety pre-assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

