---
layout: default
title: Upadacitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 394
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Upadacitinib: indikaatiotiedot eivät vielä saatavilla → kolobomatoosinen mikroftalmiaa-rhizomeelisen dysplasia-oireyhtymä

## Yhden lauseen yhteenveto

Upadacitinibin alkuperäisen hyväksytyn indikaation ja toimintamekanismin tiedot eivät ole vielä saatavilla tässä evidenssipaketin osassa (tietoaukko). TxGNN-malli ennustaa mahdollista aktiivisuutta **kolobomatoosisen mikroftalmiaa-rhizomeelisen dysplasia-oireyhtymän** kohdalla, harvinaista synnynnäistä kehityshäiriötä, mutta tämä ennuste on tällä hetkellä tuettu **0 kliinisellä tutkimuksella** ja **0 julkaisulla** — se on vain mallin antama signaali.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla (lisenssi-/indikaatiotietoja ei arkistossa) |
| Ennustettu uusi indikaatio | Kolobomatoosinen mikroftalmiaa-rhizomeelisen dysplasia-oireyhtymä |
| TxGNN-ennustepistemäärä | 99.61% (sija 4612) |
| Evidenssitaso | L5 (mallin ennuste vain, ei tukevia tutkimuksia) |
| Taiwanin markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on perusteltu?

Upadacitinibin yksityiskohtainen toimintamekanismin data ei ole tällä hetkellä saatavilla tässä evidenssipaketin osassa, eikä alkuperäinen indikaatio ole arkistossa, joten suoraa mekaanista yhteyttä ei voida rakentaa vain syöttötiedoista. Mallin omien tulosten perusteella upadacitinib on JAK1-selektiivinen inhibiittori, joka vaikuttaa sytokiinin signalointiin (IL-6, IL-4/13, IFN-polut).

Kolobomatoosinen mikroftalmiaa-rhizomeelinen dysplasia-oireyhtymä on kuitenkin rakenteellinen/kehityshäiriö — synnynnäinen silmän väärinkehitys yhdistettynä proksimaalien raajojen luuston dysplasiaan — tyypillisesti linkitetty siliopatioihin tai peroksisomaalien geenivikoihin (esim. PEX7-liittyvä rhizomeelinen kondrodysplasia punctata), ei tulehdukselliseen tai autoimmuuniseen signalointiin. Ei ole vakiintunutta yhteyttä JAK-STAT-sytokiinin signaloinnin ja silmän/luuston alkion kehityspoluille osallistuvien oireyhtymien välillä.

Mallin oma uudelleenkäyttöperustelus päättelee, että korkea TxGNN-pistemäärä heijastaa todennäköisesti **tietokantakuvaajien solmujen läheisyyttä** (esim. klusterointia muiden harvinaistoimisen/kehityshäiriöiden solmujen kanssa) eikä todellista mekaanista uskottavuutta. Mikään mekaaninen, prekliininen tai kliininen näyttö ei tällä hetkellä tue tätä yhdistelmää — tämä on yhdenmukainen L5-evidenssitason ja Odota-suosituksen kanssa.

Toinen ehdokas, brachydactyly-syndactyly-oireyhtymä (pistemäärä 99.58%, sija 4924), osoittaa saman kuvion: luurankoksi/raajojen kehityshäiriöksi (HOX, BMP/GDF, GLI3-polut) luokiteltu häiriö, jolla ei ole suoraa yhteyttä JAK1-inhibitioon, ja samoin nolla tukevia tutkimuksia tai kirjallisuutta.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

## Taiwanin markkinatiedot

Upadacitinib ei ole tällä hetkellä markkinoilla Taiwanissa (arkistossa 0 hyväksyntää), joten paikallisia tuotanto-/hyväksyntätietoja ei ole saatavilla.

## Turvallisuushuomiot

Viitaa pakkausselosteeseen turvallisuustiedoista. (Huomio: TFDA-merkinnän varoitukset/vasta-aiheet ja toimintamekanismin tiedot on merkitty ratkaisemattomiksi tietoaukoiksi — katso Johtopäätös alla.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Molemmat ennustetut indikaatiot ovat algoritmin ainoastaan (L5) antamia signaaleja, joilla ei ole tukevia kliinisiä tutkimuksia, kirjallisuutta tai uskottavaa mekaanista yhteyttä — mallin omasta perustelusta käy ilmi, että korkeat pistemäärät todennäköisesti kuvastavat tietokantakuvaajan läheisyyttä eikä biologista merkityksellisyyttä. Lääkettä ei myöskään markkinoida Taiwanissa, ja lääkkeen tason perusdata (toimintamekanismi, TFDA-merkintä) pysyy ratkaisemattomina.

**Jatkaaksemme tarvitaan seuraavaa:**
- TFDA-pakkausseloste (varoitukset/vasta-aiheet) — tällä hetkellä **estoava** tietoaukko
- JAK1-inhibition toimintamekanismin vahvistus DrugBankista — tällä hetkellä **korkea**-vakavuuden tietoaukko
- Upadacitinibin alkuperäisen hyväksytyn indikaation tiedot
- Prekliiniset tai mekaaniset tutkimukset, jotka yhdistävät suoraan JAK1-inhibition jompaan kumpaan ehdokkaisairauksista ennen kuin mitään lisäarviointivaiheesta harkitaan

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

