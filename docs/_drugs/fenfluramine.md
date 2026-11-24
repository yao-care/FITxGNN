---
layout: default
title: Fenfluramine
parent: Pelkkä mallin ennuste (L5)
nav_order: 186
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Fenfluramine: ennustettu uusi käyttöaihe Proksimaalinen 16p11.2-mikrodeleetiosyndrooma (näytön taso L5). Alkuperäinen käyttöaihe: Myokloniset epilepsiat"
monitor_inn: "Fenfluramine"
predicted_indications: ["proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "obsolete hypertelorism (disease)", "frontorhiny"]
---

# Fenfluramine
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

## Fenfluramiini: Proksimaalinen 16p11.2-mikrodeleetiosyndrooma
{: .text-alpha }

## Yhteenveto

Fenfluramiini oli alun perin painonhallintaan kehitetty serotonerginen lääkeaine, jota käytetään nykyisin epilepsian hoitoon (Fintepla). Suomessa lupatiedoissa indikaationa on myokloniset epilepsiat.
TxGNN-malli ennustaa lääkkeen voivan sopia **proksimaalisen 16p11.2-mikrodeleetiosyndrooman** hoitoon, mutta ennusteen tukena ei ole yhtään kliinistä tutkimusta eikä julkaisua. Ennuste perustuu **pelkästään mallilaskentaan**.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Myokloniset epilepsiat |
| Ennustettu uusi käyttöaihe | Proksimaalinen 16p11.2-mikrodeleetiosyndrooma |
| TxGNN-ennusteen pistemäärä | 0,9993 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Fenfluramine (epävirallinen käännös): ”Fenfluramiinin tarkkaa vaikutusmekanismia Dravet'n oireyhtymään ja Lennox–Gastaut'n oireyhtymään liittyvien kohtausten hoidossa ei tunneta. Fenfluramiinilla ja sen metaboliitilla, norfenfluramiinilla, on agonistivaikutusta serotoniinin 5-HT2-reseptoreissa.” Englanninkielinen alkuteksti: "The precise mechanism by which fenfluramine exerts its therapeutic effects in the treatment of seizures associated with Dravet syndrome and Lennox-Gastaut syndrome is unknown. Fenfluramine and the metabolite, norfenfluramine, exhibit agonist activity at serotonin 5-HT2 receptors." ([DailyMed: Fintepla (fenfluramine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d), versio 2026-10-22; haettu 2026-11-19). Tunnetun tiedon perusteella fenfluramiini vapauttaa serotoniinia ja sillä on vaikutusta sigma-1-reseptoriin. Sen teho kehitykseen liittyvissä ja epileptisissä enkefalopatioissa on osoitettu, ja mekanistisesti se voisi olla sovellettavissa myös uuteen käyttöaiheeseen. Lisäksi lääkkeen farmakologisessa tietokannassa mainitaan kohteina tryptofaanihydroksylaasi 1 ja 2 (TPH1, TPH2), mutta kohteen vaikutuksesta ei ole julkisesti saatavilla biologista aktiivisuusdataa.

16p11.2-deleetio liittyy neurokehityksellisiin häiriöihin ja epileptisiin kohtauksiin. Yhteinen kohtausfenotyyppi voisi selittää mallin ennusteen. Tämä on kuitenkin vahvistamaton hypoteesi, ei kliinisesti todennettu yhteys.

Muut mallin korkealle pisteyttämät ennusteet (hypervitaminoosi, vanhentunut hypertelorismi, frontorhiny) vaikuttavat tietämysgraafin artefakteilta, eikä niille löydy uskottavaa farmakologista perustetta. Niitä ei suositella jatkotarkasteluun.

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/003933 | Fintepla | fenfluramine hydrochloride | Epilepsies, Myoclonic | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuushuomiot

- **Tietämysgraafiin perustuvat vasta-aiheet** (TxGNN/PrimeKG-graafin lääke–tauti-vasta-aihereunat, ei valmisteyhteenvedon teksti): verenpainetauti (hypertensio), päihteiden väärinkäyttö/riippuvuus, tyypin 2 diabetes, tyypin 1 diabetes, diabeettinen ketoasidoosi, glaukooma ja keuhkoverenpainetauti.
- **Yhteisvaikutukset**: Kyselyssä löytyi kaksi farmakologista kohdetta (TPH1 ja TPH2), mutta varsinaisia lääke–lääke-yhteisvaikutuksia ei ole luokiteltu.
- Lääkeaine poistettiin aikanaan markkinoilta painonhallintakäytössä. Tämän vuoksi sydän- ja keuhkoverenkiertoon liittyvät riskit (kuten keuhkoverenpainetauti) on huomioitava erityisen tarkasti.

Muilta osin turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu ainoastaan malliin (L5): kliinisiä tutkimuksia ja julkaisuja ei ole, ja mekanistinen yhteys on vahvistamaton hypoteesi. Tietämysgraafi tuo esiin merkittäviä vasta-aiheita.

<!-- review:begin fi-lic-20261106-fenfluramine-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa, ja tietämysgraafi tuo esiin merkittäviä vasta-aiheita.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-fenfluramine-1 -->

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta ja jäsentäminen Fimean sivustolta (estävä tietoaukko turvallisuusarvioinnin jatkamiselle)
- Yksityiskohtaiset vaikutusmekanismitiedot (MOA) esimerkiksi DrugBankista
- Kirjallisuushaku ja prekliiniset tutkimukset fenfluramiinista 16p11.2-deleetiomalleissa
- Selvitys antoreittien yhteensopivuudesta ja käyttöaiheen samankaltaisuudesta alkuperäiseen käyttöaiheeseen

<!-- review:begin fi-lic-20261106-fenfluramine-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Selvitys antoreittien yhteensopivuudesta ja käyttöaiheen samankaltaisuudesta alkuperäiseen käyttöaiheeseen / Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittäminen Suomessa” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-fenfluramine-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa, ja t” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittäminen Suomessa” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Fintepla (EMEA/H/C/003933) on voimassa, ei peruutettu | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Fintepla (fenfluramine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

