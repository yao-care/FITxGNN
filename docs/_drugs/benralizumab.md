---
layout: default
title: Benralizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 67
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

# Benralizumab: Vakavasta eosinofiilistä astmasta immuunivälitteisen verihiutaleisyyden hoitoon

## Tiivistelmä yhdessä lauseessa

Benralizumab on monoklonaalinen vasta-aine, jonka vakiintunut käyttöaihe on vaikea eosinofiilistä astma, jossa se poistaa eosinofiileja anti-IL-5Rα/ADCC-mekanismilla. TxGNN-malli ennustaa mahdollisen roolin **immuunivälitteisessä verihiutaleisyydessä (ITP)**, mutta tämä yhdistelmä on tällä hetkellä tuettu **nollalla kliinisellä tutkimuksella** ja **nollalla julkaisulla** — se on puhtaasti mallin tuottama hypoteesi, jolla on eksplisiittisesti heikko mekanistinen perustelu.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihe | Vaikea eosinofiilistä astma (päätelty tukevista tutkimuspaketista; ei vahvistettu paikallisen markkinaluvan tietojen perusteella, koska lääketta ei myydä tällä markkinalla) |
| Ennustettu uusi käyttöaihe | Immuunivälitteinen verihiutaleisyys (ITP) |
| TxGNN-ennustepisteet | 99,34% |
| Näytön taso | L5 |
| Suomen markkina-asema | ✗ Ei markkinoilla |
| Rekisteröintien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Tarkempaa tietoa benralizumabin toimintamekanismista ei ole saatavilla tämän markkinan rakenteisista tiedoista. Kerätyn tukevien näyttöjen perusteella benralizumab on anti-IL-5Rα monoklonaalinen vasta-aine, joka poistaa eosinofiileja vasta-aineriippuvaisen solujen välittämän sytotoksisuuden (ADCC) kautta ja vaikuttaa pääasiassa eosinofiilistiseen astmaan liittyvien tyypin 2 inflammaation polkuun.

Immuunivälitteinen verihiutaleisyys (ITP) sitä vastoin johtuu vasta-aineiden välittämästä verihiutaleiden tuhoutumisesta makrofagien ja pernassa — mekanismissa, joka keskittyy humoraaliin autoimmuniteettiin ja retikuloendoteeliaalisen järjestelmän selektioon, ei eosinofiilin biologiaan. Mallin ehdottama yhteys on vain epäsuora hypoteesi: eosinofiilien on havaittu olevan sivustakatsojia joissakin autoimmunisairauksissa, mutta vakiintunut syy-seuraussuhde tai mekanistinen polku IL-5Rα-välitteisestä eosinofiilin poistosta verihiutaleiden säästämiseen tai ITP:n remissioon ei ole olemassa.

Lyhyesti sanottuna tämä on tapaus, jossa TxGNN samankaltaisuuspistemäärä on korkea, mutta taustalla oleva biologia ei tällä hetkellä tarjoa uskottavaa syy-seuraussuhdetta, eikä yhtään tutkimusta tai tapausraportointiinsa ole vielä tuotettu hypoteesin suoraan testaamiseksi.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole asiaan liittyvää kirjallisuutta saatavilla.

## Suomen markkina-asema

Benralizumab ei ole tällä hetkellä markkinoilla Suomessa — tiedostoissa ei ole markkinointilupeja (kokonaislupia: 0).

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta.

*(Huomautus: Paikallisia varoituksia, vasta-aiheita ja lääkkeiden välisiä vuorovaikutuksia koskevat tiedot eivät olleet saatavilla — tämä on kirjattu estäväksi tietojen puuttumaksi (DG001), joka estää muodollisen S1-turvallisuuden esiarviointia.)*

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelu:**
Tämä ennuste sijaitsee alimmalla näytön tasolla (L5) — ei kliinisiä tutkimuksia, ei kirjallisuutta, ja vain itse kuvatulla "heikolla, epäsuoralla" mekanistisella hypoteesilla tuettua. Yhdistettynä puuttuviin paikallisiin turvallisuus-/merkintätietoihin (estävä puuttuma DG001) ja puuttuviin MOA-vahvistuksiin (DG002), tällä hetkellä ei ole perustetta edetä tämän ehdokkaan osalta mallin tuloksen yli.

**Jotta voidaan edetä, tarvitaan seuraavaa:**
- TFDA/paikallinen pakkausseloste (varoitukset, vasta-aiheet) estävän puuttuman poistamiseksi ennen S1-turvallisuustarkastusta
- Vahvistettu toimintamekanismin tieto DrugBankista tai alkuperäisestä kirjallisuudesta
- Prekliininen tai translationaalinen näyttö IL-5Rα/eosinofiilin poiston yhdistämisestä verihiutaleiden autoimmuniteettiin, ennen tutkimuksen suunnittelun aloittamista
- Jatkuva valvonta tapausraporteista tai tutkijan aloittamista tutkimuksista, koska niitä ei tällä hetkellä ole olemassa

**Portfolion huomautus:** Viidestä käyttöaiheesta, joita TxGNN ennusti benralizumabille, dermatiitti (sijoitus 2) on aineellisesti enemmän näyttöä — 6 tutkimusta ja 20 julkaisua — mutta näyttö on suurelta osin negatiivista (HILLIER-vaiheen 2 RCT, NCT04605094, keskeytettiin, ja PMID 37178404 raportoi "vaikutuksen puuttumisesta" atopisen dermatiitin hoidossa). Tämä ehdokas vaatii oman erillisen arvioinnin sen sijaan, että se yhdistettäisiin tähän.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

