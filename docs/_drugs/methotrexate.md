---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Antifolate Chemotherapy to Rhabdomyosarcoma

## One-Sentence Summary

> Methotrexate is a well-established antifolate (dihydrofolate reductase inhibitor) agent; this evidence pack's TFDA/Finland regulatory data on its original approved indication is currently a documented gap.
> The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**, and — unlike most of the other candidates in this evidence pack — this direction is supported by **4 registered clinical trials** and **20 publications**, including a directly matching published Phase II pediatric trial.
> Among the 10 TxGNN-ranked candidates for this drug, Rhabdomyosarcoma is the highest evidence-tier indication (L2), which is why it was selected as the focus of this report rather than the top-ranked but evidence-free candidates (pulmonary blastoma, well-differentiated fetal lung adenocarcinoma).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (methotrexate is not currently marketed in Finland; approved-indication license text unavailable) |
| Predicted New Indication | Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a Blocking data gap). Based on known pharmacology, methotrexate is a dihydrofolate reductase (DHFR) inhibitor — an antifolate that blocks purine and thymidylate synthesis and is directly cytotoxic to rapidly dividing cells. This mechanism underlies its long-standing use across multiple pediatric and adult malignancies as part of combination chemotherapy regimens.

Rhabdomyosarcoma is a rapidly proliferating pediatric soft-tissue sarcoma, and antifolate-class cytotoxicity has direct, published clinical precedent in this disease: a Phase II trial specifically tested high-dose methotrexate monotherapy in previously untreated children with high-risk unresectable or metastatic rhabdomyosarcoma (PMID 9329466), and methotrexate has also been studied in combination regimens (e.g., with doxorubicin, and within the BOMP-EPI platinum-based regimen) for sarcomas broadly.

One important caveat: among the four registered trials returned for this indication, only one (NCT00357084) was auto-graded "highly relevant," but its actual content concerns methotrexate + glucocorticoids for **graft-versus-host disease prophylaxis**, not rhabdomyosarcoma treatment — this appears to be a relevance-grading mismatch in the source data and should not be counted as direct trial support. The genuine clinical basis for this indication therefore rests primarily on the published literature rather than the ClinicalTrials.gov registry.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357084](https://clinicaltrials.gov/study/NCT00357084) | Phase 2 | Completed | 53 | Evaluates methotrexate + glucocorticoids for newly diagnosed **acute graft-versus-host disease** after nonmyeloablative transplant — despite being flagged as highly relevant, the trial content addresses GVHD, not rhabdomyosarcoma; treat as indirect/mismatched evidence |
| [NCT00112645](https://clinicaltrials.gov/study/NCT00112645) | Phase 1 | Completed | 10 | Toxicity study of allogeneic stem cell transplant (busulfan/melphalan conditioning, methotrexate-containing GVHD prophylaxis) in relapsed/refractory pediatric solid tumors; not RMS-specific |
| [NCT00003273](https://clinicaltrials.gov/study/NCT00003273) | Phase 2 | Withdrawn | 0 | Dose-intensive induction chemotherapy plus stem cell rescue for pediatric malignant brain tumors; withdrawn, not RMS-specific |
| [NCT00253552](https://clinicaltrials.gov/study/NCT00253552) | N/A | Terminated | 4 | Filgrastim-primed bone marrow allogeneic transplant pilot for hematologic malignancies/non-malignancies; unrelated to RMS treatment |

*Note: None of the registered trials directly test methotrexate as treatment for rhabdomyosarcoma; the strongest supporting evidence for this indication comes from the published literature below.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9329466](https://pubmed.ncbi.nlm.nih.gov/9329466/) | 1997 | Phase 2 trial | Journal of Pediatric Hematology/Oncology | Phase II trial of high-dose methotrexate in previously untreated children/adolescents with high-risk unresectable or metastatic rhabdomyosarcoma; direct efficacy/safety evaluation of MTX in this exact indication |
| [36614297](https://pubmed.ncbi.nlm.nih.gov/36614297/) | 2023 | Retrospective cohort | International Journal of Molecular Sciences | BOMP-EPI regimen (bleomycin, vincristine, **methotrexate**, cisplatin alternating with etoposide/cisplatin/ifosfamide) active in adult relapsed/metastatic rhabdomyosarcoma; activity linked to HMGB1 expression |
| [3475644](https://pubmed.ncbi.nlm.nih.gov/3475644/) | 1987 | Cohort | Oncology | Weekly doxorubicin + methotrexate in 55 sarcoma patients (including RMS); objective responses in 11/39 patients at higher dose levels |
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review/Cohort | Cancer | Review of adjuvant chemotherapy (including methotrexate-containing regimens) in childhood sarcomas, ~50% of which are rhabdomyosarcoma |
| [19223736](https://pubmed.ncbi.nlm.nih.gov/19223736/) | 2009 | Review | Gan To Kagaku Ryoho | Chemotherapy indications by histological subtype of musculoskeletal sarcoma; confirms rhabdomyosarcoma is chemosensitive and benefits from adjuvant chemotherapy |
| [9039735](https://pubmed.ncbi.nlm.nih.gov/9039735/) | 1996 | Review | British Medical Bulletin | Overview of management controversies in childhood sarcomas, including chemotherapy approaches for rhabdomyosarcoma |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antifolate / DHFR-inhibitor class) |
| Myelosuppression Risk | High — antifolate mechanism directly suppresses marrow precursor proliferation; risk is dose-dependent and pronounced with high-dose regimens such as those studied in RMS (e.g., PMID 9329466) |
| Emetogenicity Classification | Low to Moderate — dose-dependent; high-dose IV regimens carry materially higher emetogenic risk than low-dose weekly regimens |
| Monitoring Items | CBC with differential, renal function (creatinine clearance, critical for MTX clearance), hepatic function, MTX serum levels with leucovorin rescue for high-dose protocols, mucositis assessment |
| Handling Protection | Yes — methotrexate must be prepared and administered under standard cytotoxic/hazardous drug handling protocols |

*No TFDA-specific toxicity or package-insert data is available for this drug in this evidence pack (Blocking data gap); the above reflects the established pharmacological profile of the antifolate class and should be confirmed against the package insert once available.*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A published Phase II trial directly evaluated high-dose methotrexate in high-risk pediatric rhabdomyosarcoma, supported by additional cohort-level combination-regimen data — meeting the L2 evidence bar (1 completed Phase 2 study). However, this evidence is decades old, current-era registered trials specific to this indication are lacking, and one purportedly high-relevance registered trial (NCT00357084) was found to be mismatched (GVHD, not RMS) on inspection — evidence should therefore be treated as supportive but dated rather than confirmatory.

**To proceed, the following is needed:**
- TFDA package insert / mechanism of action data (currently Blocking data gap)
- Confirmation of current pediatric oncology guideline status for methotrexate in rhabdomyosarcoma, given that platinum-based regimens are now more commonly used in relapsed/metastatic disease (PMID 36614297, 2023)
- Correction/re-verification of the NCT00357084 relevance grading in the underlying trial database
- Finland/Taiwan regulatory pathway assessment, since methotrexate currently has 0 marketing authorizations on file
- A dosing and myelosuppression/renal-function monitoring plan specific to the pediatric RMS population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

