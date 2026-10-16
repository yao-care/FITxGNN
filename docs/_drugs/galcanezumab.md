---
layout: default
title: Galcanezumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 198
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Galcanezumab: ennustettu uusi käyttöaihe Hepariinin kofaktori 2:n puutos (näytön taso L5). Alkuperäinen käyttöaihe: Migreeni"
monitor_inn: "GALCANEZUMAB"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Galcanezumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

# Galkanetsumabi: Migreenistä hepariinin kofaktori 2:n puutokseen

## Yhteenveto

Galkanetsumabi on CGRP-neuropeptidiin (kalsitoniinigeeniin liittyvä peptidi) sitoutuva monoklonaalinen vasta-aine, jota käytetään migreenin ehkäisyyn.
TxGNN-malli ennustaa sen voivan tehota **hepariinin kofaktori 2:n puutokseen**, mutta ennusteen tueksi ei ole löytynyt **yhtään kliinistä tutkimusta eikä yhtään julkaisua**.
Ennuste perustuu pelkästään mallin laskennalliseen tulokseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Migreeni |
| Ennustettu uusi käyttöaihe | Hepariinin kofaktori 2:n puutos |
| TxGNN-ennustepisteet | 99,50 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettu myyntilupa |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Tähän raporttiin koottu aineisto ei sisällä tarkkaa vaikutusmekanismitietoa. Tiedetään, että galkanetsumabi on CGRP:tä neutraloiva vasta-aine, jonka teho migreenin ehkäisyssä on osoitettu.

Hepariinin kofaktori 2:n puutos on perinnöllinen tromboosialttius (SERPIND1-geeni), jossa trombiinin esto on heikentynyt. CGRP-signalointia ei tunneta osaksi hyytymiskaskadia tai hepariinin kofaktori II:n toimintaa. Uskottavaa mekanistista yhteyttä alkuperäisen ja ennustetun käyttöaiheen välillä ei siis ole tunnistettu. CGRP:tä neutraloivan vasta-aineen ei voida odottaa korjaavan seriinientsyymi-inhibiittorin (serpiinin) puutosta.

Korkea pistemäärä (0,995) on graafipohjainen ennuste, eikä se yksin ole näyttöä tehosta.

### Muut ennustetut käyttöaiheet

Samalla mallilla ennustettiin kaksi muuta, hyvin samankaltaisilla pisteillä varustettua tromboosialttiuteen liittyvää tilaa:

| Sija | Ennustettu käyttöaihe | TxGNN-pisteet | Näytön taso | Suositus |
|---|------|------|------|------|
| 2 | Antitrombiinin puutos, tyyppi 2 | 99,41 % | L5 | Hold |
| 3 | Tekijä V:n liikatuotanto ja spontaani tromboosi | 99,41 % | L5 | Hold |

Kolmen ennusteen samankaltaiset pisteet ja yhteinen tromboositeema viittaavat pikemminkin järjestelmälliseen graafiartefaktaan kuin lääkekohtaiseen biologiaan. Mekanistista yhteyttä ei ole tunnistettu kummassakaan.

---

## Kliiniset tutkimukset

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

---

## Tietoa Suomen markkinoista

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004648 | Emgality | – | Migreeni |

Myyntilupa on tilassa "peruutettu", eikä Suomessa ole voimassa olevaa myyntilupaa.

---

## Turvallisuusnäkökohdat

Tämän raportin tietoihin ei sisälly valmisteyhteenvedon varoituksia tai vasta-aiheita, eikä yhteisvaikutustietoja löytynyt. Turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

Huomioitavaa: CGRP:llä on verisuonia laajentavia tehtäviä. CGRP-estäjän käyttöä potilailla, joilla on tromboosialttius, tulisi arvioida erikseen turvallisuuden näkökulmasta ennen mitään jatkotutkimuksia. Tämä ei kuitenkaan viittaa hoidolliseen hyötyyn.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain mallin laskennalliseen pisteeseen (L5): kliinisiä tutkimuksia ja julkaisuja ei ole, eikä uskottavaa mekanistista yhteyttä tunnistettu. Lisäksi Suomen myyntilupa on peruutettu.

**Eteenpäin siirtyminen edellyttäisi:**
- Valmisteyhteenvedon (Fimea) varoitusten ja vasta-aiheiden hankkimista ja läpikäyntiä, mikä estää turvallisuusseulonnan etenemisen
- Vaikutusmekanismitietojen täydentämistä (esim. DrugBank)
- Perustelua sille, miksi CGRP:n esto voisi vaikuttaa hyytymisjärjestelmään, sekä prekliinistä tai kirjallisuusnäyttöä
- Tromboottisen turvallisuuden arviointia CGRP-salpauksen osalta
- Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittämistä Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

