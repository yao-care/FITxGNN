---
layout: default
title: Hydroxocobalamin
parent: Pelkkä mallin ennuste (L5)
nav_order: 216
evidence_level: L5
indication_count: 2
monitor_inn: "HYDROXOCOBALAMIN"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
last_modified_at: 2026-11-24
description: "Hydroxocobalamin: ennustettu uusi käyttöaihe Ruokatorven suonikohjut ilman verenvuotoa (esophageal varices without bleeding) (näytön taso L5). Alkuperäinen käyttöaihe: Poisoning"
---

# Hydroxocobalamin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

## Hydroksokobalamiini: kobalamiinijohdannainen → ruokatorven suonikohjut ilman verenvuotoa (esophageal varices without bleeding)
{: .text-alpha }

## Yhteenveto

Hydroksokobalamiini on kobalamiini (B12-vitamiinin muoto), jota käytetään syanidimyrkytyksen hoidossa ja B12-vitamiinin korvaushoidossa. TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **ruokatorven suonikohjut ilman verenvuotoa (esophageal varices without bleeding)**. Ennuste perustuu pelkästään mallin pisteytykseen: tähän ennusteeseen ei ole kliinisiä tutkimuksia eikä julkaisuja, joten näyttö on **L5-tasoa**.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Poisoning |
| Ennustettu uusi käyttöaihe | Ruokatorven suonikohjut ilman verenvuotoa (esophageal varices without bleeding) |
| TxGNN-ennustepisteet | 0,9923 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Hydroxocobalamin (epävirallinen käännös): ”Syanidi on äärimmäisen toksinen myrkky. Ilman nopeaa ja asianmukaista hoitoa altistuminen suurelle syanidiannokselle voi johtaa kuolemaan minuuteissa sytokromioksidaasin estymisen vuoksi, mikä johtaa soluhengityksen pysähtymiseen. […] Kukin hydroksokobalamiinimolekyyli voi sitoa yhden syanidi-ionin korvaamalla sillä kolmenarvoiseen koboltti-ioniin liittyneen hydroksoligandin, jolloin muodostuu syanokobalamiinia, joka erittyy sitten virtsaan.” Englanninkielinen alkuteksti: "Cyanide is an extremely toxic poison. In the absence of rapid and adequate treatment, exposure to a high dose of cyanide can result in death within minutes due to the inhibition of cytochrome oxidase resulting in arrest of cellular respiration. […] Each hydroxocobalamin molecule can bind one cyanide ion by substituting it for the hydroxo ligand linked to the trivalent cobalt ion, to form cyanocobalamin, which is then excreted in the urine." ([DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b), versio 2023-04-27; haettu 2026-11-19). Tunnetut vaikutukset ovat syanidin sitominen (myrkytyskäyttö) ja B12-vitamiinin täydentäminen.

Kumpikaan ei kohdistu porttilaskimopaineeseen, suonikohjujen seinämän jännitykseen tai hemostaasiin, jotka ovat ruokatorven suonikohjujen keskeisiä mekanismeja. Uskottavaa mekanistista yhteyttä ei siis ole löydetty. Korkea pistemäärä (0,9923) voi heijastaa mallin tunnistamia tilastollisia yhteyksiä, esimerkiksi maksasairauteen tai ravitsemukselliseen puutokseen liittyviä, eikä syy-yhteyttä.

Lisäksi samaa pistemäärää on ennustettu myös verenvuotoon liittyvälle muodolle, mikä viittaa siihen, ettei malli erottele näitä tiloja toisistaan.

## Kliininen näyttö

Tälle käyttöaiheelle ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Aiheesta ei ole tällä hetkellä saatavilla kirjallisuutta.

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000806 | Cyanokit | hydroxocobalamin | Poisoning | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

- **Lääkeaineyhteisvaikutukset:** Yhteisvaikutuksia on kirjattu yhteensä 32. Keskivaikeiksi luokiteltuja ovat arseenitrioksidi, kloramfenikoli sekä radioaktiiviset jodit (I-131 ja I-123). Useimpien muiden kirjattujen yhteisvaikutusten (mm. omepratsoli, lansopratsoli, simvastatiini, loperamidi, prednisolooni, asetyylisalisyylihappo, foolihappo, valsartaani ja ramipriili) vakavuusluokka on tuntematon.
- **Vasta-aiheisiin viittaavat tiedot:** Lääkkeen on kirjattu liittyvän sairauksiin hypertensiivinen häiriö ja kohonnut verenpaine. Tämä on mallin tietopohjasta peräisin oleva viite, ei valmisteyhteenvedon teksti. Se on huomionarvoista, koska suonikohjujen taustalla on usein portaalihypertensio.

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat koostetusta aineistosta; ne tulee tarkistaa valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu ainoastaan mallin pistemäärään (0,9923). Kliinisiä tutkimuksia ja julkaisuja ei ole, eikä uskottavaa mekanismia ole tunnistettu. Näytön taso on L5.

**Eteenpäin siirtyminen edellyttää:**
- Tarkan vaikutusmekanismin selvittämistä ja sen arviointia, voiko mikään mekanismi liittyä portaalihypertensioon tai verenvuodon hallintaan
- Esikliinistä tai kliinistä näyttöä, joka tutkii suoraan tätä sairautta
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden tarkistamista (erityisesti kohonnut verenpaine)
- Yhteisvaikutusten vakavuusluokkien täydentämistä

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera); mallin ennusteita, näytön tasoja ja johtopäätöksiä ei kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

