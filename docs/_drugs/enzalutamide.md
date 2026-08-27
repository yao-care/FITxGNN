---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an androgen receptor (AR) antagonist whose established, approved use is metastatic castration-resistant/hormone-sensitive prostate cancer. TxGNN's top-ranked prediction for this drug is the composite label **"prostate cancer/brain cancer susceptibility"** (score **99.71%**), but this candidate currently has **zero clinical trials and zero publications** directly supporting it, and the model's own rationale flags it as likely overlapping with the drug's known indication rather than a genuine new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Fimea license records (0 authorizations on file). Based on the drug's known AR-antagonist mechanism referenced elsewhere in this evidence pack, Enzalutamide's approved use is prostate cancer (castration-resistant / hormone-sensitive, mCRPC/mHSPC) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Enzalutamide is formally flagged as a data gap in this evidence pack (DG002, High severity). However, the rationale attached to a related candidate ("male reproductive organ cancer," rank 6) confirms that Enzalutamide acts as an **AR (androgen receptor) antagonist**, directly blocking androgen-driven proliferation signaling in prostate cancer cells — this is the drug's core, already-approved mechanism, not a novel hypothesis.

This context matters for interpreting the rank-1 prediction: the "prostate cancer" component of "prostate cancer/brain cancer susceptibility" likely reflects the model detecting the drug's **known** indication rather than surfacing something new. The "brain cancer susceptibility" component has no established mechanistic rationale — AR signaling's role in central nervous system tumor susceptibility is not established in the literature or evidence supplied here.

The evidence pack itself explicitly recommends caution: it notes this label should be reviewed alongside the "male reproductive organ cancer" candidate to avoid double-counting the same underlying prostate-cancer biology as two separate "new" hypotheses. In short, this top-ranked prediction is best read as a **high embedding-similarity artifact** rather than a mechanistically grounded repurposing signal, and it currently has no clinical or literature corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

Enzalutamide is not currently marketed in Finland — the Fimea regulatory record shows 0 marketing authorizations and no license entries are available to summarize.

---

## Cytotoxicity

*(Included because Enzalutamide is an antineoplastic agent used for prostate cancer.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (androgen receptor signaling inhibitor; non-cytotoxic hormonal agent) |
| Myelosuppression Risk | Low — AR inhibitors as a class typically carry lower myelosuppressive potential than conventional cytotoxic chemotherapy; no drug-specific toxicity data are available in this evidence pack |
| Emetogenicity Classification | Low — oral hormonal/targeted agents generally have minimal emetogenic potential |
| Monitoring Items | Please refer to the package insert warnings and precautions (no toxicity/monitoring data available in this evidence pack) |
| Handling Protection | Please refer to the package insert warnings and precautions (institutional hazardous-drug handling classification not available in this evidence pack) |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and DDI data are all recorded as data gaps in this evidence pack — DG001, Blocking severity — meaning a formal safety pre-screen (S1) cannot currently be performed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction ("prostate cancer/brain cancer susceptibility") has no supporting clinical trials or literature and is classified L5 (model prediction only). Its "prostate cancer" component likely restates the drug's already-known indication rather than a genuine repurposing signal, and its "brain cancer susceptibility" component lacks mechanistic support. Combined with a Blocking-severity safety data gap and no Finland market presence, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently Blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record — currently High-severity data gap (DG002)
- Direct clinical or literature evidence specifically addressing "prostate cancer/brain cancer susceptibility" as a distinct indication (none currently exists)
- De-duplication review against the overlapping "male reproductive organ cancer" candidate (rank 6, L1/S3) to confirm whether these represent one biological hypothesis or two
- A completed drug-drug interaction (DDI) database query (current status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

