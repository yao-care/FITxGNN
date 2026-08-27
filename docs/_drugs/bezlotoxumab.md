---
layout: default
title: Bezlotoxumab
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: From *Clostridioides difficile* Infection Recurrence Prevention to Acute Female Pelvic Peritonitis

## One-Sentence Summary

Bezlotoxumab is a monoclonal antibody that neutralizes *C. difficile* toxin B, used to prevent recurrence of *C. difficile* infection (CDI). The TxGNN model's top prediction for this drug is **Acute Female Pelvic Peritonitis** (score 99.89%), but this candidate — and all 9 others in the top-10 list — has **zero supporting clinical trials or literature**, and the model's own mechanistic rationale flags the biological link as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of *Clostridioides difficile* infection (CDI) recurrence *(inferred from the repurposing rationale text in this evidence pack; not yet confirmed via TFDA/DrugBank structured records — see data gap DG002)* |
| Predicted New Indication | Acute Female Pelvic Peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (DrugBank field marked as data gap). Based on the mechanistic notes accompanying this prediction, bezlotoxumab is a monoclonal antibody that binds and neutralizes *C. difficile* toxin B in the gut, preventing the toxin-mediated tissue damage that drives CDI recurrence. It does not have a known antimicrobial or broader anti-inflammatory mechanism.

Acute female pelvic peritonitis is typically caused by ascending polymicrobial infection (mixed aerobic/anaerobic flora) from the genital tract, a pathophysiology unrelated to *C. difficile* toxin activity. The evidence pack's own repurposing rationale explicitly characterizes this mechanistic link as weak, with no known biological connection between toxin-B neutralization and pelvic infection pathology.

Notably, this is not an isolated case: all 10 top-ranked candidates for bezlotoxumab (pelvic peritonitis, fallopian tube cyst, tubal pregnancy, salpingitis isthmica nodosa, broad ligament disease, lumbar spinal stenosis, abdominal cystic lymphangioma, abdominal ectopic pregnancy, celiac trunk compression syndrome, pelvic varices) span structural, vascular, and anatomic conditions with no plausible link to toxin neutralization. The rationale text for several candidates explicitly labels them as likely "model noise." This pattern suggests the TxGNN score cluster here reflects an embedding-space artifact rather than a real pharmacological signal, and should be weighted accordingly.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

Bezlotoxumab is not currently marketed in Finland (market status: not marketed), and there are no marketing authorizations on record (0 total).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high raw TxGNN score, the evidence level is L5 (model prediction only) with no clinical trials, no literature, and no market presence in Finland to draw on. The mechanistic rationale itself assesses the drug-disease link as weak, and this pattern repeats across all 10 top-ranked candidates for bezlotoxumab, indicating the signal cluster is more likely model noise than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001), required before any S1 safety screening
- Confirmed original MOA and indication from an authoritative source (DrugBank API / regulatory label) — currently a High-severity gap (DG002)
- Independent mechanistic or preclinical evidence connecting toxin-B neutralization to pelvic infection pathophysiology
- Any clinical trial, case report, or observational data before this candidate can advance past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

