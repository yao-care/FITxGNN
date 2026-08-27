---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the drug-repurposing evaluation prompt (v5) to build this report directly from the Evidence Pack — no external tool calls are needed since all data is embedded in the JSON provided.

A quick note before the report: `drug.original_indications` is empty and `taiwan_regulatory.licenses` is empty (drug not marketed in Finland), so the "Original Indication" cannot be sourced from the regulatory license text as the template default rule specifies. I've inferred it from the clinical-trial/literature context in the evidence pack itself (HR+/HER2− advanced breast cancer), which is clearly labeled below as inferred rather than regulatory-confirmed.

---

# Alpelisib: From Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib is a PI3Kα inhibitor used in HR+/HER2-negative, PIK3CA-mutated advanced or metastatic breast cancer. The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but this prediction is currently supported by **0 relevant clinical trials** and **0 supportive publications** — the only clinical trial retrieved is a drug/indication mismatch, and the only literature retrieved actually documents alpelisib-induced lung and cardiac toxicity, which runs counter to the predicted benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (HR+/HER2-negative, PIK3CA-mutated advanced/metastatic BC) — *inferred from trial/literature context; not confirmed by Finnish/Fimea regulatory data* |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for alpelisib is currently a data gap in this evidence pack (DG002). Based on known pharmacology, alpelisib is a selective PI3Kα (p110α) inhibitor approved for PIK3CA-mutated breast cancer, where it blocks aberrant PI3K/AKT/mTOR signaling driving tumor cell proliferation.

The TxGNN model's rationale for linking alpelisib to pulmonary hypertension rests on a mechanistic hypothesis: in preclinical animal models, PI3Kα signaling has been implicated in pulmonary artery smooth muscle cell proliferation and anti-apoptotic signaling, and selective p110α inhibition has been shown to prevent or reverse experimental pulmonary hypertension and right ventricular hypertrophy. This provides a theoretical basis for repurposing.

However, this mechanistic hypothesis has **not** been validated in human pulmonary hypertension populations by any trial or study in this evidence pack. On the contrary, the two literature reports retrieved describe alpelisib-associated interstitial lung disease (ILD) and PI3Kα-pathway-inhibition-associated cardiac atrophy/right ventricular dysfunction — adverse effects that point in the *opposite* direction of the intended therapeutic benefit for a patient population that, by definition, has compromised pulmonary and right-heart function. The mechanistic plausibility therefore coexists with a real safety signal that argues for caution rather than support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Real-world retrospective study of **ribociclib** (not alpelisib) in HR+/HER2- advanced/metastatic breast cancer. Flagged by relevance review as **Grade C — not relevant**: wrong drug, wrong indication (breast cancer, not pulmonary hypertension); appears to be a drug-name co-occurrence mismatch and does not support this indication. |

No clinical trial in this evidence pack actually studies alpelisib in pulmonary hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Reports alpelisib-induced interstitial lung disease in a patient with advanced breast cancer — a pulmonary **adverse-effect** signal, not supportive efficacy evidence. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical/Mechanistic | J Am Heart Assoc | PI3Kα pathway inhibition (with doxorubicin) causes biventricular cardiac atrophy and right ventricular dysfunction in animal models — a cardiotoxicity signal relevant to right-heart function, which is already compromised in pulmonary hypertension. |

Neither publication provides direct evidence of efficacy in pulmonary hypertension; both instead flag lung and cardiac safety concerns relevant to this candidate indication.

---

## Finland Market Information

Alpelisib is currently **not marketed in Finland** (`market_status: 未上市`), with 0 authorizations on record. No Fimea/marketing-authorization license data is available to summarize.

---

## Cytotoxicity (Antineoplastic Drug)

Alpelisib is classified here as antineoplastic because its known original indication is breast cancer and it belongs to a targeted oncology drug class (PI3Kα inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kα / p110α inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Not established in this evidence pack (DrugBank toxicity data not retrieved). Please refer to the package insert warnings and precautions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Given the literature signals above: pulmonary function/imaging (ILD risk), cardiac function assessment (right ventricular function, given documented biventricular atrophy/dysfunction in PI3Kα-pathway inhibition), blood glucose (class-associated hyperglycemia), liver and renal function, CBC |
| Handling Protection | Oral antineoplastic small molecule; institutional hazardous/antineoplastic drug handling precautions should be followed pending confirmation from the TFDA/Fimea package insert |

---

## Safety Considerations

All formal safety fields in this evidence pack (`key_warnings`, `contraindications`, `ddi`) are data gaps. Please refer to the package insert for safety information.

**Important signal from the literature review (not part of the formal safety dataset, but material to this decision):** the only two publications identified for this candidate describe alpelisib-associated interstitial lung disease and PI3Kα-pathway-related cardiac dysfunction — both directly relevant risks for a pulmonary hypertension population, which typically has reduced pulmonary and right-ventricular reserve.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but it is unsupported by any direct human evidence — the single clinical trial retrieved is a drug/indication mismatch, and the only literature retrieved reports adverse pulmonary and cardiac effects rather than therapeutic benefit. Combined with a Blocking data gap on TFDA/Fimea labeling (DG001) and the drug not being marketed in Finland, there is currently no basis to advance this candidate beyond model prediction (evidence level L5, decision stage S0).

**To proceed, the following is needed:**
- TFDA/Fimea package insert with confirmed warnings, contraindications, and DDI data (DG001, Blocking)
- Verified mechanism-of-action documentation from DrugBank or another primary source (DG002, High)
- A trial or study that directly evaluates alpelisib (or PI3Kα inhibition) in human pulmonary hypertension patients
- Targeted pulmonary/cardiac safety assessment to reconcile the mechanistic hypothesis against the documented ILD and cardiotoxicity signals before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

