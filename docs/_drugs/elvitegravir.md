---
layout: default
title: Elvitegravir
parent: Pelkkä mallin ennuste (L5)
nav_order: 141
evidence_level: L5
indication_count: 3
---

# Elvitegravir
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

# Elvitegravir: HIV-1-infektiosta simiilivirus-infektioon (SIV) (Prekliininen malli)

## Yhdessä lauseessa

> Elvitegravir on HIV-1-integraasi-juostosiirtoinhibiittori (INSTI), joka on alun perin kehitetty osana yhdistelmäantiretroviraalihoitoa HIV-1-infektioon.
> TxGNN-malli ennustaa aktiivisuutta, joka on relevantti **simiilivirus-infektioon (SIV)** — lentivirus, joka on läheisesti sukua HIV-1:lle ja jota käytetään ihmisen ulkopuolisissa primaattien tutkimusmalleissa —
> **0 kliinisen tutkimuksen** ja **7 prekliinisen julkaisun** kanssa, jotka tukevat tätä suuntaa. Kaksi muuta matalan luottamuksen ennustetta (kissanomaisesti hankittu immunovajaatauti ja siihen liittymätön harvinainen neuroevolutionäärinen häiriö) tuotettiin myös TxGNN-mallilla, mutta niillä ei ole tukevaa näyttöä ja niihin käsitellään erikseen alla.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei virallisesti rekisteröity lähdetietojoukossa (`original_indications` on tyhjä ja `original_moa` on tietoaukko). Näytön paketin omien mekanististen kuvausten perusteella elvitegravir on HIV-1-integraasi-juostosiirtoinhibiittori, jota käytetään yhdistelmäantiretroviraalihoitona HIV-1-infektioon. |
| Ennustettu uusi indikaatio | Simiilivirus-infektio (SIV) *(ihmisen ulkopuolinen primaatilentivirus-tutkimismalli, ei ihmisen kliininen indikaatio)* |
| TxGNN-ennusteen pistemäärä | 99,89% |
| Näytön taso | L3 (putkisto-pisteyttämisen mukaan; huomaa, että kaikki tukeva kirjallisuus on prekliinistä/eläinmallia — katso varoitus alla) |
| Suomen markkinatilanne | Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidä |

**Huomio näytön paketin kahdesta muusta TxGNN-ennusteesta:**

| Sijoitus | Ennustettu indikaatio | TxGNN-pistemäärä | Näyttö | Päätös |
|---------|----------------------|-------------|----------|---------|
| 1 | Kissan hankittu immunovajaatautioireyhtymä (FIV) | 99,89% | 0 tutkimusta, 0 kirjallisuutta | Pidä |
| 3 | Neuroevolutionäärinen häiriö, jossa ataaktinen kävely, puheen puuttuminen ja vähentyneellä aivokuoren valkean aineen määrä | 99,87% | 0 tutkimusta, 0 kirjallisuutta | Pidä — todennäköisesti vääriä positiivinen tietoverkko-assosiaatio |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtainen, virallisesti lähteistetty vaikutusmekanismia kuvaava tieto (DrugBank `original_moa`-kenttä) on tällä hetkellä merkitty tietoaukoksi tässä näytön paketissa. Kuitenkin TxGNN-perustelun mukaisesti kuvatun mekanismin perusteella elvitegravir tunnetaan **HIV-1-integraasi-juostosiirtoinhibiittorina (INSTI)**, joka estää virusten cDNA-integraation juostosiirtovaiheessa isäntägenomiin. Se on kehitetty ja markkinoitu osana kiinteässä annoksessa yhdistelmäantiretroviraalihoitoa (esimerkiksi kobitsistaatin, emtrisitabiinin ja tenofoviirian kanssa) HIV-1-infektioon ihmisille.

SIV (simiilivirus) on lentivirus, joka on läheisesti sukua HIV-1:lle, ja SIV/SHIV-infektoidut apinoidut mallit ovat koko antiretroviraali-lääkkeen kehityksen aikana käytetty standardi ihmisen ulkopuolisen primaatin tutkimusmallia — mukaan lukien resistanssiprofilointi ja pre-eksposuuri/post-eksposuuri-profylaksiatutkimukset. Koska HIV-1- ja SIV-integraasit jakavat oleellisen rakenteel lisen ja funktionaalisen homologian, HIV-1:tä vastaan kehitetyt INSTI:t — mukaan lukien elvitegravir itse — on suoraan testattu ja osoitettu säilyttävän antiviraalisen aktiivisuuden SIV:ää vastaan in vitro -malleissa ja eläinmalleissa.

Tärkeää on, että tämä ennustettu "indikaatio" ei ole perinteisessä uudelleenkäytön mielessä uusi ihmisen sairaustavoite — se heijastaa elvitegraviirin vakiintunutta roolia tutkimuskomponenttina/vertailukomponenttina SIV/SHIV ihmisen ulkopuolisen primaatin mallisysteemissä pikemminkin kuin uutta kliinistä populaatiota. Tämä erottaa sen tyypillisestä lääkkeen uudelleenkäyttöskenaariosta (esimerkiksi sydän- ja verisuonisairauksia hoitava lääke uudelleenkäytetty syövän hoitoon) ja sitä pitäisi tulkita validoivaksi mallin biologisen uskottavuuden (oikein tunnistaa HIV-1 ↔ SIV mekanistinen linkki) pikemminkin kuin pinta-äänestävän uutta terapeuttista mahdollisuutta, joka vaatii kliinistä kehitystä.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehtijulkaisu | Keskeiset löydökset |
|------|-----|------|------|---------|
| [17977962](https://pubmed.ncbi.nlm.nih.gov/17977962/) | 2008 | Prekliininen (in vitro -karakterisaatio) | Journal of Virology | Elvitegraviirin (JTK-303/GS-9137) alkuperäinen karakterisaatio: estää HIV-1 cDNA-integraation juostosiirtoinhibitioilla; aktiivinen useita HIV-1-alatyyppejä ja lääkkeille resistentteja isolaatteja vastaan. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Prekliininen (resistanssiprofil ointi, SIV-malli) | Journal of Virology | Vahvistaa, että SIVmac239 on herkkä HIV-1-integraasi-juostosiirtoinhibiitoreille (INSTI), resistanssimutaatiot tuottavat samankaltaisia fenotyyppejä molemmissa viruksissa. |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Prekliininen (resistanssimutaatiotutkimus) | Journal of Virology | HIV-1-integraasi-resistanssimutaatiot (mukaan lukien elvitegraviiri-paineen alaisella valitut) tuodut SIVmac239:ään muuttavat INSTI-herkkyyttä, tukevat lajienvälistä mekanistista relevanssia. |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Prekliininen (eläinmallimetodologia) | Antimicrobial Agents and Chemotherapy | Vahvistaa simiinitrooppisen HIV:n mallia INSTI-lääkkeen resistanssin tutkimukseen, rakentuu SIV/HIV-integraasihomologialle. |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Prekliininen (humanisoidut hiirimals) | Frontiers in Immunology | Kuvaa kaksitarkoitteisen humanisoidun hiiremallin antiviraalisten strategioiden testaamisen kannalta sekä SIV:ää että HIV:tä vastaan. |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Prekliininen (posteksposuuri-profylaksia, ei pelkästään elvitegraviiria) | The Journal of Infectious Diseases | Tenofoviiriksi alakeenamidi/elvitegravir-emätininsertit osoittavat pidennettyjä posteksposuuri-suojaa SHIV:ää vastaan apinoiduilla (93–100% suoja). |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Prekliininen (lääkekluokan analoginen antiviraalinen aktiivisuus) | Antimicrobial Agents and Chemotherapy | Arvioi biktegraaviria/kabotegraviria (myöhemmän sukupolven INSTI:ä) integraasienhibiittorille-resistenttiä SIVmac239:ää ja HIV-1:tä vastaan; viittaa elvitegraviiria vertailu-/edeltäjäyhdisteen osana. |

**Varoitus:** kaikki seitsemän julkaisua ovat prekliinisiä (in vitro, solu-pohjaisia tai ihmisen ulkopuolisia primaatteja/hiiremallia) tutkimuksia. Vain kaksi (PMID 17977962, 38134382) testaavat elvitegraviiriä suoraan; loput tutkivat SIV/INSTI-lääkekluokan biologiaa tai myöhemmän sukupolven analogeja. Ihmisen kliinistä dataa ei ole olemassa tälle soveltamiselle.

---

## Suomen markkinatiedot

Elvitegraviiria ei tällä hetkellä ole hyväksytty Suomeen (0 markkinointihyväksyntää rekisteröity; markkinatilanne: Ei markkinoilla/Ei markkinoilla).

---

## Turvallisuushuomiot

Katso pakkausesite turvallisuustiedoista.

*(Kaikki turvallisuuskentät näytön paketissa — keskeiset varoitukset, vasta-aiheet ja lääke-lääke-vuorovaikutukset — on merkitty tietoaukoiksi. Huomattavasti `DG001` merkitsee TFDA-pakkausesitteen varoituksia/vasta-aiheita **estäväksi** tietoaukoksi, mikä tarkoittaa, että tämä ehdokas ei voi vielä edetä viralliseen S1-turvallisuuskatsaukseen.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
TxGNN-signaali SIV-infektiosta on mekanistisesti uskottava ja tuettu seitsemällä prekliinisellä julkaisulla, mutta se heijastaa elvitegraviirin tunnettua roolia ihmisen ulkopuolisen primaatin tutkimsusmallissa pikemminkin kuin validoitua uutta ihmisen kliinistä indikaatiota — mitään kliinisiä tutkimuksia ei ole, eikä lääkettä ole tällä hetkellä markkinoilla Suomessa. Yhdessä **estävän** tietoaukon kanssa TFDA-turvallisuus-/esite-tiedoissa (DG001), tämä ehdokas ei voi edetä alustavaa tutkimuskatsausta pidemmälle. Kaksi muuta TxGNN-ennustetta tässä paketissa (kissanomaisesti hankittu immunovajaatauti ja siihen liittymätön neuroevolutionäärinen häiriö) eivät ole tuettuja näytöllä ollenkaan ja pitäisi jäädä odottamaan; neuroevolutionäärinen häiriöennuste erityisesti pitäisi käsitellä todennäköisenä tietoverkko-väärä positiivisena, kun otetaan huomioon, ettei ole mitään uskottavaa mekanistista yhteyttä.

**Edistymisen edellytykset:**
- TFDA/sääntelyasiakirja, jossa on varoitukset, vasta-aiheet ja lääke-lääke-vuorovaikutukset (tällä hetkellä estävä aukko DG001)
- Virallisesti DrugBank-lähteinen vaikutusmekanismin (MOA) tieto (tällä hetkellä korkean vakavuuden aukko DG002)
- Translatioisen relevansssin selventäminen: koska SIV-infektio on eläinmallin konstruktio, määritä, mitä ihmisen kliinistä populaatiota (jos mitään) tämän signaalin oletetaan tukevan ennen lisää näytönkeruuta
- Jos SIV-infektioon (FIV) liittyviä signaaleja tavoitellaan eläinlääketieteen soveltamiseksi, tilaa määrätyt in vitro/in vivo FIV-integraasien estävyyden tutkimukset, koska tällaista dataa ei ole olemassa
- Ei muuta toimintaa neuroevolutionäärisen häiriö-ennusteen osalta ilman osoitettavissa olevaa mekanistista perustetta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

