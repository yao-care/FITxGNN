---
layout: default
title: Pretomanid
parent: Pelkkä mallin ennuste (L5)
nav_order: 357
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "PRETOMANID"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery"]
description: "Pretomanid: ennustettu uusi käyttöaihe Candidiasis (näytön taso L5). Alkuperäinen käyttöaihe: Tuberculosis, Multidrug-Resistant"
---

# Pretomanid
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

## Pretomanid: Candidiasis
{: .text-alpha }

## Yhteenveto

Pretomanidi on nitroimidatsooksatsiinien ryhmän lääke, jota on käytetty monilääkeresistentin tuberkuloosin hoitoon.
TxGNN-malli ennustaa sen voivan tehota **kandidoosiin** (pistemäärä 0,9969), mutta ennusteelle ei löydy tukea kliinisistä tutkimuksista eikä kirjallisuudesta: **0 kliinistä tutkimusta** ja **0 julkaisua**.
Ennuste perustuu pelkästään tietämysgraafiin, ja tässä raportissa se arvioidaan heikosti perustelluksi.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Tuberculosis, Multidrug-Resistant |
| Ennustettu uusi käyttöaihe | Candidiasis |
| TxGNN-ennustepistemäärä | 0.9969 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohtien ”Mechanism of Action” ja ”Microbiology” mukaan valmisteesta Pretomanid (epävirallinen käännös): ”Pretomanidi on nitroimidatso-oksatsiiniryhmän antimykobakteerinen lääke. […] Pretomanid-tabletti on nitroimidatso-oksatsiiniryhmän antimykobakteerinen lääke. Pretomanidi tappaa aktiivisesti lisääntyviä M. tuberculosis -bakteereja estämällä mykolihapon biosynteesiä ja estää siten soluseinän tuotannon. Anaerobisissa olosuhteissa pretomanidi vaikuttaa ei-lisääntyviin bakteereihin hengitysmyrkkynä typpioksidin vapautumisen jälkeen.” Englanninkielinen alkuteksti: "Pretomanid is a nitroimidazooxazine antimycobacterial drug. […] Pretomanid Tablet is a nitroimidazooxazine antimycobacterial drug. Pretomanid kills actively replicating M. tuberculosis by inhibiting mycolic acid biosynthesis, thereby blocking cell wall production. Under anaerobic conditions, against non-replicating bacteria, pretomanid acts as a respiratory poison following nitric oxide release." ([DailyMed: pretomanid prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1906fc9-cb3c-4e13-8a4a-da76100c1bf3), versio 2024-11-15; haettu 2026-11-20). Tunnetun farmakologian mukaan pretomanidi on esilääke, jonka *Mycobacterium tuberculosis* aktivoi deatsaflaviiniriippuvaisella nitroreduktaasilla (Ddn). Aktivoituessaan se vapauttaa typpioksidia ja reaktiivisia typpiyhdisteitä ja estää mykolihappojen synteesiä.

Candida-sienillä ei ole tätä aktivaatioreittiä eikä mykobakteerien soluseinän kohdetta, joten sienilääkevaikutusta ei ole syytä odottaa. Alkuperäisen käyttöaiheen (bakteerin aiheuttama tuberkuloosi) ja ennustetun käyttöaiheen (sieni-infektio) välillä ei ole osoitettua mekanistista yhteyttä. Hyvin korkea TxGNN-pistemäärä on pelkkä tietämysgraafin ennuste.

Ennustelistan muut kohteet eivät myöskään ole vahvempia:

- **Lepra** (pistemäärä 0,9927): *M. leprae* on sukua tuberkuloosibakteerille, joten periaatteessa yhteys on uskottavampi. *M. leprae* on kuitenkin menettänyt suuren osan genomistaan, eikä ole osoitettu, että sillä on pretomanidin tarvitsema Ddn-aktivaatioreitti. Kaikki kahdeksan löydettyä julkaisua koskevat lääkeresistenttiä tuberkuloosia, ei lepraa. Lepran hoitoon on lisäksi vakiintunut monilääkehoito (dapsoni, rifampisiini, klofatsimiini).
- **Sepelvaltimotauti** (0.9925), **sydänlihasiskemia** (0.9917) ja **sepelvaltimon poikkeava erkaneminen keuhkovaltimosta** (0.9908): sydän- ja verisuonitaudeille ei ole havaittavissa uskottavaa mekanistista yhteyttä, ja korkeat pisteet johtuvat todennäköisesti tietämysgraafin yhteisestä naapurustosta. Sepelvaltimon poikkeava erkaneminen on harvinainen synnynnäinen rakennepoikkeama, jota hoidetaan leikkauksella.

---

## Kliiniset tutkimukset

Ennustetusta käyttöaiheesta (kandidoosi) ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Kandidoosista ei ole tällä hetkellä saatavilla aiheeseen liittyvää kirjallisuutta.

Toiseksi sijoittuneesta ennusteesta (lepra) haettiin kahdeksan julkaisua, mutta ne koskevat kaikki lääkeresistenttiä tuberkuloosia eivätkä leprapotilaita. Ne eivät siis tue ennustetta. Ne kuvaavat kuitenkin pretomanidin käyttöä alkuperäisessä käyttöaiheessa:

<!-- review:begin fi-lic-20261106-pretomanid-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Tämä myyntilupa on tilaltaan peruutettu, eikä Suomessa ole voimassa olevia pretomanidivalmisteiden myyntilupia.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-pretomanid-1 -->

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [41263908](https://pubmed.ncbi.nlm.nih.gov/41263908/) | 2025 | Katsaus | Archives of Microbiology | Kattava katsaus pretomanidiin lääkeresistentin keuhkotuberkuloosin hoidossa osana BPaL-hoito-ohjelmaa |
| [41876996](https://pubmed.ncbi.nlm.nih.gov/41876996/) | 2026 | Kohorttitutkimus | BMC Infectious Diseases | BPaLM-hoito-ohjelman tehoa ja turvallisuutta selvittävä monikeskus-retrospektiivinen tutkimus Etiopiassa |
| [41080099](https://pubmed.ncbi.nlm.nih.gov/41080099/) | 2025 | Kohorttitutkimus | Pan African Medical Journal | BPaL/BPaLM-hoidon tulokset lääkeresistentissä tuberkuloosissa Kaakkois-Nigeriassa |
| [41354901](https://pubmed.ncbi.nlm.nih.gov/41354901/) | 2025 | Kohorttitutkimus | Communications Medicine | Koko genomin sekvensointi laajasti lääkeresistentin tuberkuloosin havaitsemiseksi Etiopiassa |
| [34992077](https://pubmed.ncbi.nlm.nih.gov/34992077/) | 2022 | Taloudellinen arviointi | BMJ Global Health | BPaL-hoidon budjettivaikutus laajasti lääkeresistentin tuberkuloosin hoidossa |

---

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/005167 | Dovprela (previously Pretomanid FGK) | pretomanid | Tuberculosis, Multidrug-Resistant | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset**: Tietokannasta löytyi yhteensä 14 yhteisvaikutusta.
  - **Merkittävät (Major)**: deksametasoni, lumakaftori, apalutamidi, dabrafenibi, mitotaani, lorlatinibi, entsalutamidi
  - **Kohtalaiset (Moderate)**: empagliflotsiini, sitagliptiini, somatropiini, somatreemi, barisitinibi, klofarabiini, metotreksaatti
- **Sydänturvallisuus**: QT-ajan pidentymistä on pidetty huomionarvoisena pretomanidia sisältävissä hoito-ohjelmissa. Tämä korostuu, jos lääkettä harkittaisiin sydän- ja verisuonitautien käyttöaiheisiin.

Varoituksia ja vasta-aiheita koskevat tiedot tulee tarkistaa valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Kaikkien viiden ennustetun käyttöaiheen näyttö on tasoa L5: kyse on vain mallin ennusteesta, eikä kliinisiä tutkimuksia tai aiheeseen osuvaa kirjallisuutta ole. Mekanistista yhteyttä ei ole osoitettu kandidoosille eikä sydän- ja verisuonitaudeille, ja lepran osalta se on vain teoreettisesti mahdollinen.

<!-- review:begin fi-lic-20261106-pretomanid-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Mekanistista yhteyttä ei ole osoitettu kandidoosille eikä sydän- ja verisuonitaudeille, ja lepran osalta se on vain teoreettisesti mahdollinen. Lääkkeellä ei myöskään ole voimassa olevaa myyntilupaa Suomessa.” Poistettu: ilmoitettu myyntilupien määrä tai tila ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-pretomanid-2 -->

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvitys (Fimean sivustolta), sillä turvallisuusarviointia ei voi tehdä ilman niitä
- Yksityiskohtainen vaikutusmekanismi (esim. DrugBankista)
- Prekliiniset in vitro -tiedot pretomanidin vaikutuksesta *Candida*-lajeihin ja *M. leprae* -bakteeriin sekä Ddn-reitin esiintymisestä niissä
- Lepran osalta kirjallisuushaun tarkennus, koska nykyiset osumat koskevat vain tuberkuloosia
- Sydänturvallisuuden (QT-aika) ja yhteisvaikutusten arviointi ennen mitään jatkokehitystä

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Tämä myyntilupa on tilaltaan peruutettu, eikä Suomessa ole voimassa olevia pretomanidivalmisteiden myyntilupia” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lääkkeellä ei myöskään ole voimassa olevaa myyntilupaa Suomessa” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-20 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: pretomanid prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1906fc9-cb3c-4e13-8a4a-da76100c1bf3) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

