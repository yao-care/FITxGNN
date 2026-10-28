---
layout: default
title: Pentosan Polysulfate
parent: Pelkkä mallin ennuste (L5)
nav_order: 340
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Pentosan Polysulfate: ennustettu uusi käyttöaihe Primaarinen verihiutaleiden vapautumishäiriö (primary release disorde… (näytön taso L5). Alkuperäinen käyttöaihe: Interstitiaalinen kystiitti"
monitor_inn: "Pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
---

# Pentosan Polysulfate
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

## Pentosaanipolysulfaatti: Primaarinen verihiutaleiden vapautumishäiriö
{: .text-alpha }

## Yhteenveto

Pentosaanipolysulfaatti on rikkipitoinen polysakkaridi, jota on alun perin käytetty interstitiaalisen kystiitin hoitoon.
TxGNN-malli ennustaa sen voivan tehota **primaariseen verihiutaleiden vapautumishäiriöön**, mutta ennustetta tukevat **0 kliinistä tutkimusta** ja **0 julkaisua**. Ennuste perustuu pelkästään laskennalliseen malliin, ja lisäksi lääkkeen verenvuotoriskiä lisäävä vaikutus voi olla ennustetun käyttöaiheen kannalta haitallinen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Interstitiaalinen kystiitti |
| Ennustettu uusi käyttöaihe | Primaarinen verihiutaleiden vapautumishäiriö (primary release disorder of platelets) |
| TxGNN-ennustepistemäärä | 0,9971 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Lääkkeen alkuperäistä vaikutusmekanismia koskevia tietoja ei ole tällä hetkellä saatavilla. Tunnetun tiedon perusteella pentosaanipolysulfaatti on rikkipitoinen polysakkaridi, jolla on heikko hepariinin kaltainen antikoagulanttivaikutus. Se vaikuttaa myös fibrinolyysiin ja verihiutaleisiin liittyviin reitteihin. Tämä voisi teoriassa vaikuttaa verihiutaleiden toimintaan, mutta vaikutuksen suunta on epäselvä.

Interstitiaalinen kystiitti ja verihiutaleiden vapautumishäiriö ovat lääketieteellisesti hyvin kaukana toisistaan. Verihiutaleiden vapautumishäiriö on verenvuotohäiriö, joten antikoagulanttivaikutusta omaava lääke voi pahentaa verenvuototaipumusta sen sijaan, että se auttaisi.

Ennuste perustuu siis vain korkeaan TxGNN-pistemäärään, eikä sitä ole validoitu.

### Muut mallin ennustamat käyttöaiheet

| Sija | Ennustettu käyttöaihe | TxGNN-pistemäärä | Näytön taso | Huomio |
|------|------|------|------|------|
| 2 | Glanzmannin trombasteenia | 0,9965 | L5 | Sairaudessa verihiutaleiden integriini αIIbβ3 (GPIIb/IIIa) on puutteellinen tai toimimaton. Lääkkeellä ei ole tunnettua mekanismia vian korjaamiseksi, ja sen antikoagulanttivaikutus voi lisätä verenvuotoriskiä. |
| 3 | Pseudo-von Willebrandin tauti | 0,9962 | L5 | Verihiutaleiden GPIbα:n toimintaa lisäävä vika. Rikkipitoiset polysakkaridit voivat teoriassa sitoutua von Willebrand -tekijään, mutta hyödystä ei ole näyttöä ja verenvuototaipumus voi pahentua. |

---

## Kliininen näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004246 | Elmiron | – | Interstitiaalinen kystiitti (peruutettu) |

---

## Turvallisuusnäkökohdat

Valmistekohtaisia varoituksia ja vasta-aiheita ei ollut saatavilla, joten niiden osalta on tutustuttava valmisteyhteenvetoon.

- **Tietämysgraafiin perustuvat mahdolliset vasta-aihesairaudet** (TxGNN-tietämysgraafi, ei valmisteyhteenvedon teksti): maksasairaus, sappirakon sairaus, trombosytopenia, veren hyytymishäiriö, hemofilia sekä hepariini-indusoitu trombosytopenia.
- **Lääkeyhteisvaikutukset**: tietoja löytyi yhteensä 58 yhteisvaikutuksesta. Alla on esimerkkejä keskivaikeiksi luokitelluista yhteisvaikutuksista (lähde: DDInter), jotka liittyvät pääosin verenvuotoriskin kasvuun:
  - Antikoagulantit ja trombolyytit: varfariini, apiksabaani, edoksabaani, betriksabaani, daltepariini, alteplaasi, anistreplaasi, antitrombiini III, bivalirudiini, defibrotidi
  - Verihiutaleiden estäjät: asetyylisalisyylihappo, klopidogreeli, kangrelori, silostatsoli, dipyridamoli, absiksimabi
  - Muut: kaplasitsumabi, ibritumomabitiuksetaani, tositumomabi (myös I-131)

Koska lääkkeellä on antikoagulanttivaikutus ja tietämysgraafi liittää sen verenvuotohäiriöihin, turvallisuusriski on erityisen merkittävä juuri ennustetuissa verenvuotohäiriöissä.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-mallin korkeaan pistemäärään (näytön taso L5), eikä kliinistä tai kirjallisuusnäyttöä ole. Lääkkeen antikoagulanttivaikutus voi lisäksi pahentaa ennustettuja verenvuotohäiriöitä, ja Suomessa ainoa myyntilupa on peruutettu.

**Jatkotoimien edellytyksenä on:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivustolta, sillä turvallisuusarviointia ei voida ilman niitä viedä eteenpäin
- Vaikutusmekanismitietojen täydentäminen (esim. DrugBankista)
- Prekliinisten tai mekanististen tutkimusten tekeminen verihiutaleiden toiminnasta ja verenvuotoriskistä
- Selvitys antikoagulanttivaikutuksen vaikutuksesta ennustettuihin verenvuotohäiriöihin
- Lääkemuotojen ja antoreittien yhteensopivuuden arviointi
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

