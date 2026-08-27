---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Castration-Resistant Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a second-generation taxane originally developed for metastatic castration-resistant prostate cancer (mCRPC) after docetaxel failure. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **0 registered clinical trials** matched to this indication but **20 supporting publications** — including one completed Phase II RCT directly testing cabazitaxel in breast cancer — currently backing this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic castration-resistant prostate cancer (per literature evidence in this pack; official Finnish label text unavailable — drug is not marketed in Finland) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data is not available for cabazitaxel in this evidence pack. Based on information contained in the literature evidence, cabazitaxel is a second-generation taxane and microtubule-stabilizing antimitotic agent: it binds tubulin to stabilize microtubules and arrest mitosis, in the same manner as docetaxel and paclitaxel, but was specifically engineered to reduce affinity for P-glycoprotein (P-gp) efflux pumps, giving it activity in taxane-resistant tumor cell lines (PMID 25416788, 26651178).

Cabazitaxel's original indication (mCRPC) and the predicted new indication (breast carcinoma) are both solid tumors for which taxane-class chemotherapy (paclitaxel, docetaxel) is already a clinical standard of care. Cabazitaxel's improved resistance profile is mechanistically relevant to breast cancer, where acquired resistance to earlier-generation taxanes is a recognized clinical problem.

This is not purely theoretical: a completed Phase II RCT (GENEVIEVE, PMID 28768217) already compared neoadjuvant cabazitaxel against weekly paclitaxel in operable triple-negative and luminal B/HER2-negative breast cancer, and a Phase I/II dose-escalation study (PMID 21339064) tested cabazitaxel plus capecitabine in metastatic breast cancer after anthracycline/taxane failure — indicating clinical-stage investigation of this indication already exists, beyond model prediction alone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | RCT (Phase II) | European Journal of Cancer | GENEVIEVE study: randomised neoadjuvant cabazitaxel vs weekly paclitaxel in operable TNBC/luminal B/HER2-negative breast cancer, comparing pathological complete response rates |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II (dose-escalation) | European Journal of Cancer | Cabazitaxel + capecitabine in metastatic breast cancer progressing after anthracycline/taxane treatment; established MTD, PK, and safety profile |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical (mechanistic) | Journal for ImmunoTherapy of Cancer | Cabazitaxel modulates tumor-associated macrophages, enhancing CD47-targeted immunotherapy efficacy in triple-negative breast cancer models |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Preclinical (resistance mechanisms) | Molecular Cancer Therapeutics | Characterized cabazitaxel resistance in MCF-7 breast cancer cell-derived resistant variants; showed lower cross-resistance than paclitaxel/docetaxel |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review (PK/TDM) | British Journal of Clinical Pharmacology | Review of taxane pharmacology including cabazitaxel PK/PD and therapeutic drug monitoring considerations |
| [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/) | 2016 | Review (pharmacology/patents) | Expert Opinion on Therapeutic Patents | Reviews taxane development including cabazitaxel; notes related taxane nab-paclitaxel's approval for refractory/metastatic breast cancer |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical (PDX model) | Journal of Controlled Release | Cabazitaxel-loaded PEBCA nanoparticles achieved complete remission in 6/8 basal-like breast cancer patient-derived xenografts, outperforming free drug |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | Preclinical (drug delivery) | Acta Pharmacologica Sinica | Cabazitaxel-loaded polymeric micelles showed enhanced anti-metastatic efficacy in breast cancer metastasis models |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical (drug delivery) | Chemistry and Physics of Lipids | Cabazitaxel + thymoquinone co-loaded lipospheres developed as a synergistic combination targeting p53/STAT3/Bax/BCL-2 pathways in breast cancer |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclinical (drug delivery) | Colloids and Surfaces B: Biointerfaces | Cabazitaxel-loaded nanostructured lipid carriers (NLCs) optimized and evaluated against breast cancer cell lines |

## Finland Market Information

Cabazitaxel is not currently marketed in Finland — no marketing authorizations are registered (0 licenses on file).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane class, microtubule-stabilizing antimitotic agent) |
| Myelosuppression Risk | High — neutropenia is reported as one of the most common adverse effects of cabazitaxel in the literature (PMID 21076710) |
| Emetogenicity Classification | Please refer to the package insert |
| Monitoring Items | CBC with differential (neutropenia), peripheral neuropathy assessment, renal and hepatic function |
| Handling Protection | Standard cytotoxic drug handling precautions required (PPE, closed-system transfer device) |

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/Fimea label warnings, contraindications, and drug interaction data are currently unavailable — flagged as a blocking data gap for formal safety review.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic plausibility is supported by the established role of taxanes in breast cancer treatment, and this specific indication already has clinical-stage investigation — one completed Phase II RCT (GENEVIEVE) and one Phase I/II dose-escalation study — rather than being purely a model prediction. However, no clinical trials are currently indexed against this exact indication, and Finnish regulatory/safety data are entirely absent, justifying guardrails rather than an unconditional Go.

**To proceed, the following is needed:**
- Official package insert / label safety data (warnings, contraindications, DDI) — currently a blocking data gap
- Confirmed DrugBank mechanism-of-action record
- Efficacy outcomes from the GENEVIEVE trial (PMID 28768217) and the Phase I/II capecitabine combination study (PMID 21339064)
- A breast cancer-specific safety monitoring plan addressing myelosuppression and neuropathy risk, given the drug is not currently marketed in Finland
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

