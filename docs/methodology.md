---
layout: default
title: Menetelmät
nav_order: 91
permalink: /methodology/
description: "Miten FITxGNN tuottaa ja validoi ennusteet: TxGNN-tietograafiennuste, näytön kerääminen, L1–L5-luokittelu ja päätössuositukset."
---

# Menetelmät

<div class="key-takeaway">
Tekoälyennusteesta näytön luokitteluun — jokaisen ehdokkaan arviolla on jäljitettävä perusta.
</div>

---

## Kokonaisprosessi

<p class="key-answer" data-question="Miten FITxGNN tuottaa ennusteensa?">
Alusta käyttää neljävaiheista prosessia: TxGNN-tietograafimalli ennustaa mahdollisia
lääkkeen ja sairauden välisiä yhteyksiä, minkä jälkeen jokaiselle ennustetulle parille kerätään
automaattisesti näyttöä, näyttö luokitellaan tasoille L1–L5 ja lopuksi annetaan päätössuositus.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-ennuste</strong>: lääkkeen ja sairauden väliset suhteet ennustetaan tietograafin ja graafineuroverkkojen yhdistelmällä.</li>
<li><strong>Näytön kerääminen</strong>: jokaiselle ennustetulle parille kerätään näyttöä lähteistä ClinicalTrials.gov, PubMed, DrugBank ja Fimea.</li>
<li><strong>Näytön luokittelu</strong>: luokitus tasoille L1–L5, joissa L1 on vahvin (useita vaiheen 3 RCT-tutkimuksia) ja L5 tarkoittaa pelkkää mallin ennustetta.</li>
<li><strong>Päätössuositus</strong>: Go, Proceed, Consider, Explore tai Hold näytön tason perusteella.</li>
</ol>

---

## Näytön luokittelukriteerit

<table class="comparison-table">
<thead>
<tr><th>Taso</th><th>Määritelmä</th><th>Kliininen merkitys</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Useita vaiheen 3 RCT-tutkimuksia / järjestelmällisiä katsauksia</td><td>Vahva tuki; kliinistä käyttöä voidaan harkita</td></tr>
<tr><td><strong>L2</strong></td><td>Yksittäinen RCT tai useita vaiheen 2 tutkimuksia</td><td>Kohtalainen tuki; validointitutkimuksia voidaan suunnitella</td></tr>
<tr><td><strong>L3</strong></td><td>Havainnoivat tutkimukset / laajat tapaussarjat</td><td>Alustava tuki; vaatii lisävahvistusta</td></tr>
<tr><td><strong>L4</strong></td><td>Prekliiniset / mekanistiset tutkimukset</td><td>Teoreettinen tuki; kaukana kliinisestä käytöstä</td></tr>
<tr><td><strong>L5</strong></td><td>Pelkkä mallin ennuste</td><td>Hypoteesivaihe; ei vielä näyttöä ihmisillä</td></tr>
</tbody>
</table>

---

## Kaksoismoottoriennuste

Kaksi menetelmää ajetaan rinnakkain, ja luotettavuusmerkintä kertoo, ovatko ne yhtä mieltä:

| Menetelmä | Nopeus | Tarkkuus | Kuvaus |
|--------|-------|-----------|-------------|
| Tietograafi (KG) | Nopea | Matalampi | Päättely DrugBank-suhteiden ja graafirakenteen pohjalta |
| Syväoppiminen (DL) | Hidas | Korkeampi | TxGNN-graafineuroverkkomalli |

| Luotettavuus | Lähde | Merkitys |
|------------|--------|---------|
| very_high | KG + DL | Molemmat menetelmät ovat yhtä mieltä |
| high | Vain DL | Korkeat pisteet saanut syväoppimisen tuki |
| medium | Vain KG | Tietograafin tuki |

---

## Viranomaistietojen integrointi

Suomen lääkkeiden myyntilupatiedot ovat peräisin Fimealta. Vaikuttavien aineiden nimet
kohdennetaan DrugBank-sanastoon; aineet, joita ei voida kohdentaa — kasviuutteet, rokotteet,
apuaineet ja muut DrugBankiin luetteloimattomat — jätetään ennusteen ulkopuolelle.

---

## Rajoitukset

<ol class="actionable-steps">
<li>Ennusteet ovat tilastollisia yhteyksiä, eivätkä ne <strong>osoita syy-yhteyttä tai kliinistä tehoa</strong>.</li>
<li>Luokitus L5 tarkoittaa pelkkää mallin ennustetta ilman tukevaa näyttöä ihmisillä.</li>
<li>Näytön kerääminen perustuu julkisiin tietokantoihin; julkaisemattomia tai indeksoimattomia tutkimuksia ei havaita.</li>
<li>Vaikuttavien aineiden kohdennuksesta voi jäädä kohteita pois nimieroista johtuen.</li>
</ol>

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
