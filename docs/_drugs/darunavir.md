---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is a HIV-1 protease inhibitor, best known as part of antiretroviral combination therapy for human HIV-1 infection.
The TxGNN model's top prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a lentiviral disease of non-human primates, not a human condition — supported only by **4 preclinical/animal-study publications**, none of which specifically test darunavir. No clinical trials, no Fimea market presence, and no safety documentation are currently available, so this candidate is not actionable without substantial additional data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from mechanistic rationale within this evidence pack; official indication text and MOA are marked as data gaps — see Rationale below) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical/animal studies only) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (marked as a data gap, DG002). However, the evidence pack's own repurposing rationale identifies darunavir as a **HIV-1 protease inhibitor**, acting on the retroviral Gag-Pol polyprotein cleavage step required for viral maturation.

SIV and HIV are both members of the *Lentivirus* genus and share substantial structural homology in their protease enzymes. This gives the prediction a plausible mechanistic basis in principle: a HIV-1 protease inhibitor could theoretically retain activity against SIV protease in non-human primate models.

That said, the mechanistic link is indirect. None of the four literature records specifically studied darunavir — two describe multi-drug cART regimens (emtricitabine, tenofovir, etc.) in SIV-infected macaques, and the other two describe entirely different agents (the HDAC inhibitor SAHA and the gold compound auranofin) tested in the same animal model for viral reservoir research. These are tangential, model-system references rather than direct darunavir efficacy data. Furthermore, SIV infection is a veterinary/research-animal disease, not a human indication, which limits the direct clinical translatability of this candidate for human drug repurposing purposes.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study | AIDS Research and Human Retroviruses | Evaluated two novel injectable cART regimens (not darunavir-specific) for suppressing SIV replication in SIVmac239-infected rhesus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Study | PLoS One | Combined suppressive cART with the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques to probe viral reservoirs |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Study | PLoS Pathogens | A highly intensified multi-drug ART regimen achieved long-term viral suppression and reservoir restriction in SIVmac251-infected macaques |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Study | AIDS (London, England) | Gold compound auranofin (non-darunavir agent) restricted the viral reservoir in the monkey AIDS model |

Note: none of the above studies test darunavir directly; all are SIV/macaque model studies of other agents or combination regimens.

## Other TxGNN-Predicted Indications (Not Prioritized)

This evidence pack contains three additional candidates beyond the top-ranked prediction, worth noting for completeness:

| Rank | Disease | Score | Evidence Level | Decision | Key Note |
|------|---------|-------|----------------|----------|----------|
| 2 | Feline acquired immunodeficiency syndrome (FIV) | 99.97% | L2 | Research Question | One completed Phase 4 veterinary RCT ([NCT02770508](https://clinicaltrials.gov/study/NCT02770508), n=145) directly tested boosted darunavir + lamivudine in cats — but the subjects are non-human, limiting relevance to human repurposing |
| 3 | Rare neurodevelopmental disorder (ataxic gait, absent speech, decreased white matter) | 99.97% | L5 | Hold | No mechanistic or clinical link identified; prediction-only |
| 4 | Familial combined hyperlipidemia (obsolete term) | 99.19% | L5 | Hold | Mechanistically contradictory — HIV protease inhibitors are known to *cause* dyslipidemia as an adverse effect, not treat it |

## Finland Market Information

Darunavir is currently **not marketed** in Finland (0 authorizations on record), so no product/license table is available.

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/Fimea package insert warnings and contraindications are marked as a **Blocking** data gap in this evidence pack — see Conclusion below.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication is a non-human veterinary disease (SIV), supported only by preclinical animal-model literature that does not directly test darunavir, with zero clinical trials and no market presence in Finland. Combined with a Blocking-severity gap in safety/label data, there is insufficient evidence to proceed to formal safety review (S1).

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Darunavir-specific (not combination-regimen) preclinical data in the SIV model
- Clarification of translational relevance, since the top two predictions (SIV, FIV) are veterinary rather than human indications
- If pursuing the FIV signal instead (rank 2, L2, Research Question), veterinary-to-human translational justification would be required given its stronger trial evidence (NCT02770508)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

