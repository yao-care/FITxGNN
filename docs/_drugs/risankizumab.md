---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Psoriasis to Dermatitis

## One-Sentence Summary

Risankizumab is a humanised IgG monoclonal antibody targeting the p19 subunit of IL-23, first approved in Japan (2019) for psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis and erythrodermic psoriasis. The TxGNN model predicts it may be effective for **Dermatitis** (including atopic dermatitis), with **7 clinical trials** and **17 publications** currently supporting this direction. Evidence includes a completed placebo-controlled Phase 2 RCT specifically in moderate-to-severe atopic dermatitis, though the drug is not currently marketed in Finland and key safety labeling data is missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis (psoriasis vulgaris, psoriatic arthritis, generalized pustular/erythrodermic psoriasis — per first global approval; no Finland license record available) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original MOA data for risankizumab is flagged as a data gap in this evidence pack. However, the pack's own literature and repurposing rationale supply the mechanistic picture: risankizumab is an anti-IL-23 (p19 subunit) monoclonal antibody that blocks the IL-23/Th17 signaling axis (PMID 31098898). This pathway is a well-established driver of keratinocyte hyperproliferation and inflammation in psoriasis, its original indication.

The IL-23/Th17 axis also contributes to other chronic inflammatory skin diseases, including atopic dermatitis, where Th2, Th22 and — increasingly recognized — Th17 pathways overlap. This shared immunopathogenesis is the biological basis for the TxGNN prediction linking risankizumab to dermatitis.

Consistent with this rationale, a dedicated Phase 2 placebo-controlled RCT (NCT03706040) directly tested risankizumab in adult and adolescent patients with moderate-to-severe atopic dermatitis, and a real-world cohort has reported combined dupilumab + risankizumab use in patients with concomitant atopic dermatitis and psoriasis. Notably, the literature also documents a recognized paradoxical adverse effect — eczematous/dermatitis-like eruptions emerging *during* risankizumab treatment for psoriasis (e.g., PMID 33185530, 36939506, 41645692) — which is a double-edged signal: it confirms cutaneous immunologic activity relevant to dermatitis pathways, but also flags a safety consideration that should be weighed alongside efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomized, placebo-controlled, double-blind study of risankizumab in adult and adolescent subjects with moderate to severe atopic dermatitis — the most directly relevant trial for this indication |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Open-label comparison of risankizumab vs. apremilast in moderate plaque psoriasis; supports mature clinical use in inflammatory skin disease |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Double-blind study of risankizumab in moderate-to-severe genital or scalp psoriasis |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A (observational) | Completed | 240 | Taiwan prospective cohort on durability of risankizumab response (PASI 90) vs. other biologics in moderate-to-severe plaque psoriasis |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A (observational) | Recruiting | 840 | Real-world biomarker profiling study covering atopic dermatitis, psoriasis and other immune-mediated inflammatory skin diseases |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A (observational) | Completed | 1000 | Pharmacogenetic study on 10-year survival of biologic therapies in cutaneous psoriasis ± psoriatic arthritis |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice-based topical drug testing platform for atopic dermatitis and psoriasis; low direct relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2 randomized, double-blind, placebo-controlled trial of risankizumab in moderate-to-severe atopic dermatitis, supporting IL-23/IL-22 blockade rationale in AD |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "First Global Approval" review: risankizumab's MOA (anti-IL-23 p19) and initial approval history in psoriasis-spectrum disease |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/small molecules for pediatric alopecia areata, psoriasis, atopic dermatitis and hidradenitis suppurativa |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opinion on Biological Therapy | Review of current and emerging biologics for pediatric atopic dermatitis |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Review | American Journal of Clinical Dermatology | Systematic review of systemic therapies (including risankizumab) for erythrodermic psoriasis |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Review | Inflammopharmacology | Systematic review of interleukin inhibitors (incl. IL-23) in lichen planus, therapeutic and paradoxical cutaneous effects |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Cohort | International Journal of Dermatology | Effectiveness and safety of combined dupilumab and risankizumab in patients with concomitant atopic dermatitis and psoriasis |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Cohort | Experimental Dermatology | Retrospective longitudinal study of risankizumab treatment response in patients with a history of erythrodermic psoriasis |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Reappraisal of systemic immunomodulators, including risankizumab, for psoriasis and eczema in military populations |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case Report | Journal of Dermatological Treatment | Case of acrodermatitis continua of Hallopeau successfully and rapidly treated with risankizumab |

---

## Finland Market Information

No marketing authorizations for risankizumab are currently recorded in Finland (market status: Not Marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Retrieval of the TFDA/EMA package insert (warnings, contraindications) is flagged as a Blocking data gap in this evidence pack, meaning a formal S1 safety pre-assessment cannot currently be completed. Separately, the literature evidence base surfaces a recurring paradoxical adverse-event signal — eczematous/dermatitis-like eruptions during risankizumab treatment (PMID 33185530, 36939506, 33185535, 41645692, 37014149) — that should be factored into any future safety review for a dermatitis indication specifically.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (IL-23/Th17 blockade) and a completed Phase 2 RCT in atopic dermatitis (L2 evidence) provide a genuine efficacy signal, but a Blocking data gap on official safety labeling and the drug's absence from the Finnish market (0 authorizations) mean the safety pre-assessment (S1) cannot be completed at this time.

**To proceed, the following is needed:**
- TFDA/EMA-equivalent package insert (warnings and contraindications) to complete S1 safety pre-assessment
- Confirmed original indication and full MOA documentation from DrugBank
- DDI dataset (current query returned no results)
- Targeted review of the paradoxical eczematous-reaction literature to assess risk when repurposing toward a primary dermatitis indication
- Regulatory pathway assessment for Finland market entry given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

