---
layout: default
title: Glucagon
parent: Pelkkä mallin ennuste (L5)
nav_order: 206
evidence_level: L5
indication_count: 1
monitor_inn: "GLUCAGON"
predicted_indications: ["irritable bowel syndrome"]
last_modified_at: 2026-10-27
description: "Glucagon: ennustettu uusi käyttöaihe Ärtyvän suolen oireyhtymä (irritable bowel syndrome) (näytön taso L5). Alkuperäinen käyttöaihe: Diabetes Mellitus"
---

# Glucagon
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

## Glukagoni: proglukagonista johdettu peptidihormoni → ärtyvän suolen oireyhtymä (irritable bowel syndrome)
{: .text-alpha }

## Yhden lauseen yhteenveto

Glukagoni on proglukagonista johdettu peptidihormoni, jolla on vaikutuksia ruoansulatuskanavan sileään lihakseen ja liikkuvuuteen.
TxGNN-malli ennustaa sen voivan olla hyödyllinen indikaatiossa **ärtyvän suolen oireyhtymä (irritable bowel syndrome)**.
Tätä suuntaa tukee tällä hetkellä **2 kliinistä tutkimusta** ja **20 julkaisua**, mutta lähes kaikki näyttö koskee GLP-1:tä ja sen analogeja, ei glukagonia itseään.

## Pikayhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Diabetes Mellitus |
| Ennustettu uusi käyttöaihe | Ärtyvän suolen oireyhtymä (irritable bowel syndrome) |
| TxGNN-ennustepisteet | 0,9924 |
| Näytön taso | L5 |
| Suomen markkinatilanne | Markkinoilla (voimassa olevia lupia: 2/2) |
| Myyntilupien määrä | 2 (voimassa: 2) |
| Suositeltu päätös | Hold |

## Miksi ennuste on perusteltu?

Tarkkaa vaikutusmekanismia koskevia tietoja ei ole tällä hetkellä saatavilla. Glukagoni on proglukagonista johdettu peptidi, joka vaikuttaa glukagonireseptoriin. Sillä tiedetään olevan ruoansulatuskanavan sileää lihasta rentouttava ja liikkuvuutta hillitsevä vaikutus, mikä on perustana sen käytölle diagnostisena apuna ruoansulatuskanavan kuvantamisessa.

Ärtyvän suolen oireyhtymään liittyy poikkeava suolen liikkuvuus ja viskeraalinen kipu, joten liikkuvuutta hillitsevä vaikutus voisi mekanistisesti olla yhteydessä oireisiin. Tämä on kuitenkin vain uskottava hypoteesi.

Tärkeä rajoitus: kliiniset tutkimukset ja suurin osa kirjallisuudesta koskevat GLP-1:tä ja sen analogeja (esim. ROSE-010), jotka vaikuttavat eri reseptoriin kuin glukagoni. Näyttö tukee siten lähinnä lääkeaineryhmää tai signalointireittiä, ei glukagonia suoraan. Erittäin korkea ennustepiste on laskennallinen tulos, ja se heijastaa todennäköisesti verkostollista läheisyyttä.

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Vaihe 1/2 | Päättynyt | 52 | GLP-1-analogi ROSE-010:n vaikutus ruoansulatuskanavan motoriikkaan naisilla, joilla on ummetusvaltainen ärtyvän suolen oireyhtymä. Väestö on relevantti, mutta lääke ei ole glukagoni. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Vaihe 1 | Päättynyt | 12 | Natiivin GLP-1:n ja ROSE-010:n vaikutus mahalaukun, pohjukaissuolen ja ohutsuolen liikkuvuuteen aterian jälkeen. Epäsuora mekanistinen tuki; ei IBS-potilaita. |

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systemaattinen katsaus | Frontiers in endocrinology | GLP-1-reseptoriagonistit ja ärtyvän suolen oireyhtymän paraneminen; GLP-1 ja ROSE-010 hillitsevät suolen liikkuvuutta. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Kliininen alaryhmäanalyysi | Scandinavian journal of gastroenterology | ROSE-010 lievitti kipua IBS-kohtauksissa; analyysi sopivimman potilasryhmän tunnistamiseksi. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Katsaus | Experimental physiology | L-solujen ja GLP-1:n rooli ärtyvän suolen oireyhtymän patofysiologiassa. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Kohorttitutkimus | Annals of gastroenterology | GLP-1-reseptoriagonistien määräys- ja lopetuskäytännöt IBS-potilailla. |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Tutkimus | Frontiers in nutrition | Kiertävä GLP-1 nousi low FODMAP -ruokavalion jälkeen IBS-potilailla. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Katsaus | Advances in experimental medicine and biology | Aerosolina annosteltu GLP-1 diabeteksen ja ärtyvän suolen oireyhtymän hoidossa. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Katsaus | Expert opinion on investigational drugs | Kehitteillä olevat lääkeaineet ummetusvaltaiseen IBS:ään. |
| [41974246](https://pubmed.ncbi.nlm.nih.gov/41974246/) | 2026 | Katsaus | Clinical gastroenterology and hepatology | IBS:n hoidon aukot ja perifeeristä viskeraalista afferenttia moduloivat tulevat hoidot. |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Katsaus | Cellular and molecular gastroenterology and hepatology | Aivo-suoli-mikrobiomi-akselin kaksisuuntaiset vuorovaikutukset. |
| [41480755](https://pubmed.ncbi.nlm.nih.gov/41480755/) | 2026 | Katsaus | The Journal of clinical investigation | Suoli-aivovuorovaikutusten mekanismit ja inkretiinipohjaiset hoidot. |

Yksikään lähteistä ei tutki glukagonia itseään ärtyvän suolen oireyhtymän hoidossa.

## Suomen markkinatiedot

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005391 | Ogluo | – | – |
| EMEA/H/C/003848 | Baqsimi | – | – |

## Turvallisuushuomiot

**Yhteisvaikutukset:** Yhteisvaikutustietokannasta löytyi yhteensä 25 yhteisvaikutusta. Kaikki luetellut ovat luokkaa lievä (Minor). Näihin kuuluvat varfariini ja useat beetasalpaajat, kuten asebutololi, atenololi, bisoprololi, karvedilolli, metoprololi, propranololi, sotaloli, nadololi ja labetaloli.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold**

**Perustelut:**
- Kliininen ja kirjallisuusnäyttö koskee GLP-1:tä ja sen analogeja, ei glukagonia. Yksikään viitatuista tutkimuksista ei tutki glukagonia ärtyvän suolen oireyhtymässä, joten näytön taso on L5. Korkea ennustepiste on pelkkä mallin laskennallinen tulos.

**Jatkoon tarvitaan:**
- Vaikutusmekanismitiedot (MOA) glukagonista reseptoritason päättelyn varmistamiseksi
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimea)
- Suora prekliininen tai kliininen tutkimus glukagonista ärtyvän suolen oireyhtymässä
- Arvio glukagonin ja GLP-1-analogien reseptorivaikutusten erosta suolen liikkuvuuteen
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

