---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, typically co-formulated with ritonavir (LPV/RTV) as part of antiretroviral therapy — this is confirmed only indirectly through the supporting literature in this evidence pack, since detailed original indication and mechanism-of-action data are not currently available. The TxGNN model predicts activity against **simian immunodeficiency virus (SIV) infection**, an HIV-related lentivirus that infects non-human primates, supported by **0 clinical trials** and **3 preclinical publications**. Because the predicted indication is an animal disease rather than a human condition, and core safety data are missing, this candidate requires substantial additional validation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (inferred from literature context as HIV-1 antiretroviral therapy — see Data Gap DG002) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (preclinical/mechanism studies only, non-human primate models) |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lopinavir is not currently available in this evidence pack (Data Gap DG002, severity: High). Based on the supporting literature retrieved, lopinavir is used in combination with ritonavir (LPV/RTV) as an antiretroviral regimen "as recommended in humans" (per PMID 12951220), consistent with its known role as an HIV-1 protease inhibitor.

SIV is the simian counterpart of HIV — both are primate lentiviruses with closely related viral protease structures, which is the mechanistic basis TxGNN likely used to link lopinavir to this indication. The three supporting publications describe LPV/RTV-containing antiretroviral regimens being tested in macaques experimentally infected with SIV or SHIV (chimeric SIV/HIV) as translational models for evaluating protease inhibitor efficacy — not as a proposed human therapy for a naturally occurring human disease.

**Important caveat:** SIV infection is a disease of non-human primates, not a human condition. This prediction should be interpreted as validating lopinavir's established antiretroviral/protease-inhibitory mechanism within animal HIV-model research, rather than as a novel human repurposing opportunity. The same caution applies more strongly to the rank 2 prediction (feline acquired immunodeficiency syndrome, a cat-specific disease) and rank 3 (a human neurodevelopmental genetic disorder with no supporting evidence or clear mechanistic link to protease inhibition).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque model) | Journal of Virology | Studied viral decay kinetics in SIVmac251-infected cynomolgus macaques receiving a 7-day quadruple antiretroviral regimen |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical (macaque model) | Microbes and Infection | Constructed a chimeric SHIV bearing the HIV-1 protease gene to enable in vivo testing of protease inhibitors in rhesus macaques |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (macaque model) | Journal of Virological Methods | Evaluated oral HAART (AZT + 3TC + Lopinavir/Ritonavir, human-recommended dosing) effects on CD8 subsets in SHIV(89.6P)-infected macaques |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data is flagged as a Blocking data gap (DG001) — this must be resolved before any safety-based decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (SIV infection) is a disease of non-human primates rather than a human condition, so the current evidence — while mechanistically plausible given lopinavir's known protease-inhibitor class — does not translate into an actionable human repurposing opportunity. Combined with a Blocking safety data gap and the drug's unmarketed status in Finland, there is insufficient basis to proceed.

**To proceed, the following is needed:**
- TFDA/regulatory package insert warnings and contraindications (Data Gap DG001, Blocking)
- Confirmed original indication and mechanism-of-action data for lopinavir (Data Gap DG002)
- Reassessment of whether any of the three predicted indications have a genuine human-relevant analog worth pursuing (SIV → HIV-related human indications, if any; FIV and the neurodevelopmental disorder currently show no mechanistic or evidentiary support)
- If pursuing an HIV-adjacent human indication, dedicated clinical trial and literature search using human-relevant disease terms rather than the animal-model terms currently predicted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

