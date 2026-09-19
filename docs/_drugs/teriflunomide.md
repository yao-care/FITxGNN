---
layout: default
title: Teriflunomide
parent: Vahva näyttö (L1-L2)
nav_order: 370
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **1** kpl
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

# Terflunomidi: Suomessa rekisteröimättömästä indikaatiosta uusiutuvaan-remissioon muotoiseen MS:ään

## Yhteenveto yhdessä lauseessa

Terflunomidi (DrugBank DB08880) ei ole tällä hetkellä markkinoilla Suomessa, joten alkuperäistä hyväksyttyä indikaatiota ei ole saatavilla paikallisesta sääntelyrekisteristä.
TxGNN-malli ennustaa, että se saattaa olla tehokas **uusiutuvaan-remissioon muotoiselle MS:lle (RRMS)** -
tällä hetkellä **28 kliinistä tutkimusta** ja **19 julkaisua** tukevat tätä suuntaa — huomattavasti, tämä on myös terflunomidin vakiintunut indikaatio muilla markkinoilla (markkinoitu muualla nimellä Aubagio), joten malli on pääasiassa palauttamassa tunnettua, laajasti vahvistettua indikaatiota eikä ehdottamassa uutta.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei saatavilla — Suomessa ei ole lupia tai rekisteröityjä indikaatioita |
| Ennustettu uusi indikaatio | Uusiutuvaan-remissioon muotoinen MS |
| TxGNN-ennustepistemäärä | 99.24% |
| Todisteiden taso | L1 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidättäydy |

## Miksi tämä ennuste on järkevä?

Rakenteinen `original_moa` -kenttä tälle lääkkeelle on tietoaukko. Kuitenkin tämän paketin kirjallisuustodisteet kuvaavat terflunomidin mekanismia: se on mitokondrion entsyymin dihydroorotaattidehydrogenaasi (DHODH) selektiivinen, palautuva estäjä, joka estää uuden pyrimidiinisynteesiä ja vähentää aktivoituneiden T- ja B-lymfosyyttien lisääntymistä (PMID 31098896). Tämä immunomodulaattori mekanismi on suoraan merkityksellinen autoimmuunisairauksille, T/B-solu-keskittyneille demyelinoiville sairauksille, kuten MS:lle.

Toisin kuin tyypillisen uudelleenkäytön ehdokas, täällä ei ole erillistä "alkuperäistä indikaatiota" vertailuun — todistuspaketti osoittaa nolla Suomen lisenssejä ja tyhjää `original_indications` -kenttää, mikä tarkoittaa, että terflunomidi on yksinkertaisesti koskaan ollut rekisteröity tälle markkinalle. Suomen ulkopuolella terflunomidi on kuitenkin vakiintunut, ohjeistuksiin sisältyvä ensimmäisen linjan suun kautta annettava tautia muokkaava lääke (DMT) RRMS:lle, tosiasia, jota vahvasti tukevat alla olevat kokeilu- ja kirjallisuustodisteet (mukaan lukien pivot-tutkimukset TEMSO ja TENERE vaiheessa 3 sekä sen käyttö aktiivisena vertailuarvona vähintään viidessä seuraavassa vaihe 3 tutkimuksessa uusia MS-lääkkeitä vastaan).

Tämän vuoksi tämän "ehdokkaan" käytännöllinen tulkinta on vähemmän tieteellinen löytö ja enemmän **markkinoiden rekisteröintikuilu**: terflunomidin mekanistinen ja kliininen todiste RRMS:lle on jo kypsä ja laajasti dokumentoitu; mitä puuttuu, on Suomen-kohtaiset sääntelyä ja turvallisuutta koskevat asiakirjat (katso tietoaukot alla), ei mekanistisen uskottavuuden todiste.

## Kliinisen kokeilun todisteet

| Kokeilunumero | Vaihe | Tila | Rekrytointi | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Vaihe 3 | Valmistunut | 1,088 | Pivot-tutkimus kontrolloitu RCT (TEMSO): terflunomidi vähensi uusiutumistiheyttä ja viivytti vammautumisen kertymistä uusiutuvassa MS:ssä |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Vaihe 3 | Valmistunut | 324 | TENERE: sokkotettu arvioija-vertailu terflunomidista vs interferoni beeta-1a hoidon epäonnistumisaikaan, uusiutumisasteeseen, väsymykseen ja turvallisuuteen |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Vaihe 3 | Valmistunut | 742 | Pitkäaikainen jatkotutkimus EFC6049:lle dokumentoiden pitkäaikaista turvallisuutta/sietokykyä ja tehokkuuden kestävyyttä vammautumisen ja MRI-tulosten osalta |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Vaihe 3 | Valmistunut | 185 | Vertaili ofatumumumabia vs ensimmäisen linjan DMT:tä (mukaan lukien terflunomidi) äskettäin diagnosoidussa uusiutuvassa MS:ssä |
| [NCT07189325](https://clinicaltrials.gov/study/NCT07189325) | Vaihe 3 | Ei vielä rekrytoinnissa | 250 | Anti-CD20 ylläpidon ei-alemmuustutkimus vs de-eskaloinnin strategia RRMS:ssä |
| [NCT06663189](https://clinicaltrials.gov/study/NCT06663189) | Vaihe 3 | Ei vielä rekrytoinnissa | 200 | TWINS: satunnaistettu DMT:ien lopettaminen (mukaan lukien terflunomidi) passiivisissa RRMS-potilaissa ≥55 |
| [NCT00273364](https://clinicaltrials.gov/study/NCT00273364) | Vaihe 2 | Valmistunut | 110 | Hematopoieettisen kantasolujen hoito vs muun hyväksytyn hoidon vertailu inflammatorisessa MS:ssä, joka ei vastaa hoitoon |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Vaihe 2 | Valmistunut | 147 | Jatkotutkimus, joka arvioi terflunomidin pitkäaikaista turvallisuutta ja tehokkuutta uusiutuvassa MS:ssä |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Vaihe 4 | Valmistunut | 12 | Määritti terflunomidin seerumin ja aivo-selkäydinnesteen pitoisuudet 14 mg päivittäisen annoksen ollessa |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Valmistunut | 30 | Mekanistinen tutkimus säätelevistä B-lymfosyyteistä terflunomidin terapeuttisen vaikutuksen välittäjinä |

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | ASCLEPIOS: ofatumumumab vs terflunomidi kasvokkain vertailu uusiutuvassa MS:ssä |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutiinibi (BTK-estäjä) vs terflunomidi uusiutuvassa MS:ssä |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituksimaabi vs terflunomidi uusiutuvassa MS:ssä |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | evolutionRMS1/2: evobrutinibi vs terflunomidi aktiivisen vertailun vaihe 3 tutkimukset |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM: ponesomod vs terflunomidi uusiutuvassa MS:ssä |
| [37691530](https://pubmed.ncbi.nlm.nih.gov/37691530/) | 2023 | RCT (OLE) | Multiple Sclerosis Journal | ALITHIOS avoimen merkinnän jatko: 4 vuoden ofatumumumab vs terflunomidi tehokkuus/turvallisuus |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Katsaus | JAMA | MS:n diagnoosin ja hoidon yleiskatsaus, mukaan lukien tautia muokkaavat hoidot |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Systemaattinen katsaus | Cochrane Database Syst Rev | Immunomodulaattoreiden/immunosuppressiivisten lääkkeiden verkon meta-analyysi RRMS:lle |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Katsaus | Drugs | Kattava katsaus terflunomidin mekanismiin, tehokkuuteen ja turvallisuuteen RRMS:ssä |
| [37382446](https://pubmed.ncbi.nlm.nih.gov/37382446/) | 2023 | Katsaus | Expert Rev Neurotherapeutics | Terflunomidi ensimmäisen linjan suun kautta annettavana hoitona pediatrisessa uusiutuvassa-remissioon muotoisessa MS:ssä |

## Suomen markkinatiedot

Terflunomidi ei ole tällä hetkellä markkinoilla Suomessa — todistuspaketti tallentaa **0 hyväksyntää** ja mitään lisenssi-merkintöjä. Mitään Suomen-kohtaista tuotetta, antomuotoa tai hyväksyttyä indikaatiotekstiä ei ole saatavilla.

## Turvallisuusnäkökohdat

Lue turvallisuustiedot pakkausselosteesta. (Tärkeimmät varoitukset, vasta-aiheet ja lääke-yhdysvaikutustiedot eivät ole saatavilla nykyisessä todistuspaketissa — DDI-kysely ei palauttanut yhtään tietuetta.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidättäydy**

**Perustelut:**
Tehokkuustodisteet ovat poikkeuksellisen vahvat (L1) — kaksi valmistunutta pivot-tutkimusta vaiheessa 3 (TEMSO, TENERE) sekä pitkäaikainen vaihe 3 jatko ja viisi muuta vaihe 3 kasvokkain tutkimusta vahvistavat terflunomidin validoiduksi ensimmäisen linjan RRMS:n hoitojaksoksi muualla. Tämä ehdokas ei kuitenkaan voi edetä turvallisuuden arviointiin: TFDA/Fimea pakkausseloste (varoitukset ja vasta-aiheet) on **(este)** tietoaukko, DDI-tiedot puuttuvat, ja lääkkeellä ei ole nykyisiä hyväksyntöjä tai markkinahistoriaa Suomessa.

**Jatkamiseen vaaditaan seuraavat:**
- TFDA/Fimea pakkausseloste — varoitukset ja vasta-aiheet ((este) tietoaukko, vaaditaan ennen S1 turvallisuuskatselmusta)
- Rakenteinen DrugBank MOA -tietue (Korkea prioriteetti tietoaukko)
- Lääke-lääke-yhdysvaikutustietojoukko (nykyinen kysely ei palauttanut yhtään tuloksia)
- Vahvistus Suomen/EU-sääntelyreitistä ja markkinoille saattamisen aikataulusta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

