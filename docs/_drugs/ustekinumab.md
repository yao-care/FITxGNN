---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Ustekinumab
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

# Ustekinumab: From Psoriasis to Dermatitis (Atopic Dermatitis)

## One-Sentence Summary

Ustekinumab is a human monoclonal antibody targeting IL-12/IL-23, established for moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis. The TxGNN model predicts it may also be effective for **Dermatitis** (predominantly evidenced as atopic dermatitis), with **7 clinical trials** and **20 publications** currently supporting this direction, though a blocking gap in official safety labelling remains unresolved.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis, psoriatic arthritis, Crohn's disease, ulcerative colitis (per literature evidence, PMID 36208443; no official Finland licence record on file) |
| Predicted New Indication | Dermatitis (Atopic Dermatitis) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, no official DrugBank/TFDA mechanism-of-action record is available for ustekinumab in this evidence pack. However, literature within the pack (PMID 27304428, 36208443) confirms it is a human IgG1 monoclonal antibody targeting the shared p40 subunit of interleukin (IL)-12 and IL-23, which suppresses Th1, Th17, and Th22 lymphocyte activation. On this basis, ustekinumab (brand name Stelara) is indicated for moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis.

Psoriasis and atopic dermatitis are both chronic immune-mediated inflammatory skin diseases, though they are traditionally driven by different T-helper axes — psoriasis by Th17/Th22, and atopic dermatitis primarily by Th2 with a variable Th22 contribution. Because ustekinumab blocks the IL-12/23 axis shared upstream of Th17 and Th22 differentiation, there is a plausible mechanistic bridge between the two conditions.

This bridge is not purely theoretical: PMID 27745907 directly demonstrates that ustekinumab down-regulates Th2/Th22 gene expression in patients with severe atopic dermatitis, supporting biological applicability. Multiple Phase 2 RCTs (NCT01945086, NCT01806662) and a body of systematic reviews and real-world studies have since tested this hypothesis directly in atopic dermatitis patients, which is the primary reason the evidence level here exceeds a pure prediction-only score.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Completed | 79 | Randomized, double-blind, placebo-controlled trial of ustekinumab in adult Japanese patients with severe atopic dermatitis |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Completed | 32 | Randomized pilot study of ustekinumab in chronic atopic dermatitis with sub-optimal response to prior therapy |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Completed | 676 | CLEAR study: secukinumab vs. ustekinumab efficacy (PASI-75 at week 16) in moderate-to-severe plaque psoriasis; long-term safety and tolerability also assessed |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Recruiting | 45 | Suction-blistering contact dermatitis model to study skin inflammation mechanisms of biologic therapies |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective pharmacogenetic cohort evaluating 10-year survival of biologic therapies in cutaneous psoriasis/psoriatic arthritis |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Completed | 126 | Cardiovascular risk assessment in patients with severe psoriasis treated with biologic agents |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice delivering FDA-approved atopic dermatitis/psoriasis drugs directly into skin for comparative in-situ testing |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT | Experimental Dermatology | Phase 2 double-blind, placebo-controlled trial (n=33) of ustekinumab in moderate-to-severe atopic dermatitis |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT | British Journal of Dermatology | Randomized, double-blind, placebo-controlled Phase 2 study of ustekinumab in Japanese patients with severe atopic dermatitis |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Systematic Review | Allergy | Systematic review/meta-analysis of systemic treatments for moderate-to-severe atopic dermatitis, informing EAACI guidelines |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Systematic Review | J Dermatological Treatment | Systematic review of efficacy and safety of ustekinumab specifically in atopic dermatitis |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | Systematic Review | Am J Clinical Dermatology | Systematic review/meta-analysis assessing efficacy of biologics, including ustekinumab, in atopic dermatitis |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | Observational | J Dermatological Treatment | Real-world evidence analysis of ustekinumab effectiveness in atopic dermatitis patients |
| [27745907](https://pubmed.ncbi.nlm.nih.gov/27745907/) | 2017 | Clinical/Mechanistic Study | J American Academy of Dermatology | Ustekinumab treatment in severe atopic dermatitis showed down-regulation of Th2/Th22 gene expression |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatologic Therapy | Review of off-label uses of ustekinumab, synthesizing trials, observational studies, and case reports across indications |
| [30850043](https://pubmed.ncbi.nlm.nih.gov/30850043/) | 2019 | Review | Dermatologic Clinics | Review of emerging treatment developments in atopic dermatitis, including biologics beyond dupilumab |
| [37929636](https://pubmed.ncbi.nlm.nih.gov/37929636/) | 2024 | Case Report | Australasian J Dermatology | Case of combined dupilumab + ustekinumab therapy in a patient with severe atopic dermatitis and Crohn's disease |

## Finland Market Information

Ustekinumab is currently **not marketed** in Finland — no Fimea marketing authorizations are on file (0 licences recorded).

## Safety Considerations

Please refer to the package insert for safety information. (Note: official TFDA/Fimea package-insert warnings, contraindications, and DDI data are currently a blocking data gap — see Conclusion.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Two completed Phase 2 RCTs, a Th2/Th22 mechanistic study, and multiple systematic reviews/real-world evidence directly support ustekinumab's efficacy in atopic dermatitis, giving reasonable (L2) confidence in the repurposing hypothesis. However, the drug is not currently marketed in Finland and official safety labelling (warnings/contraindications) is a **Blocking** data gap that prevents entry into formal S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) to resolve the blocking safety data gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- A completed Phase 3 RCT specifically in atopic dermatitis (current strongest direct evidence is Phase 2)
- Finland market authorization/registration pathway assessment, since the product currently holds no local licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

