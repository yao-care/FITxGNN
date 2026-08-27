---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Phenylephrine: From Decongestant/Vasoconstrictor Use to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is an α1-adrenergic receptor agonist already used pharmacologically as a nasal and ocular decongestant/vasoconstrictor, though no formal original-indication or Finland market-authorization record is present in this evidence pack.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **8 clinical trials** and **8 publications** currently identified — but most of this evidence concerns phenylephrine-containing combination products (e.g., co-phenylcaine, Polydexa) or comparator decongestants (oxymetazoline, xylometazoline, cocaine) rather than phenylephrine monotherapy tested directly against this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — phenylephrine holds no license record in this dataset (0 Finland authorizations); pharmacologically known as a nasal/ocular decongestant and vasoconstrictor |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% (rank 534) |
| Evidence Level | L3 |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not supplied for this drug (flagged as a High-severity data gap, DG002). However, the evidence pack's own rationale confirms phenylephrine is an α1-adrenergic receptor agonist whose classic pharmacology is nasal mucosal vasoconstriction and decongestion — this is an established mechanism, not a novel repurposing hypothesis.

Because this mechanism is already the textbook basis for nasal decongestant use, the TxGNN prediction of "Nasal Cavity Disease" largely reconfirms known pharmacology rather than surfacing an unexpected new indication. Supporting evidence mostly comes from phenylephrine-containing combination products used peri-procedurally (co-phenylcaine, Polydexa with phenylephrine) or from trials comparing alternative decongestants (oxymetazoline, xylometazoline, epinephrine, cocaine) for nasal mucosal shrinkage before endoscopy or sinus surgery — supporting the mechanistic class effect, though direct phenylephrine-monotherapy RCTs against a defined nasal cavity disease endpoint are limited.

Given the absence of both a documented original indication and TFDA/national package-insert safety data (DG001, Blocking severity), the mechanistic plausibility should be treated as reinforcing rather than establishing a new therapeutic claim.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Completed | 106 | Co-phenylcaine (phenylephrine + lidocaine) nasal spray vs. nasal nebulization for decongestion/local anesthesia before rigid nasoendoscopy |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Compared 0.05% oxymetazoline vs. 1:1000 epinephrine (not phenylephrine) for blood loss/visualization before endoscopic sinus surgery |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | NA | Unknown | 120 | Endonasal-endoscopic vs. external dacryocystorhinostomy for nasolacrimal duct obstruction; no phenylephrine arm specified |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind crossover RCT of an H3-antagonist on nasal congestion after allergen challenge in seasonal allergic rhinitis |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | IV esmolol vs. lidocaine for postoperative recovery quality after functional endoscopic sinus surgery |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Kovanaze (tetracaine + oxymetazoline) nasal mist vs. articaine for maxillary pulpal anesthesia; withdrawn, no enrollment |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Cocaine vs. lidocaine/xylometazoline vs. saline for intranasal analgesia before awake nasotracheal intubation; no phenylephrine arm |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Same Kovanaze vs. articaine design as NCT04104789; terminated early, minimal enrollment |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | International Journal of Clinical Practice | Double-blind RCT: cophenylcaine spray vs. placebo before flexible nasendoscopy — no significant difference in pain/discomfort |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT (indirect comparator) | PLoS ONE | Triple-blind RCT of topical tranexamic acid on bleeding/surgical field quality during FESS |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental + Clinical | Vestnik Otorinolaringologii | Safety/efficacy evaluation of Polydexa spray with phenylephrine in acute rhinosinusitis |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik Otorinolaringologii | Differential diagnosis of chronic nasal disease after surgery and topical antibiotic therapy, including Polydexa with phenylephrine |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik Otorinolaringologii | Pathogenetic approach to treating inflammatory diseases of the nose and paranasal sinuses |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | International Journal of Pediatric Otorhinolaryngology | Acoustic rhinometry of nasal cavity/nasopharynx geometry after adenotonsillectomy |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case Report | Archives of Ophthalmology | Cocaine toxicity during dacryocystorhinostomy; one patient also reacted to intranasal phenylephrine |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In Vitro | Clinical Otolaryngology and Allied Sciences | Preliminary in vitro study of drug effects on nasal ciliary beat frequency |

## Finland Market Information

Phenylephrine currently has no marketing authorization on record in Finland (market status: 未上市 / Not marketed; 0 authorizations). No product-level license data is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is consistent with phenylephrine's established α1-agonist decongestant pharmacology and is corroborated by several trials/publications, but nearly all of this evidence involves combination products or comparator decongestants rather than phenylephrine monotherapy tested directly for a defined nasal cavity disease endpoint — evidence level L3. Combined with the Blocking-severity absence of package-insert warnings/contraindications, a cautious, guardrailed path is warranted rather than a full Go.

**To proceed, the following is needed:**
- TFDA/national package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed drug mechanism-of-action documentation from DrugBank (DG002)
- A direct phenylephrine-monotherapy trial or systematic review against a defined nasal cavity disease endpoint (current evidence is mostly indirect/comparator-based)
- Confirmation of Finland marketing-authorization status, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

