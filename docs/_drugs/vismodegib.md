---
layout: default
title: Vismodegib
parent: Pelkkä mallin ennuste (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vismodegib: ennustettu uusi käyttöaihe Laajasti nodulaarinen medulloblastooma (näytön taso L5). Alkuperäinen käyttöaihe: Tyvisolusyöpä (Carcinoma, Basal Cell)"
monitor_inn: "VISMODEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "prostate cancer/brain cancer susceptibility", "Brenner tumor", "prostate leiomyoma", "benign neoplasm of sweat gland"]
---

# Vismodegib
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

# Vismodegibi: tyvisolusyövästä laajasti nodulaariseen medulloblastoomaan

## Yhden lauseen yhteenveto

Vismodegibi on suun kautta otettava Hedgehog-signalointireitin estäjä, jota on alun perin käytetty tyvisolusyövän (basaliooman) hoitoon. TxGNN-malli ennustaa sen voivan tehota **laajasti nodulaariseen medulloblastoomaan**. Tälle ennusteelle ei kuitenkaan löydy **yhtään kliinistä tutkimusta eikä julkaisua**, joten se perustuu vain mallin laskennalliseen pisteytykseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Tyvisolusyöpä (Carcinoma, Basal Cell) |
| Ennustettu uusi käyttöaihe | Laajasti nodulaarinen medulloblastooma |
| TxGNN-ennustepistemäärä | 99,93 % |
| Näytön taso | L5 (vain mallin ennuste) |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on järkevä?

Vismodegibi sitoutuu Smoothened-reseptoriin (SMO) ja estää Hedgehog-signalointireitin. Reitin poikkeava aktivoituminen on tyvisolusyövän keskeinen kasvunajuri. Tarkempia mekanismitietoja ei tässä aineistossa ole saatavilla, joten mekanismikuvaus perustuu yleisesti tunnettuun vaikutustapaan.

Medulloblastooman SHH-alaryhmä on Hedgehog-ohjautuva. Nodulaariset ja desmoplastiset variantit ovat rikastuneet SHH-aktivaatiolle, joten ennuste on mekanistisesti uskottava. Tyvisolusyövän ja medulloblastooman yhteinen tekijä on siis Hedgehog-reitin yliaktiivisuus.

Yhteys perustuu kuitenkin vain TxGNN-pisteytykseen. Tästä kohteesta ei ole aineistossa kokeellista eikä kliinistä näyttöä. Aiempi lasten medulloblastoomatyö ei myöskään sisälly kootun aineiston tietoihin, joten se pitäisi tarkistaa erikseen.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole tähän käyttöaiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole tähän käyttöaiheeseen liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002602 | Erivedge (Roche Registration GmbH) | Ei ilmoitettu | Tyvisolusyöpä (peruutettu) |

---

## Sytotoksisuus

Vismodegibi on syöpälääke, ja se kuuluu kohdennettuihin hoitoihin (Hedgehog/SMO-estäjä).

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (Hedgehog-reitin estäjä), ei perinteinen sytostaatti |
| Luuydinsuppression riski | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksettavuusluokitus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurattavat parametrit | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Käsittelysuojaus | Noudata sytotoksisten lääkkeiden käsittelyohjeita ja valmisteyhteenvedon ohjeita |

---

## Turvallisuushuomiot

**Lääkeaineyhteisvaikutukset:** Yhteisvaikutuksia on tunnistettu yhteensä 56. Aineistossa oli tarkasteltavana 20, joista:

- **Kohtalainen:** klaritromysiini.
- **Lievät:** mahalaukun happamuutta vähentävät lääkkeet, kuten protonipumpun estäjät (omepratsoli, esomepratsoli, lansopratsoli, pantopratsoli, rabepratsoli, deksylansopratsoli), H2-salpaajat (famotidiini, ranitidiini, simetidiini, nitsatidiini) sekä antasidit (alumiinihydroksidi, kalsiumkarbonaatti, magnesiumyhdisteet, natriumbikarbonaatti, natriumsitraatti, magaldraatti).

Muista turvallisuustiedoista, kuten varoituksista ja vasta-aiheista, katso valmisteyhteenveto. Vismodegibin tiedetään olevan teratogeeninen, ja yleisiä haittavaikutuksia ovat lihaskouristukset, hiustenlähtö ja makuhäiriöt.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-pistemäärään (99,93 %), eikä tukena ole kliinisiä tutkimuksia eikä kirjallisuutta (näytön taso L5).
- Suomessa vismodegibin myyntiluvat on peruutettu, ja turvallisuusprofiili (teratogeenisuus) vaatii huolellista harkintaa.

**Etenemiseksi tarvitaan:**
- Systemaattinen kirjallisuushaku medulloblastoomasta ja vismodegibista, myös lasten aiemmat tutkimukset.
- SHH-alaryhmän molekyylitason varmistus (esim. PTCH1/SMO-mutaatiot).
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden tarkistus Fimean aineistosta.
- Lapsipotilaiden turvallisuuden arviointi (mm. kasvulevyvaikutukset) ja raskauden ehkäisyn riskienhallintasuunnitelma.

**Huomio muista ennusteista:** Samassa ennustelistassa kaksi muuta kohdetta erottuu vahvemman näytön vuoksi:
- **Xeroderma pigmentosum** (näytön taso L4): neljä kirjallisuusviitettä, joista kaksi on vismodegibia koskevia tapausselostuksia, mukaan lukien 8-vuotias lapsi. Vismodegibi hoitaa tällöin kasvaimia (tyvisolusyöpiä), ei taustalla olevaa korjausmekanismin vikaa.
- **Ihosyöpä** (näytön taso L2, suositus Proceed with Guardrails): tuki on pääosin Vaihe 2- ja varhaisvaiheen tutkimuksia sekä hoitosuosituksia, mutta kohde menee suurelta osin päällekkäin alkuperäisen tyvisolusyöpäkäyttöaiheen kanssa, eikä se ole todellista uudelleenkäyttöä. Vaiheen 3 satunnaistettua tutkimusta ei tunnistettu.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

