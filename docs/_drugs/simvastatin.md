---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 8
---

# Simvastatin
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a well-established HMG-CoA reductase inhibitor (statin), classically used for hypercholesterolemia and cardiovascular risk reduction.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**,
with **19 clinical trials** and **18 publications** currently supporting this direction — though this reflects existing standard-of-care use rather than a genuinely novel signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in source data (Fimea license records absent; drug not marketed in Finland). Simvastatin is generically known as a statin used for hypercholesterolemia/dyslipidemia. |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data (`original_moa`) is marked as a data gap, but the evidence pack's repurposing rationale supplies the mechanistic story directly: simvastatin inhibits HMG-CoA reductase, lowering hepatic cholesterol synthesis and up-regulating LDL receptor expression, which increases LDL-C clearance from plasma.

Familial Hypercholesterolemia (FH) — and its genetic-nomenclature equivalent "autosomal dominant hypercholesterolemia" (independently predicted at rank 4, also scored L1) — is caused by defective LDL receptor pathway function, leading to impaired LDL clearance. Statin-driven LDL receptor up-regulation maps directly onto this disease mechanism, which is why simvastatin (and statins generally) are already first-line standard therapy for FH, including pediatric and heterozygous populations.

Because of this direct mechanistic fit, the evidence pack itself flags this as a textbook-level mechanism–indication pairing rather than a novel discovery from the TxGNN model — the two independent high-scoring predictions (FH and its genetic synonym) corroborate each other but do not represent new clinical insight.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in HeFH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin efficacy/safety/tolerability in adolescents with HeFH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH (HoFH) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term open-label extension of above HoFH ezetimibe + statin study |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs. simvastatin in FH/dyslipidaemia patients |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | Niacin ER + simvastatin vs. atorvastatin lipid effects in hyperlipidemia |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam add-on to stable statin therapy (incl. simvastatin) in pediatric HeFH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs. placebo in HeFH not controlled on background lipid-modifying therapy (incl. statins) |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab vs. placebo in HeFH not controlled on background lipid-modifying therapy (incl. statins) |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Post-marketing re-examination of VYTORIN (ezetimibe/simvastatin) safety and efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | 2026 ACC/AHA dyslipidemia guideline replacing 2018 blood cholesterol guideline; statins remain foundational therapy |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial: simvastatin ± ezetimibe effect on atherosclerosis progression in FH |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of statins for children with FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefits/risks assessment of simvastatin in FH |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin treatment reduces CAD events and mortality in heterozygous FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort | Journal of Clinical Medicine | Cellular immunity parameters in children with FH treated with simvastatin |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Cohort | The Pharmacogenomics Journal | Combined FH and statin pharmacogenomic NGS testing strategy |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin in patients with FH |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | RCT | International Angiology | Long-term efficacy/safety of ezetimibe/simvastatin in FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | RCT | Nutrition, Metabolism and Cardiovascular Diseases | Atorvastatin vs. simvastatin for LDL-C goal attainment in HeFH |

---

## Finland Market Information

Simvastatin currently has **no registered market authorizations in Finland** (`market_status: 未上市`, `total_licenses: 0`) in the evidence pack — no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The FH indication is backed by L1-level evidence (19 trials including the landmark ENHANCE RCT, 18 publications including Cochrane reviews and a 2026 ACC/AHA guideline), and is reinforced by an independent, equally L1-scored prediction for the same disease under its genetic name ("autosomal dominant hypercholesterolemia"). However, this reflects simvastatin's existing role as standard-of-care therapy rather than a novel repurposing signal, and two blocking/high-severity data gaps remain unresolved.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (DG001, blocking — currently missing entirely)
- Documented mechanism of action from DrugBank (DG002)
- Clarification of Finland market/registration status, since the drug currently shows zero licenses despite being a globally marketed generic
- Reconciliation of the FH vs. autosomal-dominant-hypercholesterolemia predictions as a single indication rather than two separate candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

