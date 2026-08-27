---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Delamanid: From Multidrug-Resistant Tuberculosis to Bovine Tuberculosis (Zoonotic TB)

## One-Sentence Summary

> Delamanid is a nitroimidazole antimycobacterial used in multidrug-resistant tuberculosis (MDR-TB) regimens; detailed original-indication text is not present in this evidence pack, as the drug is currently **not marketed in Finland** (0 licenses on record).
> The TxGNN model predicts activity against **Bovine Tuberculosis** (caused by *Mycobacterium bovis*), though direct evidence for this specific indication is currently minimal — **0 clinical trials** and **1 tangentially related publication**.
> Note: a closely related TB indication ranked immediately below it, "inactive tuberculosis," is supported by **2 clinical trials** (including two Phase 2/3 studies) and **20 publications**, and is likely the more actionable candidate within this prediction cluster.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (unmarketed in Finland; no license records available) |
| Predicted New Indication | Bovine Tuberculosis (zoonotic, *M. bovis*) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Delamanid is a nitro-dihydro-imidazooxazole derivative used within combination regimens for multidrug-resistant pulmonary tuberculosis; its efficacy against tuberculosis caused by *Mycobacterium tuberculosis* has been clinically established.

Bovine tuberculosis is caused by *Mycobacterium bovis*, a member of the *Mycobacterium tuberculosis* complex (MTBC) that is closely related to *M. tuberculosis* and can cause zoonotic human infection. Because Delamanid's antimycobacterial activity targets pathways shared across MTBC species (e.g., disruption of mycolic acid biosynthesis in nitroimidazole-class agents), mechanistic extrapolation to *M. bovis* infection is biologically plausible.

It is worth noting that all seven of the model's top predicted indications for this drug are tuberculosis-related (bovine TB, inactive TB, avian TB, tuberculoma, tuberculous ascites, cutaneous TB), which is consistent with Delamanid's established pharmacology and lends indirect support to the plausibility of the bovine TB prediction — even though direct evidence for that specific sub-indication remains sparse.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Molecular epidemiology | BMC Genomics | Whole-genome sequencing study characterizing genetic diversity and drug-resistance mechanisms in *M. bovis* isolates causing zoonotic human tuberculosis in Egypt; does not directly evaluate Delamanid treatment outcomes |

---

## Finland Market Information

Currently not marketed in Finland; no approved product licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The specific predicted indication — bovine tuberculosis — has no direct clinical or preclinical evidence supporting Delamanid's use, and the drug currently has no Finland market authorization to build on. Critical safety inputs (TFDA package insert warnings/contraindications, DG001) and mechanism-of-action detail (DG002) are also flagged as data gaps, blocking a full safety assessment.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Direct preclinical or clinical evidence of Delamanid activity specifically against *M. bovis* infection
- Consider evaluating **"inactive tuberculosis"** (rank 2) as an alternative/parallel candidate, given its stronger existing evidence base (CRUSH-TB [NCT05766267] and PHOENIx MDR-TB [NCT03568383] trials, plus 20 supporting publications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

