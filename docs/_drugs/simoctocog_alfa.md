---
layout: default
title: Simoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

> Simoctocog alfa is a recombinant human Factor VIII (B-domain-deleted rFVIII) used as replacement therapy in Hemophilia A.
> The TxGNN model's top prediction is **Pseudo-von Willebrand Disease**, but this is currently supported by **0 clinical trials** and **0 publications** — it is a computational hypothesis only, not an evidence-backed signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (FVIII replacement therapy) — inferred from internal rationale notes; formal approved-indication text not yet retrieved |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 (model prediction only) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available for simoctocog alfa (flagged as a High-severity data gap). Based on information available in this evidence pack, simoctocog alfa is a B-domain-deleted recombinant Factor VIII whose only established pharmacological action is replacing/supplementing endogenous FVIII activity in the coagulation cascade.

Pseudo-von Willebrand disease (platelet-type vWD) is caused by a gain-of-function mutation in the platelet receptor GPIbα that increases its affinity for von Willebrand factor (VWF) — the pathology sits at the platelet receptor, not at Factor VIII itself. Because plasma FVIII circulates bound to VWF and depends on it for stability, there is an indirect biochemical relationship between the two proteins, but supplementing exogenous FVIII does not correct the GPIbα defect and could theoretically worsen platelet clearance by increasing VWF–platelet binding.

Overall, the mechanistic link for this top-ranked prediction is weak, and the model score likely reflects semantic clustering around "bleeding disorders" in the knowledge graph rather than a validated causal pathway. Of the 10 predicted indications reviewed, rank #9 ("Hemophilia A with vascular abnormality") is mechanistically the most consistent with FVIII's known pharmacology, while rank #4 ("Scott syndrome") has a plausible indirect link via phosphatidylserine exposure and tenase complex assembly — both are noted here for context, though the template's primary output above reflects rank #1 as specified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Simoctocog alfa is currently **not marketed** in Finland (0 authorizations on record); no license entries are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — retrieval of the TFDA/Fimea package insert is a blocking data gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN network score (L5) — no clinical trials, no literature, and a mechanistically weak rationale (the target pathology lies in platelet receptor biology, not the coagulation factor cascade FVIII acts on). Across all 10 predicted indications for this drug, none has any clinical or literature evidence, and several (e.g., thrombotic thrombocytopenic purpura) are mechanistically contradictory to FVIII supplementation.

**To proceed, the following is needed:**
- TFDA/Fimea package insert warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism-of-action detail from DrugBank (High-priority gap, DG002)
- If pursuing further, prioritize mechanistically stronger candidates (e.g., Scott syndrome, or the FVIII-consistent "Hemophilia A with vascular abnormality") for targeted literature/trial searches before any translational commitment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

