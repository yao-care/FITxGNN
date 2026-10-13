---
layout: default
title: Lonoctocog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 269
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Lonoctokogi alfa: Hemofilia A:sta pseudo-von Willebrandin tautiin

## Yhteenveto

Lonoctokogi alfa on rekombinantti, yksiketjuinen ja B-domeenista typistetty hyytymistekijä VIII -valmiste, jota on alun perin käytetty **hemofilia A:n** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **pseudo-von Willebrandin tautiin** (pistemäärä 99,85 %), mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hemofilia A |
| Ennustettu uusi käyttöaihe | Pseudo-von Willebrandin tauti (verihiutaletyyppinen VWD) |
| TxGNN-ennusteen pistemäärä | 99,85 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Lonoctokogi alfa korvaa hemofilia A:ssa puuttuvan tekijä VIII:n aktiivisuuden. Tarkempaa vaikutusmekanismitietoa ei ole tässä raportissa käytettävissä. Tunnetun tiedon perusteella lääke on rekombinantti FVIII-korvaushoito, jonka teho hemofilia A:ssa on osoitettu.

Pseudo-von Willebrandin taudissa vika on verihiutaleiden GPIbα-reseptorin toiminnan lisääntymisessä (gain-of-function). Tämä lisää reseptorin sitoutumista von Willebrand -tekijään (VWF), jolloin suurimolekyylisiä VWF-multimeerejä häviää ja verihiutaleita poistuu verenkierrosta. Teoreettinen yhteys on, että FVIII kiertää verenkierrossa VWF:hen sitoutuneena, joten FVIII-pitoisuus voi laskea VWF:n vähentyessä.

Ensisijainen vika on kuitenkin verihiutaleperäinen, eikä FVIII-korvaus korjaa sitä. Korkea TxGNN-pistemäärä on pelkkä laskennallinen ennuste, jota ei tue mekanistinen eikä kliininen aineisto.

Muut mallin ennustamat käyttöaiheet ovat samanlaisia:

| Ennustettu käyttöaihe | TxGNN-pistemäärä | Arvio mekanistisesta yhteydestä |
|------|------|------|
| Verihiutaleiden primaarinen vapautumishäiriö | 99,84 % | Lääke ei vaikuta verihiutaleiden granulaaritoimintaan; hyöty korkeintaan epäsuora |
| Glanzmannin trombastenia | 99,76 % | Vika on verihiutaleiden aggregaatiossa (αIIbβ3), FVIII-tasot ovat yleensä normaalit; perustetta tehoon ei löytynyt |
| Scottin oireyhtymä | 99,44 % | Käsitteellinen yhteys tenaasikompleksin kautta, mutta FVIII:n lisääminen ei korjaa puuttuvaa fosfatidyyliseriinipintaa |

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004075 | Afstyla | – | Hemofilia A |

Myyntilupa on peruutettu, eikä voimassa olevia myyntilupia ole.

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkkeiden yhteisvaikutuksia ei löytynyt kyselyssä.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-malliin (L5), eikä tueksi ole kliinisiä tutkimuksia tai kirjallisuutta. Mekanistinen peruste on heikko, koska ensisijainen vika on verihiutaleperäinen. Lisäksi valmisteen myyntilupa Suomessa on peruutettu.

**Eteneminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen ja läpikäynti (Fimean sivusto), sillä ne puuttuvat ja estävät turvallisuusseulonnan
- Vaikutusmekanismitietojen täydentäminen (DrugBank)
- Kirjallisuushaku ja prekliiniset tutkimukset FVIII-korvauksen hyödystä verihiutaleperäisissä vuototaudeissa
- Selvitys valmisteen saatavuudesta ja myyntiluvan tilasta Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

