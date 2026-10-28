---
layout: default
title: Temozolomide
parent: Pelkkä mallin ennuste (L5)
nav_order: 425
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-23
description: "Temozolomide: ennustettu uusi käyttöaihe Cauda equina neoplasm (näytön taso L5). Alkuperäinen käyttöaihe: Glioma"
---

# Temozolomide
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

## Temozolomide: Cauda equina neoplasm
{: .text-alpha }

## Yhteenveto

Temotsolomidi on suun kautta otettava alkyloiva solunsalpaaja, jota käytetään gliooman hoitoon.
TxGNN-malli ennustaa sen voivan tehota **cauda equina -kasvaimeen**.
Tätä suuntaa tukee tällä hetkellä **0 kliinistä tutkimusta** ja **3 julkaisua** (kaikki tapauskertomuksia, joista vain yksi koskee suoraan cauda equinan alueen kasvainta).

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Glioma |
| Ennustettu uusi käyttöaihe | Cauda equina neoplasm |
| TxGNN-ennustepisteet | 99,30 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 5/5) |
| Myyntilupien määrä | 5 (voimassa: 5) |
| Suositeltu päätös | Hold (odotetaan lisänäyttöä) |

## Miksi ennuste on perusteltu?

Yhteen kootuissa tiedoissa ei ole kuvausta vaikutusmekanismista. Yleisen farmakologisen tiedon mukaan temotsolomidi metyloi DNA:ta (guaniinin O6- ja N7-asemat sekä adeniinin N3-asema), mikä aiheuttaa DNA-vaurioita ja kasvainsolujen apoptoosin. Lääke läpäisee veri-aivoesteen ja on hyväksytty gliooman hoitoon.

Cauda equinan kasvaimet ovat useimmiten myksopapillaarisia ependymoomia, jotka ovat neuroepiteliaalisia kasvaimia ja jakavat osan biologiastaan gliooman kanssa. Mekanistinen yhteys on uskottava, mutta teho riippuisi todennäköisesti MGMT-promoottorin metylaatiostatuksesta, jota aineistossa ei ole raportoitu.

TxGNN-pistemäärä on laskennallinen ennuste eikä kliinistä näyttöä.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Tapauskertomus | European Spine Journal | Temotsolomidilla havaittiin huomattava teho uusiutuneeseen selkärangan myksopapillaariseen ependymoomaan (kasvain syntyy selkäytimen päätesäikeestä); tapauksessa oli toistuvia uusiutumia ja aivo-selkäydinnesteen kautta tapahtunutta leviämistä. |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Tapauskertomus | Medicine | Nenän alueen NUT-karsinooma, jossa toistuvia hoitovasteita monimuotoisessa hoidossa sädehoito mukaan lukien; ei suoraan cauda equina -kasvain. |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Tapauskertomus | Neuro-Chirurgie | Epätyypillinen neuromeningeaalinen kryptokokkoosi lapsella, jota hoidettiin pontiinigliooman vuoksi; ei koske temotsolomidin tehoa cauda equina -kasvaimeen. |

## Myyntiluvat Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/001125 | Temozolomide Accord | – | Gliooma |
| EMEA/H/C/001126 | Temozolomide Teva | – | Gliooma |
| EMEA/H/C/002198 | Temozolomide Sun | – | Gliooma |
| EMEA/H/C/000229 | Temodal | – | Gliooma |
| EMEA/H/C/001124 | Temomedac | – | Gliooma |

## Sytotoksisuus

| Kohde | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Perinteinen sytotoksinen lääke (alkyloiva aine, imidatsotetratsiini) |
| Luuydinsuppression riski | Kohtalainen; neutropenia ja trombosytopenia ovat tunnettuja haittoja |
| Oksentelua aiheuttava vaikutus | Kohtalainen |
| Seurattavat parametrit | Verenkuva (erittelylaskenta mukaan lukien), maksan ja munuaisten toiminta |
| Käsittelysuojaus | Noudatettava sytotoksisten lääkkeiden käsittelyohjeita |

Tarkemmat tiedot on tarkistettava valmisteyhteenvedosta.

## Turvallisuusnäkökohdat

- **Tietämysgraafissa kirjatut vasta-aiheisiin liittyvät tilat** (TxGNN-tietämysgraafi, ei valmisteyhteenvedon teksti): maksan vajaatoiminta, trombosytopenia, neutropenia, agranulosytoosi, anemia, makrosyyttinen anemia, pneumokystoosi, pansytopenia, lymfopenia, myelodysplastinen oireyhtymä, idiopaattinen aplastinen anemia ja aplastinen anemia.
- **Lääkeyhteisvaikutukset**: tietokannassa on yhteensä 100 yhteisvaikutusta. Merkittävimmät luokitellut: naltreksoni (kohtalainen) ja levofloksasiini (lievä). Monen muun lääkkeen (mm. pantopratsoli, omepratsoli, metformiini, morfiini, prednisoni) vaikutustaso on luokittelematon.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja jatkotoimet

**Päätös: Hold**

**Perustelut:**
Ainoa suoraan aihetta koskeva näyttö on yksi tapauskertomus myksopapillaarisesta ependymoomasta, eikä kliinisiä tutkimuksia ole. Näytön taso on siksi L5, ja ennuste perustuu pääosin malliin ja mekanistiseen päättelyyn.

**Jatkoon tarvitaan:**
- Systemaattinen kirjallisuushaku temotsolomidista myksopapillaarisessa ependymoomassa ja muissa cauda equinan kasvaimissa
- Vaikutusmekanismitiedot ja MGMT-metylaatiostatuksen merkitys
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden tarkistus
- Prospektiivinen tai rekisteripohjainen selvitys tehosta ja turvallisuudesta
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

