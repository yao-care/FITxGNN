---
layout: default
title: Andexanet Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 34
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Andexanet Alfa: ennustettu uusi käyttöaihe Glanzmannin trombasteniaa (näytön taso L5). Alkuperäinen käyttöaihe: Lääkkeisiin liittyvät sivu- ja haittavaikutukset"
---

# Andexanet Alfa
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

# Andeksanetti alfa: Lääkkeeseen liittyvistä haittavaikutuksista Glanzmannin trombasteniaan

## Yhteenveto

Andeksanetti alfa on rekombinantti tekijä Xa:n kaltainen "houkutinproteiini", jota on käytetty lääkkeisiin liittyvien haittavaikutusten hoitoon, erityisesti tekijä Xa:n estäjien antikoagulaatiovaikutuksen kumoamiseen.
TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **Glanzmannin trombastenian**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta** eikä **yhtään julkaisua**.
Ennuste perustuu pelkästään mallin laskemaan korkeaan pistemäärään, ja sen biologinen perusta on heikko.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Lääkkeisiin liittyvät sivu- ja haittavaikutukset |
| Ennustettu uusi käyttöaihe | Glanzmannin trombasteniaa |
| TxGNN-ennustepistemäärä | 99,77 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Andeksanetti alfa on katalyyttisesti inaktiivinen, rekombinantti tekijä Xa:n houkutinmolekyyli. Se sitoo ja sitoutaa tekijä Xa:n estäjiä (sekä TFPI:tä) ja kumoaa siten niiden antikoagulaatiovaikutuksen. Tarkempia mekanismitietoja (MOA) ei ole tähän raporttiin koottu tietokannasta saatavilla.

Glanzmannin trombastenia on perinnöllinen verihiutalesairaus, jonka aiheuttaa GPIIb/IIIa-reseptorin (integriini alfa-IIb beta-3) vika. Andeksanetti alfa vaikuttaa hyytymiskaskadiin eikä korjaa verihiutaleiden aggregaatiohäiriötä. Uskottavaa mekanistista yhteyttä ei siis ole havaittavissa.

Mallin korkea pistemäärä heijastaa todennäköisesti tiedonhaun verkostossa jaettua "verenvuoto/hemostaasi"-naapurustoa, ei todellista farmakologista yhteyttä.

### Muut mallin ennustamat käyttöaiheet

| Sija | Ennustettu käyttöaihe | TxGNN-pistemäärä | Näytön taso | Arvio |
|------|------|------|------|------|
| 2 | Verihiutaleiden primaarinen vapautumishäiriö | 99,76 % | L5 | Ei mekanistista yhteyttä: vika on verihiutaleiden granulaeritys, ei tekijä Xa:n esto. Lisäksi tromboembolisen riskin vuoksi (varoitusruutu) kokeellinen käyttö on epäedullista. |
| 3 | Pseudo-von Willebrandin tauti | 99,65 % | L5 | Johtuu verihiutaleiden GPIb-alfan toiminnanlisäysmutaatiosta, ei liity andeksanetti alfan mekanismiin. |
| 4 | Hemofilia | 99,10 % | L4 | Hemofiliassa puuttuu tekijä VIII/IX, eikä andeksanetti alfa korvaa niitä. Löydetty kirjallisuus on epäsuoraa. |

---

## Kliiniset tutkimukset

Ensisijaisesta ennusteesta (Glanzmannin trombastenia) ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia. Myöskään muista ennustetuista käyttöaiheista ei löytynyt rekisteröityjä tutkimuksia.

---

## Kirjallisuusnäyttö

Ensisijaisesta ennusteesta (Glanzmannin trombastenia) ei ole kirjallisuutta. Alla on hemofiliaa (sija 4) koskeva kirjallisuus, joka on kuitenkin vain epäsuoraa eikä osoita andeksanetti alfan tehoa hemofiliassa.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Kohorttitutkimus | Circulation | ANNEXA-4-osa-analyysi: andeksanetti alfan teho ja turvallisuus akuutissa ruoansulatuskanavan verenvuodossa tekijä Xa:n estäjää käyttävillä potilailla |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Suositus | Thrombosis and Haemostasis | ICSH:n päivitetyt suositukset suorien oraalisten antikoagulanttien (DOAC) laboratoriomäärityksiin; mainitsee spesifisen kumoamislääkkeen |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laboratoriotutkimus | Haemophilia | DOAC-häiriön vähentäminen tekijä VIII:n ja IX:n määrityksissä; andeksanetti alfa neutraloi rivaroksabaanin vaikutuksen laboratoriossa |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Katsaus | Current Pharmaceutical Design | Uudet hemostaattiset lääkkeet: perioperatiiviset anestesiologiset näkökohdat |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Katsaus | Blood | Tekijä Xa:n estäjien kumoaminen ja kattamattomat tarpeet trauma-potilailla |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Katsaus | Drug Safety | NOAC-lääkkeiden kumoamisstrategiat: kehitystilanne ja tulevaisuuden näkymät |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Katsaus | Deutsche Medizinische Wochenschrift | Hyytymishäiriöt tehohoidossa: uusimmat kuulumiset |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Katsaus | EJHaem | Andeksanetti alfan käyttö Britannian sairaaloissa: paikallisten protokollien katsaus |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Kannanotto | British Journal of Haematology | Britannian hematologiayhdistyksen kannanotto andeksanetti alfan käyttöön |

Nämä julkaisut kuvaavat lähinnä DOAC-lääkkeiden kumoamista ja laboratoriohäiriöitä. Ne eivät osoita hyötyä hemofiliassa tai Glanzmannin trombasteniassa.

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004108 | Ondexxya (AstraZeneca AB) | – | Lääkkeisiin liittyvät sivu- ja haittavaikutukset (tila: peruutettu) |

---

## Turvallisuusnäkökohdat

- **Tromboembolinen riski**: Andeksanetti alfaan liittyy tromboembolisen riskin varoitus (varoitusruutu), mikä tekee kokeellisesta käytöstä ei-indikoidussa verenvuotohäiriössä epäedullista.
- **Lääkeinteraktiot**: Interaktiotietoja ei löytynyt.

Tarkemmat turvallisuustiedot (varoitukset ja vasta-aiheet) on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteiden tueksi ei ole kliinisiä tutkimuksia, ja mekanistinen yhteys kaikkiin neljään ennustettuun sairauteen on heikko tai puuttuu. Korkeat TxGNN-pistemäärät näyttävät johtuvan verkostoyhteyksistä eivätkä farmakologisesta perustasta. Lisäksi tromboembolinen riski ja Suomessa peruutettu myyntilupa heikentävät jatkokehityksen perusteita.

**Jatkoon etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvitys (tämänhetkinen tietoaukko estää turvallisuusseulonnan).
- Tarkka mekanismitieto (MOA) DrugBankista mekanistisen yhteyden arvioimiseksi.
- Prekliiniset tai mekanistiset tutkimukset, jotka osoittaisivat biologisen perustan jollekin ennustetulle käyttöaiheelle.
- Selvitys myyntiluvan peruuttamisen syistä ja valmisteen saatavuudesta Suomessa.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

