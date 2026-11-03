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

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care). Yhtiön tiedot, TxGNN-mallin
tausta ja tuotelinjan kaikki sivustot löytyvät <a href="{{ '/about/' | relative_url }}">Tietoa</a>-sivulta.

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
