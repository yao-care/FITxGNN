---
layout: default
title: Lataukset
nav_order: 94
permalink: /downloads/
description: "FITxGNN:n avoimen datan lataukset: FHIR-resurssit, ennustetulokset ja hakuindeksi."
---

# Lataukset

<div class="key-takeaway">
Ennusteet julkaistaan FHIR R4 -muodossa, valmiina integroitaviksi potilastietojärjestelmiin.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Suomi: mitä tiedostot nyt sisältävät

| Tiedosto | Sisältö nyt |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} lääkettä ennustettuine käyttöaiheineen |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} lääkettä näytön tason ja alkuperäisen käyttöaiheen kanssa |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} MedicationKnowledge-resurssia (yksi lääkettä kohden) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ClinicalUseDefinition-resurssia (yksi ennustettua käyttöaihetta kohden) |

Paikallisen aineiston uudelleenkäyttö: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), julkaisija Euroopan lääkevirasto (EMA); uudelleenkäyttöön sovelletaan julkaisijan ehtoja, eikä tämä sivusto myönnä lisäoikeuksia.

{% if site.data.local_facts.top_licensed.size > 0 %}Lääkkeet, joilla on eniten voimassa olevaa keskitettyä EU-myyntilupaa (EMA): {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Tarkistuslokin viimeisimmät korjaukset: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## FHIR-resurssit

Tämä sivusto julkaisee ennusteet FHIR R4 -resursseina, joita SMART on FHIR -sovellukset voivat käyttää suoraan:

| Resurssi | Polku | Kuvaus |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | FHIR-palvelimen kyvykkyyskuvaus |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Lääkeresurssit |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Ennustetut käyttöaiheet |
| Bundle | `/fhir/Bundle/all-predictions.json` | Kaikki ennusteet yhtenä nippuna |

---

## Hakuindeksi

`/data/search-index.json` tarjoaa lääkkeiden ja käyttöaiheiden hakuindeksin oman
hakukäyttöliittymän rakentamiseen.

---

## Käyttöehdot

<ol class="actionable-steps">
<li>Tämän sivuston tiedot ovat <strong>vain tutkimuskäyttöön</strong>, eikä niitä saa käyttää hoitopäätösten perustana.</li>
<li>Viitatessasi mainitse FITxGNN (藥提醒科技有限公司) ja viittaa alkuperäiseen TxGNN-julkaisuun.</li>
<li>Jatkokäytössä tiedot ovat edelleen kunkin alkuperäisen lähteen lisenssiehtojen alaisia (katso <a href="{{ '/sources/' | relative_url }}">Tietolähteet</a>).</li>
</ol>

---

## Kehittäjästä

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care). Yhtiön tiedot, TxGNN-mallin
tausta ja tuotelinjan kaikki sivustot löytyvät <a href="{{ '/about/' | relative_url }}">Tietoa</a>-sivulta.

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
