---
layout: default
title: Pegfilgrastim
parent: Pelkkä mallin ennuste (L5)
nav_order: 334
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Pegfilgrastim: ennustettu uusi käyttöaihe Vaikea ei-proliferatiivinen diabeettinen retinopatia (toissijaisesti… (näytön taso L5). Alkuperäinen käyttöaihe: Neutropenia, kuumeinen neutropenia…"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

## Pegfilgrastiimi: Neutropeniasta vaikeaan ei-proliferatiiviseen diabeettiseen retinopatiaan
{: .text-alpha }

## Yhteenveto

Pegfilgrastiimi on pitkävaikutteinen kasvutekijä (G-CSF), jota käytetään alun perin neutropenian, kuumeisen neutropenian ja solunsalpaajahoidon aiheuttaman kuumeisen neutropenian hoitoon syöpäpotilailla.
TxGNN-malli ennustaa sen voivan tehota **vaikeaan ei-proliferatiiviseen diabeettiseen retinopatiaan**, mutta ennustetta tukevat vain mallin laskema pistemäärä: **kliinisiä tutkimuksia ei ole lainkaan ja kirjallisuutta ei ole löytynyt**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Neutropenia, kuumeinen neutropenia, solunsalpaajahoidon aiheuttama kuumeinen neutropenia (syöpäpotilaat) |
| Ennustettu uusi käyttöaihe | Vaikea ei-proliferatiivinen diabeettinen retinopatia (toissijaisesti diabeettinen retinopatia yleisesti) |
| TxGNN-ennustepistemäärä | 99,89 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 11 (kaikki peruutettuja, voimassa olevia 0) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Tässä raportissa käytettävissä olevassa aineistossa ei ole yksityiskohtaista vaikutusmekanismitietoa. Tiedetään, että pegfilgrastiimi on pitkävaikutteinen G-CSF, joka lisää neutrofiilien tuotantoa ja mobilisoi hematopoieettisia kantasoluja. Sen teho neutropeniassa on osoitettu, mutta mekanistista yhteyttä diabeettiseen retinopatiaan ei ole osoitettu.

Spekulatiivinen yhteys voisi olla endoteelin progenitorisolujen mobilisaatio verisuonten korjaamiseksi. Toisaalta diabeettisessa retinopatiassa on kyse mikroverisuonivauriosta ja tulehduksesta, ja G-CSF:n aiheuttama neutrofiilien aktivaatio voisi päinvastoin pahentaa verkkokalvon tulehdusta. Korkea pistemäärä (0,999) on pelkkä mallin ennuste, jota ei tue mikään tutkimus. Toinen ennuste, diabeettinen retinopatia (pistemäärä 99,73 %), on todennäköisesti sama signaali kuin vaikea ei-proliferatiivinen muoto.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Myyntilupatiedot Suomessa

Kaikki 11 myyntilupaa on peruutettu. Alla on lupia, joista käyttöaihetieto oli saatavilla, sekä muut keskeiset valmisteet.

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000420 | Neulasta | – | Syöpä, neutropenia, kuumeinen neutropenia, solunsalpaajahoidon aiheuttama kuumeinen neutropenia |
| EMEA/H/C/006739 | Vivlipeg | – | Neutropenia, kuumeinen neutropenia, solunsalpaajahoidon aiheuttama kuumeinen neutropenia, syöpä |
| EMEA/H/C/006407 | Dyrupeg | – | Neutropenia, syöpä |
| EMEA/H/C/005085 | Nyvepria | – | – |
| EMEA/H/C/004802 | Ziextenzo | – | – |

---

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ollut käytettävissä, joten ne tulee tarkistaa valmisteyhteenvedosta.

**Lääkkeiden yhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 100 yhteisvaikutusta. Esimerkkejä keskivaikeiksi (Moderate) luokitelluista:
- Paklitakseli
- Merkaptopuriini
- Abemasiklibi
- Atsasitidiini
- Alemtutsumabi
- Aldesleukiini
- Arseenitrioksidi
- Ibritumomabitiuksetaani
- Jobenguaani (I-131)
- Fludeoksiglukoosi (18F)

Useat näistä ovat solunsalpaajia tai sädelääkkeitä, joiden kanssa myelosuppressiivinen hoito ja G-CSF:n ajoitus vaativat huolellista suunnittelua.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-mallin pistemäärään (L5). Kliinisiä tutkimuksia ja julkaisuja ei ole, eikä mekanistista yhteyttä ole osoitettu. G-CSF:n pro-inflammatorinen vaikutus voisi jopa pahentaa verkkokalvon tilaa. Lisäksi kaikki myyntiluvat Suomessa on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismitietojen täydentämistä (esim. DrugBankista)
- Valmisteyhteenvedon turvallisuustietojen (varoitukset, vasta-aiheet) hankkimista Fimean sivustolta
- Prekliinistä näyttöä G-CSF:n vaikutuksesta diabeettisen retinopatian malleissa, mukaan lukien tulehdusriskin arviointi
- Kirjallisuushakua aiheesta sekä reittien ja lääkemuotojen soveltuvuuden arviointia (silmänsisäinen vs. ihonalainen anto)
- Selvitystä siitä, onko valmistetta saatavilla Suomen markkinoilla, koska nykyiset myyntiluvat on peruutettu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

