---
layout: default
title: Atazanavir
parent: Pelkkä mallin ennuste (L5)
nav_order: 45
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Atazanavir: Lääkkeen uudelleenkäytön arviointi — Riittämätön data ennusteelle

## Yhden lauseen yhteenveto

Atazanavir (DB01072) on HIV-1-proteasin inhibiittori, jota käytetään antiretroviraalisessa hoidossa.
Nykyinen Evidence Pack ei sisällä **yhtään TxGNN-ennustettuja indikaatioita**, ja kriittiset tiedot, mukaan lukien vaikutusmekanismi, turvallisuusvaroitukset ja vasta-aiheet, puuttuvat.
Tämä arviointi ei voi edetä kliinisen merkitsevyyden arviointiin, kunnes tunnistetut tietoaukot ratkaistaan.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | HIV-1-infektio (yleinen tieto; ei vahvistettu Evidence Packissa) |
| Ennustettu uusi indikaatio | Ei ennustetta saatavilla |
| TxGNN-ennustusten pistemäärä | Ei saatavilla |
| Todisteiden taso | L5 — Ennusteita ei luotu |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätettävä |

---

## Miksi tämä ennuste on järkevä?

Tässä Evidence Packissa ei ole yhtään TxGNN-ennustettuja indikaatioita. `predicted_indications`-kenttä on tyhjä taulukko, mikä tarkoittaa, ettei lääkkeen uudelleenkäytön malli ole luonut yhtään mahdollisia uusia indikaatioita atazavaniirille. Ilman vähintään yhtä ennustetta, tämän arvioinnin perustarkoitus — uuden uudelleenkäytön hypoteesin arviointi — ei voi toteutua.

Vaikutusmekanismin tiedot on myös tunnistettu korkean vakavuuden tietoaukoksi. Pakkausselosteen varoituksista ja vasta-aiheista saaduissa tuloksissa oli tietoja sääntelylähteistä, mutta niitä ei jäsennetty strukturoiduiksi kentiksi. Ilman vahvistettua MOA:ta ja turvallisuuden perusarvoa, missään alkuperäisen indikaation ja hypoteettisen uuden indikaation välille ei voida rakentaa mekanistista siltaa.

Atazanavir tunnetaan laajalti HIV-1-proteasin inhibiittorina, joka estää viruspolyproteiinin kypsymistä. Tämä yleistieto on esitetty vain kontekstin vuoksi eikä se korvaa strukturoituja Evidence Pack -tietoja, joita tämä arviointikehys edellyttää.

---

## Turvallisuusnäkökohdat

Turvallisuustiedoista katso pakkausseloste.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätettävä**

**Perustelut:**
Evidence Pack ei sisällä TxGNN-ennustettuja indikaatioita ja siinä on kolme estävää tai korkean vakavuuden tietoaukkoa; uudelleenkäytön hypoteesia ei ole arvioitavana, ja lisäarviointiin tarvittava turvallisuuden perusarvio puuttuu.

**Jatkamista varten tarvitaan seuraavaa:**

- **TxGNN-ennuste**: Suorita TxGNN-putkilinja uudelleen DB01072:lle `predicted_indications`-kentän täyttämiseksi; taulukko on tällä hetkellä tyhjä
- **Vaikutusmekanismi (MOA)**: Hae DrugBank-ohjelmointirajapinnasta DB01072:n farmakodynaamiset ja kohdetiedot
- **Pakkausselosteen varoitukset ja vasta-aiheet**: Jäsennä TFDA/EMA-pakkausselosteen PDF (kyselylokit osoittavat onnistunutta hakua, mutta ei jäsenneltyä tulosta) `key_warnings` ja `contraindications` -kentiksi
- **Lääke-lääke-vuorovaikutukset (DDI)**: DDI-kysely palautti `not_found`; suorita kysely uudelleen vaihtoehtoisilla tunnisteilla tai käytä laajempaa DDI-tietokantaa
- **Markkinahyväksynnän tila Suomessa**: Tarkista EMA/Fimea-rekisteriä vasten; nykyinen `market_status` "Not marketed" saattaa heijastaa Taiwan-rekisteriin kohdistunutta kyselyä eikä Suomen markkinakyselyä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

