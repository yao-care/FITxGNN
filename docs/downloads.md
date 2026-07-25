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
