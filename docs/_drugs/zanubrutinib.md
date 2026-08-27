---
layout: default
title: Zanubrutinib
parent: 中證據等級 (L3-L4)
nav_order: 409
evidence_level: L4
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **6** 個
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

# Zanubrutinib：從 B 細胞惡性腫瘤到骨髓性白血病（Myeloid Leukemia）的探索

## 一句話摘要

Zanubrutinib 是第二代 BTK（Bruton's tyrosine kinase）抑制劑，目前已知藥理用途為 CLL/SLL、MCL、Waldenström 巨球蛋白血症等 **B 淋巴系**惡性腫瘤治療。TxGNN 模型預測其可能對**骨髓性白血病（Myeloid Leukemia）**有效，預測分數高達 99.65%，但目前僅有 **2 篇臨床試驗**（皆非 zanubrutinib 本身的直接證據）與**間接文獻**支持，機轉關聯性薄弱，證據等級為 L4。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | CLL/SLL 等 B 細胞惡性腫瘤（依已知藥理用途整理，本 Evidence Pack 未提供正式核准適應症清單） |
| 預測新適應症 | 骨髓性白血病（Myeloid Leukemia） |
| TxGNN 預測分數 | 99.65%（rank 4274） |
| 證據等級 | L4 |
| 芬蘭市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測值得關注（或存疑）？

目前 DrugBank 未提供正式結構化的機轉描述（MOA 欄位為資料缺口）。根據已知公開資訊，Zanubrutinib 為第二代 BTK 抑制劑，藥理作用是阻斷 B 細胞受體（BCR）訊號傳導，已證實用於 CLL/SLL、MCL、Waldenström 巨球蛋白血症等 B 淋巴系惡性腫瘤治療，相較第一代 ibrutinib 具有更高的激酶選擇性、較少脫靶效應。

骨髓性白血病（AML）屬於**髓系**而非淋巴系腫瘤，其致病驅動路徑（如 FLT3-ITD、NPM1、IDH1/2 等突變）與 BTK 訊號並無明確重疊。BTK 在髓系細胞中的角色證據薄弱，僅見於巨噬細胞/肥大細胞的次要訊號路徑，並非驅動 AML 致病的主要激酶。本次證據包中的兩項臨床試驗（NCT05665530、NCT04477291）受試藥物分別為 PRT2527（CDK9 抑制劑）與 CG-806（多激酶抑制劑），均**非 zanubrutinib 本身**，僅屬「激酶抑制劑治療血液腫瘤」的類別類比，相關性評級皆為 C。

因此，TxGNN 的高分很可能反映的是知識圖譜中「激酶抑制劑」這一藥物類別與 AML 節點的拓樸鄰近性，而非 zanubrutinib 分子本身的特異性證據。此結論也與其他 5 個較低排序的預測（如罕見遺傳症候群、神經母細胞瘤、尤文氏肉瘤等）一致——這些預測均無臨床試驗或文獻支持，被歸類為 Hold，顯示 TxGNN 對此藥物在髓系腫瘤/實體瘤方向的預測整體證據薄弱。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | 評估 PRT2527（CDK9 抑制劑）單獨或併用 zanubrutinib/venetoclax 治療復發/難治血液腫瘤之安全性與初步療效；**受試藥物非 zanubrutinib 本身**，僅為併用臂之一，相關性 Grade C |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/b | Terminated | 45 | 評估口服 CG-806（luxeptinib，多激酶抑制劑）治療復發/難治 AML 或高風險 MDS 之安全性與抗腫瘤活性；**未使用 zanubrutinib**，試驗已終止，僅提示同類機轉假說，相關性 Grade C |

> 兩項試驗皆非 zanubrutinib 治療骨髓性白血病的直接證據，僅供機轉類比參考。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 試驗（Phase 3）5 年追蹤更新：zanubrutinib 對比 BR 方案治療初治 CLL/SLL 之療效 |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | BGB-3111-215 研究更新：zanubrutinib 於 ibrutinib/acalabrutinib 不耐受 CLL/SLL 患者中安全有效 |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 單臂研究：zanubrutinib 用於先前 BTK 抑制劑不耐受之 B 細胞惡性腫瘤患者 |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Review | Blood Advances | 跨臨床研究分析 zanubrutinib 於 del(17p)/TP53 突變 CLL/SLL 患者之療效與安全性 |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | 慢性白血病（CML、CLL）之酪胺酸激酶抑制劑時代綜述 |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | BTK 抑制劑於 Waldenström 巨球蛋白血症治療管理 |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | BTK 抑制劑（含 zanubrutinib）治療患者之 B 型肝炎再活化風險探討 |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | FDA 核准抗癌藥物合成方法學綜述，僅提及 zanubrutinib 化學合成 |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case Report | Front Immunol | Waldenström 巨球蛋白血症合併 B-ALL 之罕見病例報告（KMT2D/MECOM 突變） |

> 以上文獻皆聚焦於 zanubrutinib 在 **B 細胞**惡性腫瘤（CLL/SLL、WM）的療效與安全性，**無一篇針對骨髓性白血病（AML）**，僅供藥物背景與安全性參考。

---

## 芬蘭市場資訊

Zanubrutinib 目前於芬蘭尚未取得上市許可（未上市，許可證數量 0），無可列示之核准藥品項目。

---

## 細胞毒性資訊（標靶治療藥物參考）

Zanubrutinib 屬於 B 細胞惡性腫瘤治療用藥，依已知藥理分類為標靶治療藥物，故列出以下參考資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶治療（BTK 抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考仿單警語與注意事項 |
| 致吐性分類 | 請參考仿單警語與注意事項 |
| 監測項目 | 請參考仿單建議之監測項目 |
| 處置防護 | 請參考仿單警語與注意事項 |

---

## 安全性考量

請參考仿單以獲取安全性資訊。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.65%），但支持證據皆非 zanubrutinib 於骨髓性白血病的直接證據——兩項臨床試驗受試藥物均非 zanubrutinib，文獻證據全數聚焦於 B 細胞惡性腫瘤而非髓系腫瘤；機轉上 BTK 亦非 AML 之主要驅動路徑。同時芬蘭未上市、無正式安全性資料，尚不足以支持進入下一階段評估。

**若要繼續推進，需要補充：**
- Zanubrutinib 正式的作用機轉（MOA）結構化資料（DrugBank）
- TFDA/Fimea 官方仿單警語與禁忌資料
- 針對 zanubrutinib 於髓系腫瘤（AML/MDS）之直接臨床前或臨床證據
- 藥物交互作用（DDI）完整資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

