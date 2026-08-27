---
layout: default
title: Cholic Acid
parent: 中證據等級 (L3-L4)
nav_order: 101
evidence_level: L4
indication_count: 10
---

# Cholic Acid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Cholic Acid：從膽酸合成障礙（未確認）到 HIV 感染症的探索性訊號

## 一句話摘要

Cholic acid（DrugBank ID: DB02659）在本證據包中未提供正式的原始適應症與作用機轉（MOA）資料；但由 rank 5 預測項目所附文獻與試驗（如 Cholbam® 患者登錄研究 NCT03115086）可推知其於臨床上實際用於**膽酸合成障礙（Bile Acid Synthesis Disorder）**。TxGNN 模型將本藥物排名第一的預測適應症指向 **HIV 感染症**，預測分數達 **99.79%**，但支持證據僅有 **9 篇文獻**、**無任何登記中的臨床試驗**，且其中一篇研究顯示其衍生物反而**促進** HIV-1 病毒複製，證據方向並不一致。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 膽酸合成障礙（依文獻脈絡推得，非結構化藥物資料中之正式記載） |
| 預測新適應症 | HIV infectious disease |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L4 |
| 芬蘭市場狀態 | 未上市 |
| 授權證號數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測有其道理？

目前無法取得 cholic acid 詳細作用機轉（MOA）資料。根據本證據包內可查得的脈絡，cholic acid 是一種初級膽酸，已知用於膽酸合成障礙（如市售品 Cholbam®，見 rank 5 預測項目所附之 NCT03115086 患者登錄研究與 PMID 35392794），其在體內主要透過負回饋調節 CYP7A1 影響膽固醇/膽酸代謝路徑。這與本次排名第一的預測適應症「HIV 感染症」在生理機轉上並無直接關聯。

支持 HIV 感染症此一預測的文獻，主要來自 1990 年代針對含 sodium cholate 之陰道殺精/抗菌海綿（如 Protectaid）的體外研究，顯示 cholic acid 對 HIV-1 逆轉錄酶有劑量依賴性抑制效果（PMID 7688380）。然而，另一篇 2006 年研究（PMID 16610808）發現 cholic acid 胺基衍生物**誘發** HIV-1 複製與合胞體形成，方向與治療假說相反。其餘文獻多為愛滋病患使用蛋白酶抑制劑後血漿膽酸濃度改變的觀察性研究，屬相關性資料而非治療性證據。整體而言，此預測目前僅屬模型分數驅動的探索性訊號，缺乏一致的機轉支持與臨床驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | Review | Annals of the New York Academy of Sciences | 討論含 cholic acid 之陰道殺菌海綿作為抗性病屏障法，屬綜述性質，無 HIV 治療原始數據 |
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro（負向結果） | Journal of Medicinal Chemistry | Cholic acid 胺基衍生物意外**誘發** HIV-1 複製與 T 細胞合胞體形成，與抗病毒假說方向相反 |
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | In vitro/Preclinical | Human Reproduction | Sodium cholate 展現劑量依賴性殺精及 HIV-1 逆轉錄酶體外抑制效果，為 Protectaid 海綿設計基礎 |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust N Z J Obstet Gynaecol | 綜述各類避孕/性病防護方法，未針對 cholic acid 提供臨床數據 |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | 綜述屏障式避孕法對性病/HIV 防護效果，保險套證據最充分，未涉及 cholic acid 臨床數據 |
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Review | Hepatology | 討論 HIV 患者因抗反轉錄病毒藥物交互作用被排除於 NASH 新藥試驗，非探討 cholic acid 對 HIV 之療效 |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Observational Cohort | Pharmacotherapy | HIV 患者接受蛋白酶抑制劑治療時血漿膽酸濃度改變，探討與肝毒性關聯，屬相關性而非治療性證據 |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | In vitro（病毒滅活） | Lancet | TNBP/sodium cholate 用於血液製劑之病毒滅活（HBV/HTLV-III），非全身性抗病毒治療 |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | Methodology/Assay artifact | ChemMedChem | 顯示界面活性劑 Triton X-100 會扭曲 HIV-1 蛋白酶抑制劑結合力測定，屬方法學提醒，與 cholic acid 本身療效無關 |

---

## 芬蘭市場資訊

Cholic acid 目前在芬蘭**未取得任何上市授權**（授權證號數量：0），市場狀態為「未上市」。

---

## 安全性考量

請參閱藥品仿單以取得安全性資訊。

（本證據包之關鍵警語、禁忌症與藥物交互作用查詢均為「[Data Gap]」或「not_found」，且 meta.data_gaps 中 DG001「TFDA 仿單警語/禁忌」被標註為 **Blocking** 等級，直接影響安全性初評可否進行。）

---

## 結論與下一步

**決策：Hold**

**理由：**
排名第一的預測適應症（HIV 感染症）證據等級僅為 L4，且無任何臨床試驗支持，現有文獻方向不一致（甚至有一篇顯示促進病毒複製的負向結果），不足以支持推進。此外，安全性初評所需的仿單警語/禁忌資料（DG001）為 Blocking 等級缺口，在補齊前無法進行任何後續決策。

**若要推進，需要補齊：**
- TFDA／原廠仿單之警語與禁忌症資料（解決 DG001，Blocking 等級）
- DrugBank 作用機轉（MOA）資料（解決 DG002）
- 針對 HIV 感染症之直接體內/臨床藥效證據，以釐清 PMID 16610808 之負向發現是否具代表性
- 補充建議：本證據包 rank 5（vitamin deficiency disorder）項目所附文獻與試驗（NCT03115086、PMID 35392794 等）實際指向 cholic acid 既有臨床用途「膽酸合成障礙」，其證據強度與相關性顯著優於 rank 1 之 HIV 適應症，建議評估團隊優先確認此適應症是否應納入正式老藥新用/新適應症擴充路徑評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

