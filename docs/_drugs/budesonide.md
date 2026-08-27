---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Corticosteroid Anti-Inflammatory Therapy to Bronchitis

## One-Sentence Summary

> Budesonide is a well-established inhaled/topical corticosteroid; the evidence pack does not record its specific licensed original indication or detailed MOA text, but its class-wide mechanism (local anti-inflammatory, glucocorticoid activity) is well documented.
> Among 10 TxGNN-predicted indications, **Bronchitis** is the only one with a fully completed evidence assessment (Evidence Level **L1**, Decision Stage **S3**), supported by **17 clinical trials** and **22 publications**.
> Note: "Atopic eczema" scores marginally higher on the raw TxGNN metric, but its clinical/literature relevance grading is still marked "pending" in this evidence pack, so it is not yet actionable — this report focuses on Bronchitis as the most mature candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack — `original_indications` and Finland license records are empty (see DG001/DG002 data gaps) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.81% (rank 2,511 overall) |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Budesonide in this evidence pack (DG002, High severity). Based on known information, Budesonide is a corticosteroid used in inhaled and topical formulations, and mechanistically its anti-inflammatory activity is directly applicable to airway inflammatory disease.

As an inhaled corticosteroid (ICS), budesonide suppresses airway inflammation, reduces eosinophilic infiltration, and decreases mucosal edema. This is already the standard mechanism underlying its use in asthma, COPD, and chronic bronchitis management (e.g., in combination products such as budesonide/formoterol). The mechanistic link to bronchitis is therefore direct and clinically mature, rather than a speculative cross-disease extrapolation.

The clinical trial record reinforces this: several trials use budesonide (often combined with formoterol) specifically in eosinophilic bronchitis, chronic bronchitis without obstruction, and bronchiolitis obliterans — conditions that sit on the same inflammatory-airway spectrum as the predicted indication. This convergence of an established mechanism with condition-relevant trial activity is what supports the L1 evidence rating.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02002715](https://clinicaltrials.gov/study/NCT02002715) | Phase 4 | Completed | 106 | Randomized, open-label comparison of different inhaled corticosteroid treatment durations in eosinophilic bronchitis patients; evaluates cough score and sputum eosinophil recovery |
| [NCT00202189](https://clinicaltrials.gov/study/NCT00202189) | Phase 4 | Completed | 4 | Acute effects of inhaled corticosteroids on dynamic airway function (blood flow, resistance, hyperinflation) at rest and exercise in COPD |
| [NCT00624754](https://clinicaltrials.gov/study/NCT00624754) | Phase 2 | Completed | 32 | Prospective evaluation of budesonide/formoterol (Symbicort) efficacy in bronchiolitis obliterans after allogeneic stem cell transplant |
| [NCT01560689](https://clinicaltrials.gov/study/NCT01560689) | Phase 2 | Completed | 32 | Open-label trial of inhaled budesonide/formoterol for bronchiolitis obliterans after allogeneic stem cell transplantation |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Randomized double-blind placebo-controlled trial of add-on montelukast to inhaled budesonide for non-asthmatic eosinophilic bronchitis |
| [NCT01023516](https://clinicaltrials.gov/study/NCT01023516) | Phase 2 | Completed | 615 | Phase IIb study of oral AZD9668 vs placebo added to budesonide/formoterol background therapy in COPD |
| [NCT00483743](https://clinicaltrials.gov/study/NCT00483743) | Phase 2 | Completed | 62 | Multi-center double-blind study comparing inhaled TPI 1020 vs inhaled budesonide vs placebo on safety, tolerability and pharmacodynamics in COPD |
| [NCT02526758](https://clinicaltrials.gov/study/NCT02526758) | Phase 4 | Unknown | 90 | Evaluation and treatment of small airway disease (obstructive/chronic bronchitis) in COPD using impulse oscillation system |
| [NCT06571942](https://clinicaltrials.gov/study/NCT06571942) | Phase 4 | Recruiting | 128 | Randomized controlled trial comparing inhaled triple/double therapies on small airway function in COPD and chronic bronchitis without obstruction from biomass exposure |
| [NCT03436225](https://clinicaltrials.gov/study/NCT03436225) | Phase 1 | Unknown | 80 | Evaluation of steroid therapy efficacy and hospital stay in acute bronchiolitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10780759](https://pubmed.ncbi.nlm.nih.gov/10780759/) | 2000 | RCT | European Respiratory Journal | Inhaled budesonide reduces airway inflammation, responsiveness, and cough in eosinophilic bronchitis patients |
| [37696312](https://pubmed.ncbi.nlm.nih.gov/37696312/) | 2023 | RCT | Respiratory Medicine | Tiotropium add-on to budesonide/formoterol improves pulmonary function and CAT scores in bronchiolitis obliterans after HSCT |
| [37954384](https://pubmed.ncbi.nlm.nih.gov/37954384/) | 2023 | Meta-analysis | Heliyon | Systematic review of budesonide + ambroxol inhalation for childhood pneumonia/bronchitis and its effect on inflammatory response |
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chronic Obstr Pulm Dis | Comparative risk analysis of budesonide/formoterol vs placebo/monotherapy in stable COPD |
| [11129126](https://pubmed.ncbi.nlm.nih.gov/11129126/) | 2000 | Review | Drugs | Review of inhaled budesonide suspension use in infants, children and adults with inflammatory respiratory disorders |
| [40284499](https://pubmed.ncbi.nlm.nih.gov/40284499/) | 2025 | Review | Pharmaceutics | Review of budesonide's anti-inflammatory and cell-plasticity effects across mucosal inflammatory diseases including bronchitis |
| [28810628](https://pubmed.ncbi.nlm.nih.gov/28810628/) | 2017 | Cohort | Experimental and Therapeutic Medicine | Oxygen-driven aerosol budesonide + terbutaline sulfate improves outcomes in pediatric asthmatic bronchitis |
| [35432356](https://pubmed.ncbi.nlm.nih.gov/35432356/) | 2022 | Cohort | Frontiers in Immunology | Eosinophil progenitor differentiation compared across non-asthmatic eosinophilic bronchitis, eosinophilic asthma, and controls |
| [30471087](https://pubmed.ncbi.nlm.nih.gov/30471087/) | 2018 | Preclinical | Medical Science Monitor | Budesonide combined with Astragaloside IV reduces bronchitis severity in rats via Nrf2/Keap1 pathway regulation |
| [40761058](https://pubmed.ncbi.nlm.nih.gov/40761058/) | 2025 | Cohort | Pakistan Journal of Pharmaceutical Sciences | Combination of mucolytic, bronchodilator and budesonide anti-inflammatory therapy improves secretion management and recovery time in pediatric bronchitis |

---

## Finland Market Information

Budesonide currently has **no marketing authorization on file** in Finland (`market_status`: 未上市 / Not Marketed, `total_licenses`: 0). No product-level licensing data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (TFDA package insert retrieval is flagged as a **Blocking** data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Budesonide's mechanism (ICS anti-inflammatory activity) is directly relevant to bronchitis, and evidence level L1 is supported by multiple completed Phase 4 trials and RCTs/meta-analyses in closely related conditions (eosinophilic bronchitis, chronic bronchitis, bronchiolitis obliterans). However, most trials target adjacent diagnoses rather than a "bronchitis" label per se, and the drug is not currently marketed in Finland with no local safety documentation on file.

**To proceed, the following is needed:**
- TFDA/Finland package insert retrieval — warnings, contraindications, DDI (Blocking, DG001)
- Confirmed original indication and MOA text from DrugBank or regulatory source (High priority, DG002)
- A dedicated feasibility review of Finland market entry given current "Not Marketed" status
- Disease-specific trial mapping to confirm whether "bronchitis" (vs. the more granular eosinophilic bronchitis / COPD-related chronic bronchitis subtypes seen in the trial evidence) is the correct target label for regulatory purposes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

