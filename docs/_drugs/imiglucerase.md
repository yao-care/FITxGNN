---
layout: default
title: Imiglucerase
parent: Pelkkä mallin ennuste (L5)
nav_order: 224
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "IMIGLUCERASE"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
description: "Imiglucerase: ennustettu uusi käyttöaihe Hurler syndrome (näytön taso L5). Alkuperäinen käyttöaihe: Gaucher Disease"
---

# Imiglucerase
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

## Imiglucerase: Hurler syndrome
{: .text-alpha }

## Yhteenveto

Imiglusidaasi on rekombinantti glukoserebrosidaasientsyymi, jota on alun perin käytetty **Gaucherin taudin** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **Hurlerin oireyhtymään** (MPS I), mutta ennuste perustuu vain mallilaskentaan: kliinisiä tutkimuksia ei ole, ja aiheeseen liittyy vain **1 yleiskatsaus** entsyymikorvaushoidoista, jossa ei ole imiglusidaasikohtaista tietoa MPS I:stä.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Gaucher Disease |
| Ennustettu uusi käyttöaihe | Hurler syndrome |
| TxGNN-ennustepisteet | 0.9952 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voi vaikuttaa uskottavalta?

Imiglusidaasi on rekombinantti glukoserebrosidaasi (beetaglukosidaasi), joka hydrolysoi glukosyyliseramidia ja korvaa puuttuvaa entsyymiä Gaucherin taudissa. Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Imiglucerase (epävirallinen käännös): ”Gaucherin taudille on tunnusomaista β-glukoserebrosidaasiaktiivisuuden puutos, joka johtaa glukoserebrosidin kertymiseen eri kudoksiin, kuten maksaan, pernaan ja luuytimeen. Imigluseraasin mannoosisokerit välittävät sen sitoutumista soluihin, kuten makrofageihin, ja sen internalisaatiota niihin.” Englanninkielinen alkuteksti: "Gaucher disease is characterized by a deficiency of β-glucocerebrosidase activity, which results in accumulation of glucocerebroside in various tissues including liver, spleen, and bone marrow. The mannose sugars on imiglucerase mediate binding to and internalization by cells including macrophages." ([DailyMed: Cerezyme (imiglucerase) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df60f030-866b-4374-a31f-8ae3f6b45c38), versio 2026-08-27; haettu 2026-11-19).

Hurlerin oireyhtymä (MPS I) johtuu alfa-L-iduronidaasin puutteesta, mikä johtaa glykosaminoglykaanien (dermataani- ja heparaanisulfaatti) kertymiseen. Sekä Gaucherin tauti että MPS I ovat lysosomaalisia kertymäsairauksia, joita hoidetaan entsyymikorvauksella. Yhteys on kuitenkin vain tasolla "entsyymikorvaushoidon periaate".

Mekanistisesti ennuste on heikko: entsyymi ja substraatti ovat eri, joten imiglusidaasin ei voida odottaa korjaavan MPS I:n perusvikaa. Korkea pistemäärä heijastaa todennäköisesti lysosomaalisten kertymäsairauksien läheisyyttä tietoverkossa, ei todellista entsymaattista päällekkäisyyttä. MPS I:n hyväksytty hoito on laronidaasi.

## Muut ennustetut käyttöaiheet

| Sija | Sairaus | Pisteet | Näytön taso | Arvio |
|---|---|---|---|---|
| 2 | Scheien oireyhtymä | 0.9929 | L5 | MPS I:n lievä muoto; sama puute kuin Hurlerin oireyhtymässä, ei suoraa näyttöä |
| 3 | Lisämunuaisen hyvänlaatuinen kasvain | 0.9928 | L5 | Uskottavaa mekanistista yhteyttä ei tunnistettu |
| 4 | Autosomaalinen ikytoosioireyhtymä, kuolemaan johtava kulku | 0.9924 | L5 | Heikko, spekulatiivinen yhteys ihon seramidiaineenvaihdunnan kautta; suonensisäinen hoito tuskin tavoittaa orvaskettä |
| 5 | Kolesterolinestereiden kertymätauti | 0.9912 | L5 | Aiheuttaja on lysosomaalisen happaman lipaasin puute; erityishoito on sebelipaasi alfa |

Kaikkien suositus on toistaiseksi Hold.

## Kliininen tutkimusnäyttö

Hurlerin oireyhtymään liittyviä kliinisiä tutkimuksia ei ole tällä hetkellä rekisteröity.

<!-- review:begin fi-lic-20261106-imiglucerase-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Tämä myyntilupa on tilassa "peruutettu", eikä voimassa olevia myyntilupia ole.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-imiglucerase-1 -->

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Katsaus | La Revue de médecine interne | Yleiskatsaus lysosomaalisten kertymäsairauksien entsyymikorvaushoidosta. Kuvaa, kuinka istukasta eristetty alglukeraasi ja sittemmin rekombinantti imiglusidaasi avasivat tien entsyymikorvaushoidoille. Ei imiglusidaasikohtaista tietoa MPS I:stä. |

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000157 | Cerezyme | imiglucerase | Gaucher Disease | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Yksi kohtalaisen tason yhteisvaikutus on tunnistettu miglustaatin kanssa (lähde: DDInter).

Muuten turvallisuustiedot on luettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain tietoverkon läheisyyteen. Imiglusidaasi ei korvaa MPS I:ssä puuttuvaa alfa-L-iduronidaasia, kliinisiä tutkimuksia ei ole, ainoa kirjallisuuslähde on yleinen katsaus ja MPS I:lle on jo olemassa spesifinen hoito (laronidaasi).

<!-- review:begin fi-lic-20261106-imiglucerase-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Imiglusidaasi ei korvaa MPS I:ssä puuttuvaa alfa-L-iduronidaasia, kliinisiä tutkimuksia ei ole, ainoa kirjallisuuslähde on yleinen katsaus ja MPS I:lle on jo olemassa spesifinen hoito (laronidaasi). Myös Suomen myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-imiglucerase-2 -->

**Jatkoa varten tarvitaan:**
- Yksityiskohtainen vaikutusmekanismitieto (esim. DrugBankista)
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimea), jotta turvallisuusarvio voidaan tehdä
- Prekliininen näyttö siitä, onko imiglusidaasilla mitään vaikutusta glykosaminoglykaanien kertymiseen
- Vertailu laronidaasiin hoitovaihtoehtona

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Tämä myyntilupa on tilassa "peruutettu", eikä voimassa olevia myyntilupia ole” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Myös Suomen myyntilupa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Cerezyme (imiglucerase) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df60f030-866b-4374-a31f-8ae3f6b45c38) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

