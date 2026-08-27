---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease (VOD/SOS) Prevention to Thrombotic Thrombocytopenic Purpura

> **Methodology note:** TxGNN's raw #1–#3 and #5–#9 ranked predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, congenital Factor V deficiency, etc.) are all **congenital bleeding disorders**. The evidence pack's own rationale flags these as mechanistically backwards — defibrotide is an antithrombotic/profibrinolytic agent, and using it for diseases that already impair clotting could worsen bleeding rather than help. None of these six have any supporting trial or literature evidence (all L5/Hold). This report instead focuses on **Thrombotic Thrombocytopenic Purpura (rank 4)**, the only candidate with real clinical evidence and a mechanistically coherent rationale (the near-identical "thrombocytopenic purpura" at rank 10 shares the same literature set and conclusion).

## One-Sentence Summary

Defibrotide's established clinical use — visible in this evidence pack via trial NCT02851407 — is prevention of hepatic veno-occlusive disease/sinusoidal obstruction syndrome (VOD/SOS) in patients undergoing hematopoietic stem cell transplant (HSCT). The TxGNN model's best-supported new-indication signal is **Thrombotic Thrombocytopenic Purpura (TTP)**, backed by **11 publications** (cohort studies, reviews, and case reports/series spanning 1984–2023) but **no completed clinical trials**. Critically, one of those publications reports TTP developing *after* defibrotide therapy, so this remains an open safety question rather than a settled efficacy signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally captured in this evidence pack (original indication/MOA fields are data gaps); trial evidence (NCT02851407) indicates defibrotide's established use is VOD/SOS prophylaxis in HSCT patients |
| Predicted New Indication | Thrombotic Thrombocytopenic Purpura |
| TxGNN Prediction Score | 99.71% (rank 3,665 of scored pairs) |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for defibrotide is flagged as a data gap in this pack (DG002, High severity). However, the repurposing rationale attached to the evidence itself describes defibrotide as having **endothelial-protective and antithrombotic/profibrinolytic activity** — consistent with its known role in preventing microvascular thrombosis and endothelial injury in VOD/SOS after HSCT.

TTP and transplant-associated thrombotic microangiopathy (TA-TMA) share the same underlying pathophysiology as VOD/SOS: endothelial injury and microvascular thrombus formation. This mechanistic overlap is why multiple independent case series and cohort reports from 1984–2002 explored defibrotide in TTP/TA-TMA/HUS, and why a 2023 in-vitro study found defibrotide mitigates endothelial cell injury induced by plasma from TMA-related conditions (including COVID-19 vasculopathy).

That said, the evidence is entirely observational — no RCTs exist for this indication — and one 1994 case report describes the opposite causal direction (TTP occurring *after* defibrotide treatment), which must be weighed against the treatment-oriented reports before any clinical hypothesis is pursued.

## Clinical Trial Evidence

Currently no related clinical trials registered for Thrombotic Thrombocytopenic Purpura.

*(Note: trial NCT02851407 — a completed Phase 3 HARMONY study of defibrotide for VOD/SOS prophylaxis — appears elsewhere in this evidence pack under "primary release disorder of platelets," but was graded Relevance "C": its actual indication is VOD/SOS, not a platelet-release disorder, and its primary endpoint was negative. It is not counted as supporting evidence for TTP.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Review | Rinsho Ketsueki | Management of transplant-associated thrombotic microangiopathy (TA-TMA) |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Review | Bone Marrow Transplant | Diagnosis/treatment progress in transplantation-associated TMA |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Review | Drugs | TMA in HSCT: diagnosis and treatment, incidence 0.5–76%, mortality 60–90% despite treatment |
| [11100281](https://pubmed.ncbi.nlm.nih.gov/11100281/) | 2000 | Cohort | Bone Marrow Transplant | TTP incidence/risk factors in 131 leukemic children after BMT |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Cohort | Bone Marrow Transplant | "Defibrotide as a promising treatment for TTP in patients undergoing BMT" |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Case Report | Clin Appl Thromb Hemost | Defibrotide used in recurrent/relapsed TTP |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | Case Report (adverse) | Haematologica | **TTP occurring after defibrotide therapy** — opposite-direction safety signal |
| [8317470](https://pubmed.ncbi.nlm.nih.gov/8317470/) | 1993 | Case Series | Am J Hematol | Treatment of TTP with defibrotide |
| [6547211](https://pubmed.ncbi.nlm.nih.gov/6547211/) | 1984 | Case Series | Nephron | Defibrotide as antithrombotic agent in acute renal failure due to HUS/TTP |
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | Basic Science (in vitro) | Thrombosis Research | Defibrotide mitigates endothelial injury from COVID-19/TMA patient plasma |

## Finland Market Information

Defibrotide is **not currently marketed in Finland** — 0 authorizations are on file in this evidence pack.

## Safety Considerations

No structured safety data (key warnings, contraindications, DDI) are available for defibrotide in this evidence pack — please refer to the package insert for safety information.

One evidence-derived signal worth flagging separately: PMID 7896218 (Haematologica, 1994) reports a case of TTP developing **after** defibrotide administration, indicating the drug–disease relationship for this indication may run in either direction and needs dedicated causality assessment before any clinical hypothesis is advanced.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TTP signal is mechanistically plausible and has multi-decade observational support, but rests entirely on cohort/case-level evidence with no RCTs, and includes at least one report of the opposite causal direction. Formal safety data (TFDA/package-insert warnings, DDI) and MOA confirmation are both outstanding blocking/high-severity gaps (DG001, DG002), so this cannot yet clear even an initial safety screen.

**To proceed, the following is needed:**
- TFDA/EMA package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Adjudication of the causality conflict between defibrotide-as-treatment (PMID 11960280, 10775024, 8317470) vs. defibrotide-as-trigger (PMID 7896218) for TTP
- A prospective or registry-based study, since no RCT currently exists for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

