---
layout: default
title: "Lääkkeet, joiden uudelle käyttöaiheelle on tutkimusnäyttöä"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "EU:n keskitetysti luvitetut lääkkeet (EMA), joiden TxGNN:n ennustamalle uudelle käyttöaiheelle on tutkimusnäyttöä (L1-L2): käyttöaihe, taso, tutkimukset."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「katso raportti」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Ennustettu uusi käyttöaihe" | split: "|" -%}
{%- assign lev_labels = "Näytön taso|Näyttötaso" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Lääkkeet, joiden uudelle käyttöaiheelle on kliinistä tutkimusnäyttöä

<p class="key-answer" data-question="Millä Suomessa käytettävillä lääkkeillä on kliinistä tutkimusnäyttöä uudesta käyttöaiheesta?">
FITxGNN-raportin saaneista {{ listed.size }} lääkkeestä <strong>{{ trial_drugs.size }}</strong>:lla TxGNN:n ennustaman uuden käyttöaiheen näytön taso on <strong>L1 tai L2</strong> ({{ l1.size }} tasolla L1, {{ l2.size }} tasolla L2), eli sille on löytynyt näyttöä kliinisistä tutkimuksista (satunnaistetut tutkimukset, vaiheen 2–3 tutkimukset tai järjestelmälliset katsaukset).
</p>

Lääkkeet ovat peräisin lähteestä EU:n keskitetyistä myyntiluvista ([EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), voimassa myös Suomessa; myyntiluvan tila näkyy kunkin lääkkeen raportissa); luettelo vastaa lääkeraportteja, jotka on päivitetty viimeksi {{ latest_date }}.

<div class="key-takeaway">
Tutkimusnäyttö ennustetulle käyttöaiheelle ei todista tehoa. Jokainen alla oleva ehdokas <strong>vaatii yhä kliinisen validoinnin</strong> ja viranomaisarvion ennen kliinistä käyttöä.
</div>

---

## Lääkkeet, joilla on tutkimusnäyttöä (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Lääke</th><th>Ennustettu uusi käyttöaihe</th><th>Näytön taso</th><th>Viitatut rekisteröidyt tutkimukset (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}katso raportti{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(varauksin)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Näin luet luetteloa

- **Näytön taso** noudattaa sivuston [kriteerejä]({{ '/evidence-high/' | relative_url }}): L1 = Useita vaiheen 3 RCT-tutkimuksia / järjestelmällisiä katsauksia; L2 = Yksittäinen RCT tai useita vaiheen 2 tutkimuksia. ”(varauksin)” tarkoittaa, että raportti tarkentaa tasoa varauksella; lue raportin huomautus ennen kuin nojaat siihen.
- **Ennustettu uusi käyttöaihe** on kunkin raportin pääennuste. TxGNN-tietoverkkoon jo kirjatut käyttöaiheet ja vasta-aiheet on jätetty pois, mutta jokin ennuste voi silti osua jo vakiintuneeseen käyttöön; raportti kertoo tästä, kun se koskee lääkettä.
- **Viitatut rekisteröidyt tutkimukset** laskee raportissa viitatut ClinicalTrials.gov-numerot (NCT). Raporteissa viitataan osaan löydetyistä tutkimuksista; 0 tarkoittaa, ettei raportti viittaa yhteenkään rekisteröityyn tutkimukseen, ja sen kirjallisuusnäyttöä käsittelevä osio näyttää tason perusteen.
- Kaikki tasot ja koko menetelmän näet sivuilta [Vahva näyttö (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Kaikki lääkkeet]({{ '/drugs/' | relative_url }}) ja [menetelmät]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
