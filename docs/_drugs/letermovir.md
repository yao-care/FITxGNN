---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: From Cytomegalovirus (CMV) Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is an antiviral drug highly specific to cytomegalovirus (CMV), acting as a terminase complex inhibitor; this evidence pack does not contain a recorded original indication or licensed use. TxGNN predicts it may be effective for **Vulvovaginal Candidiasis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic profile argues against pharmacological plausibility — this is most likely a model-level false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The formal `original_moa` field for letermovir is not populated in this evidence pack, but the model's own rationale describes its mechanism: letermovir is a highly specific inhibitor of the CMV DNA terminase complex (UL56/UL89/UL51). Its antiviral activity is confined to the Herpesviridae family, particularly CMV, and it does not act on any known fungal target — such as ergosterol synthesis or glucan synthase — that would be relevant to *Candida* species.

Vulvovaginal candidiasis is a fungal infection with a biology entirely unrelated to viral DNA packaging. There is no known pharmacological pathway connecting a CMV terminase inhibitor to antifungal activity, and no clinical or preclinical evidence in this pack links letermovir to any fungal indication.

Given this mismatch, the high TxGNN confidence score (99.88%) most plausibly reflects a spurious association in the knowledge-graph embedding space rather than a genuine pharmacological signal. The absence of the drug's original indication and confirmed MOA in structured form (flagged as gaps DG001/DG002) further limits the ability to validate or refute this link with confidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Letermovir is not currently marketed in Taiwan, and no drug licenses were found for this product (0 authorizations on record).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) with zero supporting clinical trials or literature, and the drug's own mechanism of action — a CMV-specific antiviral terminase inhibitor — is not pharmacologically consistent with an antifungal indication. This pattern is consistent with a knowledge-graph false positive rather than a credible repurposing signal.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Original indication and regulatory history for letermovir
- Any preclinical or in vitro data testing antifungal activity, if such data exists, to either support or close out this signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

