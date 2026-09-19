---
layout: default
title: Atezolizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Atezolizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# ATEZOLIZUMAB: Uudelleenkäytön arviointi — riittämätön tietopohja jatkamista varten

## Yhden lauseen yhteenveto

ATEZOLIZUMAB (DrugBank ID: DB11595) on lääke, josta ei ole saatavilla alkuperäistä indikaatiota tai toimintamekanismin tietoja nykyisessä Evidence Pack -kokoelmassa.
Mitään TxGNN-ennustettuja indikaatioita ei ole luotu, ja lääkettä ei tällä hetkellä markkinoida Suomessa.
Tätä arviointia ei voida suorittaa loppuun ilman lisää tiedonkeruuta.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla |
| Ennustettu uusi indikaatio | Ennusteita ei ole saatavilla |
| TxGNN-ennusteen pistemäärä | Ei saatavilla |
| Näytön taso | N/A — ennusteita ei ole luotu |
| Suomen markkinatilanne | Ei markkinoinnissa |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidätetään** |

---

## Miksi tämä ennuste on järkevä?

ATEZOLIZUMAB:lle ei ole saatavilla TxGNN-ennustettuja indikaatioita tässä Evidence Pack -kokoelmassa. `predicted_indications` -kenttä on tyhjä, mikä tarkoittaa, että arviointia varten ei ole luotu uudelleenkäytön ehdokkaita. Ilman ennustetusta indikaatiota tämän raportin keskeistä kysymystä — voiko lääkettä sijoittaa uudelleen — ei voida käsitellä.

Toimintamekanismin tiedot puuttuvat myös. MOA-tietoja vaaditaan, jotta voidaan muodostaa mekaaninen perustelu, joka linkittää tunnetun farmakologisen toiminnan uuteen terapeuttiseen kohteeseen. Ilman sitä ei voida muodostaa edes laadullisia uskottavuusväitteitä.

Lopuksi ATEZOLIZUMAB:lla ei ole hyväksyttävää tuotetta Suomessa (0 hyväksyntää, markkinatilanne: ei markkinoinnissa), mikä tarkoittaa, että uudelleenkäytön laajentamisen arviointiin ei ole paikallista sääntelyyn liittyvää vertailupohjaa.

---

## Kliiniset tutkimustodisteet

Tällä hetkellä tähän arviointiin liittyviä kliinisiä tutkimuksia ei ole rekisteröity.

---

## Kirjallisuustodisteet

Tällä hetkellä tähän arviointiin liittyvää kirjallisuutta ei ole saatavilla.

---

## Suomen markkinatiedot

ATEZOLIZUMAB:ia ei tällä hetkellä markkinoida Suomessa. Tuotehyväksynnät eivät ole tallessa.

---

## Turvallisuushuomiot

Turvallisuustietojen osalta viittaa pakkausselosteeseen.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätetään**

**Perustelut:**
ATEZOLIZUMAB:n Evidence Pack -kokoelma on kriittisesti epätäydellinen kaikissa arviointimitoissa — ennustetut indikaatiot, toimintamekanismi, alkuperäinen indikaatio ja turvallisuustiedot puuttuvat kaikki. Merkityksellinen uudelleenkäytön arviointi ei ole mahdollista nykyisessä tilassa.

**Jatkaakseen seuraavaa tarvitaan:**

- **TxGNN-ennusteen tulokset**: `predicted_indications` -kenttä on täytettävä, ennen kuin mitään uudelleenkäytön suuntaa voidaan arvioida
- **Toimintamekanismi (MOA)**: Kysy DrugBank API:a (DB11595) hakemaan farmakologisen toiminnan ja lääkkeen luokan tiedot
- **Alkuperäinen indikaatio**: Hae Fimean tuoterekisteristä tai viitteellisistä merkinnöistä EMA:lta tai FDA:lta
- **Turvallisuustiedot**: Lataa ja jäsennä pakkausselose-PDF saadaksesi varoitukset, vasta-aiheet ja erityisväestöjen varotoimet
- **Lääke-lääke-vuorovaikutustiedot**: Kysy uudelleen DDI-tietokantaa; nykyinen tulos on `not_found` (0 vuorovaikutusta palautettu)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

