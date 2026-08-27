---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

Using the evidence pack, I'm presenting the drug's most evidence-backed predicted indication (Cholesteryl Ester Storage Disease, rank 4) rather than the top TxGNN-score hit (Scheie syndrome, rank 1), because the pack's own `repurposing_rationale` flags ranks 1–3 and 6–10 as mechanistically unrelated with zero supporting evidence — using them as the headline would misrepresent the actual signal. This is noted explicitly in the report below.

---

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Cholesteryl Ester Storage Disease

## One-Sentence Summary

Sebelipase alfa is a recombinant human lysosomal acid lipase (rhLAL) enzyme replacement therapy for Lysosomal Acid Lipase Deficiency (LAL-D); Fimea/Finland licensing data on the original indication is unavailable in this evidence pack (the product is not marketed in Finland). Among 10 TxGNN-predicted indications, **Cholesteryl Ester Storage Disease (CESD)** — the late-onset phenotype of LAL-D — shows by far the strongest evidentiary support, with **9 clinical trials** (including a completed placebo-controlled Phase 3 RCT) and **19 publications**. The other 9 TxGNN-ranked candidates, including the highest raw-score hit (Scheie syndrome), have no mechanistic link to LAL and zero supporting trials or literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Fimea (product not marketed in Finland; no license records). Per supporting literature in this pack, the drug's established indication is Lysosomal Acid Lipase Deficiency (LAL-D) |
| Predicted New Indication | Cholesteryl Ester Storage Disease (CESD) |
| TxGNN Prediction Score | 99.72% (rank 4 of candidate set) |
| Evidence Level | L1 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action text is not available in structured form (DrugBank field flagged as a data gap). Based on the supporting literature in this pack, sebelipase alfa is a recombinant human lysosomal acid lipase (rhLAL) administered by intravenous infusion, which directly replaces the enzyme activity missing in LAL-D.

CESD is caused by biallelic *LIPA* mutations that reduce (but do not abolish) LAL enzyme activity — the same enzyme sebelipase alfa replaces. This is not a speculative cross-mechanism repurposing hypothesis; it is a direct enzyme-substrate match, which is why the evidence base is so much stronger here than for the model's other candidates. The pivotal Phase 3 ARISE trial (NCT01757184) — a randomized, placebo-controlled study in 66 patients with LAL-D/CESD — underpinned global regulatory approvals, and is corroborated by multiple Phase 1/2 dose-finding, long-term extension, and expanded-access studies in the same population.

By contrast, the model's top raw-score candidates — Scheie syndrome, Hurler syndrome, growth hormone insensitivity syndrome with immune dysregulation, Gaucher disease, lysosomal storage disease with skeletal involvement, autosomal ichthyosis syndrome, Tay-Sachs disease, and benign adrenal neoplasm — each involve a different, unrelated enzyme or pathway (e.g., alpha-L-iduronidase in Scheie/Hurler, glucocerebrosidase in Gaucher, hexosaminidase A in Tay-Sachs). These appear to reflect TxGNN's embedding-level similarity across "lysosomal storage disease" phenotypes rather than a true target match, and none returned any clinical trial or literature hits in this evidence pack. They are scored L5/Hold and are not evaluated further here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Phase 3 | Completed | 66 | ARISE study: randomized, placebo-controlled trial of sebelipase alfa (1 mg/kg IV every other week) in late-onset LAL-D/CESD; pivotal trial supporting global approval |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Phase 2/3 | Completed | 9 | Open-label, dose-escalation study in children with growth failure due to LAL-D; weekly infusions for up to 5 years |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Phase 2 | Completed | 31 | Multi-center, open-label study evaluating safety and efficacy in a broad LAL-D population |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Phase 1/2 | Completed | 9 | First-in-human dose-escalation study (LAL-CL01) in adults with liver dysfunction due to LAL-D; supports dosing and safety |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Phase 2 | Completed | 8 | Long-term extension of LAL-CL01; evaluated long-term safety and tolerability in adults with liver dysfunction |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Phase 2 | Terminated | 10 | Once-weekly infusions in infants with rapidly progressive LAL-D (Wolman phenotype); study terminated |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | N/A | No longer available | N/A | Expanded access protocol providing sebelipase alfa to LAL-D patients prior to commercial availability |
| [NCT02926872](https://clinicaltrials.gov/study/NCT02926872) | N/A | Terminated | 22 | DETECT: pediatric screening study for LAL-D as an underlying cause of abnormal liver tests (diagnostic, not treatment) |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | PEARL: basket trial of in-utero enzyme replacement therapy across multiple lysosomal storage disorders; not CESD-specific, indirect relevance |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | RCT | Journal of Hepatology | Final results of the Phase 3 ARISE study; confirms efficacy and safety of sebelipase alfa in children ≥4 years and adults with LAL-D |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Cohort | J Pediatr Gastroenterol Nutr | Single-arm, open-label study (NCT02112994) evaluating long-term efficacy and safety in children and adults |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | Cohort | J Clin Lipidol | Sebelipase alfa improves atherogenic cholesterol biomarkers over 52 weeks in the Phase 3 ARISE population |
| [23348766](https://pubmed.ncbi.nlm.nih.gov/23348766/) | 2013 | Cohort | Hepatology | First human study (LAL-CL01) of recombinant human LAL; clinical effect and safety profile in CESD patients |
| [24993530](https://pubmed.ncbi.nlm.nih.gov/24993530/) | 2014 | Cohort | Journal of Hepatology | 52 weeks of sebelipase alfa reduces serum transaminases and liver volume, improves serum lipids in LAL-D |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Registry | Liver International | International registry data showing sebelipase alfa improves aminotransferase levels vs. untreated LAL-D patients |
| [32103901](https://pubmed.ncbi.nlm.nih.gov/32103901/) | 2020 | Review | Drug Des Devel Ther | Review of therapeutic options for LAL deficiency, covering both Wolman disease and CESD subtypes |
| [34664536](https://pubmed.ncbi.nlm.nih.gov/34664536/) | 2022 | Review | Expert Opin Drug Saf | Safety review of sebelipase alfa across early- and late-onset LAL-D phenotypes |
| [26452566](https://pubmed.ncbi.nlm.nih.gov/26452566/) | 2015 | Review | Drugs | "Sebelipase alfa: first global approval" — regulatory and mechanistic overview |
| [41357559](https://pubmed.ncbi.nlm.nih.gov/41357559/) | 2025 | Case report | ACG Case Rep J | Case of late-onset CESD presenting as hepatic steatosis/cirrhosis, confirmed *LIPA* mutation, treated with sebelipase alfa |

## Finland Market Information

No marketing authorization for sebelipase alfa is currently registered with Fimea — the product is not marketed in Finland (0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-interaction data are currently available for this product — see data gap DG001, flagged as blocking.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Sebelipase alfa's mechanism directly addresses the enzymatic deficiency underlying CESD, and this is supported by a completed placebo-controlled Phase 3 RCT (ARISE, NCT01757184) plus multiple earlier-phase and long-term studies in the same LAL-D population — evidence is substantially stronger than for any of the other 9 TxGNN-ranked candidates. However, the product is not marketed in Finland and core safety labeling (warnings/contraindications) is a blocking data gap.

**To proceed, the following is needed:**
- Fimea/EU SmPC package insert to close the blocking safety data gap (DG001)
- DrugBank mechanism-of-action detail to close DG002
- Confirmation of whether CESD/Wolman disease should be framed as an already-approved indication elsewhere (EMA/FDA) rather than a novel repurposing candidate for this market
- Finland market access feasibility assessment given ultra-rare disease status
- No further action needed on the remaining 8 TxGNN-ranked candidates (Scheie syndrome, Hurler syndrome, growth hormone insensitivity syndrome with immune dysregulation, Gaucher disease, lysosomal storage disease with skeletal involvement, autosomal ichthyosis syndrome, Tay-Sachs disease, benign adrenal neoplasm) — Hold, no mechanistic or evidentiary support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

