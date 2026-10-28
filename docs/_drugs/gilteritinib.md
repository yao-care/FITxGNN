---
layout: default
title: Gilteritinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 201
evidence_level: L5
indication_count: 1
monitor_inn: "Gilteritinib"
predicted_indications: ["bulbar polio"]
last_modified_at: 2026-10-27
description: "Gilteritinib: ennustettu uusi käyttöaihe Bulbaarinen polio (bulbar polio) (näytön taso L5). Alkuperäinen käyttöaihe: Leukemia, Myeloid, Acute"
---

# Gilteritinib
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

## Gilteritinibi: FLT3/AXL-tyrosiinikinaasin estäjä → Bulbaarinen polio (bulbar polio)
{: .text-alpha }

## Yhteenveto

Gilteritinibi on FLT3- ja AXL-tyrosiinikinaasien estäjä, jota käytetään FLT3-mutaatiopositiivisen akuutin myeloidisen leukemian hoidossa.
TxGNN-malli ennustaa sen voivan tehota tautiin **bulbaarinen polio (bulbar polio)**.
Ennusteen tueksi ei ole tässä raportissa käytettyjen tietojen mukaan **yhtään kliinistä tutkimusta eikä julkaisua**, joten ennuste perustuu pelkästään mallin laskemaan pistemäärään.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Leukemia, Myeloid, Acute |
| Ennustettu uusi käyttöaihe | Bulbaarinen polio (bulbar polio) |
| TxGNN-ennustepistemäärä | 0,9910 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odotus) |

---

## Miksi ennuste voisi olla perusteltu?

Gilteritinibin vaikutusmekanismitiedot eivät ole saatavilla kootuissa tiedoissa. Farmakologiatietojen mukaan lääke estää FLT3-kinaasia (villityypin FLT3:n IC50 noin 5 nM, FLT3-ITD-mutaatioilla alle 2 nM) sekä useita muita reseptorityrosiinikinaaseja, kuten AXL, MERTK, NTRK1, ALK, ROS1, LTK ja RET.

Bulbaarinen polio on poliovirusinfektio, joka vaurioittaa aivorungon motorisia hermosoluja. Tunnettua biologista reittiä FLT3- tai AXL-eston ja poliovirusreplikaation tai bulbaaristen motoneuronien suojan välillä ei ole osoitettu. AXL:n on esitetty osallistuvan joidenkin muiden virusten soluunmenoon tai immuunipakoon, mutta poliovirukselle tätä ei ole osoitettu, joten yhteys olisi spekulatiivinen.

Pistemäärä 0,9910 on mallin tuottama ennuste, eikä sitä tue kliininen tai kirjallisuusnäyttö.

---

## Kliininen tutkimusnäyttö

Tähän tautiin ei ole tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Aiheeseen liittyvää kirjallisuutta ei ole tällä hetkellä saatavilla.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004752 | Xospata | – | Akuutti myeloidinen leukemia |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokka | Kohdennettu hoito (tyrosiinikinaasin estäjä) |
| Luuydinsuppression riski | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Oksettavuusluokka | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Seurattavat parametrit | Verenkuva, maksa- ja munuaisarvot (yleinen seurantasuositus; tarkennus valmisteyhteenvedosta) |
| Käsittelysuojaus | Noudatettava sytostaattien käsittelyohjeita; katso valmisteyhteenveto |

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset**: Farmakologiatietojen mukaan gilteritinibi sitoutuu useisiin reseptorityrosiinikinaaseihin (FLT3, NTRK1, AXL, MERTK, LTK, ALK, ROS1, RET). Nämä ovat kohdevaikutuksia, eivät kliinisesti luokiteltuja yhteisvaikutuksia muiden lääkkeiden kanssa.

Lisäksi mallin perustelujen mukaan gilteritinibi on luuydintä lamaava ja immuunijärjestelmää heikentävä syöpälääke, joten sen käyttö aivojen virusinfektiossa voisi aiheuttaa turvallisuusriskejä. Tarkemmat varoitukset ja vasta-aiheet on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odotus)**

**Perustelut:**
- Ennuste perustuu pelkkään mallin pistemäärään (0,9910), eikä sille ole kliinistä tai kirjallisuusnäyttöä eikä uskottavaa mekanistista yhteyttä. Näytön taso on L5. Lisäksi lääkkeen myelosuppressiivinen ja immuunijärjestelmää heikentävä luonne on riski aktiivisessa viruksen aiheuttamassa hermostoinfektiossa.

**Eteenpäin siirtymiseksi tarvitaan:**
- Vaikutusmekanismia koskevat tiedot sekä mekanistinen perustelu FLT3/AXL-eston ja poliovirusinfektion välille
- Prekliiniset tutkimukset (esim. poliovirusreplikaatio solumalleissa AXL/FLT3-eston yhteydessä)
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden läpikäynti
- Turvallisuusarvio hermostoinfektioiden potilasryhmälle
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

