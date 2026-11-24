---
layout: default
title: Mepolizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 281
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
description: "Mepolizumab: ennustettu uusi käyttöaihe Immuunituhoon liittyvä trombosytopenia (thrombocytopenia due to immune destruction) (näytön taso L5). Alkuperäinen käyttöaihe: Asthma"
---

# Mepolizumab
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

## Mepolizumab: Immuunituhoon liittyvä trombosytopenia (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Yhden lauseen yhteenveto

Mepolitsumabi on anti-IL-5-vasta-aine, jota on alun perin käytetty astman hoitoon. TxGNN-malli ennustaa sen voivan olla hyödyllinen **immuunituhoon liittyvässä trombosytopeniassa**, mutta tätä tukee vain **yksi tapausselostus** eikä yhtään kliinistä tutkimusta. Näyttö on heikkoa, ja ennuste perustuu pääosin laskennalliseen mallinnukseen.

## Pikayhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Asthma |
| Ennustettu uusi käyttöaihe | Immuunituhoon liittyvä trombosytopenia (thrombocytopenia due to immune destruction) |
| TxGNN-ennustepisteet | 0,9966 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Mepolitsumabi on interleukiini-5:n (IL-5) vasta-aine, joka vähentää eosinofiilejä. Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Mepolizumab (epävirallinen käännös): ”Mepolitsumabi on IL-5:n antagonisti (IgG1-kappa). IL-5 on tärkein sytokiini, joka vastaa eosinofiilien kasvusta ja erilaistumisesta, rekrytoinnista, aktivaatiosta ja eloonjäämisestä. Mepolitsumabi sitoutuu IL-5:een dissosiaatiovakiolla 100 pM ja estää IL-5:n biologista aktiivisuutta salpaamalla sen sitoutumisen eosinofiilien solupinnalla ilmentyvän IL-5-reseptorikompleksin alfaketjuun.” Englanninkielinen alkuteksti: "Mepolizumab is an IL-5 antagonist (IgG1 kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Mepolizumab binds to IL-5 with a dissociation constant of 100 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil cell surface." ([DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea), versio 2025-08-06; haettu 2026-11-19). Tiedossa olevan perusteella lääke tehoaa astmaan eosinofiilitulehduksen vähentämisen kautta.

Ainoa tukeva kirjallisuuslöydös on tapausselostus, jossa steroidille resistentti hypereosinofiilinen immuunihäiriö ja samanaikainen sekamuotoinen trombottinen mikroangiopatia paranivat mepolitsumabihoidolla. Tämä viittaa mahdolliseen yhteyteen eosinofiilivälitteisen immuunihäiriön ja immuunivälitteisten sytopenioiden välillä, mutta yhteys on epäsuora.

Immuunitrombosytopeniassa verihiutaleiden tuho johtuu pääasiassa autovasta-aineista ja T-soluista, ei eosinofiileistä. Mekanistinen peruste on siksi heikko muualla kuin eosinofiliaan liittyvissä tapauksissa. Erittäin korkea TxGNN-pistemäärä on laskennallinen ennuste, ei kliinistä näyttöä.

## Kliinisen tutkimuksen näyttö

Ei tällä hetkellä aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Tapausselostus | Blood Cells Mol Dis | Steroidiresistentti hypereosinofiilinen immuunihäiriö ja samanaikainen sekamuotoinen trombottinen mikroangiopatia paranivat mepolitsumabilla. |

## Muut ennustetut käyttöaiheet

Aineistossa on myös muita ennusteita, joilla on vielä heikompi tuki:

| Ennustettu käyttöaihe | TxGNN-pisteet | Näytön taso | Huomio |
|------|------|------|------|
| Verihiutaleiden primaarinen vapautumishäiriö | 0.9961 | L5 | Ainoa lähde on hypereosinofiilisen oireyhtymän (HES) hoitoa käsittelevä katsaus ([PMID 20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/), 2010), joka ei käsittele verihiutaleiden toimintaa. IL-5:n eston ja verihiutaleiden eritysvikojen välillä ei tunneta mekanistista yhteyttä. |
| Pseudo-von Willebrandin tauti | 0.9944 | L5 | Johtuu verihiutaleiden GPIbα-reseptorin toiminnanlisäysmuutoksista. Yhteyttä IL-5:n estoon ei tunneta. Ei tutkimuksia eikä kirjallisuutta. |
| Autoimmuuni trombosytopenia | 0.9933 | L5 | Todennäköisesti päällekkäinen immuunitrombosytopenian kanssa. Ei tutkimuksia eikä kirjallisuutta. Perustelu on spekulatiivinen. |
| Glanzmannin trombastenia | 0.9928 | L5 | Perinnöllinen verihiutaleiden integriini αIIbβ3:n vika. Uskottavaa mekanistista yhteyttä ei ole. Ei kliinistä näyttöä. |

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/003860 | Nucala | Mepolizumab | Asthma | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Aineistossa ei ole tietoa yhteisvaikutuksista.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu lähes kokonaan laskennalliseen malliin. Tukena on vain yksi tapausselostus eikä yhtään kliinistä tutkimusta, ja mekanistinen yhteys immuunitrombosytopeniaan on heikko.

<!-- review:begin fi-lic-20261106-mepolizumab-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Tukena on vain yksi tapausselostus eikä yhtään kliinistä tutkimusta, ja mekanistinen yhteys immuunitrombosytopeniaan on heikko. / Myyntilupa Suomessa on peruutettu, mikä rajoittaa käytännön etenemismahdollisuuksia.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-mepolizumab-1 -->

**Eteneminen edellyttää seuraavaa:**
- Vaikutusmekanismia koskevien tietojen täydentäminen
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvittäminen Fimean lähteistä (turvallisuusarvioinnin estävä tietoaukko)
- Systemaattinen kirjallisuushaku immuunitrombosytopeniasta, erityisesti eosinofiliaan liittyvistä tapauksista
- Prekliininen tai mekanistinen tutkimus IL-5-eston roolista verihiutaleiden immuunituhossa

<!-- review:begin fi-lic-20261106-mepolizumab-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Prekliininen tai mekanistinen tutkimus IL-5-eston roolista verihiutaleiden immuunituhossa / Myyntilupatilanteen selvittäminen (peruutuksen syy ja mahdollinen uusi lupa)” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-mepolizumab-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Myyntilupa Suomessa on peruutettu, mikä rajoittaa käytännön etenemismahdollisuuksia” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Myyntilupatilanteen selvittäminen (peruutuksen syy ja mahdollinen uusi lupa)” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Nucala (EMEA/H/C/003860) on voimassa, ei peruutettu | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

