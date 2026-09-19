---
layout: default
title: Rivastigmine
parent: Kohtalainen näyttö (L3-L4)
nav_order: 331
evidence_level: L4
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **1** kpl
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

# Rivastigmine: Alzheimerin taudista ja Parkinsonin taudin dementiasta glaukoomaan

## Yhden lauseen yhteenveto

Rivastigmine on kolinesteraasin estäjä, jota perinteisesti käytetään Alzheimerin taudin ja Parkinsonin taudin dementian hoitoon (tämä todistepaketti ei sisällä vahvistettua alkuperäisen indikaation tietuetta — katso huomautus alla). TxGNN-malli ennustaa, että se voi olla tehokas **glaukoomaan**, mikä on tällä hetkellä tuettu **0 kliinisen tutkimuksen** ja **3 julkaisun** perusteella, mukaan lukien yksi prekliininen eläintutkimus.

> Huomautus: `taiwan_regulatory.licenses` ja `drug.original_indications` ovat tyhjiä tässä todistupaketissa, joten yllä oleva alkuperäinen indikaatio heijastaa lääkkeen vakiintunutta kliinistä käyttöä Fimea-merkinnän sijaan. Rivastigmine (DB00989) ei ole tällä hetkellä markkinoilla Suomessa tämän tiedon mukaan.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla Fimean lupatiedoista (0 lupaa tiedostoissa); perinteisesti käytetään Alzheimerin taudin ja Parkinsonin taudin dementian hoitoon |
| Ennustettu uusi indikaatio | Glaukooma |
| TxGNN-ennustepiste | 99.27% |
| Todisteiden taso | L4 |
| Markkinatilanne Suomessa | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaista toimintamekanismi-tietoa ei ole saatavilla tässä todistupaketissa. Tunnettujen tietojen perusteella rivastigmine on selektiivinen asetyylikolinesteraasin (AChE) estäjä, aineluokka, jota perinteisesti käytetään asetyylikoliinin tasoja nostamaan keskushermostossa Alzheimerin taudin ja Parkinsonin taudin dementian hoitoon.

Mekanistinen yhteys glaukoomaan johtuu kolinergisen järjestelmän roolista silmänsisäisen paineen (IOP) sääntelyssa: asetyylikoli vaikuttaa suodattavan verkon M3-muskariinityypin reseptoreihin, mikä lisää välinesteiden ulosvirtausta ja alentaa IOP:ia. Ei-selektiivisiä AChE-estäjiä on pitkään käytetty kliinisesti IOP:ia alentavina mioottisina aineina, ja tässä paketissa oleva kirjallisuus huomauttaa, että "lievälla AChE:n estyksellä on osoitettu olevan terapeuttista merkitystä Alzheimerin taudissa, myastenia gravisissa ja glaukoomassa."

Suora prekliininen tutkimus (PMID 10673128) havaitsi, että paikallisesti annettu rivastigmine alensi IOP:ia normotensiivisissa kaneissa 8 tunnin aikana, mikä tukee biologista uskottavuutta uudelleenkäytölle sen vakiintuneen keskushermoston käytön lisäksi. Tämä jää kuitenkin eläin-/mekanistiseen todistukseen — yhtään ihmistutkimusta glaukooman potilaissa ei ole tunnistettu.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole liittyviä kliinisiä tutkimuksia rekisteröity.

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|------|--------|-------|-----------------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Prekliininen (eläintutkimus) | Journal of Ocular Pharmacology and Therapeutics | Paikallisesti annettu rivastigmine, selektiivinen AChE-estäjä, alensi silmänsisäistä painetta normotensiivisissa kaneissa 8 tunnin aikana |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Katsaus | Frontiers in Molecular Biosciences | Tarkastellaan kolinergisia (muskariinityypin) aineita IOP:n alentamiseen suodattavan verkon kautta; huomauttaa, että systeemiset sivuvaikutukset rajoittavat nykyisiä M3-agonisteja |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Katsaus | Expert Opinion on Therapeutic Patents | Tutkii AChE-estäjiä/reaktivointiaineita; huomauttaa, että lievälla AChE-estyksellä on terapeuttista merkitystä Alzheimerin taudissa, myastenia gravisissa ja glaukoomassa |

---

## Suomen markkinatiedot

Rivastigmine ei ole tällä hetkellä markkinoilla Suomessa — tässä todistupaketissa ei ole Fimean valtuutuksia (0 lupaa).

---

## Turvallisuushuomiot

Katso pakkausselosteesta turvallisuustiedot.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Todisteet rajoittuvat yhteen prekliiniseen kanitutkimukseen ja kahteen mekanistiseen katsaukseen, ilman kliinisiä tutkimuksia tai ihmisiä koskevia tutkimustietoja glaukoomassa; lääke ei myöskään ole tällä hetkellä markkinoilla Suomessa, ja turvallisuus-/varoitustiedot eivät ole saatavilla (lohkoava kuilu S1-turvallisuusseulonnalle).

**Jatkaakseen seuraavat asiat ovat tarpeen:**
- TFDA/Fimean pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä este (DG001)
- Vahvistettu toimintamekanismin tietue DrugBankista (DG002)
- Vahvistettu alkuperäinen indikaatio/lupatieto rivastigmiinille
- Ihmisiin perustuva kelpoisuuden osoitus tai vaihe 1/2 tutkimus glaukoomassa tai okulaarisessa hypertensioissa
- DDI-tiedot ennen mitään kliinistä arviointia

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

