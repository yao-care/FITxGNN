---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase is a recombinant glucocerebrosidase enzyme replacement therapy, historically used to treat Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome**,
but this direction is currently supported by **0 clinical trials** and only **2 general (non-disease-specific) review publications**, and the underlying mechanistic rationale appears weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (per literature evidence in this pack; no structured regulatory indication text available) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, data gap). Based on the information present in this evidence pack, imiglucerase is a recombinant form of glucocerebrosidase (acid β-glucosidase), used as enzyme replacement therapy (ERT) to break down glucocerebroside accumulated in Gaucher disease.

Hurler syndrome, however, is Mucopolysaccharidosis type I (MPS I), caused by deficiency of α-L-iduronidase (IDUA), an entirely different lysosomal enzyme acting on a different substrate class (heparan/dermatan sulfate, not glucocerebroside). The standard enzyme replacement for Hurler syndrome is laronidase (recombinant IDUA), not imiglucerase.

Given this, the mechanistic link between imiglucerase and Hurler syndrome is weak to absent. The high TxGNN score most likely reflects the model generalizing across the broader "lysosomal storage disease + enzyme replacement therapy" category rather than capturing a substrate-specific pharmacological relationship. This assessment is consistent across the model's other top predictions in this evidence pack (Scheie syndrome, cholesteryl ester storage disease), which show the same pattern — different causal enzymes/substrates, no disease-specific evidence, and a "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | Proceedings of the National Academy of Sciences of the United States of America | Describes PET imaging of enzyme replacement therapy; notes ERT (including imiglucerase-class recombinant lysosomal enzymes) has shown efficacy across Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, and Pompe diseases, but does not present imiglucerase-specific data for Hurler syndrome |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de medecine interne | General overview of ERT for lysosomal storage diseases; describes the historical development of imiglucerase (Cerezyme) for Gaucher disease and other disease-specific ERTs (e.g., agalsidase for Fabry disease); does not address Hurler syndrome specifically |

## Finland Market Information

Imiglucerase currently has no marketing authorization on record in Finland (market status: Not Marketed; 0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted Hurler syndrome indication lacks any disease-specific clinical or literature evidence, and the proposed mechanism does not hold up — imiglucerase targets glucocerebrosidase deficiency (Gaucher disease pathway), while Hurler syndrome is driven by a distinct enzyme deficiency (IDUA) with an established, different standard-of-care (laronidase). Evidence level is L4 (mechanism/model-level only), and the drug is not currently marketed in Finland.

**To proceed, the following is needed:**
- TFDA/official package insert data on warnings and contraindications (DG001, blocking — currently prevents entry into S1 safety review)
- Confirmed mechanism of action data (DG002)
- Disease-specific preclinical or clinical evidence directly linking the glucocerebrosidase pathway to MPS I pathophysiology, if this candidate is to be reconsidered
- Note: all 5 TxGNN-predicted indications in this evidence pack (Hurler syndrome, Scheie syndrome, adrenal adenoma, fatal ichthyosis syndrome, cholesteryl ester storage disease) are currently rated Hold due to similar mechanistic mismatches or absence of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

