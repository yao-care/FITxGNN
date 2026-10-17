---
layout: default
title: Lipegfilgrastim
parent: Pelkkä mallin ennuste (L5)
nav_order: 266
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Lipegfilgrastim: ennustettu uusi käyttöaihe Primaarinen verihiutaleiden vapautumishäiriö (näytön taso L5). Alkuperäinen käyttöaihe: Ei saatavilla koottujen tietojen perusteella (lääkkeen tiedetään ol…"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "diabetic retinopathy"]
---

# Lipegfilgrastim
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

# Lipegfilgrastiimi: Neutropenian hoidosta primaariseen verihiutaleiden vapautumishäiriöön

## Yhden lauseen yhteenveto

Lipegfilgrastiimi on pegyloitu G-CSF-kasvutekijän analogi, jota käytetään neutrofiilien määrän lisäämiseen. Tarkka alkuperäinen käyttöaihe ei sisälly tähän raportin varten koottuihin tietoihin. TxGNN-malli ennustaa lääkkeelle mahdollista tehoa **primaariseen verihiutaleiden vapautumishäiriöön**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Ei saatavilla koottujen tietojen perusteella (lääkkeen tiedetään olevan G-CSF-analogi, jota käytetään neutropenian hoidossa) |
| Ennustettu uusi käyttöaihe | Primaarinen verihiutaleiden vapautumishäiriö |
| TxGNN-ennusteen pistemäärä | 99,93 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Tälle raportille koottujen tietojen mukaan lääkkeen vaikutusmekanismia koskevia yksityiskohtaisia tietoja ei ole saatavilla. Tunnetun luokituksen perusteella lipegfilgrastiimi on pegyloitu G-CSF-analogi, joka stimuloi neutrofiilien kehitysliinan jakautumista ja erilaistumista myeloisten solujen G-CSF-reseptorin kautta.

Primaariset verihiutaleiden vapautumishäiriöt ovat verihiutaleiden omia toimintahäiriöitä (rakeiden eritys). Selvää mekanistista yhteyttä neutrofiilikohtaisen vaikutuksen ja näiden häiriöiden välillä ei ole tunnistettu. Korkea pistemäärä on todennäköisesti verkostopohjaisen ennusteen tulos, ei biologisen perustelun.

Muut ennustetut käyttöaiheet ovat samalla tavalla heikosti perusteltuja:

| Sija | Ennustettu käyttöaihe | TxGNN-pistemäärä | Näytön taso | Huomio |
|------|------|------|------|------|
| 2 | Vaikea ei-proliferatiivinen diabeettinen retinopatia | 99,91 % | L5 | Vain spekulatiivinen yhteys progenitorisolujen mobilisaation kautta; voi myös edistää patologista uudisverisuonten muodostusta |
| 3 | Pseudo-von Willebrandin tauti | 99,91 % | L5 | Johtuu verihiutaleiden GPIbα-geenin toiminnanvahvistumisvarianteista; uskottavaa mekanistista yhteyttä ei ole |
| 4 | Glanzmannin trombasteenia | 99,91 % | L5 | Johtuu integriini αIIbβ3:n puutteesta tai toimintahäiriöstä; G-CSF:llä ei tunnettua vaikutusta |
| 5 | Diabeettinen retinopatia | 99,75 % | L5 | Spekulatiivinen yhteys; verkkokalvon uudisverisuonten pahenemisen riski on selvitettävä |

---

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002556 | Lonquex (Teva B.V.) | – | – (tila: peruutettu) |

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta ja pakkausselosteesta. Lääkkeiden yhteisvaikutuksia koskevia tietoja ei löytynyt.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään graafipohjaiseen malliin: kliinisiä tutkimuksia ja julkaisuja ei ole, eikä uskottavaa mekanistista yhteyttä ole tunnistettu. Lisäksi valmisteen myyntilupa Suomessa on peruutettu, mikä heikentää käytännön toteutettavuutta.

**Eteenpäin siirtyminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta ja läpikäynti (estävä tietoaukko turvallisuusseulonnalle)
- Vaikutusmekanismin (MOA) tietojen täydentäminen esimerkiksi DrugBankista
- Alkuperäisen hyväksytyn käyttöaiheen vahvistaminen
- Prekliiniset tai mekanistiset tutkimukset, jotka tukisivat yhteyttä verihiutaleiden toimintahäiriöihin
- Diabeettisen retinopatian osalta uudisverisuonten muodostumisen riskin arviointi ennen jatkotutkimuksia
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

