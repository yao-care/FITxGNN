---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel: From Antiplatelet Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a P2Y12/ADP receptor antagonist (thienopyridine class) widely used for atherothrombotic event prevention; no Taiwan-specific approved-indication text is available in this Evidence Pack (drug not currently marketed in Taiwan). The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, but currently only literature evidence supports this specific subtype — **0 clinical trials** and **16 publications**, most of which study clopidogrel in migraine patients with a documented patent foramen ovale (PFO) or right-to-left shunt (RLS).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack — drug not marketed in Taiwan (0 license records); general drug information indicates antiplatelet/atherothrombotic event prevention |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for clopidogrel is not available from this Evidence Pack ([Data Gap] flagged as High severity, DG002). Based on the repurposing rationale generated from the knowledge graph, clopidogrel is a P2Y12 receptor antagonist that inhibits ADP-dependent platelet activation — a well-established antiplatelet mechanism.

The proposed link to migraine with brainstem aura rests on the PFO/right-to-left shunt (RLS) paradoxical microembolization hypothesis: micro-emboli or platelet aggregates crossing an undiagnosed shunt are thought to trigger cortical spreading depression, the physiological correlate of migraine aura. Because aura-type migraines (including the brainstem subtype) are mechanistically closer to this embolic trigger than migraine without aura, platelet inhibition with clopidogrel is hypothesized to reduce aura frequency in this subgroup.

Notably, a closely related and more thoroughly evidenced indication in this same pack — "migraine disorder" (rank 2, same TxGNN score range, 99.44%) — has a completed Phase 4 RCT (CANOA, n=220) directly testing clopidogrel for migraine prevention after atrial septal defect closure. Since both indications share the identical PFO/RLS mechanistic basis, that trial evidence is highly relevant supporting context for the brainstem-aura subtype, even though no trial has enrolled brainstem-aura patients specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered for "migraine with brainstem aura" specifically.

*(For context: the closely related indication "migraine disorder" has a completed Phase 4 RCT — [NCT00799045](https://clinicaltrials.gov/study/NCT00799045), the CANOA study, n=220 — testing clopidogrel + aspirin for prevention of new-onset migraine after transcatheter ASD closure.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: percutaneous PFO closure in migraine with aura, randomized controlled |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT | Cephalalgia | Pilot randomized controlled study of clopidogrel as prophylactic treatment for migraine |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Review | Headache | Systematic review on the role of antithrombotic drugs in migraine prevention |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart (British Cardiac Society) | Clopidogrel reduced migraine with aura after transcatheter PFO/ASD closure |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | J Investigative Medicine | Clopidogrel as complementary prophylaxis for drug-refractory migraine with PFO |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Cohort | Neurology | TRACTOR pilot study: thienopyridines (incl. clopidogrel) reduced migraine symptoms in PFO patients |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Cohort | Neurology | Retrospective review of thienopyridine therapy in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Cohort | Cephalalgia | Retrospective review of clopidogrel as primary therapy for migraineurs with right-to-left shunt lesions |
| [33815258](https://pubmed.ncbi.nlm.nih.gov/33815258/) | 2021 | Case Report | Frontiers in Neurology | Migraine-like headache with visual aura after endovascular coiling for PCA aneurysm |
| [36588875](https://pubmed.ncbi.nlm.nih.gov/36588875/) | 2022 | Case Report | Frontiers in Neurology | Aura migraine elicited by isolated pulmonary arteriovenous fistula |

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings, contraindications, and DDI data are flagged as a Blocking data gap — DG001 — in this Evidence Pack and must be resolved before any S1 safety pre-assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for clopidogrel in migraine with brainstem aura specifically is L2 (literature-only, including two small RCTs), with zero registered clinical trials for this exact subtype. The mechanistic rationale is credible but is entirely dependent on an unconfirmed PFO/RLS comorbidity subgroup, and no data confirms this applies broadly to brainstem-type aura.

**To proceed, the following is needed:**
- TFDA/package insert data for clopidogrel (warnings, contraindications, DDI) — currently a Blocking gap (DG001)
- DrugBank-sourced MOA confirmation — currently a High-severity gap (DG002)
- A defined patient selection protocol requiring confirmed PFO/RLS status prior to treatment
- Consideration of whether to pursue the better-evidenced "migraine disorder" indication (rank 2, completed Phase 4 CANOA RCT) instead of, or alongside, the brainstem-aura subtype
- Taiwan market/regulatory pathway assessment, since the drug currently holds zero local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

