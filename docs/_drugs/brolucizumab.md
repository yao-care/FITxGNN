---
layout: default
title: Brolucizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 79
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Brolucizumab: From Wet Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Brolucizumab (brand name Beovu) is an anti-VEGF-A antibody fragment originally used via intravitreal injection for wet age-related macular degeneration (AMD).
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but this is a **model-score-only prediction (L5)** with **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as biologically implausible — likely an embedding-similarity false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Wet age-related macular degeneration (AMD) — based on known drug profile; not documented in the Finland regulatory dataset provided |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Finland Market Status | ✗ Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for brolucizumab is not available from DrugBank (blocking data gap). Based on known drug information, brolucizumab is a humanized single-chain antibody fragment (scFv) that inhibits VEGF-A, administered by intravitreal injection for wet AMD — its efficacy in that indication is well established.

The predicted new indication, however, is a nuclear-DNA-related mitochondrial oxidative phosphorylation disorder. There is no known biological pathway overlap between VEGF-A/angiogenesis signaling and mitochondrial energy metabolism. The evidence pack's own mechanistic analysis explicitly flags this: despite the high TxGNN score (99.67%), the rationale states the mechanistic relevance is "extremely low" and that this is likely a high-scoring but biologically unexplainable prediction — possibly a false positive driven by embedding similarity rather than genuine pharmacology.

Three lower-ranked candidates (esophageal varices with/without bleeding, exocrine pancreatic insufficiency) were also predicted with similarly high scores (~99.1%), but each carries its own weakness: brolucizumab's intravitreal-only route of administration is incompatible with systemic or GI exposure needed for those indications, and anti-VEGF agents carry a known bleeding-risk signal that runs counter to a "with bleeding" varices indication. None of the four candidates currently has a defensible mechanistic case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Finland Market Information

No marketing authorizations are currently registered for brolucizumab in Finland (market status: Not marketed / not marketed; total_licenses = 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction has no known mechanistic pathway overlap with brolucizumab's anti-VEGF-A activity, zero supporting clinical trials or literature, and is explicitly flagged in the evidence pack as a likely embedding-driven false positive. Combined with the drug's non-marketed status in Finland, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- DrugBank mechanism-of-action detail (DG002)
- An independent biological-plausibility review of the mitochondrial-disorder prediction, or re-evaluation of lower-score but mechanistically coherent candidates
- If the esophageal-varices signal is pursued instead, a feasibility assessment of systemic/GI drug exposure given brolucizumab's intravitreal-only administration route
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

