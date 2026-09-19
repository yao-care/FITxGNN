---
layout: default
title: Adalimumab
parent: Kohtalainen näyttö (L3-L4)
nav_order: 18
evidence_level: L3
indication_count: 6
---

# Adalimumab
{: .fs-9 }

Näytön taso: **L3** | Ennustetut käyttöaiheet: **6** kpl
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

# Adalimumab: reumatoidiartriitista reumatoidiseen vaskuiittihin

## Yhden lauseen yhteenveto

> Adalimumab on täysin ihmisen peräisin oleva anti-TNF-α monoklonaalinen vasta-aine, joka on pitkään vakiintunut reumatoidiartriitiin ja muihin samankaltaisiin autoimmuunitulehduksellisiin sairauksiin liittyvänä hoitona.
> TxGNN-malli ennustaa, että se saattaa olla tehokas myös **reumatoidiseen vaskuiittihin (RV)**, reumatoidiartriittiin liittyvään vakavaan ekstraartikulaariseen ilmentymään,
> ja tällä hetkellä **5 kliinistä tutkimusta** ja **10 järjestettyä julkaisua** tukevat (ja mutkistavat) tätä suuntaa — kirjallisuus osoittaa sekä terapeuttisia että haitallisia yhteyksiä adalimumab-hoidon ja vaskuiitin välillä.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Reumatoidiartriitti (ja TNF-α-vetoiset autoimmuunitulehdukselliset sairaudet). *Huomio: Fimean hyväksyttävien indikaatioiden tekstiä ei ole tässä näyttöpaketissa — sääntelylupa-data puuttuu (tietoraossa).* |
| Ennustettu uusi indikaatio | Reumatoidinen vaskuiitti |
| TxGNN-ennustepistemäärä | 99.80% |
| Näyttötaso | L3 |
| Suomen markkinatilanne | ✗ Ei saatavana markkinoilla (Ei saatavana markkinoilla) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennustus on järkevä?

Yksityiskohtaisia mekanismin tietoja ei palautettu tässä näyttöpaketissa (`original_moa: [Tietoraossa]`). Hyvin vakiintuneiden julkisten tietojen perusteella adalimumab on täysin ihmisen peräisin oleva IgG1 monoklonaalinen vasta-aine, joka sitoutuu TNF-α:han ja neutraloi sen, estäen sen alavirtaan suuntautuvaa proinfiammatorista signalointia. Se on anti-TNF-luokan perustajajäsen infliksimabi ja etanersepin rinnalla, hyväksytty lukuisissa maissa reumatoidiartriittiin, psoriaattiartriittiin, aksiaalisen spondyliitiin, nuorten idiopaattiseen artriittiin, psoriaasiin ja inflammatoorisiin suolistosairauksiin.

Reumatoidinen vaskuiitti (RV) on yksi vakavimmista pitkäkestoisen, usein seropositiivisen reumatoidiartriittin ekstraartikulaarisista ilmenemismuodoista, jota aiheuttavat immunekompleksien sedimentaatio ja TNF-α-välitteinen verisuonten seinämien inflammaatio. Koska RV syntyy suoraan hallitsemattomasta RA-assosioituneet inflammaatiosta ja TNF-α on tämän reitin keskeinen sytokirii, TNF-α:n estäminen on mekanismisesti uskottava keino verisuonten seinämän inflammaation ja immunekompleksitaakan vähentämiseksi — tämä on biologinen perustelu, jonka TxGNN:n tietoverkko todennäköisesti kuvaa.

Kuitenkin näyttö on todella kaksijakoinen. Toisaalta julkaistu tapausraportti (PMID 25133007) kuvaa digitaalisen vaskuiitin RA-potilaalla, joka vastasi hyvin adalimumab-hoitoon, ja järjestelmällinen katsaus (PMID 33058033) käsittelee biologisia lääkkeitä — myös anti-TNF-aineita — osana RV:n terapeuttista arsenaalia. Toisaalta useat tapausraportit ja lääketurvallisuusvalvontakohortti (PMID 28719435, PMID 28123776, PMID 36418100) kuvaavat adalimumab- ja muita TNF-estäjälääkkeitä *aiheuttavan* vaskuiitin-kaltaisia tai lupus-kaltaisia haittavaikutuksia RA-potilaissa. Tämä paradoksi — TNF-α-esto sekä mahdollisena vaskuiitin hoitona että mahdollisena käynnistäjänä — tarkoittaa, että mekanistinen yhteys, vaikka biologisesti uskottava, ei ole vielä suunnan osalta ratkaistu ja vaatii keskittynyt turvallisuus-/tehokkuus-selvityksen ennen lisäselvityksiä.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Rekrytointi | Keskeiset tulokset |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Vaihe 2 | Ei vielä rekrytoinnissa | 80 | Perioperatiivinen immunosuppressiivinen hallinta (myös adalimumab) reumatologian potilaissa, jotka käyvät läpi hartiadiartiplastiikasta; arvioi pahenemisentaajuutta, ei suoraan RV-tehokkuutta (Grade C). |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Valmis | 184 | Monikansallinen havainnointitutkimus tosilisumabista RA-potilaissa, joilla on riittämätön DMARD/biologinen vastaus; ei RV-spesifistä (Grade C). |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Valmis | 9,261 | Todellisen maailman turvallisuustutkimus brolutsisumabista märässä AMD:ssä — ei liity adalimumabiin tai RV:hen, todennäköisesti avainsanan hakemisen artefakti (Grade C). |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Valmis | 808 | Poikkileikkaustutkimus biologisesta DMARD-hoitomalleista kiinalaisissa RA-potilaissa; ei vaskuiitin-spesifistä (Grade C). |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Tuntematon | 750,000 | Laaja kohortti, joka arvioi toisen immuuni-välitteisen inflammatorisen sairauden (IMID, myös vaskuiitti) kehittymisen riskiä biologis-/immunosuppressiivisen hoidon jälkeen ensimmäiseen IMID:hen; epäsuorasti liittyvä tämän kysymyksen turvallisuuspuolelle (Grade B). |

*Yksikään tämän joukon tutkimus ei ole suunniteltu nimenomaisesti testaamaan adalimumab-hoitoa reumatoidisen vaskuiitin tehokkuuden osalta; kaikki lueteltujen tutkimuksissa ovat epäsuoria (RA-väestötasoiset tutkimukset, biologisen DMARD-rekisterit tai todennäköiset epäsopivuudet).*

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Järjestelmällinen katsaus | Clinical Rheumatology | Järjestelmällinen katsaus biologisista lääkkeistä (myös anti-TNF-aineista) reumatoidisen vaskuiitin hoitoon — suoraan osuvain näyttölähde. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Lääketurvallisuusvalvontakohortti | RMD Open | BSRBR-RA rekisteritiedot, jotka vertailevat lupus-kaltaisten ja vaskuiitin-kaltaisten tapahtumien riskiä ja ominaisuuksia RA-potilaissa TNF-estäjillä vs. ei-biologisilla DMARD-lääkkeillä — keskeinen turvallisuussignaali. |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Katsaus | Journal of Clinical Medicine | Päivitys RA-assosioituneen episkleriitin ja skleriitin (silmän vaskuiittiset ilmenemismuodot) hoitoon. |
| [31163474](https://pubmed.ncbi.nlm.nih.gov/31163474/) | 2019 | Katsaus | Deutsche Medizinische Wochenschrift | Katsaus JAK-estäjiin reumatologiassa, asettaen ne suhteeseen anti-TNF-terapian vaihtoehdoista. |
| [37699653](https://pubmed.ncbi.nlm.nih.gov/37699653/) | 2024 | Geneettinen assosiaatiotutkimus | Annals of the Rheumatic Diseases | HLA-DRB1/HLA-DQA1 assosiaatiot adalimumab-immunogeniteettiä vastaan RA-potilaissa. |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | PK-mallinnus tutkimus | Pharmaceutics | Populaation PK-mallinnus adalimumab/etanersepi biosimilaari-annostusjärjestelmistä RA:ssa. |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Tapausraportti | Internal Medicine (Tokyo) | Akuutti keuhkojen hypertensio-kriisi reumatoidisen vaskuiitin potilaalla adalimumab-annoksen vähentämisen jälkeen — viittaa jatkuvan hoidon suojaavaan vaikutukseen. |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Tapausraportti | Internal Medicine (Tokyo) | Tosilisumab käytetään ANCA-assosioituneen nefriittin hoitoon, joka kehittyi abatasepti/adalimumab-hoidon aikana RA:ta varten. |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Tapausraportti (haittatapahtuma) | American Journal of Dermatopathology | Leukosytoklastinen vaskuiitti dermaalisella perivaskulaarisella hemofagosytoosin kanssa, joka liittyy adalimumab-hoitoon — haittava (pro-vaskuiitti) signaali. |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Tapausraportti | Case Reports in Rheumatology | Digitaalinen vaskuiitti RA-potilaalla, joka vastasi hyvin adalimumab-hoitoon — positiivinen tehokkuussignaali RV:lle. |

*Kymmenen lisäkirjallisuustietuetta haettiin, mutta ne jäävät luokittelematta (`study_type: pending`) lähdetiedoissa ja jätettiin pois tästä taulukosta odottaen luokittelua.*

---

## Suomen markkinatiedot

Adalimumab ei ole tällä hetkellä **saatavana markkinoilla** Suomessa tämän näyttöpaketin mukaan (`market_status: Not marketed`, `total_licenses: 0`), ja lupatietueita ei ole saatavilla yhteenveto. Tämä olisi vahvistettava itsenäisesti Fimean nykyistä rekisteriä vastaan, sillä adalimumab (myös alkuperäinen Humira® ja useat biosimilaarit) on laajalti saatavana EU/ETA-alueella, ja saatavana olematon tila täällä saattaa heijastaa lähdekyselyssä puutetta pikemminkin kuin todellista sääntelystä poissaoloa.

---

## Turvallisuusnäkökohdat

Katso pakkausseloste turvallisuustiedoista — `key_warnings`, `contraindications` ja DDI-tiedot on merkitty kaikki tietoraoksi tai niitä ei ole löydetty tässä näyttöpaketissa.

**Tärkeää:** metatasoisen tietoraon loki merkitsee tämän **estäväksi** ongelmaksi (DG001 — TFDA/Fimea pakkausselosteen varoitukset/vasta-aiheet, lähde: TFDA virallinen sivusto, remediointi: pakkausselosteen PDF:n hakeminen ja jäsentäminen). Näyttöpaketin mukaan tämä aukko tällä hetkellä **estää pääsyn S1 turvallisuuden esihyväksyntävaiheeseen** tälle ehdokkaalle, riippumatta edellä käsitellystä mekanistisesta tai kliinisen tutkimuksen näytöstä.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelu:**
- **Estävä** tietoraoko (DG001) tarkoittaa, että virallisen reseptiseloste-turvallisuustiedot (varoitukset/vasta-aiheet) eivät ole saatavilla, mikä sinänsä estää edistymisen muodolliseen turvallisuuden esihyväksyntään (S1).
- Tästä raoista riippumatta, sairauden-spesifistä näyttö on vain **L3** (järjestelmällinen katsaus/kohorttitaso, ei valmista RCT:tä, joka kohdistaisi adalimumab-hoitoa RV:hen) ja on **suunnallisesti sekoitettu** — julkaistut tapausraportit tukevat adalimumab-hoitoa sekä RV-liittyväiseen vaskuiittiin hoitona että mahdollisena TNF-estäjillä olevia RA-potilaita vaskuiitin-kaltaisia/lupus-kaltaisia reaktioita käynnistävänä.

**Edistymiseksi seuraavat asiat ovat tarpeen:**
- Hae ja jäsentämään TFDA/Fimea pakkausseloste ratkaisemaan estävä turvallisuus-tietoraoko (DG001).
- Hanki strukturoitu DrugBank MOA ja myrkyllisyystiedot (DG002) tukemaan muodollisesti mekanistista perustelua.
- Suorita kohdistettu lääketurvallisuusvalvonta/tapaussarja-analyysi selvittämään, käsitteleekö vai käynnistääkö TNF-α-esto adalimumab-hoitolla useammin vaskuiitin RA-potilaissa, koska nykyinen näyttö tukee molempia suuntia.
- Jos jatketaan, määritä RV-spesifisti interventiotutkimuksen kuvaus ja päätepiirteet, koska mikään valmis satunnaistettu tutkimus ei tällä hetkellä testaa adalimumab-hoitoa suoraan tätä indikaatiota varten.
- Vahvista Suomen/Fimea markkinoilla ja lisensointitilanne suoraan nykyistä rekisteriä vastaan, sillä "ei saatavana markkinoilla" -tilanne täällä saattaa heijastaa epätäydellistä lähdekyselyä pikemminkin kuin todellista sääntelystä puuttumista.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

