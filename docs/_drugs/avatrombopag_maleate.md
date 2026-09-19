---
layout: default
title: Avatrombopag Maleate
parent: Pelkkä mallin ennuste (L5)
nav_order: 51
evidence_level: L5
indication_count: 0
---

# Avatrombopag Maleate
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

# Avatrombopag maleate: Lääkkeen uusiokäytön arvio — TxGNN-ennusteita ei saatavilla

## Yhden lauseen yhteenveto

Avatrombopag maleate on trombopoetiini-reseptoriagonisti (TPO-RA), jota käytetään aikuisten verihiutaleperääntymän hoitoon.
TxGNN-malli ei palauttanut tämän lääkkeen ennustettuja uusia indikaatioita nykyisessä Evidence Pack -kokoelmassa, ja kriittiset tietomuodot, kuten vaikutusmekanismi ja turvallisuustiedot, eivät täyttyneet onnistuneesti.
Tätä arviota ei voida saattaa loppuun, kunnes tietoputken puutteet korjataan.

---

## Pikayleiskatsaus

| Aihe | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei haettu tästä Evidence Pack -kokoelmasta |
| Ennustettu uusi indikaatio | Ei yhtään — TxGNN ei palauttanut ennusteita |
| TxGNN-ennusteen pistemäärä | Ei saatavilla |
| Todistusten taso | Ei arvioitavissa |
| Suomen markkinatilanne | Ei markkinoilla |
| Lupapäätösten lukumäärä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi tämä ennuste on perusteltu?

TxGNN ei palauttanut avatrombopag maleatille ennustettuja indikaatioita tässä Evidence Pack -kokoelmassa. Ilman kohde-indikaatiota mekanistista silta-analyysia ei voida suorittaa.

Vaikutusmekanismin tiedot merkittiin tietojen puutteiksi (vakavuus: Korkea) eikä niitä täytetty huolimatta onnistuneesti kirjatusta DrugBank-kyselystä. Tämä estää arvioinnin, voiko lääkkeen farmakologia uskottavasti laajentua uudelle sairausalueelle.

Julkisesti saatavilla olevien tietojen perusteella avatrombopag maleate kuuluu TPO-reseptoriagonistiluokkaan ja stimuloi verihiutaletuotantoa — mutta ilman TxGNN:n ehdokaslähtöä ei ole lääkkeen uusiokäyttöhypoteesia, jota voitaisiin arvioida tässä vaiheessa.

---

## Suomen markkinatiedot

Avatrombopag maleatia ei tällä hetkellä markkinoida Suomessa. Fimean hyväksyntöjä ei ole rekisteröity (0 lupapäätöstä).

---

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelu:**
Evidence Pack -kokoelma on kriittisesti epätäydellinen — TxGNN ei palauttanut ennustettuja indikaatioita, vaikutusmekanismi puuttuu ja turvallisuustiedot (varoitukset, vasta-aiheet, lääkeinteraktiot) ei haettu. Arviointiin ei ole lääkkeen uusiokäyttöhypoteesia.

**Jatkamiseksi tarvitaan seuraavaa:**

- **Suorita TxGNN-ennustusputki uudelleen** avatrombopag maleatille ja varmista, että ehdokasindikaatiot kirjoitetaan kohteeseen `predicted_indications`
- **Hae vaikutusmekanismi (MOA) DrugBankista** — onnistunut kysely kirjattiin (result_count: 1), mutta tiedot ei välitetty Evidence Pack -kokoelmaan; tutkittava jäsentämisvaihetta
- **Jäsennä pakkausseloste** — TFDA pakkausseloste -kysely palautti myös 1 tuloksen (result_count: 1), mutta varoitukset ja vasta-aiheet jäivät tyhjiksi; tarkista PDF-poimimislogiikka
- **Varmista alkuperäinen hyväksytty indikaatio** Fimean / EMA:n sääntelytiedostoista lääkkeen uusiokäytön peruslinjan määrittämiseksi
- **Kun yllä mainitut asiat on ratkaistu**, luo Evidence Pack uudelleen (v5+) ja lähetä uudelleen täydelliseen arviointiin

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

