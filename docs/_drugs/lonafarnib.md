---
layout: default
title: Lonafarnib
parent: Pelkkä mallin ennuste (L5)
nav_order: 268
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "LONAFARNIB"
predicted_indications: ["leprosy"]
description: "Lonafarnib: ennustettu uusi käyttöaihe Lepra (leprosy) (näytön taso L5). Alkuperäinen käyttöaihe: Progeria"
---

# Lonafarnib
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

## Lonafarnib: Lepra (leprosy)
{: .text-alpha }

## Yhden lauseen yhteenveto

Lonafarnibi on farnesyylitransferaasin estäjä, jota on alun perin käytetty progerian ja laminopatioiden hoitoon. TxGNN-malli ennustaa sen voivan tehota **lepraan**, mutta ennustetta ei tue yksikään kliininen tutkimus eikä julkaisu (**0 kliinistä tutkimusta** ja **0 julkaisua**), joten näyttö perustuu pelkästään mallin ennusteeseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Progeria;Laminopathies |
| Ennustettu uusi käyttöaihe | Lepra (leprosy) |
| TxGNN-ennustepisteet | 0.9914 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Lonafarnibi estää farnesyylitransferaasi-entsyymiä ja siten proteiinien farnesylaatiota (esim. progeriini, Ras-perheen proteiinit ja lamiinien prosessointi). Tarkkaa vaikutusmekanismitietoa ei ole tämän raportin aineistossa saatavilla, joten tarkastelu perustuu yleiseen farmakologiaan.

Yhteys lepraan on toistaiseksi spekulatiivinen. *Mycobacterium leprae* -infektio liittyy isäntäsolun lipidiaineenvaihduntaan, Schwannin solujen signalointiin ja makrofagien vasteisiin. Prenylaatiosta riippuvaiset pienet GTPaasit (Ras/Rho/Rab) osallistuvat fagosomien kypsymiseen ja tulehdussignalointiin, joten farnesylaation esto voisi teoriassa vaikuttaa näihin prosesseihin. Tästä ei kuitenkaan ole suoraa näyttöä.

TxGNN-pistemäärä (0,9914) on tietämysgraafipohjainen ennuste, jota ei ole vahvistettu millään tutkimuksella tai julkaisulla. Alkuperäisen käyttöaiheen (progeria, harvinaissairaus) ja lepran välinen samankaltaisuus on vielä arvioimatta.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

<!-- review:begin fi-lic-20261106-lonafarnib-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntilupa on tilassa "peruutettu".” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-lonafarnib-1 -->

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005271 | Zokinvy | – | Progeria; laminopatiat |

---

## Turvallisuusnäkökohdat

- **Lääkkeiden yhteisvaikutukset**: Yhteisvaikutushaku tuotti yhteensä 100 yhteisvaikutusta, mikä on runsaasti. Esimerkkejä vakavaksi (Major) luokitelluista:
  - loperamidi
  - aprepitantti
  - triamsinoloni
  - deksametasoni
  - budesonidi
  - simetidiini
  - klaritromysiini
  - eliglustaatti
  - naloksegoli

  Kohtalaisiksi (Moderate) luokiteltuja ovat mm. hydrokortisoni, omepratsoli, betametasoni, klooripropamidi, saksagliptiini, empagliflotsiini, oksandroloni ja naldemed```iini.
- **Huomio lepran hoidon kannalta**: Lonafarnibin tiedetään liittyvän ruoansulatuskanavan haittavaikutuksiin ja CYP3A4-välitteisiin yhteisvaikutuksiin. Rifampisiini, lepran monilääkehoidon osa, on voimakas CYP3A4:n induktori ja voisi odotetusti heikentää lonafarnibialtistusta. Tämä vaikeuttaisi yhteiskäyttöä tavanomaisen lepran hoidon kanssa.

Muiden turvallisuustietojen (varoitukset, vasta-aiheet) osalta katso valmisteyhteenveto.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu yksinomaan tietämysgraafimalliin, eikä sitä tue yksikään kliininen tutkimus tai julkaisu (taso L5). Yhteisvaikutuskuorma on suuri, erityisesti lepran vakiohoidon kanssa.

<!-- review:begin fi-lic-20261106-lonafarnib-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lisäksi Suomen myyntilupa on peruutettu ja yhteisvaikutuskuorma on suuri, erityisesti lepran vakiohoidon kanssa.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-lonafarnib-2 -->

**Eteenpäin siirtyminen edellyttää seuraavaa:**
- Vaikutusmekanismin tarkempi selvitys (DrugBank) ja mekanistisen yhteyden arviointi lepraan
- Esikliininen näyttö farnesylaation eston vaikutuksesta *M. leprae* -infektioon (solu- ja eläinmallit)
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivuilta, sillä turvallisuusarviointi ei voi edetä ilman niitä
- Yhteisvaikutusten arviointi lepran monilääkehoidon kanssa (erityisesti rifampisiini ja CYP3A4)
- Myyntilupatilanteen selvittäminen Suomessa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Myyntilupa on tilassa "peruutettu"” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi Suomen myyntilupa on peruutettu ja y” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

