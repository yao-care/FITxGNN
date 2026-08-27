---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine：原始適應症資料缺失，預測新適應症為 Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)

## 一句話摘要

Capecitabine 為口服氟嘧啶類化療前驅藥；本證據包未取得其正式核准之原始適應症資料（Data Gap），但依證據包內其他預測適應症之機轉論述，capecitabine 於體內轉換為 5-FU 後經抑制 thymidylate synthase 產生細胞毒性，是 XELOX／CAPOX 等方案之標準化療骨幹藥物。TxGNN 模型將 **Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)** 列為預測分數最高的新適應症（99.94%），但目前**沒有任何臨床試驗或文獻**支持此用途，屬純模型預測。

## 重點總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無資料（本證據包未記錄核准適應症，屬資料缺口） |
| 預測新適應症 | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 台灣市場狀態 | 未上市 |
| 藥證數量 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前尚無詳細的作用機轉（MOA）資料可供引用（DG002，High severity，待透過 DrugBank API 補齊）。根據本證據包中其他胃癌亞型預測適應症的機轉論述，capecitabine 是口服氟嘧啶類化療前驅藥，於體內轉換為 5-FU 後透過抑制 thymidylate synthase 阻斷 DNA 合成，屬 XELOX、CAPOX 等方案的標準化療骨幹藥物之一。

然而，針對此次排名第一的預測適應症 GAPPS，證據包內的機轉論述明確指出：GAPPS 為體質性 APC 啟動子 1B 突變引起的遺傳性息肉症候群，臨床處置以預防性胃切除或內視鏡監測為主，並非化療適應症；**無任何試驗或文獻支持 capecitabine 於此族群之用途，純屬 TxGNN 分子相似性預測**。

值得注意的是，本證據包同批預測適應症中，第 3、5、8 名（gastric tubular adenocarcinoma、gastric cardia adenocarcinoma、gastric body carcinoma）皆已累積多筆 Phase 2/3 試驗與文獻證據，達到 L1／Proceed with Guardrails，機轉關聯性遠高於 GAPPS。相較之下，GAPPS 屬於低機轉相關性、無實證支持的預測結果。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻資料

## 台灣市場資訊

本藥品於台灣尚未上市（未上市狀態，藥證數量 0），無核准藥證與適應症文字可供摘錄。

## 細胞毒性

Capecitabine 屬氟嘧啶類（fluoropyrimidine）口服細胞毒性化療藥物，符合抗腫瘤藥物認定標準，故列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | Conventional cytotoxic（氟嘧啶類，口服 5-FU 前驅藥） |
| 骨髓抑制風險 | 請參閱仿單警語與注意事項（本證據包未提供具體毒性數據） |
| 致吐性分級 | 請參閱仿單警語與注意事項 |
| 監測項目 | CBC（含白血球分類）、肝腎功能、電解質 |
| 處置防護 | 應依細胞毒性藥品調配與處置相關規範辦理 |

## 安全性考量

請參閱仿單以獲取安全性資訊。

## 結論與後續步驟

**決策：Hold**

**理由：**
GAPPS 目前完全無臨床試驗或文獻證據支持，其標準治療為手術／內視鏡監測而非全身性化療，與 capecitabine 之細胞毒性化療機轉關聯性低；99.94% 之分數純為 TxGNN 分子相似性預測，證據等級僅 L5，不具備進入下一階段安全性評估之基礎。

**若要推進，需要補齊：**
- TFDA 仿單警語／禁忌資料（DG001，Blocking，需下載仿單 PDF 並解析）
- 作用機轉（MOA）資料（DG002，High，需查詢 DrugBank API）
- GAPPS 相關前瞻性試驗或病例系列證據（目前為零）
- 若欲推進本藥物之老藥新用評估，建議改以證據等級較高之胃癌亞型（如 gastric cardia adenocarcinoma、gastric body carcinoma、gastric tubular adenocarcinoma，皆達 L1／Proceed with Guardrails）另案處理
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

