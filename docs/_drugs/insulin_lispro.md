---
layout: default
title: Insulin Lispro
parent: Pelkkä mallin ennuste (L5)
nav_order: 235
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
description: "Insulin Lispro: ennustettu uusi käyttöaihe Autoimmuuninen munasarjatulehdus (autoimmune oophoritis) (näytön taso L5). Alkuperäinen käyttöaihe: Diabetes Mellitus"
---

# Insulin Lispro
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **9** kpl
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

## Insulin Lispro: Autoimmuuninen munasarjatulehdus (autoimmune oophoritis)
{: .text-alpha }

## Yhteenveto

Insuliinilispro on pikavaikutteinen insuliinianalogi, jota on alun perin käytetty **diabetes mellituksen** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **autoimmuuniseen munasarjatulehdukseen** (autoimmune oophoritis), mutta ennuste perustuu pelkästään laskennalliseen malliin: aiheesta ei ole yhtään kliinistä tutkimusta eikä julkaisua.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Diabetes Mellitus |
| Ennustettu uusi käyttöaihe | Autoimmuuninen munasarjatulehdus (autoimmune oophoritis) |
| TxGNN-ennustepisteet | 0.9978 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 4/4) |
| Myyntilupien määrä | 4 (voimassa: 4) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Insulin Lispro (epävirallinen käännös): ”Glukoosiaineenvaihdunnan säätely on insuliinien ja insuliinianalogien, mukaan lukien lisproinsuliinivalmisteet, ensisijainen vaikutus. Insuliinit alentavat veren glukoosipitoisuutta stimuloimalla glukoosin perifeeristä soluunottoa luustolihaksiin ja rasvakudokseen sekä estämällä maksan glukoosintuotantoa.” Englanninkielinen alkuteksti: "Regulation of glucose metabolism is the primary activity of insulins and insulin analogs, including insulin lispro products. Insulins lower blood glucose by stimulating peripheral glucose uptake by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Admelog (insulin lispro) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12ec9e3f-e2ac-43a1-b334-8b6538cf2bb0), versio 2026-09-03; haettu 2026-11-19). Insuliinilispro on pikavaikutteinen insuliinianalogi, jonka teho diabeteksessa on osoitettu. Mekanistisesti yhteys autoimmuuniseen munasarjatulehdukseen on epävarma.

Mahdollinen mutta varmistamaton selitys on, että insuliinisignalointi vaikuttaa munasarjan granuloosasolujen toimintaan. Lisäksi autoimmuunit monirauhasoireyhtymät ja diabetes menevät osittain päällekkäin, mikä voi selittää ennusteen. Insuliinilisprolle ei ole osoitettu suoraa vaikutusmekanismia tässä sairaudessa. Vakiohoitoa ovat edelleen immunosuppressio ja hormonikorvaushoito.

### Muut ennustetut käyttöaiheet

Aineistossa oli yhteensä yhdeksän ennustetta, ja kaikkien näyttö on heikko (L4–L5). Niiden tulkinta on seuraava:

| Sija | Sairaus | Pisteet | Näyttö | Tulkinta |
|------|------|------|------|------|
| 2 | Tiamiinille vasteinen toimintahäiriö­oireyhtymä | 0.9937 | L5 | Todennäköisesti heijastaa diabeteskomponenttia, ei uutta käyttöä |
| 3 | Klassinen jäykän ihmisen oireyhtymä | 0.9936 | L5 | Liittyy GAD-vasta-aineisiin ja tyypin 1 diabeteksen samanaikaisuuteen; insuliini hoitaa diabetesta, ei neurologista sairautta |
| 4 | Fokaalinen jäykän raajan oireyhtymä | 0.9936 | L5 | Sama artefakti kuin edellä |
| 5 | Opsismodysplasia | 0.9934 | L5 | Polkutason yhteys (INPPL1/SHIP2), vaikutussuunta ja kliininen merkitys tuntemattomia |
| 6 | Lääkeaiheuttama paikallinen lipodystrofia | 0.9909 | L5 | Insuliini voi aiheuttaa tilan; kyse on turvallisuushuomiosta, ei uudesta käytöstä |
| 7 | Haiman agenesia | 0.9909 | L4 | Insuliinikorvaus on perusteltu, mutta käytännössä sama kuin alkuperäinen diabetesindikaatio |
| 8 | Sentrifugaalinen lipodystrofia | 0.9904 | L5 | Perusteltu käyttö puuttuu |
| 9 | Paineen aiheuttama paikallinen lipoatrofia | 0.9903 | L5 | Pelkkä laskennallinen ennuste |

---

## Kliininen tutkimusnäyttö

Aiheesta ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ensisijaisesta ennusteesta (autoimmuuninen munasarjatulehdus) ei ole saatavilla kirjallisuutta. Ainoa aineistossa esiintynyt julkaisu liittyy haiman agenesiaan (sija 7) ja on epäsuora:

<!-- review:begin fi-lic-20261106-insulin_lispro-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikki neljä myyntilupaa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-insulin_lispro-1 -->

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Katsaus | J Am Pharm Assoc | Katsaus insuliinihoidon yleistymiseen tyypin 2 diabeteksessa ja hoidon aloittamisen käytäntöihin; ei käsittele haiman agenesiaa suoraan |

---

## Myyntilupatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000088 | Humalog | insulin lispro | Diabetes Mellitus | Voimassa |
| EMEA/H/C/000393 | Liprolog | insulin lispro | Diabetes Mellitus | Voimassa |
| EMEA/H/C/004303 | Insulin lispro Sanofi | insulin lispro | Diabetes Mellitus | Voimassa |
| EMEA/H/C/005037 | Lyumjev (previously Liumjev) | insulin lispro | Diabetes Mellitus | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 100 yhteisvaikutusta. Aineistossa näkyvät pääosin keskivaikeita (Moderate) yhteisvaikutuksia, esimerkiksi:
  - Verensokeriin vaikuttavat lääkkeet: metformiini, alogliptiini, albiglutidi, alpelisibi
  - Sympatomimeetit ja beetaagonistit: fenyyliefriini, pseudoefedriini, adrenaliini, salbutamoli, formoteroli
  - Beetasalpaaja: asebutololi
  - Hormonit ja kortikosteroidit: estradioli, etinyyliestradioli, levonorgestreeli, hydrokortisoni
  - Muut: asetatsoliamidi, hydroklooritiatsidi, doksisykliini, etanoli
  - Vähäisiä (Minor) yhteisvaikutuksia: paikalliset hydrokortisoni ja alklometasoni
- **Lipodystrofia:** Paikallinen lipodystrofia on tunnettu injektoitavan insuliinin haittavaikutus. Tämän vuoksi lipodystrofiaan liittyvien ennusteiden (sijat 6, 8 ja 9) kohdalla insuliinin käyttöä ei voida pitää tukettuna, ja se voi pahentaa tilaa.

Varoitus- ja vasta-aiheita koskevat tiedot ovat puutteelliset, joten niiden osalta on tutustuttava valmisteyhteenvetoon.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste on pelkkä laskennallinen tulos (L5): kliinisiä tutkimuksia ja julkaisuja ei ole, eikä suoraa vaikutusmekanismia ole osoitettu. Useat muut ennusteet näyttävät johtuvan diabeteksen samanaikaisuudesta tai lääkkeen tunnetuista haitoista.

<!-- review:begin fi-lic-20261106-insulin_lispro-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Useat muut ennusteet näyttävät johtuvan diabeteksen samanaikaisuudesta tai lääkkeen tunnetuista haitoista. / Lisäksi kaikki Suomen myyntiluvat on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-insulin_lispro-2 -->

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismitietojen (MOA) täydentämistä (esim. DrugBankista)
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivuilta (estää tällä hetkellä turvallisuusseulonnan)
- Kohdennettua kirjallisuushakua insuliinin ja autoimmuunisen munasarjatulehduksen yhteydestä sekä prekliinisiä tutkimuksia

<!-- review:begin fi-lic-20261106-insulin_lispro-3 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kohdennettua kirjallisuushakua insuliinin ja autoimmuunisen munasarjatulehduksen yhteydestä sekä prekliinisiä tutkimuksia / Myyntilupatilanteen selvittämistä, koska voimassa olevia lupia ei ole” Poistettu: ilmoitettu myyntilupien määrä tai tila ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-insulin_lispro-3 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Kaikki neljä myyntilupaa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi kaikki Suomen myyntiluvat on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Myyntilupatilanteen selvittämistä, koska voimassa olevia lupia ei ole” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Admelog (insulin lispro) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12ec9e3f-e2ac-43a1-b334-8b6538cf2bb0) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

