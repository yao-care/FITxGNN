---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin：從乳癌／脂肪肉瘤到 Fibroblastic Neoplasm（孤立性纖維瘤）

## One-Sentence Summary

Eribulin（DB08871）為國際上已核准用於轉移性乳癌與無法切除脂肪肉瘤之微管抑制劑，但在台灣尚未取得任何查驗登記許可證（0 張）。TxGNN 對本藥物共預測 10 個新適應症，其中證據強度最高者為 **Fibroblastic Neoplasm（孤立性纖維瘤 / Solitary Fibrous Tumor）**，有 **1 項已完成之 Phase II 臨床試驗**與 **8 篇文獻**支持；其餘候選多屬模型單獨預測（L5），評分最高的家族性地中海熱（FMF）甚至被證據包本身標記為機轉不合理的假陽性。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 台灣尚未查得核准適應症（未上市）；國際已知核准適應症為轉移性乳癌、無法切除之脂肪肉瘤 |
| Predicted New Indication（證據最強候選） | Fibroblastic Neoplasm（孤立性纖維瘤，Solitary Fibrous Tumor） |
| TxGNN Prediction Score | 99.36%（rank 8／全模型 6,643 名） |
| Evidence Level | L3（1 項已完成非隨機 Phase II 臨床試驗 + 多篇臨床前／回顧文獻） |
| 台灣上市狀態 | 未上市 |
| 查驗登記許可證數 | 0 |
| Recommended Decision | Hold |

> 注意：模型評分**最高**之候選為 autosomal recessive familial Mediterranean fever（99.82%），但證據包本身已標註此為「機轉不合理之假陽性」，故不採為本報告主標的，詳見下方多適應症總表。

---

## 多適應症預測總覽

| Rank | 預測適應症 | TxGNN Score | 臨床試驗 | 文獻 | 證據等級 | 判讀 |
|------|-----------|-------------|---------|------|---------|------|
| 1 | Autosomal recessive familial Mediterranean fever | 99.82% | 0 | 0 | L5 | **假陽性**：與 eribulin 微管抑制機轉無生物學關聯 |
| 2 | Dermatofibrosarcoma protuberans | 99.66% | 0 | 1（Review） | L4 | 軟組織肉瘤大類機轉合理，缺乏 DFSP 專一性證據 |
| 3 | Pleural mesothelioma | 99.51% | 0 | 0 | L5 | 僅模型預測，無實證 |
| 4 | Malignant peritoneal mesothelioma | 99.47% | 0 | 0 | L5 | 僅模型預測，無實證 |
| 5 | Ovarian myxoid liposarcoma | 99.47% | 0 | 0 | L4 | 脂肪肉瘤機轉已知，但為卵巢原發罕見變異型，無直接證據 |
| 6 | Pleural adenomatoid tumor | 99.46% | 0 | 0 | L5 | 多屬良性腫瘤，化療介入合理性存疑 |
| **8** | **Fibroblastic neoplasm** | **99.36%** | **1（已完成 Phase II）** | **8** | **L3** | **證據最強，建議列為研究優先** |
| 9 | Pleural epithelioid mesothelioma | 99.35% | 0 | 0 | L5 | 僅模型預測，無實證 |
| 10 | Heart fibrosarcoma | 99.35% | 0 | 0 | L4 | 與 fibroblastic neoplasm 同屬纖維肉瘤家族，可外推但無直接證據 |
| 7 | Pleural biphasic mesothelioma | 99.37% | 0 | 0 | L5 | 僅模型預測，無實證 |

以下章節聚焦於證據最強之候選（Fibroblastic Neoplasm / 孤立性纖維瘤）。

---

## Why is This Prediction Reasonable?

目前尚未取得 eribulin 之詳細作用機轉（MOA）結構化資料（TFDA 仿單解析待補，見 Data Gap DG002）。根據公開已知資訊，eribulin 屬於非紫杉烷類（non-taxane）微管動力學抑制劑（halichondrin B 類似物），其抗腫瘤活性已於乳癌及脂肪肉瘤兩類實體瘤中獲得證實。

Fibroblastic neoplasm（尤其是孤立性纖維瘤 SFT）與 eribulin 原始核准適應症之一「脂肪肉瘤」同屬軟組織肉瘤（soft tissue sarcoma）大家族，具有相近的細胞增殖與微管依賴性生物學特徵。這與義大利肉瘤群組（Italian Sarcoma Group）已針對晚期 SFT 完成之 Phase II 研究（ERASING, NCT03840772）方向一致，顯示 eribulin 在肉瘤家族內的療效外推具一定合理性。

此外，多篇體外／異種移植研究（如 HT1080 人類纖維肉瘤細胞株）顯示 eribulin 對纖維肉瘤細胞具細胞毒性，並探討抗藥性機轉與合併療法（如 methioninase 合併治療）之增效作用，進一步支持機轉層面的可信度，惟目前仍以臨床前及單臂第二期試驗為主，尚缺乏隨機對照試驗（RCT）等級證據。

---

## Clinical Trial Evidence

| 試驗編號 | Phase | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | 義大利肉瘤群組針對晚期孤立性纖維瘤（SFT）之 eribulin 單臂第二期試驗（ERASING study），2024-09 完成 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preclinical | European Journal of Cancer | 病人來源 SFT 異種移植模型顯示對 doxorubicin/dacarbazine 高度敏感，並提示 trabectedin 或 eribulin 之潛在療效 |
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | 孤立性纖維瘤（含 extrameningeal SFT）之診斷與治療現況回顧，涵蓋 NAB2-STAT6 融合基因致病機轉 |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preclinical | Anticancer Research | Recombinant methioninase 與 eribulin 對纖維肉瘤細胞具顯著協同毒殺作用，對正常纖維母細胞無此效果 |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preclinical | Anticancer Research | Methioninase 可使高度抗 eribulin 之 HT1080 纖維肉瘤細胞敏感度提升 16 倍 |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preclinical | In Vivo | 超級抗 eribulin 之 HT1080 細胞株惡性度升高，但可經 methionine 限制併用 eribulin 於裸鼠模型中協同抑制 |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Preclinical | Human Cell | 建立新型黏液纖維肉瘤（MFS）細胞株 SMU-MFS，供化療反應性研究使用 |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Preclinical | Human Cell | 建立黏液纖維肉瘤病人來源細胞株 NCC-MFS4-C1，MFS 對化療普遍具抗藥性 |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Case report | Genes, Chromosomes & Cancer | 惡性周邊神經鞘瘤（MPNST）病例合併 NTRK3 融合基因，對 entrectinib 反應顯著（與 eribulin 非直接相關，僅供肉瘤標靶治療脈絡參考） |

---

## Finland / 台灣市場資訊

目前台灣尚未有 eribulin 之查驗登記許可證（未上市，0 張），無可列示之核准劑型與適應症資料。

---

## Cytotoxicity

Eribulin 屬於化學治療用之細胞毒性抗腫瘤藥物（微管抑制劑類），符合本節適用條件。

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic（非紫杉烷類微管動力學抑制劑，halichondrin B 類似物） |
| Myelosuppression Risk | 請參考仿單警語及注意事項（毒性分級資料尚未取得） |
| Emetogenicity Classification | 請參考仿單警語及注意事項（分級資料尚未取得） |
| Monitoring Items | 請參考仿單警語及注意事項 |
| Handling Protection | 屬細胞毒性化療藥物，應依細胞毒性藥品處理相關規範辦理防護 |

---

## Safety Considerations

請參考仿單資訊以確認安全性（TFDA 仿單警語、禁忌及藥物交互作用資料目前均為缺口，DG001 列為 Blocking 等級）。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TFDA 仿單警語／禁忌資料為 Blocking 等級缺口（DG001），依規範無法完成 S1 安全性初評；且本藥於台灣尚未上市（0 張許可證）。雖然 Fibroblastic Neoplasm（孤立性纖維瘤）候選有 1 項已完成之 Phase II 臨床試驗與多篇機轉支持文獻，證據等級達 L3，但其餘 9 個預測適應症證據薄弱，多為模型單獨預測（L5），其中評分最高之 FMF 已被證據包本身標記為機轉不合理之假陽性，不應優先投入資源。

**To proceed, the following is needed:**
- 補齊 TFDA 仿單解析資料（DG001，Blocking）以完成 S1 安全性初評
- 補齊 DrugBank MOA 結構化資料（DG002）以強化機轉關聯性分析
- 追蹤 NCT03840772（ERASING study）正式發表結果，確認 SFT 適應症之療效訊號
- 針對 L5 等級候選（FMF、間皮瘤系列、pleural adenomatoid tumor）建議降低優先序或排除，避免資源錯置
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

