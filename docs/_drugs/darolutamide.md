---
layout: default
title: Darolutamide
parent: Pelkkä mallin ennuste (L5)
nav_order: 127
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Darolutamide: ennustettu uusi käyttöaihe Homotsygoottinen familiaalinen hyperkolesterolemia (näytön taso L5). Alkuperäinen käyttöaihe: Kastraatiorefraktaarinen eturauhassyöpä"
monitor_inn: "DAROLUTAMIDE"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease"]
---

# Darolutamide
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Darolutamidi: Eturauhassyövän hoidosta ennustettuun uuteen käyttöaiheeseen (homotsygoottinen familiaalinen hyperkolesterolemia)

## Yhden lauseen yhteenveto

Darolutamidi on ei-steroidinen androgeenireseptorin salpaaja, jota on alun perin käytetty kastraatiorefraktaarisen eturauhassyövän hoitoon.
TxGNN-malli ennustaa sen voivan tehota **homotsygoottiseen familiaaliseen hyperkolesterolemiaan**, mutta ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään laskennalliseen malliin.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Kastraatiorefraktaarinen eturauhassyöpä |
| Ennustettu uusi käyttöaihe | Homotsygoottinen familiaalinen hyperkolesterolemia |
| TxGNN-ennustepistemäärä | 99,11 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Tällä hetkellä yksityiskohtaiset tiedot vaikutusmekanismista eivät ole saatavilla. Tiedossa on, että darolutamidi on ei-steroidinen androgeenireseptorin salpaaja, jonka teho kastraatiorefraktaarisessa eturauhassyövässä on osoitettu.

Aineistossa ei ole mitään, mikä yhdistäisi androgeenireseptorin salpauksen LDL-reseptorin toimintahäiriöön tai tämän sairauden rasva-aineenvaihduntaan. Alkuperäinen käyttöaihe (hormoniriippuvainen syöpä) ja ennustettu käyttöaihe (perinnöllinen rasva-aineenvaihduntahäiriö) ovat lääketieteellisesti hyvin kaukana toisistaan. Korkea pistemäärä (0,991) on laskennallinen ennuste, jota mikään kliininen tieto ei tue.

Muut mallin ennustamat käyttöaiheet olivat moninainen endokriininen neoplasia (pistemäärä 99,06 %, näytön taso L4) ja HIV-infektio (99,04 %, L5). Kumpaankaan ei löydy uskottavaa mekanistista yhteyttä: kaksi moninaiseen endokriiniseen neoplasiaan liitettyä tutkimusta koskevat todennäköisesti eturauhassyöpää, eivätkä ne ole kohdennettuja kyseiseen oireyhtymään.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä kliinisiä tutkimuksia, jotka liittyisivät homotsygoottiseen familiaaliseen hyperkolesterolemiaan.

---

## Kirjallisuusnäyttö

Tällä hetkellä aiheeseen liittyvää kirjallisuutta ei ole saatavilla.

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004790 | Nubeqa | – | Kastraatiorefraktaarinen eturauhassyöpä (tila: peruutettu) |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (ei-steroidinen androgeenireseptorin salpaaja), ei tavanomainen solunsalpaaja |
| Luuydinsuppression riski | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksentelua aiheuttava vaikutus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurattavat parametrit | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja varotoimet |

---

## Turvallisuushuomioita

- **Lääkeyhteisvaikutukset:** Tietokannassa on kirjattu yhteensä 100 yhteisvaikutusta. Merkittäviä (Major) yhteisvaikutuksia on raportoitu muun muassa seuraavien lääkeaineiden kanssa:
  - deksametasoni
  - eluksadoliini
  - rosuvastatiini
- Kohtalaisia (Moderate) yhteisvaikutuksia on mm. klaritromysiinin, empagliflotsiinin, glyburidin, repaglinidin, simvastatiinin, sulfasalatsiinin, kobisistaatin, deferasiroksin ja eltrombopagin kanssa.
- Lieviä (Minor) yhteisvaikutuksia on mm. aprepitantin, simetidiinin ja mikonatsolin kanssa.
- Huomionarvoista on, että kolesterolia alentavat statiinit (rosuvastatiini: merkittävä, simvastatiini: kohtalainen) ovat yhteisvaikutuksia, mikä olisi käytännössä oleellista ennustetussa käyttöaiheessa.

Varoitukset ja vasta-aiheet: ks. valmisteyhteenveto.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu ainoastaan TxGNN-mallin pistemäärään (L5). Kliinisiä tutkimuksia ja julkaisuja ei ole, eikä androgeenireseptorin salpauksen ja LDL-reseptorin toimintahäiriön välille löydy mekanistista yhteyttä. Lisäksi Suomen myyntilupa on peruutettu, ja valmisteyhteenvedon turvallisuustiedot puuttuvat.

**Jatkaminen edellyttää seuraavaa:**
- Vaikutusmekanismin (MOA) tietojen täydentäminen, esimerkiksi DrugBankista
- Fimean valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen ja läpikäynti (turvallisuusseulonnan estävä puute)
- Prekliiniset tai mekanistiset tutkimukset, jotka selvittävät mahdollisen yhteyden androgeenireseptorin signalointiin ja lipidiaineenvaihduntaan
- Myyntilupatilanteen selvittäminen (nykyinen lupa peruutettu)
- Yhteisvaikutusten arviointi, erityisesti statiinien kanssa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

