---
layout: default
title: Carfilzomib
parent: Pelkkä mallin ennuste (L5)
nav_order: 90
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

# Carfilzomib: useiden myelooman hoidosta CMM7:ään

## Yhden lauseen yhteenveto

Carfilzomib on toisen sukupolven proteasomin estäjä; tämän näyttöpaketin kirjallisuus tunnistaa sen ensimmäisen linjan anti-myelooma-aineeksi, vaikka tälle lääkeelle ei palautettu strukturoitua alkuperäisen indikaation tietoja.
TxGNN-malli ennustaa, että se voi olla tehokas **CMM7**:lle (perinnöllinen ihon pahanlaatuinen melanooma tyypin 7), mutta kyseessä on tällä hetkellä **puhdas malliennuste ilman kliinisiä tutkimuksia ja ilman julkaisuja**, jotka tukisivat sitä.
Näytön täysin puuttuessa tämä ehdokas istuu näyttötasolla **L5** ja suositeltu päätös on **Hold**.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Useiden myelooma *(pääteltävissä tämän paketin kirjallisuuskontekstista; ei läsnä strukturoiduissa indikaatio-/lupakenttien tiedoissa)* |
| Ennustettu uusi indikaatio | CMM7 (perinnöllinen ihon pahanlaatuinen melanooma tyypin 7) |
| TxGNN-ennusteen pistemäärä | 99.37% |
| Näyttötaso | L5 |
| Suomen markkinoiden tila | ✗ Ei markkinoilla |
| Lupahyväksyntöjen määrä | 0 |
| Suositeltu päätös | Hold |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä tälle lääkeelle ei ole kirjattu strukturoituja toimintamekanismin tietoja tässä näyttöpaketissa (`original_moa: [Data Gap]`). Kuitenkin asiaan liittyvät tiedot paketin muualla kuvaavat carfilzomibia toisen sukupolven, peruuttamattomaksi proteasomin estäjäksi, joka estää 26S-proteasomin kymotripsiinitapaisen aktiivisuuden, aiheuttaa väärin taittuneiden proteiinien kertymisen, NF-κB-väylän säätelyn häiriintymisen ja apoptoosin — mekanismin, joka on vakiintunut useiden myelooman hoidossa.

CMM7-ennusteen osalta mallin oma perusteluteksti toteaa, että **ei ole tunnettu suoraa mekanistista yhteyttä** carfilzomibin proteasomin esto-väylän ja CMM7:n välillä, joka on perinnöllinen melanooman alatyyppi, johon liittyy eniten germinaalia POT1- ja muita telomeereihin ja DNA-korjaukseen liittyviä geenivariasioita. Tämä ennuste näyttää olevan laaja ekstrapolaatio yleisemmästä "melanooma"-tautiluokasta eikä CMM7-spesifinen signaali.

Erikseen (ei osa tätä erityistä ehdokasta) tämä näyttöpaketti sisältää prekliinisen kirjallisuuden carfilzomibista melanoomassa yleisemmin — viisi artikkelia, enimmäkseen solulinja- ja in-silico-tutkimuksia, jotka osoittavat pro-apoptoottiset vaikutukset B16-F1-melanoomasoluissa ja molekyylisen dokkauksen aktiivisuuden melanooman kannalta relevanteille kinaaseille. Mikään tästä kirjallisuudesta ei käsittele CMM7:ää tai sen POT1-perustuvaa biologiaa, joten se ei suoraan vahvista nykyistä ennustetta, mutta se osoittaa, että laajempi "melanooma"-luokka ei ole kokonaan mekanistisesti tutkimaton tälle lääkkeelle.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

Tällä hetkellä asiaan liittyvää kirjallisuutta ei ole saatavilla.

---

## Suomen markkinatiedot

Carfilzomib ei ole tällä hetkellä markkinoilla Suomessa; näyttöpaketissa ei ole lupahyväksyntätietueita.

---

## Sytostaattinen vaikutus

| Kohta | Sisältö |
|------|---------|
| Sytostaattisen vaikutuksen luokittelu | Kohdennettu lääkitys (proteasomin estäjä) |
| Mylosupressionin riski | Katso pakkausselosteesta varoitukset ja varotoimet |
| Pahoinvointiluokittelu | Katso pakkausselosteesta varoitukset ja varotoimet |
| Seurantakohteet | Katso pakkausselosteesta varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausselosteesta varoitukset ja varotoimet |

---

## Turvallisuushuomiot

Katso pakkausselosteesta turvallisuustiedot.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Hold**

**Perustelut:**
CMM7-ennuste perustuu ainoastaan TxGNN-mallipistemäärään (L5, S0), jolle ei ole kliinisiä tutkimuksia eikä julkaisuja, ja mekanistinen perusteluteksti vahvistaa tunnetun yhteyden puuttumisen carfilzomibin proteasomin esto-väylän ja CMM7:n POT1/telomeereihin perustuvan biologian välillä. Tällä hetkellä ei ole näyttöpohjaa edistää tätä ehdokasta.

**Jatkaakseen tarvitaan seuraavaa:**
- TFDA/valmistajan pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä esto-tietoaukko (DG001)
- Muodollinen, strukturoitu toimintamekanismin data DrugBankista tai vastaavasta (DG002)
- Prekliiniset tai mekanistiset tutkimukset, jotka suoraan yhdistävät proteasomin eston POT1-mutantin/CMM7-melanooman biologiaan
- Mikä tahansa todellisen maailman tai havainnointisignaali (jopa off-label-käytöstä), joka yhdistää carfilzomibin perinnöllisiin melanooman alatyypeihin
- Suomen markkinoiden ja sääntelyväylän arviointi, koska lääke ei ole tällä hetkellä markkinoilla siellä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

