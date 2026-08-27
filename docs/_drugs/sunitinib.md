---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

Using the evidence pack directly (no skill applies — this is a templated content-generation task with the format fully specified in the prompt).

# Sunitinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sunitinib is a multi-targeted tyrosine kinase inhibitor already established globally for renal cell carcinoma, GIST, and pancreatic neuroendocrine tumours, though it is not currently marketed in Finland. The TxGNN model predicts it may also be effective for **Liposarcoma**, with **3 clinical trials** and **9 publications** currently supporting this direction. The same evidence pack also independently recovered sunitinib's known renal cell carcinoma activity (L1 evidence), which lends credibility to the model's less-established predictions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Fimea licensing data (drug not marketed in Finland); literature within this evidence pack confirms sunitinib is a globally approved first-line therapy for advanced/metastatic renal cell carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this drug entry. Based on information embedded in the trial and literature evidence collected for this pack, sunitinib is described repeatedly as a **multitargeted receptor tyrosine kinase inhibitor**, acting on VEGFR, PDGFR, and KIT, and working by "blocking some of the enzymes needed for cell growth and by blocking blood flow to the tumor" (NCT00474994). Its efficacy in VEGF/PDGFR-driven cancers such as renal cell carcinoma is well proven — reflected in this same evidence pack, where sunitinib appears as the historical standard-of-care comparator arm in numerous Phase 3 renal cell carcinoma trials (e.g., NCT00083889, NCT02231749, NCT03141177).

Soft tissue sarcomas, including several liposarcoma subtypes, frequently show PDGFR and VEGFR pathway activation, providing a plausible mechanistic bridge from the drug's proven anti-angiogenic/anti-proliferative activity in renal cell carcinoma to activity in liposarcoma. This is not a purely theoretical leap: two completed Phase 2 trials (NCT00400569, NCT00474994) already tested sunitinib directly in liposarcoma patients as part of broader soft-tissue-sarcoma cohorts, and a published case report (PMID 23482782) documents long-lasting clinical benefit in a heavily pre-treated metastatic liposarcoma patient.

That said, liposarcoma is histologically heterogeneous. Well-differentiated and dedifferentiated subtypes are predominantly MDM2-driven rather than PDGFR/VEGFR-driven, so sunitinib's activity is likely confined to specific subtypes (e.g., myxoid/round-cell liposarcoma) rather than the disease as a whole — a caveat the evidence pack itself flags.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site trial of sunitinib malate in adult patients with metastatic/unresectable soft tissue sarcoma, including liposarcoma, leiomyosarcoma, fibrosarcoma, and MFH |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing sunitinib trial in non-GIST sarcomas (metastatic, locally advanced, or recurrent); liposarcoma among eligible histologies |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 basket study of oral regorafenib (not sunitinib) across sarcoma subtypes including liposarcoma; only indirectly relevant, cited as precedent for kinase-inhibitor activity in sarcomas |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase 2 trial | International Journal of Cancer | Phase 2 study of sunitinib malate in relapsed/refractory soft tissue sarcoma, with dedicated focus on leiomyosarcoma, liposarcoma, and MFH |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Research | Long-lasting clinical benefit of sunitinib malate in a heavily pre-treated metastatic liposarcoma patient |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review (genomic) | Cancers | Genetic, epigenetic, and transcriptomic alterations in liposarcoma relevant to target-therapy selection |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of adult soft tissue sarcomas by histological subtype, including targeted-agent options |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Review of Anticancer Therapy | Emerging systemic therapies for adult soft tissue sarcoma |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven medical treatment of soft tissue sarcomas, noting subtype-specific chemosensitivity |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case series (pathology) | American Journal of Surgical Pathology | Clinicopathologic analysis of myxoid inflammatory myofibroblastic sarcoma, a related but distinct sarcoma entity |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Genomic profiling | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma, evaluating predictors of sunitinib benefit |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol (regorafenib) | BMC Cancer | REGOSARC protocol for regorafenib in advanced soft tissue sarcoma; different drug, cited for angiogenesis-pathway rationale only |

## Finland Market Information

Sunitinib is **not currently marketed in Finland**. No Fimea marketing authorizations are on record in this evidence pack (0 licenses), so no product-level dosage form or indication text is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted receptor tyrosine kinase inhibitor; VEGFR/PDGFR/KIT), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Given the drug class, standard practice for oral VEGFR-targeted TKIs includes CBC with differential, liver and renal function, and blood pressure/cardiac monitoring; exact thresholds pending Fimea package insert (data gap) |
| Handling Protection | Oral capsule formulation; standard oral antineoplastic handling precautions apply (avoid crushing/opening capsules); confirm against local hazardous-drug handling policy pending package insert |

## Safety Considerations

Please refer to the package insert for safety information. Fimea warnings, contraindications, and drug-interaction data are not yet available in this evidence pack (flagged as a Blocking data gap — see Conclusion).

## Other Candidate Indications Identified in This TxGNN Run

This evidence pack scored ten candidate indications for sunitinib. For context, they are summarized below; only liposarcoma (rank 1) is detailed above.

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|-----------------|----------|
| 2 | Ovarian myxoid liposarcoma | 99.84% | L3 | Research Question |
| 3 | RCC associated with neuroblastoma | 99.78% | L5 | Hold (trial linkage appears mismatched) |
| 4 | RCC with Xp11.2/TFE3 fusion | 99.78% | L3 | Research Question |
| 5 | Unclassified RCC | 99.78% | L2 | Proceed with Guardrails |
| 6 | Dermatofibrosarcoma protuberans | 99.73% | L2 | Proceed with Guardrails |
| 7 | Childhood kidney cell carcinoma | 99.72% | L4 | Research Question |
| 8 | Angiolipoma | 99.67% | L5 | Hold (benign, no systemic-therapy rationale) |
| 9 | Renal carcinoma | 99.65% | L1 | Proceed with Guardrails (already a globally approved indication, not a novel finding) |
| 10 | Heart fibrosarcoma | 99.63% | L5 | Hold (no evidence, cardiotoxicity concern with TKI use) |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 2 trials and a case report directly support sunitinib activity in liposarcoma, and the mechanistic link (VEGFR/PDGFR pathway) is grounded in evidence already present in this pack. However, liposarcoma's histological heterogeneity means benefit is likely subtype-specific, and no Finland-specific regulatory or safety data currently exist.

**To proceed, the following is needed:**
- Fimea package insert warnings, contraindications, and full safety profile (currently a Blocking data gap)
- Structured DrugBank mechanism-of-action data to formally confirm target/pathway claims
- Subtype-level liposarcoma response data (e.g., myxoid/round-cell vs. well-differentiated/dedifferentiated) to refine the guardrails for patient selection
- A regulatory pathway assessment given sunitinib is not currently marketed in Finland
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

