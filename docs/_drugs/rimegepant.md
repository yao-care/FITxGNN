---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rimegepant is a small-molecule CGRP receptor antagonist (gepant class) originally developed and approved for the acute treatment of migraine (with or without aura) and preventive treatment of episodic migraine.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a migraine subtype where triptans are typically contraindicated,
with **0 dedicated clinical trials** but **14 supporting publications** on rimegepant's general migraine efficacy and vascular safety profile.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (acute treatment with/without aura; preventive treatment of episodic migraine) — not from Finland licensing data, as the drug is not currently marketed there |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (based on robust general rimegepant/migraine evidence base; no trials specific to the brainstem-aura subtype) |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for rimegepant is currently marked as a data gap in this evidence pack. Based on the supporting literature, rimegepant is a highly selective, small-molecule calcitonin gene-related peptide (CGRP) receptor antagonist — CGRP is a central mediator of migraine pathophysiology, and rimegepant blocks its signaling without the vasoconstrictive activity seen in triptans.

Migraine with brainstem aura (formerly "basilar-type migraine") is a migraine subtype in which triptans are typically avoided or contraindicated because their vasoconstrictive mechanism carries theoretical risk in the vertebrobasilar circulation. Since rimegepant's mechanism does not rely on vasoconstriction — a point reinforced by a longitudinal MRA study (PMID 41574090) showing it does not induce cerebral/extracerebral artery constriction during migraine attacks — it is mechanistically plausible that rimegepant could be used safely in this subtype where triptans cannot.

This is therefore best understood as an indication-refinement prediction rather than a novel therapeutic hypothesis: rimegepant is already approved for migraine broadly, and the model is flagging a specific, mechanistically well-supported subgroup (brainstem aura) that would benefit from a non-vasoconstrictive acute treatment option. No trials have yet directly enrolled or reported outcomes specifically in patients with brainstem aura.

## Clinical Trial Evidence

Currently no related clinical trials registered specific to migraine with brainstem aura.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Review/Regulatory (First Approval) | Drugs | Establishes rimegepant's initial FDA approval as a CGRP antagonist for acute migraine treatment, with tablet formulation under investigation for prevention and refractory trigeminal neuralgia |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 open-label long-term safety | Cephalalgia | Long-term safety, tolerability, and effectiveness of rimegepant 75mg ODT for acute migraine treatment in Chinese adults |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | Randomized placebo-controlled trial (Phase 1 PK/safety) | Clin Pharmacol Drug Dev | Confirms pharmacokinetics and safety of single/multiple 75mg rimegepant ODT dosing in healthy Chinese adults |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | J Headache Pain | Indirect comparison of onset of efficacy between lasmiditan, rimegepant, and ubrogepant for acute migraine treatment |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 open-label safety | J Headache Pain | 24-week study of once-daily 75mg rimegepant dosing for episodic migraine prevention shows good long-term tolerability |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Longitudinal MR angiography study | Brain Communications | Directly examines rimegepant's effect on cerebral/extracerebral arteries during migraine attacks, supporting it as a non-vasoconstrictive alternative to triptans — most mechanistically relevant to the brainstem-aura hypothesis |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospective cohort | Headache | Evaluates tolerability and effectiveness of off-label rimegepant use for acute migraine treatment in adolescents |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Comprehensive review of rimegepant in acute and preventive migraine treatment, noting superiority to placebo in Phase 3 trials |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook of Clinical Neurology | Reviews the pharmacology of second-generation gepants (rimegepant, ubrogepant), contrasting with first-generation hepatotoxicity concerns |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Reviews rimegepant's role among new acute migraine treatment options (lasmiditan, rimegepant, ubrogepant) |

## Safety Considerations

Please refer to the package insert for safety information. TFDA/Finland-specific warnings, contraindications, and drug-drug interaction data were not available in this evidence pack.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong — rimegepant's non-vasoconstrictive CGRP antagonism plausibly addresses the specific safety limitation of triptans in brainstem-aura migraine, and this is backed by a broad general evidence base (14 publications, including direct vascular-effect data). However, no trial has enrolled this specific subgroup, and the drug is not yet marketed in Finland, so real-world regulatory and safety data are absent.

**To proceed, the following is needed:**
- TFDA/EMA package insert data on warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Confirmed mechanism-of-action documentation from DrugBank (currently a data gap)
- A dedicated trial or subgroup analysis in patients with migraine with brainstem aura, rather than relying on general migraine trial extrapolation
- Finland/EU market authorization and licensing status for rimegepant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

