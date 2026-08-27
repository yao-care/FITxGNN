---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

Gimeracil is a component of the S-1 fixed-dose combination (tegafur/gimeracil/oteracil), a DPD (dihydropyrimidine dehydrogenase) inhibitor that potentiates 5-FU activity, with proven efficacy in gastric cancer.
The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
with **8 clinical trials** and **15 publications** currently supporting this direction, including two completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric Cancer (as part of the S-1 combination; no standalone Taiwan/Finland regulatory record on file) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Finland Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for gimeracil is not available (data gap). Based on known information, gimeracil is not itself cytotoxic — it is the DPD-inhibitor component of the S-1 fixed-dose combination (tegafur + gimeracil + oteracil). By blocking DPD-mediated breakdown of the 5-FU generated from tegafur, gimeracil raises and sustains intratumoral 5-FU concentrations, enhancing the combination's antitumour activity. S-1's efficacy in gastric cancer has been proven and forms the pharmacological basis for extrapolation to colonic neoplasm.

Gastric cancer and colonic neoplasm are both gastrointestinal, fluoropyrimidine-sensitive tumours sharing the same 5-FU-driven mechanism of action. S-1-based regimens (SOX, S-1+irinotecan, S-1+leucovorin) are already established chemotherapy backbones in colorectal cancer across multiple Asian and European trials, which supports the biological plausibility of the TxGNN prediction.

It is important to note that any observed efficacy is attributable to the **S-1 combination as a whole**, not to gimeracil as a standalone agent — gimeracil has no independent antitumour activity and functions purely as a pharmacokinetic enhancer within the fixed-dose product.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO study: S-1 vs. capecitabine (± bevacizumab) as first-line treatment for metastatic colorectal cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+leucovorin vs. TS-1 (contains gimeracil) as adjuvant treatment for Stage III colon cancer, with gene-expression predictive factor analysis |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1+oxaliplatin) vs. XELOX as adjuvant chemotherapy for Stage III colorectal cancer |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after failure of standard chemotherapy |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL regimen) in untreated metastatic colorectal cancer |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after prior irinotecan/oxaliplatin failure |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1 vs. capecitabine + oxaliplatin: comparison of subclinical coronary microvascular toxicity in metastatic GI adenocarcinoma |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib + tegafur/gimeracil/oteracil as third-line treatment for advanced metastatic colorectal cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | Real-world Study | Eur J Cancer | Population-based study: S-1 is feasible after capecitabine-induced hand-foot syndrome/cardiotoxicity in adjuvant colon cancer treatment |
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Cohort/Clinical Study | Zhonghua Zhong Liu Za Zhi | Efficacy and side effects of oxaliplatin + S-1 combination in postoperative colorectal cancer patients |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Cohort (Safety) | Gan To Kagaku Ryoho | Risk factors for severe (grade 3-4) hematological toxicity (16.1% incidence) with S-1 + irinotecan in advanced/recurrent colonic cancer |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Pharmacokinetic Study | Gan To Kagaku Ryoho | Pharmacokinetics of S-1 for treatment of peritoneal metastasis in a mouse colon cancer model |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical (Xenograft) | Oncology Reports | Irinotecan overcomes 5-FU resistance in colon cancer xenografts via downregulation of thymidylate synthase, combined with oral S-1 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case Report | Anticancer Research | Complete response maintained with S-1 + CPT-11 in hepatic metastases of colon cancer |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case Report | Gan To Kagaku Ryoho | Two-stage hepatectomy after SOX (S-1+oxaliplatin) + panitumumab downstaging for irresectable colorectal liver metastases |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case Report | J Oncol Pharm Pract | Hypertriglyceridemia induced by S-1 in a colorectal cancer patient |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case Report | Eur J Dermatol | S-1-induced erythroderma with extensive mucosal involvement and hand-foot syndrome |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case Report | Gan To Kagaku Ryoho | Laparoscopic resection of peritoneal recurrences after colorectal cancer surgery |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine-class combination) — gimeracil itself is a non-cytotoxic DPD inhibitor that potentiates 5-FU cytotoxicity within the S-1 product |
| Myelosuppression Risk | Medium — grade 3-4 hematological toxicity reported in ~16.1% of patients receiving S-1 + irinotecan (PMID 21084813) |
| Emetogenicity Classification | Low to Moderate (depends on combination partner; higher when combined with oxaliplatin/irinotecan) |
| Monitoring Items | CBC with differential, renal function (dose adjustment required per renal clearance), hepatic function, triglycerides (reported hypertriglyceridemia), skin/mucosal toxicity |
| Handling Protection | Standard cytotoxic drug handling precautions apply, consistent with fluoropyrimidine chemotherapy agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (SALTO, NCT01918852, n=161; NCT00660894, n=1535) directly support the efficacy of S-1 — the fixed-dose combination containing gimeracil — in colorectal/colon cancer, meeting the L1 evidence-level threshold. However, gimeracil's contribution is only demonstrable as part of the S-1 combination, not as a standalone agent, and critical safety/regulatory data (TFDA/Finland package insert, MOA detail) remain unavailable.

**To proceed, the following is needed:**
- TFDA/Finland package insert warnings, contraindications, and precautions (DG001, Blocking gap)
- Detailed mechanism of action data from DrugBank (DG002, High priority)
- Drug interaction (DDI) data, currently not found in the source database
- Clarification of whether the repurposing claim applies to gimeracil alone or requires the full S-1 combination
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

