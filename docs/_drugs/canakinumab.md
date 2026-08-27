---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Autoinflammatory Syndromes to Familial Mediterranean Fever

## One-Sentence Summary

Canakinumab is a human anti-IL-1β monoclonal antibody whose established use is in IL-1β–driven autoinflammatory diseases such as Cryopyrin-Associated Periodic Syndromes (CAPS). TxGNN generated 10 candidate indications for this drug; most (7 of 10) turn out to be low-confidence or entity-mismatched signals, but **Familial Mediterranean Fever (FMF)** stands out with **7 clinical trials** (5 completed Phase 3) and **20 publications**, and is already an approved indication for canakinumab in other jurisdictions (FDA/EMA) — while the product remains unmarketed locally (0 authorizations).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoinflammatory disease (Cryopyrin-Associated Periodic Syndromes / CAPS family) — no local approved-label text available; drawn from literature evidence (PMID 20065636) |
| Predicted New Indication | Familial Mediterranean Fever (autosomal dominant) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Canakinumab is a fully human monoclonal antibody that binds and neutralizes interleukin-1β (IL-1β), the central cytokine driving inflammasome-mediated autoinflammatory disease (per literature evidence PMID 20065636, PMID 35874710). Its established efficacy is in the CAPS spectrum (FCAS, Muckle-Wells syndrome, NOMID/CINCA), where uncontrolled NLRP3-inflammasome activity leads to IL-1β overproduction.

FMF shares the same downstream biology: gain-of-function MEFV mutations dysregulate the pyrin inflammasome, driving IL-1β overactivation and recurrent fever/serositis attacks. Because canakinumab's mechanism acts directly downstream of this shared IL-1β pathway, its extension from CAPS to FMF is mechanistically coherent rather than speculative — and in fact canakinumab already carries FMF as an approved indication in other jurisdictions, per the evidence pack's own rationale ("已獲多國（含 FDA/EMA）核准之適應症，非單純 TxGNN 預測").

One caveat worth flagging: most of the pivotal trials captured under this candidate's evidence set are titled as CAPS/TRAPS/Muckle-Wells studies rather than FMF-specific studies. This likely reflects that these are the drug's foundational registrational trials for the broader hereditary periodic fever syndrome label (which was later extended to include FMF), rather than FMF being untested — the one explicitly FMF-inclusive study (NCT06838143, real-world REASSURE) is ongoing. This should be verified against the actual approved label text before final sign-off.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | Completed | 35 | Pivotal 3-part randomized, double-blind, placebo-controlled withdrawal trial establishing efficacy/safety of canakinumab in Muckle-Wells syndrome (CAPS) |
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Completed | 166 | Largest long-term (≥6 month) open-label safety/efficacy cohort across CAPS phenotypes (FCAS, MWS, NOMID) |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Completed | 19 | 6-month open-label efficacy/safety study in Japanese CAPS patients, extended pending Japan approval |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | Completed | 17 | One-year open-label multicenter trial assessing efficacy, safety and tolerability in patients ≤4 years, including childhood vaccination safety |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Completed | 17 | Open-label extension providing long-term efficacy/safety/tolerability data in CAPS patients |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | Completed | 20 | 4-month multicenter dose-finding study of canakinumab in active recurrent/chronic TRAPS |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | Recruiting | 25 | Real-world non-interventional safety/effectiveness study (REASSURE) explicitly covering colchicine-resistant FMF (crFMF), CAPS, TRAPS, HIDS/MKD, sJIA; ongoing through 2028 |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic Review | Frontiers in Immunology | Systematic review of safety/efficacy of IL-1-targeted biologics (anakinra, canakinumab, rilonacept) across immune-mediated autoinflammatory disorders |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Systematic Review / Meta-analysis | Rheumatology (Oxford) | Efficacy and safety of anti-IL-1 treatment specifically in FMF patients unresponsive/intolerant to colchicine |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Review | New England Journal of Medicine | Canakinumab evaluated across monogenic autoinflammatory recurrent fever syndromes including FMF, MKD/HIDS and TRAPS |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohort | Int J Rheum Dis | Compares attack characteristics, acute-phase reactants and renal outcomes in FMF patients on canakinumab with/without colchicine |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Review | Turkish J Med Sci | Contemporary review of FMF pathogenesis through treatment, including biologic options |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Review | Presse Médicale | Overview of FMF epidemiology, MEFV/pyrin pathophysiology and treatment |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Review | Expert Rev Clin Immunol | Focused review of canakinumab specifically for FMF treatment |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Review | Clin Exp Rheumatol | IL-1 inhibition in FMF: clinical outcomes and expectations |
| [31205631](https://pubmed.ncbi.nlm.nih.gov/31205631/) | 2019 | Review | Mediterr J Hematol Infect Dis | FMF clinical impact and treatment plan formulation |
| [34684086](https://pubmed.ncbi.nlm.nih.gov/34684086/) | 2021 | Review | Medicina (Kaunas) | Amyloidosis and glomerular disease as FMF complications, relevant to treatment goals |

## Other TxGNN-Predicted Indications (Screened, Not Pursued)

For transparency: this evidence pack scored 10 candidate indications for canakinumab. Beyond FMF, only two others showed genuine (if preliminary) mechanistic and literature support; the remaining seven were flagged internally as likely database entity-mismatches with no real supporting evidence.

| Disease | Evidence Level | Recommendation | Note |
|---|---|---|---|
| Periodic fever-infantile enterocolitis-autoinflammatory syndrome | L3 | Research Question | 19 publications, but concentrated on related-but-distinct CAPS/FMF/PFAPA syndromes rather than this specific entity |
| Blau syndrome | L3 | Research Question | NOD2-driven granulomatous autoinflammation; small case series and a transcriptional-response cohort support IL-1β blockade, no controlled trials |
| Hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis, extracutaneous mastocytoma, liver angiosarcoma | L5 | Hold | No clinical trials; ≤1 unrelated literature hit each; judged as knowledge-graph association errors |
| Syndrome with combined immunodeficiency, monosomy X | L4–L5 | Hold | Literature retrieved concerns unrelated drugs/diseases; disease-label mismatch |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
FMF has L1-grade evidence — five completed Phase 3 trials across the CAPS/TRAPS/FMF autoinflammatory disease family plus an ongoing real-world FMF-inclusive study, and 10+ dedicated FMF publications — and canakinumab already holds this indication in other major markets (FDA/EMA). However, the drug is currently unmarketed locally (0 authorizations), and two Blocking/High-severity data gaps prevent a full safety sign-off.

**To proceed, the following is needed:**
- Local package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank/MOA documentation for the local regulatory dossier — currently a High-severity data gap (DG002)
- Completion of the local drug-drug interaction (DDI) query, currently returning "not found"
- Confirmation of local filing/registration status and pathway for canakinumab given its current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

