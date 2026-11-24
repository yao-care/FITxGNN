---
layout: default
title: Memantine
parent: Pelkkä mallin ennuste (L5)
nav_order: 280
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "MEMANTINE"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Memantine: ennustettu uusi käyttöaihe Pulmonary hypertension (näytön taso L5). Alkuperäinen käyttöaihe: Alzheimer Disease"
---

# Memantine
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

## Memantine: Pulmonary hypertension
{: .text-alpha }

## Yhden lauseen yhteenveto

Memantiini on NMDA-reseptorin salpaaja, jota on alun perin käytetty Alzheimerin taudin hoitoon. TxGNN-malli ennustaa sen voivan tehota ensisijaisesti **migreeniin** (migraine disorder), jonka tueksi on tällä hetkellä **1 valmistunut vaiheen 3 kliininen tutkimus** ja **19 julkaisua**. Muiden ennustettujen käyttöaiheiden (mm. keuhkoverenpainetauti) näyttö on selvästi heikompaa.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Alzheimer Disease |
| Ennustettu uusi käyttöaihe | Pulmonary hypertension |
| TxGNN-ennustepisteet | 0.9952 |
| Näytön taso | L5 (muodollisesti; käytännössä rajallinen, ks. perustelut) |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 8/8) |
| Myyntilupien määrä | 8 (voimassa: 8) |
| Suositeltu päätös | Hold (odota) |

Huomio: tiedoissa ensimmäisenä listattu ennuste on keuhkoverenpainetauti (pisteet 0.9954, näytön taso L5). Tässä raportissa pääpainopisteenä on migreeni, koska sen näyttö on vahvin. Muut ennusteet on käsitelty lyhyesti perustelujen yhteydessä.

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Memantine (epävirallinen käännös): ”Keskushermoston N-metyyli-D-aspartaatti (NMDA) -reseptorien jatkuvan aktivoitumisen eksitatorisen aminohapon glutamaatin vaikutuksesta on oletettu osaltaan aiheuttavan Alzheimerin taudin oireita. Memantiinin oletetaan saavan aikaan terapeuttisen vaikutuksensa toimimalla matalan tai kohtalaisen affiniteetin epäkilpailevana (avoimen kanavan) NMDA-reseptorin antagonistina, joka sitoutuu ensisijaisesti NMDA-reseptorin säätelemiin kationikanaviin.” Englanninkielinen alkuteksti: "Persistent activation of central nervous system N-methyl-D-aspartate (NMDA) receptors by the excitatory amino acid glutamate has been hypothesized to contribute to the symptomatology of Alzheimer’s disease. Memantine is postulated to exert its therapeutic effect through its action as a low to moderate affinity uncompetitive (open-channel) NMDA receptor antagonist which binds preferentially to the NMDA receptor-operated cation channels." ([DailyMed: memantine hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e6977ef-6a0a-4bd9-b500-6ceb15abbd5e), versio 2026-11-11; haettu 2026-11-19). Tunnetun tiedon perusteella memantiini on NMDA-reseptorin salpaaja, jonka teho Alzheimerin taudissa on osoitettu, ja mekanistisesti se voi soveltua myös migreeniin.

Glutamaattivälitteisen hermosolujen yliärtyvyyden ja aivokuoren leviävän lamaantumisen (cortical spreading depression) uskotaan liittyvän migreeniin. NMDA-reseptorin salpaus voi tasoittaa tätä yliärtyvyyttä. Alzheimerin taudissa taas glutamaatin aiheuttama eksitotoksisuus on hoidon kohteena, joten molemmissa sairauksissa yhteinen tekijä on glutamaattisignaloinnin häiriö. Katsaukset tukevat tätä yhteyttä, ja yksi julkaisu toteaa päänsäryn ja kognitiivisen heikentymisen jakavan yhteisiä patofysiologisia mekanismeja.

Näyttö on kuitenkin vielä niukkaa: eräs kommentaari on otsikoitu "Memantine for migraine – Big promise but little evidence".

Muut ennusteet:
- **Migreeni ja aivorunkoaura** (pisteet 0.9941, L4): ei omia tutkimuksia, vain epäsuoraa näyttöä laajemmasta migreeniaineistosta, mm. satunnaistettu lumekontrolloitu tutkimus aurattomassa migreenissä.
- **Keuhkoverenpainetauti** (pisteet 0.9954, L5): ei kliinisiä tutkimuksia. Kaksi löydettyä julkaisua ei käsittele memantiinia suoraan. Toinen on prekliininen NMDA-reseptoritutkimus ja toinen memantiinin nitraattijohdannaisen (MN-08) vaiheen 1 tutkimus.
- **Kyfoskolioottinen sydänsairaus** (pisteet 0.9943, L5): pelkkä mallin ennuste ilman tutkimuksia tai kirjallisuutta.

<!-- review:begin fi-lic-20261106-memantine-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikki 8 myyntilupaa on peruutettu, joten markkinoilla ei tällä hetkellä ole voimassa olevia memantiinivalmisteita näiden tietojen mukaan.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-memantine-1 -->

## Kliiniset tutkimukset

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Vaihe 3 | Valmistunut | 33 | Memantiinin ja natriumvalproaatin vertailu episodisen migreenin ennaltaehkäisyssä. Pieni otos, tuloksia ei ole saatavilla. |

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analyysi (RCT:t) | Clin Neuropharmacol | Memantiinin ja lumelääkkeen vertailu migreenipotilailla; teho on kiistanalainen |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systemaattinen katsaus | Headache | Memantiinin teho ja turvallisuus episodisen migreenin ennaltaehkäisyssä |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Verkostometa-analyysi | Front Pharmacol | Suun kautta otettavien migreenin ehkäisylääkkeiden vertailu aikuisilla |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Katsaus | Naunyn-Schmiedebergs Arch Pharmacol | Memantiini ja ketamiini mahdollisina migreenilääkkeinä |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Systemaattinen katsaus | Ann Pharmacother | Memantiinin teho ja turvallisuus primaaristen päänsärkyjen ehkäisyssä |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Katsaus | Neurotherapeutics | Glutamaatti ja sen reseptorit migreenin hoitokohteina |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (epäsuora, aurattomaan migreeniin) | Headache | Satunnaistettu kaksoissokkoutettu lumekontrolloitu tutkimus memantiinista aurattoman migreenin ehkäisyssä |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospektiivinen tutkimus | J Headache Pain | Memantiinin käyttö migreenin ehkäisyssä 60 potilaalla |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Kommentaari | Headache | "Suuri lupaus mutta vähän näyttöä" |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Hoitosuositus | Ann Intern Med | VA/DoD:n päänsäryn hoitosuositus 2023 |

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000378 | Axura | memantine hydrochloride | Alzheimer Disease | Voimassa |
| EMEA/H/C/000463 | Ebixa | memantine hydrochloride | Alzheimer Disease | Voimassa |
| EMEA/H/C/002658 | Marixino (previously Maruxa) | memantine hydrochloride | Alzheimer Disease | Voimassa |
| EMEA/H/C/002660 | Memantine Mylan | memantine hydrochloride | Alzheimer Disease | Voimassa |
| EMEA/H/C/002671 | Memantine ratiopharm | memantine hydrochloride | Alzheimer Disease | Voimassa |
| EMEA/H/C/002680 | Nemdatine | memantine | Alzheimer Disease | Voimassa |
| EMEA/H/C/002711 | Memantine Merz | memantine hydrochloride | Alzheimer Disease | Voimassa |
| EMEA/H/C/002766 | Memantine Accord | memantine hydrochloride | Alzheimer Disease | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

- **Tietämysgraafin mukaiset vasta-aiheet** (ei valmisteyhteenvedon tekstiä): maksasairaus, sappirakon sairaus ja munuaisten vajaatoiminta.
- **Lääkeyhteisvaikutukset**: tietokannasta löytyi 100 yhteisvaikutusta. Merkittävimmät (keskivaikeat) koskevat antikolinergisiä lääkkeitä: hyoskyamiini, atropiini, glykopyrronium, disyklomiini, metskopolamiini, propanteliini, skopolamiini, trospium, klidiinium ja mepenzolaatti. Lievät yhteisvaikutukset liittyvät mm. ranitidiiniin, metformiiniin, simetidiiniin ja kaliumsitraattiin.

Muilta osin turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Migreenin osalta on yksi valmistunut vaiheen 3 tutkimus, mutta se on pieni (n=33), tuloksia ei ole saatavilla ja vertailukohteena oli vaikuttava aine. Kirjallisuus on enimmäkseen katsauksia, ja yleisarvio on, että näyttö on rajallista. Turvallisuustietojen keskeiset osat puuttuvat.

<!-- review:begin fi-lic-20261106-memantine-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lisäksi Suomessa ei ole voimassa olevia myyntilupia, ja turvallisuustietojen keskeiset osat puuttuvat.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-memantine-2 -->

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivustolta (estävä tietoaukko)
- Memantiinin vaikutusmekanismitietojen täydentämistä (esim. DrugBankista)
- NCT04698525-tutkimuksen tulosten selvittämistä sekä meta-analyysien (PMID 33961371, 34352118) arvioimista tarkemmin
- Suurempaa, lumekontrolloitua vaiheen 3 tutkimusta migreenin ehkäisystä
- Myyntilupatilanteen selvittämistä ja soveltuvien antoreittien arviointia
- Muiden ennusteiden (keuhkoverenpainetauti, kyfoskolioottinen sydänsairaus) osalta ensin perustason näytön ja mekanistisen perustelun kokoamista

<!-- review:begin fi-lic-20261106-memantine-3 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntilupatilanteen selvittämistä (nykyiset luvat peruutettu) ja soveltuvien antoreittien arviointia” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-memantine-3 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Kaikki 8 myyntilupaa on peruutettu, joten markkinoilla ei tällä hetkellä ole voimassa olevia memantiinivalmisteita näiden tietojen mukaan” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi Suomessa ei ole voimassa olevia myyntilupia, ja t” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”(nykyiset luvat peruutettu)” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: memantine hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e6977ef-6a0a-4bd9-b500-6ceb15abbd5e) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

