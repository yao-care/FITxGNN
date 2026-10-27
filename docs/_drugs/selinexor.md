---
layout: default
title: Selinexor
parent: Pelkkä mallin ennuste (L5)
nav_order: 397
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
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

## Selinexor: Multippelista myeloomasta lääkkeen aiheuttamaan osteoporoosiin
{: .text-alpha }

## Yhteenveto

Selinexor on ydinvientiä estävä syöpälääke, jota on käytetty multippelin myelooman hoitoon.
TxGNN-malli ennustaa sen voivan tehota **lääkkeen aiheuttamaan osteoporoosiin**, mutta ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**. Näyttö perustuu pelkästään mallin ennusteeseen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Multippeli myelooma |
| Ennustettu uusi käyttöaihe | Lääkkeen aiheuttama osteoporoosi |
| TxGNN-ennustepistemäärä | 99,22 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Tässä raportissa käytetystä aineistosta puuttuu yksityiskohtainen vaikutusmekanismitieto. Tunnetun tiedon mukaan selinexor on selektiivinen ydinvientiä (XPO1/CRM1) estävä lääke, jonka teho multippelissa myeloomassa on osoitettu.

Mahdollinen mutta varmistamaton yhteys on, että XPO1:n esto muuttaa kasvunestäjien ja signalointisäätelijöiden (esim. NF-kB/IkB, p53) pysymistä solun ytimessä. Tämä voisi vaikuttaa osteoklastien tai osteoblastien signalointiin. Hypoteesia ei tue mikään tähän raporttiin koottu aineisto.

Lisäksi selinexorin tunnetut haittavaikutukset (pahoinvointi, ruokahaluttomuus, painon lasku, väsymys, hyponatremia, trombosytopenia) eivät sovi luuston terveyttä tavoittelevaan käyttöaiheeseen. Uusiutuneessa ja hoitoresistentissä myeloomassa potilailla on jo huomattavaa luustosairautta, minkä vuoksi mahdollista vaikutusta on vaikea erottaa perussairauden vaikutuksesta.

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005127 | Nexpovio | – | Multippeli myelooma (peruutettu) |

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
- Ennuste perustuu pelkästään korkeaan TxGNN-pistemäärään (99,22 %), eikä tukena ole kliinisiä tutkimuksia, kirjallisuutta eikä varmennettua mekanismia. Lääkkeen haittaprofiili on lisäksi epäedullinen luustoindikaatiolle, ja Suomessa ainoa myyntilupa on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimeasta (turvallisuusarvion estävä tietoaukko)
- Vaikutusmekanismin tietojen täydentämistä (esim. DrugBank)
- Prekliinistä ja mekanistista näyttöä XPO1:n estosta luun aineenvaihdunnassa (osteoklastit ja osteoblastit)
- Systemaattista kirjallisuushakua ja kliinisten tutkimusten rekisterihakua
- Hyöty–haitta-arviota, jossa huomioidaan selinexorin toksisuus ja kohdepopulaation perussairaus
- Selvitystä lääkkeen saatavuudesta ja myyntiluvan tilanteesta Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

