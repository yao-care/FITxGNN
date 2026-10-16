---
layout: default
title: Amifampridine
parent: Pelkkä mallin ennuste (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Amifampridine: ennustettu uusi käyttöaihe Glaukooma (näytön taso L5). Alkuperäinen käyttöaihe: Lambert-Eatonin myasteeninen oireyhtymä"
---

# Amifampridine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Amifampridiini: Lambert-Eatonin myasteenisesta oireyhtymästä glaukoomaan

## Yhteenveto

Amifampridiini on lääke, jota on alun perin käytetty Lambert-Eatonin myasteenisen oireyhtymän (LEMS) hoitoon. TxGNN-malli ennustaa sen voivan tehota **glaukoomaan**, mutta ennustetta tukevat vain mallilaskelmat: tähän mennessä kerätyissä tiedoissa ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Lambert-Eatonin myasteeninen oireyhtymä |
| Ennustettu uusi käyttöaihe | Glaukooma |
| TxGNN-ennustepisteet | 99,71 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 2 (molemmat peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Tässä raportissa käytetyistä tiedoista ei ole saatavilla yksityiskohtaista vaikutusmekanismia. Yleisen farmakologisen tiedon mukaan amifampridiini (3,4-diaminopyridiini) salpaa jänniteherkkiä kaliumkanavia, pidentää presynaptista depolarisaatiota ja lisää asetyylikoliinin vapautumista hermo-lihasliitoksessa. Tämä selittää sen tehon LEMS-taudissa.

Yhteys glaukoomaan on toistaiseksi vain teoreettinen. Se voisi liittyä hermosolujen ärtyvyyden tai verkkokalvon gangliosolujen toiminnan muokkaamiseen, mutta tätä tukevaa mekanistista tietoa ei ole. Alkuperäisen ja uuden käyttöaiheen samankaltaisuutta ei ole arvioitu. Silmään annosteluun ei myöskään ole perustetta, ja reittien yhteensopivuus on arvioimatta.

Toinen mallin ennustama käyttöaihe on akuutti ajoittainen porfyria (pistemäärä 99,32 %). Sekin on pelkkä mallin ennuste ilman kliinistä tai kirjallisuusnäyttöä. Amifampridiinin kouristuskynnystä laskeva vaikutus on huolenaihe tässä taudissa, koska akuuteissa kohtauksissa voi esiintyä kouristuksia.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005839 | Amifampridine SERB | – | Lambert-Eatonin myasteeninen oireyhtymä; paraneoplastiset oireyhtymät, hermoston; hermoston kasvaimet; paraneoplastiset oireyhtymät; hermoston sairaudet... |
| EMEA/H/C/001032 | Firdapse (aiemmin Zenas) | – | Lambert-Eatonin myasteeninen oireyhtymä |

Molemmat myyntiluvat on peruutettu, joten valmistetta ei tällä hetkellä ole voimassa olevalla myyntiluvalla.

## Turvallisuusnäkökohdat

- **Lääkeaineyhteisvaikutukset:** Tietokannasta löytyi yhteensä 68 yhteisvaikutusta. Vakavuudeltaan **merkittäväksi (Major)** luokiteltu on bupropioni. Muut esimerkit ovat **kohtalaisia (Moderate)**:
  - kortikosteroidit: hydrokortisoni, betametasoni, deksametasoni, prednisoloni, prednisoni
  - ruokahalua hillitsevät ja stimuloivat lääkkeet: fentermiini, fenfluramiini, deksfenfluramiini, dietyylipropioni, matsindoli, sibutramiini, efedriini
  - opioidit: morfiini, oopiumi
  - muut: levofloksasiini, metoklopramidi, dronabinoli, polyetyleeniglykoli (elektrolyyteillä)
- **Yleinen huomio:** Systeeminen kaliumkanavan salpaus voi lisätä kouristus- ja sydänriskejä. Tämä perustuu farmakologiseen arvioon, ei pakkausselosteen tietoon.

Muista varoituksista ja vasta-aiheista tietoja ei ole saatavilla. Tarkista ne valmisteyhteenvedosta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-mallin pisteisiin (näytön taso L5). Kliinisiä tutkimuksia, kirjallisuutta tai mekanistista tukea ei ole.
- Kouristusriski, 68 yhteisvaikutusta ja peruutetut myyntiluvat lisäävät kehitystyön epävarmuutta.

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismin tietojen täydentämistä (esim. DrugBankista).
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimeasta ja turvallisuusarviota ennen jatkoa.
- Prekliinisiä tai mekanistisia tutkimuksia amifampridiinin ja glaukooman yhteydestä.
- Antoreitin ja silmään kohdistuvan annostelun arviointia.
- Markkinatilanteen selvittämistä, koska voimassa olevia myyntilupia ei ole.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

