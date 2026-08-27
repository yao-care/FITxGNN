---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 1
---

# Teriflunomide
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

# Teriflunomide: From No Registered Indication in Finland to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Teriflunomide (DrugBank DB08880) is not currently marketed in Finland, so no original approved indication is on record in the local regulatory database.
The TxGNN model predicts it may be effective for **Relapsing-Remitting Multiple Sclerosis (RRMS)**,
with **28 clinical trials** and **19 publications** currently supporting this direction — notably, this is also teriflunomide's well-established indication in other markets (marketed elsewhere as Aubagio), so the model is largely recovering a known, extensively validated indication rather than proposing a novel one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license or approved-indication record exists in Finland |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The structured `original_moa` field for this drug is a data gap. However, the literature evidence in this pack does describe teriflunomide's mechanism: it is a selective, reversible inhibitor of the mitochondrial enzyme dihydroorotate dehydrogenase (DHODH), which blocks de novo pyrimidine synthesis and reduces proliferation of activated T and B lymphocytes (PMID 31098896). This immunomodulatory mechanism is directly relevant to autoimmune, T/B-cell–mediated demyelinating disease such as MS.

Unlike a typical repurposing candidate, there is no distinct "original indication" to compare against here — the evidence pack shows zero Finland licenses and an empty `original_indications` field, meaning teriflunomide has simply never been registered in this market. Outside Finland, however, teriflunomide is a well-established, guideline-recommended first-line oral disease-modifying therapy for RRMS, a fact strongly corroborated by the trial and literature evidence below (including the pivotal TEMSO and TENERE Phase 3 trials, and its use as the active comparator in at least five subsequent Phase 3 trials against newer MS agents).

Because of this, the practical interpretation of this "candidate" is less a scientific discovery and more a **market-registration gap**: the mechanistic and clinical case for RRMS is already mature and extensively documented; what is missing is Finland-specific regulatory and safety documentation (see Data Gaps below), not proof of mechanistic plausibility.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1,088 | Pivotal placebo-controlled RCT (TEMSO): teriflunomide reduced relapse frequency and delayed disability accumulation in relapsing MS |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | TENERE: rater-blinded comparison of teriflunomide vs interferon beta-1a on time to treatment failure, relapse rate, fatigue and safety |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension of EFC6049 documenting long-term safety/tolerability and durability of efficacy on disability and MRI outcomes |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Compared ofatumumab vs first-line DMT (including teriflunomide) in newly diagnosed relapsing MS |
| [NCT07189325](https://clinicaltrials.gov/study/NCT07189325) | Phase 3 | Not yet recruiting | 250 | Non-inferiority trial of anti-CD20 maintenance vs de-escalation strategy in RRMS |
| [NCT06663189](https://clinicaltrials.gov/study/NCT06663189) | Phase 3 | Not yet recruiting | 200 | TWINS: randomized withdrawal of DMTs (including teriflunomide) in inactive RRMS patients ≥55 |
| [NCT00273364](https://clinicaltrials.gov/study/NCT00273364) | Phase 2 | Completed | 110 | Hematopoietic stem cell therapy vs alternate approved therapy in inflammatory MS failing treatment |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Extension study assessing long-term safety and efficacy of teriflunomide in relapsing MS |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | Determined teriflunomide serum and CSF concentrations at the 14 mg daily dose |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic study of regulatory B lymphocytes as mediators of teriflunomide's therapeutic effect |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | ASCLEPIOS: ofatumumab vs teriflunomide head-to-head comparison in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib (BTK inhibitor) vs teriflunomide in relapsing MS |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab vs teriflunomide in relapsing MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | evolutionRMS1/2: evobrutinib vs teriflunomide active-comparator Phase 3 trials |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM: ponesimod vs teriflunomide in relapsing MS |
| [37691530](https://pubmed.ncbi.nlm.nih.gov/37691530/) | 2023 | RCT (OLE) | Multiple Sclerosis Journal | ALITHIOS open-label extension: 4-year ofatumumab vs teriflunomide efficacy/safety |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | Overview of MS diagnosis and treatment, including disease-modifying therapies |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Systematic Review | Cochrane Database Syst Rev | Network meta-analysis of immunomodulators/immunosuppressants for RRMS |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Comprehensive review of teriflunomide's mechanism, efficacy and safety in RRMS |
| [37382446](https://pubmed.ncbi.nlm.nih.gov/37382446/) | 2023 | Review | Expert Rev Neurotherapeutics | Teriflunomide as first-line oral therapy in pediatric relapsing-remitting MS |

## Finland Market Information

Teriflunomide is not currently marketed in Finland — the evidence pack records **0 authorizations** and no license entries. No Finland-specific product, dosage form, or approved-indication text is available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all unavailable in the current evidence pack — the DDI query returned no records.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is exceptionally strong (L1) — two completed pivotal Phase 3 RCTs (TEMSO, TENERE) plus a long-term Phase 3 extension and five further Phase 3 head-to-head trials establish teriflunomide as a validated first-line RRMS therapy elsewhere. However, this candidate cannot advance to safety evaluation: the TFDA/Fimea package insert (warnings and contraindications) is a **Blocking** data gap, DDI data are absent, and the drug has zero current authorizations or market history in Finland.

**To proceed, the following is needed:**
- TFDA/Fimea package insert — warnings and contraindications (Blocking gap, required before S1 safety review)
- Structured DrugBank MOA record (High priority gap)
- A drug-drug interaction dataset (current query returned no results)
- Confirmation of Finland/EU regulatory pathway and timeline for market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

