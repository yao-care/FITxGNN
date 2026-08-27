---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pantoprazole: From Undocumented Original Indication to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI); its formally recorded original indication is missing from this evidence pack (`original_indications` is empty and `original_moa` is flagged as a data gap). TxGNN's top prediction is **Active Peptic Ulcer Disease** (score **99.69%**), supported by **3 clinical trials** and **20 publications** — but the evidence pack's own rationale flags this as likely an artifact of the missing baseline indication data rather than a genuine novel repurposing signal, since peptic ulcer disease is already a well-established, on-label PPI use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (0 Finland licenses on record); PPI-class drugs are generally indicated for GERD/erosive esophagitis and peptic ulcer disease |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

`original_moa` in this evidence pack is explicitly marked as a data gap (DG002, severity: High). However, the repurposing rationale attached to this candidate does contain mechanistic detail: Pantoprazole is a proton pump inhibitor that irreversibly and specifically binds the gastric parietal-cell H+/K+-ATPase, blocking the final common step of gastric acid secretion — the standard first-line mechanism for healing acid-peptic disease.

Active peptic ulcer disease sits squarely within this core pharmacological action. Importantly, the evidence pack's own analysis flags this specific prediction as likely **not** a genuine novel repurposing signal: because `drug.original_indications` is empty in the underlying knowledge graph, TxGNN appears to be "rediscovering" a use that is already on-label for pantoprazole, rather than surfacing new therapeutic territory. The very high score (99.69%) is consistent with this — it looks more like a data-completeness artifact than a repurposing insight.

This caveat also applies to rank 6 in the same evidence pack ("duodenal ulcer disease," also L1), which shares the identical mechanistic rationale. The remaining ranked candidates in this pack (gastrojejunal ulcer, peptic ulcer perforation, duodenogastric reflux, duodenal obstruction) carry progressively weaker and more indirect mechanistic links (L2–L5), and are more plausible candidates for genuine site-specific or adjuvant-use exploration. Before treating any of the six predictions in this pack as a true "new" indication, the underlying `original_indications` field should be backfilled so TxGNN scores can be interpreted against an accurate baseline.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled trial comparing Ilaprazole vs. Pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients — direct efficacy evidence (relevance grade A). |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the effect of PPIs and statins on clopidogrel antiplatelet activity in PCI patients on dual antiplatelet therapy — a drug-interaction study, not an ulcer-healing endpoint (relevance grade B). |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Identified risk factors predicting poor SRH fading or early rebleeding after endoscopic hemostasis plus high-dose PPI in peptic ulcer hemorrhage, to guide selection for second-look endoscopy — a clinical-process study, only indirectly tied to pantoprazole efficacy (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective randomized study comparing intermittent vs. continuous pantoprazole infusion for prevention of peptic ulcer rebleeding after endoscopic therapy. |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | Journal of Gastroenterology and Hepatology | Prospective RCT: pantoprazole infusion as adjuvant to endoscopic treatment reduces rebleeding in peptic ulcer bleeding. |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Alimentary Pharmacology & Therapeutics | Compared three pantoprazole-based triple therapy regimens for H. pylori eradication and gastric ulcer healing. |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative clinical study | Hepato-gastroenterology | Compared lansoprazole vs. pantoprazole in treatment of active duodenal ulcer and H. pylori eradication. |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | RCT | Alimentary Pharmacology & Therapeutics | Two-week pantoprazole course combined with 1-week amoxicillin/clarithromycin was effective for H. pylori eradication and duodenal ulcer healing. |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Multicenter, randomized, active-controlled study of tegoprazan (a P-CAB) vs. PPI-class comparator for healing endoscopic-resection-induced artificial ulcers. |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Clinical study | Medical Archives (Sarajevo) | Assessed PPI efficacy after endoscopic hemostasis in bleeding peptic ulcer, including the role of H. pylori. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clinical Drug Investigation | Overview of pantoprazole pharmacology: irreversible H+/K+-ATPase inhibition; notes no clinically significant drug-drug interactions identified to date. |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | Reviews PPI mechanism (H+/K+-ATPase inhibition) and superiority over H2-receptor antagonists in controlling acid secretion. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review / Network Meta-analysis | American Journal of Gastroenterology | Compares P-CAB vs. PPI efficacy/safety for healing severe (Los Angeles grade C/D) reflux esophagitis. |

---

## Finland Market Information

Pantoprazole is currently **not marketed in Finland** (`market_status: 未上市`, 0 authorizations on record). No product license, dosage form, or approved-indication data are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical-trial evidence for pantoprazole in active peptic ulcer disease is strong (L1, including a direct Phase 3 RCT and multiple supporting RCTs on ulcer healing/rebleeding prevention), but the evidence pack itself flags this prediction as likely reflecting a gap in the original-indication baseline rather than a genuinely novel repurposing signal — so it should be treated as a data-quality finding first, and a repurposing candidate second, until the baseline is corrected.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a **Blocking** data gap (DG001); required before any S1 safety screening
- DrugBank-sourced mechanism of action (MOA) — currently a **High**-severity data gap (DG002)
- Backfill of `drug.original_indications` so TxGNN scores for this and the other five ranked candidates in this pack (gastrojejunal ulcer, peptic ulcer perforation, duodenogastric reflux, duodenal obstruction, duodenal ulcer) can be correctly distinguished from label-relearning artifacts
- Finland/Taiwan regulatory and licensing data, given the drug is currently unmarketed (0 licenses)
- Drug-drug interaction (DDI) data — current query status is "not_found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

