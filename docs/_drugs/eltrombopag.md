---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 1
---

# Eltrombopag
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

# Eltrombopag: From Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is a thrombopoietin (TPO) receptor agonist whose clinical evidence base centers on thrombocytopenia associated with chronic liver disease and hepatitis C infection; it is **not currently marketed in Finland**. The TxGNN model predicts a possible link to **HIV infectious disease**, but on closer review the supporting evidence almost entirely concerns **HIV-associated immune thrombocytopenia (ITP)** or **immune reconstitution thrombocytopenia** rather than direct antiviral activity, with **5 clinical trials** and **10 publications** currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (no Finland market authorization on file); trial evidence indicates historical/investigational use for **thrombocytopenia** in chronic liver disease and hepatitis C |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available in the drug record itself. Based on the evidence pack's own repurposing analysis, eltrombopag is a **TPO (thrombopoietin) receptor agonist** that works by stimulating megakaryocyte production and raising platelet counts. This mechanism has no direct link to HIV viral replication or the infection process itself.

Almost all of the identified clinical trials and case reports actually describe eltrombopag being used to manage **thrombocytopenia that occurs alongside HIV infection** — either as HIV-associated ITP, immune reconstitution thrombocytopenia after starting HAART, or thrombocytopenia in the closely related setting of chronic HCV/liver disease. This is a supportive-care use pattern, not a demonstration of anti-HIV efficacy.

Only one source, an in vitro FDA-drug-library screen (PMID 32977702), raises a mechanistic hypothesis that eltrombopag might modulate HIV-1 proviral transcription — potentially relevant to "shock and kill" latency-reversal strategies — but this is preclinical and unvalidated in humans. **The TxGNN label "HIV infectious disease" should therefore be interpreted cautiously**: the real, evidence-backed repurposing signal is eltrombopag for **HIV-associated thrombocytopenia/ITP**, not treatment of HIV infection itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Evaluated eltrombopag to reduce platelet transfusion needs in thrombocytopenic chronic liver disease patients undergoing invasive procedures; not HIV-specific |
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Open-label rollover study of eltrombopag safety/efficacy in thrombocytopenic HCV patients eligible for antiviral therapy |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | Assessed ability of eltrombopag (SB-497115-GR) to raise/maintain platelet counts in HCV patients with compensated cirrhosis |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | Large pivotal RCT of eltrombopag for thrombocytopenia in HCV patients initiating peginterferon/ribavirin therapy |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | Companion pivotal RCT (peginterferon alfa-2a arm) for eltrombopag in HCV-related thrombocytopenia |

*Note: None of the above trials enrolled HIV-infected patients specifically or tested antiviral efficacy against HIV; all target thrombocytopenia in HCV/liver disease populations.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohort | Platelets | Danish real-world cohort of TPO receptor agonist use (including eltrombopag) in refractory ITP, including secondary/infection-associated cases |
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematology/Oncology Clinics of North America | Reviews HCV, HIV, and H. pylori as infectious causes of chronic ITP; treating the underlying infection often improves thrombocytopenia |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Seminars in Hematology | Discusses therapeutic strategies for hepatitis- and other infection-related immune thrombocytopenias, including HIV |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Review | Internal Medicine Journal | Reviews TPO receptor agonist use in immune thrombocytopenia of less than 6 months' duration |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case series | J Int Assoc Provid AIDS Care | TPO receptor agonists (eltrombopag, romiplostim) used as salvage therapy in refractory HIV-associated ITP after HAART optimization |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS | Eltrombopag successfully used without splenectomy for refractory HIV-related immune reconstitution thrombocytopenia |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS | First report of eltrombopag successfully treating aplastic anaemia associated with HIV infection; showed immunomodulatory effect (reduced Th1/Th17, increased Treg/Th ratio) |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | J Coll Physicians Surg Pak | HBV infection (not HIV) causing megaloblastic anemia and severe thrombocytopenia; general infection–thrombocytopenia link |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farmacia Hospitalaria | Two case reports of eltrombopag for thrombocytopenia in chronic hepatitis C patients |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro screening | Viruses | FDA-approved drug library screen identifying modulators of HIV-1 proviral transcription; basis for a preclinical latency-reversal hypothesis |

---

## Finland Market Information

Eltrombopag currently has no marketing authorization on record in Finland (0 authorizations, market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-interaction data were retrievable at this time — this is flagged as a **Blocking** data gap (DG001) for TFDA-equivalent labeling and must be resolved before any safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence base actually addresses HIV-associated thrombocytopenia/ITP rather than treatment of HIV infection itself, and the drug is not currently marketed in Finland with no verified safety/labeling data available — evidence level L4 (preclinical/mechanistic and case-level only) does not support proceeding.

**To proceed, the following is needed:**
- TFDA/regulatory-equivalent package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action (MOA) from DrugBank or primary literature (DG002)
- Reframing of the indication hypothesis toward "HIV-associated thrombocytopenia/ITP" rather than "HIV infectious disease," followed by re-scoring
- A prospective study (even small/observational) specifically enrolling HIV-infected patients with thrombocytopenia to validate the case-report-level signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

