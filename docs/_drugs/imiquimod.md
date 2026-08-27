---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

Using the evidence pack's top-ranked prediction (pre-malignant neoplasm, TxGNN score 0.9992, evidence level L2) as the primary candidate, consistent with the template's single-indication structure.

# Imiquimod: From Actinic Keratosis / Superficial Basal Cell Carcinoma to Pre-Malignant Neoplasm

## One-Sentence Summary

> Imiquimod is a topical Toll-like receptor 7 (TLR7) agonist, established for actinic keratosis, superficial basal cell carcinoma, and external genital warts.
> The TxGNN model predicts it may be effective more broadly for **Pre-Malignant Neoplasm**,
> with **19 clinical trials** and **9 publications** — including two Cochrane systematic reviews — currently supporting this direction, though the drug is not marketed in Finland.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Actinic keratosis, superficial basal cell carcinoma, external genital warts (topical; per repurposing rationale — no formal Finland/TFDA license record on file) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data was not returned by DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). However, the evidence pack's own repurposing rationale documents imiquimod's known pharmacology: it is a TLR7 agonist that induces local interferon-α and cytokine release and activates cytotoxic T cells, driving immune-mediated clearance of abnormal epithelial cells. This mechanism underlies its established topical use for actinic keratosis, superficial basal cell carcinoma, and anogenital warts.

"Pre-malignant neoplasm" as a predicted indication is mechanistically close to the original use case rather than a distant repurposing leap — actinic keratosis and superficial BCC are themselves pre-malignant/early-malignant epithelial lesions. The predicted expansion covers other HPV- and UV-driven dysplastic conditions (cervical, vulvar, and anal intraepithelial neoplasia; lentigo maligna; Bowenoid papulosis) that share the same underlying biology: localized abnormal epithelial proliferation amenable to immune-mediated clearance via TLR7 activation. This is why the same drug class already has direct trial evidence across multiple anatomic sites rather than a single novel target.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for high-grade cervical intraepithelial neoplasia (CIN 2-3) as a non-invasive alternative to LLETZ excision; stopped early, underpowered |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neoadjuvant treatment for lentigo maligna of the face, aiming to reduce excision size/risk of intralesional excision |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Imiquimod 5% cream, 3x/week for 1-2 cycles, for actinic keratoses on the head |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Surgical excision vs. curettage + imiquimod for nodular basal cell carcinoma, non-inferiority RCT |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT of topical imiquimod efficacy in high-grade cervical intraepithelial lesions |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explorative controlled study of imiquimod for vulvar intraepithelial neoplasia 2/3 (VIN) and anogenital warts, including immune escape mechanisms |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | RCT comparing 5% imiquimod, 0.05% imiquimod, and 0.05% nanoencapsulated imiquimod gel for actinic cheilitis (pre-malignant lip lesion) |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands/forearms |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Neoadjuvant TLR7 agonist (imiquimod) immunotherapy in early-stage oral squamous cell carcinoma |
| [NCT00142454](https://clinicaltrials.gov/study/NCT00142454) | Phase 1 | Completed | 9 | Imiquimod used as vaccine adjuvant in resected Stage IIB-III malignant melanoma (safety/immunogenicity) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane Systematic Review | Cochrane Database Syst Rev | Interventions (including imiquimod) for anal intraepithelial neoplasia, an HPV-related pre-malignant condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane Systematic Review | Cochrane Database Syst Rev | Medical interventions (including imiquimod) for high-grade vulval intraepithelial neoplasia |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer, including imiquimod's role |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, including topical field therapies such as imiquimod |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical treatment strategies for non-melanoma skin cancer and precursor (pre-malignant) lesions |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical PK/PD | Urol Oncol | TLR7 agonists (imiquimod-related) evaluated for topical (pre-)malignant skin lesions and investigational intravesical use in bladder cancer |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful treatment of high-grade vulval intraepithelial neoplasia with imiquimod 5% in a renal transplant recipient |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report | Hautarzt | OCT imaging case with multiple pre-malignant lesions (actinic keratosis, SCC, Bowen's disease) resistant to topical treatment |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Bowenoid papulosis of the penis (pre-malignant HPV-related lesion) successfully treated with topical imiquimod 5% cream |

## Finland Market Information

Imiquimod currently holds no marketing authorization in Finland (0 licenses on file; market status: Not Marketed). No product-level dosage form or approved-indication data is available from this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two Cochrane systematic reviews and a completed Phase 3 RCT (lentigo maligna, n=259) support imiquimod's efficacy across several distinct pre-malignant epithelial conditions, and the mechanism is directly continuous with its established use in actinic keratosis and superficial BCC. However, no trial targets "pre-malignant neoplasm" as a unified indication — evidence is fragmented across CIN, VIN, AIN, actinic cheilitis, and lentigo maligna, and the pivotal CIN Phase 3 trial (NCT02329171) was terminated early and underpowered (n=9).

**To proceed, the following is needed:**
- TFDA/Fimea package insert with warnings, contraindications, and DDI data (currently a Blocking data gap, DG001)
- Confirmed formal mechanism-of-action documentation from DrugBank (DG002)
- Clarification of whether Finland market entry is planned, given current "Not Marketed" status
- A defined regulatory strategy for which specific pre-malignant subtype(s) (e.g., CIN, VIN, actinic cheilitis) to pursue, since "pre-malignant neoplasm" is not itself a registrable indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

