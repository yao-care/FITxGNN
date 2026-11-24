---
layout: default
title: Octreotide
parent: Pelkkä mallin ennuste (L5)
nav_order: 312
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: ennustettu uusi käyttöaihe Vulvar inverted follicular keratosis (näytön taso L5). Alkuperäinen käyttöaihe: Acromegaly"
---

# Octreotide
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

## Octreotide: Vulvar inverted follicular keratosis
{: .text-alpha }

## Yhden lauseen yhteenveto

Oktreotidi on somatostatiinianalogi, jota on alun perin käytetty akromegalian hoitoon. TxGNN-malli ennustaa sen voivan tehota **vulvan käänteiseen follikulaariseen keratoosiin**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään mallin pisteytykseen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Acromegaly |
| Ennustettu uusi käyttöaihe | Vulvar inverted follicular keratosis |
| TxGNN-ennustepisteet | 0.9958 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Octreotide (epävirallinen käännös): ”Sandostatin-injektioneste vaikuttaa farmakologisesti samalla tavoin kuin luonnollinen hormoni somatostatiini. Se estää GH:ta, glukagonia ja insuliinia vielä voimakkaammin kuin somatostatiini. […] Näiden farmakologisten vaikutustensa vuoksi oktreotidia on käytetty metastasoituneisiin karsinoidikasvaimiin liittyvien oireiden (punastuminen ja ripuli) ja VIP:tä erittävien adenoomien (vetinen ripuli) hoitoon.” Englanninkielinen alkuteksti: "Sandostatin Injection exerts pharmacologic actions similar to the natural hormone, somatostatin. It is an even more potent inhibitor of GH, glucagon, and insulin than somatostatin. […] By virtue of these pharmacological actions, octreotide has been used to treat the symptoms associated with metastatic carcinoid tumors (flushing and diarrhea), and VIP secreting adenomas (watery diarrhea)." ([DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39), versio 2026-07-22; haettu 2026-11-19). Oktreotidi on somatostatiinianalogi, joka sitoutuu pääasiassa somatostatiinireseptoreihin SSTR2 ja SSTR5 (aineiston mukaan myös SSTR3). Sen teho akromegaliassa on osoitettu.

Yhteyttä hyvänlaatuiseen follikulaariseen keratinosyyttileesioon ei voida johtaa käytettävissä olevasta aineistosta, ja mikä tahansa selitys olisi spekulatiivinen. Mallin korkea pistemäärä ei yksinään ole näyttöä tehosta. Käänteinen follikulaarinen keratoosi on hyvänlaatuinen ihomuutos, jota hoidetaan yleensä poistamalla se kirurgisesti. Systeemisen peptidilääkkeen tarve on siksi epäselvä.

### Toinen ennuste: seborrooinen keratoosi

Toiseksi sijoittui **seborrooinen keratoosi** (pisteet 0.9955). Sekään ei ole saanut tuekseen kliinisiä tutkimuksia tai julkaisuja. Hypoteesina on, että somatostatiinireseptorien kautta välittyvä signalointi voisi vaikuttaa keratinosyyttien kasvutekijäreitteihin (esim. IGF-1 ja EGFR), mutta tämä on varmistamaton. Tila on hyvänlaatuinen ja hoidetaan yksinkertaisilla paikallisilla toimenpiteillä, joten systeemisen injektoitavan peptidin hyöty–haitta-suhde on ilman tukevaa näyttöä epäsuotuisa. Kahden ennusteen todennäköisesti samankaltainen profiili viittaa siihen, etteivät ne ole toisistaan riippumatonta näyttöä.

## Kliininen tutkimusnäyttö

Ei tällä hetkellä aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/006322 | Oczyesa | octreotide hydrochloride | Acromegaly | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoitus- ja vasta-aihetietoja ei ollut tämän raportin aineistossa saatavilla, joten niihin on tutustuttava valmisteyhteenvedosta.

Tietämyskuvaajaan (TxGNN/PrimeKG) perustuvat vasta-aihesuhteet eivät ole valmisteyhteenvedon tekstiä, mutta ne antavat suuntaa. Niiden mukaan oktreotidiin liittyy varovaisuutta seuraavissa tiloissa:

- **Aineenvaihdunta:** hyperglykemia, hypoglykemia, diabetes, diabeettinen ketoasidoosi, B12-vitamiinin puutos
- **Kilpirauhanen:** kilpirauhasen vajaatoiminta, myksedeema, synnynnäinen kilpirauhasen vajaatoiminta
- **Maksa ja sappi:** maksakirroosi, maksasairaus, sappitiesairaudet, sappikivet (kolelitiaasi, koledokolitiaasi)
- **Ruoansulatuskanava:** suolilama (ileus), suolitukos
- **Sydän:** sydämenpysähdys, sydämen johtumishäiriöt
- **Munuaiset:** munuaisten vajaatoiminta, uremia

**Lääkeyhteisvaikutukset:** Interaktiokyselyssä ei löytynyt varsinaisia lääkeyhteisvaikutuksia. Tulokset kuvaavat oktreotidin farmakologisia kohdereseptoreita (SSTR2, SSTR3 ja SSTR5).

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu ainoastaan TxGNN-pisteisiin (näytön taso L5). Kliinisiä tutkimuksia ja kirjallisuutta ei ole, eikä mekanistista yhteyttä ole osoitettu. Kohdetilat ovat hyvänlaatuisia ja hoidettavissa paikallisesti, joten systeemisen lääkkeen riski–hyötysuhde on epäsuotuisa.

<!-- review:begin fi-lic-20261106-octreotide-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kohdetilat ovat hyvänlaatuisia ja hoidettavissa paikallisesti, joten systeemisen lääkkeen riski–hyötysuhde on epäsuotuisa. Lisäksi Suomen myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-octreotide-1 -->

**Eteneminen edellyttää seuraavaa:**
- Vaikutusmekanismin (MOA) tietojen täydentäminen
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimeasta (turvallisuusseulonnan edellytys)
- Prekliinisen tai mekanistisen näytön selvittäminen somatostatiinireseptorien roolista keratinosyyteissä
- Kirjallisuushaku ja tutkimusrekisterien tarkistus
- Arvio annosteluteiden soveltuvuudesta (esim. paikallinen valmiste) ja kliinisestä tarpeesta

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi Suomen myyntilupa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Oczyesa (EMEA/H/C/006322) on voimassa, ei peruutettu | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

