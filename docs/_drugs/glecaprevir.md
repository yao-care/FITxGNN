---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

# Glecaprevir: From Hepatitis C Virus Infection to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is an NS3/4A protease inhibitor originally developed (as the glecaprevir/pibrentasvir combination, Mavyret) for chronic Hepatitis C virus (HCV) infection. TxGNN predicts a possible link to **HIV infectious disease**, and while **15 clinical trials** and **20 publications** touch this space, essentially all of them treat HCV in HIV-coinfected patients rather than testing glecaprevir's efficacy against HIV itself — the mechanistic case for repurposing is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus (HCV) infection (inferred from evidence-pack literature; not confirmed via Taiwan regulatory filings — drug not yet marketed in Taiwan) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Glecaprevir is an HCV NS3/4A serine protease inhibitor — it binds and blocks the enzyme HCV uses to cleave its polyprotein precursor. HIV, by contrast, relies on an aspartic protease (from a completely different enzyme family) to cleave the Gag-Pol precursor. These two protease families have no structural or catalytic-mechanism overlap, so there is no established pharmacological basis for glecaprevir having direct anti-HIV activity.

The high TxGNN score most plausibly reflects a knowledge-graph artifact: HIV and HCV are extremely frequent co-morbidities (roughly 25–30% of HIV-positive patients in Europe/US are HCV co-infected), so the two disease nodes are densely connected through shared trial populations, shared literature, and shared care pathways — not through a validated drug-target mechanism. Consistent with this, essentially every trial and paper retrieved for this indication is an HCV-treatment study conducted *in* an HIV/HCV co-infected population (e.g., EXPEDITION-2, MAGELLAN-3), evaluating HCV sustained virologic response (SVR) as the endpoint — not HIV viral suppression.

No in vitro, preclinical, or clinical data in this evidence pack demonstrate any antiretroviral activity of glecaprevir. The one clearly relevant supporting document is a drug-drug interaction (DDI) study characterizing how glecaprevir/pibrentasvir can be safely co-administered *alongside* HIV antiretrovirals — this is compatibility data, not efficacy data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: efficacy/safety of glecaprevir/pibrentasvir for HCV GT1-6 in HIV-1 co-infected adults (HCV endpoint, not HIV) |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | Asian adults with chronic HCV GT1-6, with or without HIV co-infection; HCV treatment-naïve/experienced (HCV endpoint) |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | Asian adults with HCV + compensated cirrhosis, with/without HIV co-infection (HCV endpoint) |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot study of paritaprevir/ritonavir/ombitasvir/dasabuvir ± ribavirin or glecaprevir/pibrentasvir for recently acquired HCV, with/without HIV co-infection |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | PURGE-C: 4-week glecaprevir/pibrentasvir fixed-dose combo for acute HCV, with/without HIV-1 coinfection |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV co-infected vs HIV mono-infected controls (CV endpoint, not antiviral) |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not yet recruiting | 30 | PK/safety of glecaprevir/pibrentasvir initiated in pregnancy, HCV ± HIV |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | Completed | 33 | MAGELLAN-3: glecaprevir/pibrentasvir + sofosbuvir/ribavirin in HCV virologic-failure patients (HCV endpoint) |
| [NCT04577482](https://clinicaltrials.gov/study/NCT04577482) | N/A | Completed | 42 | Real-world effectiveness of glecaprevir/pibrentasvir in DAA-experienced HCV GT1 patients, Russia |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | Completed | 17 | Telemedicine-delivered HIV PrEP + HCV treatment feasibility study at needle-exchange sites |

**Note:** None of the trials above assess glecaprevir's effect on HIV viral load, CD4 count, or HIV clinical outcomes — all measure HCV cure (SVR) in populations that happen to also carry HIV.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Real-world response to glecaprevir/pibrentasvir in HIV/HCV-coinfected patients; addresses concern that HIV coinfection lowers DAA SVR rates |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | DDI study | J Infect Dis | Characterizes drug-drug interactions between glecaprevir/pibrentasvir and HIV antiretrovirals — coadministration safety, not anti-HIV efficacy |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Real-world study | Clin Exp Hepatol | Effectiveness of glecaprevir/pibrentasvir (HCV cure) in HIV/HCV-coinfected patients on bictegravir/emtricitabine/TAF |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | Case Report | J Prev Med Hyg | Jaundice/hyperbilirubinemia in an HIV-infected patient on glecaprevir/pibrentasvir + ART (adverse event report) |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | Protease inhibitor therapy for HCV, discusses ~25-30% HIV/HCV coinfection prevalence in Europe/US |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Review | GMS Infect Dis | Protease inhibitors for HCV treatment, same HIV/HCV coinfection context as above |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | General efficacy/safety review of glecaprevir/pibrentasvir for chronic HCV |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Review | Hepatol Int | Glecaprevir/pibrentasvir expands HCV treatment reach, reduces cost/duration |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Systematic Review/Meta-analysis | Int J Antimicrob Agents | SVR12 ~97.8% for glecaprevir/pibrentasvir across HCV GT1-6 (HCV efficacy only) |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case Report | Clin J Gastroenterol | Successful HCV genotype 4a treatment with glecaprevir/pibrentasvir in a Japanese hemophilia patient with HIV/HCV coinfection |

## Taiwan Market Information

Glecaprevir is **not currently marketed in Taiwan** (0 authorizations on record). No TFDA license or approved-indication text is available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, and formal DDI records) were not available at the time of this evidence pull (query status: not found). Note that a dedicated DDI publication (PMID 31504702, above) exists characterizing interactions between glecaprevir/pibrentasvir and HIV antiretrovirals — this should be prioritized once formal safety review begins.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score and a large volume of associated trials/literature, none of the retrieved evidence demonstrates anti-HIV activity for glecaprevir — the evidence base consists entirely of HCV-treatment studies conducted in HIV/HCV co-infected populations. The mechanistic rationale (HCV NS3/4A serine protease vs. HIV aspartic protease, unrelated enzyme families) actively argues against repurposing, and the prediction is more consistent with a knowledge-graph co-morbidity artifact than a genuine pharmacological signal. This is corroborated by the source evidence pack's own scoring (decision_stage S0, recommendation "Hold" across all 10 predicted indications).

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: TFDA package insert (warnings/contraindications) before any S1 safety screening can begin
- Resolve high-priority data gap DG002: confirmed original MOA/indication documentation from DrugBank (current record flagged as data gap despite mechanism being inferable from literature)
- In vitro or biochemical evidence of any direct interaction between glecaprevir and HIV protease or replication machinery, if this hypothesis is to be pursued further
- Formal DDI dataset (beyond the single identified publication) given the drug is not yet marketed in Taiwan and has zero registered authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

