---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide: From Unmarketed Status to Pulmonary Arterial Hypertension

## One-Sentence Summary

> Nitric Oxide (NO) currently has no documented original indication or market presence in Finland (0 authorizations on file). Among the 10 candidate indications TxGNN generated for this drug, **Pulmonary Arterial Hypertension** is the one with genuine evidentiary support — **50 clinical trials** and **20 publications** — reflecting NO's well-established pharmacology as an inhaled pulmonary vasodilator, rather than a novel repurposing hypothesis.

*Note on indication selection: TxGNN's numerically top-ranked predictions for this drug (ranks 1–6: periodontal malformation syndrome, hypertrichosis, Dandy-Walker syndrome, hair shaft abnormality, pulmonary arteriovenous malformation) carry no supporting mechanism and were scored "Hold" by the evidence pipeline itself. Rank 7, Pulmonary Arterial Hypertension, is the first prediction with a coherent mechanism and Level-1 evidence, so this report evaluates that indication.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (drug is unmarketed in Finland; no license records) |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for this NO entry is not available (flagged as a High-severity data gap), and no original indication is on file. Based on the supporting literature in this evidence pack, however, Nitric Oxide's pharmacology is well characterized: it is an endogenous, endothelium-derived signaling gas that activates soluble guanylate cyclase, raising intracellular cGMP and producing selective pulmonary vasodilation. This is the core mechanism cited across the review literature retrieved here (PMID 32442078, PMID 23822809).

Pulmonary Arterial Hypertension is pathophysiologically defined by pulmonary vascular remodeling and impaired NO bioavailability/signaling in the pulmonary endothelium. Restoring this pathway — either directly via inhaled NO or indirectly via downstream drugs (PDE5 inhibitors, soluble guanylate cyclase stimulators) that amplify the NO–cGMP axis — is already a recognized pillar of PAH treatment, alongside the endothelin and prostacyclin pathways. Inhaled NO itself has an established clinical role in acute pulmonary vasoreactivity testing and in neonatal persistent pulmonary hypertension (PPHN), where it is a standard-of-care therapy.

The strength of this candidate over the other nine predictions is that it is not an extrapolation from disease-embedding similarity alone: it is directly supported by a completed Phase 4 head-to-head hemodynamic trial (NCT04231084, iNO vs. inhaled epoprostenol) and a pivotal completed trial in neonatal PPHN (NCT00139217, n=400), plus 18 mechanistic/clinical reviews. Two closely related predictions in the same evidence pack — PAH associated with congenital heart disease (rank 8) and PAH associated with connective tissue disease (rank 9) — reinforce the same NO-pathway mechanism across different PAH subtypes, which further supports the plausibility of this signal rather than undermining it.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04231084](https://clinicaltrials.gov/study/NCT04231084) | Phase 4 | Completed | 115 | Direct acute hemodynamic comparison of inhaled NO vs. inhaled epoprostenol across PH phenotypes |
| [NCT00139217](https://clinicaltrials.gov/study/NCT00139217) | N/A | Completed | 400 | Pivotal trial establishing feasibility/safety/efficacy of non-invasive inhaled NO in PPHN |
| [NCT05213676](https://clinicaltrials.gov/study/NCT05213676) | Phase 4 | Recruiting | 600 | "NoNO Trial" — stepped-wedge de-implementation study of iNO in congenital diaphragmatic hernia |
| [NCT01142219](https://clinicaltrials.gov/study/NCT01142219) | Phase 3 | Completed | 40 | RCT of L-arginine (NO precursor) as adjuvant therapy for sickle-cell-associated PAH |
| [NCT07099144](https://clinicaltrials.gov/study/NCT07099144) | Phase 4 | Recruiting | 120 | Multi-center safety study of INOmax + ventilatory support for neonatal hypoxic respiratory failure with PH |
| [NCT01959828](https://clinicaltrials.gov/study/NCT01959828) | Phase 3 | Completed | 18 | IK-3001 inhaled NO for PH associated with cardiac surgery (Japan) |
| [NCT00955487](https://clinicaltrials.gov/study/NCT00955487) | Phase 2 | Completed | 124 | Low-dose iNO to reduce bronchopulmonary dysplasia and associated PH in premature infants |
| [NCT01265888](https://clinicaltrials.gov/study/NCT01265888) | Phase 2 | Completed | 31 | Dose-escalation study of inhaled NO (GeNOsyl system) in PAH and PH secondary to IPF |
| [NCT03132428](https://clinicaltrials.gov/study/NCT03132428) | N/A | Terminated | 140 | Observational registry of neonates with PH receiving inhaled NO via invasive/non-invasive ventilation |
| [NCT05356052](https://clinicaltrials.gov/study/NCT05356052) | N/A | Available | N/A | Expanded access program providing pulsed inhaled NO (INOpulse) for PH-related serious conditions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33773120](https://pubmed.ncbi.nlm.nih.gov/33773120/) | 2021 | RCT | Lancet Respir Med | REPLACE trial: switching PAH patients from PDE5 inhibitors to riociguat (same NO–cGMP pathway) |
| [32442078](https://pubmed.ncbi.nlm.nih.gov/32442078/) | 2020 | Review | Curr Med Chem | The NO pathway in PAH: pathomechanism, biomarkers, and drug targets |
| [23822809](https://pubmed.ncbi.nlm.nih.gov/23822809/) | 2013 | Review | Am J Respir Crit Care Med | NO deficiency and endothelial dysfunction as a driver of PAH pathogenesis |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Diagnosis and treatment overview of PAH |
| [38054614](https://pubmed.ncbi.nlm.nih.gov/38054614/) | 2024 | Review | Small | Inhalable NO delivery systems (NO-releasing microspheres) for PAH treatment |
| [38416633](https://pubmed.ncbi.nlm.nih.gov/38416633/) | 2024 | Meta-analysis | Eur Heart J | Individual participant data network meta-analysis of PAH treatment pathways, including NO pathway |
| [15194181](https://pubmed.ncbi.nlm.nih.gov/15194181/) | 2004 | Review | J Am Coll Cardiol | NO pathway and phosphodiesterase inhibitors in PAH |
| [40341051](https://pubmed.ncbi.nlm.nih.gov/40341051/) | 2025 | Review | Eur Respir J | Drugs targeting novel pathways in PAH, including established NO-pathway agents |
| [33836637](https://pubmed.ncbi.nlm.nih.gov/33836637/) | 2021 | Review | J Cardiovasc Pharmacol Ther | Combination therapy in PAH targeting the NO and prostacyclin pathways |
| [39580019](https://pubmed.ncbi.nlm.nih.gov/39580019/) | 2025 | Systematic review/meta-analysis | Nitric Oxide | NOS3 gene polymorphism and PAH risk |

---

## Finland Market Information

Nitric Oxide is currently **not marketed** in Finland under this evidence pack's data pull — no marketing authorizations, products, or approved-indication texts are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Pulmonary Arterial Hypertension prediction is backed by L1-level evidence — a completed Phase 4 head-to-head hemodynamic trial and a pivotal 400-patient PPHN trial, plus a substantial, mechanistically coherent literature base — making it far stronger than the other nine TxGNN predictions for this drug, most of which were assessed as model noise. However, at the candidate level, the **TFDA/Fimea package insert (warnings and contraindications) is flagged as a Blocking data gap**, meaning this candidate cannot yet formally enter the S1 safety review stage.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently Blocking; required before any S1 safety assessment
- Mechanism-of-action documentation from DrugBank — currently a High-severity gap
- Confirmation of Finland licensing/market status, since inhaled NO is a clinically established gas therapy elsewhere and the "0 licenses / not marketed" result here may reflect a data collection gap rather than true absence from market
- Drug interaction (DDI) data, which returned no results in this pull
- A dedicated safety monitoring plan for inhaled NO administration (e.g., methemoglobinemia risk, NO2 formation, rebound pulmonary hypertension on withdrawal) before clinical use in the PAH population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

