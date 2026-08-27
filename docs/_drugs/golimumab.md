---
layout: default
title: Golimumab
parent: 中證據等級 (L3-L4)
nav_order: 180
evidence_level: L4
indication_count: 5
---

# Golimumab
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Golimumab: From TNF-α抑制的發炎性關節炎 到 Rheumatoid Vasculitis

## 一句話總結

Golimumab（DrugBank DB06674）是一種全人源抗TNF-α單株抗體，文獻資料顯示其原始核准適應症為類風濕性關節炎（RA）、乾癬性關節炎（PsA）與僵直性脊椎炎（AS）等發炎性關節疾病；台灣官方適應症全文因未上市而無資料。TxGNN模型預測其可能對**Rheumatoid Vasculitis（類風濕性血管炎）**有效，目前僅有**3項臨床試驗**與**6篇文獻**支持，且證據等級偏弱（L4），文獻中同時存在anti-TNF誘發血管炎的矛盾安全性訊號。

> 補充說明：本Evidence Pack中TxGNN共預測5項適應症，其中排名第3（inflammatory spondylopathy）與第5（polyarticular juvenile rheumatoid arthritis）證據等級達L1，但這兩者實質上是golimumab既有核准適應症的延伸族群，而非真正意義上的老藥新用；排名第2、第4（尾骨過度活動、Kummell氏病）則缺乏任何機轉或臨床證據支持，判定為模型層級偽陽性。本報告依格式規範聚焦於排名第1之預測結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（台灣未上市，無官方適應症全文；依文獻，golimumab已知核准用於RA、PsA、AS） |
| 預測新適應症 | Rheumatoid Vasculitis |
| TxGNN預測分數 | 99.73%（rank 3425） |
| 證據等級 | L4 |
| 台灣市場狀態 | ✗ 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

## 為何此預測具有合理性？

目前缺乏詳細的作用機轉（MOA）資料。根據已知資訊，golimumab屬於抗TNF-α全人源單株抗體類別，其於RA、PsA、AS等發炎性關節疾病之療效已獲證實，機轉上理論上可延伸應用於rheumatoid vasculitis。

Rheumatoid vasculitis是RA的嚴重關節外併發症，好發於血清陽性（RF/anti-CCP陽性）病人，病理機轉牽涉TNF-α介導之血管壁發炎與免疫複合體沉積。由於golimumab抑制TNF-α訊號、已證實可改善RA關節破壞（PMID 31491879, 36項RCT網絡統合分析），理論上抑制TNF-α也可能減緩血管壁發炎程度，此為機轉延伸的合理性基礎。

然而，證據並非單向支持：文獻同時記錄anti-TNF治療與新發或惡化血管炎的矛盾訊號，例如Takayasu's arteritis在抗TNF治療下發生的案例報告（PMID 22999907），以及golimumab治療下併發嚴重感染性關節炎的個案（PMID 29075910）。此矛盾訊號屬已知的anti-TNF-induced vasculitis安全性議題，使機轉關聯方向不明確，且目前並無針對rheumatoid vasculitis此疾病本身設計的介入性療效試驗。

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 評估風濕科病人肩關節置換術前免疫抑制劑（含TNF抑制劑）停藥時程對疾病復發、疼痛、傷口併發症之影響，非血管炎特異性療效試驗 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 已完成 | 184 | 多國非介入性研究，評估Tocilizumab於RA病人（對DMARD或一種生物製劑反應不佳者）的臨床實務模式、療效與安全性，對象為RA整體而非血管炎特異性 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 狀態不明 | 750,000 | 大型資料庫研究評估biologics與免疫抑制劑治療下續發其他免疫介導發炎疾病（IMID）之風險，含血管炎類事件安全性訊號，屬觀察性研究非療效試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | RCT/Cohort | International Journal of Molecular Sciences | 36項RCT網絡統合分析，比較5種TNF抑制劑（含golimumab）對RA關節破壞之抑制效果，證實其抗發炎療效基礎 |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | 回顧風濕疾病生物製劑治療現況與限制，包含TNF抑制劑類藥物的整體療效與安全性框架 |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Seminars in Arthritis and Rheumatism | 探討RA病人併發末期腎病（ESRD）之發生率、成因與治療現況 |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatology International | RA病人接受golimumab治療期間併發壞疽性膿皮症與化膿性關節炎導致嚴重敗血症之個案 |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | 2例在抗TNF治療下發生Takayasu's動脈炎之個案報告，提示anti-TNF誘發血管炎的矛盾安全性訊號 |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocular Immunology and Inflammation | Golimumab成功治療Behçet氏病相關葡萄膜炎之個案報告 |

## 台灣市場資訊

目前無許可證紀錄——golimumab未於台灣上市（總許可證數：0）。

## 安全性考量

請參閱仿單警語與注意事項。（key_warnings、contraindications、DDI查詢皆無可用資料；TFDA仿單原文尚待解析，列為DG001阻斷性資料缺口。）

## 結論與後續建議

**決策：Hold**

**理由：**
Rheumatoid vasculitis此適應症目前僅達L4證據等級（機轉/臨床前推論層級），無疾病特異性介入性試驗，且文獻同時存在anti-TNF誘發血管炎之矛盾安全訊號，機轉關聯方向不明確，尚不足以支持進入下一階段評估。

**要繼續進行，需要補充：**
- TFDA仿單警語與禁忌全文（DG001，阻斷性缺口，影響S1安全性初評）
- Golimumab詳細作用機轉資料（DG002，影響機轉關聯性分析）
- 針對rheumatoid vasculitis之疾病特異性介入性試驗設計與結果
- Anti-TNF誘發血管炎風險之系統性安全性評估，以釐清機轉方向的矛盾訊號
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

