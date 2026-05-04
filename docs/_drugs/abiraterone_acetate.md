---
layout: default
title: Abiraterone Acetate
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# ABIRATERONE ACETATE: Drug Repurposing Evaluation — Insufficient Data for Assessment

## One-Sentence Summary

Abiraterone acetate is a CYP17A1 inhibitor primarily used for the treatment of metastatic castration-resistant prostate cancer (mCRPC). The TxGNN model has **not generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps across regulatory, safety, and mechanistic domains. **No repurposing assessment can be completed at this time.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (known use: metastatic prostate cancer) |
| Predicted New Indication | **None** — No TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — No predictions or supporting studies available |
| Taiwan Market Status | ❌ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, abiraterone acetate is a prodrug of abiraterone, which acts as a selective, irreversible inhibitor of CYP17A1 (17α-hydroxylase/C17,20-lyase). This enzyme is critical in the androgen biosynthesis pathway. By blocking CYP17A1, abiraterone reduces the production of testosterone and other androgens, thereby inhibiting the growth of androgen-dependent prostate cancer cells.

However, **no TxGNN-predicted indications were provided in the evidence pack**. Without a predicted new indication, it is not possible to evaluate the biological plausibility of any repurposing hypothesis. The absence of predictions may reflect insufficient data in the knowledge graph, or may indicate that the model did not identify high-confidence novel indications beyond the drug's established uses.

Before any repurposing analysis can proceed, the TxGNN prediction pipeline must be re-run or supplemented with additional data to generate candidate indications for evaluation.

---

## Clinical Trial Evidence

No TxGNN-predicted indication is available; therefore, no indication-specific clinical trial search was conducted.

---

## Literature Evidence

No TxGNN-predicted indication is available; therefore, no indication-specific literature search was conducted.

---

## Taiwan Market Information

Abiraterone acetate currently has **no TFDA marketing authorizations** in Taiwan. No license records were found in the regulatory query conducted on 2026-03-29.

---

## Cytotoxicity

Abiraterone acetate is an antineoplastic agent (androgen biosynthesis inhibitor targeting CYP17A1). The following cytotoxicity profile is based on the drug's known pharmacological class:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CYP17A1 inhibitor — not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (myelosuppression is uncommon; however, monitoring is recommended) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST monthly), blood pressure, serum potassium, cardiac function, cortisol levels |
| Handling Protection | Standard handling precautions for antineoplastic oral agents; no special cytotoxic handling required as it is a non-cytotoxic targeted therapy |

> Note: Abiraterone acetate must be co-administered with prednisone/prednisolone to mitigate mineralocorticoid excess side effects (hypertension, hypokalaemia, fluid retention) caused by CYP17A1 inhibition upstream of the mineralocorticoid pathway.

---

## Safety Considerations

Safety data was not available in the evidence pack. Both TFDA package insert warnings and contraindication data were queried but returned no extractable results.

> Please refer to the package insert for complete safety information. Key known safety concerns for abiraterone acetate include hepatotoxicity, mineralocorticoid-related adverse effects (hypertension, hypokalaemia, oedema), and cardiac disorders. It is contraindicated in severe hepatic impairment and in women who are or may become pregnant.

---

## Data Gaps Summary

The following critical data gaps were identified in the evidence pack:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanism-relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications were generated for abiraterone acetate, making a repurposing evaluation impossible at this stage. Additionally, the drug is not currently marketed in Taiwan, and critical safety and regulatory data gaps remain unresolved (severity: Blocking).

**To proceed, the following is needed:**
- **Re-run TxGNN prediction pipeline** with complete knowledge graph data to generate candidate new indications
- **Resolve DG001 (Blocking):** Obtain and parse the TFDA package insert to extract warnings and contraindications
- **Resolve DG002 (High):** Query DrugBank API for the full mechanism of action and obtain the DrugBank ID
- **Obtain Taiwan regulatory information:** Confirm whether abiraterone acetate has been submitted for TFDA review or if any applications are pending
- **Supplement drug identity data:** Populate DrugBank ID, brand name, and original indication fields in the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

