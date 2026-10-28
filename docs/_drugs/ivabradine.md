---
layout: default
title: Ivabradine
parent: Pelkkä mallin ennuste (L5)
nav_order: 239
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Ivabradine: ennustettu uusi käyttöaihe Hypertrikoosi (hypertrichosis) (näytön taso L5). Alkuperäinen käyttöaihe: Angina pectoris"
monitor_inn: "IVABRADINE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ivabradine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

## Ivabradiini: Angina pectoriksesta ja sydämen vajaatoiminnasta hypertrikoosiin
{: .text-alpha }

## Yhden lauseen yhteenveto

Ivabradiini on sydänlääke, jota on käytetty rasitusrintakivun (angina pectoris) ja sydämen vajaatoiminnan hoitoon.
TxGNN-malli ennustaa sen voivan tehota **hypertrikoosiin** (liialliseen karvankasvuun), mutta ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**.
Ennuste perustuu pelkästään verkostopohjaiseen laskennalliseen päättelyyn.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Angina pectoris; sydämen vajaatoiminta |
| Ennustettu uusi käyttöaihe | Hypertrikoosi (hypertrichosis) |
| TxGNN-ennustepistemäärä | 0,9979 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 5/5) |
| Myyntilupien määrä | 5 (voimassa: 5) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Ivabradiini estää HCN-kanavia (sydämen sinussolmun If-virta eli ns. "funny current"), mikä hidastaa sydämen sykettä. Tarkempaa vaikutusmekanismitietoa ei tällä hetkellä ole saatavilla tähän raporttiin koottua aineistoa varten.

Teoreettisesti HCN-kanavia, mukaan lukien HCN4, esiintyy myös karvatupen soluissa, ja ne voisivat vaikuttaa follikkelin ärtyvyyteen ja kasvusykliin. Tämä yhteys on kuitenkin vain hypoteesi. Korkea TxGNN-pistemäärä (0,9979) on verkostopohjainen ennuste, jolle ei löydy tukea tutkimuksista tai kirjallisuudesta.

Alkuperäisen käyttöaiheen (sydänsairaudet) ja ennustetun käyttöaiheen (kosmeettinen/ihon liitteisiin liittyvä tila) välillä ei ole selvää kliinistä samankaltaisuutta. Lisäksi syketta alentavan lääkkeen käyttö ei-sydänperäiseen, kosmeettiseen tilaan johtaisi epäedulliseen hyöty-haittasuhteeseen (bradykardia, fosfeenit eli valoilmiöt, eteisvärinä).

Muut ennustetut käyttöaiheet (esim. Ambras-tyypin synnynnäinen yleistynyt hypertrikoosi, hammas- ja parodontiumpoikkeavuuksiin liittyvät oireyhtymät, Dandy-Walker-oireyhtymä, perinnöllinen hiusvarren poikkeavuus ja nefrogeeninen antidiureesin epäasianmukaisen erityksen oireyhtymä) ovat samalla tavoin ilman tutkimusnäyttöä, eikä niille ole tunnistettavissa uskottavaa mekanismia.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

Kaikki viisi myyntilupaa on peruutettu.

| Myyntiluvan numero | Tuotenimi | Valmistaja | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000598 | Corlentor | Les Laboratoires Servier | Angina pectoris; sydämen vajaatoiminta |
| EMEA/H/C/000597 | Procoralan | Les Laboratoires Servier | Angina pectoris; sydämen vajaatoiminta |
| EMEA/H/C/004241 | Ivabradine Accord | Accord Healthcare S.L.U. | Angina pectoris; sydämen vajaatoiminta |
| EMEA/H/C/004187 | Ivabradine Anpharm | Anpharm Przedsiębiorstwo Farmaceutyczne S.A. | Angina pectoris; sydämen vajaatoiminta |
| EMEA/H/C/004117 | Ivabradine Zentiva | Zentiva, k.s. | Angina pectoris; sydämen vajaatoiminta |

---

## Turvallisuusnäkökohdat

**Lääkeinteraktiot:** Tietokannasta löytyi yhteensä 100 interaktiota, joista alla on lueteltu keskeisiä esimerkkejä (20 ensimmäistä).

- **Merkittävät (Major):** aprepitantti, klaritromysiini, dolasetroni, palonosetroni, sisapridi, klotrimatsoli, graniseetroni, levofloksasiini, ondansetroni, papaveriini, kobisistaatti.
- **Kohtalaiset (Moderate):** famotidiini, ranitidiini, deksametasoni, simetidiini, metreleptiini, mikonatsoli, nitsatidiini, ranitidiinibismutsitraatti, troglitatsoni.

Useat merkittävät interaktiot koskevat lääkkeitä, jotka vaikuttavat QT-aikaan tai CYP3A4-entsyymin kautta, joten yhteiskäytössä on syytä olla erityisen varovainen.

Muista turvallisuustiedoista (varoitukset, vasta-aiheet) tarkemmat tiedot löytyvät valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu ainoastaan TxGNN-mallin verkostopäättelyyn (näytön taso L5), eikä siitä ole kliinisiä tutkimuksia eikä julkaisuja. Lisäksi sykettä hidastavan lääkkeen riski-hyötysuhde ei-sydänperäisessä kosmeettisessa tilassa on epäedullinen, ja kaikki Suomen myyntiluvat on peruutettu.

**Eteneminen edellyttäisi seuraavaa:**
- Vaikutusmekanismin (MOA) tietojen täydentäminen.
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kerääminen ja jäsentäminen (turvallisuusseulonnan edellytys).
- Prekliininen näyttö HCN-kanavien (esim. HCN4) roolista karvatupen biologiassa.
- Arvio reittien yhteensopivuudesta (esim. paikallinen käyttö systeemisen sijaan), jotta sydänhaitat voitaisiin välttää.
- Myyntilupatilanteen selvittäminen Suomessa.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

