---
layout: default
title: Insulin Aspart
parent: Vahva näyttö (L1-L2)
nav_order: 229
evidence_level: L1
indication_count: 10
---

# Insulin Aspart
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **10** kpl
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

# Aspartinsuliini: Diabeteksesta tyypin 1 diabetekseen

## Yhteenveto

Aspartinsuliini on ppikavaikutteinen insuliinianalogi, jota on alun perin käytetty diabeteksen hoitoon.
TxGNN-malli ennustaa sen soveltuvan **tyypin 1 diabetekseen**, mutta kyseessä ei ole varsinainen lääkkeen uudelleenkäyttö, koska tyypin 1 diabetes kuuluu lääkkeen alkuperäisen käyttöaiheen piiriin.
Ennustetta tukee tämän raportin aineistossa **30 kliinistä tutkimusta** ja **20 julkaisua**, joista useat ovat vaiheen 3 satunnaistettuja tutkimuksia.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Diabetes mellitus |
| Ennustettu uusi käyttöaihe | Tyypin 1 diabetes mellitus |
| TxGNN-ennustepisteet | 99,95 % |
| Näytön taso | L1 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 7 (kaikki peruutettuja) |
| Suositeltu päätös | Proceed with Guardrails (eteneminen suojatoimin) |

---

## Miksi ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismia koskevia tietoja ei ole tämän raportin aineistossa saatavilla. Tunnetun farmakologian perusteella aspartinsuliini on pikavaikutteinen insuliinianalogi, joka sitoutuu insuliinireseptoriin ja korvaa tyypin 1 diabeteksessa puuttuvaa elimistön omaa insuliinia.

Tyypin 1 diabetes on diabeteksen alatyyppi, joten ennuste vastaa lääkkeen vakiintunutta käyttöä. Korkea TxGNN-pistemäärä (0,9995) on sopusoinnussa tämän kanssa. Vaiheen 3 tutkimukset tukevat suoraan tehoa ja turvallisuutta.

Muut ennustetut sairaudet (esim. autoimmuuni-ooforiitti, opsismodysplasia, jäykän ihmisen oireyhtymä ja lipodystrofiat) perustuvat pelkkään mallin ennusteeseen, eikä niille löydy kliinistä näyttöä tai uskottavaa mekanistista yhteyttä. Paikallinen lipodystrofia on lisäksi insuliini-injektioiden tunnettu haittavaikutus, joten ennuste on todennäköisesti tietämysgraafin artefakti. Pysyvässä vastasyntyneiden diabeteksessa ja haiman agenesiassa insuliinikorvaus on mekanistisesti perusteltua ja vakiohoitoa, mutta aspartinsuliinille ei ole omia tutkimuksia.

---

## Kliininen tutkimusnäyttö

Alla on tyypin 1 diabetekseen liittyvistä tutkimuksista keskeisimmät (näytön relevanssiluokka A tai B sekä suuret vaiheen 3 tutkimukset).

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Vaihe 3 | Päättynyt | 299 | Aspartinsuliini vs. lisproinsuliini insuliinipumpuissa lapsilla ja nuorilla, joilla on tyypin 1 diabetes |
| [NCT02825251](https://clinicaltrials.gov/study/NCT02825251) | Vaihe 3 | Päättynyt | 472 | Nopeammin vaikuttavan aspartinsuliinin jatkuva ihonalainen infuusio vs. NovoRapid aikuisilla |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Vaihe 3 | Päättynyt | 114 | Detemirinsuliini + aspartinsuliini vs. NPH + aspartinsuliini aikuisilla |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Vaihe 3 | Keskeytetty | 596 | Inhaloitava aterioinsuliini vs. ihonalainen aspartinsuliini, yhdessä detemirinsuliinin kanssa |
| [NCT01520818](https://clinicaltrials.gov/study/NCT01520818) | Vaihe 3 | Päättynyt | 666 | Kaksivaiheinen aspartinsuliini 50/70 vs. kaksivaiheinen ihmisinsuliini 30, tyypin 1 ja 2 diabetes |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Vaihe 3 | Päättynyt | 330 | Detemirinsuliinin valmistustavan turvallisuusvertailu, aspartinsuliini ateriainsuliinina |
| [NCT01467323](https://clinicaltrials.gov/study/NCT01467323) | Vaihe 3 | Päättynyt | 303 | Kaksivaiheinen aspartinsuliini 30 vs. kaksivaiheinen ihmisinsuliini 30/70, tyypin 1 ja 2 diabetes |
| [NCT00725036](https://clinicaltrials.gov/study/NCT00725036) | Vaihe 3 | Päättynyt | 305 | Inhaloitava ihmisinsuliini vs. ihonalainen aspartinsuliini, 24 kuukauden turvallisuus |
| [NCT01999322](https://clinicaltrials.gov/study/NCT01999322) | Vaihe 3 | Päättynyt | 37 | FIAsp:n ja aspartinsuliinin yhteensopivuus ja turvallisuus insuliinipumpussa |
| [NCT01486381](https://clinicaltrials.gov/study/NCT01486381) | Vaihe 3 | Päättynyt | 22 | Kaksivaiheisen aspartinsuliini 30:n pitkäaikaisturvallisuus nuorilla (jatkotutkimus) |

Aineistossa on yhteensä 30 tutkimusta, joista vähintään kymmenen on päättyneitä vaiheen 3 tutkimuksia. Osassa tutkimuksista aspartinsuliini on vertailuvalmiste tai taustahoito, joten näyttö on siltä osin epäsuoraa.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | Degludek vs. detemir yhdessä aspartinsuliinin kanssa raskaana olevilla naisilla, joilla on tyypin 1 diabetes (EXPECT) |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | Kerran viikossa annettava ikodekinsuliini vs. degludek basaali-bolus-hoidossa tyypin 1 diabeteksessa (ONWARDS 6) |
| [40445776](https://pubmed.ncbi.nlm.nih.gov/40445776/) | 2025 | RCT | Diabetes Technol Ther | Täysin suljettu silmukka nopeammalla aspartinsuliinilla (Fiasp) paransi glukoositasapainoa nuorilla |
| [25644227](https://pubmed.ncbi.nlm.nih.gov/25644227/) | 2015 | Systemaattinen katsaus ja meta-analyysi | Pol Arch Med Wewn | Aspartinsuliinin teho ja turvallisuus verrattuna tavalliseen ihmisinsuliiniin, tyypin 1 ja 2 diabetes |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systemaattinen katsaus | Diabetes Metab | Aspartinsuliinin ja tavallisen ihmisinsuliinin vertailu |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Katsaus | Drugs | Aspartinsuliini tuotti ateriainsuliinina matalamman HbA1c:n kuin tavallinen ihmisinsuliini tyypin 1 diabeteksessa |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Katsaus | Treat Endocrinol | Aspartinsuliini vs. tavallinen ihmisinsuliini tyypin 1 ja 2 diabeteksessa |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Katsaus | Drugs Today | Insuliinianalogit tyypin 1 diabeteksessa lapsilla ja nuorilla |
| [31902063](https://pubmed.ncbi.nlm.nih.gov/31902063/) | 2020 | Kertomuksellinen katsaus | Diabetes Ther | Insuliinihoito aikuisilla, joilla on tyypin 1 diabetes |
| [29978361](https://pubmed.ncbi.nlm.nih.gov/29978361/) | 2019 | Katsaus | Clin Pharmacokinet | Nopeammin vaikuttava aspartinsuliini uutena bolusvaihtoehtona |

Pysyvän vastasyntyneiden diabeteksen osalta on yksi katsaus insuliinihoidosta ([28527303](https://pubmed.ncbi.nlm.nih.gov/28527303/), 2017, Diabetes Res Clin Pract).

---

## Markkinatiedot Suomessa

Kaikki seitsemän myyntilupaa on peruutettu.

| Myyntilupanumero | Tuotenimi | Lääkemuoto | Käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000308 | NovoMix | – | Diabetes mellitus |
| EMEA/H/C/005033 | Insulin aspart Sanofi | – | Diabetes mellitus |
| EMEA/H/C/000258 | NovoRapid | – | Diabetes mellitus |
| EMEA/H/C/005635 | Truvelog Mix 30 | – | Diabetes mellitus |
| EMEA/H/C/004965 | Kirsty (aiemmin Kixelle) | – | Diabetes mellitus |

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkkeiden yhteisvaikutuksista ei löytynyt tietoja.

Huomioitavaa: paikallinen lipodystrofia on tunnettu insuliini-injektioiden haittavaikutus.

---

## Johtopäätös ja jatkotoimet

**Päätös: Proceed with Guardrails (eteneminen suojatoimin)**

**Perustelut:**
- Tyypin 1 diabeteksen näyttö on vahva (useita päättyneitä vaiheen 3 tutkimuksia), mutta kyseessä on lääkkeen vakiintunut alkuperäinen käyttöaihe, ei uusi käyttöaihe. Kaikki Suomen myyntiluvat on peruutettu, joten suositus riippuu valmisteen saatavuudesta ja siitä, mitä valmistetta tarkoitetaan.
- Muut ennustetut käyttöaiheet (sijat 2–10) ovat joko pelkkiä malliennusteita (Hold) tai vain epäsuorasti tuettuja tutkimuskysymyksiä (pysyvä vastasyntyneiden diabetes, haiman agenesia).

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimean sivusto) turvallisuusseulontaa varten
- Vaikutusmekanismitiedot (DrugBank)
- Selvitys peruutettujen myyntilupien syistä ja valmisteen nykyisestä saatavuudesta Suomessa
- Mahdollisten uusien käyttöaiheiden osalta aspartinsuliinille spesifiset tutkimukset
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

