---
layout: default
title: Vandetanib
parent: 高證據等級 (L1-L2)
nav_order: 397
evidence_level: L2
indication_count: 10
---

# Vandetanib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Vandetanib：從甲狀腺髓質癌到腎細胞癌

## 一句話摘要

Vandetanib（DrugBank DB05294）為口服多重酪胺酸激酶抑制劑，依證據包內文獻線索原始核准用於**甲狀腺髓質癌（Medullary Thyroid Cancer, MTC）**；TxGNN 模型預測其對**腎細胞癌（Renal Cell Carcinoma）**可能有效，預測分數 **99.92%**，目前有 **4 篇相關臨床試驗**與 **6 篇文獻**支持，但多數試驗提前終止、樣本數偏小，證據強度中等偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 甲狀腺髓質癌（依證據包內文獻佐證推斷；台灣許可證資料缺失） |
| 預測新適應症 | Renal Cell Carcinoma（腎細胞癌） |
| TxGNN 預測分數 | 99.92%（score = 0.99917870759964，rank 1186） |
| 證據等級 | L2 |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為何此預測合理？

證據包中 `original_moa` 欄位標記為資料缺口，目前無正式機轉資料可引用。不過證據包所附文獻本身提供了機轉線索：多篇文獻描述 vandetanib 為口服多重酪胺酸激酶抑制劑，同時抑制 VEGFR2/3、EGFR 及 RET 激酶活性（PMID [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/)、[15886878](https://pubmed.ncbi.nlm.nih.gov/15886878/)、[30860683](https://pubmed.ncbi.nlm.nih.gov/30860683/)）。其在甲狀腺髓質癌的療效即建立於抑制 RET 組成性活化訊號。

腎細胞癌（尤其是 clear cell RCC 及 VHL 疾病相關腎腫瘤）的主要致病機轉為 VHL-HIF-VEGF 路徑失調，導致腫瘤血管新生高度依賴 VEGFR 訊號。此與 vandetanib 的 VEGFR2/3 抑制作用直接重疊，也是目前已核准之 ccRCC 標靶藥物（sunitinib、pazopanib、axitinib）共同的作用機轉家族（class effect）。

因此，vandetanib 用於一般散發型 ccRCC 或 VHL 相關腎腫瘤在機轉上具合理性；但排名 1 的「renal cell carcinoma (disease)」為一個較廣泛的疾病分類，其下同一批預測中還包含 Xp11.2/TFE3 融合型、神經母細胞瘤相關型、未分類型等罕見亞型（rank 2–4、7、9、10），這些亞型的驅動機轉並非 VEGFR/RET 路徑，證據包本身也標註其機轉關聯「屬推論性質」，證據等級僅 L5。故整體預測的機轉合理性主要集中在 ccRCC／VHL 相關族群，而非涵蓋所有 RCC 亞型。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 關鍵發現 |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | 已完成 | 37 | 評估 vandetanib 於 VHL 疾病相關腎腫瘤，為目前唯一完成之直接證據，證據包評級 Grade A |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | 提前終止 | 7 | vandetanib + metformin 用於 HLRCC/SDH 相關腎癌或散發型乳頭狀 RCC；因故提前終止，證據包評級 Grade B |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | 提前終止 | 3 | vandetanib 單藥用於晚期 clear cell RCC；僅收案 3 人即終止，統計力極低，證據包評級 Grade C |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | 已完成 | 82 | 隨機分組評估 carboplatin+gemcitabine ± vandetanib 於不適合 cisplatin 之晚期尿路上皮癌；**證據包已查證此試驗族群為尿路上皮癌而非 RCC，屬資料誤關聯**，不應作為 RCC 直接證據，證據包評級 Grade C |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 關鍵發現 |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Review | Clinical Cancer Research | SDH 缺陷型腫瘤（含 HLRCC 相關 RCC）對細胞毒性化療及多數標靶藥物具抗性 |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clinical & Experimental Metastasis | Fumarate hydratase 缺陷型 RCC（FHdRCC）為 WHO 2022 新分類，尚無標準治療方案，多項標靶合併療法 Phase 2 試驗進行中 |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bulletin du Cancer | 說明同類多重激酶抑制劑（cabozantinib）VEGFR2/c-MET/RET 機轉與腎癌、甲狀腺癌療效關聯 |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Review/Preclinical | Molecular Cancer Research | TFE3-RCC 小鼠模型，鑑定新治療標的與診斷標記，非 VEGFR 驅動之亞型 |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | 未分類 | OncoTargets and Therapy | 綜述抗血管新生藥物（含 vandetanib）於多種實體腫瘤之應用 |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | 未分類 | ASCO Educational Book | 說明 vandetanib 為口服 RET 激酶抑制劑，已獲 FDA 核准用於轉移性甲狀腺髓質癌 |

---

## 台灣上市資訊

依台灣藥政資料，本藥目前**未取得藥品許可證**（`total_licenses = 0`），無許可證明細可列示。

---

## 細胞毒性資訊（僅適用於抗腫瘤藥物）

Vandetanib 原始適應症（甲狀腺髓質癌）與預測新適應症（腎細胞癌）均屬惡性腫瘤，且屬酪胺酸激酶抑制劑（TKI）類別，故列示本節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶治療（Targeted therapy）— 多重酪胺酸激酶抑制劑（VEGFR2/3、EGFR、RET） |
| 骨髓抑制風險 | 證據包內無直接骨髓抑制資料；同類 VEGFR-TKI 之骨髓抑制程度一般低於傳統細胞毒性化療（參考 PMID [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) VEGFR-TKI 致命性不良反應統合分析） |
| 其他已知毒性訊號 | 文獻報告 VEGFR-TKI 類藥物之肝毒性（PMID [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/)）、蛋白尿（PMID [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/)）；另有文獻標題直接示警「Vandetanib: too dangerous in medullary thyroid cancer」（PMID [23185843](https://pubmed.ncbi.nlm.nih.gov/23185843/)），提示安全性疑慮值得重視 |
| 催吐性分類 | 請參考藥品仿單以取得完整資訊 |
| 監測項目 | 肝功能、腎功能／尿蛋白、全血球計數（CBC） |
| 處理防護 | 請依細胞毒性藥品處理規範辦理 |

---

## 安全性考量

證據包中的關鍵警語（`key_warnings`）與禁忌症（`contraindications`）欄位均為資料缺口，藥物交互作用查詢亦為 not_found。

> 請參考藥品仿單以取得完整安全性資訊。

補充：證據包所收錄文獻中有一篇標題為「Vandetanib: too dangerous in medullary thyroid cancer」（PMID [23185843](https://pubmed.ncbi.nlm.nih.gov/23185843/)），顯示既有文獻對此藥安全性已有疑慮，建議正式安全性評估時優先納入查證。

---

## 結論與後續建議

**決策：Hold**

**理由：**
- 唯一完成且直接相關的 Phase 2 試驗（NCT00566995，n=37）僅涵蓋 VHL 疾病相關腎腫瘤，並非一般散發型腎細胞癌族群；其餘試驗均提前終止且樣本數極小（n=3、n=7），或已被證據包本身標註為資料誤關聯（NCT01191892 實為尿路上皮癌）。
- TFDA 仿單警語/禁忌資料為 Blocking 等級缺口（DG001），依規範無法進入 S1 安全性初評；作用機轉資料亦為 High 等級缺口（DG002），影響機轉關聯性判讀的確定性。

**需補齊以推進：**
- 取得 TFDA（或原廠）仿單完整警語、禁忌症與 DDI 資料，解除 DG001 阻斷狀態
- 取得正式 DrugBank/仿單來源之作用機轉（MOA）資料，解除 DG002
- 釐清 NCT00566995 之 VHL 亞群結果能否外推至散發型 ccRCC 一般族群
- 排除 NCT01191892 之尿路上皮癌資料誤關聯後，重新評估直接證據數量是否仍達 L2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

