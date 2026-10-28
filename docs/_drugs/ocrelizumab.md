---
layout: default
title: Ocrelizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 311
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "OCRELIZUMAB"
predicted_indications: ["HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer"]
description: "Ocrelizumab: ennustettu uusi käyttöaihe HER2 positive breast carcinoma (näytön taso L5). Alkuperäinen käyttöaihe: Multiple Sclerosis"
---

# Ocrelizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

## Ocrelizumab: HER2 positive breast carcinoma
{: .text-alpha }

## Yhden lauseen yhteenveto

Okrelitsumabi on CD20-vasta-aine, jota käytetään alun perin multippeliskleroosin (MS-taudin) hoitoon. TxGNN-malli ennustaa sen voivan tehota **HER2-positiiviseen rintasyöpään**, mutta tälle suunnalle ei ole **yhtään kliinistä tutkimusta eikä yhtään kohdennettua julkaisua**. Ennuste perustuu pelkästään mallilaskentaan.

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Multiple Sclerosis |
| Ennustettu uusi käyttöaihe | HER2 positive breast carcinoma |
| TxGNN-ennustepisteet | 0.9989 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Okrelitsumabi on humanisoitu monoklonaalinen vasta-aine, joka kohdistuu CD20:ta ilmentäviin B-soluihin ja tuhoaa niitä. Tarkempaa vaikutusmekanismitietoa ei ole tällä hetkellä saatavilla tähän raporttiin koottuna. Tunnetun tiedon perusteella lääkkeen teho MS-taudissa on osoitettu B-solujen tuhoamisen kautta.

Suoraa mekanistista yhteyttä HER2-positiiviseen rintasyöpään ei ole. Kyseinen syöpä on epiteeliperäinen kasvain, joka ei ilmennä CD20:tä, eikä B-solujen tuhoamisella ole tässä tautimuodossa vakiintunutta kasvainta vastustavaa roolia. Hyvin korkea pistemäärä (0,9989) voi heijastaa verkostotason yhteyksiä, esimerkiksi kasvaimen immuunimikroympäristöön ja kasvaimeen infiltroituviin lymfosyytteihin liittyvää biologiaa. Tätä tukevaa aineistoa ei kuitenkaan ollut käytettävissä.

Samankaltaisia ennusteita tehtiin myös muille rintasyövän alatyypeille (normal breast-like -alatyyppi, progesteronireseptoripositiivinen ja -negatiivinen rintasyöpä, luminaalinen A/B -kasvain). Niillekään ei löytynyt mekanistista perustetta tai kliinistä tukea.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Ensisijaiselle ennusteelle (HER2-positiivinen rintasyöpä) ei löytynyt aiheeseen liittyvää kirjallisuutta.

Luminaalisen A/B -rintakasvaimen ennusteen yhteydessä haettiin 18 julkaisua, mutta ne koskevat okrelitsumabia MS-taudissa, anti-CD20-hoitoja, hypogammaglobulinemiaa tai autoimmuunisairauksia. Yksikään ei käsittele rintasyöpää, joten ne eivät tue tätä käyttöaihetta. Ne on poimittu vain lääkkeen nimen perusteella.

## Suomen markkinatiedot

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004043 | Ocrevus (Roche Registration GmbH) | – | Multippeliskleroosi (lupa peruutettu) |

## Turvallisuushuomiot

**Lääkeyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 100 yhteisvaikutusta. Keskeisimmät:

- **Kohtalaiset:** kortikosteroidit (hydrokortisoni, triamsinoloni, deksametasoni, betametasoni, budesonidi, prednisolooni, prednisoni), radiofarmaseuttiset valmisteet (jobenguaani I-131, ibritumomabitiuksetaani, tositumomabi, samarium-153-leksidronaami) sekä albendatsoli, pentamidiini ja levamisoli.
- **Lievät:** sinkkiyhdisteet (sinkkisulfaatti, -asetaatti, -glukonaatti, -kloridi).

Muista turvallisuustiedoista (varoitukset ja vasta-aiheet) katso valmisteyhteenveto.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain TxGNN-mallin pisteytykseen (näytön taso L5). Kliinisiä tutkimuksia ei ole, kirjallisuus ei käsittele rintasyöpää, eikä CD20-kohteen ja CD20-negatiivisen rintasyövän välillä ole mekanistista yhteyttä. Lisäksi Suomen myyntilupa on peruutettu.

**Eteenpäin siirtymiseksi tarvitaan:**
- Vaikutusmekanismitiedot (MOA) ja selvitys siitä, mikä verkostotason yhteys selittää mallin korkean pistemäärän
- Prekliiniset tutkimukset B-solujen tai kasvaimeen infiltroituvien lymfosyyttien roolista HER2-positiivisessa rintasyövässä
- Valmisteyhteenvedon varoitukset ja vasta-aiheet turvallisuusarviointia varten
- Myyntilupatilanteen selvitys Suomessa (voimassa oleva lupa tai kansallinen reitti)
- Lääkkeenantoreittien yhteensopivuuden arviointi
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

