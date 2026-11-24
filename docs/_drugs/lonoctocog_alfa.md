---
layout: default
title: Lonoctocog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 269
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Lonoctocog Alfa: ennustettu uusi käyttöaihe Pseudo-von Willebrandin tauti (verihiutaletyyppinen VWD) (näytön taso L5). Alkuperäinen käyttöaihe: Hemofilia A"
monitor_inn: "LONOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome"]
---

# Lonoctocog Alfa
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

## Lonoctokogi alfa: Hemofilia A:sta pseudo-von Willebrandin tautiin
{: .text-alpha }

## Yhteenveto

Lonoctokogi alfa on rekombinantti, yksiketjuinen ja B-domeenista typistetty hyytymistekijä VIII -valmiste, jota on alun perin käytetty **hemofilia A:n** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **pseudo-von Willebrandin tautiin** (pistemäärä 0,9985), mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hemofilia A |
| Ennustettu uusi käyttöaihe | Pseudo-von Willebrandin tauti (verihiutaletyyppinen VWD) |
| TxGNN-ennusteen pistemäärä | 0,9985 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Lonoctokogi alfa korvaa hemofilia A:ssa puuttuvan tekijä VIII:n aktiivisuuden. ChEMBL-tietokantaan (EMBL-EBI) on kirjattu valmisteen Lonoctocog Alfa vaikutusmekanismiksi (epävirallinen käännös): ”Hyytymistekijä VIII:n eksogeeninen proteiini”. Englanninkielinen alkuteksti: "Coagulation factor VIII exogenous protein" ([ChEMBL CHEMBL4594603 (lonoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594603), CC BY-SA 3.0; haettu 2026-11-19). Tunnetun tiedon perusteella lääke on rekombinantti FVIII-korvaushoito, jonka teho hemofilia A:ssa on osoitettu.

Pseudo-von Willebrandin taudissa vika on verihiutaleiden GPIbα-reseptorin toiminnan lisääntymisessä (gain-of-function). Tämä lisää reseptorin sitoutumista von Willebrand -tekijään (VWF), jolloin suurimolekyylisiä VWF-multimeerejä häviää ja verihiutaleita poistuu verenkierrosta. Teoreettinen yhteys on, että FVIII kiertää verenkierrossa VWF:hen sitoutuneena, joten FVIII-pitoisuus voi laskea VWF:n vähentyessä.

Ensisijainen vika on kuitenkin verihiutaleperäinen, eikä FVIII-korvaus korjaa sitä. Korkea TxGNN-pistemäärä on pelkkä laskennallinen ennuste, jota ei tue mekanistinen eikä kliininen aineisto.

Muut mallin ennustamat käyttöaiheet ovat samanlaisia:

| Ennustettu käyttöaihe | TxGNN-pistemäärä | Arvio mekanistisesta yhteydestä |
|------|------|------|
| Verihiutaleiden primaarinen vapautumishäiriö | 0,9984 | Lääke ei vaikuta verihiutaleiden granulaaritoimintaan; hyöty korkeintaan epäsuora |
| Glanzmannin trombastenia | 0,9976 | Vika on verihiutaleiden aggregaatiossa (αIIbβ3), FVIII-tasot ovat yleensä normaalit; perustetta tehoon ei löytynyt |
| Scottin oireyhtymä | 0,9944 | Käsitteellinen yhteys tenaasikompleksin kautta, mutta FVIII:n lisääminen ei korjaa puuttuvaa fosfatidyyliseriinipintaa |

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

<!-- review:begin fi-lic-20261106-lonoctocog_alfa-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntilupa on peruutettu, eikä voimassa olevia myyntilupia ole.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-lonoctocog_alfa-1 -->

---

## Tiedot Suomen markkinoilta

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/004075 | Afstyla | lonoctocog alfa | Hemophilia A | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkkeiden yhteisvaikutuksia ei löytynyt kyselyssä.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-malliin (L5), eikä tueksi ole kliinisiä tutkimuksia tai kirjallisuutta. Mekanistinen peruste on heikko, koska ensisijainen vika on verihiutaleperäinen.

<!-- review:begin fi-lic-20261106-lonoctocog_alfa-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Mekanistinen peruste on heikko, koska ensisijainen vika on verihiutaleperäinen. Lisäksi valmisteen myyntilupa Suomessa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-lonoctocog_alfa-2 -->

**Eteneminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen ja läpikäynti (Fimean sivusto), sillä ne puuttuvat ja estävät turvallisuusseulonnan
- Vaikutusmekanismitietojen täydentäminen (DrugBank)
- Kirjallisuushaku ja prekliiniset tutkimukset FVIII-korvauksen hyödystä verihiutaleperäisissä vuototaudeissa
- Selvitys valmisteen saatavuudesta ja myyntiluvan tilasta Suomessa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Myyntilupa on peruutettu, eikä voimassa olevia myyntilupia ole” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi valmisteen myyntilupa Suomessa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella (päivitetty 2026-11-20; aiempi versio tallessa lokissa) | [ChEMBL CHEMBL4594603 (lonoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594603) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

