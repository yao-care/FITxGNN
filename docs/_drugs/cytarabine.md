---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Acute Myeloid Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a classic S-phase-specific antimetabolite chemotherapy agent long used for acute myeloid leukemia and other hematologic malignancies.
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma**,
with **3 clinical trials** and **20 publications** currently retrieved, though most evidence is indirect (centered on NSCLC rather than SCLC itself).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute leukemias (e.g., AML, ALL) and CNS/leptomeningeal leukemia — based on known pharmacology; Finland-specific licensing text not available |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cytarabine (Ara-C) is a pyrimidine nucleoside analog. After intracellular phosphorylation it is incorporated into DNA and inhibits DNA polymerase, making it an S-phase-specific cytotoxic agent — theoretically most active against rapidly proliferating cell populations. This mechanism underlies its established role in acute leukemias, where blast cells divide rapidly.

Small cell lung carcinoma is likewise characterized by an exceptionally high proliferative fraction, providing a plausible mechanistic rationale for extrapolating an S-phase-specific cytotoxic agent from leukemia to SCLC. However, the retrieved evidence base is not SCLC-specific: the majority of clinical trials and publications involve **non-small cell lung cancer (NSCLC)** rather than SCLC, and the clinical behavior, growth kinetics, and chemosensitivity profiles of NSCLC and SCLC differ substantially. Mechanistic extrapolation from NSCLC data to SCLC therefore requires caution, even though a smaller set of older SCLC-specific studies (1979–1988) does exist showing cytarabine used in combination regimens for SCLC.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed + involved-field radiotherapy for leptomeningeal metastasis from solid tumors (not SCLC-specific; drug is pemetrexed, not cytarabine — indirect relevance) |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent leptomeningeal metastasis from NSCLC; notes cytarabine as a commonly used intrathecal chemotherapy comparator, but is not itself testing cytarabine |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy trial in early-stage NSCLC (vinorelbine/cisplatin/docetaxel/gemcitabine/pemetrexed); terminated, and does not specify cytarabine use |

*No trial in this evidence set directly tests cytarabine in SCLC; all three are graded "C" (indirect relevance) in the evidence pack.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | Randomized Trial | J Clin Oncol | CALGB randomized study of chemotherapy + radiotherapy ± warfarin in limited-stage SCLC |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Cohort/Combined Modality | Med Pediatr Oncol | Cyclophosphamide + doxorubicin + subcutaneous cytosine arabinoside plus radiotherapy in 20 previously untreated SCLC patients |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical Study | Am J Clin Oncol | Continuous-infusion Ara-C alone (no responses, severe toxicity) and Ara-C added to CAV regimen in SCLC |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical Study | Am J Clin Oncol | Etoposide + infusional Ara-C in relapsed/refractory SCLC (17 patients) |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II Trial | Tumori | Cytarabine + cisplatin + vindesine in advanced NSCLC; 18% response rate |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II Trial | Cancer | High-dose cytarabine + cisplatin in chemo-naive NSCLC; 14% response rate, Grade III/IV myelosuppression in ~46% |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | Pilot Study | Eur J Cancer Clin Oncol | Cisplatin + cytarabine combination in advanced NSCLC |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case Series | Am J Med | Meningeal carcinomatosis in SCLC treated with intensive chemotherapy; 78% response rate |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case Report | Gan To Kagaku Ryoho | Multidisciplinary treatment of meningeal carcinomatosis in SCLC |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiot Chemother | Review of Ara-C analogs and mechanisms of resistance/deactivation |

## Finland Market Information

Cytarabine is currently **not marketed in Finland** — no authorizations are on record (0 licenses). No Fimea-approved product or indication text is available for extraction.

## Cytotoxicity

Cytarabine is a conventional cytotoxic chemotherapy agent (antimetabolite class); this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (pyrimidine nucleoside antimetabolite, S-phase specific) |
| Myelosuppression Risk | High — dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia are expected, particularly with high-dose regimens |
| Emetogenicity Classification | Moderate to High (dose-dependent; standard-dose regimens are moderately emetogenic, high-dose IV regimens are highly emetogenic) |
| Monitoring Items | CBC with differential and platelet count, liver and renal function, neurologic exam (cerebellar toxicity with high-dose regimens), conjunctivitis surveillance (high-dose IV) |
| Handling Protection | Yes — requires handling under cytotoxic/hazardous drug precautions (closed-system transfer devices, PPE per institutional cytotoxic handling protocols) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence linking cytarabine to SCLC is largely indirect — most retrieved trials/literature concern NSCLC, and the few SCLC-specific studies are small, decades-old combination-regimen reports rather than confirmatory trials. Combined with a Blocking data gap on TFDA/Fimea safety labeling and the drug currently being unmarketed in Finland, a Go or Guardrails decision is premature.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action record for cytarabine
- SCLC-specific (not NSCLC-extrapolated) clinical trial evidence, ideally Phase II/III
- Drug-drug interaction data, currently unavailable (query returned not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

