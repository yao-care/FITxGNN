---
layout: default
title: Ofatumumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 313
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Ofatumumab: ennustettu uusi käyttöaihe Krooninen lymfosyyttileukemia / pieni lymfosyyttilymfooma (CLL/SLL) (näytön taso L5). Alkuperäinen käyttöaihe: Relapsoiva-remittoiva multippeliskleroosi"
monitor_inn: "OFATUMUMAB"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "follicular lymphoma", "leukemia, lymphocytic, susceptibility to", "metastatic neoplasm", "malignant spiradenoma", "Langerhans cell histiocytosis"]
---

# Ofatumumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **8** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

# Ofatumumabi: Multippeliskleroosista krooniseen lymfosyyttileukemiaan / pieneen lymfosyyttilymfoomaan (CLL/SLL)

## Yhden lauseen yhteenveto

Ofatumumabi on CD20-vasta-aine, jota käytetään alun perin aaltomaisesti etenevän multippeliskleroosin (relapsoiva-remittoiva MS) hoitoon.
TxGNN-malli ennustaa sen voivan tehota **krooniseen lymfosyyttileukemiaan / pieneen lymfosyyttilymfoomaan (CLL/SLL)**.
Tätä suuntaa tukee tällä hetkellä **20 kliinistä tutkimusta** (mukana kolme vaiheen 3 tutkimusta) ja **20 julkaisua**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Relapsoiva-remittoiva multippeliskleroosi |
| Ennustettu uusi käyttöaihe | Krooninen lymfosyyttileukemia / pieni lymfosyyttilymfooma (CLL/SLL); sijalla 1 ennusteluettelossa oli CLL/SLL:n molekulaarinen alatyyppi (pistemäärä 99,77 %), jolle ei löytynyt tutkimuksia. Tässä raportissa arvioidaan pääasiassa CLL/SLL-kokonaisuutta (sija 5) |
| TxGNN-ennustepistemäärä | 99,55 % (CLL/SLL) |
| Näytön taso | L1 (huomautus: vaiheen 3 tutkimuksissa ofatumumabi oli vertailuhoito, ks. alla) |
| Suomen markkinatilanne | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Proceed with Guardrails (jatka suojatoimin) |

---

## Miksi ennuste on perusteltu?

Tämän raportin käyttöön kootuissa tiedoissa ei ole tällä hetkellä yksityiskohtaista vaikutusmekanismitietoa. Tunnetun tiedon perusteella ofatumumabi on täysin ihmisperäinen anti-CD20-monoklonaalinen vasta-aine. Sen teho B-solujen tuhoamisessa on osoitettu, ja mekanistisesti se voi soveltua CLL/SLL:n hoitoon.

Ofatumumabi sitoutuu CD20-molekyylin kalvon lähellä olevaan epitooppiin ja aiheuttaa komplementtivälitteistä sytotoksisuutta sekä vasta-aineriippuvaista soluvälitteistä sytotoksisuutta. MS:ssa hoidon tavoitteena on vähentää autoreaktiivisia B-soluja. CLL/SLL:ssä taas pahanlaatuiset B-solut ilmentävät CD20:tä, joten sama kohde on hyödynnettävissä.

Ofatumumabilla on vakiintunut kehityshistoria CLL:ssä: vaiheen 3 tutkimus (duvelisibi vs. ofatumumabi, n=319), lukuisia vaiheen 2 tutkimuksia sekä meta-analyysejä. Huomionarvoista on, että vaiheen 3 tutkimuksissa ofatumumabi toimi **vertailuhaarana**, joten ne tukevat sen aktiivisuutta mutta eivät osoita sen ylivertaisuutta. Lisäksi CLL-hoidon nykystandardi (BTK- ja BCL2-estäjät) kilpailee ofatumumabin kanssa.

---

## Kliininen tutkimusnäyttö

Alla on valikoima CLL/SLL:n tutkimuksista (enintään 10 olennaisinta).

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01578707](https://clinicaltrials.gov/study/NCT01578707) | Vaihe 3 | Päättynyt | 391 | Ibrutinibi vs. ofatumumabi uusiutuneessa/refraktaarisessa CLL/SLL:ssä (ofatumumabi vertailuhoitona) |
| [NCT02004522](https://clinicaltrials.gov/study/NCT02004522) | Vaihe 3 | Päättynyt | 319 | Duvelisibi vs. ofatumumabi uusiutuneessa/refraktaarisessa CLL/SLL:ssä (DUO); ofatumumabi vertailuhoitona |
| [NCT02049515](https://clinicaltrials.gov/study/NCT02049515) | Vaihe 3 | Päättynyt | 99 | DUO-tutkimuksen jatko: duvelisibi tai ofatumumabi etenemisen jälkeen |
| [NCT01024010](https://clinicaltrials.gov/study/NCT01024010) | Vaihe 2 | Päättynyt | 82 | Pentostatiini, syklofosfamidi ja ofatumumabi aiemmin hoitamattomassa CLL:ssä |
| [NCT03280160](https://clinicaltrials.gov/study/NCT03280160) | Vaihe 2 | Tuntematon | 84 | Ibrutinibi ja sen jälkeinen ofatumumabikonsolidaatio hoitamattomassa CLL/SLL:ssä |
| [NCT01113632](https://clinicaltrials.gov/study/NCT01113632) | Vaihe 2 | Päättynyt | 77 | Ofatumumabi iäkkäille ja fludarabiinia kieltäytyville hoitamattomille potilaille |
| [NCT01496976](https://clinicaltrials.gov/study/NCT01496976) | Vaihe 2 | Päättynyt | 45 | Ofatumumabi + suuriannoksinen metyyliprednisoloni, sitten ofatumumabi + lenalidomidi (HiLOG), hoitamaton CLL/SLL |
| [NCT01243190](https://clinicaltrials.gov/study/NCT01243190) | Vaihe 2 | Päättynyt | 44 | Ofatumumabi varhaisvaiheen suuren riskin CLL/SLL:ssä |
| [NCT01217749](https://clinicaltrials.gov/study/NCT01217749) | Vaihe 1/2 | Päättynyt | 71 | Ibrutinibi + ofatumumabi uusiutuneessa/refraktaarisessa CLL/SLL:ssä |
| [NCT02135133](https://clinicaltrials.gov/study/NCT02135133) | Vaihe 2 | Päättynyt | 27 | Idelalisibi + ofatumumabi hoitamattomassa CLL/SLL:ssä |

Lisäksi follikulaarisessa lymfoomassa (ennusteluettelon sija 3, pistemäärä 99,70 %) on useita päättyneitä vaiheen 2 tutkimuksia (mm. NCT01286272, n=135; NCT00494780, n=59; NCT01190449, n=51; NCT00394836, n=116) ja yksi päättynyt vaiheen 3 tutkimus (NCT01077518, n=346, päättyi ennenaikaisesti), mutta vaiheen 3 -tulokset eivät ole tässä aineistossa arvioitavissa.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [37138022](https://pubmed.ncbi.nlm.nih.gov/37138022/) | 2023 | Meta-analyysi | Annals of Hematology | Ofatumumabipohjaisten hoito-ohjelmien teho CLL:ssä verrattuna muihin hoitoihin |
| [28580841](https://pubmed.ncbi.nlm.nih.gov/28580841/) | 2017 | Systemaattinen katsaus ja meta-analyysi | Hematology | 13 kliinisen tutkimuksen yhdistetty arvio ofatumumabin tehosta ja turvallisuudesta CLL:ssä |
| [24925211](https://pubmed.ncbi.nlm.nih.gov/24925211/) | 2015 | Vaiheen 2 tutkimus | Leukemia & Lymphoma | Ofatumumabi + bendamustiini aiemmin hoidetussa CLL/SLL:ssä |
| [25736010](https://pubmed.ncbi.nlm.nih.gov/25736010/) | 2015 | Kliininen hoitosuositus (NCCN) | JNCCN | Uudet anti-CD20-vasta-aineet (ofatumumabi, obinututsumabi) mahdollistivat tehokkaat kemoimmunoterapiat |
| [25828085](https://pubmed.ncbi.nlm.nih.gov/25828085/) | 2015 | Katsaus | Haematologica | Ofatumumabin rooli immunoterapiana CLL:ssä |
| [26566719](https://pubmed.ncbi.nlm.nih.gov/26566719/) | 2015 | Katsaus | Expert Opin Drug Saf | Ofatumumabin turvallisuusprofiili CLL:ssä; suotuisa toksisuusprofiili |
| [20481657](https://pubmed.ncbi.nlm.nih.gov/20481657/) | 2010 | Lääkekatsaus | Drugs | Ofatumumabi indusoi ADCC:n ja CDC:n; pivotaalitutkimus fludarabiini- ja alemtutsumabirefraktaarisessa CLL:ssä |
| [20068404](https://pubmed.ncbi.nlm.nih.gov/20068404/) | 2009 | Lääkekatsaus | mAbs | Ofatumumabi sitoutuu uuteen kalvon lähellä olevaan epitooppiin ja irtoaa kohteesta hitaammin kuin rituksimabi |
| [32482755](https://pubmed.ncbi.nlm.nih.gov/32482755/) | 2020 | Katsaus | Haematologica | CD20:n säätely ja toiminta; ilmentyminen vaihtelee B-solusyöpien välillä |
| [38174814](https://pubmed.ncbi.nlm.nih.gov/38174814/) | 2024 | Systemaattinen katsaus (Cochrane) | Cochrane Database Syst Rev | Ylläpitohoito kroonisessa lymfosyyttileukemiassa |

Follikulaarisesta lymfoomasta on lisäksi satunnaistettuja ja vaiheen 2 julkaisuja, esim. [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) (CALGB 50904, 2019) ja [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) (rituksimabirefraktaarinen FL, 2012; vasteosuus 13 % / 10 %).

---

## Suomen markkinatiedot

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005410 | Kesimpta | Ei tietoa | Relapsoiva-remittoiva multippeliskleroosi (myyntilupa peruutettu) |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito / immunoterapia (anti-CD20-monoklonaalinen vasta-aine) |
| Myelosuppression riski | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Oksettavuusluokitus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Seurattavat parametrit | Verenkuva (erittelylaskenta), maksa-arvot, immunoglobuliinitasot ja infektioiden seuranta |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |

---

## Turvallisuushuomiot

- **Lääkeyhteisvaikutukset:** Yhteisvaikutuskyselyssä löytyi yhteensä 80 yhteisvaikutusta. Merkittäviksi (Major) luokiteltuja ovat mm. deferipronin, samarium-153-leksidronaamin, adalimumabin, barisitinibin, sertolitsumabipegolin, kladribiinin ja klotsapiinin kanssa. Kohtalaisia (Moderate) ovat mm. atsatiopriinin, alemtutsumabin, anakinran, kanakinumabin, tsidovudiinin, klooramfenikolin ja roflumilastin kanssa sekä useiden rokotteiden (mm. jäykkäkouristustoksoidi, pernaruttorokote, elävä koleraroke) kanssa. Yhteisvaikutukset liittyvät pääosin päällekkäiseen immuunisuppressioon tai luuydinsuppressioon.

Muuten turvallisuustiedot: katso valmisteyhteenveto.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Proceed with Guardrails (jatka suojatoimin)**

**Perustelut:**
- CLL/SLL:ssä on useita päättyneitä vaiheen 2 tutkimuksia, kolme päättynyttä vaiheen 3 tutkimusta (ofatumumabi vertailuhoitona) sekä meta-analyyseja, ja CD20 on perusteltu hoitokohde. Näyttö on kuitenkin epäsuoraa ofatumumabin ylivertaisuuden osalta, ja nykystandardi (BTK- ja BCL2-estäjät) sekä onkologisen valmisteen kaupallinen poisto rajoittavat soveltuvuutta.
- Follikulaarinen lymfooma on toissijainen tutkimuskysymys (vain vaiheen 2 näyttö, useita keskeytettyjä tutkimuksia). Muut ennusteet (CLL/SLL:n alatyypit, alttiusnimike, metastaattinen kasvain, pahanlaatuinen spiradenooma, Langerhansin solujen histiosytoosi) ovat Hold-tasolla, koska itsenäistä näyttöä ei ole tai se on hyvin vähäistä.

**Jatkaminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kerääminen (Fimean aineisto puuttuu) ennen turvallisuusseulontaa
- Yksityiskohtaiset vaikutusmekanismitiedot
- Saatavuuden selvitys, koska Suomessa on vain peruutettu myyntilupa, sekä vertailu nykyisiin standardihoitoihin (BTK- ja BCL2-estäjät)
- Turvallisuuden seurantasuunnitelma erityisryhmille (iäkkäät potilaat, infektioriski, immunosuppressiivisten lääkkeiden yhteiskäyttö)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

