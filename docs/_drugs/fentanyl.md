---
layout: default
title: Fentanyl
parent: Pelkkä mallin ennuste (L5)
nav_order: 163
evidence_level: L5
indication_count: 2
---

# Fentanyl
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

# Fentanyyli: dokumentoimattomasta alkuperäisestä indikaatiosta nephrogenic syndrome of inappropriate antidiuresis -oireyhtymään

## Yhden lauseen yhteenveto

Fentanyilin alkuperäisen indikaation tiedot eivät sisälly tähän näyttöpakettiin, ja lääkettä ei ole tällä hetkellä markkinoitu Suomessa. TxGNN-malli ennustaa, että fentanyyli voi olla merkityksellinen **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)** -oireyhtymälle, ja mallin pistemäärä on korkea (**99.46%**), mutta tueksi ei ole löydetty yhtään kliinistä tutkimusta tai kirjallisuutta.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu tässä näyttöpaketissa (lisenssejä tai alkuperäisiä indikaatioita ei saatavilla) |
| Ennustettu uusi indikaatio | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN-ennusteen pistemäärä | 99.46% (upottamisen sijoitus 5778) |
| Näyttötaso | L5 — vain mallin ennuste, ei tukevia tutkimuksia |
| Suomen markkinatilanne | ✗ Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on järkevä?

Fentanyilin vaikutusmekanismin tietoja ei ole saatavilla tässä näyttöpaketissa (`original_moa: [Data Gap]`), ja lääkkeen alkuperäinen indikaatio/indikaatiot ovat myös dokumentoimattomat tässä, joten fentanyilin tunnetun farmakologian ja NSIAD:n välinen suhde ei ole todistettavissa käytössä olevista tiedoista.

Mallin omat uudelleenkäyttöperustelu-kentät tälle kandidaatille (`mechanistic_link`, `similarity_to_original`) on merkitty **odottavaksi** — mikä tarkoittaa, että mekanistista tai samankaltaisuusanalyysiä ei ole vielä suoritettu tälle ennusteelle. Tämä on puhtaasti upottamiseen perustuva assosiaatio TxGNN:stä, jolla ei ole tukevia kliinisiä tutkimuksia, kirjallisuutta eikä asiantuntijoiden tarkistamaa perustelua tällä hetkellä.

Ilman vaikutusmekanismin tietoja, alkuperäisen indikaation kontekstia tai tukevia tutkimuksia, tätä ennustetta tulee käsitellä validoimattomana mallin tuloksena eikä mekanistisesti perustelluna hypoteesina.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

## Suomen markkinatiedot

Fentanyylilla ei ole tällä hetkellä Fimean markkinointihyväksyntöjä arkistossa (`total_licenses: 0`), joten tuote-/hyväksyntätaulukkoa ei voida tuottaa.

## Turvallisuushuomiot

Kaikki turvallisuustiedot löydät pakkausselosteesta.

*(Huomio: TFDA/Fimea-selostetiedot on merkitty **estäväksi** tietovajeeksi — sen puuttuminen estää alkuperäisen S1-turvallisuusarvioinnin loppuunsaattamisen tälle kandidaatille.)*

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Tätä ennustetta tuetaan vain TxGNN-mallin pistemäärällä, eikä sillä ole kliinisiä tutkimuksia, kirjallisuutta eikä suoritettua mekanistista perustelua (näyttötaso L5). Lääke on myös markkinoimaton Suomessa, ja **estävän** vakavuuden tietovahe (puuttuva TFDA/Fimea-seloste) estää jopa alkuperäisen turvallisuusarvioinnin.

**Etenemiseksi tarvitaan seuraavaa:**
- TFDA/Fimea-seloste (varoitukset, vasta-aiheet) — estävä vahe, vaaditaan ennen S1-turvallisuusarviointia
- Drugbank-lähteinen vaikutusmekanismin (MOA) tieto fentanyylille
- Fentanyilin alkuperäisen indikaation historia mekanistisen samankaltaisuuden arvioimiseksi NSIAD:lle
- Odottavien mekanistisen linkin ja samankaltaisuus-alkuperäiseen-nähden -analyysin loppuunsaattaminen tälle kandidaatille
- Kohdennettu kirjallisuuden ja klinisten tutkimusten haku erityisesti fentanyyli–NSIAD-assosiaatiolle, koska nykyiset PubMed/ClinicalTrials.gov/ICTRP-kyselyt palautuivat nollilla tuloksilla

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

