---
layout: default
title: Fremanezumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 196
evidence_level: L5
indication_count: 1
monitor_inn: "FREMANEZUMAB"
predicted_indications: ["atrophoderma vermiculata"]
last_modified_at: 2026-11-24
description: "Fremanezumab: ennustettu uusi käyttöaihe atrofoderma vermiculata (atrophoderma vermiculata) (näytön taso L5). Alkuperäinen käyttöaihe: Migraine Disorders"
---

# Fremanezumab
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

## Fremanezumabi: CGRP-vasta-aine → atrofoderma vermiculata (atrophoderma vermiculata)
{: .text-alpha }

## Yhteenveto

Fremanezumabi on CGRP:tä (kalsitoniinigeeniin liittyvää peptidiä) estävä vasta-aine, jota käytetään migreenin hoidossa. TxGNN-malli ennustaa, että sen vaikutus voisi ulottua myös **atrofoderma vermiculata (atrophoderma vermiculata) -tilaan**, joka on harvinainen follikulaarinen ihon surkastumishäiriö. Ennusteen tueksi ei ole löytynyt yhtään kliinistä tutkimusta eikä julkaisua, joten ennuste perustuu pelkästään malliin.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Migraine Disorders |
| Ennustettu uusi käyttöaihe | atrofoderma vermiculata (atrophoderma vermiculata) |
| TxGNN-ennustepistemäärä | 0,9904 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Odota (Hold) |

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Fremanezumab (epävirallinen käännös): ”Fremanetsumabi-vfrm on humanisoitu monoklonaalinen vasta-aine, joka sitoutuu kalsitoniinigeeniin liittyvään peptidiin (CGRP) ligandina ja estää sen sitoutumisen reseptoriin.” Englanninkielinen alkuteksti: "Fremanezumab-vfrm is a humanized monoclonal antibody that binds to calcitonin gene-related peptide (CGRP) ligand and blocks its binding to the receptor." ([DailyMed: Ajovy (fremanezumab-vfrm) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e344ea-5916-4947-b6f2-4a76ccc04b6b), versio 2026-06-05; haettu 2026-11-19). Tiedossa on, että lääke kuuluu CGRP:hen kohdistuviin monoklonaalisiin vasta-aineisiin ja että sen teho migreenissä on osoitettu.

Atrofoderma vermiculata on harvinainen follikulaarinen ihon surkastumishäiriö. Käytettävissä olevista tiedoista ei ole nähtävissä CGRP:hen liittyvää patofysiologiaa, eikä mekanistista yhteyttä alkuperäisen ja ennustetun käyttöaiheen välillä voitu osoittaa. Korkea pistemäärä (0,9904) on pelkkä mallin tuottama ennuste, ja se voi heijastaa verkostoartefakteja eikä todellista biologiaa. Kliinisen suosituksen perustaa ei siten ole.

## Kliininen tutkimusnäyttö

Ennustetusta käyttöaiheesta ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Aiheesta ei ole tällä hetkellä saatavilla kirjallisuutta.

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/004833 | Ajovy | fremanezumab | Migraine Disorders | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Yhteisvaikutuksia ei löytynyt haetuista tiedoista.

## Johtopäätös ja jatkotoimet

**Päätös: Odota (Hold)**

**Perustelu:**
Ennuste perustuu ainoastaan TxGNN-mallin pistemäärään. Kliinisiä tutkimuksia tai julkaisuja ei ole, eikä uskottavaa mekanistista yhteyttä CGRP-reittiin ole havaittavissa. Näytön taso on L5.

**Etenemiseksi tarvitaan:**
- Fremanezumabin vaikutusmekanismitiedot ja arvio CGRP:n roolista atrofoderma vermiculatassa
- Valmisteyhteenvedon varoitukset ja vasta-aiheet turvallisuusarviointia varten
- Ensimmäiset prekliiniset tai kliiniset tutkimukset, jotka tarkastelevat juuri tätä sairautta
- Arvio siitä, onko ennuste verkostoartefakti

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera); mallin ennusteita, näytön tasoja ja johtopäätöksiä ei kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Ajovy (fremanezumab-vfrm) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e344ea-5916-4947-b6f2-4a76ccc04b6b) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

