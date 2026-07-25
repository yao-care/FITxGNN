---
layout: default
title: Tietoa
nav_order: 90
permalink: /about/
description: "FITxGNN on 藥提醒科技有限公司:n (yao.care) kehittämä lääkkeiden uudelleensijoittelun ennustealusta, joka perustuu Harvardin TxGNN-malliin ja kattaa Fimean hyväksymät lääkkeet Suomessa."
---

# Tietoa

<div class="key-takeaway">
Nopeutamme lääkkeiden uudelleensijoittelun näytön validointia tekoälyn avulla — ennusteesta näyttöön yhdellä silmäyksellä.
</div>

---

## Tausta

<p class="key-answer" data-question="Mikä FITxGNN on?">
<strong>FITxGNN</strong> on lääkkeiden uudelleensijoittelun tutkimusta tukeva alusta, joka perustuu
Harvardin yliopiston Zitnik Labin <em>Nature Medicine</em> -lehdessä julkaisemaan TxGNN-malliin.
Se ennustaa käyttöaiheiden laajentamista Fimean Suomessa hyväksymille lääkkeille. Tekoälyn
ennustepisteiden lisäksi alusta yhdistää kliinistä näyttöä ClinicalTrials.gov-palvelusta ja
PubMedistä, jotta tutkijat voivat nopeasti arvioida kunkin ennusteen uskottavuutta.
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

## Mitä lääkkeiden uudelleensijoittelu tarkoittaa?

<p class="key-answer" data-question="Mitä lääkkeiden uudelleensijoittelu tarkoittaa?">
<strong>Lääkkeiden uudelleensijoittelu</strong> tarkoittaa uusien hoidollisten käyttötarkoitusten
löytämistä olemassa oleville lääkkeille. Verrattuna kokonaan uuden lääkkeen kehittämiseen —
10–15 vuotta ja 1&ndash;2 miljardia Yhdysvaltain dollaria — uudelleensijoittelu vie 3–5 vuotta ja
100&ndash;300 miljoonaa dollaria, ja turvallisuustiedot ihmisillä ovat jo olemassa,
joten epäonnistumisen riski on pienempi.
</p>

<table class="comparison-table">
<thead>
<tr><th>Näkökulma</th><th>Uuden lääkkeen kehittäminen</th><th>Lääkkeen uudelleensijoittelu</th></tr>
</thead>
<tbody>
<tr><td>Aika</td><td>10&ndash;15 vuotta</td><td>3&ndash;5 vuotta</td></tr>
<tr><td>Kustannus</td><td>1&ndash;2 miljardia USD</td><td>100&ndash;300 miljoonaa USD</td></tr>
<tr><td>Turvallisuustiedot</td><td>Täytyy hankkia alusta alkaen</td><td>Ihmisillä kerätyt tiedot jo saatavilla</td></tr>
<tr><td>Epäonnistumisen riski</td><td>Erittäin suuri (&gt;90 %)</td><td>Pienempi</td></tr>
</tbody>
</table>

---

## Mikä TxGNN on?

<p class="key-answer" data-question="Mikä TxGNN on?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> on syväoppimismalli,
jonka on kehittänyt Zitnik Lab Harvard Medical Schoolissa ja joka on julkaistu <em>Nature Medicine</em>
-lehdessä. Se ennustaa uusia lääkkeen ja sairauden välisiä yhteyksiä ja on ensimmäinen erityisesti
kliinikoille suunniteltu lääkkeiden uudelleensijoittelun perusmalli.
</p>

<blockquote class="expert-quote">
"TxGNN yhdistää tietograafin, jossa on 17 080 biolääketieteellistä entiteettiä, ja käyttää graafineuroverkkoja
oppiakseen solmujen välisiä monimutkaisia suhteita. Näin se ennustaa lääkkeiden mahdollista tehoa
harvinaisissa sairauksissa."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Tietolähteet

<table class="comparison-table">
<thead>
<tr><th>Tyyppi</th><th>Lähde</th><th>Kuvaus</th></tr>
</thead>
<tbody>
<tr><td>Tekoälyennuste</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Harvardin tietograafiin perustuva ennustemalli</td></tr>
<tr><td>Kliiniset tutkimukset</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Maailmanlaajuinen kliinisten tutkimusten rekisteri</td></tr>
<tr><td>Kirjallisuus</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Biolääketieteellisen kirjallisuuden tietokanta</td></tr>
<tr><td>Lääketiedot</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Lääke- ja kohdemolekyylitietokanta</td></tr>
<tr><td>Myyntilupatiedot</td><td><a href="https://fimea.fi/">Fimea</a></td><td>Suomen lääkkeiden myyntilupatiedot</td></tr>
</tbody>
</table>

---

## Tieteellinen perusta

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Laajuus

| Kohde | Arvo |
|------|-------|
| Lääkeraportteja | 516 |
| Lääkeviranomainen | Fimea |
| Käyttöönotettuja sivustoja | 30 maata / aluetta |

---

## Yhteystiedot

- **GitHub Issues**: <https://github.com/yao-care/FITxGNN/issues>
- **Kehittäjä**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Tuotteen yleiskuvaus**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
