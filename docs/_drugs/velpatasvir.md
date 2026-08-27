---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Velpatasvir is an NS5A-inhibitor antiviral used in fixed-dose combination products (e.g., sofosbuvir/velpatasvir) for chronic hepatitis C. TxGNN predicts it may also be effective against **Hepatitis B Virus Infection** (score **99.87%**), but of the **26 clinical trials** and **20 publications** retrieved for this pairing, only one trial and one case report actually reference HBV — and neither shows an antiviral effect of velpatasvir against HBV itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (as part of fixed-dose combinations such as sofosbuvir/velpatasvir) — no formal indication record found in this evidence pack |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for velpatasvir is officially flagged as a data gap in this evidence pack. Based on the trial and literature context that is present, velpatasvir is known to act as an NS5A protein inhibitor and is used exclusively in combination antiviral regimens (with sofosbuvir, ± voxilaprevir) for chronic **hepatitis C virus (HCV)** infection — its "original indication" here has to be inferred from trial context rather than a confirmed regulatory record.

Hepatitis C and hepatitis B are both hepatotropic viral infections, which is likely why a knowledge-graph model such as TxGNN would place them close together (shared organ tropism, shared "viral hepatitis" phenotype, overlapping patient populations, and shared literature co-occurrence). However, the two viruses are biologically unrelated at the molecular target level: HCV is a single-stranded RNA virus (Flaviviridae) whose NS5A protein is velpatasvir's target, while HBV is a partially double-stranded DNA virus (Hepadnaviridae) that replicates via reverse transcriptase and has no NS5A homolog. There is therefore no established mechanistic basis for velpatasvir having direct anti-HBV activity.

Consistent with this, the vast majority of the 26 retrieved clinical trials and 20 publications are studies of sofosbuvir/velpatasvir (or sofosbuvir/velpatasvir/voxilaprevir) treating **HCV**, in some cases in patients who happen to be HCV/HBV co-infected. Only one trial (NCT04997564, TAF prophylaxis against HBV reactivation during HCV treatment) and one case report (PMID 31542053, HBV reactivation during SOF/VEL therapy for HCV) reference HBV directly — and both describe HBV as a co-infection/reactivation safety concern during HCV treatment, not as a treatment target of velpatasvir itself. This indicates the TxGNN association is very likely driven by network/phenotype proximity rather than validated pharmacology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | Only trial in the set that directly addresses HBV: prophylactic TAF + 12-week SOF/VEL in HCV/HBV co-infected patients, to prevent HBV reactivation during HCV treatment — an HBV *safety-management* study, not an HBV efficacy study of velpatasvir |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Phase 3 | Completed | 222 | Shortened interferon-free SOF/VEL therapy for recently acquired HCV (± HIV coinfection); graded "C" — unrelated to HBV |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | SOF/VEL ± ribavirin efficacy/safety in treatment-naive chronic HCV (genotypes 1–6); graded "C" — unrelated to HBV |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Real-world Vosevi (SOF/VEL/VOX) effectiveness in DAA-failure HCV patients; graded "C" — unrelated to HBV |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | SOF/VEL ± ribavirin in chronic HCV with decompensated cirrhosis — establishes VEL safety in advanced liver disease, no HBV endpoint |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug-interaction study of SOF/VEL/VOX with a hormonal contraceptive — pharmacokinetic, no HBV relevance |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Completed | 40 | Natural history/vertical transmission of chronic HCV in pregnancy, with postpartum SOF/VEL treatment — no HBV endpoint |
| [NCT05016609](https://clinicaltrials.gov/study/NCT05016609) | Phase 4 | Unknown | 1800 | Test-and-treat HCV care models among people who inject drugs — no HBV endpoint |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after HCV eradication in HIV/HCV patients — no HBV endpoint |
| [NCT03086044](https://clinicaltrials.gov/study/NCT03086044) | Phase 4 | Unknown | 148 | Transplanting organs from HCV-positive donors to HCV-negative recipients — no HBV endpoint |

**Note:** These trials were returned by an "HBV infection" evidence query, but essentially all of them are chronic HCV treatment/safety studies. Only NCT04997564 addresses HBV, and only as a reactivation-prevention safety measure during HCV therapy — none demonstrate antiviral efficacy of velpatasvir against HBV.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | Journal of medical case reports | Only HBV-specific reference: describes HBV reactivation via a surface-antigen immune-escape mutant in an anti-HBc-positive patient during SOF/VEL treatment for HCV — an adverse-event report, not evidence of anti-HBV effect |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | RCT | Lancet Gastroenterology & Hepatology | SOF/VEL safety/efficacy in treatment-naive HCV genotype 4 patients in Rwanda — HCV efficacy trial, no HBV endpoint |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World Journal of Gastroenterology | Reviews pediatric HBV and HCV management, including DAAs for HCV — general context, no HBV efficacy data for velpatasvir |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Reviews | Summarizes HBV/HCV burden estimates and DAA advances presented at a viral hepatitis conference — background only |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional | Annals of Hepatology | Compares global HBV and HCV drug pricing — a health-economics comparison, not clinical/efficacy evidence |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective | Klinicka mikrobiologie a infekcni lekarstvi | Retrospective review of antiviral treatment for chronic HBV and HCV in children in Ostrava — descriptive, not velpatasvir-specific HBV data |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | European Journal of General Practice | General-practice review of chronic HCV diagnosis and treatment — no HBV content |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohort | Journal of Gastroenterology and Hepatology | Real-world SOF/VEL ± ribavirin efficacy/safety in HCV genotype 3 — no HBV content |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Cross-sectional | Cureus | SOF/VEL efficacy in HCV patients with chronic kidney disease — no HBV content |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clinical Pharmacokinetics | PK/PD review of DAA regimens (including SOF/VEL) for HCV — no HBV content |

**Note:** Of the 20 publications retrieved, only PMID 31542053 mentions HBV directly, and it describes a reactivation adverse event during HCV treatment rather than any therapeutic benefit of velpatasvir against HBV.

---

## Finland Market Information

No marketing authorization was found for velpatasvir in Finland (`total_licenses = 0`, market status: **Not marketed**). No authorization number, product name, or approved-indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not available in this evidence pack; DDI database query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is high (99.87%), there is no plausible mechanistic basis for velpatasvir — an HCV NS5A inhibitor — to have direct antiviral activity against HBV, a hepadnavirus with no NS5A homolog. Nearly all retrieved trials and publications are HCV treatment studies; only one trial and one case report reference HBV at all, and both describe HBV reactivation/co-infection safety management rather than therapeutic efficacy against HBV.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for velpatasvir (DG002) and TFDA/EU package-insert warnings and contraindications (DG001), both currently flagged as blocking data gaps
- In vitro or preclinical evidence of any anti-HBV activity for velpatasvir before further evaluation is warranted
- If such evidence emerges, re-score against the L1–L5 evidence framework; absent it, this candidate should not advance past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

