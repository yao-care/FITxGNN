---
layout: default
title: Pertuzumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 342
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-25
monitor_inn: "PERTUZUMAB"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
description: "Pertuzumab: ennustettu uusi käyttöaihe Ectomesenchymoma (näytön taso L5). Alkuperäinen käyttöaihe: Breast Neoplasms"
---

# Pertuzumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

## Pertuzumab: Ectomesenchymoma
{: .text-alpha }

## Yhteenveto

Pertutsumabi on HER2-reseptorin dimerisaatiota estävä vasta-aine, jota on alun perin käytetty rintasyövän hoidossa. TxGNN-malli ennustaa sen tehoavan **progesteronireseptoripositiiviseen rintasyöpään**. Ennusteen tueksi on tähän mennessä koottu **1 kliininen tutkimus** ja **20 julkaisua**. Kyseessä on käytännössä laajennus alkuperäisen käyttöaiheen sisällä, ei varsinainen uudelleenkäyttö.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Breast Neoplasms |
| Ennustettu uusi käyttöaihe | Ectomesenchymoma |
| TxGNN-ennustepistemäärä | 0.9971 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 3/3) |
| Myyntilupien määrä | 3 (voimassa: 3) |
| Suositeltu päätös | Etene suojatoimin (Proceed with Guardrails) |

---

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Pertuzumab (epävirallinen käännös): ”Pertutsumabi kohdistuu ihmisen epidermaalisen kasvutekijäreseptori 2 -proteiinin (HER2) solunulkoiseen dimerisaatiodomeeniin (alidomeeni II) ja estää siten HER2:n ligandiriippuvaisen heterodimerisaation muiden HER-perheen jäsenten, mukaan lukien EGFR:n, HER3:n ja HER4:n, kanssa. Tämän seurauksena pertutsumabi estää ligandin käynnistämää solunsisäistä signalointia kahden tärkeän signaalireitin, mitogeeniaktivoidun proteiinikinaasin (MAP-kinaasin) ja fosfoinositidi-3-kinaasin (PI3K), kautta.” Englanninkielinen alkuteksti: "Pertuzumab targets the extracellular dimerization domain (Subdomain II) of the human epidermal growth factor receptor 2 protein (HER2) and, thereby, blocks ligand-dependent heterodimerization of HER2 with other HER family members, including EGFR, HER3, and HER4. As a result, pertuzumab inhibits ligand-initiated intracellular signaling through two major signal pathways, mitogen-activated protein (MAP) kinase, and phosphoinositide 3-kinase (PI3K)." ([DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff), versio 2026-04-30; haettu 2026-11-19). Tunnetun farmakologian perusteella pertutsumabi sitoutuu HER2-reseptoriin (ERBB2) ja estää sen heterodimerisaatiota, mikä vaimentaa kasvusignalointia. Sen teho on osoitettu HER2-positiivisessa rintasyövässä yhdessä trastutsumabin kanssa.

Progesteronireseptoripositiivinen (PR+) rintasyöpä on reseptorien perusteella määritelty rintasyövän alaryhmä, johon kuuluvat myös HR+/HER2+ -kasvaimet. Hoidon hyöty määräytyy HER2-statuksen, ei PR-statuksen mukaan. Ennuste on siksi mekanistisesti uskottava vain HER2-positiivisessa osajoukossa. Vaiheen 2 neoadjuvanttitutkimukset (mm. NeoSphere, WSG-ADAPT ja WSG TP-II) tukevat aktiivisuutta HR+/HER2+ -taudissa.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Vaihe 3 | Päättynyt | 517 | Satunnaistettu kaksoissokkoutettu ekvivalenssitutkimus: pertutsumabin biosimilaari QL1209 vs. viitevalmiste yhdessä trastutsumabin ja dosetakselin kanssa HER2-positiivisessa varhaisen tai paikallisesti levinneen rintasyövän neoadjuvanttihoidossa. Tutkimus ei testaa erityisesti PR-positiivista tautia. |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT | Br J Cancer | Biosimilaari QL1209 vastasi viitepertutsumabia HER2+/ER/PR-negatiivisessa neoadjuvanttihoidossa (vaihe 3). |
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | RCT | J Clin Oncol | WSG TP-II: neoadjuvanttinen trastutsumabi + pertutsumabi + endokriinihoito vs. kemoterapia HR+/HER2+ -varhaisessa rintasyövässä. |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: kaksoissalpaus ± viikoittainen paklitakseli, vaiheen 2 tutkimus. |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Kohorttianalyysi | Lancet Oncol | NeoSphere: 5 vuoden elinaika ilman taudin etenemistä ja turvallisuus neoadjuvanttipertutsumabilla. |
| [41401771](https://pubmed.ncbi.nlm.nih.gov/41401771/) | 2026 | RCT | ESMO Open | Biosimilaari TQB2440 vs. viitepertutsumabi HER2+, ER/PgR-negatiivisessa rintasyövässä. |
| [39753653](https://pubmed.ncbi.nlm.nih.gov/39753653/) | 2025 | Verkostometa-analyysi | Sci Rep | Optimaalisen neoadjuvanttihoidon vertailu HR+/HER2+ -rintasyövässä. |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Ohje | J Clin Oncol | ASCO:n päivitetty ohje levinneen HER2-positiivisen rintasyövän systeemihoidosta. |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Katsaus | Cancer Treat Rev | Katsaus HR+/HER2+ -rintasyövän nykytilaan ja tulevaisuuteen. |
| [26321480](https://pubmed.ncbi.nlm.nih.gov/26321480/) | 2015 | Katsaus | Breast | Luminaalisen HER2- ja HER2-rikastetun alatyypin biologia ja hoitovaikutukset. |
| [41387082](https://pubmed.ncbi.nlm.nih.gov/41387082/) | 2026 | Kohortti | Breast | Munasarjatoiminnan suppressio ja aromataasinestäjät premenopausaalisilla HR+/HER2+ -potilailla. |

---

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/002547 | Perjeta | pertuzumab | Breast Neoplasms | Voimassa |
| EMEA/H/C/005386 | Phesgo | pertuzumab; trastuzumab | Breast Neoplasms | Voimassa |
| EMEA/H/C/006583 | Poherdy | pertuzumab | Breast Neoplasms | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Solunsalpaajaluonne

| Kohta | Sisältö |
|------|------|
| Luokitus | Kohdennettu hoito (monoklonaalinen HER2-vasta-aine); ei perinteinen sytotoksinen lääke |
| Luluydinsuppressio | Tietoa ei ole saatavilla; ks. valmisteyhteenvedon varoitukset ja varotoimet |
| Pahoinvointia aiheuttava vaikutus | Tietoa ei ole saatavilla; ks. valmisteyhteenveto |
| Seurantakohteet | Sydämen toiminta (LVEF) on tutkimuksissa ollut keskeinen turvallisuusseurannan kohde; verenkuva sekä maksa- ja munuaisarvot |
| Käsittelysuojaus | Ks. valmisteyhteenvedon varoitukset ja varotoimet |

---

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Idelalisibin kanssa on kirjattu keskivaikea (Moderate) yhteisvaikutus. Lisäksi pertutsumabin kohde on ERBB2 (HER2).
- Sydänturvallisuutta on tutkittu erikseen vaiheen 2 tutkimuksissa (TRYPHAENA, BERENICE).

Muilta osin turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Etene suojatoimin (Proceed with Guardrails)**

**Perustelut:**
- Pertutsumabin teho on vakiintunut HER2-positiivisessa rintasyövässä, ja valmistetta tukee valmistunut vaiheen 3 RCT sekä useita neoadjuvanttitutkimuksia, myös HR+/HER2+ -taudissa. Hyöty riippuu HER2-statuksesta, ei PR-statuksesta, joten kyseessä on laajennus nykyisen käyttöaiheen sisällä.

**Eteneminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvittäminen (Fimean valmisteyhteenveto), koska nämä tiedot puuttuvat ja estävät turvallisuusarvioinnin.
- Vaikutusmekanismitietojen täydentäminen.
- Potilasvalinnan rajaaminen HER2-positiivisiin kasvaimiin ja sydänturvallisuuden seurantasuunnitelma.

<!-- review:begin fi-lic-20261106-pertuzumab-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Vaikutusmekanismitietojen täydentäminen. / Markkinatilanteen selvitys: Suomessa on vain peruutettuja myyntilupia.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-pertuzumab-1 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Markkinatilanteen selvitys: Suomessa on vain peruutettuja myyntilupia” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: 2 myyntilupaa (Perjeta (EMEA/H/C/002547), Phesgo (EMEA/H/C/005386)) ovat voimassa, ei peruutettuja | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

