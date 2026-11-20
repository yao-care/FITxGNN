---
layout: default
title: Fostamatinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Fostamatinib: ennustettu uusi käyttöaihe Autosomaalinen trombosytopenia, normaalit verihiutaleet (näytön taso L5). Alkuperäinen käyttöaihe: Trombosytopenia"
monitor_inn: "Fostamatinib"
predicted_indications: ["autosomal thrombocytopenia with normal platelets", "non-syndromic esophageal malformation"]
---

# Fostamatinib
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

## Fostamatinib: Autosomaalinen trombosytopenia, normaalit verihiutaleet
{: .text-alpha }

## Yhden lauseen yhteenveto

Fostamatinibi on Suomessa (EU-keskitetyn myyntiluvan kautta) trombosytopenian hoitoon hyväksytty lääke. TxGNN-malli ennustaa sen voivan tehota **autosomaaliseen trombosytopeniaan, jossa verihiutaleet ovat normaalit**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste on toistaiseksi pelkkä laskennallinen signaali.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Trombosytopenia |
| Ennustettu uusi käyttöaihe | Autosomaalinen trombosytopenia, normaalit verihiutaleet |
| TxGNN-ennusteen pistemäärä | 0,9945 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Fostamatinibi on R406:n esilääke, ja R406 on pernan tyrosiinikinaasin (SYK) estäjä. Sen tunnettu käyttö immuunitrombosytopeniassa perustuu siihen, että SYK:n esto vähentää makrofagien Fc-reseptorivälitteistä verihiutaleiden tuhoamista. Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Fostamatinib (epävirallinen käännös): ”Fostamatinibi on tyrosiinikinaasin estäjä, jolla on osoitettu olevan vaikutusta pernan tyrosiinikinaasiin (SYK). Fostamatinibin päämetaboliitti, R406, estää Fc-aktivoivien reseptorien ja B-solureseptorin signaalinvälitystä.” Englanninkielinen alkuteksti: "Fostamatinib is a tyrosine kinase inhibitor with demonstrated activity against spleen tyrosine kinase (SYK). The major metabolite of fostamatinib, R406, inhibits signal transduction of Fc-activating receptors and B-cell receptor." ([DailyMed: Tavalisse (fostamatinib) prescribing information, Rigel Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21149cc3-049b-43e2-b141-c9499160556c), versio 2025-11-05; haettu 2026-11-19).

TxGNN-pistemäärä on erittäin korkea, mutta se näyttää johtuvan verkostollisesta läheisyydestä alkuperäiseen trombosytopenia-käyttöaiheeseen. Ennustettu sairaus viittaa perinnölliseen (autosomaaliseen) verihiutaleiden määrän häiriöön, joka todennäköisesti ei ole immuunivälitteinen. Tällöin vasta-ainevälitteistä verihiutaleiden poistumaa ei ole, eikä SYK:n estolle ole selvää mekanistista perustetta. Ennustetta tulee siksi pitää vain laskennallisena signaalina.

Toinen ennustettu käyttöaihe, **ei-oireyhtymälliset ruokatorven epämuodostumat** (pistemäärä 0,9905), ei saa mitään mekanistista tukea. Kyseessä ovat sikiökauden ruoansulatuskanavan kehityshäiriöistä johtuvat synnynnäiset rakenteelliset viat (esim. ruokatorven atresia, tracheoesofageaalifisteli). SYK:n esto vaikuttaa immuunisolujen signalointiin eikä korjaa anatomisia kehityshäiriöitä. Korkea pistemäärä on todennäköisesti tietämysgraafin artefakti, ja tila vaatii yleensä kirurgista korjausta.

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole aiheeseen liittyvää kirjallisuutta.

<!-- review:begin fi-lic-20261106-fostamatinib-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntilupa on tilassa "peruutettu", joten voimassa olevia myyntilupia ei ole.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-fostamatinib-1 -->

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005012 | Tavlesse | – | Trombosytopenia |

## Turvallisuusnäkökohdat

**Lääkkeiden yhteisvaikutukset:** Yhteisvaikutustietokannasta löytyi yhteensä 100 yhteisvaikutusta. Alla on esimerkkejä ensimmäisistä 20 tuloksesta.

- **Merkittävä (Major):** klaritromysiini
- **Kohtalainen (Moderate):** rabepratsoli, omepratsoli, deksalansopratsoli, simetidiini, hydrokortisoni, deksametasoni, betametasoni, budesonidi, triamsinoloni, alosetroni, alvimopaani, aprepitantti, dolasetroni, dronabinoli, eliglustaatti, empagliflotsiini, loperamidi, pioglitatsoni, morfiini

Muiden turvallisuustietojen osalta katso valmisteyhteenveto.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Kummallekin ennustetulle käyttöaiheelle on vain mallipohjainen ennuste (L5) ilman kliinistä tai kirjallisuusnäyttöä. Ensimmäisen ennusteen mekanistinen perustelu on heikko (sairaus ei todennäköisesti ole immuunivälitteinen) ja toisen uskottavaa mekanismia ei ole.

<!-- review:begin fi-lic-20261106-fostamatinib-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ensimmäisen ennusteen mekanistinen perustelu on heikko (sairaus ei todennäköisesti ole immuunivälitteinen) ja toisen uskottavaa mekanismia ei ole. Lisäksi lääkkeellä ei ole voimassa olevaa myyntilupaa Suomessa.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-fostamatinib-2 -->

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitus- ja vasta-aihetietojen hankinta Fimeasta (estää turvallisuusseulonnan jatkamisen)
- Vaikutusmekanismitietojen (MOA) täydentäminen DrugBankista
- Selvitys siitä, onko ennustetun perinnöllisen trombosytopenian taustalla SYK-reitin mekanismi
- Prekliiniset tai kirjallisuuteen perustuvat selvitykset ennen mahdollisia kliinisiä tutkimuksia

<!-- review:begin fi-lic-20261106-fostamatinib-3 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Prekliiniset tai kirjallisuuteen perustuvat selvitykset ennen mahdollisia kliinisiä tutkimuksia / Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittäminen” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-fostamatinib-3 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Myyntilupa on tilassa "peruutettu", joten voimassa olevia myyntilupia ei ole” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi lääkkeellä ei ole voimassa olevaa myyntilupaa Suomessa” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittäminen” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Tavalisse (fostamatinib) prescribing information, Rigel Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=21149cc3-049b-43e2-b141-c9499160556c) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

