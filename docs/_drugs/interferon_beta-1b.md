---
layout: default
title: Interferon Beta-1B
parent: Pelkkä mallin ennuste (L5)
nav_order: 236
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Interferon Beta-1B: ennustettu uusi käyttöaihe Harvinaissoluleukemia (hairy cell leukemia) (näytön taso L5). Alkuperäinen käyttöaihe: Multippeliskleroosi"
monitor_inn: "INTERFERON BETA-1B"
predicted_indications: ["hairy cell leukemia", "autoimmune disease of central nervous system"]
---

# Interferon Beta-1B
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

## Interferoni beeta-1b: Multippeliskleroosista harvinaissoluleukemiaan
{: .text-alpha }

## Yhden lauseen yhteenveto

Interferoni beeta-1b on lääke, jota on alun perin käytetty multippeliskleroosin (MS) hoitoon. TxGNN-malli ennustaa sen voivan tehota **harvinaissoluleukemiaan** (hairy cell leukemia), mutta ennusteelle ei löydy tukea: **kliinisiä tutkimuksia ei ole lainkaan** eikä **kirjallisuutta** ole saatavilla. Ennuste perustuu pelkästään laskennalliseen malliin.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Multippeliskleroosi |
| Ennustettu uusi käyttöaihe | Harvinaissoluleukemia (hairy cell leukemia) |
| TxGNN-ennusteen pistemäärä | 0,9916 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Interferon Beta-1B (epävirallinen käännös): ”BETASERON-valmisteen (beeta-1b-interferoni) vaikutusmekanismia MS-tautia sairastavilla potilailla ei tunneta.” Englanninkielinen alkuteksti: "The mechanism of action of BETASERON (interferon beta-1b) in patients with multiple sclerosis is unknown." ([DailyMed: Betaseron (interferon beta-1b) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5), versio 2026-03-03; haettu 2026-11-19). Tunnetun tiedon perusteella interferoni beeta-1b on tyypin I interferoni, jolla on immuunivastetta muokkaavia vaikutuksia MS:ssä. Sen tehosta MS:n hoidossa on olemassa vahvaa näyttöä.

Mekanistinen yhteys harvinaissoluleukemiaan on epäsuora. Interferoni alfa on historiallisesti ollut käytössä harvinaissoluleukemian hoidossa, ja tyypin I interferoneilla on luokkatasolla immuunivastetta muokkaavia ja solujen jakautumista estäviä vaikutuksia. Tämä voi selittää mallin ennusteen. Tämä päätelmä ei kuitenkaan perustu raporttia varten koottuun aineistoon, eikä interferoni beeta-1b:lle itselleen ole tässä aineistossa tukevaa näyttöä tähän käyttöaiheeseen.

Ennuste on siis pelkkä laskennallinen signaali. Sitä ei voida pitää kliinisesti varmennettuna.

---

## Kliinisen tutkimuksen näyttö

Harvinaissoluleukemiaan ei tällä hetkellä ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

*Huomio:* Toiseksi sijoittuneelle ennusteelle (keskushermoston autoimmuunisairaus) löytyi tutkimuksia, mutta ne koskevat lähes yksinomaan lääkkeen nykyistä MS-käyttöaihetta eivätkä siten ole uutta käyttöaihetta tukevaa näyttöä. Merkittävin niistä on vaiheen 3 BENEFIT-jatkotutkimus NCT00185211 (468 osallistujaa, valmistunut).

---

## Kirjallisuusnäyttö

Harvinaissoluleukemiaan ei tällä hetkellä ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000081 | Betaferon | interferon beta-1b | Multiple Sclerosis | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 100 yhteisvaikutusta. Merkittävin on:
- **Bupropioni** (vakava, Major)

Muut luetellut yhteisvaikutukset ovat luokaltaan kohtalaisia (Moderate), esimerkiksi:
- Pioglitatsoni ja rosiglitatsoni
- Simvastatiini ja rosuvastatiini
- Klaritromysiini ja levofloksasiini
- Naltreksoni
- Minosykliini
- Anaboliset steroidit (oksandrolooni, oksimetoloni, stanotsololi)

Muiden turvallisuustietojen osalta tutustu valmisteyhteenvetoon.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennusteen pistemäärä on korkea (0,9916), mutta harvinaissolulleukemiaan ei ole kliinisiä tutkimuksia eikä kirjallisuutta, joten näyttötaso on L5 (vain mallin ennuste).

<!-- review:begin fi-lic-20261106-interferon_beta-1b-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ennusteen pistemäärä on korkea (0,9916), mutta harvinaissolulleukemiaan ei ole kliinisiä tutkimuksia eikä kirjallisuutta, joten näyttötaso on L5 (vain mallin ennuste). Lisäksi Betaferonin myyntilupa Suomessa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-interferon_beta-1b-1 -->

**Eteenpäin siirtyminen edellyttää seuraavaa:**
- Vaikutusmekanismin (MOA) tietojen täydentäminen
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen ja analysointi (Fimea) turvallisuusarviointia varten
- Prekliininen ja kirjallisuuteen perustuva selvitys interferoni beeta-1b:n vaikutuksesta harvinaissolulleukemiassa sekä vertailu interferoni alfaan
- Reittien ja lääkemuotojen yhteensopivuuden arviointi
- Myyntiluvan tilanteen selvittäminen

<!-- review:begin fi-lic-20261106-interferon_beta-1b-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntiluvan tilanteen selvittäminen (nykyinen lupa on peruutettu)” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-interferon_beta-1b-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi Betaferonin myyntilupa Suomessa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”(nykyinen lupa on peruutettu)” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Betaferon (EMEA/H/C/000081) on voimassa, ei peruutettu | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Betaseron (interferon beta-1b) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

