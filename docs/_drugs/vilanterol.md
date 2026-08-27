---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: From COPD/Asthma Bronchodilator Therapy to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a long-acting β2-adrenergic agonist (LABA) already used worldwide as a component of combination inhalers (e.g. fluticasone furoate/vilanterol, umeclidinium/vilanterol, and the triple combination FF/UMEC/VI) for COPD and asthma maintenance therapy, though it is **not currently marketed in Taiwan**. The TxGNN model predicts it may be effective for **Obstructive Lung Disease**, a signal strongly corroborated by **50 clinical trials** and **20 publications** already in the evidence pack — this is less a novel repurposing hypothesis than a confirmation of vilanterol's well-established pharmacological class effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty); based on the trial evidence itself, vilanterol is an established LABA component of COPD/asthma combination inhalers |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% (rank 636) |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on known pharmacology and the pattern of clinical trial evidence collected here, vilanterol is a long-acting β2-adrenergic receptor agonist (LABA) that relaxes bronchial smooth muscle to produce sustained (24-hour) bronchodilation. It is not marketed as a standalone agent but as a component of fixed-dose combination inhalers — fluticasone furoate/vilanterol (FF/VI), umeclidinium/vilanterol (UMEC/VI), and the triple therapy fluticasone furoate/umeclidinium/vilanterol (FF/UMEC/VI) — used globally (e.g. as Breo/Relvar Ellipta, Anoro Ellipta, Trelegy Ellipta).

The predicted indication, "Obstructive Lung Disease," is mechanistically direct: airway smooth muscle relaxation via β2-agonism is the core pharmacological rationale for treating both COPD and asthma, the two dominant obstructive lung diseases. Nearly all 50 clinical trials in this pack were conducted specifically in COPD or asthma populations, and the drug already has extensive regulatory approval in other jurisdictions for this exact disease category.

Because vilanterol's known, approved use elsewhere overlaps almost entirely with the TxGNN-predicted indication, this candidate should be interpreted primarily as a **Taiwan market-access gap** (the drug/combinations are not currently registered or marketed in Taiwan per this evidence pack) rather than a genuinely novel mechanistic repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Phase 3 | Completed | 16,568 | FF/VI vs. placebo in COPD with cardiovascular risk — assessed effect on survival |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4,233 | 12-month effectiveness study of FF/VI vs. usual maintenance therapy in asthma |
| [NCT02924688](https://clinicaltrials.gov/study/NCT02924688) | Phase 3 | Completed | 2,436 | FF/UMEC/VI triple therapy vs. FF/VI dual therapy in inadequately controlled asthma |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1,811 | FF/UMEC/VI once-daily vs. budesonide/formoterol twice-daily in COPD |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | Completed | 1,621 | FF/VI 100/25mcg vs. VI 25mcg alone in COPD — isolates contribution of FF component |
| [NCT01313650](https://clinicaltrials.gov/study/NCT01313650) | Phase 3 | Completed | 1,538 | Registrational study of UMEC/VI (Anoro) and individual components in COPD |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | Completed | 1,055 | "Closed" triple therapy (FF/UMEC/VI) vs. "open" triple therapy (FF/VI + UMEC) in COPD |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | UMEC/VI 62.5/25mcg vs. tiotropium 18mcg — lung function (trough FEV1) in COPD |
| [NCT01316900](https://clinicaltrials.gov/study/NCT01316900) | Phase 3 | Completed | 846 | GSK573719/vilanterol vs. vilanterol alone vs. tiotropium over 24 weeks in COPD |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Phase 4 | Completed | 800 | Single-inhaler triple therapy (FF/UMEC/VI) vs. tiotropium monotherapy in COPD |

*40 additional trials are available in the evidence pack (largely COPD/asthma efficacy and real-world comparative-effectiveness studies); the 10 above were selected for enrollment size, phase, and pivotal/registrational relevance.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT trial: once-daily single-inhaler triple therapy vs. dual therapy in COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT | Am J Respir Crit Care Med | IMPACT trial follow-up: FF/UMEC/VI reduced all-cause mortality vs. UMEC/VI in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy for COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN trial: FF/UMEC/VI vs. FF/VI in inadequately controlled asthma |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | RCT (subgroup) | Eur Respir J | Effect of exacerbation history on IMPACT trial outcomes |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network Meta-Analysis | Advances in Therapy | FF/UMEC/VI vs. other COPD therapies — comparative efficacy synthesis |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic Review/Meta-analysis | BMC Pulm Med | UMEC/VI vs. other bronchodilators in COPD management |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic Review | Clin Respir J | Fixed-dose UMEC/VI combination in COPD |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Review | Expert Rev Respir Med | FF/VI once-daily combination therapy for stable COPD |
| [24259654](https://pubmed.ncbi.nlm.nih.gov/24259654/) | 2014 | Review | Ann Pharmacother | Efficacy/safety of FF/VI combination for COPD maintenance |

*10 additional publications are available in the pack, including further real-world comparative-effectiveness studies (e.g. PMID 39797646, 39731707, 40619503) and pharmacokinetic/QT safety studies.*

---

## Taiwan Market Information

Vilanterol (and its combination products) currently has **no drug licenses on file and is not marketed in Taiwan** (0 authorizations). No approved product name, dosage form, or indication text is available from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan-specific warnings, contraindications, or drug interaction data were returned by this evidence pack, and the DDI database query returned no results.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical evidence base is exceptionally strong (L1 — many completed Phase 3 RCTs, including pivotal registrational and mortality-outcome trials such as IMPACT and FULFIL), and the predicted indication aligns with vilanterol's already-established international use. However, this is currently a **regulatory market-access question for Taiwan rather than an unproven repurposing hypothesis** — the drug is not marketed locally, and a Blocking data gap (missing TFDA package insert / warnings / contraindications) prevents completion of the initial safety assessment (S1).

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-priority gap, DG002)
- Formal drug-drug interaction (DDI) data, as the current query returned no results
- Confirmation of Taiwan regulatory filing/registration status for FF/VI, UMEC/VI, and FF/UMEC/VI combination products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

