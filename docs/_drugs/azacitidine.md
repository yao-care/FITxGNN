---
layout: default
title: Azacitidine
parent: Pelkkä mallin ennuste (L5)
nav_order: 57
evidence_level: L5
indication_count: 0
---

# Azacitidine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **0** kpl
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

# Azacitidine: uudelleenkäytön analyysi — todistepaketti epätäydellinen

## Yhden lauseen yhteenveto

Azacitidine on pyridiini-nukleosidi-analogi (hypometyylaava aine), joka on indikoitu myelodysplastisissa oireyhtymissä (MDS) ja akuutissa myeloidisessa leukemiassa (AML). **Tämä todistepaketti ei sisällä TxGNN-ennustamia uusia indikaatioita**, ja kriittisiä tietoja — mukaan lukien vaikutusmekanismi ja turvallisuusvaroitukset — ei voitu hakea. Täydellistä uudelleenkäytön arviointia ei voida antaa, kunnes alla luetellut tietoaukot on korjattu.

---

## Pika-yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Myelodysplastiset oireyhtymät (MDS) / Akuutti myeloidinen leukemia (AML) |
| TxGNN-ennustettu uusi indikaatio | Ei saatavilla — `predicted_indications` array on tyhjä |
| TxGNN-ennusteen pistemäärä | Ei saatavilla |
| Todisteiden taso | Ei arvioitavissa |
| Taiwanese markkinoiden tila | Ei markkinoilla (TFDA: 0 hyväksyntää) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidätä** |

---

## Miksi analyysi on epätäydellinen?

Tämä todistepaketti puuttuu kahdesta tietoluokasta, jotka vaaditaan ennen kuin repurposing-arviointia voidaan jatkaa:

**1. TxGNN-ennustetut indikaatiot**
`predicted_indications`-kenttä on tyhjä taulukko. TxGNN-mallin output on pääsignaali, joka ohjaa ehdokkaiden valintaa tässä putkessa. Ilman ennusteita ei ole uutta indikaatiota, jota arvioida, sijoittaa tai suositella. Tämä on kriittisin puuttuva input.

**2. Vaikutusmekanismi (MOA)**
MOA-tietoja ei haettu tähän todistepakettiin (DG002, vakavuus: Korkea). Farmakologisesta kirjallisuudesta azacitidine tunnetaan DNA:n hypometyylaavaksi aineeksi — se sisältyy DNA:han ja RNA:han, estää DNA:n metyylitransferaasin (DNMT), ja aktivoi siten hiljennetyt syöpäsuppressorigeenit, aiheuttaen syöpäsolujen differentiaation tai apoptoosin. Kuitenkin, koska tämä tieto ei ole muodollisesti vahvistettu todistepakettissa, mekanistisen uskottavuuden analyysia mille tahansa tulevalle ennustetulle indikaatiolle ei voida systemaattisesti validoida rakenteisten tietojen vastaan.

---

## Taiwan-markkinoiden tiedot

TFDA-kyselyn mukaan tässä todistepakettissa (kyselyn pvm: 2026-03-29) azacitidine ei ole **markkinoilla Taiwanissa**. Kysely palautti 0 tulosta.

> **Huomio rajat ylittävässä kontekstissa:** EU/EMA-markkinoilla azacitidine:lla (Vidaza®, Onureg®) on hyväksytyt indikaatiot MDS:lle, AML:lle ja kronikalle myelomonosyyttileukemialle (CMML). Jos tämä raportti on tarkoitettu Suomen (Fimea) markkinoille, Fimean sääntelykyselyä on tehtävä erikseen markkinoiden nykyisen aseman vahvistamiseksi.

---

## Sytotoksisisuus

Azacitidine on anti-neoplastinen aine. Jopa ilman täydellistä todistepakettitietoa sen farmakologinen luokka (pyridiini-nukleosidi-analogi / DNA:n hypometyylaava aine) sallii seuraavan luokittelun:

| Kohta | Sisältö |
|------|---------|
| Sytotoksisisuuden luokittelu | Perinteinen sytotoksinen — Epigeneettinen modifioija (DNA:n hypometyylaava aine) |
| Luuydinhalvantumisen riski | **Korkea** — neutropenia, trombosytopenia ja anemia ovat yleisiä annoksen rajoittavia toksisuuksia |
| Oksentamisherkkyyden luokittelu | Kohtalainen |
| Seurantakohteet | Täydellinen verenkuva erilaistuksella (vähintään ennen jokaista sykliä), seerumin kreatiniini, maksatoimintakokeet, seerumin bikarbonaatti |
| Käsittelysuoja | On noudatettava sytotoksisten lääkkeiden käsittelysääntöjä (suljetuissa siirtojärjestelmissä, täydellinen PPE) |

---

## Turvallisuusnäkökohdat

Turvallisen tiedon osalta viittaa pakkausselosteeseen.

Kaikki turvallisuuskentät (tärkeät varoitukset, vasta-aiheet, lääkkeiden väliset vuorovaikutukset) palautuivat ilman tietoja tässä todistepakettissa. TFDA-pakkausselosteen kysely kirjattiin onnistuneeksi (kyselyn tunnus 4), mutta sisältöä ei jäsennetty rakenteisiin kenttiin. DDI-kysely palautti `not_found`.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Azacitidine (DB00928) -todistepaketti on kriittisesti epätäydellinen kaikissa kolmessa keskeisessä arviointidomaanissa — ennustetuissa indikaatioissa, vaikutusmekanismissa ja turvallisuustiedoissa. Suosituksen antaminen ilman näitä inputteja ei täyttäisi vähimmäistodisteiden standardeja.

**Jatkamista varten tarvitaan seuraavaa:**

1. **Suorita TxGNN-ennusteet** Azacitidine:lle (DB00928) `predicted_indications`-kentän täyttämiseksi — tämä estää kaiken muun jäljessä olevan analyysin
2. **Hae MOA-tiedot DrugBank-ohjelmointirajapinnasta** (ratkaisee DG002) — vaaditaan mekanistisen uskottavuuden arviointiin
3. **Jäsennä TFDA-pakkausseloste** (ratkaisee DG001) — PDF-tiedosto löydettiin (kysely 4 palautti menestyksen), mutta varoitukset ja vasta-aiheet ei poimittu rakenteisiin kenttiin
4. **Varmista DDI-kattavuus** — DDI-kysely palautti `not_found`; ristiintarkista DrugBank-interaktiotietokantaa tai muita DDI-lähteitä vastaan
5. **Vahvista Suomen/Fimean markkinatilanne erikseen**, jos tämä ehdokas on tarkoitettu Suomen repurposing-putkeen, sillä TFDA- ja Fimean sääntelytietueet ovat riippumattomia

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

