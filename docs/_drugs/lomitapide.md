---
layout: default
title: Lomitapide
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Macrothrombocytopenia With Mitral Valve Insufficiency

## One-Sentence Summary

Lomitapide is a microsomal triglyceride transfer protein (MTP) inhibitor originally approved (as Juxtapid/Lojuxta) for homozygous familial hypercholesterolemia (HoFH). TxGNN's top-ranked new-indication prediction, **macrothrombocytopenia with mitral valve insufficiency**, carries a **99.92% model score** but is currently backed by **zero clinical trials and zero publications** — the signal exists only inside the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Homozygous Familial Hypercholesterolemia (HoFH) — inferred from trial/literature evidence (Juxtapid/Lojuxta); not present in structured `taiwan_regulatory` licensing data |
| Predicted New Indication | Macrothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Finland Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lomitapide's mechanism is well characterized in the underlying trial/literature evidence even though the structured `original_moa` field is a data gap: it inhibits MTP in the liver and intestine, blocking assembly and secretion of apoB-containing lipoproteins (VLDL, chylomicrons), which lowers LDL‑C, apoB and total cholesterol. This is the basis for its approval in HoFH.

Macrothrombocytopenia with mitral valve insufficiency is a rare, largely genetic platelet/connective-tissue disorder. There is no established biological pathway linking MTP-mediated lipoprotein assembly to platelet size regulation or mitral valve structure, and the evidence pack's own rationale explicitly flags this: "無機轉證據。屬罕見遺傳性巨大血小板症候群，與 MTP 抑制無已知關聯，零試驗零文獻，純模型預測" (no mechanistic evidence; a rare hereditary macrothrombocytopenia syndrome with no known relationship to MTP inhibition; zero trials, zero literature, pure model prediction).

This pattern repeats across ranks 1–8 and 10 in this evidence pack — all platelet/coagulation disorders (hereditary thrombocytopenia, dense granule disease, pseudo-von Willebrand disease, Glanzmann thrombasthenia, platelet storage pool deficiency, etc.) score extremely high (>99.5%) with no supporting mechanism, trials, or literature. This clustering, combined with the fact that a mechanistically *sensible* indication (hyperlipoproteinemia — rank 9, which is actually lomitapide's own original approval territory) scores *lower* than these implausible candidates, suggests a knowledge-graph embedding artifact — likely driven by co-occurrence of lipid and hematologic parameters in shared patient records — rather than a genuine pharmacological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Finland Market Information

Lomitapide has no marketing authorizations on file for Finland (0 licenses recorded; market status: not marketed).

## Safety Considerations

Formal safety fields (key warnings, contraindications, drug interactions) are marked as data gaps in the source evidence pack (DG001, Blocking severity) — please refer to the package insert for detailed safety information.

**Note:** Although not captured in the structured `safety` fields, the repurposing-rationale text for a related predicted indication explicitly notes that lomitapide carries a known hepatotoxicity risk and is contraindicated in pregnant and neonatal populations — relevant context for any future evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (macrothrombocytopenia with mitral valve insufficiency) has no mechanistic plausibility, no clinical trials, and no literature support — evidence level L5, decision stage S0. The same holds for 8 of the other 9 ranked candidates in this pack. The only candidate with strong evidence, hyperlipoproteinemia (L1, 12 trials including pivotal Phase 3 studies, 19 publications), is not a genuine repurposing opportunity — it reflects lomitapide's *existing* approved indication (HoFH) resurfacing under a broader disease-ontology term, not a novel use.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data (DG001, Blocking) before any safety evaluation can begin
- Verified DrugBank MOA record (DG002) to properly ground mechanistic-link analysis
- A model/embedding-level audit of why TxGNN concentrates high scores on unrelated platelet/coagulation-disorder nodes for an MTP inhibitor
- If pursuing lipid-adjacent extensions is of interest, evaluate label-adjacent conditions such as familial chylomicronemia syndrome (PMID 36152419) as an off-label extension review — not as a novel repurposing candidate from this prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

