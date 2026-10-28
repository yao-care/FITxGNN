---
layout: default
title: Sotatercept
parent: Pelkkä mallin ennuste (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "SOTATERCEPT"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
description: "Sotatercept: ennustettu uusi käyttöaihe Acute lymphoblastic leukemia (disease) (näytön taso L5). Alkuperäinen käyttöaihe: Hypertension, Pulmonary"
---

# Sotatercept
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

## Sotatercept: Acute lymphoblastic leukemia (disease)
{: .text-alpha }

## Yhteenveto

Sotatercepti on aktiviini-reseptori tyyppi IIA:n Fc-fuusioproteiini, jota on käytetty alun perin keuhkoverenpainetaudin (pulmonaalihypertensio) hoitoon.
TxGNN-malli ennustaa sen voivan tehota **akuuttiin lymfoblastileukemiaan**.
Ennusteen tueksi ei ole tässä raportissa käytettävissä **yhtään kliinistä tutkimusta eikä julkaisua**, joten näyttö perustuu pelkästään mallin ennusteeseen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hypertension, Pulmonary |
| Ennustettu uusi käyttöaihe | Acute lymphoblastic leukemia (disease) |
| TxGNN-ennustepisteet | 99,78 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa ei ole tällä hetkellä saatavilla. Sotatercepti tunnetaan aktiviini-reseptori tyyppi IIA:n Fc-fuusioproteiinina, joka sitoo aktiviini- ja GDF-ligandeja. Sen teho keuhkoverenpainetaudissa liittyy tähän signaalireitin muokkaukseen.

Yhteys akuuttiin lymfoblastileukemiaan on tällä hetkellä spekulatiivinen. Mahdollinen selitys voisi liittyä aktiviini- ja TGF-beeta-signalointiin luuytimen mikroympäristössä, mutta tätä ei tue mikään käytettävissä oleva tutkimus- tai kirjallisuusnäyttö. Korkea ennustepistemäärä on pelkkä mallin tuottama ennuste, eikä alkuperäisen ja uuden käyttöaiheen samankaltaisuutta ole vielä arvioitu.

## Muut ennustetut käyttöaiheet

Mallin muut kärkiennusteet ovat samalla tavoin vailla kliinistä tai kirjallisuusnäyttöä (kaikki taso L5, päätös Hold):

| Sija | Käyttöaihe | Pisteet | Huomio |
|------|------|------|------|
| 2 | Vaikea ei-proliferatiivinen diabeettinen retinopatia | 99,77 % | Mahdollinen yhteys verkkokalvon verisuonten uudelleenmuovautumiseen on hypoteesi |
| 3 | Diabeettinen retinopatia | 99,72 % | Silmäturvallisuus on arvioitava ensin (verenvuodot, telangiektasiat) |
| 4 | Lääkeaineen aiheuttama osteoporoosi | 99,65 % | Aktiviinisignalointi vaikuttaa luuaineenvaihduntaan, ihmisvaikutus varmistamatta |
| 5 | Diabeettinen kaihi | 99,49 % | Mekanistista perustetta ei voida muodostaa |
| 6 | HER2-positiivinen rintasyöpä | 99,43 % | Spekulatiivinen; vaikutus kasvainbiologiaan voi olla ennakoimaton |
| 7 | Transitionaalisoluinen karsinooma | 99,39 % | TGF-beeta-reitti liittyy virtsarakon syövän etenemiseen, suoraa näyttöä ei ole |
| 8 | Eturauhasen virtsaputken uroteelikarsinooma | 99,36 % | Todennäköisesti graafin läheisyyden tuottama artefakti |
| 9 | Munuaisaltaan sarkomatoidi transitionaalisoluinen karsinooma | 99,36 % | Harvinainen muoto, ontologialähtöinen ennuste |
| 10 | Infiltroiva rakon sarkomatoidi uroteelikarsinooma | 99,34 % | Harvinainen muoto, todennäköinen graafiartefakti |

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005647 | Winrevair | – | Keuhkoverenpainetauti (pulmonaalihypertensio) |

Tämä myyntilupa on tilaltaan peruutettu, eikä voimassa olevia myyntilupia ole.

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkkeiden yhteisvaikutuksia ei löytynyt käytetyistä tiedoista.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu yksinomaan TxGNN-mallin pisteisiin (taso L5), eikä kliinisiä tutkimuksia, kirjallisuutta tai varmennettua vaikutusmekanismia ole. Lisäksi Suomen myyntilupa on peruutettu.

**Eteenpäin siirtymiseksi tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (estää tällä hetkellä turvallisuusseulonnan)
- Yksityiskohtainen vaikutusmekanismitieto (esim. DrugBankista)
- Prekliininen ja kirjallisuuteen perustuva arviointi aktiviini-/TGF-beeta-reitin merkityksestä akuutissa lymfoblastileukemiassa
- Annosteluteiden yhteensopivuuden ja alkuperäisen ja uuden käyttöaiheen samankaltaisuuden arviointi
- Myyntilupatilanteen selvitys Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

