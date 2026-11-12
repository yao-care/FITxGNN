---
layout: default
title: Ranolazine
parent: Pelkkä mallin ennuste (L5)
nav_order: 366
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Ranolazine: ennustettu uusi käyttöaihe Nefrogeeninen antidiureesioireyhtymä (näytön taso L5). Alkuperäinen käyttöaihe: Angina pectoris (rasitusrintakipu)"
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
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

## Ranolatsiini: Uusi ennustettu käyttöaihe nefrogeeninen antidiureesioireyhtymä
{: .text-alpha }

## Yhden lauseen yhteenveto

Ranolatsiini on lääke, jota on alun perin käytetty rasitusrintakivun (angina pectoris) hoitoon.
TxGNN-malli ennustaa sen voivan olla tehokas **nefrogeenisessä antidiureesin epäasianmukaisen erityksen oireyhtymässä (NSIAD)**,
mutta ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**, joten näyttö perustuu pelkästään laskennalliseen ennusteeseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Angina pectoris (rasitusrintakipu) |
| Ennustettu uusi käyttöaihe | Nefrogeeninen antidiureesin epäasianmukaisen erityksen oireyhtymä (NSIAD) |
| TxGNN-ennustepisteet | 0,9965 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voi olla perusteltu?

Ranolatsiinin alkuperäistä vaikutusmekanismia koskevia tietoja ei ole tällä hetkellä saatavilla. Yleisesti ranolatsiinin kuvataan estävän sydänlihassolun myöhäistä natriumvirtaa (late INa), ja sillä on vaikutuksia myös muihin ionikanaviin ja kuljettajaproteiineihin. Angina pectoriksessa tämä vähentää sydänlihassolun kalsiumkuormitusta ja iskemian haittoja.

NSIAD johtuu vasopressiinin V2-reseptorin (AVPR2) toiminnan lisääntymiseen johtavista mutaatioista. Reseptori on jatkuvasti aktiivinen, jolloin elimistö pidättää vettä vasopressiinista riippumatta. Käyttöaiheet ovat siis patofysiologisesti kaukana toisistaan: suoraa mekanistista yhteyttä myöhäisen natriumvirran eston ja V2-reseptori-/akvaporiini-2-reitin välillä ei ole osoitettu käytettävissä olevissa tiedoissa.

Ennuste heijastaa todennäköisesti tietämysgraafin läheisyyttä (esim. yhteisiä naapurisolmuja) eikä välttämättä todellista farmakologista yhteyttä. NSIAD on lisäksi erittäin harvinainen sairaus, jonka hoitovaihtoehdot ovat rajalliset, joten korkeaan ennusteeseen on suhtauduttava varovaisesti. Mikä tahansa yhteys olisi tällä hetkellä spekulatiivinen ja vaatisi testaamista prekliinisissä malleissa.

---

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

<!-- review:begin fi-lic-20261106-ranolazine-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myyntilupa on tilaltaan peruutettu, eikä voimassa olevia myyntilupia ole.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-ranolazine-1 -->

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000805 | Ranexa (aiemmin Latixa) | – | Angina pectoris |

---

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole tässä aineistossa saatavilla, joten turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

- **Tietämysgraafin perusteella ilmoitetut vasta-aiheisiin liittyvät sairaudet** (eivät perustu myyntiluvan tekstiin): pitkä QT-oireyhtymä, familiaalinen pitkä QT-oireyhtymä, kääntyvien kärkien takykardia (torsades de pointes), munuaissairaus, märkävirtsaisuus (pyoureter) ja maksakirroosi.
- **Lääkeyhteisvaikutukset**: kyselyssä löytyi yhteensä 100 yhteisvaikutusta. Merkittävimmät (vaikeusaste *Major*): **aprepitantti, deksametasoni, klaritromysiini, dolasetroni ja eliglustaatti**. Kohtalaisia (*Moderate*) ovat mm. famotidiini, metformiini, loperamidi, bisakodyyli, budesonidi, kanagliflotsiini, dapagliflotsiini ja empagliflotsiini. Lieviä (*Minor*) ovat mm. bupropioni, lorkaseriini ja simetidiini.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ainoa tuki on korkea TxGNN-pistemäärä (0,9965), joka on laskennallinen ennuste eikä kliinistä näyttöä.

<!-- review:begin fi-lic-20261106-ranolazine-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ainoa tuki on korkea TxGNN-pistemäärä (0,9965), joka on laskennallinen ennuste eikä kliinistä näyttöä. Kliinisiä tutkimuksia ja kirjallisuutta ei ole, mekanistinen yhteys on osoittamatta, eikä lääkkeellä ole voimassa olevaa myyntilupaa Suomessa.” Poistettu: ilmoitettu myyntilupien määrä tai tila ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-ranolazine-2 -->

**Etenemiseksi tarvitaan:**
- Vaikutusmekanismin (MOA) tiedot ja mekanistisen yhteyden analyysi
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (turvallisuusseulonta ei ole mahdollinen ilman niitä)
- Prekliiniset tutkimukset (esim. AVPR2/akvaporiini-2-reitin mallit) hypoteesin testaamiseksi
- Tietämysgraafin ennusteen taustalla olevien yhteyksien selvitys
- Arvio QT-aikaan, munuaisten ja maksan toimintaan liittyvistä riskeistä sekä merkittävistä yhteisvaikutuksista
- Selvitys lääkkeen saatavuudesta Suomessa

<!-- review:begin fi-lic-20261106-ranolazine-3 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Selvitys lääkkeen saatavuudesta Suomessa, koska myyntilupa on peruutettu” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-ranolazine-3 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Myyntilupa on tilaltaan peruutettu, eikä voimassa olevia myyntilupia ole” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Kliinisiä tutkimuksia ja kirjallisuutta ei ole, mekanistinen yhteys on osoittamatta, eikä lääkkeellä ole voimassa olevaa myyntilupaa Suomess” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”koska myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

