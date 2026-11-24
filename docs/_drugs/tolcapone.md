---
layout: default
title: Tolcapone
parent: Pelkkä mallin ennuste (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Tolcapone: ennustettu uusi käyttöaihe Rasmussenin subakuutti enkefaliitti (näytön taso L5). Alkuperäinen käyttöaihe: Parkinsonin tauti"
monitor_inn: "TOLCAPONE"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome", "paralysis agitans, juvenile, of Hunt"]
---

# Tolcapone
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

## Tolkaponi: Rasmussenin subakuutti enkefaliitti
{: .text-alpha }

## Yhden lauseen yhteenveto

Tolkaponi on COMT-estäjä, jota on alun perin käytetty Parkinsonin taudin hoitoon. TxGNN-malli ennustaa sen voivan tehota **Rasmussenin subakuuttiin enkefaliittiin**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään mallin laskemaan pisteytykseen.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Parkinsonin tauti |
| Ennustettu uusi käyttöaihe | Rasmussenin subakuutti enkefaliitti |
| TxGNN-ennustepisteet | 0,9993 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Tolcapone (epävirallinen käännös): ”Tolkaponi on katekoli-O-metyylitransferaasin (COMT) selektiivinen ja palautuva estäjä. Nisäkkäillä COMT:tä on eri elimissä. Suurin aktiivisuus on maksassa ja munuaisissa. COMT:tä esiintyy myös sydämessä, keuhkoissa, sileissä lihaksissa ja luustolihaksissa, suolistossa, lisääntymiselimissä, eri rauhasissa, rasvakudoksessa, ihossa, verisoluissa ja hermokudoksissa, erityisesti gliasoluissa.” Englanninkielinen alkuteksti: "Tolcapone is a selective and reversible inhibitor of catechol- O -methyltransferase (COMT). In mammals, COMT is distributed throughout various organs. The highest activities are in the liver and kidney. COMT also occurs in the heart, lung, smooth and skeletal muscles, intestinal tract, reproductive organs, various glands, adipose tissue, skin, blood cells and neuronal tissues, especially in glial cells." ([DailyMed: Tasmar (tolcapone) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0e47a9d-78e7-4523-983a-aa259f221736), versio 2020-10-02; haettu 2026-11-19). Tiedetään kuitenkin, että tolkaponi on COMT-entsyymin (katekoli-O-metyylitransferaasi) estäjä, joka pidentää levodopan vaikutusta Parkinsonin taudissa.

Rasmussenin enkefaliitti on autoimmuuni- ja tulehdusperäinen aivosairaus. Koottujen tietojen perusteella COMT:n eston tai katekoliamiiniaineenvaihdunnan ja tämän taudin patologian välille ei ole osoitettu uskottavaa yhteyttä. Korkea pistemäärä (0,999) on siis mallin ennuste, jota ei tue mekanistinen tai kliininen näyttö.

Muista ennustetuista käyttöaiheista kaksi on mekanistisesti uskottavampia:
- **Lewyn kappale -dementia**: jakaa alfa-synukleiinipatologian ja dopaminergisen vajauksen Parkinsonin taudin kanssa. Ainoa löydetty julkaisu (PMID 39259788) on prekliininen iPSC-organoidimalli, ei potilastutkimus.
- **Juveeli parkinsonismi (paralysis agitans, juvenile, of Hunt)**: kyse on käytännössä Parkinsonin tautiin liittyvästä historiallisesta nimikkeestä, joten käyttö kuuluisi nykyisen käyttöaiheen piiriin eikä olisi todellista lääkkeen uudelleenkäyttöä.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole aiheeseen liittyvää kirjallisuutta Rasmussenin enkefaliitin osalta.

---

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000132 | Tasmar | tolcapone | Parkinson Disease | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuushuomiot

- **Tietämysgraafiin perustuvat vasta-aiheet** (TxGNN/PrimeKG, ei valmisteyhteenvetoteksti): maksasairaus, sappirakon sairaus, melanooma, hypotensio, rabdomyolyysi, nodulaarinen fasciitti, tardiivi dyskinesia sekä kielen, kasvojen ja posken dyskinesia.
- **Lääkeyhteisvaikutukset**: yhteensä 65 tunnistettua yhteisvaikutusta. Merkittävin on **metyleenisininen (Major)**. Keskivaikeita (Moderate) ovat mm. epinefriini, morfiini, kodeiini, dronabinoli, nabiloni, naltreksoni, metoklopramidi, prometatsiini, klooripfeniramiini, setiritsiini, dekstrometorfaani, oopiumi ja etanoli. Lieviä (Minor) ovat varfariini ja dikumaroli.
- **Maksatoksisuus**: tolkaponin käyttöä on rajoitettu maksatoksisuushistorian vuoksi, mikä on erityinen huolenaihe esimerkiksi maksaan vaikuttavissa sairauksissa.

Valmisteyhteenvedon varoitus- ja vasta-aihetiedot puuttuvat, joten ne on tarkistettava Fimean valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste on puhtaasti malliperusteinen (L5), eikä kliinistä tai kirjallisuusnäyttöä ole. Mekanistista yhteyttä COMT:n estoon ei ole osoitettu.

<!-- review:begin fi-lic-20261106-tolcapone-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Mekanistista yhteyttä COMT:n estoon ei ole osoitettu, ja tolkaponin maksaturvallisuushuoli sekä myyntilupien peruuntuminen Suomessa heikentävät asemaa entisestään.” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-tolcapone-1 -->

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismitietojen (MOA) täydentämistä esimerkiksi DrugBankista
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivustolta
- Prekliinistä tai kliinistä näyttöä COMT:n eston vaikutuksesta Rasmussenin enkefaliittiin
- Jos tavoitteena on uskottavampi suunta, Lewyn kappale -dementian arviointia kliinisen näytön näkökulmasta
- Maksaturvallisuuden seurantasuunnitelmaa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”ja tolkaponin maksaturvallisuushuoli sekä myyntilupien peruuntuminen Suomessa heikentävät asemaa entisestään” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Tasmar (tolcapone) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0e47a9d-78e7-4523-983a-aa259f221736) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

