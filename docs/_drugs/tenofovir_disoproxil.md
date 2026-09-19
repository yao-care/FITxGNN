---
layout: default
title: Tenofovir Disoproxil
parent: Pelkkä mallin ennuste (L5)
nav_order: 368
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Tenofovir disoproxil: HIV-infektiosta simiaanin immunodefisienssi-viruksen infektioon

## Yhden lauseen yhteenveto

> Tenofovir disoproxil on nukleotidi-käänteiskopioinnin estäjä, jonka vakiintunut käyttö — viitattuna tämän todistepaketin omassa kirjallisuudessa (iPrEx-tutkimus, PMID 20874040) — on HIV:n altistumisen estolääkitys ja hoito.
> TxGNN-mallin parhaiten sijoittuva ennustus on **simiaanin immunodefisienssi-viruksen (SIV) infektio**, ei-ihmisillä primaateilla esiintyvä tauti eikä ihmisen indikaatio, johon liittyy **2 kliinistä tutkimusta** ja **20 julkaisua**, joista useimmat ovat makakkien/eläinmallin tutkimuksia.
> Ottaen huomioon ennustuksen ei-inhimillisen luonteen ja useat estävät tietokuilut, tämä kandidaatti on **tällä hetkellä kelpaamaton** ihmisten lääkkeiden uudelleenkäyttöön.

---

## Nopea katsaus

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei saatavilla — ei lisenssi- tai indikaatiotekstiä Suomelle; lääkkeen jo hyväksytty ihmisen käyttö (HIV-infektio/PrEP) on päätelty vain toimitetun kirjallisuuden kontekstista, ei `taiwan_regulatory`:sta |
| Ennustettu uusi indikaatio | Simiaanin immunodefisienssi-viruksen infektio *(ei-ihmisillä primaateilla esiintyvä tauti — ei ihmisen indikaatio)* |
| TxGNN-ennustusten pistemäärä | 99.95% |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Hold |

---

## Miksi tämä ennustus on järkevä?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla (`original_moa: [Data Gap]`). Tämän todistepaketin kontekstin perusteella tenofovir disoproxil on tenofovirin (PMPA) suun kautta otettava prekursori, nukleotidi-analogin käänteiskopioinnin estäjä. Sen toimitetussa uudelleenkäytön perustelusta todetaan, että ainoa ihmisen RCT-luokan kirjallisuus tässä paketissa (PMID 20874040, iPrEx-altistumisen estolääkitystutkimus) arvioi itse asiassa tenofovirin **jo hyväksyttyä** käyttöä ihmisen HIV-infektiota ehkäisevässä hoidossa — ei uutta indikaatiota.

Mekanistisesti tenofovirin antiretroviraali-aktiivisuus HIV:n käänteiskopioinnin estäjää vastaan on suoraan analoginen sen aktiivisuuteen makakkien SIV-käänteiskopioinnin estäjää vastaan, koska SIV ja HIV ovat läheisesti toisiinsa liittyviä lentiviruksia. Tämä selittää erittäin korkean TxGNN-pistemäärän. Kuitenkin **SIV-infektio on ei-ihmisillä primaateilla esiintyvä tauti, jota käytetään laboratoriomallina HIV-tutkimukseen — se ei ole ihmisen diagnoosi**, joten tämä ennustus ei edusta todellista uutta ihmisen indikaatiota; se heijastaa mallin oikeaoppista tenofovirin klusterointia lentivirukseen liittyväten tautimerkkien kanssa sen tietokaavion sisällä, joista useat sattuvat olemaan eläintautien ontologiaehtoja.

Paketin seuraavat kolme sijoiteltua kandidaattia vahvistavat tätä kuviota pikemminkin kuin kompensoivat sitä: sijoitus 2 ("feline acquired immunodeficiency syndrome") on kissojen eläinlääketieteellinen tauti; sijoitus 3 (harvinainen neurokehityshäiriö) ei ole tukenut mitään näyttöä ja sillä ei ole uskottavaa mekanistista yhteyttä antiviraalisen NRTI:n kanssa; ja sijoitus 4 ("obsolete familial combined hyperlipidemia") on merkitty omassa taudilabelissaan vanhentuneeksi ontologiatermin sekä vain epäsuoraksi, ei-mekanistisella kirjallisuuden tuella. Kaikki neljä saivat "Hold" -suosituksen lähdelaskennassa.

---

## Kliiniset tutkimukset

| Tutkimuksen numero | Vaihe | Tila | Osallistujat | Keskeiset tulokset |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Peruutettu | 0 | Tutki HIV/SIV-viraalin hajoamiskineetikkaa raltegraviirilla (integraasi-inhibiittorin, ei tenofoviriini); tutkimus oli peruutettu ilman osallistujia. Matala relevanssi (Grade C) — eri lääke, ei varsinaisia SIV-potilaita. |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Vaihe 1/2 | Tuntematon | 12 | Arvioi vedolizumaabia yhdessä antiretroviraali-hoidon kanssa HIV-virologisen remission saavuttamiseksi hoitoon naiiville ihmispotilaille; tenofovir ei ollut pääasiallinen interventio ja tutkimuspopulaatio oli ihminen HIV, ei SIV. Matala relevanssi (Grade C). |

*Huomautus: molemmat tutkimukset merkittiin matalan relevanssin (Grade C) oleviksi lähdetodistepaketin toimesta — kumpikaan ei testaa suoraan tenofovir disoproxilia vastaan SIV-infektiota.*

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT (ihminen) | Pharmacotherapy | Käsittelee HIV:n systeemistä altistumisen estolääkitystä (PrEP) ihmisillä — tämä on tenofovirin vakiintunut käyttö, ei uutta SIV-indikaatiota; tautimerkin epäsuhta merkitty lähteen perusteluissa. |
| [14557287](https://pubmed.ncbi.nlm.nih.gov/14557287/) | 2003 | Katsaus | Clinical Microbiology Reviews | Käsittelee asyklisen nukleosidi-fosfonaattien (sidofovir, adefovir, tenofovir) kliinistä potentiaalia DNA-viruksia ja retroviruksia vastaan, mukaan lukien SIV-mallit. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Eläintutkimus (makakki) | J Infect Dis | Suun kautta otettava tenofovir alafenamidi + emtricitabiini suojasi makakkeja peräsuolen SHIV-infektiolta (PrEP-malli). |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Eläintutkimus (makakki) | JCI Insight | Hypo-osmolaarinen peräsuolen tenofovir-suihkemuoto esti SHIV:n hankkimisen makakkeissa. |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Eläintutkimus (nuori makakki) | J Acquir Immune Defic Syndr | Suun kautta otettava tenofovir DF ja paikallinen tenofovir GS-7340 suojasivat nuoria makakkeja toistuvaa suun kautta tapahtuvaa SIV-altistusta vastaan (pediatrinen siirtymämalli). |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Eläintutkimus (makakki) | J Infect Dis | Tenofovir DF kemoprofylaksia antoi osittaista suojaa SHIV-infektiota vastaan useiden viraalisten haasteiden alaisena. |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Eläintutkimus (makakki) | J Virol | Vaginaalinen tenofovir-geeli antoi kestävää suojaa SHIV-infektiota vastaan makakkeissa, korreloiden kudoksen lääkkeen tasojen kanssa. |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Eläintutkimus (makakki) | J Infect Dis | Emtricitabiini/tenofovir DF esti vaginaalista SHIV-infektiota makakkeissa, jotka olivat ko-infektioita Chlamydia ja Trichomonas kanssa. |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Eläintutkimus (makakki) | J Infect Dis | Tenofovir alafenamidi/elvitegravir-vaginaaliinsertit antoivat pidennettyä altistumisen jälkeistä suojaa SHIV:ta vastaan makakkeissa. |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Eläintutkimus (makakki) | J Infect Dis | Emtricitabiini/tenofovir DF esti tenofovir-resistentin (K65R) SHIV-kannan siirtymistä makakkeissa. |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Luonnollinen historia (Afrikan vihreä makakki) | J Virol | Karakterisoi SIVagm-viraalin dynamiikkaa tenofovir/emtricitabiin-hoidon alaisena luonnollisen isännän, ei-edistyvässä apinaperikunnassa. |

*10 lisä-PMID:a lähdepaketissa (esim. 41959211, 14963139, 20497048) ovat luokittelemattomia ("pending" tutkimustyyppi) eikä niitä priorisoitu tässä.*

---

## Suomen markkinatiedot

Ei sovellettavissa — TENOFOVIR DISOPROXIL:lla on tällä hetkellä **0 markkinointilupia** Suomelle (`market_status: Not marketed`). Tuote/annostelu/indikaatiotietoa ei ole saatavilla.

---

## Turvallisuusarviot

Katso turvallisuustietoja pakkausselosteesta. *(Kaikki turvallisuuskentät todistepakettissa — keskeiset varoitukset, vasta-aiheet ja lääkkeiden välisten vuorovaikutusten kysely — ovat tietokuiluja; TFDA/Fimea-pakkausselosteen varoitukset on merkitty **Blocking**-vakavuuden kuiluksi (DG001), joka on ratkaistava ennen S1-turvallisuusarvioiden tekemistä.)*

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Hold**

**Perustelut:**
- Korkeimpaan sijoitettu ennustettu indikaatio (SIV-infektio) on ei-ihmisillä primaateilla esiintyvä taudin malli, ei ihmisen indikaatio, jota voitaisiin tavoitella uudelleenkäytön polun kautta; sijoitukset 2–4 ovat vastaavasti kelpaamattomia (eläinlääketieteellinen tauti, vanhentunut ontologiatermi, tai nolla näyttö). Kaikki neljä kandidaattia sisältävät lähteestä määritetyn "Hold" -suosituksen.
- Kaksi Blocking/High-vakavuuden tietokuilua jää avoimeksi: TFDA/Fimea-pakkausselosteen varoitukset ja vasta-aiheet (Blocking — estää S1-turvallisuusarvion), ja vahvistettu vaikutusmekanismi (High).

**Jatkamiseksi tarvitaan seuraavat:**
- Ratkaisu DG001 (TFDA/Fimea-pakkausselosteen varoitukset/vasta-aiheet) ennen kuin jokin turvallisuusvaiheen arvio voi alkaa
- Ratkaisu DG002 (vahvistettu MOA DrugBankin kautta) mekanistisen relevanssin asianmukaiseksi arvioinniksi
- Uudelleen suorittaa TxGNN-taudinsovitus ihmisen-ainoilla tautien ontologian suodattimella eläinmalli- ja vanhentuneisiin tautimerkkeihin kandidaatin sijoituksesta
- Jos todellinen ihmisen indikaatio on toivottu, hankkia lisäennustettuja kandidaatteja nykyisten 4 parhaan ulkopuolella, koska mikään heistä ei ole tällä hetkellä kelvollinen

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

