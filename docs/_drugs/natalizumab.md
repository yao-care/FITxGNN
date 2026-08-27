---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a humanized monoclonal antibody used to treat relapsing-remitting multiple sclerosis (RRMS) by blocking α4-integrin-mediated leukocyte migration. The TxGNN model predicts it may be effective for **Bronchitis**, but this prediction currently has **no supporting clinical trials and no supporting literature** — it is a model-only signal that runs counter to the drug's known immunosuppressive risk profile.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (relapsing-remitting) — inferred from literature context; not present in Finland market data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned a Data Gap). Based on known information from the evidence pack's literature context, natalizumab is a monoclonal antibody targeting α4-integrin, used for relapsing-remitting multiple sclerosis; its efficacy in MS is well established in the cited literature, which repeatedly references its use in RRMS patient cohorts.

For the bronchitis prediction specifically, the mechanistic rationale supplied alongside the score is explicitly skeptical: α4-integrin blockade could theoretically reduce leukocyte infiltration of airway mucosa, but bronchitis is predominantly infectious or irritant in origin. Natalizumab's defining safety concern is *increased* infection risk (most notably progressive multifocal leukoencephalopathy, PML, from JC virus reactivation) — a direction that runs opposite to what would be needed to safely treat an infection-driven respiratory condition. No clinical trial or publication in this evidence pack connects natalizumab to bronchitis in either direction.

For added context: among this drug's other predicted indications, the highest-evidence candidate (psoriasis, L4, 19 publications) shows the *opposite* relationship — multiple case reports and a cohort study document natalizumab **inducing or aggravating** psoriasis (paradoxical reaction), not treating it. This pattern reinforces that a high TxGNN score alone should not be read as a treatment signal without directional literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Natalizumab is not currently marketed in Finland (market status: 未上市, 0 authorizations on record). No product license data is available for this candidate.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/package-insert warnings, contraindications, and drug-drug interaction data are all outstanding — see Data Gap DG001, Blocking severity.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction has no clinical trial or literature support (L5, model prediction only), and the proposed mechanism conflicts with natalizumab's known immunosuppressive/infection-risk profile (including PML), making it biologically implausible as currently evidenced.

**To proceed, the following is needed:**
- TFDA/Finland package insert data (safety warnings, contraindications) — DG001, currently blocking S1 safety review
- Confirmed mechanism of action from DrugBank — DG002
- Preclinical or in vitro evidence linking α4-integrin blockade to bronchitis pathophysiology, since none currently exists
- If further candidates from this same drug are pursued, prioritize psoriasis (L4, 19 publications) for review instead — though note the existing literature there points toward an adverse (disease-inducing) relationship rather than a therapeutic one, so it would also require careful reframing before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

