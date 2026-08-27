---
layout: default
title: Norelgestromin
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 1
---

# Norelgestromin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin is the active metabolite of norgestimate and the main active ingredient of transdermal contraceptive patches (Ortho Evra/Xulane), originally used for hormonal contraception. The TxGNN model predicts it may be relevant to **Amenorrhea**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on mechanistic plausibility alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (active ingredient of transdermal contraceptive patch) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a data gap). Based on the information available in this evidence pack, norelgestromin is the active metabolite of norgestimate, classified as a third-generation progestin, and serves as the main active ingredient of the Ortho Evra/Xulane contraceptive patch. Its established pharmacological action is agonism of the progesterone receptor, which suppresses ovulation and alters the endometrium.

Progestin-class drugs are clinically known to commonly cause amenorrhea as a side effect, and continuous progestin regimens are sometimes deliberately used to induce amenorrhea for management of conditions such as menorrhagia. This gives norelgestromin a plausible mechanistic link to amenorrhea. However, the TxGNN prediction does not distinguish between "inducing" and "treating" amenorrhea, so the directionality of this association is unclear.

Because the original MOA field is a confirmed data gap, this mechanistic rationale should be treated as provisional until verified against external pharmacology sources (e.g., DrugBank, DailyMed) before it can support any causal claim.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by mechanistic reasoning (L5, model prediction only) with no clinical trials or published literature confirming a therapeutic effect in amenorrhea, and the directionality (induces vs. treats) is unresolved. Core drug-level data — TFDA/Fimea package insert warnings and contraindications, and confirmed mechanism of action — are also blocking data gaps.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap
- Clinical or literature evidence specifically evaluating norelgestromin (or related progestins) for amenorrhea treatment, rather than as a contraceptive side effect
- Clarification of whether the intended application is inducing or treating amenorrhea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

