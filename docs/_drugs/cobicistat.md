---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: From HIV Pharmacokinetic Boosting to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Cobicistat is not itself an antiviral agent — it is a pharmacokinetic booster (CYP3A4/CYP2D6, P-gp, and OATP1B1/1B3 inhibitor) co-formulated with antiretroviral drugs such as elvitegravir and atazanavir for HIV treatment. The TxGNN model predicts it may be relevant to **Simian Immunodeficiency Virus (SIV) Infection**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and rests entirely on graph-embedding similarity to HIV-related nodes.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text available — cobicistat is not marketed in Finland; globally known as a pharmacokinetic booster used alongside antiretroviral agents (no direct antiviral activity of its own) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in the evidence pack. Based on available pharmacological knowledge, cobicistat is a structural analog of ritonavir and acts as a potent inhibitor of CYP3A4/CYP2D6 and the transporters P-gp and OATP1B1/1B3. Its clinical role is to raise plasma concentrations of co-administered antiretrovirals rather than to exert direct antiviral effect.

SIV is a lentivirus infecting non-human primates and is taxonomically related to HIV, which likely explains why the TxGNN knowledge graph places cobicistat close to SIV-infection nodes — both share proximity to HIV/lentivirus-related entities in the embedding space. However, this is a topological similarity, not a demonstrated pharmacological one: cobicistat has no known direct antiviral activity against SIV or HIV itself, and SIV infection is a veterinary/animal-model disease rather than a human clinical indication.

The two other TxGNN candidates in this pack reinforce the same caution: feline immunodeficiency syndrome (rank 2) is likewise a veterinary lentivirus condition inferred purely from retrovirus homology, and the rare neurodevelopmental white-matter disorder (rank 3) has no plausible mechanistic link to cobicistat's known CYP/transporter-inhibition profile. All three predictions score similarly high (~99.9%) yet have zero supporting trials or literature — consistent with a graph-embedding artifact rather than a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Cobicistat holds no marketing authorization in Finland (market status: not marketed; 0 authorizations on record), so no product/dosage-form information is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (SIV infection, feline immunodeficiency syndrome, and a rare neurodevelopmental disorder) are Evidence Level L5 — model prediction only, with no supporting clinical trials or literature — and two of the three target animal, not human, diseases. Combined with a **Blocking** data gap on TFDA/Fimea package-insert safety data (DG001), this candidate cannot proceed past initial screening (S0).

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) to clear the Blocking gap (DG001) before any S1 safety review
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Independent pharmacological or preclinical evidence connecting cobicistat's CYP3A4/P-gp/OATP inhibition to a human-relevant indication, since the current top predictions are non-human disease models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

