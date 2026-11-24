---
layout: default
title: Trabectedin
parent: Pelkkä mallin ennuste (L5)
nav_order: 448
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "TRABECTEDIN"
predicted_indications: ["female breast carcinoma"]
description: "Trabectedin: ennustettu uusi käyttöaihe Female breast carcinoma (näytön taso L5). Alkuperäinen käyttöaihe: Sarcoma"
---

# Trabectedin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

## Trabectedin: Female breast carcinoma
{: .text-alpha }

## Yhteenveto

Trabektediini on solunsalpaaja, jota on käytetty pehmytkudossarkooman ja munasarjasyövän hoitoon. TxGNN-malli ennustaa, että se voisi tehota **naispuoliseen rintasyöpään**. Aihetta tukee tällä hetkellä **1 kliininen tutkimus** (jonka yhteys rintasyövän tehoon on epävarma) ja **20 julkaisua**, joista osa on satunnaistettuja vaiheen 2 tutkimuksia.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Sarcoma;Ovarian Neoplasms; Ovarian Neoplasms;Sarcoma |
| Ennustettu uusi käyttöaihe | Female breast carcinoma |
| TxGNN-ennustepistemäärä | 0.9973 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 2/2) |
| Myyntilupien määrä | 2 (voimassa: 2) |
| Suositeltu päätös | Hold (odotetaan lisänäyttöä) |

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Trabectedin (epävirallinen käännös): ”Trabektediini on alkyloiva lääkeaine, joka sitoutuu DNA:n pienen uurteen guaniinitähteisiin muodostaen addukteja, mikä johtaa DNA-kierteen taipumiseen kohti suurta uurretta. Adduktien muodostuminen käynnistää tapahtumaketjun, joka voi vaikuttaa DNA:ta sitovien proteiinien, mukaan lukien joidenkin transkriptiotekijöiden, myöhempään aktiivisuuteen sekä DNA:n korjausreitteihin, mikä johtaa solusyklin häiriintymiseen ja lopulta solukuolemaan.” Englanninkielinen alkuteksti: "Trabectedin is an alkylating drug that binds guanine residues in the minor groove of DNA, forming adducts and resulting in a bending of the DNA helix towards the major groove. Adduct formation triggers a cascade of events that can affect the subsequent activity of DNA binding proteins, including some transcription factors, and DNA repair pathways, resulting in perturbation of the cell cycle and eventual cell death." ([DailyMed: Evdi (trabectedin) prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c1d50f5c-4202-27f3-4798-a9708114ddea), versio 2026-06-29; haettu 2026-11-19). Alla oleva mekanistinen perustelu on johdettu kirjallisuudesta ja yleistiedosta, ei toimitetuista lähtötiedoista.

Trabektediini sitoutuu DNA:n pieneen uraan ja aiheuttaa DNA-vaurioita. Se on erityisen tehokas soluissa, joiden homologinen rekombinaatiokorjaus on puutteellinen (esim. BRCA1/2-puutos). Lisäksi se muokkaa kasvaimen mikroympäristöä vähentämällä kasvaimeen liittyviä makrofageja ja vaikuttaa transkriptiotekijöiden toimintaan.

Alkuperäiset käyttöaiheet (sarkooma, munasarjasyöpä) jakavat osittain saman DNA-vaurio- ja mikroympäristöbiologian rintasyövän kanssa. Siksi laajennus on mekanistisesti johdonmukainen, erityisesti BRCA-puutteisissa ja kolmoisnegatiivisissa rintasyövissä. Esikliininen tutkimus trabektediinin ja IL-12:n yhdistelmästä kolmoisnegatiivisessa rintasyövässä tukee tätä.

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Vaihe 2 | Päättynyt | 76 | Arvioitiin trabektediinin kerta-annoksen vaikutusta EKG:n QT-aikaan edenneissä kiinteissä kasvaimissa. Kyseessä on turvallisuus-/farmakologiatutkimus, ei tehotutkimus rintasyövässä. |

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Satunnaistettu vaiheen 2 tutkimus | Clin Breast Cancer | Trabektediini monoterapiana edenneessä rintasyövässä antrasykliini- ja taksaanihoidon jälkeen; verrattiin kahta antoaikataulua. |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Vaiheen 2 tutkimus | Ann Oncol | Teho germinaalisesti BRCA1/2-mutatoituneessa metastaattisessa rintasyövässä. |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Vaiheen 2 tutkimus | Clin Breast Cancer | Teho hormonireseptoripositiivisessa, HER2-negatiivisessa edenneessä rintasyövässä XPG-ekspression mukaan. |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Vaiheen 1 tutkimus | Eur J Cancer | Trabektediinin ja doksorubisiinin yhdistelmä sarkoomassa ja edenneessä rintasyövässä (38 potilasta, 9 rintasyöpäpotilasta). |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Katsaus | Expert Opin Investig Drugs | Trabektediini rintasyövän hoidossa; vaikutus transkriptioon ja makrofagien vähentäminen. |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Katsaus | Cancer Treat Rev | Trabektediini BRCA-puutteisilla potilailla. |
| [18410797](https://pubmed.ncbi.nlm.nih.gov/18410797/) | 2008 | Katsaus | Semin Oncol | Uudet lääkkeet antrasykliini- ja taksaaniresistentissä metastaattisessa rintasyövässä. |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Esikliininen | Cancer Immunol Res | Trabektediini vahvistaa IL-12:n kasvainvastaista vaikutusta kolmoisnegatiivisessa rintasyövässä. |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Esikliininen | Eur Cytokine Netw | Trabektediinin antiangiogeeniset vaikutukset rintasyöpäsoluissa. |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Esikliininen | Toxicol Lett | Apoptoosin induktio MCF-7- ja MDA-MB-453-rintasyöpäsoluissa. |

## Myyntiluvat Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000773 | Yondelis | trabectedin | Ovarian Neoplasms; Sarcoma | Voimassa |
| EMEA/H/C/006433 | Trabectedin Accord | trabectedin | Sarcoma; Ovarian Neoplasms | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Perinteinen sytotoksinen lääke (DNA:n alkyloiva, merellistä alkuperää) |
| Myelosuppression riski | Korkea: kirjallisuuden mukaan 3.–4. asteen neutropeniaa noin 50 %:lla ja trombosytopeniaa noin 20 %:lla potilaista; myös maksatoksisuutta |
| Oksettavuusluokitus | Tietoa ei ole saatavilla; katso valmisteyhteenveto |
| Seurantakohteet | Verenkuva (erittelylaskenta), maksa-arvot, munuaisten toiminta; QT-aikaan liittyviä tutkimuksia on tehty |
| Käsittelysuojaus | Noudatettava sytotoksisten lääkkeiden käsittelyohjeita |

## Turvallisuusnäkökohdat

**Lääkkeiden yhteisvaikutukset:** Tietokannasta löytyi yhteensä 100 yhteisvaikutusta. Merkittävin on **vakava (Major)** yhteisvaikutus **klaritromysiinin** kanssa. Useimmat muut listatut ovat keskivaikeita (Moderate), esimerkiksi:
- deksametasoni
- aprepitantti
- simetidiini
- metronidatsoli
- mikonatsoli
- levofloksasiini
- rosuvastatiini ja simvastatiini
- pioglitatsoni ja rosiglitatsoni

Muista turvallisuustiedoista (varoitukset, vasta-aiheet) katso valmisteyhteenveto.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold**

**Perustelut:**
- Rintasyöpää koskevaa vaiheen 2 näyttöä on (mm. satunnaistettu tutkimus ja BRCA-mutaatiotutkimus), ja mekanistinen perusta on uskottava. Ainoa rekisteröity kliininen tutkimus on kuitenkin QT-turvallisuustutkimus, eikä vaiheen 3 tehonäyttöä ole.

<!-- review:begin fi-lic-20261106-trabectedin-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ainoa rekisteröity kliininen tutkimus on kuitenkin QT-turvallisuustutkimus, eikä vaiheen 3 tehonäyttöä ole. Lisäksi molemmat Suomen myyntiluvat on peruutettu, eikä valmisteyhteenvedon turvallisuustietoja ole saatavilla.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-trabectedin-1 -->

**Jatkamiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimealta
- Vaikutusmekanismitietojen täydentäminen (DrugBank)
- Rintasyöpää koskevien vaiheen 2 tutkimusten tulosten arviointi tarkemmin (teho, osallistujaryhmät, haittavaikutukset), erityisesti BRCA-mutaatiota kantavien ja kolmoisnegatiivisten potilaiden osalta
- Suunnitelma myelosuppression ja maksatoksisuuden seurannasta sekä yhteisvaikutusten (erityisesti klaritromysiini) hallinnasta

<!-- review:begin fi-lic-20261106-trabectedin-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Rintasyöpää koskevien vaiheen 2 tutkimusten tulosten arviointi tarkemmin (teho, osallistujaryhmät, haittavaikutukset), erityisesti BRCA-mutaatiota kantavien ja kolmoisnegatiivisten potilaiden osalta / Selvitys myyntiluvan peruuttamisen syistä ja valmisteen saatavuudesta Suomessa” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-trabectedin-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi molemmat Suomen myyntiluvat on peruutettu, eikä valmisteyhteenvedon turvallisuustietoja ole saatavilla” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Selvitys myyntiluvan peruuttamisen syistä ja valmisteen saatavuudesta Suomessa” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: 2 myyntilupaa (Trabectedin Accord (EMEA/H/C/006433), Yondelis (EMEA/H/C/000773)) ovat voimassa, ei peruutettuja | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Evdi (trabectedin) prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c1d50f5c-4202-27f3-4798-a9708114ddea) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

