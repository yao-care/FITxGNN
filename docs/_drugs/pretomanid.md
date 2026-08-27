---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 5
---

# Pretomanid
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

# Pretomanid: From Multidrug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

Pretomanid (PA-824) is a nitroimidazooxazine antimycobacterial approved internationally as part of the BPaL/BPaLM regimen for extensively drug-resistant (XDR) and treatment-intolerant/non-responsive multidrug-resistant (MDR) pulmonary tuberculosis. The TxGNN model predicts it may be effective for **Candidiasis**, with a prediction score of **99.69%**, but currently **0 clinical trials** and **0 publications** support this direction, and the evidence pack's own mechanistic analysis explicitly finds no biological rationale for the link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multidrug-resistant / extensively drug-resistant pulmonary tuberculosis (BPaL/BPaLM regimen) — no local license record exists; this is derived from the literature entries in the evidence pack, not from a formal indication field |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (`original_moa` is a data gap). However, the evidence pack's own supporting text describes pretomanid's known pharmacology: it is a bicyclic nitroimidazole prodrug that is activated by the mycobacterium-specific Ddn nitroreductase, which inhibits mycolic acid synthesis and releases nitric oxide to produce bactericidal activity against *Mycobacterium* species.

This mechanism is specific to mycobacterial cell wall biosynthesis and has no known counterpart in fungal biology. Candidiasis is caused by *Candida* species (fungi), which do not share the Ddn-nitroreductase activation pathway or mycolic acid synthesis machinery that pretomanid targets. The evidence pack's own rationale for this prediction states explicitly: *"無。Pretomanid 作用標的為分枝桿菌特有的 Ddn 硝基還原酶活化路徑與分枝菌酸合成抑制，Candida 為真菌，無同源標的，亦無已知抗真菌活性機轉"* — i.e., no mechanistic link exists.

Given the absence of any supporting mechanism, clinical trial, or literature evidence, this prediction should be treated as a likely model artifact rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Pretomanid holds no local marketing authorization in this market (`market_status: 未上市`, `total_licenses: 0`), so no authorization records are available to list.

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** the underlying data pack flags this drug's local package-insert warnings/contraindications as a **blocking data gap (DG001)** — meaning no formal S1 safety assessment can be completed yet. Separately, the pack's own analysis of a different candidate indication (myocardial ischemia) notes that pretomanid carries a **known QT-prolongation risk**, particularly when used in the BPaL regimen with bedaquiline. This is not formal safety data extracted from a label, but it is a documented signal worth carrying forward into any future evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical or literature evidence for candidiasis, and the evidence pack's own mechanistic review concludes there is no plausible biological link (antimycobacterial vs. antifungal target mismatch). A blocking data gap on the local package insert (DG001) also prevents any formal safety review from proceeding.

**To proceed, the following is needed:**
- Local regulatory package insert (warnings/contraindications) to resolve DG001 before any S1 safety assessment
- Confirmed MOA data via DrugBank API to resolve DG002
- In vitro/in vivo antifungal activity data for pretomanid against *Candida*, since none currently exists
- For reference, the next-ranked prediction (leprosy, L4) has actual trial/literature coverage but is also contradicted by direct in vitro evidence (PMID 17005816) showing *M. leprae* is naturally resistant to PA-824 — so it is not a stronger candidate either. Ranks 3–5 (coronary artery disease, myocardial ischemia, anomalous coronary artery) have no mechanistic basis and no evidence, and should be treated as low-priority model noise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

