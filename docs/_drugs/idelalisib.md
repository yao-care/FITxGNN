---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# Idelalisib: From Chronic Lymphocytic Leukemia/Follicular Lymphoma to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib is a first-in-class, oral PI3Kδ inhibitor originally developed for relapsed chronic lymphocytic leukemia (CLL), follicular lymphoma (FL), and small lymphocytic lymphoma (SLL). The TxGNN model predicts it may also be effective for **Mantle Cell Lymphoma (MCL)**, with **9 clinical trials** and **20 publications** currently touching on this direction — though the evidence remains early-stage and MCL is not an approved indication for this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed CLL, relapsed follicular lymphoma, relapsed small lymphocytic lymphoma (per literature, e.g. PMID 25187123, 25637459) |
| Predicted New Indication | Mantle Cell Lymphoma (MCL) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (internally staged as "Research Question", decision stage S2) |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data was not retrieved for this candidate (data gap DG002). Based on the literature captured in this evidence pack, idelalisib is described as a first-in-class, orally administered, selective inhibitor of the delta isoform of phosphatidylinositol 3-kinase (PI3Kδ) — an enzyme expressed predominantly in hematopoietic cells that plays a non-redundant role in B-cell receptor (BCR) signaling, a pathway that drives survival, proliferation, and microenvironment retention of malignant B cells.

Idelalisib's original approved population (CLL, FL, SLL) shares this BCR/PI3Kδ dependency with MCL, which is also a B-cell non-Hodgkin lymphoma. This shared pathway is the basis of the TxGNN prediction, and it is reflected in real-world trial design: several early idelalisib studies enrolled MCL patients alongside CLL/FL/iNHL cohorts under a common "B-cell malignancy" umbrella (e.g., NCT01088048, NCT01796470).

However, the mechanistic rationale is only partially borne out clinically. A dedicated Phase 1 study of idelalisib monotherapy in relapsed/refractory MCL (PMID 24615778) and an early cohort report (PMID 24795031) showed some single-agent activity, but subsequent preclinical work (PMID 33850273, PMID 40466505) identified **intrinsic resistance** of MCL cells to idelalisib, requiring combination strategies (e.g., p300/CBP inhibition, CBX5-mediated ferroptosis induction) to restore sensitivity. As the internal repurposing rationale notes: mechanistically plausible, but single-agent clinical activity is limited and MCL is not a currently approved indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib (GS-9973) + idelalisib in relapsed/refractory hematologic malignancies incl. MCL, CLL, DLBCL, iNHL; direct MCL evaluation but terminated early — Grade A relevance, underpowered |
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 | Completed | 106 | Idelalisib + lenalidomide in relapsed/refractory MCL; completed combination-therapy exploratory study — Grade B |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as post-allogeneic HSCT maintenance in B-cell malignancies incl. MCL; terminated, small sample — Grade C |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completed | 121 | Real-life PK/side-effect correlation study of ibrutinib and idelalisib in hematological malignancies incl. MCL |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib combined with targeted anti-cancer therapies in B-cell malignancies incl. MCL; terminated |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Pirtobrutinib (LOXO-305) in CLL/SLL/NHL populations, including MCL as comparator/reference group |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unknown | 464 | Quality-of-life assessment of oral lymphoma therapies (incl. idelalisib) in patients incl. MCL |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Idelalisib + chemo/immunomodulatory/anti-CD20 agents in relapsed/refractory iNHL, MCL, or CLL |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 + idelalisib dose-escalation safety study in FL and MCL patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 clinical study | Blood | First dedicated Phase 1 study of idelalisib monotherapy in R/R MCL (n=40); defined dosing, evaluated ORR/PFS/DOR |
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Cohort | Cancer Discovery | Idelalisib showed single-agent activity in heavily pretreated MCL patients |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacol Sin | MCL shows intrinsic resistance to idelalisib; p300/CBP inhibitor A-485 restores sensitivity in vitro/in vivo |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ-inhibitor resistance in MCL; propolis restores sensitivity via ferroptosis induction |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical | Clin Cancer Res | Idelalisib inhibits MCL cell growth via disruption of translation-regulatory mechanisms |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances anti-tumor effect of CDK4/6 inhibitor palbociclib via PLK1 in MCL/DLBCL |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | Br J Haematol | Overview of current regimens and novel agents (incl. PI3K inhibitors) for MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Review | Expert Opin Pharmacother | Review of treatment options for MCL, including novel targeted agents |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | Review | Curr Treat Options Oncol | Review of current and emerging therapies in MCL |
| [24273091](https://pubmed.ncbi.nlm.nih.gov/24273091/) | 2013 | Review | Am J Hematol | 2013 update on MCL diagnosis, risk-stratification, and clinical management |

---

## Finland Market Information

Idelalisib is not currently marketed in Finland — 0 authorizations are on file, and the drug's Finnish regulatory status is recorded as "未上市" (not marketed).

---

## Cytotoxicity

Idelalisib is an antineoplastic agent (targeted small-molecule kinase inhibitor used for hematologic malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Formal hematologic toxicity data was not retrieved in this evidence pack (DDI/warnings query returned no results); literature associated with idelalisib in B-cell malignancies notes neutropenia among reported adverse events (PMID 27054023) |
| Emetogenicity Classification | Not established in the retrieved data; please refer to the package insert |
| Monitoring Items | CBC with differential (cytopenias), liver function tests (hepatotoxicity), pulmonary symptom monitoring (pneumonitis), GI symptom monitoring (idelalisib-associated colitis/diarrhea, per NCT02928510 and PMID 28775119) |
| Handling Protection | Yes — as an oral targeted antineoplastic agent, standard cytotoxic/hazardous drug handling precautions should be followed pending confirmation against the local package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for idelalisib in MCL is limited to a single dedicated Phase 1 monotherapy study (n=40) and several early-phase or prematurely terminated combination trials (L2 evidence, decision stage S2). Preclinical literature further indicates intrinsic MCL resistance to idelalisib, and MCL is not an approved indication for this drug — mechanistic plausibility exists, but confirmatory efficacy is lacking.

**To proceed, the following is needed:**
- Confirmatory randomized (Phase 2/3) efficacy data specifically in MCL
- Resistance-informed combination strategy data (e.g., epigenetic co-inhibition) given reported intrinsic MCL resistance
- TFDA/Finland package insert warnings and contraindications (currently a Blocking data gap, DG001) before any S1 safety assessment can proceed
- Formal DrugBank-sourced mechanism-of-action documentation (currently a data gap, DG002)
- Confirmation of Finland market entry pathway, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

