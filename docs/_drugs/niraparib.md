---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: From Ovarian Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Niraparib is a PARP inhibitor established as maintenance therapy for recurrent epithelial ovarian, fallopian tube, and primary peritoneal cancer (per trial/literature records in this evidence pack; structured regulatory fields for original indication and MOA are not populated). The TxGNN model's top-ranked prediction for this drug is **Epiglottis Neoplasm**, but this candidate currently has **zero clinical trials and zero publications** supporting it — the prediction rests entirely on model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (maintenance treatment of recurrent epithelial ovarian/fallopian tube/primary peritoneal cancer) — derived from trial/literature text; structured field is a data gap |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured drug record (`original_moa: [Data Gap]`). Based on information found elsewhere in this evidence pack, niraparib is a PARP (poly ADP-ribose polymerase) inhibitor that exploits synthetic lethality in tumors with homologous recombination deficiency (HRD), including BRCA1/2 mutations — it is used clinically as maintenance therapy in platinum-sensitive, BRCA-mutated or HRD-positive ovarian cancer.

Epiglottis neoplasm falls under head and neck squamous cell carcinoma, a tumor type with a very low prevalence of HRD/BRCA mutations compared to high-grade serous ovarian cancer. There is no established biological rationale connecting niraparib's synthetic-lethality mechanism to this tumor site.

Consequently, this prediction should be treated as a pure model-score signal rather than a mechanistically or clinically supported hypothesis. The high TxGNN score most likely reflects embedding similarity in the knowledge graph rather than genuine biological plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Cytotoxicity

Niraparib is an antineoplastic (targeted anticancer) agent, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for niraparib in epiglottis neoplasm, and the mechanistic link is theoretical at best given the low HRD/BRCA prevalence in head and neck cancers — this is an L5, model-only prediction. Notably, a lower-ranked candidate in this evidence pack, "cystic neoplasm" (largely reflecting high-grade serous ovarian/endometrial serous carcinoma), has substantially stronger support (3 trials, 9 publications, L2/S2) and may warrant separate evaluation.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a **Blocking** data gap preventing entry into S1 safety review
- Confirmed mechanism-of-action documentation from DrugBank
- Preclinical or mechanistic data on PARP inhibitor activity in laryngeal/hypopharyngeal tumors, or HRD/BRCA mutation prevalence data specific to epiglottis neoplasm
- If pursuing repurposing further, prioritize the higher-evidence "cystic neoplasm" (HGSOC/endometrial serous carcinoma) candidate instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

