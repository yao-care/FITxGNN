---
layout: default
title: Eftrenonacog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
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

Valmistaja on Swedish Orphan Biovitrum AB (publ).

<!-- review:begin fi-lic-20261106-eftrenonacog_alfa-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntilupa on peruutettu, eikä Suomessa ole voimassa olevia myyntilupia. Valmistaja on Swedish Orphan Biovitrum AB (publ).” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-eftrenonacog_alfa-1 -->

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkeinteraktioita ei löytynyt kyselyssä, eikä tietämysgraafista löytynyt vasta-aiheita.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-malliin (L5), eikä tukevia kliinisiä tutkimuksia tai julkaisuja ole. Kaikissa kolmessa ennustetussa käyttöaiheessa vika on verihiutaleissa tai VWF-akselilla, ei tekijä IX:ssä, joten mekanistinen peruste puuttuu.

<!-- review:begin fi-lic-20261106-eftrenonacog_alfa-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikissa kolmessa ennustetussa käyttöaiheessa vika on verihiutaleissa tai VWF-akselilla, ei tekijä IX:ssä, joten mekanistinen peruste puuttuu. Lisäksi valmisteen myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-eftrenonacog_alfa-2 -->

**Jatkaminen edellyttäisi seuraavaa:**
- Vaikutusmekanismitietojen (MOA) täydentäminen DrugBankista
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivustolta, mikä on turvallisuusseulonnan edellytys
- Biologisen perusteen osoittaminen esikliinisillä tai mekanistisilla tutkimuksilla ennen kliinisiä suunnitelmia
- Reittien yhteensopivuuden ja ennustettujen käyttöaiheiden samankaltaisuuden arviointi alkuperäiseen käyttöaiheeseen nähden

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Myyntilupa on peruutettu, eikä Suomessa ole voimassa olevia myyntilupia” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi valmisteen myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

