---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Febuxostat: From Xanthine Oxidase Inhibition to Purine Metabolism Disorders

## One-Sentence Summary

Febuxostat is a xanthine oxidase (XOR) inhibitor; the evidence pack does not record a confirmed original approved indication (flagged as a Blocking/High-severity data gap). TxGNN surfaces **three related purine-metabolism candidates** — Renal Hypouricemia, HPRT Partial Deficiency, and Lesch-Nyhan Syndrome — each scoring above **99.6%**, but the supporting evidence is limited to case reports, reviews, and one low-confidence trial rather than completed RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — DG001/DG002) |
| Predicted New Indication (Top Score) | Hypouricemia, Renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Other candidate indications in this evidence pack:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 2 | Hypoxanthine Guanine Phosphoribosyltransferase (HPRT) Partial Deficiency | 99.98% | L4 | S2 | Proceed with Guardrails |
| 3 | Lesch-Nyhan Syndrome | 99.68% | L3 | S2 | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in the drug record (`original_moa: [Data Gap]`), but the evidence pack's own literature consistently describes febuxostat as a **non-purine selective xanthine oxidoreductase (XOR) inhibitor** that blocks the terminal step of purine catabolism, lowering uric acid production.

For **Rank 1 (Hypouricemia, Renal)**, there is a direct mechanistic tension worth flagging: hypouricemia is a state of *abnormally low* serum urate, while febuxostat's pharmacology *lowers* urate further — the opposite direction. The literature clarifies the actual clinical logic is not "treating" hypouricemia itself, but using febuxostat in patients with **renal hypouricemia (URAT1/GLUT9 transporter defects)** to prevent **exercise-induced acute kidney injury (EIAKI)**, a distinct prophylactic use case. This nuance means the disease label matches the patient population, not the treatment goal, and should be reflected precisely in any downstream protocol.

For **Rank 2 (HPRT Partial Deficiency)** and **Rank 3 (Lesch-Nyhan Syndrome)**, the mechanistic story is coherent and consistent with febuxostat's core pharmacology: both conditions arise from defective purine salvage (HPRT enzyme), forcing compensatory overproduction of uric acid via the XOR pathway. Blocking XOR directly addresses the resulting hyperuricemia/gout, and is analogous to the established (though off-label in these rare diseases) use of allopurinol, a related XOR inhibitor. Febuxostat would only manage the metabolic/hyperuricemia component — it has no effect on the neurobehavioral features of Lesch-Nyhan syndrome.

---

## Clinical Trial Evidence

### Hypouricemia, Renal (Rank 1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Shanghai Xu-hui Central Hospital study on uric acid control and stone recurrence/renal function in hyperuricemia-related calculi; **relevance graded C (low confidence)** — no clear direct link to renal hypouricemia stated, no public results. |

### HPRT Partial Deficiency (Rank 2)

Currently no related clinical trials registered.

### Lesch-Nyhan Syndrome (Rank 3)

Currently no related clinical trials registered.

---

## Literature Evidence

### Hypouricemia, Renal (Rank 1)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical rheumatology | Narrative review of hypouricemia etiology and clinical management for rheumatologists. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review | Internal Medicine (Tokyo) | Case-based discussion proposing non-purine selective XOR inhibitors (incl. febuxostat) to prevent exercise-induced AKI in renal hypouricemia patients. |

### HPRT Partial Deficiency (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32128695](https://pubmed.ncbi.nlm.nih.gov/32128695/) | 2020 | Case Report | CEN case reports | Novel HPRT1 p.V35M mutation causing HPRT-related hyperuricemia with familial juvenile gout, no neurological symptoms. |
| [26073243](https://pubmed.ncbi.nlm.nih.gov/26073243/) | 2015 | Case Report | Internal Medicine (Tokyo) | Novel HPRT mutation combined with known variants, presenting as gout with reduced erythrocyte HPRT activity. |

### Lesch-Nyhan Syndrome (Rank 3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40763966](https://pubmed.ncbi.nlm.nih.gov/40763966/) | 2025 | Case Series | Zhonghua Yixue Yichuanxue Zazhi | Clinical, genetic, and treatment characteristics of two pediatric Lesch-Nyhan syndrome cases. |
| [32128695](https://pubmed.ncbi.nlm.nih.gov/32128695/) | 2020 | Case Report | CEN case reports | Discusses HPRT partial vs. complete deficiency (Lesch-Nyhan) distinction and hyperuricemia presentation. |

---

## Taiwan Market Information

Febuxostat currently has **no marketing authorization on record in Taiwan** (`market_status: 未上市`, 0 licenses). No product name, dosage form, or approved indication data is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** The evidence pack flags a **Blocking-severity data gap (DG001)** — TFDA package insert warnings/contraindications have not yet been retrieved — which explicitly **prevents entry into S1 safety screening** for any of the above indications. Drug interaction data was also queried with `not_found` status (0 interactions). No safety evaluation should proceed until this gap is closed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (missing TFDA label/warnings, DG001) prevents S1 safety screening regardless of which indication is pursued, so no candidate can advance yet despite two of the three (Ranks 2–3) reaching a "Proceed with Guardrails" evidence stage internally.
- All three candidates are currently supported only by case reports, narrative reviews, or a single low-confidence (Grade C), status-unknown trial — no completed RCT evidence exists for any of them.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA package insert (warnings, contraindications) — this is the blocking item (DG001).
- Obtain formal DrugBank MOA and original-indication data (DG002) to properly frame the original-vs-new indication comparison.
- Resolve the Rank 1 mechanistic ambiguity (prophylaxis of EIAKI in renal hypouricemia patients vs. "treating" hypouricemia) before writing any protocol referencing this indication.
- If prioritizing Ranks 2–3 (HPRT partial deficiency / Lesch-Nyhan syndrome), seek case-series or registry-level data given the rarity of these conditions, since RCTs are unlikely to exist.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

