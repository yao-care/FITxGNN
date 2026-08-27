---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Renal Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

Sirolimus (rapamycin) is an mTOR inhibitor originally developed as an immunosuppressant for prophylaxis of renal transplant rejection. The TxGNN model predicts it may be effective for **Liposarcoma**, with **5 clinical trials** (mostly of sirolimus-class analogues) and **12 publications** currently supporting this direction. However, a **blocking data gap** in Finnish/TFDA safety labeling means this candidate cannot yet enter formal safety screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal transplant rejection prophylaxis (immunosuppression) — well-established original use; no Finland-specific license text is available in this pack |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned no MOA field). Based on known pharmacology, sirolimus is an mTOR (mechanistic target of rapamycin) inhibitor, whose efficacy as an immunosuppressant in solid organ transplantation is well established. Mechanistically, this same mTOR-blocking activity is what is being explored for anti-tumour effect in liposarcoma.

Liposarcoma, particularly the dedifferentiated subtype, has demonstrated activation of the Akt-mTOR and MAPK signalling pathways (PMID 26518767), giving a direct mechanistic rationale for mTOR blockade as an anti-proliferative strategy. This is reinforced by class-wide evidence: sirolimus analogues (temsirolimus, ridaforolimus, everolimus) have completed multiple Phase 1/2 trials in advanced soft-tissue sarcoma and liposarcoma, including a single-arm Phase 2 trial of sirolimus itself combined with cyclophosphamide (NCT02821507, n=70, completed).

That said, no Phase 3 confirmatory trial exists for sirolimus (or its analogues) specifically in liposarcoma, and the trial evidence is drawn substantially from related rapalogs rather than sirolimus itself — the mechanistic case is stronger than the direct clinical-trial case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide, single-arm, in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; based on preclinical mTOR-inhibition tumor-growth-prevention data |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus, a sirolimus prodrug) + liposomal doxorubicin dosing study in recurrent sarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus in pediatric recurrent/refractory solid tumors (sarcoma) |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor, AP23573) once-daily x5/2-week schedule in advanced sarcoma |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib (CDK4/6i) + everolimus (mTORi) in advanced dedifferentiated liposarcoma and leiomyosarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT (Phase 2) | Clin Cancer Res | Ribociclib + everolimus shows synergistic growth inhibition in dedifferentiated liposarcoma/leiomyosarcoma models, supporting combined CDK4/mTOR targeting |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT/Cohort | J Am Soc Nephrol | Sirolimus after early cyclosporine withdrawal reduced cancer risk in renal transplant recipients (n=525) |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/Translational | Tumour Biol | Akt-mTOR and MAPK pathway activation demonstrated across 99 dedifferentiated liposarcoma specimens, supporting mTOR-targeted therapy rationale |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplant Proc | Cancer screening cohort in renal transplant patients on long-term immunosuppression |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Review of novel therapeutics (including mTOR-pathway agents) in soft tissue sarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of new molecular-targeted treatments for advanced sarcomas |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical (Xenograft) | Cancer Genomics Proteomics | Chloroquine + rapamycin synergistic autophagy inhibition effective against well-differentiated liposarcoma |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical (PDX) | In Vivo | Chloroquine + rapamycin arrests tumor growth in a patient-derived orthotopic xenograft model of dedifferentiated liposarcoma |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128, an ATP-competitive mTOR kinase inhibitor, shows potent antitumor activity in bone/soft-tissue sarcoma models |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Review of targeted treatment approaches for rare connective tissue tumors and sarcomas |

---

## Finland Market Information

Sirolimus is currently **not marketed** in Finland (0 authorizations on record), so no product/authorization data is available for this section.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/Fimea warnings, contraindications, and DDI data are currently unavailable — see Conclusion for the related blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Sirolimus is not currently marketed in Finland, and a **blocking** data gap (DG001: missing TFDA/Fimea package insert warnings and contraindications) means the candidate cannot yet enter the S1 safety pre-screening stage, regardless of the L2-level clinical/mechanistic evidence supporting liposarcoma as a repurposing target. Note also that this same evidence pack identifies other sirolimus-predicted indications (e.g., PEComa/angiomyolipoma and lymphangioleiomyomatosis) with comparably strong or stronger real-world validation (approved same-class agents everolimus and nab-sirolimus), which may warrant separate prioritization.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings and contraindications) — required to clear the blocking S1 safety gap
- Detailed mechanism of action data via DrugBank API
- Drug-drug interaction (DDI) data (current query returned no results)
- Confirmation of route/dosage-form compatibility for an oncology (liposarcoma) treatment setting, since sirolimus is currently only formulated/dosed for transplant immunosuppression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

