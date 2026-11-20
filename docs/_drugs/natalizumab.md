---
layout: default
title: Natalizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 297
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
description: "Natalizumab: ennustettu uusi käyttöaihe Keuhkoputkentulehdus (bronchitis) (näytön taso L5). Alkuperäinen käyttöaihe: Aaltoileva multippeliskleroosi (relapsoiva-remittoiva MS) ja multippe…"
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
---

# Natalizumab
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

## Natalitsumabi: Keuhkoputkentulehdus
{: .text-alpha }

## Yhden lauseen yhteenveto

Natalitsumabi on monoklonaalinen vasta-aine, jota on alun perin käytetty aaltoilevaoireisen multippeliskleroosin (MS-taudin) hoitoon.
TxGNN-malli ennustaa sen voivan tehota **keuhkoputkentulehdukseen**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.
Ennuste perustuu pelkästään mallilaskentaan, ja sitä on pidettävä todennäköisenä tietoverkon artefaktina.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Aaltoileva multippeliskleroosi (relapsoiva-remittoiva MS) ja multippeliskleroosi |
| Ennustettu uusi käyttöaihe | Keuhkoputkentulehdus (bronchitis) |
| TxGNN-ennusteen pistemäärä | 0,9946 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 2/2) |
| Myyntilupien määrä | 2 (voimassa: 2) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Natalitsumabi salpaa alfa4-integriinin välittämää valkosolujen kulkeutumista tulehduskohtiin. MS-taudissa tämä estää tulehdussolujen pääsyn keskushermostoon. Teoriassa sama mekanismi voisi vaikuttaa myös hengitysteiden tulehdukseen.

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Natalizumab (epävirallinen käännös): ”Natalitsumabi sitoutuu α4β1- ja α4β7-integriinien α4-alayksikköön, jota ilmentyy kaikkien leukosyyttien paitsi neutrofiilien pinnalla, ja estää leukosyyttien α4-välitteisen adheesion niiden vastareseptoriin (vastareseptoreihin). α4-integriiniperheen reseptoreihin kuuluvat verisuonten soluadheesiomolekyyli 1 (VCAM-1), jota ilmentyy aktivoituneessa verisuonten endoteelissa, sekä limakalvojen addressiinisoluadheesiomolekyyli 1 (MAdCAM-1), jota esiintyy ruoansulatuskanavan verisuonten endoteelisoluissa.” Englanninkielinen alkuteksti: "Natalizumab binds to the α4-subunit of α4β1 and α4β7 integrins expressed on the surface of all leukocytes except neutrophils, and inhibits the α4-mediated adhesion of leukocytes to their counter-receptor(s). The receptors for the α4 family of integrins include vascular cell adhesion molecule-1 (VCAM-1), which is expressed on activated vascular endothelium, and mucosal addressin cell adhesion molecule-1 (MAdCAM-1) present on vascular endothelial cells of the gastrointestinal tract." ([DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962), versio 2026-10-09; haettu 2026-11-19). Keuhkoputkentulehdus on useimmiten infektioperäinen tai itsestään paraneva, ja systeeminen immuunivaste-estävä hoito lisäisi infektioriskiä. Ennuste on siksi todennäköisesti verkkopohjainen artefakti eikä aidosti hoidollinen löydös.

---

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

---

## Tietoa Suomen markkinoista

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005752 | Tyruko (Sandoz GmbH), voimassa | – | Aaltoileva multippeliskleroosi; multippeliskleroosi |
| EMEA/H/C/000603 | Tysabri (Biogen Netherlands B.V.), voimassa | – | Multippeliskleroosi |

<!-- review:begin fi-row-20261112-natalizumab-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/005752 / Tyruko (Sandoz GmbH), peruutettu / – / Aaltoileva multippeliskleroosi; multippeliskleroosi; EMEA/H/C/000603 / Tysabri (Biogen Netherlands B.V.), peruutettu / – / Multippeliskleroosi” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntiluvat Tyruko (EMEA/H/C/005752), Tysabri (EMEA/H/C/000603) ovat voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-natalizumab-1 -->

---

## Turvallisuushuomioita

- **Tietoverkon vasta-aiheet:** Tietämysverkon (PrimeKG) mukaan natalitsumabiin liittyy vasta-aihemerkintä **progressiiviselle multifokaaliselle leukoenkefalopatialle (PML)**. Tämä ei perustu valmisteyhteenvedon tekstiin.
- **Lääkeyhteisvaikutukset:** Yhteisvaikutuksia löytyi yhteensä 100. Merkittäviä (Major) ovat mm.:
  - kortikosteroidit: hydrokortisoni, triamsinoloni, deksametasoni, betametasoni, budesonidi, prednisoloni ja prednisoni
  - radiofarmaseuttiset ja vasta-ainevalmisteet: jobenguaani (I-131), ibritumomabitiuksetaani, tositumomabi (myös I-131)
  - muut: levamisoli, trimetreksaatti, merkaptopuriini
  - Kohtalainen (Moderate): naltreksoni
  - Vähäisiä (Minor): sinkkiyhdisteet (sulfaatti, asetaatti, glukonaatti, kloridi)

Muiden ennustettujen käyttöaiheiden kirjallisuus (psoriaasi, parapsoriaasi, akuutti lichenoidi pityriaasi) viittaa lisäksi siihen, että natalitsumabi voi aiheuttaa tai pahentaa ihomuutoksia. Psoriaasista on raportoitu sekä paranemista (PMID 33589543) että natalitsumabin aiheuttamia tai pahentamia tapauksia.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelu:**
- Korkeasta TxGNN-pistemäärästä (0,9946) huolimatta ennusteelle ei ole kliinistä eikä kirjallista tukea (taso L5). Lääkkeen PML-riski ja infektioalttiuden lisääntyminen tekevät riski-hyötysuhteesta epäedullisen keuhkoputkentulehduksessa.

<!-- review:begin fi-lic-20261106-natalizumab-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lääkkeen PML-riski ja infektioalttiuden lisääntyminen tekevät riski-hyötysuhteesta epäedullisen keuhkoputkentulehduksessa. Lisäksi Suomessa kaikki myyntiluvat on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 2 myyntilupaa, joista 2 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-natalizumab-1 -->

**Eteneminen edellyttäisi seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta ja läpikäynti Fimeasta (estää tällä hetkellä turvallisuusseulonnan)
- Vaikutusmekanismitietojen täydentäminen (esim. DrugBankista)
- Prekliinisen tai kliinisen näytön löytäminen keuhkoputkentulehduksesta
- Arvio siitä, onko tarkasteltavaksi järkevämpää valita jokin muu ennustettu käyttöaihe, jolle löytyy kirjallisuutta

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi Suomessa kaikki myyntiluvat on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: 2 myyntilupaa (Tyruko (EMEA/H/C/005752), Tysabri (EMEA/H/C/000603)) ovat voimassa, ei peruutettuja | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

