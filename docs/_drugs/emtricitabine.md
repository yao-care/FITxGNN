---
layout: default
title: Emtricitabine
parent: Kohtalainen näyttö (L3-L4)
nav_order: 144
evidence_level: L4
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **3** kpl
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

# Emtricitabiini: HIV-1-infektioiden hoidosta kissahivenloisen immunovajaatekisuuden hoitoon

## Yksirivinen yhteenveto

> Emtricitabiini on kytidiinin analogisti-NRTI, jota käytetään kliinisesti HIV-1-antiretroviraalihoitojärjestelmien osana (esim. Truvada, Atripla). Tämä on dokumentoitu tämän paketin kliinisten tutkimusten ja kirjallisuusälyjen tietueissa.
> TxGNN-mallin korkeimmalla sijalla oleva ennuste on **Kissahivenloinen Hankittu Immunovajaatekisuuden Oireyhtymä (FIV)**, jossa on **4 kliinistä tutkimusta** ja **1 julkaisu** löydetty —
> kuitenkin tämä signaali on **laji-/ontologia-epäsovinnaisuus** (eläinlääketieteen indikaatio, ei ihmisen lääkkeen uudelleenkäytön mahdollisuus) eikä sitä pitäisi toteuttaa sellaisenaan.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | *Ei täytetty jäsennellyissä kentissä (`original_indications` ja `original_moa` ovat tietoaukkojen aiheita)*. Tämän paketin kliinisten tutkimusten ja kirjallisuuden tekstiin perustuen emtricitabiini käytetään osana antiretroviraalihoitoa **HIV-1-infektioon** (esim. Truvada, Atripla) |
| Ennustettu uusi indikaatio | Kissahivenloinen Hankittu Immunovajaatekisuuden Oireyhtymä (FIV) |
| TxGNN-ennustuspistemäärä | 99.92% |
| Näyttötaso | L4 |
| Suomen markkinatieto | ✗ Ei kaupallinen |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidätä** |

---

## Miksi tämä ennuste on järkevä?

Emtricitabiinin yksityiskohtaiset vaikutusmekanismin tiedot eivät ole saatavilla tässä paketissa (`original_moa: [Data Gap]`). Perustuen tietoihin, jotka on upotettu kliinisiin tutkimuksiin ja kirjallisuusälyihin itseensä, emtricitabiini on sytiidiinin nukleosidi-analogisti käänteistranskriptaasin inhibiittori (NRTI), jota käytetään osana yhdistelmäantiretroviraalihoitojärjestelmiä (yhdessä tenofovirin kanssa ja muiden aineiden kanssa, esim. Truvada, Atripla) HIV-1-infektioiden hoitoon ja ehkäisyyn ihmisillä.

TxGNN-mallin ranking 1 -ennuste — Kissahivenloisen immunovajaatekisuuden viruksen (FIV) infektio — on mekanistisesti uskottava hyvin abstraktilla tasolla: FIV, kuten HIV, on lentivirus, joka riippuu käänteistranskriptaasista replikointiin, joten RT-inhibiittorin olisi periaatteessa voitava vaikuttaa molempiin. Kuitenkin tämä **ei ole pätevä ihmisen lääkkeen uudelleenkäytön signaali**. FIV on *eläinlääketieteen* tauti-entiteetti kissoissa, ja farmakokinetiikka, annostus ja myrkyllisyysprofiili eroavat merkittävästi lajien välillä. Paketin oma `repurposing_rationale` sanoo eksplisiittisesti, että se "ei kuulu ihmisen lääkkeen uudelleenkäytön (human drug repurposing) piiriin". Korkea TxGNN-pistemäärä täällä heijastaa todennäköisesti tietokaavioyksikön/upotuksen samankaltaisuutta FIV- ja HIV-solmujen välillä eikä aito uusi ihmisen terapiamahdollisuus.

Tästä syystä alla olevat kliiniset tutkimukset ovat kaikki ihmisen HIV-1-tutkimuksia, jotka sattuivat viittaamaan emtricitabiini-sisältäviin hoitojärjestelmiin — ne **eivät ole näyttöä FIV-indikaatiolle itselleen**, ja jokainen on arvioitu "C" (alhainen relevanssi / entiteetin epäsovinnaisuus) lähde-evidenssipipeline-puolesta.

---

## Kliinisen tutkimuksen näyttö

| Tutkimuksen numero | Vaihe | Tila | Osallistujat | Tärkeimmät tulokset |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Vaihe 3 | Valmis | 844 | Dolutegravir + Abakavir/Lamivudiini vs. Atripla (Efavirenitsi/Emtricitabiini/Tenofovir) ART-naiiveissa HIV-1-aikuisissa. Ihmisen tutkimus; **Arvio C — laji-/entiteetin epäsovinnaisuus FIV:n kanssa** |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Vaihe 2 | Valmis | 208 | Dolutegravirin annoksen valinta-tutkimus + Abakavir/Lamivudiini tai Tenofovir/Emtricitabiini ART-naiiveissa HIV-1-aikuisissa. **Arvio C — epäsovinnaisuus** |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Vaihe 4 | Valmis | 145 | Vahvistettu Darunavir + Lamivudiini vs. Darunavir + Emtricitabiini/Tenofovir tai Lamivudiini/Tenofovir naiiveissa HIV-1-potilaissa. **Arvio C — epäsovinnaisuus** |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Vaihe 3 | Valmis | 828 | Dolutegravir vs. Raltegravir, molemmat kaksinkertaisella NRTI-selkärankareilla (sisältäen Emtricitabiini/Tenofovir), ART-naiiveissa HIV-1-aikuisissa. **Arvio C — epäsovinnaisuus** |

*Kaikki neljä tutkimusta ovat ihmisen HIV-1-tutkimuksia; mikään ei arvioi FIV/kissaindikatiota suoraan.*

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät tulokset |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Eläinkohortti/Katsaus (Taso 3) | Viruses | Yhdistelmäantiretroviraalihoito (Dolutegravir + Tenofovir + Emtricitabiini) arvioitiin farmakokinetiikalla ja kliinisilla tuloksilla FIV-infektoituneissa kissoissa; voimakasta hoitoa FIV:lle ei tällä hetkellä ole. |

---

## Suomen markkina-tieto

Emtricitabiinin markkinointilupaa ei ole tässä evidenssipaketissa (`total_licenses = 0`, `market_status = Not marketed / Ei kaupallinen`). Suomalaisista tuote-/lisenssi-tiedoista ei ole tällä hetkellä tiivistettävää.

---

## Lisäennustetut signaalit tässä evidenssipaketissa (Lisätieto)

Tämä ehdokaspaketti (`TW-DB00879-multi`) sisältää kaksi muuta TxGNN-ennustusta, jotka kannattaa esille tuoda täydellisyyden vuoksi, koska ne merkittävästi muuttavat kokonaisehdokkaan tulkintaa:

### Ranking 2 — Apinan immunovajaatekisuuden virus (SIV) -infektio
TxGNN-pistemäärä 99.92% (ranking 1108) · Näyttötaso **L2** · Suositus: **Tutkimuskysymys**

Tämä on paketin vahvimman näytön signaali (2 kliinistä tutkimusta, 20 julkaisua), mutta perustelut selventävät, että se **ei ole uusi indikaatio** — se edustaa ei-ihmisen primaatin (makaakin) esikliinistä mallitietoa, joka historiallisesti tuki emtricitabiini/tenofovirin (Truvada) jo hyväksyttyä ihmisen PrEP-indikatiota eikä uutta terapiasuuntaa.

| Tutkimuksen numero | Vaihe | Tila | Osallistujat | Tärkeimmät tulokset |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Peruutettu | 0 | HIV-hajoamiskinetiiikan tutkimus (Raltegravir); viitattiin SIV-hajoamisvertailuihin makaakinissa. Arvio C — peruutettu/laji-epäsovinnaisuus. |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Vaihe 1/2 | Tuntematon | 12 | Vedolitsumabi + ART HIV-virologiselle remissioon; ihmisen tutkimus, ei SIV. Arvio C — epäsovinnaisuus. |

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät tulokset |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Katsaus | Pharmacotherapy | Yleiskatsaus systeemiseen PrEP:iin HIV-ehkäisyä varten. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Kohortti (ei-ihmisen primaatin esikliininen) | J Infect Dis | Suun kautta annettu Emtricitabiini + Tenofovir alafenamidi suojaa makaakineja peräsuolen SHIV-infektiosta. |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Kohortti (ei-ihmisen primaatin esikliininen) | J Infect Dis | Emtricitabiini/Tenofovir DF estää tenofovir-resistenttiä (K65R) SHIV-tartuntaa makaakinissa. |
| [32128569](https://pubmed.ncbi.nlm.nih.gov/32128569/) | 2020 | Kohortti (ei-ihmisen primaatin esikliininen) | J Infect Dis | Pitkävaikutteinen Kabotegravir vs. suun kautta annettu Emtricitabiini/Tenofovir DF peniaalista SHIV-altistusta vastaan makaakinissa. |
| [19656878](https://pubmed.ncbi.nlm.nih.gov/19656878/) | 2009 | Kohortti (ei-ihmisen primaatin esikliininen) | J Virol | Paikallinen tenofovir ± Emtricitabiini-geeli suojaa täydellisesti makaakineja toistuvasta emätinperäisestä SHIV-altistuksesta. |
| [21632769](https://pubmed.ncbi.nlm.nih.gov/21632769/) | 2011 | Kohortti (ei-ihmisen primaatin esikliininen) | J Virol | Satunnainen Truvada-profylaksi suojaa emtricitabiini-resistenttiä (M184V) SHIV-peräsuolen tartuntaa vastaan. |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Kohortti (ei-ihmisen primaatin esikliininen) | J Infect Dis | Emätinperäinen Emtricitabiini/Tenofovir-geeli suojaa toistuvaa peräsuolen SHIV-altistusta vastaan makaakinissa. |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Kohortti (ei-ihmisen primaatin esikliininen) | J Infect Dis | Suun kautta annettu Tenofovir alafenamid/Emtricitabiini vs. TAF-yksin emätinperäistä SHIV-infektiota vastaan makaakinissa. |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Kohortti (ei-ihmisen primaatin esikliininen) | AIDS Res Hum Retroviruses | HIV VLP -rokote + osittainen suun kautta annettu PrEP estää SHIV-infektiota ja kehittää immuniteettia makaakinissa. |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Kohortti (ei-ihmisen primaatin esikliininen) | J Infect Dis | Emtricitabiini/Tenofovir DF estää emätinperäistä SHIV:tä makaakinissa, jotka ovat samanaikaisesti infektoituneet C. trachomatiksia/T. vaginaliksella. |

*(10 20:stä kokonaistuloksesta näytetty, priorisoidaan Emtricitabiini-spesifisen PrEP-tehokkuuden relevanssin mukaan; loput 10 ovat pääosin SIV-patogeneesin/resistanssimekanismitutkimuksia, joilla on vain periferinen lääkerelevanssi.)*

### Ranking 3 — Neurokehityksen häiriö, jossa on ataaksinen kävely, puhetta puuttuu ja vähennetty kortikaaliset valkean aineen määrä
TxGNN-pistemäärä 99.92% (ranking 1168) · Näyttötaso **L5** · Suositus: **Pidätä**

Tällä hetkellä ei ole liittyviä kliinisiä tutkimuksia rekisteröitynä. Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta. Paketin oma perustelut sanoo, että virusestäjä RT-inhibiittorin ja tämän geneettisen neurokehityshäiriön kausaalisuusmekanismin (neuronaalimuuttojen/myelinaation geeniviat) välillä ei ole tunnettua biologista linkkiä — tämä on todennäköisesti tietokaaviossa olevan yhteisesiintymisen artefakti eikä todellinen farmakologinen signaali.

---

## Turvallisuusnäkökulmat

Katso pakettiselosteesta turvallisuustietoja. *(Kaikki jäsennellyt turvallisuuskentät — tärkeimmät varoitukset, vasta-aiheet ja lääkevuorovaikutukset — ovat täyttämättömiä tietoaukkojen aiheita tässä paketissa; erityisesti `DG001` merkitsee puuttuvat TFDA/sääntelyyn liittyvät pakettiselostevaroitukset **Estävänä** aukkona, joka on ratkaistava ennen kuin mikään turvallisuusvaiheesta (S1) tehtävä arviointi voi edetä.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Mikään kolmesta TxGNN-ennusteesta tässä paketissa ei ole validoitu, toimiva *uusi ihmisen* indikaatio: ranking 1 -signaali (FIV) on laji-epäsovinnaisuuden eläinlääketieteen entiteetti, ranking 2 -signaali (SIV) on esikliinistä näyttöä indikaatiolle (PrEP), jota emtricitabiini-sisältävällä tuotteilla jo on, ei uutta, ja ranking 3 -signaalilla ei ole kliinisiä tutkimuksia, ei kirjallisuutta eikä uskottavaa mekanistista linkkiä. Yhdistettynä estävään turvallisuuden tietoaukkoon (ei TFDA/pakettiselostevaroituksia tai vasta-aiheita) ja Suomen markkinan puutteeseen, tämä ehdokas ei täytä kriitteereitä edetä S0/S1:n yli.

**Etenemiseen vaaditaan seuraavaa:**
- Ratkaise **DG001** (Estävä): hanki TFDA-pakettiselostevaroitukset/vasta-aiheet ennen S1-turvallisuusarviointia
- Ratkaise **DG002** (Korkea): vahvista Emtricitabiinin vaikutusmekanismi DrugBank API -kyselyä käyttämällä
- Selventää ennustelupipeline-kanssa, pitäisikö laji-epäsovinnaisuuden tauti-entiteetit (kissahivenloinen/apinahivenloinen) suodattaa pois ihmisen indikation ehdokaspoolia ranking-/pisteytysvaiheessa
- Jos aito uusi ihmisen indikaatio etsitään edelleen emtricitabiinille, kohtele ranking 2:ta (SIV) vain vahvistuksena jo-olevalle PrEP-indikatiolla — eikä uutena ehdokkaana — ja deprioritisoi rankingit 1 ja 3 virheellisiksi signaaleiksi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

