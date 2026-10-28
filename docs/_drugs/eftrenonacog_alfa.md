---
layout: default
title: Eftrenonacog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Eftrenonacog Alfa: ennustettu uusi käyttöaihe Pseudo-von Willebrandin tauti (verihiutaletyyppinen VWD) (näytön taso L5). Alkuperäinen käyttöaihe: Hemofilia B"
monitor_inn: "EFTRENONACOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia"]
---

# Eftrenonacog Alfa
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

## Eftrenonogi alfa: Hemofilia B:stä Pseudo-von Willebrandin tautiin (verihiutaletyyppinen VWD)
{: .text-alpha }

## Yhteenveto

Eftrenonogi alfa on yhdistelmä-DNA-tekniikalla valmistettu tekijä IX:n ja Fc-osan fuusioproteiini, jota on alun perin käytetty **hemofilia B:n** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **pseudo-von Willebrandin tautiin**, mutta ennuste perustuu pelkästään malliin: **kliinisiä tutkimuksia ei ole** eikä **julkaisuja ole**, ja mekanistinen peruste on heikko.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hemofilia B |
| Ennustettu uusi käyttöaihe | Pseudo-von Willebrandin tauti (verihiutaletyyppinen VWD) |
| TxGNN-ennustepistemäärä | 0,9948 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa (MOA) ei ole tällä hetkellä saatavilla. Eftrenonogi alfa on rekombinantti tekijä IX:n Fc-fuusioproteiini (rFIXFc), joka korvaa puuttuvaa tekijä IX:ää hemofilia B:ssä. Sen teho alkuperäisessä käyttöaiheessa perustuu veren hyytymiskaskadin sisäisen reitin korjaamiseen.

Pseudo-von Willebrandin tauti johtuu verihiutaleiden GPIbα-reseptorin toimintaa lisäävistä mutaatioista. Ne aiheuttavat von Willebrand -tekijän liiallisen sitoutumisen sekä suurten VWF-multimeerien ja verihiutaleiden liiallisen poistuman. Vika on siis verihiutale–VWF-akselilla, ei tekijä IX:n puutoksessa. Tekijä IX:n korvaushoidolle ei näin ollen ole selvää mekanistista perustetta.

Korkea pistemäärä on todennäköisesti verkkopohjainen ennuste, joka heijastaa vuotohäiriöiden välisiä yhteisiä assosiaatioita tietämysgraafissa, ei biologista perustetta.

Muut ennustetut käyttöaiheet noudattavat samaa kaavaa:

| Sija | Ennustettu käyttöaihe | Pistemäärä | Näytön taso | Arvio |
|------|------|------|------|------|
| 2 | Verihiutaleiden primaari vapautumishäiriö | 0,9942 | L5 | Tekijä IX ei korjaa verihiutaleiden sisäistä toimintahäiriötä |
| 3 | Glanzmannin trombasteenia | 0,9928 | L5 | Vika on integriini αIIbβ3:ssa; tekijä IX ei korjaa aggregaatiohäiriötä |

---

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004142 | Alprolix | – | Hemofilia B |

Myyntilupa on peruutettu, eikä Suomessa ole voimassa olevia myyntilupia. Valmistaja on Swedish Orphan Biovitrum AB (publ).

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkeinteraktioita ei löytynyt kyselyssä, eikä tietämysgraafista löytynyt vasta-aiheita.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-malliin (L5), eikä tukevia kliinisiä tutkimuksia tai julkaisuja ole. Kaikissa kolmessa ennustetussa käyttöaiheessa vika on verihiutaleissa tai VWF-akselilla, ei tekijä IX:ssä, joten mekanistinen peruste puuttuu. Lisäksi valmisteen myyntilupa on peruutettu.

**Jatkaminen edellyttäisi seuraavaa:**
- Vaikutusmekanismitietojen (MOA) täydentäminen DrugBankista
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivustolta, mikä on turvallisuusseulonnan edellytys
- Biologisen perusteen osoittaminen esikliinisillä tai mekanistisilla tutkimuksilla ennen kliinisiä suunnitelmia
- Reittien yhteensopivuuden ja ennustettujen käyttöaiheiden samankaltaisuuden arviointi alkuperäiseen käyttöaiheeseen nähden
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

