---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Fidaxomicin: From Clostridioides difficile Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrocyclic antibiotic whose established use is treating *Clostridioides difficile* infection through gut-restricted (non-systemic) antibacterial activity. The TxGNN model predicts possible efficacy for **Staphylococcal Scalded Skin Syndrome (SSSS)**, but this direction currently has **zero supporting clinical trials and zero publications** (L5, model prediction only), and the accompanying mechanistic analysis in this evidence pack actually argues *against* plausibility, since fidaxomicin has negligible systemic absorption.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridioides difficile* infection (CDI) — based on known drug class/mechanism; no Finland market license data exists to confirm this formally |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome (SSSS) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Finland Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action data for fidaxomicin is not available at the drug-record level (DrugBank MOA field: data gap). However, the evidence pack's own mechanistic rationale fields indicate fidaxomicin is a narrow-spectrum macrocyclic antibiotic that inhibits bacterial RNA polymerase (σ subunit), with activity concentrated against *Clostridium*-related organisms including *C. difficile*. Critically, oral bioavailability is reported as **<0.5%**, meaning the drug acts almost entirely within the gut lumen and does not achieve meaningful systemic circulation.

SSSS is caused by exfoliative-toxin-producing *Staphylococcus aureus* and requires **systemic** anti-staphylococcal antibiotic therapy to control the underlying infection. Given fidaxomicin's near-total lack of systemic absorption, it cannot reach a skin-based staphylococcal infection at therapeutic concentrations — the pharmacokinetic profile is fundamentally mismatched to this indication's requirements. The rationale text accompanying this prediction explicitly states that "the mechanism and PK characteristics do not support this indication."

For context, this same TxGNN batch flags 9 candidate indications for fidaxomicin, and the internal rationale for most of them (bullous impetigo, impetigo, hordeolum, vulvovaginal candidiasis, punctate epithelial keratoconjunctivitis) similarly notes mechanistic mismatch — either wrong pathogen class (e.g., vulvovaginal candidiasis is fungal; fidaxomicin has no antifungal activity) or wrong compartment (skin/eye infections requiring systemic or topical exposure fidaxomicin cannot provide). The one exception flagged as comparatively more plausible is **toxin-mediated infectious botulism** (rank 5), where the proposed mechanism — suppressing intraluminal *Clostridium botulinum* proliferation — parallels fidaxomicin's established gut-restricted anti-*Clostridium* action against *C. difficile*. Even so, that indication has no clinical trial or literature support either. Overall, this batch should be treated as low-confidence model output requiring substantial independent validation before any indication is pursued.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Finland Market Information

Fidaxomicin is not currently marketed in Finland; no Fimea market authorization records exist for this product (total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug-drug interaction data were retrievable for fidaxomicin at this time; a TFDA/Fimea package insert lookup is flagged as a Blocking data gap in this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SSSS) has no clinical or literature support (L5) and its own mechanistic assessment argues against pharmacological plausibility due to fidaxomicin's negligible systemic absorption. Combined with the drug's unmarketed status in Finland and missing MOA/safety documentation, there is insufficient basis to advance.

**To proceed, the following is needed:**
- TFDA/Fimea package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed original mechanism-of-action documentation from DrugBank — High-severity gap (DG002)
- If pursuing further, in vitro/in vivo evidence of systemic or topical anti-staphylococcal efficacy for SSSS, since current PK data contradicts the prediction
- Consider redirecting evaluation toward toxin-mediated infectious botulism (rank 5), which has a mechanistically more coherent rationale (shared *Clostridium* genus, gut-localized action) but still requires de novo preclinical/clinical evidence generation, as none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

