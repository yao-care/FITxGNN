---
layout: default
title: Lecanemab
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 0
---

# Lecanemab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Lecanemab：阿茲海默症 — 老藥新用預測資料待補

## One-Sentence Summary

Lecanemab（品牌名 Leqembi）是一種人源化抗類澱粉蛋白 β（Aβ）單株抗體，目前核准適應症為早期阿茲海默症（輕度認知障礙／輕度癡呆）。
本次 Evidence Pack 中 **TxGNN 預測結果為空**，且監管安全性資料尚未完整擷取，無法進行標準的老藥新用潛力評估。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 早期阿茲海默症（Mild Cognitive Impairment / Mild Alzheimer's Dementia） |
| Predicted New Indication | 尚無 — 本 Evidence Pack 未含 TxGNN 預測 |
| TxGNN Prediction Score | 不適用 |
| Evidence Level | 無法評估 |
| Taiwan Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

目前 Evidence Pack 中 MOA 欄位未填入，但根據已公開的藥理文獻，Lecanemab 的作用機轉已相當明確：

Lecanemab 優先結合可溶性 Aβ **原纖維（protofibrils）**，透過促進免疫清除減少腦內類澱粉斑塊負荷，進而減緩阿茲海默症神經退行性進程。此機轉不同於過去以 Aβ 單體或不可溶性斑塊為標靶的抗體（如 aducanumab），使其在 CLARITY AD Phase 3 試驗中顯示出統計學上顯著的認知功能延緩效果（CDR-SB 減緩 27%）。

由於 **predicted_indications 陣列為空**，本報告無法對新適應症進行機轉關聯性分析。在 TxGNN 知識圖譜補齊 Lecanemab 節點資料之前，任何「從阿茲海默症到 X 疾病」的預測均不具備資料基礎，不應進行推斷。

---

## Taiwan Market Information

台灣目前無任何 Lecanemab 核准授權紀錄（查詢日期 2026-03-29）。

美國 FDA 已於 2023 年 7 月給予 Leqembi 完全核准（Biologics License Application），適應症為早期症狀性阿茲海默症。台灣審查進度尚待 TFDA 官網最新公告。

---

## Safety Considerations

TFDA 仿單安全性資料擷取作業尚未完成（見資料缺口 DG001）。根據 FDA 核准仿單及已發表臨床資料，以下為已知關鍵安全警示，供評估參考：

- **關鍵警告：ARIA（Amyloid-Related Imaging Abnormalities）**
  - ARIA-E（腦水腫 / 腦溝積液）及 ARIA-H（腦微出血 / 含鐵血黃素沉積）為最重要安全訊號，CLARITY AD 試驗中 ARIA-E 發生率約 12.6%，ARIA-H 約 17.3%。
  - ApoE ε4 純合子攜帶者風險顯著升高，建議治療前進行基因型篩查。
  - 需定期以 MRI 監測。
- **抗凝血劑合併使用**：出血風險增加，應謹慎評估。
- **嚴重過敏 / 輸注相關反應**：約 26% 患者在靜脈輸注時發生，多為輕中度。

> 完整禁忌症與警語請待 TFDA 仿單 PDF 解析完成後補充。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence Pack 缺少 TxGNN 預測輸出（`predicted_indications` 為空），且兩項關鍵資料缺口（DG001 安全性仿單、DG002 MOA）尚未解除，目前無法對任何新適應症進行有效評估。

**To proceed, the following is needed:**

- **\[DG001 — Blocking\]** 從 TFDA 官網下載 Lecanemab 仿單 PDF 並解析警語／禁忌症，以完成 S1 安全初評
- **\[DG002 — High\]** 補齊 DrugBank MOA 資料（DB14580），確認 Aβ protofibrils 結合機轉在知識圖譜中的節點連結
- **\[Pipeline\]** 確認 TxGNN 預測管線是否已納入 Lecanemab 節點；若 KG 中缺乏足夠邊（edges），需先補充疾病–靶點–藥物三元組後重新執行預測
- **\[Regulatory\]** 追蹤 TFDA 審查進度；若台灣尚無 Lecanemab 核准，需確認資料引用是否改以 FDA／EMA 仿單為準
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

