---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Bupivacaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is an amide-type local anesthetic that blocks voltage-gated sodium channels to suppress nerve conduction, used clinically for local and regional anesthesia. The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans**, a chronic skin condition caused by *Borrelia burgdorferi* infection, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic assessment finds no plausible biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (amide-type local anesthetic; specific approved indication text not available) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Finland Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form for this candidate. Based on the mechanistic assessment included with the prediction, bupivacaine is an amide-type local anesthetic whose established pharmacology is blockade of voltage-dependent sodium channels, suppressing neural conduction for local/regional anesthesia.

Acrodermatitis chronica atrophicans, by contrast, is a late-stage cutaneous manifestation of chronic *Borrelia burgdorferi* infection, driven by chronic inflammation and abnormal collagen metabolism leading to skin fibrosis and atrophy. There is no established pharmacological pathway connecting sodium-channel blockade to the inflammatory/fibrotic processes underlying this disease.

The evidence pack's own rationale for this prediction explicitly states that no credible mechanistic pathway can be established given the absence of original MOA documentation, and that the score should be treated as a pure TxGNN embedding-similarity output rather than a biologically grounded hypothesis. Three additional candidate indications (neonatal dermatomyositis, childhood interstitial lung disease secondary to connective tissue disease, and amyopathic dermatomyositis) were also evaluated for bupivacaine at similarly high TxGNN scores (99.0–99.15%), and each carries the same conclusion — no known immunomodulatory, antifibrotic, or disease-relevant pharmacology, and no supporting trials or literature. Two of these (neonatal and childhood-onset conditions) additionally raise safety concerns given bupivacaine's known cardiotoxicity and reduced clearance in neonates/infants.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Finland Market Information

No marketing authorizations for bupivacaine were found in this market (total authorizations: 0; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Package insert warnings/contraindications and drug interaction data for this candidate are flagged as a Blocking data gap (DG001) and have not yet been retrieved — this must be resolved before any S1 safety review can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has evidence level L5 (model prediction only) with zero supporting clinical trials or literature, and the mechanistic rationale itself finds no biologically plausible link between bupivacaine's sodium-channel-blocking activity and the fibrotic/inflammatory pathology of acrodermatitis chronica atrophicans. Combined with the drug's non-marketed status and missing safety documentation, there is currently no basis to advance this candidate beyond model prediction.

**To proceed, the following is needed:**
- TFDA/Fimea package insert data on warnings, contraindications, and drug interactions (DG001, Blocking)
- Confirmed original MOA and approved indication text from DrugBank (DG002, High)
- A biologically grounded mechanistic hypothesis linking bupivacaine to the target disease before further evidence collection is warranted
- Re-screening of the other three co-predicted candidates (neonatal dermatomyositis, childhood ILD-CTD, amyopathic dermatomyositis) is not recommended given their similarly unsupported rationale and, for the pediatric indications, added safety risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

