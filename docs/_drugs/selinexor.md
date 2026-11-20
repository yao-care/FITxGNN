---
layout: default
title: Selinexor
parent: Pelkkä mallin ennuste (L5)
nav_order: 397
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Selinexor: ennustettu uusi käyttöaihe Lääkkeen aiheuttama osteoporoosi (näytön taso L5). Alkuperäinen käyttöaihe: Multippeli myelooma"
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
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

## Selinexor: Lääkkeen aiheuttama osteoporoosi
{: .text-alpha }

## Yhteenveto

Selinexor on ydinvientiä estävä syöpälääke, jota on käytetty multippelin myelooman hoitoon.
TxGNN-malli ennustaa sen voivan tehota **lääkkeen aiheuttamaan osteoporoosiin**, mutta ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**. Näyttö perustuu pelkästään mallin ennusteeseen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Multippeli myelooma |
| Ennustettu uusi käyttöaihe | Lääkkeen aiheuttama osteoporoosi |
| TxGNN-ennustepistemäärä | 0,9922 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Selinexor (epävirallinen käännös): ”Ei-kliinisissä tutkimuksissa seliineksori estää reversiibelisti tuumorisuppressoriproteiinien (TSP), kasvunsäätelijöiden ja onkogeenisten proteiinien mRNA:iden tumasta ulos kuljetusta salpaamalla eksportiini 1:tä (XPO1). Seliineksorin aiheuttama XPO1:n esto johtaa TSP:iden kertymiseen tumaan ja useiden onkoproteiinien, kuten c-myc:n ja sykliini D1:n, vähenemiseen, solusyklin pysähtymiseen ja syöpäsolujen apoptoosiin.” Englanninkielinen alkuteksti: "In nonclinical studies, selinexor reversibly inhibits nuclear export of tumor suppressor proteins (TSPs), growth regulators, and mRNAs of oncogenic proteins by blocking exportin 1 (XPO1). XPO1 inhibition by selinexor leads to accumulation of TSPs in the nucleus and reductions in several oncoproteins, such as c-myc and cyclin D1, cell cycle arrest, and apoptosis of cancer cells." ([DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8), versio 2026-05-12; haettu 2026-11-19). Tunnetun tiedon mukaan selinexor on selektiivinen ydinvientiä (XPO1/CRM1) estävä lääke, jonka teho multippelissa myeloomassa on osoitettu.

Mahdollinen mutta varmistamaton yhteys on, että XPO1:n esto muuttaa kasvunestäjien ja signalointisäätelijöiden (esim. NF-kB/IkB, p53) pysymistä solun ytimessä. Tämä voisi vaikuttaa osteoklastien tai osteoblastien signalointiin. Hypoteesia ei tue mikään tähän raporttiin koottu aineisto.

Lisäksi selinexorin tunnetut haittavaikutukset (pahoinvointi, ruokahaluttomuus, painon lasku, väsymys, hyponatremia, trombosytopenia) eivät sovi luuston terveyttä tavoittelevaan käyttöaiheeseen. Uusiutuneessa ja hoitoresistentissä myeloomassa potilailla on jo huomattavaa luustosairautta, minkä vuoksi mahdollista vaikutusta on vaikea erottaa perussairauden vaikutuksesta.

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005127 | Nexpovio | – | Multippeli myelooma (voimassa) |

<!-- review:begin fi-row-20261112-selinexor-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/005127 / Nexpovio / – / Multippeli myelooma (peruutettu)” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntilupa Nexpovio (EMEA/H/C/005127) on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-selinexor-1 -->

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (ydinvientiä estävä, XPO1-estäjä) |
| Myelosuppression riski | Keskisuuri–korkea (trombosytopenia tunnettu haittavaikutus) |
| Oksettavuusluokitus | Keskisuuri–korkea (pahoinvointi yleistä) |
| Seurattavat parametrit | Täydellinen verenkuva (trombosyytit, neutrofiilit), natrium, paino ja ravitsemustila, maksa- ja munuaisarvot |
| Käsittelysuojaus | Noudatettava sytotoksisten lääkkeiden käsittelyohjeita |

Tarkemmat tiedot: ks. valmisteyhteenvedon varoitukset ja varotoimet.

## Turvallisuusnäkökohdat

**Lääkeaineiden yhteisvaikutukset:** Tietokannasta löytyi yhteensä 81 yhteisvaikutusta. Merkittäviksi (Major) luokiteltuja ovat muun muassa:
- deferipronin
- samarium (153Sm) leksidronaamin
- adalimumabin
- barisitinibin
- certolitsumabipegolin
- kladribiinin
- klotsapiinin kanssa

Keskinkertaisiksi (Moderate) luokiteltuja ovat muun muassa strontiumkloridi Sr-89, roflumilasti, kloramfenikoli, tsidovudiini, atsatiopriini, alemtutsumabi, anakinra sekä useat rokotteet (mm. pernarokote ja kolerarokote).

Muuta turvallisuustietoa: ks. valmisteyhteenveto.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään korkeaan TxGNN-pistemäärään (0,9922), eikä tukena ole kliinisiä tutkimuksia, kirjallisuutta eikä varmennettua mekanismia. Lääkkeen haittaprofiili on lisäksi epäedullinen luustoindikaatiolle.

<!-- review:begin fi-lic-20261106-selinexor-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lääkkeen haittaprofiili on lisäksi epäedullinen luustoindikaatiolle, ja Suomessa ainoa myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-selinexor-1 -->

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimeasta (turvallisuusarvion estävä tietoaukko)
- Vaikutusmekanismin tietojen täydentämistä (esim. DrugBank)
- Prekliinistä ja mekanistista näyttöä XPO1:n estosta luun aineenvaihdunnassa (osteoklastit ja osteoblastit)
- Systemaattista kirjallisuushakua ja kliinisten tutkimusten rekisterihakua
- Hyöty–haitta-arviota, jossa huomioidaan selinexorin toksisuus ja kohdepopulaation perussairaus
- Selvitystä lääkkeen saatavuudesta ja myyntiluvan tilanteesta Suomessa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”ja Suomessa ainoa myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Nexpovio (EMEA/H/C/005127) on voimassa, ei peruutettu | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

