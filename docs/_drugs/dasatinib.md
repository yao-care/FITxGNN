---
layout: default
title: Dasatinib
parent: Kohtalainen näyttö (L3-L4)
nav_order: 112
evidence_level: L3
indication_count: 10
---

# Dasatinib
{: .fs-9 }

Näytön taso: **L3** | Ennustetut käyttöaiheet: **10** kpl
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

# Dasatinibi: Kroonisesta myeloidileukemiasta Ewingin sarkooma

## Yhden lauseen yhteenveto

Dasatinibi on toisen sukupolven tyrosiinikinaasi-inhibiittori, joka on hyväksytty kroonisen myeloidileukemian (CML) ja Philadelphian-kromosomin positiivisen akuutin lymfoblastisen leukemian (Ph+ ALL) hoitoon. TxGNN-mallin pääennuste on, että se saattaa olla tehokas myös **Ewingin sarkooma**ssa, ja siitä on tunnistettu tällä hetkellä **3 kliinistä tutkimusta** ja **9 julkaisua**, vaikka mekanistinen perustelu (SRC/FAK-signalointipolun estäminen) on vahvempi kuin kliininen näyttö, joka pysyy suurelta osin prekliinisenä ja ei-tautikohtaisena.

> **Huomio mallin validoinnista:** TxGNN:n rank-2-ennuste dasatiinille on "myeloidileukemia" — mikä ei ole uusi indikaatio vaan dasatinibin *alkuperäinen*, jo hyväksytty käyttötarkoitus (vahvistettu DASISION-tutkimuksella, PMID 27217448, tässä samassa näyttöpaketissa). Tämä on hyödyllinen järkevyyden tarkistus: malli palauttaa oikein tunnetun todellisen positiivisen tuloksen, mikä antaa epäsuorasti uskottavuutta sen Ewingin sarkooman rankaukselle, mutta ei korvaa tautikohtaista validointia.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Krooninen myeloidileukemia (CML) / Ph+ ALL *(ei ole läsnä Taiwan/Suomen sääntelyaineistossa — lääke ei ole markkinoilla siellä; perustuu globaalisti vahvistettuihin hyväksyttyihin käyttötarkoituksiin, joita tämän näyttöpaketin kirjallisuus tukee)* |
| Ennustettu uusi indikaatio | Ewingin sarkooma |
| TxGNN-ennusteen pistemäärä | 99.90% (rank 1502) |
| Näytön taso | L3 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Hyväksynnän määrä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista toimintamekanismin tietoa ei ole saatavilla (tietoaukko, korkea vakavuus). Tunnetun tiedon perusteella dasatinibi on monikohteinen kinaasi-inhibiittori, joka alun perin kehitettiin BCR-ABL-ohjattujen leukemioiden hoitoon, ja sen teho kroonisessa myeloidileukemiassa ja Ph+ ALL:ssa on hyvin vakiintunut ja mekanistisesti se saattaa olla tehokas myös hematopoieettisten kasvainten ulkopuolella sen aktiivisuuden vuoksi SRC-perhekinaasin, c-KIT:n ja PDGFR-β:n vastaisesti.

Ewingin sarkooma on biologisesti selvästi erillään CML:stä — se on luun/pehmeän kudoksen sarkoomia neuroektodermaalista alkuperää, jota ohjaa EWSR1-FLI1-fuusiogeeni, ei BCR-ABL. Siksi sillä ei ole jaettu sairauden perimää dasatinibin alkuperäisen indikaation kanssa; perustelu sen sijaan perustuu kokonaan jaettuun alasvirran molekyylikohteeseen eikä jaettuun tumorin alkuperään.

Mekanistisesti Ewingin sarkooman solujen invaasiota ja metastaasiota ohjaa vahvasti SRC/FAK-signalointi. Dasatinibi, voimakkaana SRC-perhekinaasin estäjänä, on osoitettu in vitro -kokeissa tukahduttavan migraatiota/invaasiota ja aiheuttavan apoptoosia Ewingin sarkooman solulinjoissa. Tämä on kuitenkin epäsuora mekanistinen yhteys (alavirtaan signaloinnin solmun estäminen) eikä suora osuma taudin ohjaajageeniin, ja yksittäin annettu dasatinibi on aiemmin alitoiminut Phase 2:n korisarja-tutkimuksessa, joka sisälsi Ewingin sarkooman — mikä viittaa siihen, että mahdollinen tulevaisuuden kliininen hyöty vaatisi todennäköisesti yhdistelmästrategioita yksittäisagenttihoidon sijasta.

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tilanne | Osallistujamäärä | Tärkeimmät löydökset |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Lopetettu | 7 | Ewingin sarkooman ja siihen liittyvien kasvainten hoitoon tarkoitettu dasatinibin ja ifosfamidi-, karboplatiini- ja etopositiidiyhdistelmällä toteutettu pediatrinen tutkimus; tutkimus lopetettiin, ja pieni otoskoko (n=7) rajoittaa johtopäätöksien tekemistä merkittävästi. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Valmistunut | 366 | Yksittäisen dasatinibin korisarja-tutkimus edistyneissä sarkoomeissa (vasteen esiintyminen, 6 kuukauden PFS); Ewingin sarkooma oli yksi useista sisällytetyistä alatyypeistä, ei tautispesifinen suunnittelu — Ewingin sarkooman erityisiä alaotostuloksia ei raportoitu täällä. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Rekrytoi | 41 | B7-H3 CAR-T-soluterapiatutkimus (ei dasatinibi) pediatrisissa/nuoren aikuisuuden uusiutuneissa/refraktaarisissa kiinteissä kasvaimissa; päällekkäinen vain sairauspopulaation osalta, ei tutkimuslääkkeen osalta. |

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|-----|------|------|---------|
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Katsaus | Curr Treat Options Oncol | Kondrosarkooman systeemisen hoidon katsaus; sivuava suhteessa Ewingin sarkoomaan, todennäköisesti löydetty sarkoomatyyppien välisen haun päällekkäisyyden kautta. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Katsaus | Oncology Letters | Src-signaloinnin rooli sarkooman biologiassa; tukee Src:ia mahdollisena terapeuttisen kohdeluokkana. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Prekliininen (in vitro) | Cancer Research | Dasatinibi estää migraatiota/invaasiota useissa sarkooman solulinjoissa ja aiheuttaa apoptoosia Src-riippuvaisissa luusarkooman soluissa. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Prekliininen | Sarcoma | Tutkii FAK-Src-kompleksin kohdintamista DSRCT:ssa, Ewingin sarkoomassa ja rabdomyosarkoomassa; huomioidaan, että yksittäinen dasatinibi epäonnistui aiemmin Phase 2 -tutkimuksessa näille alatyypeille, mikä motivoi yhdistelmälähestymistapoja. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Prekliininen (in vitro) | Oncology Reports | Dasatinibi osoittaa antiproliferatiivista ja antimimigratiivista aktiviteettiä neuroblastoomassa ja Ewingin sarkoomassa solulinjoissa, yhdistetty c-KIT/PDGFR-estoon. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Prekliininen | Neoplasia | Tenaskiini C ja Src yhteistoiminnassa ajavat invadopodian muodostumista ja metastaattista invaasiota Ewingin sarkoomassa. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Prekliininen (in vitro) | Neoplasia | Mikro-ympäristön stressi indusoi Src-riippuvaista invadopodian aktivoitumista ja solun migraatiota Ewingin sarkoomassa. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Prekliininen (eri aine: plerixafor) | Cell Commun Signal | CXCR4-antagonisti plerixafor (ei dasatinibi) edistää Ewingin sarkooman proliferaatiota reseptori-tyrosiinikinaasi-signaloinnin kautta; sisällytetty taudin päällekkäiseen hakuun, ei dasatinibi-tutkimus. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Potilastapauskertomus | Case Reports in Oncology | Kuvaa harvinaista kromosomaalipoikkeavuutta CML:n blastikriisissä; ei liity Ewingin sarkoomaan — todennäköisesti hakuvirhe. |

## Sytoktoksisuus

Dasatinibi on antineoplasminen aine (tyrosiinikinaasi-inhibiittoriluokka), joten tämä osio pätee. Huomio: TFDA:n/sääntelyasetuksen pakkausselostetiedot dasatiinille ovat **estävä** tietoaukko tässä näyttöpaketissa (pakkausselosteita ei ole saatavilla), joten alla olevat tiedot perustuvat lääkeluokkaan ja tässä näyttöpaketissa oleviin turvallisuussignaaleihin eikä viralliseen merkintään — ne eivät korvaa merkinnän tarkistamista.

| Kohde | Sisältö |
|------|------|
| Sytoktoksisuuden luokitus | Kohdennettu terapia — toisen sukupolven monikohteinen tyrosiinikinaasi-inhibiittori (BCR-ABL, SRC-perhe, c-KIT, PDGFR-β) |
| Luuydinsuppression riski | Kohtalainen–Korkea — sytopeniat (mukaan lukien trombosytopenia) ovat dasatinibin ja muiden BCR-ABL TKI:iden tunnettu luokkavaikutus (esim. erityinen tutkimus tutki IL-11:ää TKI-liittyvään trombosytopeniaan, NCT00493181); säännöllinen hematologlinen seuranta on perusteltua |
| Pahoinvointiherkkyyden luokitus | Matala (suun kautta annettava kohdennettu terapia, ei tavanomainen sytotoksinen kemikaali) |
| Seuranta-asiat | Täydellinen verenkuva erottelulla, maksan toiminta ja keuhko-/pleurastatukselle — tämän näyttöpaketin kirjallisuus dokumentoi dasatinibiin liittyvää pleuraefuusiota/kylotraksea ja interstiisin pneumoniittia luokkarelevantteina haittavaikutuksina |
| Käsittelysuoja | Suun kautta otettava vaarallinen/antineoplasminen aine — laitoksen vaarallisten lääkkeiden käsittelystandardit pätevät; virallinen TFDA-merkinnän varoitus on vireillä (estävä tietoaukko) |

## Turvallisuusnäkökulmat

Ole hyvä ja katso pakkausselosteesta turvallisuustiedot. TFDA:n merkinnän varoitukset, kontraindikaatiot ja lääkeaineiden väliset vuorovaikutusdata eivät ole saatavilla (Estävä tietoaukko — DG001), joten yhtään strukturoitua turvallisuustietoa tästä näyttöpaketista ei voida siteerata täällä.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Mekanistinen perustelu (SRC/FAK-signalointipolkuriippuvuus Ewingin sarkoomassa) on uskottava, mutta kliininen tuki on heikko — ainoa merkityksellisen ilmoittautumismäärän omaava tautispesifinen tutkimus (NCT00464620) on ei-tautispesifinen sarcoma-korisarja-tutkimus, ja ainoa Ewingin sarkooman-kohdistettu tutkimus lopetettiin n=7:llä. Yhdessä estävän tietoaukon kanssa TFDA:n turvallisuus/merkintätiedoista (mikä estää jopa alkuperäisen S1-turvallisuusarvioinnin) ja lääkkeen ollessa markkinoimatta Suomessa, tälle ei ole riittävää perustaa jatkaa tällä hetkellä.

**Jatkamista varten tarvitaan seuraavat asiat:**
- TFDA:n/sääntelyasetuksen pakkausseloste (varoitukset, kontraindikaatiot, DDI) estävän turvallisuusaukon ratkaisemiseksi
- Vahvistettu toimintamekanismidata DrugBankista
- Ewingin sarkooman-spesifeistä alaotostulokset NCT00464620:stä (valmistunut Phase 2 -korisarja-tutkimus)
- Kaikki päivitetyt yhdistelmähoitotutkimukset, koska yksittäinen dasatinibi on aiemmin alitoiminut sarkoomatutkimuksissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

