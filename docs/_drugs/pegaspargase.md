---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Hodgkin Lymphoma (Extranodal NK/T-Cell Lymphoma)

## One-Sentence Summary

> Pegaspargase (PEGylated L-asparaginase) is an established chemotherapy component for acute lymphoblastic leukemia (ALL)/lymphoblastic lymphoma, where it depletes serum asparagine to selectively kill asparagine-synthetase-deficient malignant lymphoblasts.
> This evidence pack contains **10 TxGNN-ranked candidate indications**; two of the top five (precursor lymphoblastic lymphoma/leukemia and "acute lymphoblastic leukemia") are simply the drug's **existing, already-approved use** rather than a new hypothesis.
> The most credible genuinely **new-use** signal in this pack is ranked #8 and labeled **"Hodgkin lymphoma,"** but nearly all of its supporting trials and literature actually study **Extranodal NK/T-cell Lymphoma (ENKTL)** — a distinct, aggressive non-Hodgkin subtype in which asparaginase-based regimens (SMILE, P-GEMOX, GELOX, DDGP) are already used in real-world practice, backed by **18 clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) / Lymphoblastic Lymphoma *(inferred from clinical-trial context and repurposing rationale — `original_indications` field was empty in the evidence pack)* |
| Predicted New Indication | Hodgkin Lymphoma (label) — supporting evidence corresponds primarily to **Extranodal NK/T-cell Lymphoma (ENKTL)** |
| TxGNN Prediction Score | 99.71% (rank 3726 of model output) |
| Evidence Level | L2 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

**Note on this evidence pack:** This is a multi-indication candidate pack (`candidate_id: TW-DB00059-multi`) containing 10 ranked TxGNN predictions. The table below summarizes all of them so the reader understands the full portfolio before the deep dive on the primary candidate.

### Portfolio of All TxGNN-Predicted Indications in This Pack

| Rank | Disease Label | Score | Evidence Level | Recommendation | Note |
|------|---------------|-------|-----------------|-----------------|------|
| 1 | Precursor lymphoblastic lymphoma/leukemia | 99.96% | L1 | Proceed with Guardrails | **Not a new indication** — this is the drug's core existing use |
| 2 | Pregerminal center CLL/SLL | 99.95% | L5 | Hold | No trials/literature; mechanistically weak (mature, slow-proliferating B cells) |
| 3 | CLL/SLL (IGHV-mutated subtype) | 99.95% | L5 | Hold | Same as above |
| 4 | Follicular lymphoma | 99.90% | L5 | Hold | No evidence; indolent germinal-center lymphoma, weak rationale |
| 5 | Acute lymphoblastic leukemia | 99.89% | L1 | Proceed with Guardrails | **Not a new indication** — duplicate of rank 1 |
| 6 | Methylcobalamin deficiency (cblE) | 99.74% | L5 | Hold | Biologically implausible (B12/MTRR metabolic defect) — likely graph noise; recommend exclusion |
| 7 | Lymphoid neoplasm | 99.71% | L2 | Research Question | Overly broad label; evidence overlaps substantially with existing ALL trials |
| **8** | **Hodgkin lymphoma** | **99.71%** | **L2** | **Research Question** | **Primary candidate analyzed below — evidence base is largely ENKTL, not classic Hodgkin lymphoma** |
| 9 | CLL/SLL | 99.68% | L5 | Hold | No evidence |
| 10 | Blast-phase CML, BCR-ABL1+ | 99.61% | L3 | Research Question | Plausible only if lymphoid blast crisis; weak evidence (2 trials, 1 case report) |

---

## Why is This Prediction Reasonable?

Pegaspargase is a PEGylated form of *E. coli*-derived L-asparaginase. Malignant lymphoblasts in ALL/lymphoblastic lymphoma characteristically lack asparagine synthetase (ASNS) and depend on exogenous serum asparagine to sustain protein synthesis. Pegaspargase depletes plasma asparagine, selectively starving these malignant cells while sparing most normal tissues — a mechanism explicitly confirmed in the evidence pack's own rationale text, even though the drug-level `original_moa` field itself is marked as a data gap (DG002).

Ranks 1 and 5 in this pack ("precursor lymphoblastic lymphoma/leukemia" and "acute lymphoblastic leukemia") are **not new hypotheses** — they are simply the drug's already-established indication being re-surfaced by the model with very high confidence. This is a useful model-calibration signal (it confirms TxGNN correctly recognizes Pegaspargase's real pharmacology) but has no repurposing value.

The most actionable **genuinely new** signal is rank 8. TxGNN's disease ontology labels it "Hodgkin lymphoma," but essentially all of the associated trials and papers (SMILE, P-GEMOX, GELOX, DDGP regimens) describe **Extranodal NK/T-cell Lymphoma (ENKTL)** — a mature NK/T-cell neoplasm that, like ALL, frequently shows low ASNS expression and is asparagine-dependent, giving a biologically coherent rationale for asparaginase-based therapy. ENKTL is biologically and clinically distinct from classic Hodgkin lymphoma, so this is very likely an **ontology/label mapping issue** rather than a genuine Hodgkin lymphoma signal. Because asparaginase-based regimens for ENKTL are already widely used in Asia-Pacific clinical practice (largely outside Western label indications), this represents a credible "old drug, already-adopted new use" story that merits formal indication/label clarification before further action.

---

## Clinical Trial Evidence

*(Trials shown are the evidence supporting the rank-8 candidate; nearly all study ENKTL rather than classic Hodgkin lymphoma — see caveat above.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02085655](https://clinicaltrials.gov/study/NCT02085655) | Phase 3 | Unknown | 264 | Randomized comparison of PA-Gemox followed by thalidomide vs. AspaMetDex regimen in NKTCL |
| [NCT02631239](https://clinicaltrials.gov/study/NCT02631239) | Phase 3 | Unknown | 256 | Etoposide/dexamethasone/pegaspargase ± methotrexate with sandwiched radiotherapy in stage I–II ENKTL, nasal type |
| [NCT02359162](https://clinicaltrials.gov/study/NCT02359162) | Phase 3 | Terminated | 50 | Randomized P-Gemox vs. EPOCH as first-line chemotherapy in NK/T-cell lymphoma |
| [NCT02918747](https://clinicaltrials.gov/study/NCT02918747) | Phase 2 | Unknown | 100 | Randomized P-Gemoxd + radiotherapy vs. P-CHOP + radiotherapy in early-stage ENKTL |
| [NCT02533323](https://clinicaltrials.gov/study/NCT02533323) | Phase 2 | Terminated | 50 | Pegaspargase-Gemox (P-Gemox) as first-line therapy in newly diagnosed, nasal-type ENKTL |
| [NCT06583083](https://clinicaltrials.gov/study/NCT06583083) | Phase 2 | Recruiting | 84 | Sintilimab (PD-1 antibody) + P-GEMOX vs. P-GEMOX alone in advanced-stage ENKTL |
| [NCT02080234](https://clinicaltrials.gov/study/NCT02080234) | Phase 2 | Unknown | 40 | GELOX (gemcitabine/oxaliplatin/asparaginase) with concurrent radiotherapy in stage IE/IIE ENKTL |
| [NCT02705508](https://clinicaltrials.gov/study/NCT02705508) | Phase 2 | Unknown | 35 | PEG-ASP + etoposide + gemcitabine (PEG regimen) as first-line therapy for NK/T-cell lymphoma |
| [NCT07457177](https://clinicaltrials.gov/study/NCT07457177) | Phase 2 | Not yet recruiting | 40 | Golidocitinib + pegaspargase + anti-PD-1 antibody as first-line therapy for advanced ENKTL |
| [NCT06953739](https://clinicaltrials.gov/study/NCT06953739) | Phase 3 | Not yet recruiting | 60 | Pegaspargase + P-GEMD vs. P-Gemox in untreated early-stage (non-upper-aerodigestive) or advanced ENKTL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27723108](https://pubmed.ncbi.nlm.nih.gov/27723108/) | 2017 | RCT | Hematological Oncology | Phase 2 multicenter trial of MESA (methotrexate/etoposide/dexamethasone/pegaspargase) in newly diagnosed, relapsed, or refractory ENKTL, nasal type; CR 43.5%, ORR 87% |
| [34449095](https://pubmed.ncbi.nlm.nih.gov/34449095/) | 2021 | Cohort | American Journal of Hematology | Multicenter study of sequential P-GEMOX + radiotherapy in early-stage ENKTL |
| [29194798](https://pubmed.ncbi.nlm.nih.gov/29194798/) | 2018 | Cohort | European Journal of Haematology | Multicenter retrospective study of GELOXD/P-GEMOXD efficacy and tolerance in newly diagnosed nasal-type ENKTL |
| [2345067](https://pubmed.ncbi.nlm.nih.gov/2345067/) | 1990 | Review/Phase 2 | Investigational New Drugs | Phase 2 trial of PEG-L-asparaginase in refractory non-Hodgkin lymphoma (21 patients) |
| [30241515](https://pubmed.ncbi.nlm.nih.gov/30241515/) | 2018 | Cohort | BMC Cancer | PEG-L-CHOP regimen shown safe and effective in adult ENKTL with low hypersensitivity rate |
| [24299319](https://pubmed.ncbi.nlm.nih.gov/24299319/) | 2014 | Case Series | Neoplasma | DDGP regimen (pegaspargase/dexamethasone/cisplatin/gemcitabine) in newly diagnosed ENKTL |
| [37486391](https://pubmed.ncbi.nlm.nih.gov/37486391/) | 2023 | Cohort | Annals of Hematology | "Sandwich" modified SMILE regimen (including pegaspargase) in pediatric newly diagnosed ENKTL |
| [29764116](https://pubmed.ncbi.nlm.nih.gov/29764116/) | 2019 | Cohort | Cancer Research and Treatment | Low circulating CD4+ T-cell count predicts poor prognosis in ENKTL treated with pegaspargase-based chemotherapy |
| [19786301](https://pubmed.ncbi.nlm.nih.gov/19786301/) | 2010 | Case Report | Leukemia Research | Two ENKTL patients refractory to CHOP responded to single-agent pegaspargase |
| [8481665](https://pubmed.ncbi.nlm.nih.gov/8481665/) | 1993 | Review | Leukemia & Lymphoma | Historical review of L-asparaginase/PEG-asparaginase development and lymphoid-malignancy applications |

---

## Finland Market Information

Pegaspargase currently holds **no marketing authorization in Finland** (`market_status: Not Marketed`, `total_licenses: 0`). No product listings, dosage forms, or approved indication text were available in this evidence pack for the Finnish market.

---

## Cytotoxicity

Pegaspargase is an antineoplastic agent used exclusively within combination chemotherapy regimens for hematologic malignancies, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — enzyme-based, asparagine-depleting agent (not a DNA-damaging cytotoxic; mechanism is metabolic/protein-synthesis inhibition) |
| Myelosuppression Risk | Low to Moderate as monotherapy — asparaginase itself is not strongly myelosuppressive, but it is invariably combined with myelosuppressive agents (vincristine, anthracyclines, cytarabine, etc.) in ALL/ENKTL regimens, and combination-regimen myelosuppression is well documented in the literature evidence above |
| Emetogenicity Classification | Low (asparaginase-class agents are generally classified as low emetogenic risk) |
| Monitoring Items | Liver function tests (hepatotoxicity), lipid panel/triglycerides (hypertriglyceridemia), coagulation parameters — fibrinogen, antithrombin (thrombosis/bleeding risk), amylase/lipase (pancreatitis), blood glucose (hyperglycemia), and hypersensitivity monitoring; CBC with differential per standard combination-regimen practice |
| Handling Protection | Yes — must be handled under standard cytotoxic/hazardous drug handling precautions (closed-system transfer, PPE) |

*(Toxicity items above are derived from literature evidence within this pack — e.g., pancreatitis, hypertriglyceridemia, and hepatotoxicity case reports/cohorts identified for pegaspargase — since DrugBank-level toxicity/warning data was not directly available in this evidence pack.)*

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Both `key_warnings` and `contraindications` were marked as data gaps, and the DDI query returned no results in this evidence pack. Note separately: Data Gap DG001 flags that TFDA/Fimea package-insert warnings and contraindications are a **Blocking**-severity gap — this must be resolved before any S1 safety pre-assessment can proceed, regardless of the efficacy evidence level discussed above.)*

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
- Two of this pack's top predictions (ranks 1 and 5) merely restate Pegaspargase's existing approved use and carry no repurposing value; several others (ranks 2, 3, 4, 6, 9) have no supporting clinical or literature evidence and are likely model noise, including one (cblE, rank 6) that is biologically implausible.
- The only credible new-use signal (rank 8) is confounded by a disease-label mismatch — real-world evidence supports **Extranodal NK/T-cell Lymphoma**, not classic Hodgkin lymphoma — and while the ENKTL evidence base is genuinely substantial (L2, 18 trials, 20 publications, including Phase 3 RCTs), it cannot be scored or acted on correctly until the disease-label mapping is verified.
- Separately, this candidate is currently gated by a **Blocking**-severity data gap (DG001: missing TFDA/Fimea package-insert warnings/contraindications), which prevents any safety pre-assessment regardless of efficacy evidence quality.

**To proceed, the following is needed:**
- Verify and correct the disease-ontology mapping for the rank-8 prediction (confirm ENKTL vs. classic Hodgkin lymphoma before any further scoring)
- Obtain TFDA/Fimea package insert (warnings, contraindications) to resolve the blocking safety data gap (DG001)
- Obtain formal DrugBank/MOA documentation to resolve the MOA data gap (DG002)
- If ENKTL is confirmed as the intended target indication, request updated evidence retrieval using "extranodal NK/T-cell lymphoma" as the disease query term rather than "Hodgkin lymphoma"
- Given zero current Finland marketing authorization, evaluate feasibility/regulatory pathway before any repurposing program is initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

