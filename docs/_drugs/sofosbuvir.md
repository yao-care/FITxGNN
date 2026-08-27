---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is an NS5B RNA-dependent RNA polymerase inhibitor originally developed as the nucleotide-analog backbone of chronic Hepatitis C virus (HCV) combination regimens (e.g. with ledipasvir, velpatasvir). The TxGNN model predicts it may be effective for **Hepatitis B virus infection**, but the clinical evidence assembled for this candidate is largely discouraging: the one purpose-built HBV monoinfection trial (APOSTLE) found no meaningful antiviral effect attributable to sofosbuvir itself, and several reports instead describe HBV reactivation risk during sofosbuvir-based HCV treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (inferred from the clinical trial/literature corpus in this evidence pack — TFDA-specific approved indication text is unavailable) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data from DrugBank/TFDA is a confirmed data gap for this candidate. However, the literature surfaced in this evidence pack consistently and repeatedly identifies sofosbuvir as a nucleotide-analog prodrug that is metabolized intracellularly to its active triphosphate form (GS-331007-TP), which competitively inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp) and terminates viral RNA chain synthesis. This mechanism is what made it the backbone of essentially every trial and case report in this pack, virtually all of which concern chronic HCV treatment.

HBV, unlike HCV, replicates via a reverse-transcriptase intermediate rather than an RdRp acting on genomic RNA — so there is no direct enzymatic target overlap between sofosbuvir's mechanism and HBV replication. The TxGNN prediction most plausibly reflects the drug's clinical co-occurrence with HBV in the literature (HCV/HBV coinfection is common and heavily studied) rather than a validated antiviral mechanism against HBV itself.

This is borne out by the direct evidence: the one HBV-monoinfection trial (APOSTLE, NCT03312023/PMID 36045503) tested ledipasvir/sofosbuvir specifically because retrospective data suggested a modest HBsAg decline in HCV/HBV-coinfected patients — but that decline has been attributed to the NS5A inhibitor ledipasvir, not sofosbuvir. Separately, several coinfection trials and case reports (NCT02613871, and multiple literature reports below) describe HBV DNA **rising** — i.e., reactivation — during sofosbuvir-based HCV therapy, which is the opposite of a therapeutic effect. Sofosbuvir has no known enzymatic activity against the HBV polymerase.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | APOSTLE trial: ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; primary/secondary endpoints were HBsAg and HBV DNA decline. Published results (PMID 36045503) found no meaningful antiviral effect attributable to sofosbuvir itself. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | LDV/SOF FDC in HCV/HBV genotype 1/2 coinfected subjects (Taiwan); primary endpoint was HCV SVR, not HBV suppression — HBV DNA rose in most patients, a reactivation signal rather than efficacy signal. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of incidence, morbidity, and predisposing factors for HBV reactivation during direct anti-HCV treatment of HCV/HBV coinfected patients — a safety/reactivation study, not an HBV efficacy trial. |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | 12-week SOF/VEL regimen combined with prophylactic TAF to prevent HBV reactivation in HCV/HBV-coinfected patients — supports reactivation risk management, not sofosbuvir efficacy against HBV. |

*Note: the remaining ~45 trials returned for this indication in the evidence pack are chronic-HCV efficacy trials that mention HBV only as a coinfection/exclusion criterion; they were excluded here as not directly relevant to an HBV indication.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT (Phase 2 pilot) | Journal of Medical Virology | APOSTLE trial primary publication: LDV/SOF in HBV-monoinfected subjects; HBsAg/HBV DNA decline endpoints not achieved in a way attributable to sofosbuvir. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort study | Journal of Clinical Gastroenterology | Examined risk of HBV reactivation in actively/previously infected patients receiving LDV/SOF for HCV — reactivation incidence and outcomes remain unclear but documented. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | Journal of Viral Hepatitis | HBV reactivation in cancer patients receiving DAAs (including sofosbuvir-based regimens) for HCV/HBV coinfection. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort study | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment in HCV/HBV coinfected patients with pretreatment HBeAg seroconversion. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir and ribavirin. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | Journal of Medical Case Reports | HBV reactivation via a surface-antigen immune-escape mutant in an HBcAb-positive patient during sofosbuvir/velpatasvir treatment for HCV. |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Case report / ADR alert | Hospital Pharmacy | FDA MedWatch-style report of hepatitis B reactivation associated with simeprevir and sofosbuvir treatment for HCV. |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Modelling study | The Lancet Gastroenterology & Hepatology | Global HBV prevalence/care-cascade modelling (background epidemiology; not sofosbuvir-specific). |

## Taiwan Market Information

Sofosbuvir currently holds **no marketing authorizations in Taiwan** (`taiwan_regulatory.total_licenses = 0`, market status 未上市). No product name, dosage form, or approved-indication data is available in the regulatory database for this candidate.

## Safety Considerations

Formal key warnings, contraindications, and drug-interaction data for sofosbuvir are currently a data gap in the source databases (TFDA package insert not yet ingested; DDI query returned no results). Please refer to the package insert for complete safety information once obtained.

One safety signal specific to this repurposing candidate does emerge from the literature evidence itself and should be flagged: multiple case reports and cohort studies (PMIDs 29334502, 33523503, 31632097, 33031326, 31542053, 27621502) describe **HBV reactivation** — sometimes with severe hepatitis flares — occurring during or after sofosbuvir-based DAA treatment of HCV in HBV-coinfected or previously HBV-exposed patients. This is a safety concern to monitor for, not a therapeutic effect, and should be weighed heavily against any HBV-repurposing rationale.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only HBV-specific trial evidence (APOSTLE, NCT03312023/PMID 36045503) found no sofosbuvir-attributable antiviral effect in HBV monoinfection, and coinfection data instead show a reactivation risk rather than a therapeutic benefit — the evidence direction contradicts the repurposing hypothesis. Sofosbuvir's known mechanism (HCV NS5B RdRp inhibition) also has no enzymatic basis for activity against HBV's reverse transcriptase.

**To proceed, the following is needed:**
- TFDA package insert / DrugBank MOA data to complete a formal S1 safety pre-screen (currently blocking, DG001/DG002)
- A mechanistic or enzymatic study specifically testing sofosbuvir against HBV polymerase, if this candidate is to be pursued further
- Systematic review of the HBV reactivation signal (frequency, risk factors) before considering sofosbuvir in any HBV-coinfected population

**Note on related candidates in this evidence pack:** the same TxGNN run also scored sofosbuvir against Hepatitis E virus infection (rank 2, L3, in vitro RdRp inhibition plus a completed pilot trial NCT03282474 — recommended as a **Research Question** rather than Hold) and Kyasanur forest disease (rank 7, L4, direct enzymatic inhibition of a homologous flaviviral RdRp shown in vitro — also **Research Question**). Both show stronger mechanistic plausibility than the top-ranked HBV prediction and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

