---
layout: default
title: Orlistat
parent: Pelkkä mallin ennuste (L5)
nav_order: 319
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Orlistat: ennustettu uusi käyttöaihe Hypervitaminoosi (näytön taso L5). Alkuperäinen käyttöaihe: Lihavuus"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
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

## Orlistaatti: Lihavuuden hoidosta hypervitaminoosiin
{: .text-alpha }

## Yhteenveto

Orlistaatti on ruoansulatuskanavan lipaasin estäjä, jota on alun perin käytetty **lihavuuden** hoitoon.
TxGNN-malli ennustaa sen voivan olla hyödyllinen **hypervitaminoosin** hoidossa, mutta ennuste perustuu pelkästään laskennalliseen mallinnukseen: tähän suuntaan ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Lihavuus |
| Ennustettu uusi käyttöaihe | Hypervitaminoosi |
| TxGNN-ennusteen pistemäärä | 0,9942 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 2/2) |
| Myyntilupien määrä | 2 (voimassa: 2) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Orlistat (epävirallinen käännös): ”Orlistaatti on maha-suolikanavan lipaasien palautuva estäjä. Se saa aikaan terapeuttisen vaikutuksensa mahalaukun ja ohutsuolen luumenissa muodostamalla kovalenttisen sidoksen mahalaukun ja haiman lipaasien aktiivisen seriinitähteen kohtaan.” Englanninkielinen alkuteksti: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), versio 2026-09-30; haettu 2026-11-19). Tunnetun tiedon mukaan orlistaatti estää mahalaukun ja haiman lipaasia ja vähentää ravinnon rasvan imeytymistä noin 30 %. Se on siis rasvanimeytymistä estävä lääke, jonka teho lihavuuden hoidossa on osoitettu.

Rasvaliukoiset vitamiinit (A, D, E ja K) imeytyvät ravinnon rasvan mukana. Orlistaatti vähentää siksi myös niiden imeytymistä. Teoriassa tämä voisi vähentää vitamiinien kertymistä rasvaliukoisessa hypervitaminoosissa, esimerkiksi A- tai D-vitamiinin liikasaannissa.

Ennuste on kuitenkin vain laskennallinen. Pitäisi osoittaa, että vaikutus on kliinisesti merkittävän suuri, ettei se koske vesiliukoisten vitamiinien liikaa ja että hoito on turvallista jo sairailla potilailla. Lääkkeen tunnettu varoitus on päinvastoin vitamiinipuutos, mikä on turvallisuusriski eikä hoidollinen hyöty.

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000154 | Xenical | orlistat | Obesity | Voimassa |
| EMEA/H/C/000854 | Alli (previously Orlistat GSK) | orlistat | Obesity | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

- **Tietämyskaavion (PrimeKG) mukaiset vasta-aiheet** (eivät perustu valmisteyhteenvetoon): maksan vajaatoiminta, primaarinen hyperoksaluria, anorexia nervosa, bulimia nervosa, vitamiinipuutostila, kolestaasi, hyvänlaatuinen toistuva intrahepaattinen kolestaasi, familiaalinen intrahepaattinen kolestaasi sekä lääkkeen aiheuttama maksavaurio.
- **Lääkeyhteisvaikutukset**: yhteensä 100 yhteisvaikutusta, joista osa on keskivaikeita (moderate) ja osa lieviä (minor). Keskeisiä esimerkkejä:
  - Keskivaikeat: abakaviiri, lamivudiini, emtrisitabiini, atatsanaviiri, akarboosi, albiglutidi, alogliptiini, metformiini, kanagliflotsiini, klooripropamidi, amiodaroni, kannabidioli, asparaginaasi, kalaspargaasipegoli, brentuksimabivedotiini ja klofarabiini.
  - Lievät: kolekalsiferoli, kalsifediolli ja kalsitrioli (D-vitamiinivalmisteet).

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat aineistosta, joten ne on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkkään laskennalliseen malliin (L5) ilman kliinistä tai kirjallista näyttöä. Lisäksi lääkkeen tunnettu haittavaikutus, vitamiinipuutos, on ristiriidassa käyttöaiheen kanssa.

<!-- review:begin fi-lic-20261106-orlistat-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lisäksi lääkkeen tunnettu haittavaikutus, vitamiinipuutos, on ristiriidassa käyttöaiheen kanssa, ja kaikki myyntiluvat Suomessa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-orlistat-1 -->

**Eteneminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hakemista Fimean sivustolta (estää turvallisuusarvioinnin jatkamisen).
- Vaikutusmekanismitietojen täydentämistä (DrugBank).
- Kirjallisuushaun ja prekliinisten tutkimusten tekemistä siitä, vähentääkö orlistaatti kliinisesti merkittävästi rasvaliukoisten vitamiinien (A, D) kertymistä.
- Turvallisuuden arviointia sairailla potilailla, erityisesti maksa- ja sappivaivoissa.
- Myyntilupatilanteen selvittämistä, koska valmisteet eivät ole tällä hetkellä markkinoilla Suomessa.

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”ja kaikki myyntiluvat Suomessa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: 2 myyntilupaa (Alli (EMEA/H/C/000854), Xenical (EMEA/H/C/000154)) ovat voimassa, ei peruutettuja | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

