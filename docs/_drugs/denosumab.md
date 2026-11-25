---
layout: default
title: Denosumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 137
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
description: "Denosumab: ennustettu uusi käyttöaihe Vaikea ei-proliferatiivinen diabeettinen retinopatia (toissijainen en… (näytön taso L5). Alkuperäinen käyttöaihe: Luun jättisolukasvain (luukudoksen kasvaimet)"
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
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

## Denosumabi: vaikea ei-proliferatiivinen diabeettinen retinopatia
{: .text-alpha }

## Yhden lauseen yhteenveto

Denosumabi on RANKL-estäjä, jota on alun perin käytetty luun jättisolukasvaimen ja postmenopausaalisen osteoporoosin (luun resorption) hoitoon.
TxGNN-malli (syväoppiminen) ennustaa sen voivan tehota **vaikeaan ei-proliferatiiviseen diabeettiseen retinopatiaan** (pistemäärä 0.9963) ja **diabeettiseen retinopatiaan** (0.9923).
Kumpaankaan indikaatioon ei ole **yhtään kliinistä tutkimusta**, ja diabeettisen retinopatian osalta on vain **2 epäsuoraa julkaisua**, joten näyttö on heikkoa.

---

## Pikayhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Luun jättisolukasvain (luukudoksen kasvaimet); postmenopausaalinen osteoporoosi ja luun resorptio |
| Ennustettu uusi käyttöaihe | Vaikea ei-proliferatiivinen diabeettinen retinopatia (toissijainen ennuste: diabeettinen retinopatia) |
| TxGNN-ennustepistemäärä | 0.9963 (diabeettinen retinopatia: 0.9923) |
| Näytön taso | L5 (vaikea ei-proliferatiivinen diabeettinen retinopatia); L4 (diabeettinen retinopatia) |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: vähintään 20) |
| Myyntilupien määrä | vähintään 20 |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Denosumab (epävirallinen käännös): ”Denosumabivalmisteet sitoutuvat RANKL:ään, joka on transmembraaninen tai liukoinen proteiini ja välttämätön osteoklastien eli luun resorptiosta vastaavien solujen muodostumiselle, toiminnalle ja eloonjäämiselle. Denosumabivalmisteet estävät RANKL:ää aktivoimasta reseptoriaan, RANK:ta, osteoklastien ja niiden esiasteiden pinnalla.” Englanninkielinen alkuteksti: "Denosumab products bind to RANKL, a transmembrane or soluble protein essential for the formation, function, and survival of osteoclasts, the cells responsible for bone resorption. Denosumab products prevent RANKL from activating its receptor, RANK, on the surface of osteoclasts and their precursors." ([DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd), versio 2026-11-04; haettu 2026-11-19). Tunnetun lääkeluokan perusteella denosumabi on RANKL-estäjä, joka vähentää luun resorptiota. Sen teho luustoindikaatioissa on osoitettu, ja mekanistisesti se voisi mahdollisesti liittyä diabeettiseen retinopatiaan RANKL/RANK/OPG-signaloinnin kautta.

Alkuperäiset käyttöaiheet (luun jättisolukasvain, osteoporoosi) ja ennustettu silmänpohjan mikroverisuonisairaus ovat kliinisesti kaukana toisistaan. Mahdollinen yhteys kulkisi tulehduksen, verisuonivaurion ja verisuonten kalkkiutumisen kautta, mutta tämä on toistaiseksi spekulatiivista. Mikään koottu aineisto ei yhdistä denosumabia suoraan verkkokalvon mikroverisuonisairauteen, eikä mekanismia voida tarkistaa puuttuvan MOA-tiedon vuoksi.

Ennusteen ainoa tuki on siis TxGNN-mallin korkea pistemäärä.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Diabeettinen retinopatia (2 epäsuoraa julkaisua). Vaikeaan ei-proliferatiiviseen diabeettiseen retinopatiaan ei ole kirjallisuutta.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Todennäköisesti havainnoiva tutkimus/katsaus (luokitus epävarma) | Diabetes, Obesity & Metabolism | Denosumabi osteoporoosin hoidossa: yhteys tyypin 2 diabeteksen ilmaantuvuuteen sekä mikro- ja makrovaskulaarisiin komplikaatioihin (mm. retinopatia), verrattuna bisfosfonaatteihin; sisältää meta-analyysin. Vain katkaistu tiivistelmä saatavilla, joten retinopatiatulokset ovat vahvistamattomia. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Todennäköisesti havainnoiva tutkimus | Cureus | FRAX-murtumariskityökalun käyttö aikuisilla, joilla on tyypin 2 diabetes. Ei käsittele denosumabin vaikutusta verkkokalvoon. |

Kumpikaan julkaisu ei testaa denosumabia diabeettisessa retinopatiassa, joten ne ovat vain epäsuoraa, diabetekseen liittyvää näyttöä.

---

## Tiedot Suomen markkinoilta

Myyntiluvat ja niiden tila ovat alla olevassa taulukossa.

<!-- review:begin fi-lic-20261106-denosumab-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikki 20 myyntilupaa on peruutettu. Alla viisi esimerkkiä.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-denosumab-1 -->

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/006152 | Izamby | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006156 | Stoboclo | denosumab | Osteoporosis, Postmenopausal; Osteoporosis; Bone Resorption | Voimassa |
| EMEA/H/C/006238 | Ponlimsi | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006268 | Conexxence | denosumab | Osteoporosis; Osteoporosis, Postmenopausal; Bone Resorption | Voimassa |
| EMEA/H/C/006269 | Bomyntra | denosumab | Neoplasms, Bone Tissue; Giant Cell Tumor of Bone | Voimassa |
| EMEA/H/C/006377 | Zadenvi | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006399 | Osvyrti | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006434 | Bildyos | denosumab | Bone Resorption; Osteoporosis, Postmenopausal; Osteoporosis | Voimassa |
| EMEA/H/C/006435 | Bilprevda | denosumab | Giant Cell Tumor of Bone; Neoplasms, Bone Tissue | Voimassa |
| EMEA/H/C/006436 | Junod | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006437 | Yaxwer | denosumab | Neoplasms, Bone Tissue; Giant Cell Tumor of Bone | Voimassa |
| EMEA/H/C/006468 | Xbryk | denosumab | Neoplasms, Bone Tissue; Giant Cell Tumor of Bone | Voimassa |
| EMEA/H/C/006490 | Kefdensis | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006507 | Rolcya | denosumab | Osteoporosis; Osteoporosis, Postmenopausal; Bone Resorption | Voimassa |
| EMEA/H/C/006526 | Evfraxy | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006534 | Vevzuo | denosumab | Neoplasms, Bone Tissue; Giant Cell Tumor of Bone | Voimassa |
| EMEA/H/C/006552 | Zvogra | denosumab | Giant Cell Tumor of Bone; Neoplasms, Bone Tissue | Voimassa |
| EMEA/H/C/006722 | Xbonzy | denosumab | Giant Cell Tumor of Bone; Neoplasms, Bone Tissue | Voimassa |
| EMEA/H/C/006734 | Acvybra | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |
| EMEA/H/C/006797 | Denosumab Intas | denosumab | Bone Resorption; Osteoporosis; Osteoporosis, Postmenopausal | Voimassa |

Taulukossa näytetään 20 näissä tiedoissa olevasta 32 keskitetystä EU-myyntiluvasta (voimassa olevat ensin).

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Solunsalpaajaominaisuudet

| Kohta | Sisältö |
|------|------|
| Solunsalpaajaluokitus | Ei perinteinen solunsalpaaja; biologinen lääke (monoklonaalinen vasta-aine, RANKL-estäjä). Käyttöaiheena mm. luun jättisolukasvain. |
| Myelosuppression riski | Tietoja ei ole saatavilla; katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksentelua aiheuttavuus | Tietoja ei ole saatavilla; katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurantakohteet | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja varotoimet |

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Yhteisvaikutustietokannasta löytyi yhteensä 100 yhteisvaikutusta. Esimerkkejä keskivaikeista (Moderate) yhteisvaikutuksista:
- Kortikosteroidit: hydrokortisoni, triamsinoloni, deksametasoni, betametasoni, budesonidi, prednisolooni, prednisoni, metyyliprednisolooni
- Immuunijärjestelmään vaikuttavat lääkkeet: takrolimuusi, dupilumabi, levamisoli
- Solunsalpaajat ja radiofarmaseuttiset valmisteet: merkaptopuriini, trimetreksaatti, ibritumomabitiuksetaani, tositumomabi, jobenguaani (I-131)
- Hormonit: kortikotropiini, tetrakosaktidi

Muuta turvallisuustietoa, kuten varoituksia ja vasta-aiheita, katso valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Ennuste perustuu lähes yksinomaan TxGNN-mallin korkeaan pistemäärään. Kliinisiä tutkimuksia ei ole, ja kaksi julkaisua ovat vain epäsuoraa, diabetekseen liittyvää näyttöä, joka ei testaa denosumabia retinopatiassa.
- Turvallisuustietoja ei ole saatavilla.

<!-- review:begin fi-lic-20261106-denosumab-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Suomessa kaikki denosumabin myyntiluvat on peruutettu, ja turvallisuustietoja ei ole saatavilla.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-denosumab-2 -->

**Jatkotoimiin tarvitaan:**
- Denosumabin vaikutusmekanismitiedot (MOA), jotta mekanistinen yhteys retinopatiaan voidaan arvioida
- Valmisteyhteenvedon varoitukset ja vasta-aiheet Fimean sivustolta turvallisuusarviointia varten
- Julkaisun 38899553 koko teksti sen selvittämiseksi, raportoiko se retinopatiatuloksia
- Prekliiniset tutkimukset tai havainnoivat aineistot, jotka tarkastelevat RANKL/OPG-signalointia verkkokalvon mikroverisuonisairaudessa
- Selvitys Suomen myyntilupien nykytilasta ja lääkemuodoista, mukaan lukien antoreitin soveltuvuus silmänpohjan käyttöaiheeseen

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Kaikki 20 myyntilupaa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Suomessa kaikki denosumabin myyntiluvat on peruutettu, ja t” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

