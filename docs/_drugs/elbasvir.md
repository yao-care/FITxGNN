---
layout: default
title: Elbasvir
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Elbasvir
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

# Elbasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Elbasvir is an NS5A inhibitor originally developed as part of the elbasvir/grazoprevir combination (Zepatier) for chronic Hepatitis C virus (HCV) infection. TxGNN predicts it may be effective for **Hepatitis B Virus Infection**, with a very high score (99.71%), but on closer review the **13 clinical trials** and **18 publications** cited as "evidence" are almost entirely HCV studies with no genuine HBV efficacy data — this prediction appears to be a knowledge-graph artifact rather than a real pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory licensing data (drug not marketed in Finland). Based on the trial/literature evidence in this pack, elbasvir's established clinical use is chronic Hepatitis C Virus (HCV) genotype 1/4/6 infection, as the elbasvir/grazoprevir fixed-dose combination (Zepatier) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.71% (rank 3637) |
| Evidence Level | L5 (model prediction only — no study in the evidence set actually tests HBV efficacy) |
| Finland Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this pack (data gap). Based on the clinical trial and literature evidence collected for this candidate, elbasvir is an HCV-specific **NS5A protein inhibitor**, used exclusively in combination with grazoprevir (an NS3/4A protease inhibitor) to treat chronic HCV genotype 1, 4, and 6 infection.

HCV and HBV are only superficially related — both cause "viral hepatitis" — but they belong to entirely different viral families with unrelated replication machinery. HCV (Hepacivirus, Flaviviridae) is a positive-sense RNA virus that depends on the NS5A protein for replication complex assembly, which is elbasvir's drug target. HBV (Hepadnaviridae) is a reverse-transcribing DNA virus with no NS5A homolog; its replication depends on polymerase/reverse transcriptase and core capsid proteins that elbasvir has no known activity against.

Consistent with this, essentially all 13 clinical trials and 18 publications retrieved under "hepatitis B virus infection" are actually grazoprevir/elbasvir studies conducted in **HCV**-infected populations (including HCV/HIV co-infection, transplant, and dialysis cohorts) — none test elbasvir against HBV. The high TxGNN score most likely reflects the model picking up on shared "hepatitis" semantics in the knowledge graph rather than a genuine mechanistic or empirical link. This assessment is consistent with the pack's own repurposing rationale and its L5/Hold designation.

---

## Clinical Trial Evidence

*Note: these trials were retrieved under the "hepatitis B virus infection" query but are HCV trials of grazoprevir/elbasvir; none test HBV efficacy directly (see relevance grading below).*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Completed | 413 | Grazoprevir+uprifosbuvir with elbasvir or ruzasvir in chronic HCV GT3/4/5/6 — not an HBV trial (relevance grade C) |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33808 | Adverse-event rates of DAA therapy vs. untreated in HCV patients — not HBV |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV co-infected patients — unrelated to HBV (grade C) |
| [NCT01532973](https://clinicaltrials.gov/study/NCT01532973) | Phase 1 | Completed | 48 | Safety/PK/PD of elbasvir in HCV-infected males — not HBV (grade C) |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Completed | 301 | Grazoprevir/elbasvir efficacy in HCV GT1/4/6 patients on opiate substitution therapy — not HBV (grade C) |
| [NCT03797066](https://clinicaltrials.gov/study/NCT03797066) | Phase 4 | Terminated | 13 | Grazoprevir/elbasvir test-and-treat in homeless population with HCV GT1/4 — not HBV |
| [NCT02332707](https://clinicaltrials.gov/study/NCT02332707) | Phase 2 | Completed | 443 | Grazoprevir+uprifosbuvir with elbasvir or ruzasvir in HCV GT1/2 — not HBV |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | Grazoprevir+elbasvir for acute HCV GT1/4 (Dutch DAHHS-2 study) — not HBV |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Completed | 573 | Grazoprevir+elbasvir ± ribavirin in chronic HCV — not HBV |
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Phase 2 | Completed | 15 | Pembrolizumab in HCV+/− advanced HCC patients; elbasvir not the study intervention — not HBV (grade C) |

3 additional trials in the evidence pack (NCT01932762, NCT03110055, NCT02115321) were also reviewed and are likewise HCV-only studies.

---

## Literature Evidence

*All 18 retrieved publications concern elbasvir/grazoprevir in HCV populations; none provide direct evidence of anti-HBV activity.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Cohort | Antimicrob Agents Chemother | Grazoprevir/elbasvir efficacy in HCV GT1b liver/kidney transplant recipients — HCV only |
| [30049677](https://pubmed.ncbi.nlm.nih.gov/30049677/) | 2018 | Case report | BMJ Case Rep | HCV-associated dermatomyositis case — unrelated to HBV or elbasvir efficacy |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm Sin B | Overview of direct-acting anti-HCV agents; explicitly distinguishes HCV from HBV/HIV, no HBV data on elbasvir |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Review | Klin Mikrobiol Infekc Lek | General pediatric review of chronic HBV/HCV antiviral treatment in Ostrava; not elbasvir-specific HBV evidence |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Review | Liver Int | Title references both HCV eradication and an HBV cure but abstract unavailable; no elbasvir-HBV data confirmed |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Review | Ann Hepatol | Global HBV/HCV drug pricing comparison — economic analysis, not efficacy data |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Real-world study | J Viral Hepat | Real-world liver/renal safety of elbasvir/grazoprevir in Taiwan HCV GT1 patients — HCV only |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | PK/PD update on HCV DAA regimens including elbasvir/grazoprevir — HCV only |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | N/A | Hepatology | HCV protease-inhibitor resistance evolution — unrelated to elbasvir's NS5A target or HBV |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Review | Cancers | HCC risk in chronic kidney disease, discussed in HCV context — no elbasvir/HBV data |

Remaining publications (PMID 35260039, 29077864, 28992878, 31521479, 32925725, 33208686, 36535062, 32306039) follow the same pattern — grazoprevir/elbasvir real-world or transplant studies in HCV populations.

---

## Finland Market Information

Elbasvir currently holds **no marketing authorization in Finland** (0 licenses on record; market status: 未上市/Not marketed). No product/authorization data is available for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available for this drug (TFDA package insert retrieval flagged as a **Blocking** data gap, DG001), and DDI query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Elbasvir's known target (HCV NS5A) has no plausible mechanistic link to HBV, which belongs to an unrelated virus family with different replication machinery. The 13 trials and 18 publications nominally tied to this prediction are, on inspection, all HCV studies — none test HBV efficacy — so the L5 "model prediction only" evidence level is appropriate, and the TxGNN score should be treated as a likely knowledge-graph artifact rather than a real signal.
- The other nine indications ranked below this one in the same evidence pack (hepatitis E, hepatitis A, animal viral hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, HIV, feline AIDS, SIV, and an unrelated neurodevelopmental disorder) were all also scored L5/Hold for the same reason — apparent semantic clustering around "hepatitis"/"viral infection" rather than genuine pharmacology.
- Elbasvir is not marketed in Finland, and core safety data (TFDA warnings/contraindications, MOA) are blocked or missing (DG001, DG002), so this candidate cannot yet enter a safety pre-assessment (S1) regardless of indication.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank (DG002)
- TFDA/EMA package insert warnings and contraindications (DG001 — currently blocking)
- Genuine preclinical or in vitro evidence of elbasvir activity against HBV polymerase/core proteins, if this indication is to be pursued further
- Given the weak mechanistic basis, consider deprioritizing this candidate in favor of TxGNN predictions with stronger target-disease alignment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

