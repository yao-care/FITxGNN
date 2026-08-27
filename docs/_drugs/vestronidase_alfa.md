---
layout: default
title: Vestronidase Alfa
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Vestronidase Alfa：從 Mucopolysaccharidosis VII（Sly 症候群）到 Scheie 症候群

## 摘要

Vestronidase alfa（重組人類 β-glucuronidase, GUS）為第七型黏多醣症（MPS VII, Sly 症候群）之酵素替代療法，目前於美國、歐盟已核准上市。TxGNN 模型預測其可能對 **Scheie 症候群**（MPS I 最輕型亞型）有效，預測分數 **99.90%**，但目前**沒有任何臨床試驗或文獻證據**支持此連結，且兩病致病酵素完全不同。

## 總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | Mucopolysaccharidosis VII（MPS VII, Sly 症候群）※台灣法規資料庫無正式許可證紀錄，此項出自佐證文獻，非 TFDA 仿單原文 |
| 預測新適應症 | Scheie 症候群（MPS I 輕型） |
| TxGNN 預測分數 | 99.90%（排名 1529） |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻支持） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | **Hold（不建議推進）** |

## 這個預測合理嗎？

本證據包中正式的作用機轉欄位標示為資料缺口（DG002），但佐證文獻（PMID 30467742）明確指出：vestronidase alfa 是重組人類 β-glucuronidase（GUS），用於補充 MPS VII 患者因 GUS 缺陷而無法分解的 glycosaminoglycans（GAGs），已於美國與歐盟核准用於 MPS VII 治療。

Scheie 症候群屬於 MPS I 的最輕型亞型，其致病酵素缺陷為 **α-L-iduronidase（IDUA）**，而非 GUS。兩者雖同屬黏多醣症家族、臨床表現上都有骨骼與結締組織受累的相似性，但致病酵素路徑完全不同——補充 GUS 無法代償 IDUA 缺陷，機轉上不成立。

TxGNN 的高分很可能反映的是知識圖譜中「MPS 疾病群組」表型相似性造成的模型偏誤，而非真正藥理學上的合理性。此預測目前無任何臨床試驗或文獻直接支持，應視為純模型假說。

## 臨床試驗證據

目前無相關已註冊之臨床試驗。

## 文獻證據

目前無相關文獻。

## 台灣市場資訊

Vestronidase alfa 在台灣未上市，無許可證紀錄可列示。

## 安全性考量

請參閱藥品仿單以獲取安全性資訊（TFDA 仿單警語/禁忌屬關鍵資料缺口 DG001，Blocking 等級，尚未取得）。

## 結論與後續建議

**決策：Hold（不建議推進）**

**理由：**
此預測缺乏任何臨床試驗或文獻證據（證據等級 L5、決策階段 S0），且致病酵素機轉與原藥物補充酵素不對應，判斷為知識圖譜相似性雜訊，不具備推進至下一階段的證據基礎。

**若欲繼續推進，需補充：**
- TFDA 仿單警語與禁忌症資料（DG001，Blocking，須先完成才能進行 S1 安全性初評）
- 正式作用機轉（MOA）文件（DG002，High）
- Scheie 症候群相關體外/體內機轉驗證研究，確認 GUS 補充對 IDUA 缺陷是否存在任何代償路徑
- 建議優先評估本證據包中證據等級較高的候選適應症——**Hurler syndrome**（rank 3，L3，decision_stage S1，已有 1 篇 Phase 1 試驗 NCT04532047），其證據基礎明顯優於 Scheie 症候群
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

