---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 2
---

# Fremanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

> Fremanezumab is a fully humanized anti-CGRP monoclonal antibody established as a preventive treatment for episodic and chronic migraine.
> The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a rare migraine subtype in which triptans are contraindicated due to vasoconstrictive risk.
> This direction is currently supported only by **mechanistic and case-level literature (0 dedicated clinical trials, 20 related publications)** — no trials have specifically enrolled this subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic/chronic migraine) — per literature evidence; not formally confirmed by a Finnish label |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (mechanistic/preclinical + case-level evidence, no dedicated trials) |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is not available in this evidence pack [Data Gap: DG002]. Based on the repurposing rationale and supporting literature, fremanezumab is a humanized anti-CGRP monoclonal antibody that peripherally blocks calcitonin gene-related peptide (CGRP) signaling, inhibiting activation of the trigeminovascular system — the core mechanism underlying its established use as a migraine-preventive agent (e.g., PMID 30725283, "Role of CGRP in Migraine").

Migraine with brainstem aura is a subtype of migraine with aura that is routinely excluded from standard migraine trials, historically because triptans carry vasoconstrictive contraindications in this population. Because CGRP monoclonal antibodies act through peripheral CGRP blockade rather than direct vasoconstriction, they are mechanistically plausible for this subtype without the safety concerns that limit triptan use — a rationale echoed in case-based literature on hemiplegic migraine and migraine with aura more broadly (PMID 35268319, PMID 40264646, PMID 41618146).

However, mechanistic plausibility should be distinguished from direct efficacy evidence. Preclinical work using the cortical spreading depression (CSD) model — the accepted physiological correlate of migraine aura — found that fremanezumab did **not** prevent CSD occurrence and had no effect on CSD-induced arterial dilatation/plasma protein extravasation (PMID 31127003, PMID 31895266), though it did slow CSD propagation and shorten cortical recovery in one model. This mixed preclinical signal means the case for efficacy specifically in brainstem aura remains a research question rather than an established mechanistic transfer.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports/Review | J Clin Med | Reviews scarce evidence on anti-CGRP mAbs (incl. fremanezumab) for preventing migraine aura specifically, despite well-documented efficacy on headache pain |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | General review of CGRP's role in migraine pathophysiology, including the aura subgroup |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report/Review | Frontiers in Neurology | Case of hemiplegic migraine (aura subtype) treated with anti-CGRP mAb; notes these patients are systematically excluded from RCTs |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual Patient Analysis | J Headache Pain | Quantitative analysis of anti-CGRP mAb effectiveness/safety in hemiplegic migraine, a rare aura subtype excluded from RCTs |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational Case Series | CNS Neurosci Ther | Observational case series on anti-CGRP-targeted therapy's effect on migraine aura specifically |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Cohort (post hoc, Phase 3b FOCUS) | Eur J Neurol | Fremanezumab efficacy/QoL analyzed in subgroups with and without aura or neurological dysfunction |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Basic/Mechanistic (CSD model) | J Neurosci | Fremanezumab did not affect CSD-induced arterial dilatation or plasma protein extravasation in an animal aura model |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Basic/Mechanistic (CSD model) | Pain | Fremanezumab slowed CSD propagation and shortened cortical recovery but did not prevent CSD occurrence in rats |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Real-world Cohort | Frontiers in Neurology | 3-month real-world efficacy/tolerability of fremanezumab in chronic migraine (not aura-specific) |
| [35775208](https://pubmed.ncbi.nlm.nih.gov/35775208/) | 2022 | Cohort | Cephalalgia | Effects of anti-CGRP mAbs (incl. fremanezumab) on central/neurological symptoms of migraine |

---

## Finland Market Information

Fremanezumab is not currently marketed in Finland (0 authorizations on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. [DG001: TFDA/label warnings and contraindications are a blocking data gap; DDI query returned no results.]

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The mechanistic case — peripheral CGRP blockade avoiding the vasoconstrictive risk that excludes triptans in this subtype — is reasonable, but no clinical trials have enrolled patients with migraine with brainstem aura specifically, and the only directly relevant preclinical (CSD) data show fremanezumab does not prevent the aura-correlate phenomenon itself. Evidence level is L4, consistent with a research hypothesis rather than a decision-ready signal.

**To proceed, the following is needed:**
- TFDA/EU label warnings and contraindications (currently blocking — DG001)
- DrugBank-sourced mechanism of action detail (currently missing — DG002)
- A dedicated observational study or case series in migraine-with-brainstem-aura patients (current evidence is either general-migraine or hemiplegic-migraine, a related but distinct aura subtype)
- Clarification of why preclinical CSD data show no effect on aura-correlate physiology despite clinical case reports suggesting benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

