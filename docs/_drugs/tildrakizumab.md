---
layout: default
title: Tildrakizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 437
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "TILDRAKIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "drug-induced osteoporosis"]
description: "Tildrakizumab: ennustettu uusi käyttöaihe Vaikea ei-proliferatiivinen diabeettinen retinopatia (severe nonproliferative diabetic retinopathy) (näytön taso L5). Alkuperäinen käyttöaihe: Psoriasis"
---

# Tildrakizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

Tildrakitsumabi: Psoriaasista vaikeaan ei-proliferatiiviseen diabeettiseen retinopatiaan

## Yhden lauseen yhteenveto

Tildrakitsumabi on anti-IL-23 p19 -monoklonaalinen vasta-aine, jota on alun perin käytetty **psoriaasin** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **vaikeaan ei-proliferatiiviseen diabeettiseen retinopatiaan**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Näyttö perustuu pelkästään mallin ennusteeseen.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Psoriasis |
| Ennustettu uusi käyttöaihe | Vaikea ei-proliferatiivinen diabeettinen retinopatia (severe nonproliferative diabetic retinopathy) |
| TxGNN-ennustepistemäärä | 0.9963 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Tämän raportin tietoihin ei sisälly tildrakitsumabin tarkkaa vaikutusmekanismitietoa. Tiedossa on, että tildrakitsumabi on anti-IL-23 p19 -vasta-aine, jonka teho psoriaasissa on osoitettu. Mekanistisesti sen voidaan ajatella soveltuvan myös tulehdusvälitteisiin sairauksiin.

Ehdotettu yhteys on epäsuora. IL-23/IL-17-akselin tulehdussytokiinien on esitetty osallistuvan diabeettiseen mikrovaskulaariseen sairauteen ja verkkokalvon tulehdukseen. Tämä on kuitenkin vain TxGNN-tietämysgraafin ennuste, eikä sitä tue yksikään haettu tutkimus tai julkaisu.

Lisäksi suuri vasta-ainemolekyyli läpäisee silmän kudokset huonosti systeemisen annostelun jälkeen. Mahdollinen vaikutus verkkokalvoon vaatisi lasiaisensisäisen tai muun annostelutavan validoinnin. Vakiintuneet anti-VEGF- ja kortikosteroidihoidot asettavat uudelle ehdokkaalle korkean rimman.

### Muut ennustetut käyttöaiheet

| Sija | Käyttöaihe | TxGNN-pistemäärä | Näytön taso | Huomio |
|---|---|---|---|---|
| 2 | Diabeettinen retinopatia | 0,9953 | L5 | Sama perustelu kuin sijalla 1; ei tutkimuksia eikä julkaisuja |
| 3 | Diabeettinen kaihi | 0,9921 | L5 | Selvää mekanistista yhteyttä ei ole; todennäköisesti graafin läheisyydestä johtuva artefakti. Leikkaus on ratkaiseva hoito |
| 4 | Lääkkeiden aiheuttama osteoporoosi | 0,9920 | L5 | IL-23/IL-17 vaikuttaa luun uudelleenmuodostukseen, joten yhteys on uskottava mutta epäsuora; vain hypoteesi prekliiniseen tutkimukseen |

---

## Kliiniset tutkimukset

Ei tällä hetkellä aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoista

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004514 | Ilumetri | – | Psoriaasi |

Myyntilupa on tilassa "peruutettu", eikä voimassa olevia myyntilupia ole.

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset** (kyselyn perusteella yhteensä 78 yhteisvaikutusta; alla esimerkkejä saaduista tuloksista):

- **Merkittävät (Major):** adalimumabi, barisitinibi, sertolitsumabipegoli, kladribiini. Näihin liittyy lähinnä immunosuppression additiivinen riski.
- **Kohtalaiset (Moderate):** esim. roflumilasti, takrolimuusi, atsatiopriini, siklosporiini, anakinra, kanakinumabi, alemtutsumabi, denosumabi, alefasepti sekä tietyt rokotteet (mm. jäykkäkouristustoksoidi, pernaruttorokote, elävä koleravasta-ainerokote).
- **Vähäiset (Minor):** sinkkivalmisteet (sulfaatti, asetaatti, glukonaatti, kloridi).

Pakkausselosteen varoituksia ja vasta-aiheita ei ollut käytettävissä. Tarkista turvallisuustiedot valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennusteen pistemäärä on korkea (0,9963), mutta näyttö on tasoa L5: ei kliinisiä tutkimuksia, ei julkaisuja eikä prekliinistä aineistoa. Lisäksi systeemisen vasta-aineen silmäpenetraatio on rajallinen ja vakiintuneet hoidot ovat vahvoja. Myyntilupakin on Suomessa peruutettu.

**Jatkaminen edellyttää seuraavaa:**
- Vaikutusmekanismin (MOA) tietojen täydentäminen
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kerääminen turvallisuusseulontaa varten (estävä tietopuute)
- Prekliiniset tiedot IL-23/IL-17-akselin roolista diabeettisessa retinopatiassa
- Annostelureitin ja silmäpenetraation arviointi (esim. lasiaisensisäinen anto)
- Kirjallisuushaku ja kliinisten tutkimusten rekisterihaku uudelleen
- Arvio lääkkeen markkinatilanteesta ja saatavuudesta Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

