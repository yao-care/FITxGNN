---
layout: default
title: Panobinostat
parent: Pelkkä mallin ennuste (L5)
nav_order: 329
evidence_level: L5
indication_count: 1
---

# Panobinostat
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

# Panobinostaatti: multippelin myelooman hoidosta myeloidileukemiaan

## Yhteenveto

Panobinostaatti on histonideasetylaasin (HDAC) estäjä, jota on alun perin käytetty multippelin myelooman hoitoon.
TxGNN-malli ennustaa sen voivan tehota **myeloidileukemiaan**.
Suuntaa tukee tällä hetkellä **16 kliinistä tutkimusta** ja **20 julkaisua**. Näyttö koostuu pääosin varhaisen vaiheen tutkimuksista ja prekliinisistä töistä.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Multippeli myelooma |
| Ennustettu uusi käyttöaihe | Myeloidileukemia |
| TxGNN-ennustepisteet | 99,70 % |
| Näytön taso | L1 (muodollisesti; ks. huomautus alla) |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (pidätetään) |

*Huomautus näytön tasosta:* L1 perustuu yhteen Phase 3 -tutkimukseen (NCT04326764). Se päättyi ennenaikaisesti vain 52 potilaan jälkeen, joten se ei täytä L1-kriteeriä "vähintään kaksi valmistunutta Phase 3 -satunnaistettua tutkimusta". Käytännössä näyttö on heikompaa, noin L2–L3.

---

## Miksi ennuste on perusteltu?

Tämän lääkkeen vaikutusmekanismitiedot eivät ole saatavilla kokoamassamme aineistossa. Seuraava päättely perustuu lääkeryhmän yleisesti tunnettuihin ominaisuuksiin. Panobinostaatti on pan-HDAC-estäjä. Myeloidisissa leukemioissa (AML, MDS, CML) epigeneettinen vaimentuminen ja onkogeenisten fuusioproteiinien rekrytoimat HDAC-entsyymit estävät solujen erilaistumista. HDAC:n esto palauttaa histonien asetylaation, aktivoi uudelleen kasvaimenestäjägeenejä sekä edistää erilaistumista ja apoptoosia.

Sekä multippeli myelooma että myeloidileukemia ovat veren ja luuytimen pahanlaatuisia sairauksia, joissa epigeneettinen säätely on häiriintynyt. Lääkkeen teho myeloomassa osoittaa sen vaikuttavan hematologisiin syöpäsoluihin. Mekanismi voi siksi soveltua myös myeloidileukemiaan.

Lisäksi panobinostaatilla voi olla yhteisvaikutuksia hypometyloivien aineiden (atsasitidiini), solunsalpaajien (idarubisiini/sytarabiini, fludarabiini/sytarabiini) ja tyrosiinikinaasi-inhibiittorien (imatinibi) kanssa. Prekliiniset työt viittaavat myös immuunivälitteiseen erilaistumisvaikutukseen plasmasytoidisten dendriittisolujen aktivaation ja IFNAR-signaloinnin kautta. Erittäin korkea TxGNN-pistemäärä (0,997) on yhdenmukainen tämän kanssa, mutta ei korvaa kliinistä näyttöä.

---

## Kliininen tutkimusnäyttö

Alla on tärkeimmät tutkimukset 16:sta löydetystä.

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04326764](https://clinicaltrials.gov/study/NCT04326764) | Phase 3 | Päättynyt ennenaikaisesti | 52 | Panobinostaatti-ylläpitohoito ja luovuttajan lymfosyyti-infuusiot vs. pelkät infuusiot suuren riskin AML/MDS-potilailla kantasolusiirron jälkeen; todennäköisesti alitehoinen |
| [NCT00946647](https://clinicaltrials.gov/study/NCT00946647) | Phase 1/2 | Valmistunut | 113 | Suun kautta otettava panobinostaatti + atsasitidiini vs. pelkkä atsasitidiini MDS-, CMML- ja AML-potilailla |
| [NCT00880269](https://clinicaltrials.gov/study/NCT00880269) | Phase 2 | Valmistunut | 59 | Panobinostaatti yksinään refraktaarisessa AML:ssä |
| [NCT01055483](https://clinicaltrials.gov/study/NCT01055483) | Phase 1 | Valmistunut | 59 | Panobinostaatti + sytarabiini + mitoksantroni uusiutuneessa tai refraktaarisessa AML:ssä |
| [NCT00691938](https://clinicaltrials.gov/study/NCT00691938) | Phase 1/2 | Valmistunut | 52 | Panobinostaatti + desitabiini ≥ 60-vuotiailla suuren riskin MDS/AML-potilailla |
| [NCT01242774](https://clinicaltrials.gov/study/NCT01242774) | Phase 1 | Valmistunut | 46 | Panobinostaatti + idarubisiini ja sytarabiini AML:n induktiohoidossa; turvallisuus ja siedettävyys |
| [NCT00840346](https://clinicaltrials.gov/study/NCT00840346) | Phase 1/2 | Valmistunut | 46 | Panobinostaatti + idarubisiini ja sytarabiini ≥ 65-vuotiailla uusilla AML-potilailla |
| [NCT01451268](https://clinicaltrials.gov/study/NCT01451268) | Phase 1/2 | Tila tuntematon | 62 | Panobinostaatti-ylläpito kantasolusiirron jälkeen (PANOBEST) |
| [NCT01463046](https://clinicaltrials.gov/study/NCT01463046) | Phase 1 | Valmistunut | 29 | Annoksen määritys yhdessä sytarabiinin ja daunorubisiinin kanssa iäkkäillä AML-potilailla |
| [NCT01321346](https://clinicaltrials.gov/study/NCT01321346) | Phase 1 | Valmistunut | 30 | Annoksen määritys lapsilla, joilla on refraktaarisia hematologisia syöpiä |

Muita tutkimuksia ovat muun muassa panobinostaatti + imatinibi CML:ssä (NCT00686218), pediatrinen AML/MDS (NCT02676323), CML:n kiihtynyt vaihe ja blastivaihe (NCT00449761) sekä kroonisen vaiheen CML (NCT00451035). Nämä tutkimukset olivat pieniä tai päättyivät ennenaikaisesti.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [24413064](https://pubmed.ncbi.nlm.nih.gov/24413064/) | 2014 | Kliininen Phase Ib/II -tutkimus | Blood Cancer J | Panobinostaatti + atsasitidiini 39 potilaalla (AML 29, MDS 10); maksimaalisesti siedetty annos ja alustava teho |
| [32809242](https://pubmed.ncbi.nlm.nih.gov/32809242/) | 2020 | Kliininen tutkimus | Cancer | Turvallisuus, farmakokinetiikka ja farmakodynamiikka lapsilla ja nuorilla aikuisilla, joilla on uusiutunut AML |
| [27485472](https://pubmed.ncbi.nlm.nih.gov/27485472/) | 2016 | Katsaus | Expert Opin Investig Drugs | Panobinostaatti akuutin myeloidileukemian hoidossa |
| [23826641](https://pubmed.ncbi.nlm.nih.gov/23826641/) | 2013 | Katsaus | Expert Opin Investig Drugs | Panobinostaatti lymfoidisissa ja myeloidisissa pahanlaatuisissa kasvaimissa |
| [31739588](https://pubmed.ncbi.nlm.nih.gov/31739588/) | 2019 | Katsaus | Cancers | HDAC-estäjät akuutissa myeloidileukemiassa |
| [38965693](https://pubmed.ncbi.nlm.nih.gov/38965693/) | 2024 | Hoitosuositus | Pediatr Blood Cancer | Uusiutuneen/refraktaarisen Down-oireyhtymään liittyvän myeloidileukemian hoito; atsasitidiini ± panobinostaatti yhtenä vaihtoehtona (ei panobinostaattispesifinen) |
| [35311997](https://pubmed.ncbi.nlm.nih.gov/35311997/) | 2022 | Prekliininen (mekanistinen) | Cancer Discov | Panobinostaatin AML-solujen erilaistumisvaikutus edellyttää plasmasytoidisten dendriittisolujen aktivaatiota ja IFNAR-signalointia |
| [25612941](https://pubmed.ncbi.nlm.nih.gov/25612941/) | 2015 | Prekliininen | Leuk Res | Panobinostaatti + marizomibi AML- ja bortetsomibiresistenteissä malleissa |
| [27725868](https://pubmed.ncbi.nlm.nih.gov/27725868/) | 2016 | Prekliininen | Am J Transl Res | Synergistinen vaikutus ABT-199:n (venetoklaksi) kanssa AML-soluissa ex vivo |
| [26529495](https://pubmed.ncbi.nlm.nih.gov/26529495/) | 2015 | Prekliininen | Cancer Biol Ther | Synergia MK-1775:n (Wee1-estäjä) kanssa AML-soluissa |

---

## Myyntiluvat Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/003725 | Farydak (peruutettu) | – | Multippeli myelooma |

---

## Solunsalpaajaominaisuudet

| Kohta | Sisältö |
|------|------|
| Luokitus | Kohdennettu hoito / epigeneettinen lääke (pan-HDAC-estäjä) |
| Luuydinsuppression riski | Tämän hoitoryhmän lääkkeillä luuydinsuppressio on tavallinen; tarkemmat tiedot on tarkistettava valmisteyhteenvedosta |
| Pahoinvointia aiheuttava vaikutus | Valmisteyhteenvedon mukaan |
| Seurantakohteet | Verenkuva (erittelylaskenta), maksa- ja munuaisarvot, elektrolyytit |
| Käsittelysuojaus | Noudatettava solunsalpaajien käsittelyä koskevia ohjeita |

Tarkemmat tiedot on tarkistettava valmisteyhteenvedon varoituksista ja käyttöön liittyvistä varotoimista.

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Yhteisvaikutuksia on kirjattu yhteensä 527. Esimerkkejä:

- **Merkittävät (Major):** asetyylisalisyylihappo, klaritromysiini, levofloksasiini, dolasetroni, palonosetroni, eliglustaatti, pikosulfaatti, polyeteeniglykoli (3350, elektrolyyttien kanssa), natriumsulfaatti
- **Kohtalaiset (Moderate):** famotidiini, loperamidi, aprepitantti, deksametasoni, bisakodyyli, simetidiini, naltreksoni, metoklopramidi, metreleptiini, mikonatsoli
- **Lievät (Minor):** metronidatsoli

Useat merkittävistä yhteisvaikutuksista koskevat lääkkeitä, jotka voivat vaikuttaa sydämen QT-aikaan tai joita käytetään syöpähoidon oheislääkityksenä (pahoinvointilääkkeet, suolen tyhjennysvalmisteet). Käyttöä suunniteltaessa on tarkistettava potilaan koko lääkitys.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (pidätetään)**

**Perustelut:**
- Mekanistinen peruste on uskottava ja varhaisen vaiheen tutkimuksia on paljon, mutta ainoa Phase 3 -tutkimus päättyi ennenaikaisesti 52 potilaan jälkeen, eikä sen tuloksia ole vahvistettu. Lisäksi lääkevalmisteen myyntiluvat Suomessa on peruutettu, mikä vaikeuttaa saatavuutta.
- Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat, joten turvallisuusarviointia ei voida viedä eteenpäin.

**Jatkaminen edellyttää:**
- NCT04326764-tutkimuksen tulosten hankkimista ja arviointia
- Valmisteyhteenvedon (varoitukset ja vasta-aiheet) hankkimista Fimean sivustolta
- Vaikutusmekanismitietojen täydentämistä DrugBankista
- Selvitystä lääkkeen saatavuudesta Suomessa, koska myyntiluvat on peruutettu
- Arviota siitä, mitkä yhdistelmähoidot (esim. atsasitidiini) ovat lupaavimpia, sekä yhteisvaikutusten (erityisesti QT-aikaan vaikuttavien lääkkeiden) hallintasuunnitelmaa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

