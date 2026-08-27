---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor generally known for use in Type 2 Diabetes Mellitus, though this evidence pack contains no confirmed Taiwan-approved indication text and shows the drug is **not currently marketed in Taiwan**. The TxGNN model links it to **Focal Stiff Limb Syndrome** (part of the stiff-person syndrome spectrum), but this pairing sits at rank 9036 with **zero clinical trials and zero publications** currently supporting it. The model's own rationale text describes the association as likely knowledge-graph noise rather than a biologically grounded hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack — drug is not currently marketed in Taiwan and no licensing/indication record exists |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.06% (rank 9036) |
| Evidence Level | L5 |
| Market Status (Taiwan) | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action text was not returned in this evidence pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology rather than dataset-verified content, Empagliflozin belongs to the SGLT2 (sodium-glucose cotransporter-2) inhibitor class, which acts on the renal proximal tubule to reduce glucose reabsorption.

Focal stiff limb syndrome is a localized variant within the stiff-person syndrome spectrum — an autoimmune neurological disorder driven by anti-GAD65 antibody attack on GABAergic neurons, causing insufficient central inhibitory signaling and muscle rigidity. There is no established pharmacological pathway connecting renal SGLT2 inhibition to central GABAergic neurotransmission or to autoimmune antibody modulation.

The evidence pack's own repurposing rationale is explicit on this point: it characterizes the Empagliflozin–stiff-limb-syndrome and Empagliflozin–classic-SPS pairings (ranks 9036 and 9037, with nearly identical scores) as likely **knowledge-graph co-occurrence noise between metabolic and neurological nodes**, not a biologically plausible hypothesis. No mechanistic bridge, preclinical study, clinical trial, or published case report supports the link. This should be read as a low-confidence, exploratory model output rather than a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

No authorization records available — Empagliflozin is not currently marketed in Taiwan (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications and the DDI database both returned no data for this drug — retrieving the official TFDA package insert is flagged as a Blocking data gap, DG001, and must be resolved before any safety evaluation (S1) can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence, no plausible mechanistic pathway between SGLT2 inhibition and stiff-person-syndrome pathophysiology, and the prediction itself sits at a low model rank (9036) with the source rationale explicitly describing it as likely graph noise. Combined with the absence of confirmed original-indication and Taiwan safety data, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Official TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Confirmation of Empagliflozin's original approved indication(s) and Taiwan licensing status
- Independent preclinical or mechanistic evidence linking SGLT2 inhibition to GABAergic/autoimmune pathways before any further investment in this indication
- Re-screening of ClinicalTrials.gov, ICTRP, and PubMed on a recurring basis, since all three returned zero hits as of the 2026-04-20 query date

---

**Aside for your review:** the source template's Quick Overview field is labeled "Finland Market Status" (and the section header "Finland Market Information"), but this evidence pack's actual data lives under `taiwan_regulatory` and was sourced from TFDA (`query_log` source `tfda`/`tfda_package_insert`). I relabeled these to Taiwan in the report above rather than propagate what looks like a copy-paste artifact from the Finland-project template. Given `.claude/p0_consistency_check.sh` exists specifically to catch this class of cross-project copy-paste issue, you may want to run it against the report-generation template/prompt source to confirm and fix it upstream.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

