---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 0
---

# Basiliximab
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

# Basiliximab: From Organ Transplant Rejection Prevention — No TxGNN Repurposing Predictions Available

## One-Sentence Summary

Basiliximab (Simulect®) is a chimeric monoclonal antibody targeting the IL-2 receptor (CD25), clinically established for prevention of acute rejection in renal transplant recipients.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, meaning a new indication target cannot yet be evaluated.
This report documents the data status and recommends the next steps needed before a repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of acute organ rejection in renal transplantation (IL-2 receptor antagonist, per DrugBank DB00074) |
| Predicted New Indication | Not available — TxGNN prediction pipeline returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No prediction to evaluate |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

Basiliximab is a chimeric monoclonal antibody (IgG1κ) directed against the α-chain of the interleukin-2 receptor (CD25), which is expressed on activated T-lymphocytes. By competitively blocking IL-2 binding, basiliximab suppresses clonal expansion of T-cells, thereby reducing the acute rejection response following allogeneic transplantation.

The TxGNN knowledge-graph model relies on rich pharmacological and disease-association data to generate repurposing candidates. The Evidence Pack shows that critical inputs — including the drug's mechanism-of-action annotation and original indication classification — were flagged as data gaps at the time of pipeline execution. The absence of these structured inputs is the most likely reason the model returned an empty prediction list.

There is emerging off-label clinical interest in basiliximab for **graft-versus-host disease (GVHD)** and steroid-refractory inflammatory conditions, which suggests plausible biological rationale for repurposing once the pipeline inputs are completed and rerun.

---

## Finland Market Information

Basiliximab is not currently registered in Finland. No marketing authorizations were found in the regulatory query performed on 2026-03-29.

> **Note:** Basiliximab (Simulect®) holds EMA approval for prophylaxis of acute organ rejection in de novo allogeneic renal transplantation in adult and paediatric patients, which may serve as the basis for a future Finnish market application. EMA documentation can be consulted as a reference source.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) were not available in the Evidence Pack for this evaluation cycle. Please refer to the official package insert and EMA product information for full safety information, including post-transplant lymphoproliferative disorder risk, cytokine release syndrome precautions, and immunosuppression-related infection risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline returned no candidate indications for basiliximab, and critical input fields (MOA annotation, original indication classification) were flagged as blocking data gaps. Without a prediction target, a repurposing evidence assessment cannot be conducted.

**To proceed, the following is needed:**

1. **Complete the MOA data gap (DG002):** Query DrugBank API for structured pharmacology data and populate the `original_moa` field so the knowledge graph can build correct node embeddings.
2. **Classify original indication (DG001):** Map basiliximab to a structured disease ontology term (e.g., MONDO or ICD-10 for "prophylaxis of renal allograft rejection") and re-run the TxGNN prediction pipeline.
3. **Re-run TxGNN:** After resolving the above gaps, execute the prediction pipeline; candidate indications (e.g., GVHD, autoimmune nephritis) are expected to appear.
4. **Obtain safety source data:** Download and parse the EMA/TFDA package insert PDF to populate warnings and contraindications fields before proceeding to the safety screening stage (S1).
5. **Confirm Finland registration pathway:** If a repurposing candidate is identified, assess whether the EMA-approved transplant rejection indication can anchor a line-extension application in Finland.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

