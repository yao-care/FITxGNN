---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using the evidence pack you provided, here is the evaluation report for **Acetylsalicylic Acid (Aspirin) → Migraine with Brainstem Aura** (the rank‑1 TxGNN prediction, `predicted_indications[0]`).

A quick methodological note before the report: this evidence pack actually contains **9 predicted indications** for aspirin with very different evidence quality — from essentially unsupported hits (e.g., *atrophoderma vermiculata*, *ulerythema ophryogenesis*, score >0.99 but zero literature/trials) to already well‑established uses (e.g., *thrombotic disease*, rank 8, L1 evidence, "Proceed with Guardrails"). Per the report specification, the primary report below covers **only rank 1** (`predicted_indications[0]`). I flag the stronger, lower‑ranked candidates in the Conclusion since they are relevant context for decision‑making, but they are outside the formal scope of this single‑indication report format.

---

# Acetylsalicylic Acid: From Antiplatelet/Analgesic Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a long-established analgesic, antipyretic, anti-inflammatory, and antiplatelet drug. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, with **0 disease-specific clinical trials** but **19 supporting publications** — mostly general migraine-with-aura literature rather than trials on this exact subtype. Evidence is currently hypothesis-generating rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No license text on file in the Fimea dataset (data gap, see DG001); aspirin is broadly established for analgesia, antipyresis, anti-inflammatory therapy, and antiplatelet/cardiovascular prophylaxis |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% (rank 947 among all predictions) |
| Evidence Level | L3 |
| Finland Market Status | ✗ Not Marketed (per current dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for aspirin is not available in this evidence pack (data gap DG002, High severity). Based on well-established pharmacological knowledge, however, aspirin is an irreversible COX-1/COX-2 inhibitor that blocks prostaglandin (PGE2) synthesis and, at low doses, permanently inactivates platelet thromboxane A2 production — giving it combined anti-inflammatory and antiplatelet effects.

Migraine with aura is thought to be driven by cortical spreading depression, trigeminovascular activation, neurogenic inflammation, and platelet/serotonin (5-HT) release during attacks. Aspirin's anti-inflammatory action (PGE2 synthesis inhibition) and antiplatelet effect could plausibly reduce neurogenic inflammation and platelet-mediated 5-HT release during an attack. The link is arguably strongest for the **brainstem aura** subtype specifically: this subtype is traditionally considered a relative contraindication for vasoconstrictive agents such as triptans (due to brainstem/basilar territory involvement), whereas aspirin has no vasoconstrictive action. This gives aspirin a theoretical mechanistic advantage as a non-vasoconstrictive option in exactly the population where the first-line acute drug class is discouraged.

That said, this mechanistic argument is currently an extrapolation. Almost all of the supporting literature addresses "migraine with aura" in general — not migraine with brainstem aura specifically — so the disease-specificity of the evidence is weak even though the general drug-class rationale is sound.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT (double-blind, double-dummy) | Cephalalgia | IV lysine acetylsalicylate vs. subcutaneous sumatriptan vs. placebo in 278 acute migraine patients (with/without aura); ASA showed efficacy broadly comparable to sumatriptan |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Reviews evidence on antithrombotic drugs (including aspirin) as migraine preventive therapy |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Cohort | Current Health Sciences Journal | 203 migraine-with-aura patients; ASA (low dose, n=95) compared with other prophylactic therapies (n=108) for efficacy/tolerability in aura prevention |
| [29017164](https://pubmed.ncbi.nlm.nih.gov/29017164/) | 2017 | Observational Case Series | European Neurology | Aspirin used as prophylaxis specifically for migraine with aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / Evidence Assessment (AHS) | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including aspirin-containing regimens |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Compares pathophysiology and management of episodic migraine with vs. without aura |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Overview of migraine-with-aura pathophysiology, centered on cortical spreading depression |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT (PRIMA trial) | European Heart Journal | Randomized trial of percutaneous PFO closure in migraine with aura — relevant to the aura/vascular mechanism link, not aspirin itself |
| [10534294](https://pubmed.ncbi.nlm.nih.gov/10534294/) | 1999 | Review | Journal of Women's Health & Gender-Based Medicine | Reviews menstrual migraine, largely without aura; hormonal influence on migraine frequency |
| [15891416](https://pubmed.ncbi.nlm.nih.gov/15891416/) | 2005 | Review | Current Opinion in Neurology | Discusses the PFO–migraine–stroke relationship relevant to aura pathophysiology |

*9 additional lower-relevance publications (general headache/triptan reviews, case reports) were identified but are not shown here; none specifically address migraine with brainstem aura or test aspirin in that subtype.*

---

## Finland Market Information

No marketing authorizations are on file for acetylsalicylic acid in the current dataset (0 licenses; status: Not Marketed). This is likely a **data-source limitation** rather than a true absence from the Finnish market — aspirin is a globally available, long-genericized OTC drug, and this gap should be verified against Fimea's product register directly before being treated as a factual finding.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No structured warnings, contraindications, or DDI data were retrievable for this candidate — see data gap DG001, Blocking severity, which also prevents a formal S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L3 (observational cohort + case series + reviews), with **zero clinical trials specific to migraine with brainstem aura** — the supporting literature almost entirely addresses migraine with aura in general, not this specific subtype.
- Two blocking/high-severity data gaps (Fimea package insert/warnings — DG001; DrugBank MOA — DG002) prevent even a preliminary safety screen (S1), so no safety-based comparison against triptan contraindications in this subtype can be made yet.

**To proceed, the following is needed:**
- Resolve DG001: obtain Fimea package insert (warnings, contraindications) to enable a formal S1 safety pre-assessment
- Resolve DG002: structured DrugBank MOA extraction to firm up the mechanistic rationale
- A prospective study or registry analysis specifically in migraine-with-brainstem-aura patients (current evidence is aura-general, not subtype-specific)
- Clarification of Finland market/licensing status, since "0 licenses" for a globally marketed OTC drug looks like a data gap rather than fact

**Additional context for portfolio prioritization:** this evidence pack's other TxGNN candidates for aspirin include several with much stronger evidence at lower TxGNN rank — notably *thrombotic disease* (rank 8, evidence level L1, "Proceed with Guardrails") and *thrombophilia* (rank 9, L2, "Proceed with Guardrails"). These reflect aspirin's already well-established antithrombotic role rather than a novel repurposing opportunity, but may be more actionable near-term than the brainstem-aura candidate covered in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

