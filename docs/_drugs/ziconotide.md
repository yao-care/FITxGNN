---
layout: default
title: Ziconotide
parent: Kohtalainen näyttö (L3-L4)
nav_order: 410
evidence_level: L4
indication_count: 10
---

# Ziconotide
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **10** kpl
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

# Zikonotidi: Kroonisesta kipusta migraiiniin

## Yhden lauseen yhteenveto

> Zikonotidi on N-tyypin kalsiumkanavaestäjä, jota alun perin käytetään selkäydintälineisesti muille hoitomuodoille vastustuskykyisten kroonisten vakaiden kipujen hoitoon (nämä tiedot eivät ole saatavilla strukturoituna tässä todistuspaketissa; lähteenä yleinen lääkkeistä saatava tieto). TxGNN-malli ennustaa sen olevan tehokas **migraiinin** hoidossa, mutta tätä tukee tällä hetkellä vain **0 kliinistä tutkimusta** ja **1 tapausraportin julkaisu**, joten todistusperusta on erittäin heikko.

---

## Pikakatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Muille hoitomuodoille vastustuskykyinen krooninen vakava kipu, joka vaatii selkäydintälineistä analgesiahoitoa *(ei kirjattu todistuspaketissa — yleinen lääkkeistä saatava tieto; original_indications-kenttä on tyhjä)* |
| Ennustettu uusi indikaatio | Migraini |
| TxGNN-ennustuspisteet | 99.92% |
| Todisteiden taso | L4 |
| Taiwanin markkina-asema | Ei markkinoilla (Ei markkinoilla) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaiset vaikutusmekanismin tiedot eivät ole saatavilla todistuspaketissa (original_moa: Tietoaukko). Tämän ennustetun uudelleenkäytön perustelun mukaan Ziconotidi estää valikoivasti N-tyypin (Cav2.2) jänniteohjattuja kalsiumkanavia ja estää presynaptisen hermoston välittäjäaineiden, kuten glutamaatin ja CGRP:ään liittyvien polkujen vapautumista.

Migraiinin patofysiologia liittyy trigeminivaskularisen järjestelmän epänormaaliin hermoston välittäjäaineiden vapautumiseen, ja perinnöllinen hemipleginen migraini on geneettisesti yhteydessä P/Q-tyypin (CACNA1A) kalsiumkanavien mutaatioihin. Tämä antaa kalsiumkanavan modulaatiolle yleistä mekanistista uskottavuutta migraiinin hoidossa.

Kuitenkin kanavan alatyyppi, jota Ziconotidi estää (N-tyyppi), eroaa alatyypistä, joka on geneettisesti yhteydessä migraiiniin (P/Q-tyyppi), joten tämä mekanistinen ekstrapolointi tulee käsitellä varovaisuudella. Tukitodisteet rajoittuvat yhteen vuoden 2015 tapausraporttiin, jossa kroonisen migraiinin päänsärky ratkesi selkäydintälineisellä Ziconotidi-hoidolla — informatiivinen signaali, mutta kaukana vahvistavasta näytöstä.

---

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-------|--------|-------|-------------------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Tapausraportti | Journal of Pain Research | Yksittäinen tapaus, jossa kroonisen migraiinin päänsärky ratkesi selkäydintälineisen Ziconotidi-hoidon jälkeen; raportointi keskittyi sen N-tyypin kalsiumkanavan estävään vaikutukseen kroonisessa kovassa kivussa ilman opioidien aiheuttamia toleranssi- ja riippuvuusongelmia |

---

## Taiwanin markkina-tiedot

Ziconotidi ei ole tällä hetkellä markkinoilla Taiwanissa (0 lupaa tietueissa), joten tuote- ja lupitaulukko ei ole saatavilla.

---

## Turvallisuusnäkökohdat

Turvallisuustiedot (keskeiset varoitukset, vasta-aiheet, lääkevuorovaikutukset) ovat kokonaan puuttuvat tästä todistuspaketista — TFDA:n pakkausselosteen varoitukset/vasta-aiheet-kohta on merkitty **estäväksi** tietoaukoksi (DG001), mikä estää muodolliseen S1-turvallisuuden esiarviointiin osallistumisen.

> Turvallisustiedot löytyvät pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
- Korkeimmalle sijoitetulla ennustetulla indikaatiolla (migraini) on vain yksi tapausraportti ja nolla kliinistä tutkimusta, ja mekanistinen yhteys perustuu N-tyypin kalsiumkanavaan, joka eroaa migraiiniin geneettisesti liittyneestä P/Q-tyypin kanavasta. Turvallisuustiedot ovat kokonaan puuttuvat (estävä aukko), ja lääke ei ole markkinoilla Taiwanissa — mikään kriteereistä "Jatka" tai "Jatka valvonnalla" ei täyty.

**Jatkamista varten tarvitaan seuraavat tiedot:**
- TFDA:n pakkausseloste varoituksineen ja vasta-aiheet (DG001, estävä)
- Todennettava vaikutusmekanismin tieto DrugBank API:n kautta (DG002)
- Prospektiivinen tai havainnoiva kliininen tutkimus, joka nimenomaisesti arvioi Ziconotidea migraiinin hoidossa, ottaen huomioon edellä mainitun N-tyypin ja P/Q-tyypin kanavien välisen eron
- Selkäydintälineisen antoreitin toteutettavuuden ja hyväksyttävyyden vahvistaminen migraiinipotilaiden osalta, koska Ziconotiden hyväksytty antoreitti on huomattavasti invasiivisempi verrattuna vakiomuotoisiin migraiinin hoitokeinoihin

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

