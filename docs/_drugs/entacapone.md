---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to Lewy Body Dementia

## One-Sentence Summary

Entacapone (DB00494) is a COMT (catechol-O-methyltransferase) inhibitor, originally used as an adjunct to levodopa/carbidopa therapy for Parkinson's disease motor fluctuations. This evidence pack is a **multi-indication screen**: TxGNN surfaced 10 candidate new indications (all >99% prediction score), but only **2 of the 10 have any supporting real-world evidence** — Lewy Body Dementia (1 clinical trial, 3 publications) and Progressive Supranuclear Palsy-Corticobasal Syndrome (1 clinical trial). The remaining 8 candidates are pure model predictions (L5, no clinical trials or literature at all). Given a **Blocking**-severity data gap on safety labeling and the absence of any interventional trial actually testing entacapone in a new indication, the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, adjunct to levodopa/carbidopa (inferred from repurposing rationale narrative; formal MOA/indication fields are data gaps — see below) |
| Predicted New Indication (highest-evidence candidate) | Lewy body dementia |
| TxGNN Prediction Score | 99.25% (rank 7 of screened candidates; top-ranked candidate overall, PLA2G6-associated neurodegeneration, scored 99.76% but has zero supporting evidence) |
| Evidence Level | L4 (preclinical/mechanistic + non-interventional trial only) |
| Finland Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned from the structured DrugBank query for this pack (flagged as data gap DG002). However, the repurposing rationale fields embedded in this evidence pack consistently describe entacapone by its established pharmacology: a peripheral **COMT inhibitor** that blocks the O-methylation of levodopa, thereby prolonging levodopa's plasma half-life and increasing central dopamine availability. It is approved worldwide (though not currently marketed in Finland per this pack) as an add-on to levodopa/carbidopa for Parkinson's disease patients experiencing "wearing-off" motor fluctuations.

Lewy body dementia (LBD) shares meaningful pathophysiology with Parkinson's disease: both are alpha-synucleinopathies with substantial nigrostriatal dopaminergic neuron loss, and LBD patients frequently exhibit parkinsonian motor symptoms that are treated off-label with levodopa-based regimens. Extending COMT inhibition to LBD is mechanistically plausible as a way to enhance dopaminergic therapy efficacy in this population. One in-vitro study in the evidence base (PMID 23913715) additionally suggests some antiparkinsonian agents may influence alpha-synuclein oligomer formation, offering a secondary, exploratory molecular rationale — though this evidence is indirect (in vitro only) and does not establish clinical efficacy.

A second, weaker candidate — Progressive Supranuclear Palsy–Corticobasal Syndrome (PSP-CBS) — also shares a "dopaminergic-adjacent" mechanistic story, but the rationale text itself cautions that PSP-CBS patients typically respond poorly to levodopa (reported response rate <20%), meaning any COMT-inhibitor benefit would likely be marginal. The remaining 8 candidates (PLA2G6-associated neurodegeneration, Rasmussen encephalitis, myelitis, juvenile Hunt-type parkinsonism, transaldolase deficiency, lethal infantile mitochondrial myopathy, fructose-1,6-bisphosphatase deficiency, and a perisylvian polymicrogyria syndrome) each have rationale text explicitly noting **weak, indirect, or absent** pharmacological linkage to COMT inhibition — these appear to reflect knowledge-graph network propagation rather than genuine drug-disease relationships, and none carry any clinical trial or literature support.

---

## Overview of All 10 TxGNN-Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|-----------------|
| 1 | PLA2G6-associated neurodegeneration | 99.76% | L5 | Hold |
| 2 | Rasmussen subacute encephalitis | 99.73% | L5 | Hold |
| 3 | Myelitis | 99.63% | L5 | Hold |
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L5 | Hold |
| 5 | Transaldolase deficiency | 99.43% | L5 | Hold |
| 6 | Lethal infantile mitochondrial myopathy | 99.28% | L5 | Hold |
| **7** | **Lewy body dementia** | **99.25%** | **L4** | **Research Question** |
| 8 | Fructose-1,6-bisphosphatase deficiency | 99.22% | L5 | Hold |
| 9 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.06% | L5 | Hold |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 99.04% | L4 | Research Question |

Only ranks 7 and 10 cleared decision stage S1; all others remain at S0 with no clinical trial or literature evidence identified.

---

## Clinical Trial Evidence (Lewy Body Dementia)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA imaging study in patients with autonomic failure/synucleinopathies (including DLB spectrum). **Not an entacapone interventional trial** — no treatment arm; provides only dopaminergic-uptake biomarker background (Relevance grade: C). |

*Note: For Progressive Supranuclear Palsy-Corticobasal Syndrome, one related trial was also found — [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) (gait pattern analysis, observational, N=120) — but it likewise involves no entacapone intervention (Relevance grade: C).*

---

## Literature Evidence (Lewy Body Dementia)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro | Journal of Neuroscience Research | Examined effects of antiparkinsonian agents (including levodopa-pathway drugs) on β-amyloid and α-synuclein oligomer formation in vitro; offers indirect molecular support only. |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | In vitro (iPSC organoid model) | Science Advances | Models Lewy body disease using SNCA-triplication cortical organoids to screen therapeutic candidates; mechanistic/disease-model study, not a direct entacapone efficacy study. |
| [11268898](https://pubmed.ncbi.nlm.nih.gov/11268898/) | 2001 | Review | Presse Médicale | General Parkinson's disease review; background context only. |

---

## Finland Market Information

Entacapone is currently **not marketed in Finland** under this evidence pack (0 authorizations on record), so no local product/authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. A **Blocking**-severity data gap (DG001) was identified: TFDA/label warnings and contraindications could not be retrieved for this evidence pack, and the DDI database query returned no results (`not_found`). This gap must be closed before any formal safety assessment (S1) can proceed for the candidate indications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No completed or ongoing trial directly tests entacapone as a treatment for any of the 10 predicted indications; the only two trials identified (for Lewy body dementia and PSP-CBS) are non-interventional biomarker/observational studies with Grade C relevance.
- A Blocking-severity data gap (missing label safety/contraindication data) prevents even a preliminary safety assessment, and the drug is not currently marketed in Finland.

**To proceed, the following is needed:**
- Resolve DG001 (obtain and parse the official package insert for warnings/contraindications) before any S1 safety evaluation.
- Resolve DG002 (confirm mechanism of action via DrugBank API) to substantiate the COMT-inhibition rationale formally rather than relying on narrative inference.
- If pursuing Lewy body dementia or PSP-CBS further, design or identify an actual interventional study testing entacapone (not just imaging/gait biomarkers) in these populations, with particular attention to the known risk of dopaminergic-agent-induced psychiatric side effects (hallucinations) in LBD patients.
- Given the weak/indirect mechanistic rationale for the other 8 candidates, no further investment is recommended for those indications absent new evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

