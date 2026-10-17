---
layout: default
title: "L\u00e4\u00e4kkeiden Uudelleensijoittelun Ennusteet \u2014 Suomi"
nav_order: 1
description: "Tekoälyyn perustuvat lääkkeiden uudelleenkäytön ennusteet Suomelle. Näyttöön perustuva analyysi hyväksyttyjen lääkkeiden mahdollisista uusista käyttöaiheista."
permalink: /
---

# Lääkkeiden uudelleenkäytön ennusteet — Suomi

This project uses the TxGNN knowledge graph to predict potential new therapeutic uses for medicines approved in Finland.

**Disclaimer**: This content is for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before application.

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
kyseisen mallin päälle. Se kattaa kansallisten lääkerekisteritietojen integroinnin, syväoppimiseen perustuvan ennusteen, josta tietograafiin jo kirjatut käyttöaiheet on suljettu pois, PubMed- ja ClinicalTrials-näytön luokittelun sekä
SMART on FHIR -integraation potilastietojärjestelmiin.
