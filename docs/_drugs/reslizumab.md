---
layout: default
title: Reslizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 375
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
description: "Reslizumab: ennustettu uusi käyttöaihe Immuunituhoon liittyvä trombosytopenia (thrombocytopenia due to immune destruction) (näytön taso L5). Alkuperäinen käyttöaihe: Asthma"
---

# Reslizumab
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

## Reslizumab: Immuunituhoon liittyvä trombosytopenia (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Yhteenveto

Reslitsumabi on anti-IL-5-monoklonaalinen vasta-aine, jota on alun perin käytetty astman hoitoon. TxGNN-malli ennustaa sen voivan tehota **immuunituhoon liittyvään trombosytopeniaan**, mutta ennustetta tukevat tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua**. Ennuste perustuu yksinomaan laskennalliseen malliin.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Asthma |
| Ennustettu uusi käyttöaihe | Immuunituhoon liittyvä trombosytopenia (thrombocytopenia due to immune destruction) |
| TxGNN-ennustepisteet | 0,9953 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Reslitsumabi on anti-IL-5-vasta-aine, joka vähentää eosinofiilien signalointia. Tarkempaa vaikutusmekanismia koskevia tietoja ei ole tämän raportin aineistossa saatavilla.

Immuunivälitteisen trombosytopenian (esim. ITP) taustalla ovat pääasiassa autovasta-aineiden aiheuttama verihiutaleiden tuho ja heikentynyt megakaryopoieesi. Tunnettua mekanistista yhteyttä IL-5-reittiin ei ole. Mahdollinen yhteys olisi spekulatiivinen, esimerkiksi eosinofiilien tai Th2-aktiivisuuden osuus joissakin potilasryhmissä. Erittäin korkea TxGNN-pistemäärä (0,9953) on vain laskennallinen ennuste.

Toinen ennustettu käyttöaihe, primaarinen verihiutaleiden vapautumishäiriö (pistemäärä 0,9925), on myös heikosti perusteltu: kyseessä on verihiutaleiden oma toimintahäiriö (rakeiden eritys), jossa IL-5-reitin osuutta ei tunneta.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Ensisijaiselle ennustetulle käyttöaiheelle (immuunituhoon liittyvä trombosytopenia) ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

Toiselle ennustetulle käyttöaiheelle (primaarinen verihiutaleiden vapautumishäiriö) löytyi yksi julkaisu, joka ei kuitenkaan tue ennustetta suoraan:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Katsaus | Current Medical Research and Opinion | Katsaus hypereosinofiilisen oireyhtymän (HES) hoitoon, mukaan lukien toinen anti-IL-5-lääke mepolitsumabi. Käsittelee eosinofiilisairautta, ei verihiutalehäiriöitä, joten antaa korkeintaan epäsuoraa taustatietoa. |

## Myyntiluvat Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/003912 | Cinqaero | Ei tietoa | Astma (tila: voimassa) |

<!-- review:begin fi-row-20261112-reslizumab-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/003912 / Cinqaero / Ei tietoa / Astma (tila: peruutettu)” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntilupa Cinqaero (EMEA/H/C/003912) on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-reslizumab-1 -->

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkkeiden yhteisvaikutuksia koskevia tietoja ei löytynyt.

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain laskennalliseen malliin (L5): kliinisiä tutkimuksia ei ole, eikä kirjallisuus tue sitä, ja mekanistinen yhteys on heikko.

<!-- review:begin fi-lic-20261106-reslizumab-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ennuste perustuu vain laskennalliseen malliin (L5): kliinisiä tutkimuksia ei ole, eikä kirjallisuus tue sitä, ja mekanistinen yhteys on heikko. Lisäksi ainoa Suomessa ollut myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-reslizumab-1 -->

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismitietojen (MOA) täydentämistä
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivuilta (turvallisuusarvio ei ole mahdollinen ilman niitä)
- Mekanistisen yhteyden selvittämistä (esim. eosinofiilien tai Th2-aktiivisuuden rooli immuunivälitteisessä trombosytopeniassa) esikliinisillä tai kirjallisuuteen perustuvilla selvityksillä
- Lääkkeen myyntitilanteen ja saatavuuden selvittämistä

<!-- review:begin fi-lic-20261106-reslizumab-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lääkkeen myyntitilanteen ja saatavuuden selvittämistä, koska myyntilupa on peruutettu” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-reslizumab-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi ainoa Suomessa ollut myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”koska myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Cinqaero (EMEA/H/C/003912) on voimassa, ei peruutettu | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

