---
layout: default
title: Baricitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 62
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# BARICITINIB: Lääkkeen uudelleenkäytön arviointi — Tiedonkeruu epätäydellinen

## Yhden lauseen yhteenveto

BARICITINIB on JAK1/JAK2-inhibiittori, joka on hyväksytty useissa maissa reumatoiditta nivelreumaa ja muita tulehdussairauksia vastaan.
Nykyinen Evidence Pack ei sisällä TxGNN-ennustetuloksia uusille indikaatioille, eikä lääkkeellä ole **markkinointilupaa Suomessa**.
Täydellinen uudelleenkäytön arviointi ei ole mahdollista, kunnes estävät tietoaukot on korjattu.

---

## Pika-yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla Evidence Packissa |
| Ennustettu uusi indikaatio | TxGNN-ennusteita ei saatavilla |
| TxGNN-ennusteen pistemäärä | N/A |
| Todisteiden taso | L5 — Mallin tuotos puuttuu |
| Suomen markkinatilanne | Ei markkinoitu |
| Hyväksynnän lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi täyttä ennuste-analyysia ei voida suorittaa

Kaksi estävää tietoaukoa estävät vakiomukaisen arvioinnin:

**DG001 (Estävä):** Pakkausselosteen varoitukset ja vasta-aiheet eivät ole käsiteltyjä. Ilman tätä pakollinen S1-turvallisuusseulonta ei voida suorittaa, eikä uudelleenkäytön ehdokkaan arviointia voida turvallisesti jatkaa.

**DG002 (Korkea):** Toimintamekanismin tiedot DrugBankista eivät ole haettu. Ilman sitä on mahdotonta selittää, miksi BARICITINIB:in farmakologia voisi siirtyä uuteen indikaatioon — tämä on arviointikehyksen ydinvaatimus.

Lisäksi `predicted_indications`-kenttä palautti tyhjän taulukon, mikä tarkoittaa, että TxGNN joko ei ole vielä ajettu tälle lääkkeelle tai se ei ole tuottanut rankattuja ehdokkaita. Kaikki seuraavat osiot (kliinisten tutkimusten evidenssi, kirjallisuuden evidenssi, ennustetun indikaation yleiskatsaus) riippuvat tästä tuloksesta eikä niitä voi täyttää.

---

## Tiedot Suomen markkinoista

BARICITINIB:lla ei tällä hetkellä ole **markkinointilupaa** Suomessa. Rekisterissä ei ole rekisteröityjä tuotteita, annostemuotoja tai hyväksyttyjä indikaatioita.

---

## Turvallisuushuomiot

Katso turvallisuustiedot pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelu:**
Evidence Pack on rakenteellisesti epätäydellinen — TxGNN-ennusteet puuttuvat ja Estävä-tason tietoaukko (DG001) estää turvallisuusseulonnan. Tämän ehdokkaan kehittäminen ilman näiden aukkojen ratkaisemista olisi metodologisesti kestämätöntä.

**Jatkaakseen tarvitaan seuraavat:**

- **[Estävä — DG001]** Lataa ja jäsennä BARICITINIB:n pakkausseloste PDF TFDA-verkkosivulta poimiaksesi varoitukset ja vasta-aiheet; tämä avaa S1-turvallisuusportin
- **[Korkea — DG002]** Kysy DrugBank-ohjelmointirajapintaa BARICITINIB:lle (DB11817) saadaksesi toimintamekanismin, lääkkeen kategoriat ja myrkyllisyystiedot
- **[Vaaditaan]** Aja TxGNN-malli DB11817:lle tuottamaan rankattuja ennustettuja indikaatioita; ilman `predicted_indications`, mitään uudelleenkäytön tavoitetta ei voida arvioida
- **[Vaaditaan]** Suorita todisteiden keräämisprosessi uudelleen (kliiniset tutkimukset, kirjallisuus) kun ennustettu indikaatio on vahvistettu
- **[Valinnainen]** Tarkista Fimec:in hyväksyntätilanne kansallisen lääketietokannan kautta mahdollisista viimeaikaisista hyväksynnöistä, joita tässä kyselysyklissä ei ole otettu huomioon

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

