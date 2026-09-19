---
layout: default
title: Netarsudil
parent: Kohtalainen näyttö (L3-L4)
nav_order: 260
evidence_level: L4
indication_count: 2
---

# Netarsudil
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **2** kpl
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

# Netarsudil: Silmänpaineen kohoamisesta primaariseen perinnölliseen glaukoomaan

## Yhden lauseen yhteenveto

Netarsudil on Rho-kinaasi (ROCK) / norepinefriinin siirtäjä (NET) -duaaliestiö, jolla on vakiintunut silmänpainetta alentava mekanismi ja jota käytetään glaukooman ja silmän verenpaineen nousun hoidossa (markkinoilla muissa maissa nimillä Rhopressa/Rocklatan). TxGNN-malli ennustaa, että se voi olla tehokas myös erityisesti **primaarisessa perinnöllisessä glaukooomassa**, mutta tämä suppeampi ennustus perustuu tällä hetkellä vain **1 epäsuoraan liittyvään kliiniseen tutkimukseen** ja **ei yhdellekään omakseen julkaistusta tutkimukselle**.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Avokulmainen glaukooma / silmän verenpaineen nousu (vakiintunut käyttö kirjallisuuden perusteella; ei markkinoilla Suomessa tämän aineiston mukaan) |
| Ennustettu uusi indikaatio | Primaarinen perinnöllinen glaukooma |
| TxGNN-ennusteen pistemäärä | 99.50% |
| Näytöntaso | L4 |
| Suomen markkinointi | ✗ Ei markkinoilla |
| Lupa-autorisaatioiden lukumäärä | 0 |
| Suositeltu päätös | Pidättäytyminen |

## Miksi tämä ennuste on järkevä?

Netarsudil on kaksoisestäjä, joka estää Rho-kinaasia (ROCK) ja norepinefriinin siirtäjää (NET). Se vaikuttaa verkkokalvon verkkosolukkoon vähenentäen nesteen ulosvirtausresistanssia ja alentaa episkleraalisen venoosin painetta, mikä alentaa silmän sisäistä painetta (IOP). Tämä mekanismi selittää sen hyvin dokumentoidun tehokkuuden avokulmaisen glaukooman ja silmän verenpaineen nousun hoidossa – indikaatio, jota tämän näyttöpaketin toisen sijoituksen ennuste tukee 36 kliinisellä tutkimuksella (mukaan lukien useat valmistuneet Phase 3 -pivoittutkimukset, kuten ROCKET ja MERCURY -sarjat) ja 20 julkaisulla, näytöntasolla L1.

Primaarinen perinnöllinen glaukooma on glaukooman geneetinen alatyyppi, joka liittyy tyypillisesti verkkokalvon verkkosolukon rakenteellisiin tai toiminnallisiin puutoksiin (esim. ulosvirtausreitillä olevia geenejä vaikuttavat mutaatiot). Koska netarsudiilin IOP-alentava vaikutus toimii suoraan tässä samassa ulosvirtausreitissä, on mekanistisesti uskottavaa, että se voisi lisätä ulosvirtausta perinteisestä puutoksesta riippumatta – mahdollisesti ohittaen pikemminkin kuin korjatakseen geneettistä poikkeavuutta.

Kuitenkaan mikään tutkimus tässä näyttöpaketissa ei suoraan testaa netarsudiilin IOP-tehokkuutta geneettisesti vahvistetussa perinnöllisen glaukooman populaatiossa. Ainoastaan asiaan liittyvä tutkimus (NCT06969586) arvioi sarveiskalvon endoteelisuojaa glaukooma-potilailla, joilla on Fuchsin endoteelisen sarveiskalvon dystrofija – täysin eri päätetulos – ja se on luokiteltu "C":ksi (epäsuora relevanssi). Rank-1-ennuste on siksi parhaiten ymmärrettävissä vahvan yleisen avokulmaisen glaukooman näytön ekstrapolaationa, ei suorana todistuksena perinnöllisen alatyypissä.

## Kliinisen tutkimuksen näyttö

| Tutkimuksen numero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A | Kutsulla osallistava | 50 | Arvioi, suojavatko topikaalit ROCK-estäjät sarveiskalvon endoteelisoluja silmänmustaisen leikkauksen jälkeen potilailla, joilla on glaukooma ja Fuchsin endoteelisen sarveiskalvon dystrofija (FECD); vertaa topikaalista ROCK-estäjää lumelääkkeeseen. Luokiteltu "C"-relevanssiksi – päätetulos on sarveiskalvon endoteelisolun menetys, ei IOP-tehokkuus perinnöllisessä glaukooomassa, ja osallistaminen on vain kutsulla. |

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta, joka olisi spesifistä primaariselle perinnölliselle glaukooomalle.

## Suomen markkinatiedot

Netarsudil ei ole tällä hetkellä markkinoilla Suomessa (markkinointi status: Ei markkinoilla; 0 autorisaatiota), joten tuote-/autorisaatiotaulukkoa ei ole saatavilla.

## Turvallisuusnäkökohdat

Katso tuoteselosteesta turvallisuustiedot. (Netarsudiilin tärkeimmät varoitukset, vasta-aiheet ja lääkevuorovaikutustiedot eivät ole vielä saatavilla tässä näyttöpaketissa – TFDA/Fimea-tuoteselosteen haku on merkitty blokkaavasiksi tietojen puutteeksi, katso alla.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidättäytyminen**

**Perustelut:**
Rank-1 TxGNN-ennuste (primaarinen perinnöllinen glaukooma) perustuu tällä hetkellä yhteen epäsuoraan liittyvään tutkimukseen ilman tukevaa kirjallisuutta (L4, päätösvaiheen S1) – riittämätön edistymiselle. Netarsudiilin mekanismi on hyvin validoitu glaukooomalle yleisesti, mutta tämä vahvempi näyttöperusta ei suoraan vahvista tehokkuutta perinnöllisessä alatyypissä, ja blokkava turvallisuustietojen puutos (ei TFDA/Fimea-tuotelehteä) estää jopa alkuperäisen turvallisuusseulonnan.

**Edistymiselle tarvitaan seuraavaa:**
- TFDA/Fimea-tuoteseleosteen (varoitukset, vasta-aiheet) – tällä hetkellä turvallisuusarvioinnin este (S1)
- Vahvistettu mekanismin dokumentaatio DrugBankista (tällä hetkellä tietojen puute)
- Tutkimus, joka suoraan arvioi IOP-tehokkuutta geneettisesti vahvistetussa primaarisessa perinnöllisessä glaukooomassa, pikemminkin kuin ekstrapolaatio yleisen avokulmaisen glaukooman tiedoista
- Lääkevuorovaikutus (DDI) -tiedot, joita ei tällä hetkellä löydy

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

