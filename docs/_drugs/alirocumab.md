---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

Alirocumab is a PCSK9-inhibitor monoclonal antibody originally used to lower LDL cholesterol and reduce cardiovascular risk in patients with hypercholesterolemia. The TxGNN model predicts it may also be effective for **Cholesterol Catabolic Process Disease** (a category that includes homozygous familial hypercholesterolemia, HoFH), with **1 completed Phase 3-related clinical trial** and **19 publications** currently supporting this direction. This candidate is essentially an extension of alirocumab's core mechanism rather than a mechanistic leap, which is reflected in its unusually strong evidence base compared with the drug's other predicted indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / ASCVD risk reduction (PCSK9 inhibition) — *official approved-label text unavailable; see Data Gap note below* |
| Predicted New Indication | Cholesterol Catabolic Process Disease (incl. homozygous familial hypercholesterolemia) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is currently a data gap for this record. Based on the literature evidence collected in this pack, alirocumab is a human monoclonal antibody that binds circulating PCSK9 (proprotein convertase subtilisin/kexin type 9), preventing it from binding to the hepatic LDL receptor (LDLR). By blocking PCSK9-mediated LDLR degradation, more LDLR is recycled to the hepatocyte surface, increasing clearance of LDL cholesterol from the blood (PMID 39947256, 38185721).

The predicted new indication, "cholesterol catabolic process disease," is not a distant or speculative target — it describes disorders of cholesterol handling and clearance, including homozygous familial hypercholesterolemia (HoFH), a condition defined by severely impaired LDLR function. Since alirocumab's entire pharmacology is built around enhancing LDLR-mediated clearance, this indication sits directly on-mechanism rather than requiring a novel biological hypothesis. This is consistent with why the evidence level here (L1) is far stronger than for the drug's other TxGNN-ranked candidates (e.g., ichthyosis, xanthomatosis, or diaphyseal dysplasia), which involve mechanistically unrelated or indirect graph connections.

Supporting this, the literature base includes both dedicated HoFH treatment reviews (PMID 39751968) and large-scale, long-term safety data from the ODYSSEY OUTCOMES program (47,296 patient-years, PMID 38658193), indicating that the drug-disease relationship is already well characterized in real-world and controlled settings, even though it has not been evaluated here as a de novo "new indication" trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | EPIC-HIV study: evaluated PCSK9 inhibition's effect on cardiovascular risk and atherosclerotic plaque in HIV-infected patients with dyslipidemia; directly tests PCSK9 inhibition's impact on cholesterol-metabolism-related cardiovascular outcomes. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Reviews novel pharmacological therapies, including PCSK9 inhibitors, for homozygous familial hypercholesterolemia (HoFH). |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Review (RCT synthesis) | Kardiologia Polska | Synthesizes evidence on PCSK9 inhibitors' impact on lipid parameters and cardiovascular event reduction. |
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Safety/Observational | European Heart Journal - Cardiovascular Pharmacotherapy | Alirocumab safety analysis from ODYSSEY OUTCOMES, covering 47,296 patient-years of observation. |
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | Post hoc RCT analysis | Diabetes Care | ODYSSEY OUTCOMES post hoc analysis of alirocumab's effect on lipoprotein(a), LDL-C, and diabetes risk. |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduction and Targeted Therapy | Comprehensive review of PCSK9 biology and its therapeutic targeting across lipid and non-lipid diseases. |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review | Current Opinion in Lipidology | Update on PCSK9-directed therapies and their differing mechanisms of action. |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Reviews diagnostics and treatment of familial hypercholesterolemia, including PCSK9-targeted options. |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | Review | Pharmacotherapy | State-of-the-art review of current and emerging PCSK9-directed therapies for ASCVD risk reduction. |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Review (mechanism) | Pharmacology & Therapeutics | Compares intracellular vs. extracellular PCSK9-targeting strategies, discussing alirocumab specifically. |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Review | International Journal of Molecular Sciences | Reviews current dyslipidemia treatment approaches, including PCSK9 inhibition. |

---

## Finland Market Information

Currently no marketing authorization records are available for Alirocumab in Finland (market status: **Not Marketed**, 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available for this record — notably, the official TFDA/Fimea package insert (warnings and contraindications) has not yet been retrieved, which is flagged as a **Blocking** data gap and prevents this candidate from completing formal safety pre-assessment (S1) at the drug level.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is mechanistically well-aligned with alirocumab's established pharmacology (PCSK9 inhibition → LDLR-mediated cholesterol clearance), and is supported by a completed Phase 3-related trial plus a substantial literature base, including long-term safety data from ODYSSEY OUTCOMES. However, the drug-level safety review remains blocked by a missing official package insert, so guardrails are required before any further action.

**To proceed, the following is needed:**
- Retrieve the official TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Obtain formal DrugBank mechanism-of-action documentation to replace the current data gap (DG002)
- Clarify whether "cholesterol catabolic process disease" as scored by TxGNN maps to a genuinely new indication or substantially overlaps with alirocumab's existing approved use in HoFH/hypercholesterolemia
- Confirm route-of-administration compatibility for the target population (currently marked "pending")
- Note: other TxGNN-predicted indications for this drug (e.g., xanthomatosis, ichthyosis, diaphyseal dysplasia) carry only L4–L5 evidence and remain on **Hold** pending stronger mechanistic or clinical support; they are not part of this recommendation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

