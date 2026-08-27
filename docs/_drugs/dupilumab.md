---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is a human monoclonal antibody targeting IL-4Rα that blocks IL-4/IL-13 signaling; per the evidence captured in this dataset, it has established use in Th2-driven inflammatory diseases such as atopic dermatitis, asthma, and eosinophilic COPD. The TxGNN model predicts it may also be effective for **Bronchitis**, but this is currently supported by only **1 clinical trial** (with a disease-label mismatch flag) and **6 publications**, most of which actually address asthma or COPD rather than bronchitis specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (no Finland marketing licenses on file); literature evidence in this pack indicates the drug is approved for atopic dermatitis, asthma, and eosinophilic COPD |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% (rank 1226) |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (`original_moa: [Data Gap]`). Based on information embedded in the supporting literature, dupilumab is a fully human IgG4 monoclonal antibody that binds the shared IL-4Rα subunit, blocking downstream signaling of interleukin-4 and interleukin-13 — the key cytokines driving Th2/type-2 airway and skin inflammation. Its efficacy in Th2-driven diseases (atopic dermatitis, moderate-to-severe asthma, eosinophilic COPD) is well documented in the evidence pack.

Bronchitis — particularly chronic or eosinophilic bronchitis — can share the same Th2/eosinophilic inflammatory pathway seen in asthma and COPD exacerbations, which is the mechanistic basis for the TxGNN prediction. However, "bronchitis" as a standalone diagnostic label is broader and less specific than asthma or COPD, and the trial/literature evidence retrieved for this indication is largely borrowed from adjacent, better-studied conditions rather than bronchitis itself.

Critically, the single retrieved clinical trial (NCT04362501) was graded **C (data mismatch)** by the relevance review — its actual target population is chronic rhinosinusitis without nasal polyps (CRSsNP), not bronchitis, sharing only the underlying Th2 mechanism. This means the mechanistic rationale is plausible, but direct, disease-specific clinical evidence for bronchitis is currently lacking.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab for chronic rhinosinusitis without nasal polyps (CRSsNP) — **relevance grade C**: actual target disease is CRSsNP, not bronchitis; only shares Th2 inflammatory mechanism, flagged as a data-label mismatch |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT extension (TRAVERSE) | Lancet Respir Med | Long-term (>1 year) open-label extension confirming safety and sustained efficacy of dupilumab in moderate-to-severe **asthma**, not bronchitis specifically |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | RCT substudy (imaging) | Chest | MRI-based ventilation defect imaging in prednisone-dependent severe asthma patients on anti-T2 biologic treatment |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review/Meta-analysis | J Asthma | Meta-analysis of RCTs evaluating dupilumab efficacy/safety in uncontrolled **asthma** |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review (COPD) | Tuberc Respir Dis | Comprehensive review of pharmacologic therapies (including biologics) for preventing **COPD** exacerbations |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses treatment challenges in smoking-induced airway diseases including chronic bronchitis, emphysema, and asthma-COPD overlap; notes these patients are typically excluded from major trials |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review (pediatric plastic bronchitis) | Pediatr Pulmonol | Reviews novel therapies for eosinophilic pediatric plastic bronchitis (abstract not available in this dataset) |

---

## Finland Market Information

No Finland marketing authorizations are on file for dupilumab in this dataset — `market_status: 未上市 (Not Marketed)`, `total_licenses: 0`.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: A **Blocking**-severity data gap (DG001 — TFDA/Fimea package insert warnings and contraindications) is recorded in this dataset, which by itself prevents entry into the S1 safety pre-assessment stage regardless of efficacy evidence strength.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence specific to bronchitis is weak: the sole clinical trial is a confirmed disease-label mismatch (actual target: CRSsNP), and the literature predominantly covers asthma and COPD rather than bronchitis itself.
- A Blocking-severity data gap (missing package insert warnings/contraindications) prevents even initial safety screening (S1), independent of the efficacy question.

**To proceed, the following is needed:**
- Retrieve TFDA/Fimea package insert (warnings, contraindications) to unblock S1 safety review (DG001)
- Confirm mechanism of action via DrugBank API query (DG002)
- Source bronchitis-specific (not asthma/COPD-proxy) clinical trial and literature evidence, or formally re-scope the indication to a better-defined Th2-driven phenotype (e.g., eosinophilic/chronic bronchitis)
- Separately, note that rank-2 predicted indication **dermatitis** in this same dataset carries substantially stronger evidence (L1, multiple completed Phase 3/4 RCTs, "Proceed with Guardrails") and may warrant prioritized evaluation ahead of bronchitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

