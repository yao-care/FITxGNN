---
layout: default
title: Lapatinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 213
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: Lääkkeen uudelleenkäyttöä koskevan arvioinnin raportti

## Yhden lauseen yhteenveto

Lapatinib on proteiinityrosiinikinaasin kaksoisestäjä, joka kohdistuu HER2:iin (ErbB2) ja EGFR:iin (ErbB1), ja se kehitettiin alun perin HER2-positiiviseen edistyneeseen rintasyöpään.
**Tämä todistusten kokoelma on kriittisesti epätäydellinen: kenttä `predicted_indications` on tyhjä**, mikä tarkoittaa, että TxGNN-uudelleenkäyttöennusteita ei ole saatavilla tätä kertaa arviointia varten.
Ilman ennustettua uutta käyttöosoitusta täydellistä uudelleenkäytön analyysia ei voida tuottaa — päätös on **Pysäytä** kunnes todistusten kokoelma on täytetty.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen käyttöosoitus | HER2-positiivinen edistynyt tai etäpesäkkeinen rintasyöpä (aihealueiden tiedoista; ei läsnä todistusten kokoelmassa) |
| Ennustettu uusi käyttöosoitus | **Ei saatavilla** — kenttä `predicted_indications` on tyhjä |
| TxGNN-ennustepistemäärä | Ei saatavilla |
| Todisteiden taso | Ei voida määrittää |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pysäytä** |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaiset toimintamekanismin tiedot eivät ole tällä hetkellä saatavilla todistusten kokoelmassa (`original_moa: [Data Gap]`). Julkisesti tunnetun farmakologian perusteella lapatinib (DrugBank-tunniste: DB01259) on pieni-molekylaarinen, palautuva proteiinityrosiinikinaasin intrasellulaarisen domeenin kaksoisestäjä, joka kohdistuu HER2/ErbB2:een ja EGFR/ErbB1:een. Estämällä alavirtaan olevia RAS/MAPK- ja PI3K/AKT-signaloitumisreittejä se estää HER2-ylituotettujen syöpäsolujen lisääntymisen ja selviytymisen.

Koska tässä todistusten kokoelmassa ei ole TxGNN-ennustetta, ei ole mahdollista arvioida mekanistista uskottavuutta mihinkään tiettyyn uuteen käyttöosoitukseen. Kun ennuste-pipeline tarjoaa kohteeksi valitun käyttöosoituksen, HER2/EGFR-signaloitumisen ja kyseisen sairauden mekanistinen yhteys voidaan muodollisesti arvioida.

**Tämä osio täydennetään, kun kenttä `predicted_indications` on täytetty.**

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä tähän todistusten kokoelmaan ei ole rekisteröity asiaan liittyviä kliinisiä tutkimuksia.

> *Syy: kenttä `predicted_indications` on tyhjä. Klinisen tutkimuksen todisteet ovat käyttöosoituskohtaisia, eikä niitä voi hakea ilman kohdesairautta.*

---

## Kirjallisuuden todisteet

Tällä hetkellä tähän todistusten kokoelmaan ei ole saatavilla asiaan liittyvää kirjallisuutta.

> *Syy: kenttä `predicted_indications` on tyhjä. Kirjallisuuden todisteet ovat käyttöosoituskohtaisia, eikä niitä voi hakea ilman kohdesairautta.*

---

## Suomen markkinatiedot

Lapatinib-lääkkeellä on **0 hyväksyntää** kyselyyn lähetetyssa sääntelytietokannassa. Lääke ei ole tällä hetkellä **markkinoilla**.

| Hyväksyntänumero | Tuotteen nimi | Lääkemuoto | Hyväksytty käyttöosoitus |
|------------------|---------------|-----------|-------------------------|
| — | — | — | Rekisteröityjä hyväksyntöjä ei ole |

---

## Solumyrkyllisyys

Lapatinib on syöpänsolujen kasvua estävä kohdennettu lääkehoito (HER2/EGFR-proteiinityrosiinikinaasin kaksoisestäjä). Seuraavaa sovelletaan:

| Kohde | Sisältö |
|-------|---------|
| Solumyrkyllisyysluokitus | Kohdennettu lääkehoito — HER2/EGFR-proteiinityrosiinikinaasin kaksoisestäjä |
| Luuydinsuppressio-riski | Alhainen tai kohtalainen (pienempi luuydinsuppressio kuin perinteisillä sytostaateiilla; neutropeniaa on raportoitu, mutta harvemmin) |
| Pahoinvointiluokitus | Alhainen |
| Valvottavat tekijät | LFTs, sydämen toiminto (LVEF), täydellinen verenkuva, elektrolyytit (QTc-seuranta vaaditaan) |
| Käsittelysuojat | Katso pakkausselosteesta varoituksia ja varotoimia |

---

## Turvallisuustarkastelut

Katso turvallisesta tiedosta pakkausselosteesta.

> *Kaikki turvallisuuskentät (`key_warnings`, `contraindications`, DDI) on merkitty tietovajeiksi nykyisessä todistusten kokoelmassa. TFDA-pakkausseloste-kysely palautti tuloksen (kyselylokin tunniste 4, tila: success), mutta jäsenneltyä sisältöä ei ladattu tähän todistusten kokoelman versioon. Korjaus: jäsennä TFDA-pakkausseloste-PDF.*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pysäytä**

**Perustelu:**
Tästä todistusten kokoelmasta puuttuu kaksi kriittisintä komponenttia uudelleenkäytön analyysille — `predicted_indications` (TxGNN-tuloste) ja `original_moa` — mikä tekee mahdottomaksi arvioida sekä ehdokaskäyttöosoitusta että ennusteen mekanistista uskottavuutta.

**Jatkamista varten tarvitaan seuraavaa:**

- **[Esto]** Aja TxGNN-ennuste-pipeline tunnukselle DB01259 ja täytä kenttä `predicted_indications` vähintään yhdellä ehdokassairaudella, mukaan lukien `txgnn.score`, `evidence.clinical_trials` ja `evidence.literature`
- **[Korkea]** Hae lapatiniibin toimintamekanismi (MOA) DrugBank-ohjelmistorajapinnasta (DrugBank-kysely palautti onnistumisen 1 tuloksella kyselylokin tunnisteen 3 — nämä tiedot olisi jo pitänyt jäsennellä)
- **[Korkea]** Jäsennä TFDA-pakkausseloste-PDF (kyselylokin tunniste 4 palautti onnistumisen) poistaaksesi `key_warnings` ja `contraindications` sekä ratkaisemaan tietovajeita DG001/DG002
- **[Keskitaso]** Aja DDI-kysely uudelleen laajemmalla hakualueella (nykyinen tulos: `not_found`; harkitse synonyymia tai tuotenimenä hakua lapatiniibin/Tykerb-nimelle)
- Kun kenttä `predicted_indications` on täytetty, tuota tämä raportti uudelleen Evidence Pack v5+-versiolla

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

