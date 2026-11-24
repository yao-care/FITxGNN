# FITxGNN - Claude CLI 使用指引

本 repo 的維運以母 repo（yao-care/txgnn）CLAUDE.md 為準；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用芬蘭文，依據是 EMA 集中許可（medicines output report）；在地字樣集中在 `src/fitxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/fitxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/fitxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `scripts/sync_license_tables.py`（程式表前後有 `<!-- licenses:begin/end -->` 標記，2026-11-24 起）、`snapshots/fi_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/fitxgnn/regulatory/licenses.py` | 快照存事實層、本藥號碼與程式表列；gate 依快照驗程式區塊、市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 17–20、22 項 | 紀錄都已套用、許可證＝快照（含程式表）、頁首＝主預測等級、撤回預測沒有對外發布、正文張數＝程式改寫結果 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 正文裡跟許可證事實矛盾、直接刪掉的子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 555 筆紀錄（300 頁；
其中 0 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
2026-11-12 正文許可證張數／狀態對事實層的掃描，以 11 筆 `fi-lic-20261112-*` 更正 9 頁：crizotinib、ramucirumab（表格與決策理由寫芬蘭許可已失效）、mometasone、pioglitazone、vildagliptin（寫另幾張已撤銷）、anagrelide、bictegravir、leflunomide、tezacaftor（下一步以「已撤銷的許可」為前提）；EMA 資料這些都是 Authorised。另有約 215 頁、313 列許可證表格把 Authorised 的產品標成 peruutettu／mitätöity（母目錄 checker 的表格列狀態檢查只對 Us 生效），未在這次處理。
2026-11-12 許可證表格列狀態：311 列（213 頁）把 EMA 現行有效（Authorised）的許可寫成 peruutettu（11 月 AI 重產照證據包錯誤狀態寫的），以 213 筆 `fi-row-20261112-*`（每張表一筆）把狀態字改成站上有效列的寫法（(voimassa)／Voimassa），其他文字不動；母目錄 `check_drug_page.py --row-status FITxGNN` 為 0。
同時 site_config 的 MARKET_RE 由 `[Mm]arkkina` 放寬為 `[Mm]arkkin|Myyntilu|Myyntitiedot`：原本認不得「Tiedot Suomen markkinoilta／markkinoista」「Myyntiluvat／Myyntilupatiedot／Myyntitiedot Suomessa」標題（約 120 頁），這些市場段落的號碼歸屬與表格列狀態都漏驗；放寬後 gate 仍 exit 0。

## 市場段落許可證表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站逐站做，本站做表＋B）：每週許可證排程只改得到概覽表狀態列／張數列，AI 寫的自由格式許可證表（表頭十幾種寫法、適應症欄是 AI 譯成芬蘭文的治療領域、
狀態寫在適應症格「(voimassa)」「(peruutettu)」，2026-11-12 就以 213 筆 fi-row 紀錄人工更正過）與正文寫死的張數，會跟每週變的 EMA 資料矛盾、checker 擋頁。
- A. `scripts/sync_license_tables.py`（照 DETxGNN 同名檔，同為 EMA 資料）：市場段落（MARKET_RE 的各種標題；「<藥>: tunnetut käyttöaiheet ja markkinatilanne」段跳過）的第一張許可證表
  （表頭第一格含 lupa／luvan）換成程式依證據包 tfda.records 產生的「| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |」：
  品名、成分、治療領域照 EMA 英文原文（用戶決定欄位不翻譯、表頭註明語言），Tila 照 EMA status 轉本站寫法（Authorised→Voimassa、Withdrawn→Peruttu…），Voimassa 在前、最多 20 列；
  partial 頁表下加「Taulukossa näytetään N näissä tiedoissa olevasta M keskitetystä EU-myyntiluvasta …」，表後來源句；沒有人用集中許可時一句 NONE_LINE。段落裡沒有表的頁加在段落結尾。
  前後 `<!-- licenses:begin/end -->`；快照存 rows／total；gate 第 18 項（licenses.py＋sync_license_tables.block_problems）擋程式區塊≠快照重算、市場段落沒有程式表。
  接進：每週排程（`license_adapter.sync_tables`＋`PAGE_NOTE`）、`apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 結尾（`--no-rewrite` 不跑；不帶 `--ws` 時用 txgnn_ws.sh 預設工作目錄，沒有事實層就只依現有快照重排與改寫）。
  `--migrate`（第一次換表用）拿掉只講舊表列了幾筆的說明句（CAPTION）。
- B. `scripts/rewrite_license_counts.py`＋`src/fitxgnn/regulatory/count_prose.py`（照 Kr／My／DE 移植，芬蘭文句型：「N myyntilupaa on voimassa」「N voimassa olevaa myyntilupaa」
  「N myyntilupaa, joista V on voimassa」「V … N:sta」「Kaikki N myyntilupaa」「voimassa on N」「Myyntilupien määrä: N」「N/M」）；有保留、講證據包、相對數、劑型或單方／複方、廠商、
  獸用、其他國家或 Fimea、講表格筆數、預測或試驗字樣、partial 頁不改；跨過 0／1（芬蘭文 1 用主格、2 以上用分格）、molemmat 而總數不是 2、「kaikki … voimassa」而事實不符列 grammar／premise，不改。
  gate 第 22 項擋「再跑一次會變」。
- 2026-11-24 套用（資料 data-20261116-082921）：程式區塊 445 頁（公開 446 頁中有市場段落的 443 頁全部：AI 表 437 頁換掉、段落沒有表的 6 頁補區塊；noindex 2 頁；
  沒有市場段落的 3 頁 etanercept、desloratadine、bimatoprost 不加）；`--migrate` 拿掉舊表說明句 3 句（amlodipine、emtricitabine、formoterol）。
  正文張數程式改寫 0 句（句型明確的張數都已跟事實層一致；量測時市場段落有數字的句子 26 句，多是舊表說明句）。
  錨在舊表列上的 215 筆標 superseded（fi-row-20261112-* 213 筆、fi-lic-20261112-crizotinib-1、fi-lic-20261112-pioglitazone-1）。
  查核紀錄同 id 重發（前版存 history）：更正文字是舊表說明句的 15 筆（「Taulukossa on viisi ensimmäistä」「Viisi esimerkkiä:」「Viides taulukon ulkopuolinen lupa: Incresync…」等）改成
  「Myyntiluvat ja niiden tila ovat alla／yllä olevassa taulukossa.」（metformin 改成「Alla olevan taulukon valmisteet ovat kaikki yhdistelmävalmisteita…」，證據包 19 張全是複方）；
  說明框寫死「on kirjattu N myyntilupaa, joista V voimassa」的 546 筆（其中 6 筆已跟現行事實不符：abacavir、lamivudine、zidovudine 各 2 筆）改成不寫數字、指向概覽表與程式表，
  site_config 的 T["figures"] 同步改（reviews_from_edits 之後產生的紀錄也不寫數字）。
  另寫的寬偵測（公開頁正文講許可張數／狀態、對事實層）改前 3 句、改後 3 句：inclisiran 待辦「Peruutetun myyntilupatilanteen selvittäminen」（Leqvio 有效）以 `fi-lic-20261124-inclisiran-1` 更正，
  其餘是 catumaxomab 的 2017 年歷史句（查核紀錄更正文字）與 vildagliptin「tyypin 2 diabetes」誤中。單方／複方標籤全量對照證據包成分欄：0 句錯。待查清單沒有新增。
  checker 全量前後都是 0（row-status 0）；gate exit 0。last_modified_at：正文有變的 445 頁改 2026-11-24。
- 母目錄 `.claude/license_labels/FITxGNN.json` 現在是 {"Voimassa": valid, "Peruutettu": valid}：程式表另會寫「Peruttu」（Withdrawn，cancelled），要加 "Peruttu": "cancelled" 與 preferred.cancelled
  （「Peruutettu」記成 valid 看起來是 10 月學錯的）；本站沒改母目錄。沒加時排程的 lts.apply 可能把程式表的格改成 EMA 原文，但 sync_tables 會照證據包重排，頁面不受影響。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 365 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Yksityiskohtaista vaikutusmekanismitietoa ei ole tällä hetkellä saatavilla.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `fi-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（suomi）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：344 頁寫入紀錄（美國仿單 302、ChEMBL 42），20 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 42 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 55 筆紀錄、3 頁列待查；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）4 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Alkuperäinen käyttöaihe: Ei kirjattu paikallisiin tietoihin」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：EMA 集中許可（不含 Fimea 國家許可）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：acetylsalicylic_acid「Alkuperäinen käyttöaihe: Ei kirjattu paikallisiin tietoihin」→「Keskitetyt EU-myyntiluvat (EMA): 3 (voimassa: 3)」；2026-11-19 改了 19 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site FITxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。
