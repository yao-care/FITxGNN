---
layout: default
title: Trastuzumab Deruxtecan
parent: Pelkkä mallin ennuste (L5)
nav_order: 388
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
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

# Trastuzumab deruxtecan: HER2-positiivisesta rinta- ja mahalaukisen syövästä lääkkeen aiheuttamaan osteoporoosiin

## Yhden lauseen yhteenveto

Trastuzumab deruxtecan on HER2-kohdennettu vasta-aine-lääkekonjugaatti (ADC), jota käytetään tällä hetkellä HER2-positiivisen rintasyövän, mahalaukisen syövän ja muiden kasvainten hoitoon. TxGNN-malli ennustaa mahdollista yhteyttä **lääkkeen aiheuttamaan osteoporoosiin**, mutta tämä ennuste on tällä hetkellä tuettu **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja taustalla oleva mekanismi näyttää osoittavan vastakkaiseen suuntaan kliinisen uskottavuuden kannalta.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | HER2-positiivinen rintasyöpä, mahalaukisen syöpä ja muut kasvaimet (lääkkeen mekanismin kuvauksen mukaan; ei virallista indikaatiotietoa tässä tietoaineistossa) |
| Ennustettu uusi indikaatio | Lääkkeen aiheuttama osteoporoosi |
| TxGNN-ennustepistemäärä | 99.31% (sijoitus 7027) |
| Näyttötaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoitu |
| Hyväksynnän määrä | 0 |
| Suositeltu päätös | Keskeytä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla strukturoidussa muodossa. Tämän näyttöpaketin tunnettujen tietojen perusteella trastuzumab deruxtecan on HER2-kohdennettu vasta-aine-lääkekonjugaatti, jonka kuorma, DXd, on topoisomeraasi I -inhibiittori — sytostaattisen kemoterapia-agentin luokka. Se käytetään kliinisesti HER2-positiivisen rintasyövän, mahalaukisen syövän ja niihin liittyvien kasvainten hoitoon.

Ei ole tunnettua farmakologista polkua, jonka kautta tämä lääke hoitaisi osteoporosia. Päinvastoin, sytostaattiset ADC:t ja niihin liittyvät syöpähoidon skeemit (kemoterapia, kortikosteroidit, munasarjojen/endokriininen supressio) ovat tunnistettuja riskitekijöitä, jotka **aiheuttavat** luun menetystä sen sijaan, että ne kääntäisivät sitä. Ennustetun assosiaation suunta on siksi vastoin lääkkeen tunnetusta farmakologiasta.

Näistä syistä ennuste tulkitaan parhaiten todennäköisesti mallin kohinaksi tai kääntyneeksi/sekaantuneeksi assosiaatioksi TxGNN-tietoverkossa eikä aidoksi uudelleenkäyttösignaaliksi. Minkään tukevan kliinisen kokeen, kirjallisuuden tai vaikutusmekanismin dokumentaation puuttuminen rajoittaa entisestään luottamusta tähän ennusteeseen.

---

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta

---

## Suomen markkinatiedot

Tämä lääke ei ole tällä hetkellä markkinoitu Suomessa, eikä markkinointilupia ole kirjattu.

---

## Sytostaattisuus

| Kohde | Sisältö |
|-------|---------|
| Sytostaattisuusluokitus | Kohdennettu terapia (ADC), jolla on sytostaattinen kuorma — topoisomeraasi I -inhibiittori (DXd) |
| Luuydinsuppression riski | Katso pakkausselosteesta varoitukset ja varotoimet |
| Emetogenisuusluokitus | Katso pakkausselosteesta varoitukset ja varotoimet |
| Valvontakohteet | Katso pakkausselosteesta varoitukset ja varotoimet |
| Käsittelysuojaus | Sytostaattisen lääkkeen käsittelysuojaukset ovat sovellettavissa, koska kuormalla on sytostaattinen (topoisomeraasi I -inhibiittori) vaikutus |

---

## Turvallisuushuomiot

Katso pakkausselosteesta turvallisuustiedot.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Keskeytä**

**Perustelut:**
Huolimatta korkeasta TxGNN-ennustepisteestä, ei ole olemassa yhtään kliinistä koetta tai kirjallisuustoista (Näyttötaso L5), ja ehdotettu mekanismi vastustaa lääkkeen tunnetun sytostaattisen farmakologian kanssa — sytostaattiset syöpälääkkeet ovat luultavammin *aiheuttavat* lääkkeen aiheuttamaa osteoporosia sen sijaan, että ne hoitaisivat sitä. Tämä kuvio on yhdenmukainen mallin kohinan kanssa, ei aito uudelleenkäyttösignaali.

**Jotta voidaan edetä, seuraavaa tarvitaan:**
- Strukturoidut vaikutusmekanismin (MOA) tiedot DrugBankista tai toisesta virallisesta lähteestä
- TFDA/viranomaisten pakkausseloste (varoitukset, vasta-aiheet) täydellisen perusturvallisuusarvioinnin suorittamiseksi
- Itsenäinen biologinen perusteltu tai prekliininen näyttö, joka selittää mahdollisen yhteyden luun aineenvaihduntaan ennen lisäinvestointeja
- Kirjallisuus- ja tutkimusneuvojen jatkuva seuranta uusien näyttöjen varalta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

