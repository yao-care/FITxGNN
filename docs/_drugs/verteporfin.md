---
layout: default
title: Verteporfin
parent: Pelkkä mallin ennuste (L5)
nav_order: 401
evidence_level: L5
indication_count: 1
---

# Verteporfin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

# Verteporfini: neovaskularisaation valokuvallisesta hoidosta mitokondriaalisen oksidatiivisen fosforylaation häiriöihin

## Yhden lauseen yhteenveto

Verteporfini (DrugBank DB00460) on bentsoporfyriinijohdannainen valoherkkä aine, joka on vakiintunut valokuvallisen hoidon käytössä korioideaalisen neovaskularisaation hoitoon. TxGNN-malli ennustaa, että se voi olla merkityksellinen **ydingenomiin liittyvien poikkeavuuksien aiheuttamille mitokondriaalisen oksidatiivisen fosforylaation häiriöille**, mutta tätä ennustetta tukevat tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** — se on pelkästään mallin antama signaali, jolla ei vielä ole riippumatonta näyttöä.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Valokuvallinenhoidon käyttö korioideaalisen neovaskularisaation hoitoon (esim. ikään liittyvä makularappeuma) — perustuu vakiintuneisiin farmakologisiin tietoihin; ei sisälly tähän näyttöpakettiin, jossa puuttuvat `original_indications`-tiedot |
| Ennustettu uusi indikaatio | Ydingenomiin liittyvien poikkeavuuksien aiheuttama mitokondriaalinen oksidatiivisen fosforylaation häiriö |
| TxGNN-ennusteen pistemäärä | 99.49% (maailmanlaajuinen sijoitus 5558) |
| Näytön taso | L5 |
| Taiwanin markkinatilanne | Ei markkinoilla (ei markkinoitu) |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Odottaa |

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaisia toimintamekanismin tietoja ei ole saatavilla tässä näyttöpaketissa (merkitty tietojen puutteeksi **DG002**, korkea vakavuus). Vakiintuneiden farmakologisten tietojen perusteella verteporfini kertyy mieluiten nopeasti jakautuviin ja neovaskularisoiduissa kudoksissa, ja kun se aktivoidaan ei-lämpimällä punavalolla, se tuottaa reaktiivisia happiyhdisteitä, jotka valikoidusti vahingoittavat kohteen endoteelia — sen vakiintunut kliininen rooli on oftalmologinen valokuvallinenhoidon soveltaminen.

Ennustetulla indikaatiolla — ydingenomiin liittyvälla mitokondriaalisen oksidatiivisen fosforylaation häiriöllä — ei ole ilmeistä mekanistista yhteneväisyyttä tämän fotoaktivaatioprosessin kanssa. TxGNN:n pistemäärä heijastaa tietoverkkojen assosiaatiota pikemminkin kuin vahvistettua farmakologista yhteyttä, ja paketin omat `repurposing_rationale`-kentät (`mechanistic_link`, `similarity_to_original`) on molemmat merkitty **odottaviksi**, mikä tarkoittaa, että asiantuntijapohjaista mekanistista tarkistusta ei ole vielä suoritettu.

Koska alkuperäinen indikaatio puuttuu myös tästä näyttöpaketista (tyhjä `original_indications`), alkuperäisen ja ennustetun indikaation välinen vertailu ei voi perustua annettuihin tietoihin. Tämä ennuste tulisi käsitellä vain hypoteesia herättävänä, kunnes mekanistinen tarkistus on suoritettu ja TFDA/viranomaislaajennus on vahvistettu (tietojen puute **DG001**, esto-vakavuus).

## Kliiniset tutkimusnäytöt

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäytöt

Tällä hetkellä asiaan liittyvää kirjallisuutta ei ole saatavilla.

## Taiwanin markkinatiedot

Verteporfini ei ole markkinoilla Taiwanissa (markkinatilanne: ei markkinoitu), jossa on 0 aktiivista valtuutta kirjattuna — lisensitaulukkoa ei ole saatavilla.

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odottaa**

**Perustelut:**
Tämä on L5, pelkästään mallin antama ennustesignaali, jolla ei ole kliinisiä tutkimuksia, kirjallisuutta eikä suoritettua mekanistista analyysia, yhdistettynä estävään tietojen puutteeseen TFDA-laajennuksesta. Tällä hetkellä ei ole riittäviä näyttöjä edetäkseen edes turvavalvonnan alaisina.

**Edetäkseen tarvitaan seuraava:**
- TFDA:n pakkausseloste (varoitukset/vasta-aiheet) — esto-puute DG001
- Vahvistettu toimintamekanismi (DrugBank/alkuperäinen kirjallisuus) — korkea puute DG002
- Vahvistetut alkuperäisen indikaation tiedot (tällä hetkellä tyhjät tässä paketissa)
- `mechanistic_link`- ja `similarity_to_original`-perustelun analyysin saattaminen loppuun
- Jatkuva seuranta nousevan kliinisen tutkimuksen tai kirjallisuuden osalta tästä indikaatiosta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

