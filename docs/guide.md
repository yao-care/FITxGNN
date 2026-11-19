---
layout: default
title: Käyttöopas
nav_order: 92
permalink: /guide/
description: "FITxGNN-käyttöopas: miten lääkkeitä haetaan, miten näytön tasoja luetaan ja miten suosituksia tulkitaan."
---

# Käyttöopas

<div class="key-takeaway">
Tarkista ensin näytön taso, sitten suositus, ja lue lopuksi alkuperäinen kirjallisuus.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Suomi: esimerkki tältä sivustolta

Raportti luetaan tällä sivustolla kolmessa vaiheessa: näytön taso, paikalliset markkinatiedot, tarkistusloki.

{% assign gx = site.data.local_facts.example %}
{% if gx %}Avaa [{{ gx.t }}]({{ gx.u | relative_url }}): otsikossa näkyy näytön taso **{{ gx.l }}**; tärkein ennustettu uusi käyttöaihe on **{{ gx.i }}**; paikallisissa tiedoissa on **{{ gx.lt }}** keskitettyä EU-myyntilupaa (EMA), joista **{{ gx.lv }}** voimassa olevaa; sivun tarkistuslokissa on **{{ gx.r }}** merkintää.{% endif %}

{% if site.data.local_facts.most_reviewed.size > 0 %}Lääkkeet, joilla on eniten tarkistuslokin merkintöjä: {% for r in site.data.local_facts.most_reviewed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.r }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Tarkistuslokin viimeisimmät korjaukset: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Lääkkeen hakeminen

<ol class="actionable-steps">
<li>Käytä sivun yläreunan hakukenttää (vaikuttavien aineiden nimet osuvat paremmin kuin kauppanimet).</li>
<li>Tai selaa koko luetteloa sivulla <a href="{{ '/drugs/' | relative_url }}">Kaikki lääkkeet</a>.</li>
<li>Voit myös selata näytön tason mukaan: <a href="{{ '/evidence-high/' | relative_url }}">vahva</a>, <a href="{{ '/evidence-medium/' | relative_url }}">kohtalainen</a>, <a href="{{ '/evidence-low/' | relative_url }}">pelkkä mallin ennuste</a>.</li>
</ol>

---

## Raportin lukeminen

<p class="key-answer" data-question="Mitä näytön tasot L1–L5 tarkoittavat?">
Jokainen lääkeraportti luettelee ennustetut uudet käyttöaiheet, ja jokaisella käyttöaiheella on
näytön taso L1&ndash;L5. <strong>L1 tarkoittaa, että useat vaiheen 3 satunnaistetut kontrolloidut
tutkimukset tukevat sitä jo; L5 tarkoittaa pelkkää mallin ennustetta ilman näyttöä ihmisillä.</strong>
Täydelliset kriteerit ovat sivulla
<a href="{{ '/methodology/' | relative_url }}">Menetelmät</a>.
</p>

| Jos näet | Se tarkoittaa | Suositeltu toimenpide |
|-----------|----------|------------------|
| L1 / L2 | Kliinisistä tutkimuksista on näyttöä | Tarkastele alkuperäisiä NCT- ja PMID-tietueita |
| L3 / L4 | Havainnoivaa tai prekliinistä näyttöä | Käsittele tutkimusvihjeenä |
| L5 | Pelkkä mallin ennuste | Vain hypoteesien muodostukseen; ei kliiniseen käyttöön |

---

## Lähdeviittaukset ja jäljitettävyys

Jokaisella raportin näyttökohdalla on jäljitettävä tunniste:

- **NCT-numero**: linkittää ClinicalTrials.gov-rekisteröintiin
- **PMID**: linkittää PubMed-tietueeseen
- **DrugBank ID**: linkittää lääke- ja kohdemolekyylitietoihin

Lue alkuperäinen kirjallisuus ja varmista asiayhteys, ennen kuin viittaat mihinkään tämän alustan johtopäätökseen.

---

## Usein kysytyt kysymykset

<p class="key-answer" data-question="Voiko ennusteita käyttää kliinisesti?">
<strong>Ei.</strong> Tämän alustan ennusteet ovat tutkimusvihjeitä, eivät kliinisiä neuvoja. Kaikki
lääkkeiden uudelleensijoittelun kliininen soveltaminen edellyttää täydellistä kliinisten tutkimusten
validointia ja viranomaisarviointia.
</p>

<p class="key-answer" data-question="Miksi en löydä tiettyä lääkettä?">
Vaikuttavan aineen on kohdennuttava DrugBank-sanastoon, jotta se voidaan sisällyttää ennusteeseen.
Kasviuutteet, rokotteet, apuaineet ja muut DrugBankiin luetteloimattomat kohteet eivät esiinny tällä alustalla.
</p>

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
