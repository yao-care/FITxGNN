---
layout: default
title: Atosiban
parent: Pelkkä mallin ennuste (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Atosiban
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Atosiban: Uudelleenkäytön arviointi — riittämättömät tiedot jatkamiselle

## Yhden lauseen yhteenveto

Atosiban (DrugBank ID: DB09059) on oksitosiini/vasopressiini-reseptori-antagonisti, joka tunnetaan laajasti tokolitiikkana ennenaikaisen synnytyksen hoitossa (hyväksytty EU:ssa tuotenimellä Tractocile).
Nykyinen näyttöpaketti sisältää **ei yhtään TxGNN-ennustettua uutta indikaatiota**, ja kriittiset tietoaukot toimintamekanismissa ja turvallisuustiedoissa estävät perusteellisen uudelleenkäytön arviointin.
**Suositeltu päätös on odottaa** kunnes tiedonkeruu on valmis.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Tunnettu tokolitiikka ennenaikaisen synnytyksen hoitoon (ei rekisteröity Taiwanissa) |
| Ennustettu uusi indikaatio | Ei ennusteita saatavilla |
| TxGNN-ennusteen pistemäärä | N/A |
| Näytön taso | L5 — mallin ennustetta ei luotu; ei tukevia tutkimuksia |
| Taiwanin markkinoiden tila | ✗ Ei markkinoilla (0 lupaa) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | **Odottaa** |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaisia toimintamekanismia koskevia tietoja ei ole saatavilla tässä näyttöpaketissa. Vakiintuneen farmakologisen tiedon perusteella, Atosiban on oksitosiini- ja vasopressiini V1a-reseptorien kilpailullinen antagonisti. Estämällä oksitosiinin aiheuttamia kohdukon supistuksia, sitä käytetään kliinisesti uhkaavan ennenaikaisen synnytyksen viivyttämiseen raskauden viikolla 24–33. Se on hyväksytty Euroopan unionissa, mutta ei ole rekisteröity Taiwanissa.

TxGNN-ennusteita uusille indikaatioille ei luotu tälle ehdokkaalle. Tämä voi johtua puuttuvista molekyylitiedoista, mallille syötetystä riittämättömästä datasta, tai lääkkeen kapeasta reseptoriprofiilistä, joka rajoittaa soveltuvuutta eri sairauksiin. Ilman ennustettuja indikaatioita, mekaanista siltaa mihinkään uuteen sairauteen ei voida arvioida.

Täydellinen uudelleenkäytön perustelu tulee mahdolliseksi, kun TxGNN-putki ajetaan uudelleen täydellisillä lääkkeen ominaisuuksilla, ja toimintamekanismin tiedot noudetaan DrugBankista.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole liittyvää kliinistä tutkimusta rekisteröity uusille indikaatioille.

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole liittyvää kirjallisuutta saatavilla uusille indikaatioille.

---

## Turvallisuusasiat

Turvallisustiedot löytyvät pakkausselosteesta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Odottaa**

**Perustelu:**
Atosibania koskeva näyttöpaketti ei sisällä yhtään TxGNN-ennustettua uutta indikaatiota ja siinä on estävän vakavuustason tietoaukot turvallisuustiedoissa ja toimintamekanismissa; vastuullinen uudelleenkäytön arviointi ei ole mahdollinen tässä vaiheessa.

**Jatkamiseksi tarvitaan seuraavaa:**

- **TxGNN-mallin uudelleenajo**: Luo ennustetut indikaatiot käyttämällä täydellisiä lääkkeen ominaisuuksien tietoja (DrugBank molekyyliprofiilit, kohde-annotaatiot)
- **Toimintamekanismi (MOA)**: Nouda DrugBank API:stä (DB09059) — merkitty korkean vakavuustason tietoaukoksi
- **Turvallisuustiedot**: Lataa ja jäsennä TFDA tai EMA/EU pakkausseloste, jotta voit poimia keskeiset varoitukset, vasta-aiheet ja lääke-lääke-interaktiot — merkitty estävän vakavuustason tietoaukoksi
- **Näytön keruu**: Kun ennustettu indikaatio on saatavilla, suorita kliinisen tutkimuksen ja kirjallisuushaut uuden kohdesairauden osalta (ClinicalTrials.gov, PubMed)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

