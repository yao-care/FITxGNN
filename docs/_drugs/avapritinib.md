---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib：Evidence Pack 資料不足 — 初步缺口評估報告

## 摘要

Avapritinib（DB15233）為一種激酶抑制劑類藥物，目前未於台灣上市。
本 Evidence Pack **未包含任何 TxGNN 預測適應症**，且作用機轉（MOA）及安全性資料均存在關鍵缺口，
**無法執行完整的老藥新用評估**，建議列為 **Hold** 待補齊資料後重新評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | Evidence Pack 中未提供 |
| 預測新適應症 | 本 Pack 無 TxGNN 預測結果 |
| TxGNN 預測分數 | 無 |
| 證據等級 | L5（模型預測層級，但本 Pack 尚無預測輸出） |
| 台灣市場狀態 | ✗ 未上市 |
| 許可證件數 | 0 |
| 建議決策 | **Hold** |

---

## 為何無法進行機轉關聯分析

本 Evidence Pack 缺少以下兩項核心資料，導致機轉–適應症推論無法執行：

目前 Avapritinib 的詳細作用機轉資料不在此 Pack 中（DG002，High severity）。原始適應症欄位亦為空白，無法建立「原始疾病 → 作用機轉 → 預測疾病」的推論鏈。

此外，TxGNN 模型對本藥物**未輸出任何預測適應症**（`predicted_indications: []`），代表此輪評估缺乏老藥新用的候選目標，整份報告的核心分析章節因此無法展開。

---

## 臨床試驗證據

目前無可評估的預測適應症，無對應臨床試驗資料。

---

## 文獻證據

目前無可評估的預測適應症，無對應文獻資料。

---

## 台灣市場資訊

Avapritinib **目前未於台灣取得藥品許可證**。TFDA 查詢（查詢日期：2026-03-29）結果為 0 筆，`taiwan_regulatory.licenses` 為空。

---

## 安全性考量

請參閱藥品仿單之警語與禁忌事項。

> 本 Evidence Pack 的安全性警語、禁忌症及藥物交互作用查詢均未返回有效資料（DDI 查詢狀態：not\_found）。TFDA 仿單警語/禁忌（DG001，**Blocking** 級別缺口）尚待補齊，此缺口將阻擋 S1 安全性初評進行。

---

## 結論與下一步行動

**決策：Hold**

**理由：**
本 Evidence Pack 存在 Blocking 級別資料缺口（DG001：TFDA 仿單警語）及 High 級別缺口（DG002：MOA），且 TxGNN 未產出任何預測適應症，目前不具備執行老藥新用評估的基本條件。

**進入下一階段所需補齊：**

1. **（Blocking）** 補齊 TFDA 仿單 PDF 並解析警語與禁忌事項（DG001）
2. **（High）** 透過 DrugBank API 取得作用機轉（MOA）資料（DG002）
3. **（必要）** 確認 TxGNN 是否已對 DB15233 執行預測，若無請觸發預測流程
4. **（建議）** 確認原始核准適應症（GIST / 全身性肥大細胞增多症等）並填入 `original_indications`
5. **（建議）** 補充藥物交互作用（DDI）資料

---

> ⚠️ **資料完整性警示**
> 本報告為資料缺口分析，非正式的老藥新用評估報告。待上述資料補齊、TxGNN 產出預測適應症後，需重新執行完整報告流程（候選 ID：TW-DB15233-multi，版本 v4，資料截止日：2026-04-20）。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

