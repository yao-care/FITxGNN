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

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care, yritysrekisterinumero
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

FITxGNN on yhtiön "TxGNN Drug Repurposing" -tuotelinjan Suomen sivusto.
Sama järjestelmä on otettu käyttöön 30 maassa ja alueella, kukin nimellä `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN ja niin edelleen) osoitteessa `{cc}txgnn.yao.care`.
Tuotteen yleiskuvaus: <https://www.yao.care/medical/txgnn/>.

Itse TxGNN-mallin on kehittänyt Zitnik Lab Harvard Medical Schoolissa, ja se on julkaistu
*Nature Medicine* -lehdessä. Tämä alusta on tuotantojärjestelmä, jonka 藥提醒科技有限公司 on rakentanut
kyseisen mallin päälle. Se kattaa kansallisten lääkerekisteritietojen integroinnin, tietograafiin ja
syväoppimiseen perustuvan kaksoisennusteen, PubMed- ja ClinicalTrials-näytön luokittelun sekä
SMART on FHIR -integraation potilastietojärjestelmiin.

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
