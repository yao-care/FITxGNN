---
layout: default
title: Metformin
parent: Pelkkä mallin ennuste (L5)
nav_order: 284
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Metformin: ennustettu uusi käyttöaihe Fokaalinen jäykän raajan oireyhtymä (näytön taso L5). Alkuperäinen käyttöaihe: Tyypin 2 diabetes"
monitor_inn: "METFORMIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
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

# Metformiini: Tyypin 2 diabeteksesta fokaaliseen jäykän raajan oireyhtymään

## Yhden lauseen tiivistelmä

Metformiini on suun kautta otettava lääke, jota on alun perin käytetty tyypin 2 diabeteksen hoitoon.
TxGNN-malli ennustaa sen voivan tehota **fokaaliseen jäykän raajan oireyhtymään** (focal stiff limb syndrome).
Ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**, joten ennuste perustuu pelkästään mallilaskentaan.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Tyypin 2 diabetes |
| Ennustettu uusi käyttöaihe | Fokaalinen jäykän raajan oireyhtymä |
| TxGNN-ennustepistemäärä | 99,45 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 19 (kaikki peruutettuja, voimassa 0) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Tämän lääkkeen yksityiskohtaisia vaikutusmekanismitietoja ei ole tällä hetkellä saatavilla. Tunnetun tiedon perusteella metformiini on tyypin 2 diabeteksen hoidossa todettu lääke, jonka tiedetään aktivoivan AMPK-entsyymiä ja vähentävän maksan glukoosintuotantoa. Mekanistista yhteyttä fokaaliseen jäykän raajan oireyhtymään ei kuitenkaan ole osoitettu.

Fokaalinen jäykän raajan oireyhtymä kuuluu jäykän ihmisen oireyhtymän (stiff-person) kirjoon. Sen taustalla on autoimmuuni-, GABAergisen tai glysinergisen järjestelmän häiriö. Selvää yhteyttä metformiinin vaikutukseen ei ole, joten mekanistinen perustelu on spekulatiivinen.

Korkea pistemäärä voi heijastaa graafipohjaista yhteyttä: jäykän ihmisen oireyhtymä esiintyy usein yhdessä tyypin 1 diabeteksen ja muiden autoimmuunisairauksien kanssa. Tämä yhteisesiintyvyys ei kuitenkaan tue metformiinin hoitovaikutusta.

Muita ennustettuja käyttöaiheita (kaikilla näytön taso L5 ja suositus Hold):
- klassinen jäykän ihmisen oireyhtymä (pistemäärä 99,45 %)
- opsismodysplasia (99,40 %)
- tiamiinille vastaava toimintahäiriöoireyhtymä (99,40 %)
- lääkeaineen aiheuttama paikallinen lipodystrofia (99,06 %)

---

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

Kaikki myyntiluvat on peruutettu. Alla on viisi esimerkkiä (kaikki yhdistelmävalmisteita, joissa metformiini on yhtenä vaikuttavana aineena):

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002059 | Komboglyze | – | Tyypin 2 diabetes |
| EMEA/H/C/005738 | Vildagliptin / Metformin hydrochloride Accord | – | Tyypin 2 diabetes |
| EMEA/H/C/003770 | Synjardy | – | Tyypin 2 diabetes |
| EMEA/H/C/005778 | Sitagliptin / Metformin hydrochloride Sun | – | Tyypin 2 diabetes |
| EMEA/H/C/000861 | Janumet | – | Tyypin 2 diabetes |

---

## Turvallisuushuomiot

**Tietämysgraafin (PrimeKG) perusteella tunnistetut vasta-aiheisiin liittyvät sairaudet** (eivät ole valmisteyhteenvedon tekstiä, vaan graafin lääke–sairaus-yhteyksiä):
- maksan vajaatoiminta ja maksasairaus
- munuaissairaus
- haimatulehdus
- sappirakon sairaus
- sydämen vajaatoiminta
- aivolisäkkeen vajaatoiminta ja siihen liittyvät hormonipuutokset (mm. kasvuhormonin puutos, hypogonadotrooppinen hypogonadismi, Kallmannin oireyhtymä, Sheehanin oireyhtymä)
- lisämunuaiskuoren vajaatoiminta
- kateenkorvan sairaus
- märkävirtsanjohdin (pyoureter)

**Lääkeyhteisvaikutukset:** Yhteisvaikutuksia on tunnistettu yhteensä 100. Tärkeimpiä ovat:
- **Vakavat (Major):** asetratsoliamidi, etanoli
- **Kohtalaiset (Moderate):** esim. dolutegraviiri, abemasiklibi, ranitidiini, nifedipiini, ibuprofeeni, ketorolaakki, hydrokortisoni, hydroklooritiatsidi, epinefriini, salbutamoli, formoteroli, etinyyliestradioli, fenyylefriini, pseudoefedriini, asetoheksamidi
- **Lievät (Minor):** akarboosi, paikallinen hydrokortisoni, paikallinen alklometasoni

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat tästä aineistosta, joten ne tulee tarkistaa pakkausselosteesta ja valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste on pelkkä mallilaskenta (L5): kliinisiä tutkimuksia ja julkaisuja ei ole, eikä mekanistinen yhteys metformiinin vaikutukseen ole uskottava. Lisäksi Suomessa ei ole voimassa olevia metformiinia sisältäviä myyntilupia.

**Jatkaminen edellyttää seuraavaa:**
- Vaikutusmekanismitietojen (MOA) täydentäminen
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean aineistosta (turvallisuusarvion edellytys)
- Prekliinisen tai mekanistisen näytön kartoittaminen metformiinin vaikutuksesta jäykän ihmisen oireyhtymän kirjoon (esim. AMPK/mTOR-vaikutukset T-soluihin)
- Systemaattinen kirjallisuushaku ja kliinisten tutkimusten rekisterihaku
- Tarkistus, onko Suomessa voimassa olevia metformiinivalmisteita (nykyisessä aineistossa kaikki 19 myyntilupaa on peruutettu)
- Muiden ennustettujen käyttöaiheiden (erityisesti lipodystrofia ja tiamiinille vastaava oireyhtymä) vertailu, sillä niillä on epäsuora biologinen perustelu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

