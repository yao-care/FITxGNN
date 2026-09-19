---
layout: default
title: Niraparib
parent: Pelkkä mallin ennuste (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: munasarjasyövästä kurkunkannen kasvaimeen

## Yhden lauseen yhteenveto

Niraparib on PARP-inhibiittori, joka on vakiintunut ylläpitohoitona uusiutuvan epiteelisen munasarjasyövän, munatorven ja primaarisen peritoneaalisen syövän hoitoon (perustuen tämän näyttöpakettiin sisältyviin tutkimus- ja kirjallisuustietueisiin; alkuperäisen indikaation ja toimintamekanismin strukturoidut säädösalakentät eivät ole täytetty). TxGNN-mallin parhaiten sijoittuva ennuste tälle lääkeaineelle on **kurkunkannen kasvain**, mutta tämä ehdokas on tällä hetkellä **nolla kliinistä tutkimusta ja nolla julkaisua** joiden perusteella se voidaan tukea – ennuste perustuu kokonaan mallin pisteytysarvoon.

## Pikakatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Munasarjasyöpä (uusiutuvan epiteelisen munasarjasyövän/munatorven/primaarisen peritoneaalisen syövän ylläpitohoito) – peräisin tutkimus- ja kirjallisuusviitteistä; strukturoidtu kenttä on tietoaukko |
| Ennustettu uusi indikaatio | Kurkunkannen kasvain |
| TxGNN-ennustuspistemäärä | 99.99% |
| Näyttötaso | L5 |
| Suomen markkinoiden tila | Ei kaupallisesti saatavilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on kohtuullinen?

Yksityiskohtainen toimintamekanismin tieto ei ole saatavilla strukturoidussa lääkeainetietueessa (`original_moa: [Data Gap]`). Näyttöpakettiin muualla sisältyvien tietojen perusteella niraparib on PARP (poly-ADP-riboosipolymeraasi) -inhibiittori, joka hyödyntää synteettistä letaalisuutta tuumoreissa, joissa on homologisen rekombinaation puute (HRD), mukaan lukien BRCA1/2-mutaatiot – sitä käytetään kliinisesti ylläpitohoitona platinasensitiiviissä, BRCA-mutoiduissa tai HRD-positiivisissa munasarjasyövissä.

Kurkunkannen kasvain kuuluu pään ja kaulan okasolusyöpään, tuumorityyppi, jossa on paljon pienempi HRD/BRCA-mutaatioiden esiintyvyys verrattuna korkeatasoisen seroosin munasarjasyöpään. Ei ole vakiintunutta biologista perustelua, joka yhdistäisi niraparib-inhibiittorin synteettisen letaalisuuden mekanismin tähän tuumoripaikkaan.

Näin ollen tämä ennuste on käsiteltävä puhtaana mallin pisteytyssignaalina eikä mekanistisesti tai kliinisesti tuetuna hypoteesina. Korkea TxGNN-pistemäärä heijastaa todennäköisesti tietokaavion upotussimilaarisuutta eikä todellista biologista uskottavuutta.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

## Sytotoksisuus

Niraparib on antineoplasminen (kohdennettu syöpälääke), joten tämä osio pätee.

| Kohta | Sisältö |
|------|---------|
| Sytotoksisuuden luokittelu | Kohdennettu hoito (PARP-inhibiittori) |
| Luuydinsuppression riski | Katso pakkausselosteesta varoituksista ja varotoimista |
| Pahoinvointiriskin luokittelu | Katso pakkausselosteesta varoituksista ja varotoimista |
| Seurantakohdat | Katso pakkausselosteesta varoituksista ja varotoimista |
| Käsittelyturvallisuus | Katso pakkausselosteesta varoituksista ja varotoimista |

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustiedot.

## Päätelmä ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Ei ole kliinistä tutkimus- tai kirjallisuusnäyttöä niraparibille kurkunkannen kasvaimeen, ja mekanistinen yhteys on teoreettista parhaimmillaan, koska pään ja kaulan syövissä HRD/BRCA-esiintyvyys on alhainen – tämä on L5, vain-mallinnettu ennuste. Huomionarvoista on, että alemmin sijoittuva ehdokas tässä näyttöpaketissa, "kystinen kasvain" (suurelta osin korkeatasoisen seroosin munasarjasyövän/endometriaalisen seroosin karsinooman heijastelu), on paljon paremmin tuettu (3 tutkimusta, 9 julkaisua, L2/S2) ja voi vaatia erillistä arviointia.

**Jatkamista varten tarvitaan seuraava:**
- TFDA/Fimea pakkausseloste (varoitukset, vasta-aiheet) – tällä hetkellä **estävä** tietoaukko, joka estää siirtymisen S1-turvallisuusarviointiin
- Vahvistettu toimintamekanismi-dokumentaatio DrugBankista
- Prekliininen tai mekanistinen tieto PARP-inhibiittorin aktiivisuudesta larynksi- tai hypofarynsks-tuumoreissa, tai HRD/BRCA-mutaatioiden esiintyvyystiedot kurkunkannen kasvaimille
- Jos halutaan jatkaa uudelleenkäyttötutkimusta, aseta etusijalle korkeamman näytön "kystinen kasvain" (HGSOC/endometriaalinen seeroosinen karsinooma) -ehdokas

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

