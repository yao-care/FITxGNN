---
layout: default
title: Mannitol
parent: Pelkkä mallin ennuste (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitoli: Osmoottisesta diureettisesta käytöstä nefrogeenisen sopimattoman antidiureesi-oireyhtymän hoitoon

## Yhden lauseen yhteenveto

Mannitolin alkuperäistä indikaatiota ei voida vahvistaa tästä todistusaineistosta — Suomen markkinavaltuutuksia ei ole saatavilla ja mekanismin tiedot puuttuvat. TxGNN-malli ennustaa mahdollisen yhteyden **nefrogeeniseen sopimattoman antidiureesi-oireyhtymään (NSIAD)**, mutta tätä tukevat tällä hetkellä **0 kliinistä tutkimusta** ja vain **1 yleinen katsausartikkeli**, joka ei erityisesti arvioi mannitolia tälle indikaatiolle.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla — hyväksyttyä indikaatiotekstiä ei löydetty todistusaineistosta (0 Suomen valtuutusta kirjattu) |
| Ennustettu uusi indikaatio | Nefrogeeninen sopimattoman antidiureesi-oireyhtymä |
| TxGNN-ennustepistemäärä | 99.97% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on perusteltu?

Mannitolin mekanismin yksityiskohtaisia tietoja ei ole tällä hetkellä saatavilla todistusaineistosta (merkitty korkean vakavuuden tietovajeeksi). Yleisen farmakologisen tiedon perusteella mannitoli on osmoottinen diureetti, joka vetää vapaata vettä verisuonistoon ja edistää veden munuaisissa tapahtuvaa erittymistä; tämä yleinen ominaisuus on mallin mekanistisen yhteyden perusta NSIAD:iin.

NSIAD on harvinainen synnynnäinen häiriö, jonka aiheuttaa V2-vasopressiini-reseptorin voitontoiminnallinen mutaatio, joka tuottaa hyponatremian, joka jäljittelee SIADH:ta. Uusien käyttötarkoitusten perusteluteksti huomioi, että mannitolin osmoottinen diureesi voisi teoriassa nostaa seerumin natriumia akuutisti, mutta tämä **ei ole** NSIAD:n tavanomainen hoito (nesterajoitus tai urea ovat tavanomaiset). Ainoa tukeva julkaisu (PMID 26706473) on yleinen katsaus hyponatremian arvioinnin yleisiin sudenkuoppiin — se ei arvioi mannitolin tehoa NSIAD:ssa erityisesti.

Näiden perusteella mekaaninen uskottavuus on teoreettinen eikä näyttöön perustuva. On huomionarvoista myös, että kaikki 10 TxGNN:n mannitolille ennustamaa indikaatiota tässä todistusaineistossa arvioitiin "Pidätä"-kategoriaan, ja useissa on erityisiä huomautuksia, joita kannattaa merkitä: pahanlaatuisen hypertermian liittyvät ennusteet (sijoitukset 3–4, 7, 8, 10) voivat heijastaa sekaannusta dantroleenin kanssa (mannitoli on yleinen täytne/yhdessä annettu laimentaja IV-dantroleenille, ei aktiivinen MH-hoito), ja nefrogeenisen diabetes insipiduksen ennuste (sijoitus 9) voi heijastaa *vastakkaista* kausaalista suuntaa — mannitoli on tunnettu nefrogeenisen diabetes insipiduksen oireiden aiheuttaja eikä hoito sille. Tämä yleinen kuvio viittaa siihen, että mallin pistemäärä yksin ei ole vielä luotettava signaali tälle lääkkeelle.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|-------|--------|-------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Katsaus | European Journal of Internal Medicine | Yleinen katsaus hyponatremian arvioinnin yleisiin diagnostisiin sudenkuoppiin; ei arvioi mannitolin hoitoa NSIAD:ssa erityisesti |

---

## Suomen markkinatiedot

Mannitolista ei ole kirjattu Suomen markkinavaltuutuksia (0 valtuutusta; markkinatilanne: ei markkinoilla).

---

## Turvallisuushuomiot

Katso pakkausseloste turvallisuustiedoista. (Tärkeät varoitukset, vasta-aiheet ja lääkevuorovaikutustiedot eivät ole tällä hetkellä saatavilla tässä todistusaineistosta — TFDA/Fimea-merkinnän tietovajeeksi on merkitty Estävä, ja DDI-kysely ei palauttanut tuloksia.)

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelu:**
Pääennuste (NSIAD) perustuu teoreettiseen mekanistiseen argumenttiin, ei tavanomaisen hoidon käyttöön, ja sitä tukee ainoastaan yksi epäspesifinen katsausartikkeli ilman kliinisiä tutkimuksia. Yhdessä merkinnän/turvallisuustietojen estävän vajeen kanssa ja lääkkeen vahvistamattoman alkuperäisen indikaation ja ei-markkinoilla-olevuuden kanssa Suomessa, ei ole vielä riittävästi näyttöä edistyä alkuseulonnan jälkeen (S0).

**Edistymiseksi seuraavat kohdat ovat tarpeellisia:**
- TFDA/Fimea pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä Estävä tietovajeeksi
- Vahvistettu mekanismi DrugBankista — tällä hetkellä korkean vakavuuden tietovajeeksi
- Vahvistettu alkuperäinen indikaatio / mannitolin lisensointihistoria Suomessa
- Erityisiä kliinisiä tai mekanistisia tutkimuksia, joissa suoraan arvioidaan mannitolia NSIAD:ssa (ei yleisiä hyponatremian katsauksia)
- Lääkevuorovaikutus (DDI) -tietojoukko — nykyinen kysely ei palauttanut tuloksia
- Manuaalinen tarkistus, jotta voidaan sulkea pois sekaannus pahanlaatuisen hypertermian liittyvistä ja nefrogeenisen diabetes insipiduksen ennusteista, joita edellä mainittiin

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

