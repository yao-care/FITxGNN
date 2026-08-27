---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 1
---

# Glucagon
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

# Glucagon: From Unspecified Original Indication to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon (DrugBank DB00040) is a pancreatic hormone; no original indication, mechanism-of-action, or Finland market data is available in this evidence pack. The TxGNN model predicts a **99.24%** score for **Irritable Bowel Syndrome (IBS)**, but nearly all of the 11 clinical trials and 20 publications retrieved actually concern **GLP-1 (glucagon-like peptide-1) receptor agonists** (liraglutide, ROSE-010, exendin-4, native GLP-1) — a different peptide and receptor system — not glucagon itself, strongly suggesting a name-collision artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (drug not marketed in Finland; original indication not provided in source data) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glucagon is not available in this evidence pack, and no original indication or Finland licensing record exists to anchor a comparison.

More importantly, the retrieved evidence itself raises a **data-quality concern rather than supporting the prediction**. Glucagon and GLP-1 (glucagon-like peptide-1) are both cleavage products of the same *proglucagon* gene, but they act on structurally distinct receptors with different — in some respects opposite — physiology: glucagon raises blood glucose via the glucagon receptor (hepatic glycogenolysis/gluconeogenesis), while GLP-1 is an incretin that acts on the GLP-1 receptor to slow gastric emptying, modulate gut motility, and suppress glucagon release. Essentially all of the trials and publications surfaced here (liraglutide, ROSE-010, exendin-4, "native GLP-1") test GLP-1 receptor agonists, not glucagon.

This pattern is consistent with a keyword-matching artifact: the string "glucagon" appears inside "glucagon-like peptide-1" in nearly every source document, which can inflate both retrieval counts and the TxGNN score without any of the evidence actually pertaining to glucagon. No trial or publication in this pack tests glucagon (the hormone) directly against IBS. Combined with the missing MOA, missing original indication, and "not marketed" status, the prediction should be treated as unreasonable to act on until the underlying entity confusion is resolved.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Mechanism of colonic butyrate action in IBS; no glucagon involvement (relevance: C — unrelated) |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Small-intestinal organoid model for nutrient antigens/therapeutics; no glucagon involvement (relevance: C — unrelated) |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated (n=8) | 8 | Tests liraglutide (a GLP-1 receptor agonist), not glucagon, in IPAA patients with high bowel frequency (relevance: C — wrong drug) |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Whole-grain rye bread effect on gut-microbiota-brain axis; no glucagon involvement (relevance: C — unrelated) |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Fructo-oligosaccharide supplementation in reactive hypoglycaemia; not a glucagon intervention trial (relevance: C — unrelated) |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low-energy diet vs. diet + intragastric balloon in obesity; no glucagon involvement (relevance: C — unrelated) |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Eating rate of ultra-processed foods and metabolic response; no glucagon involvement (relevance: C — unrelated) |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise training effects on gut dysbiosis and GLP-1 (not glucagon) in IBS (relevance: C — wrong hormone) |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 vs. GLP-1 analogue ROSE-010 on GI motility; not glucagon (relevance: C — wrong drug) |
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (GLP-1 analogue) effect on GI motility in constipation-predominant IBS; not glucagon (relevance: C — wrong drug) |

All 10 trials listed above are graded **C (low/no relevance)** in the source data — none directly tests glucagon in IBS.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36269141](https://pubmed.ncbi.nlm.nih.gov/36269141/) | 2022 | RCT | Gut Microbes | Probiotic *Bacillus subtilis* BS50 reduces GI symptoms in healthy adults; unrelated to glucagon |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | Pain response to GLP-1 receptor agonist ROSE-010 in IBS subpopulations — GLP-1, not glucagon |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Annals of Gastroenterology | Prescription/discontinuation patterns of GLP-1 receptor agonists in IBS patients — GLP-1, not glucagon |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cell Mol Gastroenterol Hepatol | Brain-gut-microbiome axis overview; does not address glucagon specifically |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Review | Frontiers in Endocrinology | Systematic review/meta-analysis of GLP-1 receptor agonists for IBS improvement — GLP-1, not glucagon |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Review | The Journal of Headache and Pain | GLP-1 receptor agonists for headache/pain disorders; notes GLP-1 inhibits glucagon release (opposite direction) |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Role of L-cell-derived GLP-1 in IBS pathophysiology — GLP-1, not glucagon |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolized GLP-1 for diabetes and IBS; GLP-1, not glucagon |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | General IBS treatment review beyond fiber/antispasmodics; no glucagon-specific data |
| [23330973](https://pubmed.ncbi.nlm.nih.gov/23330973/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Metabolic/toxicological considerations for newer IBS drugs; no glucagon-specific data |

## Finland Market Information

Glucagon is not currently marketed in Finland — no authorization records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence supporting this prediction almost entirely concerns GLP-1 receptor agonists (a distinct hormone/receptor system), not glucagon itself, indicating the TxGNN score and retrieved evidence are likely driven by name overlap ("glucagon" within "glucagon-like peptide-1") rather than a genuine pharmacological signal. Combined with the absence of original-indication, MOA, and Finland market data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmation from the TxGNN model owners on whether GLUCAGON (DB00040) and GLP-1/GLP-1 receptor agonists were correctly disambiguated during training/scoring
- A literature and trial search specifically restricted to pancreatic glucagon (not GLP-1) and gastrointestinal motility or IBS
- DrugBank-sourced original indication and mechanism-of-action data for DB00040
- Finland/TFDA package insert data (warnings, contraindications, DDI) once market status changes or the candidate is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

