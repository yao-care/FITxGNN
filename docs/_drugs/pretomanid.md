---
layout: default
title: Pretomanid
parent: Pelkkä mallin ennuste (L5)
nav_order: 357
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Pretomanid: ennustettu uusi käyttöaihe Kandidoosi (näytön taso L5). Alkuperäinen käyttöaihe: Monilääkeresistentti tuberkuloosi"
monitor_inn: "PRETOMANID"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery"]
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

## Pretomanidi: Monilääkeresistentin tuberkuloosin hoidosta ennustettuun kandidoosiin
{: .text-alpha }

## Yhteenveto

Pretomanidi on nitroimidatsooksatsiinien ryhmän lääke, jota on käytetty monilääkeresistentin tuberkuloosin hoitoon.
TxGNN-malli ennustaa sen voivan tehota **kandidoosiin** (pistemäärä 99,69 %), mutta ennusteelle ei löydy tukea kliinisistä tutkimuksista eikä kirjallisuudesta: **0 kliinistä tutkimusta** ja **0 julkaisua**.
Ennuste perustuu pelkästään tietämysgraafiin, ja tässä raportissa se arvioidaan heikosti perustelluksi.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Monilääkeresistentti tuberkuloosi |
| Ennustettu uusi käyttöaihe | Kandidoosi |
| TxGNN-ennustepistemäärä | 99,69 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Tämän raportin laatimiseen kerätyissä tiedoissa ei ole yksityiskohtaista vaikutusmekanismia. Tunnetun farmakologian mukaan pretomanidi on esilääke, jonka *Mycobacterium tuberculosis* aktivoi deatsaflaviiniriippuvaisella nitroreduktaasilla (Ddn). Aktivoituessaan se vapauttaa typpioksidia ja reaktiivisia typpiyhdisteitä ja estää mykolihappojen synteesiä.

Candida-sienillä ei ole tätä aktivaatioreittiä eikä mykobakteerien soluseinän kohdetta, joten sienilääkevaikutusta ei ole syytä odottaa. Alkuperäisen käyttöaiheen (bakteerin aiheuttama tuberkuloosi) ja ennustetun käyttöaiheen (sieni-infektio) välillä ei ole osoitettua mekanistista yhteyttä. Hyvin korkea TxGNN-pistemäärä on pelkkä tietämysgraafin ennuste.

Ennustelistan muut kohteet eivät myöskään ole vahvempia:

- **Lepra** (pistemäärä 99,27 %): *M. leprae* on sukua tuberkuloosibakteerille, joten periaatteessa yhteys on uskottavampi. *M. leprae* on kuitenkin menettänyt suuren osan genomistaan, eikä ole osoitettu, että sillä on pretomanidin tarvitsema Ddn-aktivaatioreitti. Kaikki kahdeksan löydettyä julkaisua koskevat lääkeresistenttiä tuberkuloosia, ei lepraa. Lepran hoitoon on lisäksi vakiintunut monilääkehoito (dapsoni, rifampisiini, klofatsimiini).
- **Sepelvaltimotauti** (99,25 %), **sydänlihasiskemia** (99,17 %) ja **sepelvaltimon poikkeava erkaneminen keuhkovaltimosta** (99,08 %): sydän- ja verisuonitaudeille ei ole havaittavissa uskottavaa mekanistista yhteyttä, ja korkeat pisteet johtuvat todennäköisesti tietämysgraafin yhteisestä naapurustosta. Sepelvaltimon poikkeava erkaneminen on harvinainen synnynnäinen rakennepoikkeama, jota hoidetaan leikkauksella.

---

## Kliiniset tutkimukset

Ennustetusta käyttöaiheesta (kandidoosi) ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Kandidoosista ei ole tällä hetkellä saatavilla aiheeseen liittyvää kirjallisuutta.

Toiseksi sijoittuneesta ennusteesta (lepra) haettiin kahdeksan julkaisua, mutta ne koskevat kaikki lääkeresistenttiä tuberkuloosia eivätkä leprapotilaita. Ne eivät siis tue ennustetta. Ne kuvaavat kuitenkin pretomanidin käyttöä alkuperäisessä käyttöaiheessa:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [41263908](https://pubmed.ncbi.nlm.nih.gov/41263908/) | 2025 | Katsaus | Archives of Microbiology | Kattava katsaus pretomanidiin lääkeresistentin keuhkotuberkuloosin hoidossa osana BPaL-hoito-ohjelmaa |
| [41876996](https://pubmed.ncbi.nlm.nih.gov/41876996/) | 2026 | Kohorttitutkimus | BMC Infectious Diseases | BPaLM-hoito-ohjelman tehoa ja turvallisuutta selvittävä monikeskus-retrospektiivinen tutkimus Etiopiassa |
| [41080099](https://pubmed.ncbi.nlm.nih.gov/41080099/) | 2025 | Kohorttitutkimus | Pan African Medical Journal | BPaL/BPaLM-hoidon tulokset lääkeresistentissä tuberkuloosissa Kaakkois-Nigeriassa |
| [41354901](https://pubmed.ncbi.nlm.nih.gov/41354901/) | 2025 | Kohorttitutkimus | Communications Medicine | Koko genomin sekvensointi laajasti lääkeresistentin tuberkuloosin havaitsemiseksi Etiopiassa |
| [34992077](https://pubmed.ncbi.nlm.nih.gov/34992077/) | 2022 | Taloudellinen arviointi | BMJ Global Health | BPaL-hoidon budjettivaikutus laajasti lääkeresistentin tuberkuloosin hoidossa |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005167 | Dovprela (aiemmin Pretomanid FGK) | – | Monilääkeresistentti tuberkuloosi |

Tämä myyntilupa on tilaltaan peruutettu, eikä Suomessa ole voimassa olevia pretomanidivalmisteiden myyntilupia.

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
- Kaikkien viiden ennustetun käyttöaiheen näyttö on tasoa L5: kyse on vain mallin ennusteesta, eikä kliinisiä tutkimuksia tai aiheeseen osuvaa kirjallisuutta ole. Mekanistista yhteyttä ei ole osoitettu kandidoosille eikä sydän- ja verisuonitaudeille, ja lepran osalta se on vain teoreettisesti mahdollinen. Lääkkeellä ei myöskään ole voimassa olevaa myyntilupaa Suomessa.

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvitys (Fimean sivustolta), sillä turvallisuusarviointia ei voi tehdä ilman niitä
- Yksityiskohtainen vaikutusmekanismi (esim. DrugBankista)
- Prekliiniset in vitro -tiedot pretomanidin vaikutuksesta *Candida*-lajeihin ja *M. leprae* -bakteeriin sekä Ddn-reitin esiintymisestä niissä
- Lepran osalta kirjallisuushaun tarkennus, koska nykyiset osumat koskevat vain tuberkuloosia
- Sydänturvallisuuden (QT-aika) ja yhteisvaikutusten arviointi ennen mitään jatkokehitystä
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

