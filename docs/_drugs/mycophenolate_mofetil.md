---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Organ Transplant Rejection Prophylaxis to HIV Infectious Disease

## One-Sentence Summary

Mycophenolate mofetil (MMF) is a purine-synthesis-inhibiting immunosuppressant historically used to prevent rejection after solid organ transplantation. The TxGNN model predicts it may be effective for **HIV infectious disease**, with **10 clinical trials** and **20 publications** currently retrieved in support of this direction — though the strongest human data date from small, mostly investigator-initiated studies conducted in the early-to-mid 2000s.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of organ transplant rejection (renal, cardiac, hepatic) — based on general pharmacological knowledge; no Finland-specific approved indication text is available (see below) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for this candidate were not returned from DrugBank (flagged as a High-severity data gap, DG002). However, the repurposing evidence pack supplies a specific mechanistic rationale: MMF inhibits inosine monophosphate dehydrogenase (IMPDH), depleting the guanine nucleotide pool and blocking proliferation of lymphocytes — including activated CD4+ T cells, the primary target/reservoir cells for HIV replication.

This is not a purely speculative mechanistic leap. Because activated, proliferating CD4+ T cells are both the preferred substrate for HIV infection and the cell population MMF most potently suppresses, researchers proposed in the late 1990s and 2000s that MMF could shrink the pool of cells available for viral replication and slow CD4+ T-cell depletion in chronic HIV-1 infection. MMF was also studied as an adjunct to nucleoside reverse transcriptase inhibitors (particularly abacavir and didanosine), where mycophenolic acid was shown to deplete intracellular deoxyguanosine triphosphate (dGTP) and potentiate antiretroviral activity in vitro and in small clinical cohorts.

Taken together, the prediction reflects a genuine, previously-tested immunomodulatory hypothesis rather than a novel mechanistic guess — but the human evidence base remains limited to small, mostly Phase 1/2 pilot and cohort studies, several of which were terminated or withdrawn before completion.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study — evaluates whether MMF can dampen chronic immune hyperactivation and slow CD4+ T-cell decline in ART-naive chronic HIV-1 patients, and its effect on HIV-1 RNA and disease progression |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy assessing effects of MMF on cardiovascular surrogate markers in HIV-1 infected patients |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | Withdrawn | 0 | Planned safety/tolerability and antiretroviral-activity study of MMF added to abacavir in heavily treatment-experienced HIV patients; withdrawn before enrollment, no data generated |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal transplantation in HIV-infected patients with end-stage renal disease, examining safety of MMF-based immunosuppression in this population |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor bone marrow transplant (HIV-cure-directed research context) using MMF as standard GVHD prophylaxis, not as the primary study drug |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT to induce mixed hematopoietic chimerism in HIV-1-infected patients, with post-transplant immunosuppression using cyclosporine and MMF |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Multicenter follow-up of renal transplantation in HIV-1 infected patients with end-stage renal insufficiency, evaluating acute graft rejection incidence |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Pilot RCT of amdoxovir (DAPD) with or without MMF in treatment-experienced HIV patients; primary study drug is DAPD, MMF is an add-on arm |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | MMF plus cyclosporine vs. cyclophosphamide plus prednisolone for anti-EPO-associated pure red cell aplasia — not an HIV indication |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Thiotepa/busulfan/fludarabine conditioning for haploidentical HSCT in elderly AML patients — unrelated to MMF/HIV, likely a keyword co-occurrence mismatch |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | 17 chronic HIV-1 patients randomized to MMF vs. continued HAART after treatment interruption; assessed immune response and plasma/lymphatic tissue viral load |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Controlled trial | AIDS | HAART with or without MMF in treatment-naive HIV-1 patients; studied effect on plasma HIV-1 RNA decay rate and the latent reservoir |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort (Tier 1) | AIDS Res Hum Retroviruses | No detrimental immunological effects observed when combining MMF with HAART in treatment-naive acute/chronic HIV-1 patients |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort (Tier 1) | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing ART was associated with intracellular dGTP depletion and decreased plasma HIV-1 RNA in 5 heavily pretreated patients |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Cohort | J Clin Invest | Antiproliferative drugs combined with cognate peptide stimulation selectively reduced clonally expanded HIV-infected CD4+ T cells |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK study | Clin Pharmacokinet | Pharmacokinetics/pharmacodynamics of low-dose MMF in HIV patients on abacavir, efavirenz, and nelfinavir |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK study | Clin Pharmacokinet | Effect of MMF on pharmacokinetics of antiretrovirals and on intracellular nucleoside triphosphate pools |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | Open-label pilot of MMF added to a multidrug-resistant HIV-1 regimen (abacavir, ddI, amprenavir, ritonavir ± efavirenz) in 7 heavily treated AIDS patients |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review (Tier 2) | Curr Top Med Chem | Reviews immunosuppressive drugs, including MMF, as adjuncts to HAART targeting chronic immune activation in HIV disease |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical study | AIDS | Safety, tolerability and antiretroviral activity of amdoxovir (DAPD) with or without MMF in drug-resistant HIV-1 infection |

---

## Finland Market Information

Mycophenolate mofetil is currently **not marketed in Finland** — no marketing authorizations are on record (0 licenses found). No product/dosage-form/indication data are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, and drug–drug interaction records) could not be retrieved for this candidate; the TFDA-equivalent package insert warnings/contraindications are recorded as a **Blocking** data gap (DG001) that must be resolved before any S1 safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IMPDH-inhibition mechanism gives a biologically coherent rationale for suppressing HIV target-cell proliferation, and this hypothesis was actually tested clinically in the 2000s (small cohorts, pilot RCTs, and one PK series) with encouraging but not definitive results — no confirmatory Phase 3 efficacy trial exists, several relevant studies were withdrawn or terminated, and the MAN2 study's outcome status remains "Unknown." Combined with the complete absence of validated safety/DDI data and the drug's non-marketed status in Finland, the evidence does not yet support proceeding to development or clinical guardrail design.

**To proceed, the following is needed:**
- Official package insert / TFDA-equivalent warnings and contraindications (resolves Blocking gap DG001)
- Confirmed mechanism-of-action documentation from DrugBank (resolves High-severity gap DG002)
- A completed drug–drug interaction database query (currently "not_found")
- Verification of final outcomes/publication status for the MAN2 study (NCT00120419/NCT00247494)
- Assessment of the regulatory pathway required for Finland market entry if this indication is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

