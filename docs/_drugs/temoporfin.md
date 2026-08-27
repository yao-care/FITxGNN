---
layout: default
title: Temoporfin
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Temoporfin
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

# Temoporfin: From Head and Neck Squamous Cell Carcinoma (PDT) to Benign Neoplasm of Tongue

## One-Sentence Summary

Temoporfin (mTHPC/Foscan) is a second-generation photosensitizer with an established clinical literature base in photodynamic therapy (PDT) for head and neck squamous cell carcinoma. The TxGNN model predicts it may also be effective for **Benign Neoplasm of Tongue**, currently supported by **11 publications** (mostly cohort/case series studies) but **no registered clinical trials**. The drug is not yet marketed in Finland.

*Note: This evidence pack scored 10 candidate indications for temoporfin. Benign Neoplasm of Tongue was selected as the featured candidate here because it has the strongest evidence tier (L3, decision stage S2) among all 10 — the raw #1-ranked prediction by TxGNN score alone (nasopharyngeal teratoma) has zero supporting literature/trials and was flagged by the model's own rationale as likely graph-prediction noise (Hold, L5).*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Finland license text on file); literature consistently documents established use in PDT for head and neck squamous cell carcinoma, including oral cavity and tongue base tumors |
| Predicted New Indication | Benign Neoplasm of Tongue |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L3 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, DrugBank-sourced mechanism of action data is not available for temoporfin ([Data Gap] in the drug record). However, the evidence pack's own literature base provides consistent mechanistic detail: temoporfin (mTHPC) is a second-generation photosensitizer that selectively accumulates in tumor tissue and, upon activation with 652 nm red light, generates singlet oxygen that induces tumor cell apoptosis/necrosis and local vascular damage.

The tongue and oral cavity are the anatomical sites with the deepest published PDT experience for this drug. Multiple cohort and case-series studies (early-stage oral cavity/oropharynx neoplasms, oral dysplasia, tongue base carcinoma, field cancerization of the oral cavity) directly apply mTHPC-PDT to tongue and adjacent oral tissue, including a pharmacokinetic/fluorescence-microscopy study confirming selective mTHPC localization in squamous cell carcinomas of the upper aerodigestive tract versus healthy tissue.

Mechanistically, this supports extension from established malignant head-and-neck indications to benign/early neoplastic lesions of the tongue: the same tumor-selective photosensitizer uptake and localized phototoxic ablation mechanism that clears malignant oral lesions is plausible for benign or early-stage tongue neoplasms, which is consistent with the convergent (though separately scored) evidence for the closely related "benign neoplasm of floor of mouth" indication (also L3/S2) in this same evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23775429](https://pubmed.ncbi.nlm.nih.gov/23775429/) | 2013 | Review | Lasers in Surgery and Medicine | Airway management strategies for head and neck PDT; post-operative swelling is a well-documented risk, tracheostomy often needed for tongue base tumors |
| [21412802](https://pubmed.ncbi.nlm.nih.gov/21412802/) | 2011 | Cohort | Lasers in Surgery and Medicine | PDT outcomes for oral dysplasia; minimally invasive intervention usable before/after conventional modalities |
| [20706842](https://pubmed.ncbi.nlm.nih.gov/20706842/) | 2011 | Cohort | Eur Arch Otorhinolaryngol | Outcome analysis of 170 patients (226 lesions) with early-stage oral cavity/oropharynx neoplasms treated with PDT |
| [9612194](https://pubmed.ncbi.nlm.nih.gov/9612194/) | 1996 | Cohort/Case Series | J Clin Laser Med Surg | Early PDT trial in upper aerodigestive tract using mTHPC in 27 patients with early lesions |
| [11485842](https://pubmed.ncbi.nlm.nih.gov/11485842/) | 2001 | Pharmacokinetic Study | J Photochem Photobiol B | Fluorescence microscopy confirms selective mTHPC localization in SCC of upper aerodigestive tract vs. healthy tissue |
| [24037957](https://pubmed.ncbi.nlm.nih.gov/24037957/) | 2013 | Technical/Planning Study | Lasers in Surgery and Medicine | MR/CT-based treatment planning method for mTHPC-mediated interstitial PDT of head and neck cancer |
| [26179387](https://pubmed.ncbi.nlm.nih.gov/26179387/) | 2015 | Case Series | World J Surg Oncol | Postoperative temoporfin-PDT as adjuvant treatment after robot-assisted salvage surgery for recurrent tongue base SCC with involved margins |
| [9334805](https://pubmed.ncbi.nlm.nih.gov/9334805/) | 1997 | Case Series | International Journal of Cancer | mTHPC-PDT in 19 patients with oral cancer, including field cancerization cases |
| [22152039](https://pubmed.ncbi.nlm.nih.gov/22152039/) | 2011 | Case Report | Head & Neck Oncology | mTHPC-PDT in end-stage/recurrent tongue base carcinoma; reduced tumor-associated symptoms with lower morbidity/mortality than alternatives |
| [9788423](https://pubmed.ncbi.nlm.nih.gov/9788423/) | 1998 | Preclinical | Int J Radiat Oncol Biol Phys | Interstitial mTHPC-PDT dosimetry study distinguishing tumor damage from striated muscle damage |

---

## Finland Market Information

Currently not marketed in Finland. No product licenses are on file (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple cohort and case-series studies (spanning 1996–2015) consistently support mTHPC-PDT activity in tongue and oral cavity neoplasms, giving this candidate the highest evidence tier (L3) among the 10 indications scored for temoporfin. However, evidence is limited to observational/case-series designs with no randomized controlled trials, and the drug currently has no Finland market authorization.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) and DrugBank toxicity/category data (currently [Data Gap])
- TFDA/Fimea package insert warnings and contraindications (currently [Data Gap], flagged Blocking in data gaps)
- Confirmation of the drug's formally approved original indication text (not present in this evidence pack)
- A prospective or randomized trial specifically evaluating mTHPC-PDT for benign tongue neoplasms
- Photosensitivity/light-avoidance and airway-monitoring protocol, given procedural risks noted in the literature (post-operative swelling, airway compromise)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

