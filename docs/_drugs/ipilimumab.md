---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the report template (v5) supplied in the prompt to generate the evaluation report. The pack contains two predicted indications — non-cutaneous melanoma (rank 2) has real trial/literature evidence and an actionable L2/S3 score, while choroideremia (rank 1 by raw score) has zero supporting evidence and an explicit Hold with a flagged mechanistic conflict. I'm building the primary report around non-cutaneous melanoma (the one an evaluator can actually act on) and disclosing the choroideremia signal briefly rather than silently dropping it.

# Ipilimumab: From Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

> Ipilimumab is a CTLA-4 immune checkpoint inhibitor with established use in metastatic melanoma (marketed globally as Yervoy).
> The TxGNN model predicts it may also be effective for **non-cutaneous melanoma** (uveal, mucosal, leptomeningeal, and acral subtypes),
> with **50 clinical trials** and **5 publications** currently available as supporting context, though most trials study melanoma broadly rather than non-cutaneous subtypes specifically.

*Note: The TxGNN model separately flagged **choroideremia** as a higher-scoring candidate (score 0.99, rank 9029), but with zero clinical trials or literature, an evidence level of L5, and a Hold recommendation — its own rationale notes no known biological link to CTLA-4 blockade and a potential mechanistic conflict (checkpoint inhibitors can induce ocular immune-related adverse events such as uveitis). It is not carried forward as a primary candidate in this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma (known public labeling for ipilimumab/Yervoy; not confirmed via Finland licensing data — no entries on file) |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L2 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for this record is a data gap (DG002). Based on known information and the evidence pack's own rationale, ipilimumab is an anti-CTLA-4 monoclonal antibody: it blocks the CTLA-4 inhibitory checkpoint on T cells, releasing the brake on T-cell activation and enhancing anti-tumor immune response. This mechanism is not specific to any particular anatomical origin of melanoma.

Non-cutaneous melanoma (uveal, mucosal, acral, and leptomeningeal subtypes) is biologically distinct from cutaneous melanoma in mutational profile and prognosis, but the underlying immune-evasion pathway CTLA-4 blockade targets is not tissue-specific. Since ipilimumab's efficacy in melanoma broadly is already well established (including combination regimens with nivolumab across multiple approved and investigational settings), the mechanistic extension to non-cutaneous subtypes is plausible in principle.

One important caveat: the input pack shows `original_indications` as empty and Finland `market_status` as "not marketed," which is itself a data gap rather than evidence that melanoma is a genuinely novel indication for this drug. Ipilimumab (Yervoy) already carries melanoma indications in multiple jurisdictions. This prediction should therefore be read as an extension into an under-studied *subtype* of an already-approved disease, not as an entirely new therapeutic hypothesis — which affects how much additional evidence is really needed before action.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Phase 3 | Active, not recruiting | 267 | DREAMseq: sequencing of ipilimumab+nivolumab vs. dabrafenib+trametinib in BRAF-mutant advanced melanoma; highest-grade direct evidence for the ipilimumab-melanoma mechanism. |
| [NCT02939300](https://clinicaltrials.gov/study/NCT02939300) | Phase 2 | Completed | 18 | Ipilimumab + nivolumab in leptomeningeal metastases from melanoma — directly relevant non-cutaneous/CNS-spread population. |
| [NCT03645928](https://clinicaltrials.gov/study/NCT03645928) | Phase 2 | Recruiting | 245 | TIL therapy (lifileucel) combined with checkpoint inhibitors in solid tumors; ipilimumab as adjunct, indirect support. |
| [NCT04133948](https://clinicaltrials.gov/study/NCT04133948) | Phase 1/2 | Completed | 44 | Neoadjuvant domatinostat + nivolumab ± ipilimumab in Stage III cutaneous/unknown-primary melanoma. |
| [NCT01654692](https://clinicaltrials.gov/study/NCT01654692) | Phase 2 | Completed | 86 | Ipilimumab + fotemustine in unresectable/metastatic melanoma; supportive combination data. |
| [NCT01927419](https://clinicaltrials.gov/study/NCT01927419) | Phase 2 | Completed | 142 | RCT of nivolumab + ipilimumab vs. ipilimumab monotherapy in untreated unresectable/metastatic melanoma. |
| [NCT01810016](https://clinicaltrials.gov/study/NCT01810016) | Phase 1 | Terminated | 8 | NY-ESO-1 vaccine + ipilimumab in unresectable/metastatic melanoma; small, terminated, weak evidence. |
| [NCT02452294](https://clinicaltrials.gov/study/NCT02452294) | Phase 2 | Unknown | 22 | Buparlisib in melanoma with brain metastases previously failing ipilimumab; ipilimumab is background therapy, not the study drug. |
| [NCT01496807](https://clinicaltrials.gov/study/NCT01496807) | Phase 1 | Completed | 31 | Ipilimumab (Yervoy) + peginterferon (Sylatron) safety/tolerability in Stage IIIB/C/IV melanoma. |
| [NCT01940809](https://clinicaltrials.gov/study/NCT01940809) | Phase 1 | Terminated | 15 | Ipilimumab ± dabrafenib/trametinib/nivolumab sequencing study in BRAF-mutant metastatic melanoma; terminated, small sample. |

*Note: 50 trials were returned by the search; the pack graded only 10 for relevance (1×A, 5×B, 4×C) and left the remaining ~40 as "pending" review — the table above lists all 10 graded trials. None of the trials specifically enroll a "non-cutaneous melanoma" cohort by name; relevance is inferred from shared mechanism and, for NCT02939300/NCT02626962-type trials, from non-cutaneous subtypes (leptomeningeal, uveal) appearing as enrolled populations.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort/Expanded-access | The Medical Journal of Australia | Real-world efficacy/tolerability of ipilimumab in pretreated cutaneous, **uveal**, and **mucosal** melanoma — directly addresses non-cutaneous subtypes. |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | Retrospective comparison of anti-PD-1 monotherapy vs. anti-PD-1 + ipilimumab by age group in advanced melanoma. |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Current Cancer Drug Targets | Review of melanoma adjuvant treatment; explicitly notes only ~5% of melanoma is non-cutaneous and discusses trial landscape 2000–2015. |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discovery Medicine | Clinical update on anti-PD-1 antibodies alone or combined with ipilimumab as standard frontline therapy for advanced melanoma. |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Case report of colonic metastasis from melanoma treated with immunotherapy; illustrates immune-related GI adverse events during ipilimumab-containing regimens. |

---

## Finland Market Information

No product authorizations are on file for ipilimumab in Finland (`total_licenses = 0`, `market_status = 未上市/not marketed`). This is a data gap rather than confirmation of non-availability, since ipilimumab (Yervoy) is approved in the EU/EEA more broadly.

---

## Cytotoxicity

Ipilimumab is an antineoplastic agent (used to treat melanoma) but is not a conventional cytotoxic chemotherapy — it is a monoclonal antibody immune checkpoint inhibitor.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody) |
| Myelosuppression Risk | Low — checkpoint inhibitors as a class do not typically cause significant bone marrow suppression, unlike conventional cytotoxics |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function, thyroid/endocrine function, renal function, and clinical monitoring for immune-related adverse events (colitis, hepatitis, dermatitis, endocrinopathy) rather than routine cytopenia surveillance |
| Handling Protection | Standard institutional precautions for monoclonal antibody infusion; not subject to cytotoxic chemotherapy handling regulations, but local hazardous-drug policy should be confirmed |

*This assessment is based on the established pharmacological class profile of CTLA-4 inhibitors, since drug-specific toxicity data was not returned in this pack (DG001/DG002).*

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were all flagged as data gaps in this pack — DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism of CTLA-4 blockade is not anatomically specific, and ipilimumab already has substantial melanoma trial and literature support, including one Phase 3 RCT (DREAMseq) and dedicated evidence in uveal/mucosal/leptomeningeal subtypes (PMID 24999899, NCT02939300). However, most of the 50 trials study melanoma broadly rather than non-cutaneous subtypes specifically, and this candidate is better framed as a subgroup extension of an existing indication than a genuinely novel repurposing hypothesis — hence guardrails rather than an unconditional Go.

**To proceed, the following is needed:**
- Formal mechanism-of-action confirmation from DrugBank (DG002)
- TFDA/Fimea package insert warnings, contraindications, and DDI data (DG001)
- Subtype-stratified efficacy data specific to non-cutaneous melanoma (currently inferred, not directly reported, in most trials)
- Confirmation of actual Finland/EU marketing and authorization status, since "not marketed" here likely reflects a data gap rather than true unavailability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

