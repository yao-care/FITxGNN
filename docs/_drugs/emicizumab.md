---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

Using the drug repurposing evaluation report template (v5) as instructed by the prompt, here is the report generated from the Evidence Pack.

---

# Emicizumab: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Emicizumab is a bispecific monoclonal antibody whose established clinical use (per the literature contained in this evidence pack) is bleeding prophylaxis in congenital and acquired hemophilia A. The TxGNN model's top-ranked prediction is **Pseudo-von Willebrand Disease**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review states there is **no plausible mechanistic link** between emicizumab and this disease. Formal Finland/TFDA regulatory data (original indication, package-insert warnings, mechanism of action) are currently unavailable and are flagged as data gaps.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in regulatory data (data gap). Literature context in this pack indicates congenital/acquired Hemophilia A (FVIII-mimetic prophylaxis) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank in this evidence pack (Data Gap DG002, severity: High). Based on information found elsewhere in this same evidence pack (literature abstracts collected under the "acquired coagulation factor deficiency" candidate), emicizumab is a bispecific antibody that mimics the cofactor function of activated coagulation Factor VIII by bridging Factor IXa and Factor X, restoring thrombin generation. It is used clinically for bleeding prophylaxis in both congenital hemophilia A (with or without FVIII inhibitors) and, increasingly, acquired hemophilia A.

The top-ranked TxGNN candidate, Pseudo-von Willebrand Disease, is a gain-of-function disorder of platelet membrane glycoprotein Ib (GPIbα) that causes abnormal spontaneous binding between platelets and von Willebrand factor. This is a **platelet-receptor defect**, not a coagulation-factor-cascade defect — mechanistically distinct from emicizumab's FIXa–FX bridging activity. The evidence pack's own repurposing rationale for this candidate explicitly concludes there is "no mechanistic plausibility support" (無機轉合理性支持) for this pairing.

This is an important caveat for interpreting the 99.99% TxGNN score: despite being the single highest-scoring prediction among the ten candidates in this pack, it carries the weakest possible evidence tier (L5 — model prediction only, no trials, no literature) and a mechanistic rationale that argues *against* biological plausibility. A high similarity score from the model should be read as a network-topology signal, not as evidence of mechanistic fit — the two must be evaluated separately, as they are in this pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

---

## Other Candidates in This Evidence Pack (Supplementary)

Because the top-ranked candidate has essentially no direct evidence, it is worth noting that two lower-ranked candidates in the same evidence pack carry meaningfully stronger support and may be better targets for follow-up evaluation:

| Rank | Disease | TxGNN Score | Evidence Level | Supporting Evidence |
|------|---------|-------------|-----------------|----------------------|
| 3 | Glanzmann thrombasthenia | 99.98% | L4 | 1 registry-type trial ([NCT04398628](https://clinicaltrials.gov/study/NCT04398628), non-interventional, relevance grade C) + 1 review article (PMID [37391649](https://pubmed.ncbi.nlm.nih.gov/37391649/), focused on rFVIIa, not emicizumab-specific). Mechanistic link is indirect — Glanzmann's is a GPIIb/IIIa platelet-aggregation defect, not a FVIII/IX/X-pathway defect. |
| 5 | Acquired coagulation factor deficiency | 99.90% | Not yet finalized in this pack ("pending"), but data suggests it should score well above L4 | 1 registry trial + **20 PubMed publications**, including a completed Phase 3 study (AGEHA, PMID [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/)) and a published Phase 2 trial directly testing emicizumab in acquired hemophilia A (GTH-AHA-EMI, *Lancet Haematology*, PMID [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/)). Mechanism directly matches emicizumab's known FVIII-mimetic activity. |

**Risk flags identified elsewhere in this pack that should not proceed further:**
- **Rank 8 – Thrombotic thrombocytopenic purpura**: mechanistically contraindicated. TTP is a pro-thrombotic, ADAMTS13-deficiency disorder; administering a pro-coagulant (emicizumab) is directionally opposite to the treatment goal and raises a safety concern, not just an evidence gap.
- **Rank 10 – "flood factor deficiency"**: the evidence pack itself flags this as a likely OCR/data-mapping error with no resolvable disease-ontology match; it should be corrected at the source before any further evaluation.

---

## Finland Market Information

Emicizumab is not currently marketed in Finland — `taiwan_regulatory.market_status` reports "Not Marketed" with 0 registered marketing authorizations. No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — including a Blocking-severity gap for TFDA package-insert warnings/contraindications, DG001 — so no S1 safety pre-screen can be completed at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Pseudo-von Willebrand Disease) has L5 evidence — no clinical trials, no literature — and its own mechanistic rationale explicitly rules out biological plausibility. Combined with a Blocking-severity data gap on TFDA package-insert safety data (DG001), this candidate cannot proceed past S0/S1 in its current form.

**To proceed, the following is needed:**
- TFDA/EU package-insert warnings and contraindications (DG001, Blocking) — required before any S1 safety pre-screen
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Confirmed original indication and Finland licensing history (currently absent from `taiwan_regulatory`)
- If pursuing this evidence pack further, **redirect evaluation priority to rank 5 (acquired coagulation factor deficiency)**, which already has a completed Phase 3 trial (AGEHA) and a published Phase 2 RCT (GTH-AHA-EMI) directly supporting emicizumab use — this candidate likely merits an L1/L2 evidence-level reassessment rather than the "pending" status currently shown
- Correct the disease-ontology mapping for rank 10 ("flood factor deficiency") before further use
- Exclude rank 8 (TTP) from further repurposing consideration on mechanistic/safety grounds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

