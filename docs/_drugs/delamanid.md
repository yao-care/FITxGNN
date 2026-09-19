---
layout: default
title: Delamanid
parent: Pelkkä mallin ennuste (L5)
nav_order: 118
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **7** kpl
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

# Delamanidi: Immuuntoleranssisia tuberkuloosia aiheuttavasta taudinmuodosta siipailun tuberkuloosiin (zoonootinen TB)

## Yhden lauseen yhteenveto

> Delamanidi on nitroimidatsoli-antimykobakteeri, jota käytetään immuuntoleranssisissa tuberkulooseissa (MDR-TB) -säännöstelyissä; yksityiskohtaista alkuperäisen indikaation tekstiä ei ole saatavilla tässä todistusmateriaalipaketissa, koska lääke on tällä hetkellä **markkinoimatta Suomessa** (0 lupaa rekisterissä).
> TxGNN-malli ennustaa aktiivisuutta **siipailun tuberkuloosia** vastaan (jota aiheuttaa *Mycobacterium bovis*), vaikka suora todiste tälle erityiselle indikaatiolle on tällä hetkellä minimaalinen — **0 kliinistä tutkimusta** ja **1 epäsuorasti liittyvä julkaisu**.
> Huomio: läheisesti liittyvä TB-indikaatio, joka sijoitettiin välittömästi sen alle eli "passiivinen tuberkuloosi", on tuettu **2 kliinisellä tutkimuksella** (mukaan lukien kaksi 2. ja 3. vaiheen tutkimusta) ja **20 julkaisulla**, ja se on todennäköisesti toimintakelpoisempi ehdokas tässä ennustejoukossa.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu todistusmateriaalipaketissa (markkinoimatta Suomessa; ei lupaa rekisterissä) |
| Ennustettu uusi indikaatio | Siipailun tuberkuloosi (zoonootinen, *M. bovis*) |
| TxGNN-ennuste-pistemäärä | 99.91% |
| Todistetasot | L5 |
| Suomen markkina-asema | ✗ Markkinoimatta |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Pidä varauksessa |

---

## Miksi tämä ennuste on kohtuullinen?

Yksityiskohtaisia mekanismin toiminta-aineistoja ei ole tällä hetkellä saatavilla. Tunnettujen tietojen perusteella delamanidi on nitrodi-hydro-imidstsoolioksatsooli-johdannainen, jota käytetään immuuntoleranssisia keuhkotuberkuloosi-säännöstelyjä sisältävissä yhdistelmähoidoissa; sen teho tuberkuloosia vastaan, jota aiheuttaa *Mycobacterium tuberculosis*, on vahvistettu kliinisesti.

Siipailun tuberkuloosi on *Mycobacterium bovis* -bakteerille aiheutunut tauti, joka kuuluu *Mycobacterium tuberculosis* -kompleksiin (MTBC) ja on lähellä sukua *M. tuberculosisille* sekä voi aiheuttaa zoonootisen ihmisen infektion. Koska delamaniidin antimykobakteeri-aktiivisuus kohdistuu MTBC-lajien välillä jaettuihin polkuihin (esim. mykolihappojen biosynteesin häiriintyminen nitroimidatsooli-luokan aineissa), mekanistinen ekstrapolaatio *M. bovis* -infektioihin on biologisesti uskottava.

On huomionarvoista, että kaikki seitsemän mallin parhaiten ennustamaa indikaatiota tälle lääkkeelle liittyvät tuberkuloosiin (siipailun TB, passiivinen TB, lintujen TB, tuberkulooma, tuberkuloottinen askites, ihon TB), mikä on johdonmukaista delamaniidin vakiintuneen farmakologian kanssa ja tarjoaa epäsuoraa tukea siipailun TB-ennusteen uskottavuudelle — vaikka suora todiste tälle erityiselle osa-indikaatiolle jää edelleen niukaksi.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei liittyviä rekisteröityjä kliinisiä tutkimuksia

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeiset löydökset |
|------|------|--------|---------|----------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Molekyyliepidemiologia | BMC Genomics | Kokonaisgenomisekvenssintutkimus, joka kuvaa geneettisen monimuotoisuuden ja lääkeresistenssin mekanismeja *M. bovis* -eristöissä, jotka aiheuttavat zoonootista ihmisen tuberkuloosia Egyptissä; ei suoraan arvioi delamaniidin hoidon tuloksia |

---

## Suomen markkina-tiedot

Tällä hetkellä markkinoimatta Suomessa; hyväksyttyjen tuotelupien rekisteriä ei ole saatavilla.

---

## Turvallisuusnäkökohdat

Turvallisueista tietoja varten ks. pakkausseloste.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä varauksissa**

**Perustelut:**
Erityiselle ennustetulle indikaatiolle — siipailun tuberkuloosille — ei ole suoraa kliinistä tai prekliinistä näyttöä delamaniidin käytön puolesta, ja lääkkeellä ei tällä hetkellä ole Suomen markkinavaltuutusta, johon rakentaa. Kriittiset turvallisuutta koskevat syötteet (TFDA-pakkausseloste varoitukset/vasta-aiheet, DG001) ja mekanismin toiminta-aiheet (DG002) on myös merkitty tietojen puutoksiksi, mikä estää täydellisen turvallisuuden arvioinnin.

**Jatkamista varten tarvitaan seuraavaa:**
- TFDA-pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä tietojen puute (DG001)
- Vahvistetut mekanismin toiminta-aineistot DrugBankista (DG002)
- Suora prekliininen tai kliininen todiste delamaniidin aktiivisuudesta erityisesti *M. bovis* -infektiota vastaan
- Harkitse **"passiivisen tuberkuloosin"** (sijoitus 2) arviointia vaihtoehtoisena/rinnakkaisena ehdokkaana sen vahvemman olemassa olevan todistetasoon nähden (CRUSH-TB [NCT05766267] ja PHOENIx MDR-TB [NCT03568383] -tutkimukset sekä 20 tukevaa julkaisua)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

