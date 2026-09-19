---
layout: default
title: Diroximel Fumarate
parent: Pelkkä mallin ennuste (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

# Diroximel Fumarate: Dokumentoimattomasta alkuperäisestä käyttöaiheesta diabeettiseen kataraktaan

## Yhden lauseen yhteenveto

Evidenssipaketti ei dokumentoi diroximel-fumaraatin alkuperäistä hyväksyttyä käyttöaihetta tai yksityiskohtaista vaikutusmekanismia (molemmat merkitty tietovajeiksi), ja lääkettä ei ole tällä hetkellä markkinoilla Suomessa. TxGNN-malli ennustaa mahdollista tehokkuutta **Diabeettiseen kataraktaan**, mutta tämä ja kaikki yhdeksän muuta listalla olevaa oftalmologista käyttöaihetta ovat tällä hetkellä tuettu **nollalla kliinisellä tutkimuksella** ja **nollalla julkaisulla** — ennustus on puhtaasti mallipisteisiin perustuva hypoteesi ilman ulkoista validointia.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihde | Ei saatavilla nykyisessä evidenssipakettissa |
| Ennustettu uusi käyttöaihde | Diabeettinen katarakta |
| TxGNN-ennustuspisteet | 99.9993% |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennustus on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla (DrugBank ei palauttanut MOA-tekstiä tälle lääkkeelle). Tämän evidenssipaketin sisältämien mekanististen perusteluiden perusteella diroximel-fumaraatin aktiivinen metaboliitti, monomethyyli-fumaaraatti (MMF), aktivoi Nrf2-ARE-antioksidanttireittä. Sama reitti on ehdotettu teoreettisena linkkinä kaikkien kymmenen TxGNN-ennustetun käyttöaiheen yli, jotka klusteroituvat lähes kokonaan kataraktan alityyppien ja diabeettisen retinopatian ympärille.

Koska `original_indications` on tyhjä evidenssipaketin osalta, lääkkeen alkuperäisen hyväksynnän ja diabeettisen kataraktan välistä yhteyttä ei voida arvioida täältä saatavien tietojen perusteella.

Mekanistisesti kataraktan muodostuminen diabeetikolla liittyy linssin kristalliiniproteiinien hapettavaan aggregaatioon hyperglykemisen stressin olosuhteissa. Nrf2-reitin aktivaatio voisi teoreettisesti vähentää tätä hapettavaa vahinkoa, minkä vuoksi malli esittää tätä uskottavaksi signaaliksi. Rationaalilta itseltään kuitenkin nimenomaisesti todetaan, että kyseessä on epäsuora, osoittamaton mekanistinen hypoteesi — ei ole olemassa oftalmologista prekliinistä tai kliinistä näyttöä, joka vahvistaa, että systeemisesti annettu diroximel-fumaaraatti saavuttaa terapeuttisia pitoisuuksia linssissa tai verkkokalvotudoksessa.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole liittyvää rekisteröityä kliinistä tutkimusta

## Kirjallisuuden näyttö

Tällä hetkellä kirjallisuutta ei ole saatavilla

## Markkinatilanne Suomessa

Diroximel-fumaaraattia ei ole tällä hetkellä markkinoilla Suomessa (0 rekisteröityä hyväksyntää); lisenssitietoja ei ole saatavilla taulukoitavaksi.

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Ennustus perustuu kokonaan TxGNN-mallipisteisiin (L5), joilla ei ole tukemassa kliinisiä tutkimuksia, kirjallisuutta tai prekliinistä oftalmologista aineistoa, ja lääkettä ei ole markkinoilla Suomessa. Lääkkeen ydin-tasoiset faktat — alkuperäinen käyttöaihde, vahvistettu vaikutusmekanismi ja TFDA:n turvallisuus- ja merkintätiedot — ovat kaikki ratkaisemattomia tietovajeita (DG001 on merkitty Esto, DG002 Korkea), joten kandidaatti ei voi vielä siirtyä turvallisuuden esiseulontaan (S1).

**Jotta voidaan edetä, tarvitaan seuraavaa:**
- TFDA:n/valmistajan pakkausseloste (varoitukset, vasta-aiheet, lääkkeiden väliset yhteisvaikutukset) — tällä hetkellä Esto per DG001
- Vahvistettu alkuperäinen käyttöaihde ja vaikutusmekanismi DrugBankista tai sääntelylähteestä — DG002
- Prekliininen näyttö siitä, että systeeminen annos saavuttaa Nrf2-reitin aktivaation linssissa tai verkkokalvotudoksessa
- Kaikki in vitro- tai eläinkokeista saadut tiedot antioksidantin vaikutuksesta diabeettisen kataraktan tai retinopatian malleissa
- Antoreitin toteutettavuusarviointi oftalmologisen kohteen saavuttamiselle

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

