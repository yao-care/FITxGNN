---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Aliskiren: From Hypertension to Pulmonary Hypertension Due to Lung Disease and/or Hypoxia

## One-Sentence Summary

Aliskiren is a direct renin inhibitor (DRI), a drug class originally developed to treat essential hypertension by blocking the rate-limiting step of the renin-angiotensin-aldosterone system (RAAS). The TxGNN model's top-ranked prediction suggests it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia**, but this direction is currently supported by **0 clinical trials** and **20 publications that, on review, do not actually address Aliskiren or this indication** — the evidence is essentially a keyword coincidence around "hypoxia" rather than substantive mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (based on general drug-class knowledge; not confirmed by TFDA/Fimea license data in this evidence pack — see Data Gap DG001) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Finland Market Status | ❌ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack (Data Gap DG002). Based on known public drug information, Aliskiren is a first-in-class direct renin inhibitor (DRI). Unlike ACE inhibitors or ARBs, which act downstream, Aliskiren blocks the rate-limiting step of the RAAS cascade at the point of renin activity, and its efficacy in essential hypertension is well established.

Mechanistically, one could argue that upstream RAAS blockade might extend to Group 3 pulmonary hypertension (pulmonary hypertension due to lung disease and/or hypoxia), since RAAS activation has been implicated in some models of pulmonary vascular remodeling. However, **this evidence pack does not actually support that link**. All 20 retrieved publications discuss "hypoxia" in unrelated contexts — brain aging, cognitive impairment, gastric cancer glycolysis, tumor biology, multiple sclerosis, headache — and none mention Aliskiren, renin inhibition, or the renin-angiotensin system in relation to hypoxic/lung-disease-associated pulmonary hypertension. This is best characterized as a **keyword co-occurrence artifact** ("hypoxia") rather than genuine mechanistic evidence. Furthermore, the pathophysiology of Group 3 pulmonary hypertension is primarily driven by hypoxic pulmonary vasoconstriction and vascular remodeling, not RAAS activation, so the mechanistic rationale itself is weak even before considering the absence of supporting literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review (unrelated topic) | Ageing Research Reviews | Discusses hypoxia and brain aging/neurodegeneration; no mention of Aliskiren, RAAS, or pulmonary hypertension |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review (unrelated topic) | Metabolic Brain Disease | Reviews hypoxia-induced cognitive impairment mechanisms; not related to renin inhibition or lung disease |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic research (unrelated) | Advanced Science | Gastric cancer glycolysis via NAT10/SEPT9/HIF-1α pathway under hypoxia; unrelated to Aliskiren |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review (unrelated topic) | J Cellular Biochemistry | General hypoxia biology across disease states; no drug-specific content |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review (unrelated topic) | Trends in Cancer | Deubiquitinases and hypoxia in cancer; unrelated to pulmonary hypertension |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review (unrelated topic) | Respiratory Care Clinics of N. America | Mechanisms of hypoxemia (physiology review); no drug relevance |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review (unrelated topic) | Clinical Oncology | Hypoxia and radiotherapy/cancer treatment resistance; unrelated |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review (unrelated topic) | Rev Med Inst Mex Seguro Soc | High-altitude hypoxia and human acclimatization; no drug relevance |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review (unrelated topic) | Redox Biology | Hypoxia in multiple sclerosis pathology; unrelated to Aliskiren |
| [27146279](https://pubmed.ncbi.nlm.nih.gov/27146279/) | 2017 | Review (unrelated topic) | Cephalalgia | Hypoxic mechanisms in migraine/cluster headache; unrelated |

**Note:** All 20 retrieved papers were reviewed and classified as unrelated to Aliskiren or to pulmonary hypertension due to lung disease/hypoxia specifically — they surfaced purely due to shared use of the word "hypoxia." No literature-based support for this indication currently exists.

---

## Finland Market Information

No marketing authorizations are on record for Aliskiren in Finland (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`). No product/dosage-form/indication data is available to tabulate.

---

## Other Predicted Indications (Additional Context)

The evidence pack contains 6 additional TxGNN-predicted indications for Aliskiren beyond the top-ranked one. For a complete picture of this candidate's overall repurposing potential, they are summarized below:

| Rank | Disease | Evidence Level | Recommendation | Key Note |
|------|---------|----------------|-----------------|----------|
| 2 | Pulmonary hypertension, unclear multifactorial mechanism | L5 | Hold | No trials/literature; near-identical score to rank 1 suggests knowledge-graph score propagation, not independent evidence |
| 3 | Malignant hypertensive renal disease | L4 | Hold | Only supporting literature is an unrelated C3aR/renin-fibrosis mechanistic study; **ALTITUDE trial safety signal applies (see Safety Considerations)** |
| 4 | Malignant renovascular hypertension | L5 | Hold | No trials/literature; likely graph-neighbor score bleed from rank 3 |
| 5 | Braddock syndrome (KAT6B-related) | L5 | Hold | No plausible biological link to RAAS/renin; likely a spurious model prediction — recommend excluding from further work |
| 6 | Chronic pulmonary heart disease (cor pulmonale) | L4 | **Research Question** | ALOFT Phase 2 RCT (Aliskiren add-on in heart failure) showed BNP/NT-proBNP reduction, but in systolic HF populations, not lung-disease-driven right heart failure — indirect extrapolation only |
| 7 | Cerebrovascular disorder | **L1** | Hold | Highest evidence tier in the pack, but the direction is **harmful**: the ALTITUDE Phase 3 RCT showed Aliskiren + ACEI/ARB in diabetic/renally-impaired patients *increased* ischemic stroke risk |

None of the seven predicted indications currently support a "Go" decision; the strongest-evidence finding (rank 7) is a safety signal against combination use, not a repurposing opportunity.

---

## Safety Considerations

Please refer to the package insert for safety information — no key warnings, contraindications, or drug-drug interaction data are recorded for Aliskiren in this evidence pack (TFDA/Fimea package insert not yet retrieved; see Data Gap DG001, severity: Blocking).

**Important safety signal identified during evidence review (not part of the core safety fields, but material to this candidate):**
- The **ALTITUDE trial** (Aliskiren Trial in Type 2 Diabetes Using Cardio-Renal Endpoints), a Phase 3 RCT, was stopped early and showed that Aliskiren combined with ACE inhibitors or ARBs in patients with type 2 diabetes and renal impairment significantly increased the risk of **non-fatal stroke, hyperkalemia, hypotension, and renal complications** (PMID [23418282](https://pubmed.ncbi.nlm.nih.gov/23418282/), [26188211](https://pubmed.ncbi.nlm.nih.gov/26188211/)).
- This is directly relevant to two of the higher-scoring predicted indications above (malignant hypertensive renal disease, cerebrovascular disorder), both of which involve renally-impaired or high-cardiovascular-risk populations — the same population in which ALTITUDE showed harm.
- Any further work on this candidate must formally incorporate this known dual-RAAS-blockade risk before any clinical exploration proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pulmonary hypertension due to lung disease/hypoxia) has no clinical trial support and its literature evidence is a keyword-coincidence artifact rather than genuine mechanistic or clinical evidence (Evidence Level L5). Across all seven predicted indications, only one (chronic pulmonary heart disease) has evidence trending supportive, and it is only strong enough to be framed as a research question, not an actionable candidate. The single highest-evidence-tier finding (cerebrovascular disorder, L1) is actually a **safety signal against** repurposing in RAAS-combination contexts, based on a completed Phase 3 RCT (ALTITUDE).

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action and pharmacological category data (DG002)
- If pursuing the "chronic pulmonary heart disease" research question, dedicated trials or literature evaluating Aliskiren specifically in lung-disease-driven right heart failure (cor pulmonale), not extrapolated from systolic heart failure data (ALOFT)
- A formal safety review addressing the ALTITUDE trial's stroke/hyperkalemia/renal signal before considering any indication involving renal impairment, diabetes, or combination RAAS blockade
- Independent confirmation (or exclusion) of the Braddock syndrome and other L5 predictions, which currently show no biological plausibility and may be model artifacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

