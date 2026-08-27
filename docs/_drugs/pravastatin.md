---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 9
---

# Pravastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin (HMG-CoA reductase inhibitor) originally used to lower LDL cholesterol in hypercholesterolemia and mixed dyslipidemia. The TxGNN model predicts potential efficacy in **Homozygous Familial Hypercholesterolemia (HoFH)**, but the supporting evidence is largely indirect — **1 clinical trial** (testing a different drug, alirocumab, in the same patient population) and **13 publications**, most of which discuss other statins or cholesterol-lowering agents rather than pravastatin specifically in HoFH.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (statin class) — formal label text unavailable, drug not marketed in Finland |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap: MOA). Based on known information, pravastatin belongs to the statin (HMG-CoA reductase inhibitor) class, which lowers LDL cholesterol by inhibiting hepatic cholesterol synthesis and upregulating LDL receptor expression. Its efficacy in general hypercholesterolemia is well established, and statins as a class are used across the spectrum of hyperlipidemic conditions, which is the mechanistic basis for the TxGNN prediction linking pravastatin to HoFH.

However, the biological rationale is weaker for HoFH specifically than for other lipid disorders. HoFH patients carry near-complete loss of functional LDL receptors, so the LDL-receptor-upregulation mechanism that drives statin efficacy has limited effect in this population — clinical practice typically requires add-on therapy with PCSK9 inhibitors, ezetimibe, or LDL apheresis rather than statin monotherapy. Direct evidence for pravastatin alone in HoFH is sparse; most of the supporting literature and the one clinical trial in this evidence pack actually involve other agents (alirocumab, rosuvastatin, ezetimibe, atorvastatin) studied in HoFH or related hypercholesterolemia populations, with pravastatin appearing only via statin-class extrapolation.

Notably, a related but lower-ranked prediction in this evidence pack — **familial hypercholesterolemia (heterozygous, rank 6)** — has substantially stronger direct evidence for pravastatin (multiple pediatric trials and pharmacokinetic studies specifically using pravastatin), though it is scored as an already-established indication rather than a novel repurposing candidate. This should be considered alongside the HoFH prediction when prioritizing further work.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (not pravastatin) in children/adolescents (8–17y) with HoFH; assessed LDL-C reduction at 12/24/48 weeks on top of background lipid-lowering therapy. Relevance graded B — same patient population, but different drug/mechanism (PCSK9 inhibitor). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guideline for management of dyslipidemia and cardiovascular disease prevention. |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (INTREPID) | Lancet HIV | Phase 4 RCT comparing pitavastatin vs. pravastatin; pravastatin's non-CYP450 metabolism reduces DDI risk relative to other statins. |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of statins in children with familial hypercholesterolemia, covering both heterozygous and homozygous forms. |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the same Cochrane review on statins for pediatric familial hypercholesterolemia. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review (rosuvastatin) | Drugs | Rosuvastatin superior to pravastatin/atorvastatin/simvastatin in lipid profile improvement across 6–52 week trials. |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review (ezetimibe) | Am J Cardiovasc Drugs | Ezetimibe mechanism and LDL-C reduction data; relevant as combination-therapy context for severe hypercholesterolemia. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin indicated for hypercholesterolemia, mixed dyslipidemia, and homozygous familial hypercholesterolemia. |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review (atorvastatin) | Ann Pharmacother | Efficacy/safety review of atorvastatin in primary hypercholesterolemia and mixed dyslipidemias. |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review (ezetimibe) | Cardiovasc Drug Rev | Ezetimibe as first-in-class cholesterol absorption inhibitor, used when statin monotherapy is insufficient. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review (atorvastatin) | Drugs | Pharmacology and therapeutic potential of atorvastatin in hyperlipidemias. |

---

## Finland Market Information

Pravastatin is not currently marketed in Finland — no marketing authorizations were found in the regulatory data source.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings, contraindications, and drug interaction data are flagged as a **Blocking** data gap — DG001 — and could not be retrieved for this evaluation.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN score is high, but the direct evidence for pravastatin specifically in HoFH is weak — the sole clinical trial studies a different drug (alirocumab) in the same population, and most supporting literature discusses other statins/agents rather than pravastatin. Evidence level is L3 (reviews/guidelines, no dedicated pravastatin-HoFH RCT), so this candidate should not proceed without closing key data gaps.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Confirmed mechanism of action data for pravastatin — currently a **High** severity gap (DG002)
- A pravastatin-specific study (or at minimum PK/PD data) in HoFH patients, given that HoFH typically requires PCSK9 inhibitors/ezetimibe/apheresis rather than statin monotherapy
- Consider cross-referencing with the stronger, pravastatin-specific evidence available for heterozygous familial hypercholesterolemia (rank 6 in this evidence pack) when setting priorities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

