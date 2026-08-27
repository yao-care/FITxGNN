---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a guanosine nucleoside analogue originally developed and approved for chronic hepatitis B virus (HBV) infection, where it inhibits the HBV reverse transcriptase. The TxGNN model's top-ranked prediction is **chronic hepatitis C virus infection**, supported by **40 clinical trials** and **20 publications** in the evidence pack — however, on closer inspection, none of this evidence demonstrates direct anti-HCV efficacy; the trials and literature almost entirely concern entecavir's real, established use in HBV (including HBV/HCV co-infection management), and the evidence pack itself grades this HCV signal as low-confidence (**Evidence Level L4, Recommendation: Hold**).

> ⚠️ **Important caveat:** This evidence pack's rank-2 prediction, "hepatitis B virus infection" (score 99.85%, **Evidence Level L1**), is explicitly annotated in the source data as entecavir's **original, already-approved indication**, not a new repurposing candidate. The rank-1 "hepatitis C" signal appears to be a TxGNN knowledge-graph artifact arising from HBV/HCV co-infection studies and shared "viral hepatitis" ontology terms, rather than a genuine mechanistic repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus (HBV) infection *(inferred from evidence-pack rationale; no Finland/Taiwan regulatory license record available — drug is not marketed there)* |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Finland Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for entecavir is not available in this evidence pack (Data Gap DG002, High severity). Based on known pharmacology, entecavir is a deoxyguanosine nucleoside analogue that is phosphorylated intracellularly to its active triphosphate form, which competitively inhibits the HBV reverse transcriptase — blocking priming, negative-strand DNA synthesis, and positive-strand DNA synthesis. This is a highly specific, well-established mechanism for suppressing HBV replication.

Hepatitis C virus, by contrast, is a positive-strand RNA flavivirus whose replication depends on the NS5B RNA-dependent RNA polymerase — a structurally and catalytically distinct enzyme with no known cross-reactivity to entecavir's reverse-transcriptase-inhibiting mechanism. The evidence pack's own repurposing rationale for this prediction states directly: *"缺乏直接生物學合理性"* (lacks direct biological plausibility), and notes that essentially all of the listed clinical trials either (a) study direct-acting antivirals (DAAs) for HCV while entecavir is used only to control the HBV side of HBV/HCV co-infection, or (b) study entecavir's real target — HBV — with no HCV efficacy endpoint at all.

In short, this prediction most likely reflects a TxGNN knowledge-graph artifact: entecavir and HCV co-occur frequently in the literature because of shared "viral hepatitis" disease-ontology proximity and HBV/HCV co-infection management studies, not because of a genuine antiviral mechanism against HCV. No trial or publication in this pack reports an HCV virologic-response endpoint attributable to entecavir itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studied HBV reactivation during direct-acting antiviral (DAA) treatment of HCV/HBV co-infection; entecavir addressed only the HBV component, not HCV. |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Drug-drug interaction/PK study of entecavir or TDF with morphothiadine mesilate/ritonavir in healthy subjects; not an HCV efficacy trial. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Entecavir vs. adefovir in HBV patients with hepatic decompensation; unrelated to HCV. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | Observational antiviral-effect study of entecavir in Black/Hispanic patients with chronic HBV; unrelated to HCV. |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Phase 3 | Unknown | 120 | Tenofovir vs. lamivudine for HBV with severe acute exacerbation; does not involve entecavir or HCV. |
| [NCT01354652](https://clinicaltrials.gov/study/NCT01354652) | Phase 4 | Terminated | 5 | Investigated lactic acidosis incidence during entecavir treatment in HBV cirrhosis/hepatic failure; safety study, unrelated to HCV. |
| [NCT03272009](https://clinicaltrials.gov/study/NCT03272009) | Phase 1 | Completed | 73 | Safety/PK/PD study of FXR-agonist EYP001a in chronic HBV; drug/target unclear, not HCV-related. |
| [NCT05416008](https://clinicaltrials.gov/study/NCT05416008) | N/A | Unknown | 150 | Observational study of long-term nucleos(t)ide analogue use and hepatic steatosis in chronic HBV; unrelated to HCV. |
| [NCT01020565](https://clinicaltrials.gov/study/NCT01020565) | Phase 2 | Completed | 60 | Japanese Phase 2 safety/antiviral-activity study of entecavir in chronic HBV; unrelated to HCV. |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Prospective entecavir study in HBV-related HCC patients post-radiofrequency ablation; unrelated to HCV. |

**Note:** All 10 trials above were internally graded "C" (low relevance) in the evidence pack — none provides direct evidence of anti-HCV efficacy for entecavir.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV RNA dynamics in anti-HCV-antibody-positive chronic HBV patients undergoing nucleos(t)ide analogue (including entecavir) therapy — describes HCV virologic behavior during HBV-directed treatment, not HCV treatment efficacy. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener medizinische Wochenschrift | Overview of chronic hepatitis B and C treatment landscape; entecavir discussed only in the HBV context. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Reviews management of HBV/HCV coinfection; highlights therapeutic challenge but does not attribute anti-HCV activity to entecavir. |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Review | Chinese Clinical Oncology | Discusses optimal timing of HBV/HCV antiviral therapy in hepatocellular carcinoma; general background, not entecavir-specific HCV data. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Reviews HBV and HCV antiviral medications and renal effects; entecavir listed among HBV nucleoside analogues only. |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World Journal of Gastroenterology | Background review on HBV/HCV/alcohol-related hepatocellular carcinoma; no direct entecavir-HCV data. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clinics and Research in Hepatology and Gastroenterology | Pediatric HBV/HCV management overview; entecavir mentioned in HBV context only. |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Practice & Research Clinical Gastroenterology | Fibrosis progression in chronic viral hepatitis; entecavir referenced for HBV fibrosis regression, not HCV. |
| [38631661](https://pubmed.ncbi.nlm.nih.gov/38631661/) | 2024 | In vitro mechanistic | Antiviral Research | USP7's role in HBV replication and entecavir's antiviral efficacy — HBV-specific mechanistic study, not HCV. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Case report | Clinics and Research in Hepatology and Gastroenterology | Case report of an HBV/HCV co-infected patient; illustrates treatment complexity but not entecavir efficacy against HCV. |

**Note:** No RCT or systematic review in this pack reports entecavir efficacy against HCV; all identified literature relates to HBV treatment or HBV/HCV co-infection management context.

---

## Finland Market Information

Entecavir is currently **not marketed in Finland** (0 authorizations on record in this evidence pack). No product license, brand name, or dosage-form data is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information. *(This evidence pack's warnings, contraindications, and drug-interaction fields are marked as data gaps — DG001, Blocking severity — meaning no formal safety assessment for this indication is currently possible from the available data.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (chronic hepatitis C virus infection) lacks direct mechanistic plausibility — entecavir targets the HBV reverse transcriptase, which has no known activity against the HCV NS5B RNA polymerase — and none of the 40 associated trials or 20 publications demonstrate an anti-HCV efficacy endpoint attributable to entecavir. This pattern is consistent with a knowledge-graph artifact driven by HBV/HCV co-infection literature rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Formal TFDA/Fimea package-insert data (warnings, contraindications, drug interactions) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- In vitro confirmation (or refutation) of any entecavir activity against HCV NS5B polymerase, if this indication is to be pursued further
- Note: if repurposing analysis is desired for entecavir, the rank-2 signal in this pack (hepatitis B virus infection, Evidence Level L1, "Proceed with Guardrails") should instead be treated as documentation of its **existing, approved use** — with guardrails around lamivudine-resistant patients, renal-impairment dose adjustment, and lactic acidosis monitoring — rather than as a novel repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

