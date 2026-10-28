---
layout: default
title: Aflibercept
parent: Pelkkä mallin ennuste (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Aflibercept: ennustettu uusi käyttöaihe Esotropia (näytön taso L5). Alkuperäinen käyttöaihe: Kostea silmänpohjan ikärappeuma, makulaturvotus…"
monitor_inn: "AFLIBERCEPT"
predicted_indications: ["esotropia"]
---

# Aflibercept
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

## Aflibersepti: Esotropia
{: .text-alpha }

## Yhden lauseen yhteenveto

Aflibersepti on VEGF:n (verisuonten endoteelikasvutekijän) estäjä, jota on alun perin käytetty silmänpohjan kosteaan ikärappeumaan, makulaturvotukseen ja verkkokalvon laskimotukoksiin sekä (Zaltrap-valmisteena) paksusuolen ja peräsuolen syöpään.
TxGNN-malli ennustaa sen voivan tehota **esotropiaan** (silmien sisäänpäin kääntyminen), mutta ennuste perustuu pelkästään mallilaskentaan: aiheesta ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Kostea silmänpohjan ikärappeuma, makulaturvotus, verkkokalvon laskimotukos, suonikalvon neovaskularisaatio ja diabeteksen komplikaatiot |
| Ennustettu uusi käyttöaihe | Esotropia |
| TxGNN-ennustepisteet | 0.9938 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 14/14) |
| Myyntilupien määrä | 14 (voimassa: 14) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennustetta voidaan pitää järkevänä – vai voidaanko?

Aflibersepti toimii VEGF-A:n, VEGF-B:n ja istukkakasvutekijän (PlGF) loustoimijana ("trap"), ja sitä annetaan silmänsisäisesti verkkokalvon verisuoni- ja uudissuonisairauksiin. Yksityiskohtaista vaikutusmekanismitietoa ei ole tähän raporttiin koottu aineistossa saatavilla, mikä rajoittaa mekanistista arviointia.

Esotropia on silmien asentovirhe, jonka taustalla ovat tyypillisesti hermo-lihasperäiset, taittovirheisiin liittyvät tai kahden silmän yhteisnäön tekijät. Kerätyn aineiston perusteella aflibersepitin ja esotropian välille ei löydy suoraa mekanistista yhteyttä. Korkea pistemäärä (0,9938) tulee TxGNN-mallista (syväoppiminen) ja heijastaa todennäköisesti malliin oppimia yhtäläisyyksiä toisiinsa liittyvien sairauksien välillä, ei biologista perustetta.

VEGF-estäjiä on tutkittu silmäsairauksissa, jotka voivat aiheuttaa toissijaisesti kierosilmäisyyttä (esim. keskosen retinopatia), mutta yhteys on epäsuora eikä todista vaikutusta esotropiaan itseensä.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Tietoa Suomen markkinoista

Kaikki 14 myyntilupaa on peruutettu. Valmisteet on lueteltu alla (enintään 5).

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002392 | Eylea | – | Kostea ikärappeuma, makulaturvotus, diabeteksen komplikaatiot, verkkokalvon laskimotukos, suonikalvon neovaskularisaatio |
| EMEA/H/C/002532 | Zaltrap | – | Paksusuolen ja peräsuolen syöpä |
| EMEA/H/C/006339 | Pavblu | – | Kostea ikärappeuma, makulaturvotus, verkkokalvon laskimotukos, suonikalvon neovaskularisaatio, diabeteksen komplikaatiot |
| EMEA/H/C/006056 | Opuviz | – | Kostea ikärappeuma, makulaturvotus, diabeteksen komplikaatiot, verkkokalvon laskimotukos |
| EMEA/H/C/006150 | Afqlir | – | Kostea ikärappeuma, makulaturvotus, diabeteksen komplikaatiot, verkkokalvon laskimotukos |

---

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 78 yhteisvaikutusta. Merkittäviksi (Major) luokiteltuja ovat esimerkiksi:
  - deferipronin
  - samarium-153-leksidronaamin
  - adalimumabin
  - barisitinibin
  - sertolitsumabipegolin
  - kladribiinin
  - klotsapiinin kanssa.

  Kohtalaisia (Moderate) ovat mm. strontiumkloridi Sr-89, roflumilasti, kloramfenikoli, tsidovudiini, atsatiopriini, anakinra, alemtutsumabi ja kanakinumabi.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat koottuna aineistosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Ennuste perustuu vain TxGNN-malliin (L5), eikä kliinisiä tutkimuksia tai julkaisuja ole. Suoraa mekanistista yhteyttä esotropiaan ei ole tunnistettu, ja lisäksi kaikki Suomen myyntiluvat on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivustolta (estää turvallisuusseulonnan jatkamisen)
- Vaikutusmekanismitietojen täydentämistä (esim. DrugBank)
- Kirjallisuushakua anti-VEGF-hoidoista kierosilmäisyyteen ja keskosen retinopatiaan
- Prekliinistä tai mekanistista näyttöä VEGF:n roolista esotropiassa
- Antoreittien yhteensopivuuden ja lääkemuotojen arviointia
- Myyntilupatilanteen selvittämistä, koska voimassa olevia lupia ei ole
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

