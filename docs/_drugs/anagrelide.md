---
layout: default
title: Anagrelide
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Anagrelide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide (DrugBank DB00261) is a platelet-lowering agent whose established clinical use — per the literature included in this evidence pack — is essential thrombocythemia (ET), a clonal myeloproliferative disorder. The TxGNN model predicts it may also be effective for **Reactive Thrombocytosis**, but this direction is currently supported only by **0 clinical trials** and **10 background/review publications**, none of which directly test anagrelide in reactive thrombocytosis. Notably, several of these same publications state that reactive thrombocytosis typically does **not** require platelet-lowering drug therapy, which weakens rather than strengthens the repurposing case.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Finland regulatory data (drug not marketed there). Based on the literature in this evidence pack, anagrelide's established use is essential thrombocythemia / clonal thrombocytosis (e.g., PMID 16019501, 38455691) |
| Predicted New Indication | Reactive Thrombocytosis |
| TxGNN Prediction Score | 99.83% (rank 2305) |
| Evidence Level | L4 (background/mechanistic and case-level literature only; no clinical trial or study directly tests anagrelide for this indication) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for anagrelide is currently a flagged data gap (DG002, High severity) — DrugBank did not return structured MOA content in this query. Based on the literature retrieved, anagrelide is described as an agent used to suppress megakaryocytic proliferation and reduce platelet production, positioned alongside busulfan, hydroxyurea, and interferon-alpha as a cytoreductive option for clonal thrombocytosis (PMID 7783354, 15270658).

The predicted new indication, reactive thrombocytosis, shares a surface-level phenotype with the original indication — both present as an elevated platelet count. This is likely why the TxGNN knowledge graph linked them: essential thrombocythemia and reactive thrombocytosis are frequently discussed together in the differential-diagnosis literature (PMID 10494240, 17171694, 1994734), which creates strong node proximity in a knowledge graph even though the two conditions have different underlying biology.

Importantly, this same literature works against a straightforward repurposing rationale: reactive thrombocytosis is a secondary response to another underlying process (infection, inflammation, splenectomy, iron deficiency, etc.), and multiple sources in this pack explicitly state it "does not require any therapeutic intervention" in most cases (PMID 15270658), unlike clonal thrombocytosis where treatment is guided by platelet count thresholds and thrombotic risk (PMID 10494240). Any plausible use of anagrelide in reactive thrombocytosis would likely be limited to rare, severe/symptomatic cases (e.g., extreme hyperthrombocytosis with end-organ risk, as discussed in the thrombocytapheresis review, PMID 28380402) — not the general reactive thrombocytosis population implied by the predicted indication label. This distinction should be treated as a caution flag rather than confirmation of the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leukemia & Lymphoma | Critical review of anagrelide therapy in essential thrombocythemia; distinguishes clonal thrombocytosis (requires cytoreduction) from reactive thrombocytosis (usually does not) |
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Review of Anticancer Therapy | Drug profile of anagrelide (Agrylin) MOA and therapeutic potential in clonal thrombocytosis; explicitly notes reactive thrombocytosis does not require intervention |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | The Medical Journal of Australia | ET diagnosis requires excluding reactive thrombocytosis; treatment threshold is platelet count >1000×10⁹/L |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | The American Journal of the Medical Sciences | Background pathophysiology of thrombocytosis/thrombocythemia and cytokine regulation of platelet production; not drug-specific |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki (Japanese) | Diagnosis/treatment overview of ET; lists anagrelide among agents suppressing megakaryocytic proliferation |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Case-based Review | Leukemia Research | Reviews thrombocytapheresis for extreme hyperthrombocytosis in myeloproliferative neoplasms; discusses limits of medical cytoreduction when rapid reduction is needed |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective/Observational | Pediatric Blood & Cancer | Retrospective analysis of 12 pediatric cases comparing essential vs. reactive thrombocythemia; highlights diagnostic overlap |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski Arhiv za Celokupno Lekarstvo | ET with ankylosing spondylitis (a condition associated with reactive thrombocytosis) managed with anagrelide plus DMARDs/etanercept |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | European Journal of Case Reports in Internal Medicine | Acute MI in an ET patient on anagrelide therapy — a safety signal relevant to thrombotic/cardiac risk |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | Perioperative management guideline for thrombocytosis in digital replantation; not anagrelide-specific |

---

## Finland Market Information

Anagrelide is not currently marketed in Finland (0 marketing authorizations on record), so no product/indication data is available.

---

## Safety Considerations

TFDA/package-insert warnings and contraindications for anagrelide could not be retrieved in this query (Data Gap DG001, **Blocking severity** — this gap alone prevents the candidate from clearing the initial safety screening stage). Drug-drug interaction data was also queried but not found. Until this data gap is resolved, please refer directly to the anagrelide package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence level is L4 at best — no clinical trials and no literature directly evaluating anagrelide's efficacy in reactive thrombocytosis exist; the retrieved literature is background/mechanistic and, if anything, argues that most reactive thrombocytosis does not warrant platelet-lowering drug therapy.
- A Blocking-severity safety data gap (TFDA warnings/contraindications, DG001) means this candidate cannot yet proceed to safety evaluation regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/official package-insert warnings and contraindications for anagrelide
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank
- Identify a clinically plausible reactive-thrombocytosis subpopulation (e.g., severe/symptomatic hyperthrombocytosis with thrombotic risk) rather than the general reactive thrombocytosis population, and search for any case series or trials specific to that subgroup
- Clarify why TxGNN ranked this association highly, given that the literature evidence base actually cautions against routine drug treatment of reactive thrombocytosis

*Note: A second candidate indication, "inverse Klippel-Trenaunay syndrome" (TxGNN score 99.59%, rank 4816), was also evaluated for this drug. It has zero supporting clinical trials or literature and an implausible mechanistic link (Klippel-Trenaunay-spectrum disorders are associated with thrombocytopenia/consumptive coagulopathy, not thrombocytosis). It is assessed as Evidence Level L5 with a **Hold** recommendation and is very likely a knowledge-graph node-proximity artifact rather than a genuine repurposing signal; no further action is recommended on this indication.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

