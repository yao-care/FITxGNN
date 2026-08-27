---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Hyponatremia (SIADH) to Autosomal Dominant Polycystic Kidney Disease (ADPKD) with Polycystic Liver Disease

## One-Sentence Summary

Tolvaptan is a vasopressin V2-receptor antagonist most widely known for treating SIADH-related hyponatremia (this evidence pack does not include a confirmed original-indication record — see data gap below). The TxGNN model predicts strong potential for **Polycystic Kidney Disease 3, with or without Polycystic Liver Disease (ADPKD/PLD)**, and this is not a purely speculative signal: **20 supporting publications**, including **2 pivotal completed Phase 3 RCTs** (TEMPO 3:4, REPRISE), already back this use in other markets, even though no trial matched this exact disease term in our clinical-trials search.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyponatremia (SIADH) — well-established use; not confirmed in this evidence pack (TFDA label data gap, DG001) |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease (ADPKD/PLD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action documentation is not available in this evidence pack (data gap DG002). Based on the TxGNN repurposing rationale, tolvaptan is understood to act as a **vasopressin V2-receptor (V2R) antagonist**, blocking cAMP generation in renal collecting-duct epithelial cells — the pathway that drives cyst expansion and total kidney volume growth in ADPKD.

Notably, this "predicted" indication is not a novel hypothesis: tolvaptan is already an approved, mechanistically-validated therapy for ADPKD in multiple countries. The evidence pack's own rationale explicitly flags this — the "未上市" (not marketed) status recorded here most likely reflects a market-specific regulatory gap (e.g., Taiwan) rather than genuine scientific uncertainty. The polycystic liver disease component of the prediction is mechanistically plausible (cAMP-driven cystogenesis is shared between renal and hepatic cysts) but is supported by weaker, indirect evidence (EASL guideline mention rather than dedicated hepatic trials).

Because V2R blockade directly targets the shared cystogenic mechanism, and because two independent Phase 3 RCTs (TEMPO 3:4 in early-stage disease, REPRISE in later-stage disease) demonstrated slowed kidney function decline, the mechanism-to-indication link here is unusually strong compared to typical TxGNN predictions.

## Clinical Trial Evidence

Currently no related clinical trials are registered under this exact predicted-disease term in the evidence pack's clinical trial search. (Note: the pivotal RCTs establishing tolvaptan's efficacy in ADPKD — TEMPO 3:4, REPRISE — are captured under Literature Evidence below rather than the structured clinical-trials field.)

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (Phase 3, TEMPO 3:4) | The New England Journal of Medicine | Tolvaptan slowed the increase in total kidney volume and the decline in eGFR versus placebo in early ADPKD — landmark trial establishing V2R antagonism as disease-modifying therapy. |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (Phase 3, REPRISE) | The New England Journal of Medicine | In later-stage ADPKD (lower eGFR), tolvaptan slowed kidney function decline versus placebo, extending efficacy evidence beyond early-stage disease. |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review & Meta-analysis | Nefrologia | Pooled analysis confirms tolvaptan's efficacy in delaying ADPKD progression to end-stage renal disease, alongside expected hepatic/renal safety signals. |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Reviews disease-modifying agents, including tolvaptan, for preventing ADPKD progression and compares relative effectiveness. |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrology, Dialysis, Transplantation | ERA Working Group consensus on practical initiation and monitoring of tolvaptan therapy in ADPKD, based on TEMPO 3:4/REPRISE evidence. |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Practice Guideline (EASL) | Journal of Hepatology | EASL guideline on management of cystic liver diseases, referencing tolvaptan's mechanistic relevance to polycystic liver disease. |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD pathophysiology and genetics, naming tolvaptan as the only approved disease-modifying therapy. |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Notes tolvaptan slows renal function decline and cyst growth in ADPKD; discusses concurrent polycystic liver disease management. |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | Randomized Trial (Pediatric) | Pediatric Nephrology | Evaluated tolvaptan safety/pharmacodynamics and progression-risk estimation in pediatric ADPKD patients (NCT02964273). |
| [29175241](https://pubmed.ncbi.nlm.nih.gov/29175241/) | 2018 | Review | Journal of Hepatology | Clinical management guidance for polycystic liver disease, including case discussion relevant to cyst-burden reduction strategies. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by L1-level evidence (two completed Phase 3 RCTs plus multi-society consensus/guideline endorsement), but Taiwan-specific regulatory and safety data (TFDA label, drug interactions) are entirely absent, so a full safety evaluation (S1) cannot be completed despite strong efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert / label — warnings and contraindications (Blocking gap, DG001)
- Official MOA confirmation via DrugBank API (High-priority gap, DG002)
- Drug-drug interaction data (tolvaptan is a known CYP3A4 substrate; interactions e.g. with strong CYP3A4 inhibitors need verification)
- Clarification of Taiwan market-entry status, since tolvaptan is already approved for this indication in multiple other jurisdictions
- Note: 9 other TxGNN-predicted indications for this drug were also screened (L4–L5 evidence) and remain on **Hold**; two of them (thoracic malformation; malformation syndrome with periodontal component) show literature entirely unrelated to the predicted disease and are likely ontology-matching artifacts, not genuine repurposing candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

