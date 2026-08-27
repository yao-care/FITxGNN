---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine currently positioned for anesthesia induction and procedural sedation rather than as an oral treatment for chronic insomnia.
The TxGNN model predicts it may be effective for **Insomnia**, with **32 clinical trials** and **11 publications** identified in the search — though only a small, mostly historical subset directly supports this direction.
Given a blocking gap in local safety/label data, the current evidence level is **L2** and the recommendation is to **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no local marketing authorization on file); available data indicates current clinical use is procedural sedation / anesthesia induction |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available for this record. However, the evidence pack's repurposing rationale confirms midazolam is a short-acting benzodiazepine acting at the benzodiazepine binding site of the GABA-A receptor, enhancing GABAergic inhibitory neurotransmission — a pharmacology that is inherently sedative-hypnotic in nature and directly relevant to insomnia treatment.

Clinically, midazolam today is used almost exclusively for anesthesia induction and procedural sedation, not as a chronic oral hypnotic, largely because of its very short half-life, injectable route of administration, controlled-substance status, and dependence/withdrawal risk. The predicted link to insomnia is therefore not a novel mechanistic discovery but reflects a known class effect shared with other benzodiazepine hypnotics (e.g., flurazepam).

This class effect is supported by real historical evidence: several Phase-level RCTs from the 1980s–1990s directly tested oral midazolam in patients with sleep disorders/chronic insomnia and found it effective and generally well tolerated, before its clinical use shifted almost entirely toward procedural sedation. This gives the TxGNN prediction plausible pharmacological and historical grounding, even though it does not represent a new therapeutic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | IV midazolam vs. dexmedetomidine, combined with spinal anesthesia, compared for postoperative sleep quality after TURP; graded most directly relevant (Grade B) trial in the pack. |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam evaluated in patients with sleep disturbance/anxiety undergoing laparoscopic colorectal cancer resection; trial description notes oral midazolam solution is "safe and effective for short-term hypnosis." |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not yet recruiting | 195 | Oral melatonin vs. oral midazolam as premedication in children undergoing tonsillectomy, comparing sleep-inducing/anxiolytic effect. |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | Compared sleep quality/quantity (24-hour polysomnography) and delirium incidence between dexmedetomidine and midazolam in mechanically ventilated ICU patients; terminated early, very small sample. |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of sleep stages/total sleep time between α2-agonist (dexmedetomidine) and GABA-agonist (midazolam) sedation; terminated early, very small sample. |

*Note: 32 trials were retrieved in total; the majority (graded "C" or judged low relevance on review) involve midazolam only as a background sedation agent in unrelated surgical/ICU studies and are not listed here to avoid diluting the evidence table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Double-blind study in 30 women with insomnia secondary to neuromuscular disease: midazolam 15 mg and Vesparax both effective hypnotics; midazolam better tolerated with no hangover effect. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | Multicenter dose-finding study (75 patients, oral midazolam 10–30 mg) in mild-to-moderate insomnia secondary to musculoskeletal/neuropathic disorders; established optimal dose range. |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Multicenter, randomized, double-blind, parallel-group study of sleep, performance, and plasma levels during 14-day use of flurazepam vs. midazolam in chronic insomnia patients. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Executive summary of the above 14-day flurazepam vs. midazolam chronic-insomnia study (companion paper; abstract text not available). |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | General review of insomnia pathogenesis (hyperarousal state) and its relationship to cerebral hypoperfusion; background context, not midazolam-specific. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of clinical use of hypnotics, discussing benzodiazepine pharmacokinetic/pharmacodynamic differences and rationale for a variety of agents in insomnia subtypes. |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT | Journal of Clinical Medicine | Pilot study of lemborexant (not midazolam) for insomnia in high-risk pancreato-biliary patients post-endoscopy; notes benzodiazepines traditionally used for insomnia may worsen delirium risk — relevant safety context. |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are not currently available for this record — DDI query returned "not_found," and TFDA package-insert warnings/contraindications are flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Historical Phase-level RCTs (1980s–1990s) show oral midazolam was effective for insomnia/sleep disorders, but this reflects a known benzodiazepine class effect rather than a novel signal, and no recent or large-scale trials directly target chronic insomnia. Critically, TFDA package-insert warnings/contraindications are entirely missing (Blocking gap, DG001), which prevents this candidate from clearing the S1 safety screening stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA package insert warnings, precautions, and contraindications (DG001, blocking)
- DrugBank mechanism-of-action detail (DG002)
- Drug-drug interaction data (current DDI query status: not_found)
- Assessment of an oral formulation and dosing regimen suitable for chronic insomnia use, given midazolam's short half-life and controlled-substance status
- Local marketing authorization pathway analysis, since the drug currently has zero registered licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

