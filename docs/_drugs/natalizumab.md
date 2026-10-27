---
layout: default
title: Natalizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 297
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Natalizumab: ennustettu uusi käyttöaihe Keuhkoputkentulehdus (bronchitis) (näytön taso L5). Alkuperäinen käyttöaihe: Aaltoileva multippeliskleroosi (relapsoiva-remittoiva MS) ja multippe…"
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
---

# Natalizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

## Natalitsumabi: Multippeliskleroosista keuhkoputkentulehdukseen
{: .text-alpha }

## Yhden lauseen yhteenveto

Natalitsumabi on monoklonaalinen vasta-aine, jota on alun perin käytetty aaltoilevaoireisen multippeliskleroosin (MS-taudin) hoitoon.
TxGNN-malli ennustaa sen voivan tehota **keuhkoputkentulehdukseen**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.
Ennuste perustuu pelkästään mallilaskentaan, ja sitä on pidettävä todennäköisenä tietoverkon artefaktina.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Aaltoileva multippeliskleroosi (relapsoiva-remittoiva MS) ja multippeliskleroosi |
| Ennustettu uusi käyttöaihe | Keuhkoputkentulehdus (bronchitis) |
| TxGNN-ennusteen pistemäärä | 99,46 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 2 (molemmat peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Natalitsumabi salpaa alfa4-integriinin välittämää valkosolujen kulkeutumista tulehduskohtiin. MS-taudissa tämä estää tulehdussolujen pääsyn keskushermostoon. Teoriassa sama mekanismi voisi vaikuttaa myös hengitysteiden tulehdukseen.

Yksityiskohtaista vaikutusmekanismitietoa ei kuitenkaan ole tämän raportin aineistossa saatavilla. Keuhkoputkentulehdus on useimmiten infektioperäinen tai itsestään paraneva, ja systeeminen immuunivaste-estävä hoito lisäisi infektioriskiä. Ennuste on siksi todennäköisesti verkkopohjainen artefakti eikä aidosti hoidollinen löydös.

---

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

---

## Tietoa Suomen markkinoista

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005752 | Tyruko (Sandoz GmbH), peruutettu | – | Aaltoileva multippeliskleroosi; multippeliskleroosi |
| EMEA/H/C/000603 | Tysabri (Biogen Netherlands B.V.), peruutettu | – | Multippeliskleroosi |

---

## Turvallisuushuomioita

- **Tietoverkon vasta-aiheet:** Tietämysverkon (PrimeKG) mukaan natalitsumabiin liittyy vasta-aihemerkintä **progressiiviselle multifokaaliselle leukoenkefalopatialle (PML)**. Tämä ei perustu valmisteyhteenvedon tekstiin.
- **Lääkeyhteisvaikutukset:** Yhteisvaikutuksia löytyi yhteensä 100. Merkittäviä (Major) ovat mm.:
  - kortikosteroidit: hydrokortisoni, triamsinoloni, deksametasoni, betametasoni, budesonidi, prednisoloni ja prednisoni
  - radiofarmaseuttiset ja vasta-ainevalmisteet: jobenguaani (I-131), ibritumomabitiuksetaani, tositumomabi (myös I-131)
  - muut: levamisoli, trimetreksaatti, merkaptopuriini
  - Kohtalainen (Moderate): naltreksoni
  - Vähäisiä (Minor): sinkkiyhdisteet (sulfaatti, asetaatti, glukonaatti, kloridi)

Muiden ennustettujen käyttöaiheiden kirjallisuus (psoriaasi, parapsoriaasi, akuutti lichenoidi pityriaasi) viittaa lisäksi siihen, että natalitsumabi voi aiheuttaa tai pahentaa ihomuutoksia. Psoriaasista on raportoitu sekä paranemista (PMID 33589543) että natalitsumabin aiheuttamia tai pahentamia tapauksia.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelu:**
- Korkeasta TxGNN-pistemäärästä (0,995) huolimatta ennusteelle ei ole kliinistä eikä kirjallista tukea (taso L5). Lääkkeen PML-riski ja infektioalttiuden lisääntyminen tekevät riski-hyötysuhteesta epäedullisen keuhkoputkentulehduksessa. Lisäksi Suomessa kaikki myyntiluvat on peruutettu.

**Eteneminen edellyttäisi seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta ja läpikäynti Fimeasta (estää tällä hetkellä turvallisuusseulonnan)
- Vaikutusmekanismitietojen täydentäminen (esim. DrugBankista)
- Prekliinisen tai kliinisen näytön löytäminen keuhkoputkentulehduksesta
- Arvio siitä, onko tarkasteltavaksi järkevämpää valita jokin muu ennustettu käyttöaihe, jolle löytyy kirjallisuutta
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

