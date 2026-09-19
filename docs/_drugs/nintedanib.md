---
layout: default
title: Nintedanib
parent: Kohtalainen näyttö (L3-L4)
nav_order: 263
evidence_level: L4
indication_count: 3
---

# Nintedanib
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **3** kpl
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

# Nintedanibi: idiopaattisesta keuhkojen fibroosista dermatofibrosarkooma protuberansiin

> **Huomautus tietojen alkuperästä:** Todistenippu ei sisällä lähdettyjä alkuperäisen indikaation tai MOA-tietoja (`original_indications: []`, `original_moa: "[Data Gap]"`, merkitty DG001/DG002. Tässä mainittu alkuperäinen indikaatio (idiopaattinen keuhkojen fibrooosi) heijastaa nintedanibin hyvin vakiintunutta julkista lääkkeen luokittelua ja vaatii vahvistamisen ensisijaisesta lähteestä (DrugBank/Fimean merkintä) ennen käyttöä muodollisessa turvallisuusarvioinnissa.

## Yhden lauseen yhteenveto

Nintedanibi on moneksi kohteeksi vaikuttava tyrosiinkinaasin estäjä, joka tunnetaan yleisesti sen käytöstä fibroottisissa keuhkosairauksissa. TxGNN-malli ennustaa, että se saattaa olla tehokas **dermatofibrosarkooma protuberansiin**, mutta tätä suuntaa tukee tällä hetkellä vain **yksi mekanismiin liittyvä julkaisu** ja **ei rekisteröityjä kliinisiä tutkimuksia**.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu nykyisessä todistenipussa (estävä tietovaje — katso DG001) |
| Ennustettu uusi indikaatio | Dermatofibrosarcoma protuberans |
| TxGNN-ennustepistemäärä | 99.15% |
| Todisteen taso | L4 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia nintedanibin vaikutusmekanismin tietoja ei ole saatavilla tässä todistenipussa (DG002). Yleisesti tunnetun farmakologian perusteella nintedanibi on kolmoiskulmakiinaasi-estäjä, joka kohdennetaan VEGFR:ään, FGFR:ään ja PDGFR:ään, ja sen tehokkuus fibroottisissa keuhkosairauksissa on vakiintunut laajemmassa kirjallisuudessa — mutta tätä ei ole vahvistettu tässä nippussa lähteellä tuetulla asiakirjalla.

Ainoa tukeva julkaisu (PMID 29408302) on pienimolekyylisten PDGFR-estäjien farmakologinen katsaus pahanlaatuisissa taudeissa. Dermatofibrosarcoma protuberans on kasvain, jota luonnehtii COL1A1–PDGFB-geenifuusio, joka aiheuttaa jatkuvan PDGFR-signalointireitin aktivaation. Jos nintedanibin PDGFR-inhibiittinen aktiivisuus vahvistetaan, on uskottava mekanistinen perustelu PDGFR-ohjautuvissa sarkoomeissa, kuten DFSP:ssa ja liposarkooomassa olevan aktiivisuuden kannalta — mikä on johdonmukainen sen kanssa, että kaikki kolme TxGNN:n eniten sijoitettua ennustetta ovat pehmeän kudoksen sarkoomat.

Tätä mekanistista yhteyttä tukee tällä hetkellä vain luokan tason kirjallisuus, ei lääkekohtaiset tai tautikohtaiset tutkimukset, ja sitä tulee käsitellä hypoteesin tuottavana pikemminkin kuin vahvistavana.

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|------|--------|---------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Katsaus | Pharmacological Research | Arvioi pienimolekyylisiä PDGFR-estäjiä pahanlaatuisissa taudeissa; kuvailee PDGF/PDGFR-signalointireittiä, joka on merkityksellinen PDGFR-ohjautuville kasvaimille, kuten DFSP:lle, mikä tukee luokan tasoisilla mekanistisia perusteluja pikemminkin kuin lääkekohtaisia tehokkuustietoja |

## Suomen markkinatiedot

Nintedanibia ei ole tällä hetkellä markkinoilla Suomessa; todistenipussa ei ole saatavilla lupamerkintöjä (`total_licenses: 0`).

## Turvallisuutta koskevat huomiot

Katso turvallisuustietoja pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelu:**
Ennuste perustuu yksittäiseen luokan tasoiseen mekanismin katsaukseen ilman lääkekohtaisia tai tautikohtaisia kliinisiä tai prekliinisiä tietoja, ilman rekisteröityjä tutkimuksia mille tahansa kolmesta ennustetusta sarkooma-indikaatiosta, ja ilman Suomen markkinoiden läsnäoloa, johon vedota todellisen maailman turvallisuuskokemukseen. Estävä tietovaje (DG001 — TFDA/Fimean pakkausseloste varoitukset ja vasta-aiheet) estää myös pääsyn S1-turvallisuuden esiseulonnan vaiheeseen.

**Jotta voidaan edetä, tarvitaan seuraavaa:**
- TFDA/Fimean pakkausseloste tiedot (varoitukset, vasta-aiheet) DG001:n ratkaisemiseksi ja S1-turvallisuuden esiseulonnan avauksi
- Vahvistettu alkuperäinen indikaatio ja MOA DrugBankista tai hyväksytystä merkinnästä (DG002)
- Lääkekohtaiset prekliiniset tai tapauskohtaiset todisteet (esim. PDGFR-inhibiittinen aktiivisuus vahvistettu nintedanibille DFSP- tai liposarkooma-malleissa)
- Jatkuva kirjallisuuden/tutkimusten seuranta, koska liposarkooomalla ja ovaarisen myksoidisen liposarkooomalla ei ole tällä hetkellä muuta tukea kuin TxGNN-pistemäärä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

