---
layout: default
title: Tasonermin
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Tasonermin
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

# Tasonermin: From Soft Tissue Sarcoma (Limb Perfusion) to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Tasonermin (recombinant human TNF-alpha, marketed elsewhere as Beromun) is a cytokine agent whose established clinical use is isolated limb perfusion for soft tissue sarcoma. The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, but this is currently a **pure model prediction with zero supporting clinical trials or publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma (isolated limb perfusion) — per known drug background; not licensed in Finland |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism of action data for Tasonermin is not yet available (flagged as a High-severity data gap). Based on known general information, Tasonermin is a recombinant human TNF-alpha with tumor vascular-endothelial-disruptive, pro-apoptotic, and immunomodulatory activity, giving it theoretical broad-spectrum antitumor potential across solid tumors.

However, its only established clinical use is isolated limb perfusion for soft tissue sarcoma — a locoregional delivery route chosen specifically because systemic administration of TNF-alpha causes severe, shock-like toxicity. Prostatic urethra urothelial carcinoma has no established locoregional perfusion treatment paradigm analogous to limb perfusion, so the delivery model that makes Tasonermin clinically usable does not obviously transfer to this indication.

No urothelial-carcinoma-specific mechanistic, preclinical, or clinical evidence currently supports this prediction — it derives purely from TxGNN's graph-based association scoring.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Tasonermin is not currently marketed in Finland (0 authorizations on record); no license or approved-indication data is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy / cytokine therapy (recombinant TNF-alpha) |
| Myelosuppression Risk | Please refer to the package insert for safety information; known systemic risk for this class is severe cytokine-release/shock-like reaction rather than classic myelosuppression |
| Emetogenicity Classification | Please refer to the package insert for safety information |
| Monitoring Items | Hemodynamic/cardiovascular monitoring (particularly if any systemic or perfusion-based exposure), CBC, liver and renal function |
| Handling Protection | Handle per institutional cytotoxic/biologic agent protocols pending confirmed labeling |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at evidence level L5 (decision stage S0) — the prediction is unsupported by any clinical trial, ICTRP record, or publication, and a Blocking data gap (missing TFDA/Fimea package insert warnings and contraindications) prevents even an initial safety review (S1). The mechanistic rationale is also weak: Tasonermin's only validated use relies on a locoregional perfusion delivery route not applicable to this new indication.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) to unblock S1 safety review
- Confirmed mechanism of action data from DrugBank or primary literature
- Preclinical or early clinical evidence specific to prostatic urethra urothelial carcinoma
- A feasible delivery-route rationale, given TNF-alpha's systemic toxicity constraints

*Note: This same L5/Hold status and evidence gap apply to the other 9 TxGNN-predicted indications in this evidence pack (ranks 2–10), none of which have clinical trial or literature support.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

