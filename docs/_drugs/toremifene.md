---
layout: default
title: Toremifene
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 1
---

# Toremifene
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

# Toremifene: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Toremifene 是一種選擇性雌激素受體調節劑（SERM），原始適應症為乳癌治療（本證據包中原始 MOA 資料缺失，芬蘭市場狀態為未上市）。TxGNN 模型預測其對 **HIV 感染症** 可能有效，目前僅有 **0 篇臨床試驗** 與 **1 篇文獻** 支持此方向，且該文獻探討的是抗真菌機轉而非直接抗病毒機轉，證據強度薄弱。

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 乳癌 (Breast Cancer)（取自 repurposing rationale 敘述，非正式核准適應症欄位；正式仿單資料尚缺，見 DG001） |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Finland Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

目前尚無可用的詳細作用機轉（MOA）資料（DG002，High severity）。根據既有分類資訊，Toremifene 屬於選擇性雌激素受體調節劑（SERM），其乳癌適應症的療效已獲證實，但本證據包中並無正式的原始適應症登記文字或核准仿單可供交叉驗證。

Toremifene 與 HIV 感染症之間並無直接的抗病毒機轉關聯。唯一支持此預測的文獻（PMID 24520056）研究的是雌激素受體拮抗劑（tamoxifen、toremifene）對新型隱球菌（*Cryptococcus neoformans*）EF-hand 蛋白的直接結合能力及抗真菌活性，屬於**抗黴菌機轉**，並非抗反轉錄病毒機轉。隱球菌腦膜炎雖為 HIV/AIDS 病人常見的伺機性感染，但該文獻支持的實際適應症應為「治療 HIV 患者之伺機性隱球菌感染（輔助抗真菌治療）」，而非「直接治療 HIV 病毒感染」。兩者臨床定位不同，TxGNN 高分預測（99.41%）與現有機轉證據之間存在明顯落差，屬於間接、薄弱的推論鏈。

因此，儘管模型分數高，此預測方向的生物學合理性目前僅建立在單一體外機轉研究上，尚不足以支持進入下一階段安全性或臨床評估。

## Clinical Trial Evidence

目前無相關臨床試驗註冊

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Mechanistic (in vitro) | mBio | 雌激素受體拮抗劑（tamoxifen、toremifene）對新型隱球菌具直接殺菌活性，可結合真菌 EF-hand 蛋白，並與 fluconazole、amphotericin B 於體內外實驗中呈現加乘抗真菌效果；未涉及抗 HIV 病毒機轉 |

## Finland Market Information

此藥品於芬蘭目前未上市（0 筆查驗登記），無授權資料可供列出。

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy（荷爾蒙類 SERM，非傳統細胞毒性化療藥物） |
| Myelosuppression Risk | 請參考仿單警語與注意事項 |
| Emetogenicity Classification | 請參考仿單警語與注意事項 |
| Monitoring Items | 請參考仿單警語與注意事項 |
| Handling Protection | 請參考仿單警語與注意事項 |

## Safety Considerations

請參考仿單以取得安全性資訊。

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
目前唯一支持證據為單篇體外抗真菌機轉研究，並非直接抗 HIV 病毒證據，且原始適應症、MOA、TFDA 仿單警語等關鍵資料均缺失（DG001 為 Blocking 等級），無法進行安全性初評，故暫不推進。

**To proceed, the following is needed:**
- 取得 TFDA（或當地主管機關）正式仿單，確認警語與禁忌症（DG001，Blocking）
- 補齊 Toremifene 完整作用機轉資料（DG002，High）
- 釐清此適應症方向應定位為「抗 HIV 病毒治療」或「HIV 患者伺機性隱球菌感染輔助治療」，並據此重新檢索對應臨床試驗與文獻
- 若後續方向確定為伺機性感染輔助治療，需補充與現有抗黴菌藥物（如 fluconazole、amphotericin B）併用之藥物交互作用資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

