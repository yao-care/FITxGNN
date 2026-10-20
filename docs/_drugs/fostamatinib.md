---
layout: default
title: Fostamatinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Fostamatinib: ennustettu uusi käyttöaihe Autosomaalinen trombosytopenia, normaalit verihiutaleet (näytön taso L5). Alkuperäinen käyttöaihe: Trombosytopenia"
monitor_inn: "Fostamatinib"
predicted_indications: ["autosomal thrombocytopenia with normal platelets", "non-syndromic esophageal malformation"]
---

# Fostamatinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

# Fostamatinib: Trombosytopeniasta ennustettuun autosomaaliseen trombosytopeniaan (normaalit verihiutaleet)

## Yhden lauseen yhteenveto

Fostamatinibi on Suomessa (EU-keskitetyn myyntiluvan kautta) trombosytopenian hoitoon hyväksytty lääke. TxGNN-malli ennustaa sen voivan tehota **autosomaaliseen trombosytopeniaan, jossa verihiutaleet ovat normaalit**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste on toistaiseksi pelkkä laskennallinen signaali.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Trombosytopenia |
| Ennustettu uusi käyttöaihe | Autosomaalinen trombosytopenia, normaalit verihiutaleet |
| TxGNN-ennusteen pistemäärä | 99,45 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettu (ei voimassa olevaa myyntilupaa) |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Fostamatinibi on R406:n esilääke, ja R406 on pernan tyrosiinikinaasin (SYK) estäjä. Sen tunnettu käyttö immuunitrombosytopeniassa perustuu siihen, että SYK:n esto vähentää makrofagien Fc-reseptorivälitteistä verihiutaleiden tuhoamista. Tämän raportin tietoihin ei kuitenkaan sisälly vahvistettua vaikutusmekanismitietoa, joten mekanistista yhteyttä ei voida varmentaa.

TxGNN-pistemäärä on erittäin korkea, mutta se näyttää johtuvan verkostollisesta läheisyydestä alkuperäiseen trombosytopenia-käyttöaiheeseen. Ennustettu sairaus viittaa perinnölliseen (autosomaaliseen) verihiutaleiden määrän häiriöön, joka todennäköisesti ei ole immuunivälitteinen. Tällöin vasta-ainevälitteistä verihiutaleiden poistumaa ei ole, eikä SYK:n estolle ole selvää mekanistista perustetta. Ennustetta tulee siksi pitää vain laskennallisena signaalina.

Toinen ennustettu käyttöaihe, **ei-oireyhtymälliset ruokatorven epämuodostumat** (pistemäärä 99,05 %), ei saa mitään mekanistista tukea. Kyseessä ovat sikiökauden ruoansulatuskanavan kehityshäiriöistä johtuvat synnynnäiset rakenteelliset viat (esim. ruokatorven atresia, tracheoesofageaalifisteli). SYK:n esto vaikuttaa immuunisolujen signalointiin eikä korjaa anatomisia kehityshäiriöitä. Korkea pistemäärä on todennäköisesti tietämysgraafin artefakti, ja tila vaatii yleensä kirurgista korjausta.

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005012 | Tavlesse | – | Trombosytopenia |

Myyntilupa on tilassa "peruutettu", joten voimassa olevia myyntilupia ei ole.

## Turvallisuusnäkökohdat

**Lääkkeiden yhteisvaikutukset:** Yhteisvaikutustietokannasta löytyi yhteensä 100 yhteisvaikutusta. Alla on esimerkkejä ensimmäisistä 20 tuloksesta.

- **Merkittävä (Major):** klaritromysiini
- **Kohtalainen (Moderate):** rabepratsoli, omepratsoli, deksalansopratsoli, simetidiini, hydrokortisoni, deksametasoni, betametasoni, budesonidi, triamsinoloni, alosetroni, alvimopaani, aprepitantti, dolasetroni, dronabinoli, eliglustaatti, empagliflotsiini, loperamidi, pioglitatsoni, morfiini

Muiden turvallisuustietojen osalta katso valmisteyhteenveto.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Kummallekin ennustetulle käyttöaiheelle on vain mallipohjainen ennuste (L5) ilman kliinistä tai kirjallisuusnäyttöä. Ensimmäisen ennusteen mekanistinen perustelu on heikko (sairaus ei todennäköisesti ole immuunivälitteinen) ja toisen uskottavaa mekanismia ei ole. Lisäksi lääkkeellä ei ole voimassa olevaa myyntilupaa Suomessa.

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitus- ja vasta-aihetietojen hankinta Fimeasta (estää turvallisuusseulonnan jatkamisen)
- Vaikutusmekanismitietojen (MOA) täydentäminen DrugBankista
- Selvitys siitä, onko ennustetun perinnöllisen trombosytopenian taustalla SYK-reitin mekanismi
- Prekliiniset tai kirjallisuuteen perustuvat selvitykset ennen mahdollisia kliinisiä tutkimuksia
- Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittäminen
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

