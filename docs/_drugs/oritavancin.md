---
layout: default
title: Oritavancin
parent: Pelkkä mallin ennuste (L5)
nav_order: 274
evidence_level: L5
indication_count: 3
---

# Oritavancin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

# Oritavancin: Ennustettu uusi indikaatio — Bacteroidaceae-infektiosairaus

## Yhden lauseen yhteenveto

> Oritavancin alkuperäinen hyväksytty indikaatio ei ole dokumentoitu nykyisessä datapakkauksessa (tietoaukko).
> TxGNN-mallin paras ennuste tälle lääkkeelle on **Bacteroidaceae-infektiosairaus**, pisteellä **99.48%**,
> mutta **0 kliinistä tutkimusta** ja **0 julkaisua** tukevat tätä suuntaa, ja lääkkeen oma toimintamekanismi on suoraan ristiriidassa ennusteen kanssa.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu saatavilla olevassa datassa (tietoaukko) |
| Ennustettu uusi indikaatio | Bacteroidaceae-infektiosairaus |
| TxGNN-ennusteen pistemäärä | 99.48% |
| Näytön taso | L5 |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Keskeytä |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaiset alkuperäisindikaatio- ja muodolliset toimintamekanismitiedot eivät ole saatavilla oritavancin-lääkkeelle tässä näyttöpaketissa (merkitty korkeaksi vakavuusasteiseksi tietoaukoksi). Ennusteen yhteydessä olevien mekanististen huomioiden perusteella oritavancin on lipoglykopeptidi-antibiootikka, joka estää bakteerin peptidoglykaanitransglykosylaatiota/transpeptidaatiota ja häiritsee solun kalvon eheyttä — mekanismi, joka vaikuttaa vain Gram-positiivisia organismeja vastaan (mukaanlukien MRSA ja VRE).

Tämä mekanismi ei tue parasta ennustetta. *Bacteroidaceae* ovat Gram-negatiivisia anaerobeja, joiden ulkokalvo estää glykopeptidien penetraation kohdesijaintiin — glykopeptideistä tiedetään farmakologisesti olevan tehotonta Gram-negatiivisia bakteereita vastaan. Ennuste on siis suorassa ristiriidassa vakiintuneen farmakologian kanssa huolimatta sen korkeasta TxGNN-pisteestä.

Sama kuvio pätee kahteen seuraavaksi sijoitettuun ehdokkaaseen tässä näyttöpaketissa: oftalminen herpes zoster (sijoitus 2, pistemäärä 99.03%) on viruksen (VZV) aiheuttama, jolle solun seinään kohdistuva antibiootikalla ei ole uskottavaa mekanismia; ja *Mycoplasma pneumoniae* -keuhkokuume (sijoitus 3, pistemäärä 99.01%) koskee patogeenia, jolla ei ole lainkaan solun seinää, joka on oritavancin ainoa tunnettu kohdesija. Kaikki kolme parasta tämän lääkkeen ennustetta on sisäisesti merkitty mekanistisesti perusteettomiksi, mikä on tärkeä varaus näitä raakoja TxGNN-pisteitä tulkittaessa.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole niihin liittyviä rekisteröityjä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta

## Suomen markkinatiedot

Oritavancin ei ole tällä hetkellä markkinoilla Suomessa; hyväksyntätietueita ei ole saatavilla (0 lisenssejä).

## Turvallisuushuomiot

Katso turvallisuustiedot pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Keskeytä**

**Perustelut:**
Huolimatta korkeasta TxGNN-ennustepisteestä (99.48%), tälle lääkkeelle annetussa uudelleenkäyttöperustelussa on eksplisiittisesti tunnistettu mekanistinen ristiriita — glykopeptidi-antibioottit eivät ole aktiivisia Gram-negatiivisia bakteereita vastaan — eikä ole lainkaan tosielämän näyttöä (ei kliinisiä tutkimuksia, ei kirjallisuutta). Kaksi seuraavaksi paremmin sijoittunutta ehdokasta tälle lääkkeelle osoittavat saman kuvion (viraalinen etiologia ja ilman solun seinää oleva patogeeni, molemmat yhteensopimattomia lääkkeen solun seinään kohdistuvan mekanismin kanssa), ja turvallisuustiedot (varoitukset, vasta-aiheet, lääkkeiden yhteisvaikutukset) ovat esto-aukko, joka estää S1-turvallisuusseulonnan.

**Jatkamista varten tarvitaan seuraavaa:**
- TFDA/Fimea-pakkausseloste-data (varoitukset, vasta-aiheet) — tällä hetkellä esto-aukko (DG001)
- Vahvistettu alkuperäinen indikaatio ja muodollinen MOA-dokumentaatio — tällä hetkellä korkean vakavuusasteen aukko (DG002)
- Riippumaton farmakologinen katsaus, joka sovittaa yhteen TxGNN-pistemäärän mekanistisen ristiriidan kanssa ennen kuin mitään lisäarviointia suoritetaan
- Lääkkeiden yhteisvaikutusten/turvallisuustietokannan haku (nykyinen tila: ei löydetty)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

