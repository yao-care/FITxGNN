"""本站查核機制的在地設定（2026-11-12 建；核心流程比照 TwTxGNN、UsTxGNN，程式在同目錄與 scripts/）。

頁面上的查核框、查核紀錄表、說明文字用本站語言（芬蘭文）；依據是 EMA 集中許可（medicines output report）。
改這裡的字樣後跑 python3 scripts/apply_drug_reviews.py 重套，gate（scripts/check_seo_docs.py）會檢查。
COMMITS／REGEN_COMMITS：2026-10-31～11-06 正文的許可證刪改提交與期間內 AI 重產報告的提交（scripts/reviews_from_edits.py --git 用）。
"""
import json as _json

C = _json.loads(r"""{
 "SITE": "FITxGNN",
 "ID_PREFIX": "fi",
 "SNAPSHOT": "fi_licenses.json.gz",
 "HEADER_LABEL": "Näytön taso",
 "OVERVIEW_LABELS": [
  "Näytön taso",
  "Näyttötaso",
  "Todisteen taso"
 ],
 "WITHDRAWN_RE": "Peruttu|Peruutettu",
 "DESC_LEVEL_RE": "näytön taso (L[1-5]|N/A)",
 "DESC_LEVEL_FMT": "näytön taso {lv}",
 "NA_DESC": "vain tunnetut käytöt",
 "HEADER_RULE_NOTE": "2026-11-12 實測：有 Quick Overview 等級的頁，頁首等於第一個等級（427 頁）；另 4 頁是頁首 N/A、沒有預測的頁（格內只寫說明），不重算",
 "MARKET_RE": "[Mm]arkkina",
 "ID_RE": "EMEA/H/C/\\d{4,6}(?:/X/\\d+)?",
 "PROSE_ID_RE": "EMEA/H/C/\\d{4,6}",
 "ORIGINAL_LABELS": [
  "Alkuperäinen käyttöaihe",
  "Alkuperäinen indikaatio"
 ],
 "ORIGINAL_NONE_RE": "^\\s*(ei kirjattu|ei saatavilla|ei yhtään|ei tietoa|n/a|–|-)",
 "ORIGINAL_SPLIT_RE": "[;,/()]+|\\bja\\b|\\btai\\b",
 "ORIGINAL_NOTE": "2026-11-12：證據包的許可證紀錄來自 EMA 集中許可清單；可比對頁數以程式輸出為準",
 "COMMITS": [
  "d41492e2",
  "60471841",
  "c0d4bcf7"
 ],
 "REGEN_COMMITS": [
  "5031d007",
  "59be858b",
  "08ddfd34",
  "7df54820",
  "ee41e5e5",
  "1a3597a6"
 ],
 "SOURCES": [
  {
   "title": "EMA – Medicines output (European public assessment reports)",
   "url": "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"
  }
 ],
 "PROGRAM_LINE_RE": null,
 "CLASSIFY": [
  [
   "tw",
   "Taiwan|TFDA|台灣|臺灣"
  ],
  [
   "combo",
   "yhdistelmä|yksikomponent|yhden vaikuttavan"
  ],
  [
   "cancel",
   "peruttu|peruutettu|lakkautett|lakann|mitätö|ei (?:ole )?(?:voimassa|myyntiluvallinen|markkinoilla)|vanhentun|ei voimassa olevaa"
  ],
  [
   "count",
   "\\b\\d+\\b[^.;]{0,40}(?:myyntilu|valmiste|pakkau|tuote)|(?:myyntilu|valmiste|pakkau)[^.;]{0,30}\\b\\d+\\b|\\b(?:kaikki|molemmat)\\b[^.;]{0,30}(?:myyntilu|voimassa)|\\bvoimassa"
  ],
  [
   "product",
   "\\b(?:tabletti|kapseli|injektio|voide|markkinoilla|lääkemuoto)"
  ]
 ],
 "T": {
  "label": {
   "correct": "Tarkistuskorjaus",
   "annotate": "Tarkistushuomautus",
   "rereview": "Odottaa uudelleenarviointia",
   "rereview_result": "Uudelleenarvioinnin tulos"
  },
  "action": {
   "correct": "Korjattu",
   "annotate": "Huomautus lisätty",
   "rereview": "Merkitty uudelleenarvioitavaksi",
   "section": "Lähteistetty osio lisätty",
   "rereview_result": "Uudelleenarviointi tehty",
   "header_level": "Otsikon näytön taso laskettu uudelleen pikakatsauksesta",
   "description_level": "Sivun kuvauksen näytön taso yhdenmukaistettu otsikon kanssa"
  },
  "verdict": {
   "maintain": "Ennallaan",
   "downgrade": "Alennettu",
   "upgrade": "Nostettu",
   "withdraw": "Peruttu"
  },
  "log_head": "## Tarkistusloki",
  "disclaimer_re": "Vastuuvapauslauseke",
  "log_cols": [
   "Tarkistuspäivä",
   "Kohta",
   "Toimenpide",
   "Lähde"
  ],
  "level_same": "näytön taso {o} ennallaan",
  "level_change": "näytön taso {o} → {n}",
  "orig": "Alun perin tässä luki: ”{x}”",
  "table_updated": "Sivun kohdat ”{labels}” päivitettiin uudelleenarvioinnin tuloksen mukaisiksi; alkuperäiset arvot ovat alla tarkistuslokissa.",
  "decision": "Päätössuositus: {x}",
  "source": "Lähde",
  "rereviewed": "Merkitty uudelleenarvioitavaksi → arvioitu uudelleen (ks. uudelleenarvioinnin tulos)",
  "hdr": "Otsikon näytön taso laskettu uudelleen pikakatsauksesta ({o} → {n})",
  "hdr_withdraw": "Pääennuste peruttiin uudelleenarvioinnissa; otsikon näytön taso laskettu uudelleen ({o} → {n})",
  "now_listed": ", nyt luettelossa ”{x}”",
  "rr": "Uudelleenarviointi: {v}, {c}",
  "tu": "; {l}: ”{a}” → ”{b}”",
  "desc": "Sivun kuvaus: ”{a}” muutettu muotoon ”{b}” (seuraa otsikon tasoa; muu teksti ennallaan, alkuperäinen tallessa lokissa)",
  "revised": " (päivitetty {d}; aiempi versio tallessa lokissa)",
  "superseded": "Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: {a})",
  "regen": "Ei enää sivulla raportin uudelleenluonnin jälkeen ({d}: {n}; aiemmin: {a})",
  "program": "Ei enää sivulla ohjelmakorjauksen jälkeen ({d}: {n}; aiemmin: {a})",
  "withdrawn": "Tarkistus peruttu ({d}: {n}; aiemmin: {a})",
  "intro": "Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.",
  "intro_header": "Alla on tämän sivun tarkistusloki; otsikon näytön taso seuraa pikakatsausta. Mallin ennusteita, yhteenvetotaulukkoa ja johtopäätöksiä ei ole kirjoitettu uudelleen.",
  "intro_rr": "Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja, eikä mallin ennustetekstiä ole kirjoitettu uudelleen; näytön tasoja ja päätöksiä on muutettu vain uudelleenarvioinnin tuloksen perusteella (alennus, nosto tai peruminen), ja alkuperäiset arvot ovat alla.",
  "figures": "Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu {total} myyntilupaa, joista {valid} voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa.",
  "data_as_of": "EMA:n keskitetysti myönnetyt myyntiluvat, tilanne {date}",
  "notes": {
   "tw": "Poistettu: Taiwanin mallipohjasta (TFDA) jäänyt teksti, joka ei koske tätä sivua.",
   "combo": "Poistettu: tieto yksi- tai yhdistelmävalmisteista ei vastannut myyntilupatietoja ({d}).",
   "cancel": "Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja ({d}).",
   "count": "Poistettu: ilmoitettu myyntilupien määrä tai tila ei vastannut myyntilupatietoja ({d}).",
   "product": "Poistettu: valmisteiden kuvaus ei vastannut myyntilupatietoja ({d}).",
   "generic": "Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa ({d})."
  },
  "notes_with_figures": [
   "cancel",
   "count",
   "product",
   "generic"
  ],
  "summary": "Poistettu: ”{x}”",
  "regen_note": "raportti luotiin uudelleen marraskuussa 2026, eikä se enää sisällä tätä väitettä"
 }
}""")
