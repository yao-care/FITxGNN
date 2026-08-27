---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

> Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody originally developed for rheumatoid arthritis and juvenile idiopathic arthritis.
> TxGNN predicts it may also be effective for **Ankylosing Spondylitis**, but the supporting evidence — **9 clinical trials** and **19 publications**, including two dedicated Phase 3 trials — actually points toward a **negative** result rather than a positive signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (established from literature evidence; no TFDA/Fimea license record available) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap). Based on the literature evidence collected, tocilizumab is a humanized monoclonal antibody that blocks both membrane-bound and soluble IL-6 receptors, and it is established for use in rheumatoid arthritis (RA), systemic and polyarticular juvenile idiopathic arthritis, and giant cell arteritis — all conditions where IL-6 plays a central pathogenic role.

Rheumatoid arthritis and ankylosing spondylitis (AS) are both chronic inflammatory rheumatic diseases, which is likely why TxGNN's knowledge-graph model flagged AS as a high-scoring candidate (99.99%) — the two diseases share treatment classes (biologic DMARDs) and overlapping patient registries in the literature.

However, the mechanistic rationale is weaker than the score suggests: AS and axial spondyloarthritis are primarily driven by the IL-17/TNF axis, not IL-6. This is not a theoretical concern — it has already been tested directly. Two purpose-built Phase 3 randomized, placebo-controlled trials in AS patients (NCT01209689, NCT01209702) were conducted and both were **terminated**, having failed to demonstrate superiority over placebo (per the repurposing rationale, ASAS20 response was not significantly better than placebo). This is a case of direct clinical evidence returning a **negative** result, not a case of insufficient data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | Pivotal placebo-controlled RCT in AS patients with inadequate response to prior anti-TNF therapy; trial terminated — negative pivotal result |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Seamless Phase II/III RCT in NSAID-failure, TNF-naive AS patients; sister trial to NCT01209689, also terminated — negative result |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Studies **secukinumab**, not tocilizumab, in Takayasu arteritis — drug mismatch, not directly applicable |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean multi-disease biologics/tsDMARD registry covering RA, AS and PsA; observational safety data only, no AS-specific efficacy signal |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells — conducted in RA patients, not AS; indirect IL-6 biology reference only |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Observational cytokine-profiling study across systemic inflammatory diseases; not AS-specific interventional evidence |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management around shoulder arthroplasty in rheumatology patients; not an AS efficacy trial |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | Real-world registry of **Inflectra (infliximab)**, not tocilizumab — drug mismatch |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large-scale registry study on risk of developing additional immune-mediated inflammatory diseases; not an AS treatment trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT (BUILDER-1/2) | Annals of the Rheumatic Diseases | Randomized, placebo-controlled trials assessing short-term symptomatic efficacy of tocilizumab in AS — the primary clinical efficacy data source for this indication |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-analysis | Medicine | Comparative effectiveness of biologic regimens for AS across RCTs; provides comparative context for tocilizumab vs. other biologics |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Reviews the rationale and evidence for IL-6 antagonism specifically in AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis (Cohort) | Clinical Rheumatology | Quantifies serious infection risk with biologics (including tocilizumab) in AS/nr-axSpA RCTs |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Cohort/Review | Osteoporosis International | Systemic bone effects of biologic therapies in RA and AS |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Review | Joint Bone Spine | Reviews biologic agents for AS beyond TNFα antagonists, including IL-6 blockade |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clinical and Experimental Rheumatology | Compares biologics in RA vs. AS and notes differing pathogenesis and treatment response |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Frontiers in Medicine | Two cases of successful tocilizumab treatment for AA amyloidosis complicating AS |
| [32872025](https://pubmed.ncbi.nlm.nih.gov/32872025/) | 2020 | Case Report | Medicine | AS complicating Turner syndrome; literature review context |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Cohort | Expert Review of Clinical Immunology | Compares infection risk between non-biologics and biologics (including tocilizumab) in inflammatory arthritis |

---

## Finland Market Information

Tocilizumab currently has no market authorization in Finland (Fimea market status: **Not Marketed**, 0 licenses on record). No product/dosage-form data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Two purpose-built Phase 3 RCTs in AS (NCT01209689, NCT01209702) were directly tested and terminated without demonstrating efficacy over placebo, indicating IL-6 blockade is likely insufficient for a disease primarily driven by the IL-17/TNF axis. This is a high-quality **negative** finding, not a data gap — pursuing this indication further is not supported by current evidence.

**To proceed, the following is needed:**
- TFDA/local package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- If repurposing tocilizumab remains a priority, consider redirecting resources toward candidates in this same Evidence Pack with materially stronger support — notably **polyarticular JIA** (rank 7, L1 evidence, decision stage S3, "Proceed with Guardrails," already an approved indication elsewhere) and **RF-positive polyarticular JIA** (rank 10, L2, "Proceed with Guardrails") — rather than Ankylosing Spondylitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

