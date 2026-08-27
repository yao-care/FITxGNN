---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using no additional coding tools — this is a direct content-generation task per the detailed prompt template. Below is the report generated from the Evidence Pack.

---

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

> Adalimumab is a fully human anti-TNF-α monoclonal antibody, long established as a treatment for rheumatoid arthritis and related autoimmune inflammatory diseases.
> The TxGNN model predicts it may also be effective for **Rheumatoid Vasculitis (RV)**, a severe extra-articular manifestation of RA,
> with **5 clinical trials** and **10 curated publications** currently supporting (and complicating) this direction — the literature shows both therapeutic and adverse associations between adalimumab and vasculitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (and related TNF-α–driven autoimmune diseases). *Note: Fimea-specific approved-indication text is not present in this evidence pack — regulatory license data is empty (data gap).* |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned in this evidence pack (`original_moa: [Data Gap]`). Based on well-established public information, adalimumab is a fully human IgG1 monoclonal antibody that binds and neutralizes TNF-α, blocking its downstream pro-inflammatory signaling. It is a founding member of the anti-TNF class alongside infliximab and etanercept, approved across numerous countries for rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, juvenile idiopathic arthritis, psoriasis, and inflammatory bowel disease.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of long-standing, often seropositive rheumatoid arthritis, driven by immune-complex deposition and TNF-α–mediated inflammation of blood vessel walls. Because RV arises directly from uncontrolled RA-associated inflammation, and TNF-α is a key cytokine in that pathway, suppressing TNF-α is mechanistically plausible as a way to reduce vascular wall inflammation and immune-complex burden — this is the biological rationale TxGNN's knowledge graph is likely capturing.

However, the evidence is genuinely two-sided. On one hand, a published case report (PMID 25133007) describes digital vasculitis in an RA patient responding well to adalimumab, and a systematic review (PMID 33058033) discusses biologics — including anti-TNF agents — as part of the RV therapeutic armamentarium. On the other hand, multiple case reports and a pharmacovigilance cohort (PMID 28719435, PMID 28123776, PMID 36418100) describe adalimumab and other TNF inhibitors *inducing* vasculitis-like or lupus-like adverse reactions in RA patients. This paradox — TNF-α blockade as both a potential treatment and a potential trigger of vasculitis — means the mechanistic link, while biologically plausible, is not yet directionally resolved and requires focused safety/efficacy disambiguation before further evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management (incl. adalimumab) in rheumatology patients undergoing shoulder arthroplasty; assesses flare risk, not RV efficacy directly (Grade C). |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multinational observational study of tocilizumab in RA patients with inadequate DMARD/biologic response; not RV-specific (Grade C). |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Real-world safety study of brolucizumab in wet AMD — unrelated to adalimumab or RV, likely a keyword-matching artifact (Grade C). |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biologic DMARD treatment patterns in Chinese RA patients; not vasculitis-specific (Grade C). |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large cohort assessing risk of developing a second immune-mediated inflammatory disease (IMID, incl. vasculitis) after biologic/immunosuppressive treatment for a first IMID; indirectly relevant to the safety side of this question (Grade B). |

*No trial in this set was designed specifically to test adalimumab's efficacy in rheumatoid vasculitis; all listed trials are indirect (RA population studies, biologic safety registries, or likely mismatches).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | Systematic review of biological drugs (including anti-TNF agents) in the treatment of rheumatoid vasculitis — the most directly relevant evidence source. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Pharmacovigilance Cohort | RMD Open | BSRBR-RA registry data comparing risk/characteristics of lupus-like and vasculitis-like events in RA patients on TNF inhibitors vs. non-biologic DMARDs — key safety signal. |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | Journal of Clinical Medicine | Update on treatment of RA-associated episcleritis and scleritis (ocular vasculitic manifestations). |
| [31163474](https://pubmed.ncbi.nlm.nih.gov/31163474/) | 2019 | Review | Deutsche Medizinische Wochenschrift | Review of JAK inhibitors in rheumatology, contextualizing alternatives to anti-TNF therapy. |
| [37699653](https://pubmed.ncbi.nlm.nih.gov/37699653/) | 2024 | Genetic Association Study | Annals of the Rheumatic Diseases | HLA-DRB1/HLA-DQA1 associations with immunogenicity to adalimumab in RA patients. |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | PK Modeling Study | Pharmaceutics | Population PK modeling of adalimumab/etanercept biosimilar dosing regimens in RA. |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis in a rheumatoid vasculitis patient following adalimumab dose reduction — suggests a protective effect of continued therapy. |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | Tocilizumab used to treat ANCA-associated nephritis that developed during abatacept/adalimumab therapy for RA. |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report (Adverse Event) | American Journal of Dermatopathology | Leukocytoclastic vasculitis with dermal perivascular hemophagocytosis associated with adalimumab therapy — an adverse (pro-vasculitic) signal. |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | Digital vasculitis in an RA patient that responded well to adalimumab — a positive efficacy signal for RV. |

*Ten additional literature records were retrieved but remain unclassified (`study_type: pending`) in the source data and were excluded from this table pending classification.*

---

## Finland Market Information

Adalimumab is currently **not marketed** in Finland per this evidence pack (`market_status: 未上市`, `total_licenses: 0`), and no license records are available to summarize. This should be independently confirmed against the current Fimea register, since adalimumab (including originator Humira® and multiple biosimilars) is widely marketed in the EU/EEA, and an unmarketed status here may reflect a gap in the source query rather than actual regulatory status.

---

## Safety Considerations

Please refer to the package insert for safety information — `key_warnings`, `contraindications`, and DDI data are all marked as data gaps or not found in this evidence pack.

**Important:** the meta-level data gap log flags this as a **Blocking** issue (DG001 — TFDA/Fimea package insert warnings/contraindications, source: TFDA official site, remediation: retrieve and parse the package insert PDF). Per the evidence pack, this gap currently **prevents entry into the S1 safety pre-assessment stage** for this candidate, independent of the mechanistic or clinical-trial evidence discussed above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking** data gap (DG001) means official prescribing-label safety information (warnings/contraindications) is unavailable, which by itself prevents progression to formal safety pre-assessment (S1).
- Independent of that gap, the disease-specific evidence is only **L3** (systematic review/cohort level, no completed RCT targeting adalimumab in RV) and is **directionally mixed** — published case reports support adalimumab both as a treatment for RV-related vasculitis and as a possible trigger of vasculitis-like/lupus-like reactions in RA patients on TNF inhibitors.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/Fimea package insert to resolve the Blocking safety data gap (DG001).
- Obtain structured DrugBank MOA and toxicity data (DG002) to formally support the mechanistic rationale.
- Conduct a focused pharmacovigilance/case-series analysis to disambiguate whether TNF-α blockade with adalimumab more often treats or triggers vasculitis in RA patients, since current evidence supports both directions.
- If proceeding, define an RV-specific interventional trial design and endpoints, since no completed randomized trial currently tests adalimumab directly for this indication.
- Confirm Finland/Fimea market and licensing status directly against the current register, as the "not marketed" status here may reflect an incomplete source query rather than true regulatory absence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

