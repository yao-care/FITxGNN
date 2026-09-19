---
layout: default
title: Icatibant
parent: Vahva näyttö (L1-L2)
nav_order: 186
evidence_level: L1
indication_count: 7
---

# Icatibant
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **7** kpl
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

# Ikatibantti: Perinnöllisestä angioödeemasta (HAE) C1-inhibiittorin puutokseen

## Yhden lauseen yhteenveto

> Ikatibantti (DrugBank DB06196) on bradykiniini-B2-reseptorin antagonisti, jota käytetään maailmanlaajuisesti (tuotenimi Firazyr) perinnöllisen angioödeeman (HAE) äkillisten kohtausten hoitoon, kun kyseessä on C1-inhibiittorin puutos, vaikka sitä **ei ole tällä hetkellä markkinoilla Suomessa**.
> TxGNN-malli ennustaa sen olevan tehokas **C1-inhibiittorin puutokseen**, tilalle, joka on HAE:n taustalla, ja sillä on tukena **23 kliinistä tutkimusta** ja **20 julkaisua**.
> Tämä on enemmän vahvistus ikatibantin jo vakiintuneen maailmanlaajuisen indikaation osalta kuin uuden käyttöindikaation tunnistaminen — avoin kysymys on Suomen markkinoille pääsy ja paikallinen merkintä, ei tehokkuus.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Perinnöllinen angioödeema (HAE), jonka aiheuttaa C1-inhibiittorin puutos *(pääteltävissä kliinisistä tutkimuksista/kirjallisuustodisteista; virallista lisenssitekstiä Suomesta ei ole saatavilla)* |
| Ennustettu uusi indikaatio | C1-inhibiittorin puutos |
| TxGNN-ennustepisteet | 99,99 % |
| Todistusaineiston taso | L1 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksilla |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla suoraan tästä paketista DrugBankista (tietoaukko DG002). Kuitenkin tässä kerätty kirjallisuustodiste dokumentoi ikatibantin **selektiivisenä bradykiniini-B2-reseptorin antagonistina**: se kilpailevasti estää bradykiniinia sitoutumasta sen B2-reseptoriin, mikä estää verisuonipermeabiliteettia lisäävää ja turvotusta aiheuttavaa vaikutusta, jonka bradykiniini muuten aiheuttaa (PMID 34965883, PMID 24925394).

C1-inhibiittorin (C1-INH) tehtävänä on tavallisesti hillitä kallikreiiini-kiniini-kaskaadia; kun sitä puuttuu tai se toimii väärin (perinnöllinen tai hankittu), hallitsematon bradykiniinin tuotanto ajaa turvotuskohtauksia, jotka määrittelevät perinnöllistä ja hankittua angioödeemaa. Ikatibantti ei korjaa entsyymin puutosta itsessään, vaan estää viimeisen yhteisen loppupään effetorin (B2-reseptorin), mikä on syy siihen, että se on jo vakio tarpeen mukaan annettava hoito HAE-kohtauksille useilla markkinoilla (Japani, Iso-Britannia, Espanja, Taiwan, Kiina tämän paketin tutkimus- ja rekisteritodisteen mukaan).

Koska "C1-inhibiittorin puutos" on patofysiologinen merkintä samalle sairausprosessille, jonka ikatibantti jo hoitaa kliinisesti, TxGNN-ennuste tulisi lukea siten, että malli palauttaa oikein olemassa olevan, hyvin vahvistetun indikaation sen sijaan että se paljastaisi genuinisti uuden terapeuttisen hypoteesin. Tämän lainkäyttöalueen käytännön kysymys on siis rekisteröinti ja paikallinen merkintä, ei käsitteen todiste.

---

## Kliinisten tutkimusten todisteet

| Tutkimuksen numero | Vaihe | Tila | Osallistujamäärä | Keskeiset tulokset |
|---------|------|------|------|---------|
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Vaihe 3 | Päättynyt | 98 | Satunnaistettu, kaksoissokkouttu, lumekontrolloitu tutkimus ihonalaisesti annetusta ikatibantin injektiosta äkillisiin HAE-kohtauksiin |
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Vaihe 3 | Päättynyt | 84 | Satunnaistettu, kaksoissokkouttu, lumekontrolloitu tutkimus ihonalaisesti annetusta ikatibantin injektiosta ihon- ja vatsaontelon HAE-kohtauksiin |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Vaihe 3 | Päättynyt | 85 | Satunnaistettu, kaksoissokkouttu pää-päävertailututkimus: ikatibantti vs. suun kautta otettava traneksamiinihappo HAE:ssa |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Päättynyt | 1761 | Ikatibantin tulostutkimus (IOS) — suuri monikansallinen prospektiivinen rekisteri reaalimaailman turvallisuudesta ja tuloksista |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Vaihe 3 | Päättynyt | 151 | Avoin tutkimus itse antamasta ihonalaisesta ikatibantin injektiosta HAE-kohtauksiin |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A | Päättynyt | 179 | FIRAZYR-jälkimarkkinoinnin lääkkeiden käyttötutkimus Japanissa |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Vaihe 3 | Päättynyt | 32 | Yksittäisen annoksen ikatibantin farmakokinetiikka, siedettävyys ja turvallisuus lapsille ja nuorille HAE-potilaille |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Vaihe 3 | Päättynyt | 8 | Avoin ikatibantin tehokkuus-, PK- ja turvallisuustutkimus japanilaisissa HAE-potilaissa |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Vaihe 4 | Päättynyt | 5 | Ikatibantin injektio (Icanticure®) bradykiniini-indusoidussa angioödeemassa, Taiwanin NHI-korvattu hoitoympäristö |
| [NCT05489640](https://clinicaltrials.gov/study/NCT05489640) | N/A | Päättynyt | 85 | Reaalimaailman UK-tutkimus kotihoitopotilaan omakseen antamasta hoitosta — hoitokäytännöt ja potilaan raportoitavat tulokset |

---

## Kirjallisuustodisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|-----|------|------|---------|
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Katsaus | J Allergy Clin Immunol | C1-INH-puutosta aiheuttavan HAE:n tautitaakka Aasian ja Tyynenmeren alueella |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | Retrospektiivinen tutkimus | JACI In Practice | Kahden keskuksen analyysi diagnoosista, kulusta ja hoidosta hankkineessa C1-INH-puutoksessa |
| [37146882](https://pubmed.ncbi.nlm.nih.gov/37146882/) | 2023 | Havainnoiva tutkimus | JACI In Practice | Kansallinen UK-tutkimus HAE:n ja hankitun C1-inhibiittorin puutoksen väestörakenteesta |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospektiivinen tutkimus | J Clin Pharmacol | Reaalimaailman epävirallisen käytön reseptiinkirjoituskäytännöt C1-INH-väkevyyksille ja ikatibanttille |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Rekisterianalyysi | Clin Exp Allergy | Ikatibantin ja C1-inhibiittorin käyttö kurkunpään HAE-kohtausten hoidossa |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Rekisteri (IOS) | Allergy Asthma Clin Immunol | Reaalimaailman ikatibantin hoitotulokset espanjalaisissa HAE-1/2-potilaissa |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Katsaus | J Investig Allergol Clin Immunol | Yleiskatsaus nykyisistä ja nousevista HAE-terapioista, mukaan lukien ikatibantti |
| [33472202](https://pubmed.ncbi.nlm.nih.gov/33472202/) | 2021 | Valtakunnallinen retrospektiivinen tutkimus | Int Arch Allergy Immunol | Hankitun C1-INH-puutoksen esiintyminen, ominaisuudet ja hallinta Tšekin tasavallassa |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Kliiniset suositukset | Rev Med Interne | CREAK-diagnoosin ja -hoito-ohjeet hankitulle C1-INH-puutoksesta aiheutuneelle angioödeemalle |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Tapaussarja | J Clin Immunol | Ikatibantin ja uudelleenyhdistelmä-C1-inhibiittorin käyttö HAE-kohtauksissa raskauden aikana |

---

## Suomen markkinatieto

Ikatibantti ei tällä hetkellä pidä mitään myyntilupaa Suomessa (`market_status: Not marketed`, `total_licenses: 0`). Tuotetasoa koskevia lisensointitietoja ei ole saatavilla yhteenvetoa varten.

---

## Turvallisuushuomioon otettavat asiat

Katso turvallisuustiedoista pakkausesite.

*(Huomautus: Suomeen ominaisuuksien pakkausesite, keskeiset varoitukset, vasta-aiheet tai lääke-lääke-vuorovaikutustiedot eivät ole tällä hetkellä saatavilla — katso DG001/DG002 alla. Reseptintiedot lainkäyttöalueista, joissa ikatibantti/Firazyr on jo hyväksytty, esimerkiksi EU SmPC, tulisi tarkistaa väliaikaisena viitteenä.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksilla**

**Perustelut:**
Tehokkuustodiste on vahva ja johdonmukainen — kolme päättynyttä Vaihe 3 RCT:tä sekä suuri monikansallinen reaalimaailman rekisteri (IOS, n=1761) tukevat jo ikatibanttia HAE:ssa/C1-inhibiittorin puutoksessa (Todistusaineiston taso L1). Esto ei ole kliininen todiste vaan paikallisen sääntelyvalmiuden tila: ikatibanttia ei ole vielä markkinoilla Suomessa, ja Suomeen ominaisuuksien pakkausesite/turvallisuustiedot ovat **estävä** tietoaukko (DG001), joka on ratkaistava ennen kuin muodollinen S1-turvallisuustarkistus voidaan aloittaa.

**Jatkaakseen tarvitaan seuraavaa:**
- Hanki Fimean-hyväksytty pakkausesite (varoitukset ja vasta-aiheet) — Estävä aukko, DG001
- Vahvista vaikutusmekanismi ja lääkkeen luokittelu suoraan DrugBank API:n kautta — DG002
- Suorita muodollinen lääke-lääke-vuorovaikutus (DDI) -tarkistus (nykyinen automaattinen kysely palautti "not found")
- Arvioi Suomen sääntelytapa (esim. keskinäinen tunnustaminen/hajautettu menettely) ottaen huomioon, että ikatibantti on jo hyväksytty muualla EU:ssa ja Aasia-Tyynenmeren alueella tälle samalle indikaatiolle

*Huomautus: Ennusteet sijoituksilla 2–7 tässä todistusaineistopaketeissa (serpinopathy, pseudo-von Willebrand-tauti, primaarinen trombosyyttien vapautushäiriö, immuunivälitteinen nekrotisoiva myopatia, antisynthetaasi-oireyhtymä, Glanzmannin trombastenias) saivat kaikki L5/S0/Pidä — ei kliinisiä tutkimuksia, ei kirjallisuutta ja heikko-poissaoleva mekaaninen linkitys mallin omien perustelujen mukaan — eikä ole suositeltavaa jatkaa evaluointia näille.*

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

