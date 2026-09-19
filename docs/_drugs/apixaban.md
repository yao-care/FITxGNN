---
layout: default
title: Apixaban
parent: Pelkkä mallin ennuste (L5)
nav_order: 36
evidence_level: L5
indication_count: 1
---

# Apixaban
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

# Apixaban: Näyttöpaketti puutteellinen — uudelleenkohdentamisen ehdokkaita ei tunnistettu

## Yhden lauseen yhteenveto

Apixaban on suora antikoagulantti (Tekijä Xa:n estäjä), jota käytetään laajalti kansainvälisesti aivohalvauksen ehkäisyyn eteisvärinässä ja laskimotromboembolia (VTE) hoidossa.
Nykyinen Näyttöpaketti (v4) ei palautunut mitään TxGNN-ennustamia uusia indikaatioita, ja kriittiset lähtötiedot — mukaan lukien vaikutusmekanismi ja turvallisuusdata — jäävät ratkaisematta.
Tämä raportti on alustavaa paikkamerkki; täydellinen uudelleenkohdentamisen arviointi ei voi edetä, kunnes tietojen puutteet on korjattu.

---

## Pika-yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla Näyttöpaketista |
| Ennustettu uusi indikaatio | Ei tunnistettu |
| TxGNN-ennustepistemäärä | N/A |
| Näyttötaso | — (ei ennusteita arvioitavaksi) |
| Taiwanin markkinatilanne | Ei markkinoilla (Ei markkinoilla) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | **Pidä** |

---

## Miksi ennusteita ei ole saatavilla

TxGNN-malli palautti tyhjän `predicted_indications`-listan Apixabanille. Kyselylokin perusteella DrugBank kyselyyn vastattiin onnistuneesti (result_count: 1), mutta putkilinja ei tuottanut pisteytettyjä ehdokkaita. Kolme todennäköistä syytä:

1. **Puuttuvat alkuperäiset indikaatiot**: `original_indications`-kenttä on tyhjä, mikä on saattanut aiheuttaa, että taudin ja lääkkeen verkon läpikulku aloitettiin määrittelemättömästä ankkuripisteestä, jolloin ei syntynyt ehdokasteitä.
2. **MOA-puuttue (DG002, korkea vakavuus)**: Ilman vaikutusmekanismin tietoja TxGNN ei voi rakentaa mekanismitason samankaltaisuuspiirteitä, joita käytetään ehdokassairauden-lääkkeen linkkien pisteyttämiseen.
3. **Turvallisuusportti ei läpäissyt (DG001, estävä vakavuus)**: TFDA:n pakkausseloste-kysely palautti tuloksen, mutta varoitukset/vasta-aiheet eivät jäsentyneet Näyttöpakettiin. Tämä estävä puuttue estää putkilinjaa etenemästä turvallisuuden esiarviointiin (S1), mikä on saattanut pysäyttää koko työnkulun.

Kunnes kaikki estävät puutteet on ratkaistu ja TxGNN-ajo suoritetaan uudelleen, uudelleenkohdentamisen ehdokkaita ei voi arvioida.

---

## Taiwanin markkinatiedot

Apixabanilla ei ole **rekisteröityjä myyntilupia** Taiwan FDA:ssa (TFDA). Lääkettä ei markkinoida kaupallisesti Taiwanissa minkään tuotenimen alla tietojen rajapäivään (2026-04-20) mennessä.

---

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustiedot.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
Kaksi ratkaisematta jäänyttä tietojen puutetta — yksi estävä (DG001: TFDA:n pakkausseloste turvallisuusdata) ja yksi korkea (DG002: MOA) — estävät jopa alustavaa arviointia. Lisäksi TxGNN-malli tuotti nolla ennusteita, mikä tarkoittaa, että uudelleenkohdentamisen hypoteesia ei ole arvioitavaksi tässä vaiheessa.

**Jatkaakseen seuraava on tarpeen:**

- [ ] **Suorita TxGNN-putkilinja uudelleen** ratkaisemisen jälkeen DG001:n ja DG002:n — `predicted_indications`-lista täytyy täyttää ennen kuin mitään arviointia voidaan suorittaa
- [ ] **Ratkaise DG001 (estävä)**: Lataa ja jäsennä TFDA:n pakkausseloste-PDF puruaksesi varoitukset ja vasta-aiheet; tämä vaaditaan S1-turvallisuuden esiarviointiin
- [ ] **Ratkaise DG002 (korkea)**: Kysy DrugBank API:sta Apixabanin vaikutusmekanismia (Tekijä Xa:n esto-polkua) ja täytä `original_moa`
- [ ] **Täytä `original_indications`**: Lisää hyväksytyn indikaation luettelo (esim. aivohalvauksen ehkäisy ei-venttiiliperäisessä eteisvärinässä, VTE:n hoito/profylaksia) antaaksesi TxGNN:lle oikeat verkko-ankkuripisteet
- [ ] **Suorita DDI-kysely uudelleen**: DDI-haku palautti `not_found`; tarkista, heijasteleeko tämä todellista vuorovaikutustietojen puuttumista vai kyselyn epäonnistumista

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

