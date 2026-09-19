---
layout: default
title: Aprepitant
parent: Pelkkä mallin ennuste (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: Arviointi keskeytetty — kriittiset tietoaukot tunnistettu

## Yhteenveto

Aprepitant (DrugBank: DB00673) on NK1 (neurokiini-1) -reseptoriagonisti, joka on hyväksytty kansainvälisesti kemoterapian aiheuttaman pahoinvoinnin ja oksentelun (CINV) ehkäisyyn.
Tämä näyttöpaketti (v4, 2026-04-20) on **puutteellinen**: TxGNN-ennusteputkilinja on palauttanut **ei yhtään ennustettua indikaatiota**, ja kaksi kriittistä tietoaukoa jää ratkaisematta.
Mitään merkityksellistä uudelleenkäyttöarviointia ei voida suorittaa, kunnes nämä aukot on korjattu.

---

## Pikayleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | NK1-reseptoriagonisti / antiemetikum (CINV-profylaksia) |
| Ennustettu uusi indikaatio | Odottaa — TxGNN-ennusteet eivät ole vielä käytettävissä |
| TxGNN-ennustepistemäärä | N/A |
| Näyttötaso | N/A |
| Taiwanin markkinoiden tila | ✗ Ei markkinoitu |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | **Keskeytä** |

---

## Miksi arviointia ei voida vielä suorittaa

Tällä hetkellä tämän näyttöpaketin yksityiskohtaisia vaikutusmekanismitietoja ei ole saatavilla (tietoaukko DG002, vakavuus: Korkea). Julkisesti saatavilla olevien tietojen perusteella aprepitantti on NK1-reseptoriagonisti, jonka FDA ja EMA ovat hyväksyneet CINV:n ja leikkauksen jälkeisen pahoinvoinnin ja oksentelun (PONV) ehkäisyyn. Sitä käytetään yleisesti yhdessä kortikosteroidien ja 5-HT₃-antagonistien kanssa antiemetisen profylaksin osana.

Kriittisempää on, että **TxGNN ei ole tuottanut yhtään ennustettua indikaatiota** aprepitantille tässä näyttöpaketissa (`predicted_indications`-taulukko on tyhjä). Ilman TxGNN-ennustepistemäärää ja kohdeindikaatiota uudelleenkäyttöhypoteesia ei voida arvioida.

Kaksi tietoaukoa on ratkaistava, ennen kuin tämä kandidaatti voi edetä:

| Aukon tunnus | Kohde | Vakavuus | Vaikutus | Korjaus |
|--------------|-------|----------|---------|--------|
| DG001 | TFDA-pakkausseloste varoitukset / vasta-aiheet | **Estävä** | Ei voida suorittaa S1-turvallisuustarkastusta | Lataa TFDA-seloste PDF ja jäsennä |
| DG002 | Vaikutusmekanismi (MOA) | **Korkea** | Ei voida suorittaa mekanismin relevanssianalyysia | Kysy DrugBank API:sta DB00673 |

---

## Taiwanin markkinatiedot

Aprepitantilla on **nolla** hyväksyttyä lisenssiä Taiwanissa. Sitä ei ole tällä hetkellä markkinoitu kotimaassa.

---

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Keskeytä**

**Perustelut:**
Näyttöpaketti ei sisällä TxGNN-ennusteita ja kaksi ratkaisematonta tietoaukkoa, joiden vakavuus on Estävä/Korkea; uudelleenkäyttöarviointiraporttia ei voida luoda mielekkäällä tavalla tässä vaiheessa.

**Jotta voidaan edetä, seuraava on tarpeen:**

1. **Suorita TxGNN-ennusteputkilinja** — luo rankatut indikaatioennusteet aprepitantille ja täytä `predicted_indications`
2. **Ratkaise DG001** — lataa ja jäsennä TFDA:n (tai EMA:n/FDA:n) pakkausseloste PDF:ää avainvaroitusten ja vasta-aiheita varten
3. **Ratkaise DG002** — kysy DrugBank API:sta aprepitantin vaikutusmekanismitiedot
4. **Luo uudelleen näyttöpaketti** — kun kaikki aukot on ratkaistu, tuota v5-näyttöpaketti täydellisenä tietona ja lähetä uudelleen täyden raportin luomista varten

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

