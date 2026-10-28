---
layout: default
title: Lapatinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 246
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "LAPATINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
description: "Lapatinib: ennustettu uusi käyttöaihe Dermatofibrosarcoma protuberans (näytön taso L5). Alkuperäinen käyttöaihe: Breast Neoplasms"
---

# Lapatinib
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

## Lapatinib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## Yhden lauseen yhteenveto

Lapatinibi on kaksoisvaikutteinen EGFR/HER2-tyrosiinikinaasin estäjä, jota on alun perin käytetty rintasyövän hoitoon. TxGNN-malli ennustaa sen voivan tehota **dermatofibrosarkooma protuberansiin (DFSP)**, mutta ennuste perustuu pelkästään laskennalliseen mallinnukseen: tähän suuntaan ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**.

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Breast Neoplasms |
| Ennustettu uusi käyttöaihe | Dermatofibrosarcoma protuberans |
| TxGNN-ennustepistemäärä | 0.9930 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odotetaan) |

## Miksi ennuste voi olla perusteltu?

Lapatinibi estää sekä EGFR- (ErbB1) että HER2-reseptoria (ErbB2), ja sitä käytetään HER2-positiivisessa rintasyövässä. Tämän raportin tarpeisiin koottu aineisto ei sisällä tarkempaa vaikutusmekanismikuvausta, joten mekanistista perustetta ei voida varmentaa toimitetusta datasta.

DFSP on pehmytkudossarkooma, jota ajaa pääasiassa COL1A1-PDGFB-fuusiogeeni, joka aiheuttaa PDGFRB-reseptorin jatkuvan aktivaation. Sitä hoidetaan leikkauksella ja PDGFR-estäjä imatinibilla. Mahdollinen yhteys voisi olla jaettu reseptorityrosiinikinaasien signalointi (EGFR/ERBB:n jatkosignalointireitit, kuten PI3K/AKT ja MAPK) tai läheisyys tietämysgraafissa.

Lapatinibilla ei kuitenkaan ole osoitettua vaikutusta PDGFR:ään, joka on DFSP:n pääasiallinen ajuri. Tämä heikentää ennusteen uskottavuutta merkittävästi, vaikka pistemäärä on korkea.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000795 | Tyverb | – | Rintasyöpä (Breast Neoplasms) |

Myyntilupa on peruutettu (valmistaja Novartis Europharm Limited), eikä Suomessa ole voimassa olevia myyntilupia.

## Sytotoksisuus

| Kohde | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (tyrosiinikinaasin estäjä) |
| Myelosuppression riski | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksettavuusluokitus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurantaparametrit | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja varotoimet |

## Turvallisuusnäkökohdat

- **Tietämysgraafin (PrimeKG) vasta-aihemerkinnät** (eivät perustu valmisteyhteenvedon tekstiin): pitkä QT-oireyhtymä, familiaalinen pitkä QT-oireyhtymä, torsades de pointes, maksan vajaatoiminta, kaliumin puutos, interstitiaalinen keuhkosairaus, lääkeaiheuttama maksavaurio ja sydämen vajaatoiminta.
- **Lääkeyhteisvaikutukset** (100 löydettyä yhteisvaikutusta, alla keskeisimmät):
  - **Merkittävät (Major):** loperamidi, klaritromysiini.
  - **Kohtalaiset (Moderate):** mm. famotidiini, ranitidiini, simetidiini, omepratsoli, rabepratsoli, deksalansopratsoli, deksametasoni, betametasoni, hydrokortisoni, triamsinoloni, budesonidi, aprepitantti, pioglitatsoni, saksagliptiini, bisakodyyli, pikosulfaatti ja polyetyleeniglykoli.

Muuta turvallisuustietoa varten katso valmisteyhteenveto.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Vaikka TxGNN-pistemäärä on korkea (0,9930), ennuste on pelkkä laskennallinen ehdotus ilman kliinisiä tutkimuksia tai julkaisuja (näyttötaso L5). Lapatinibilla ei ole osoitettua vaikutusta DFSP:n pääajuriin PDGFRB:hen, ja DFSP:lle on jo vakiintunut kohdennettu hoito (imatinibi). Lisäksi Suomen myyntilupa on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismitietojen täydentämistä (esim. DrugBankista) ja mekanistisen yhteyden arviointia DFSP:hen
- Prekliinistä näyttöä (esim. DFSP-solulinjat, EGFR/HER2-ekspression ja -signaloinnin tarkastelu kasvaimissa)
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivustolta turvallisuusarviota varten
- Arviota siitä, tuoko lapatinibi lisäarvoa imatinibiin verrattuna, sekä tilanteen selvittämistä, kun valmiste ei ole markkinoilla Suomessa
- Sydän- (QT-aika, sydämen vajaatoiminta), maksa- ja keuhkoturvallisuuden seurantasuunnitelmaa, jos jatkotutkimuksia harkitaan
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

