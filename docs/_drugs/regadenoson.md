---
layout: default
title: Regadenoson
parent: Pelkkä mallin ennuste (L5)
nav_order: 370
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
description: "Regadenoson: ennustettu uusi käyttöaihe Anafylaksia (näytön taso L5). Alkuperäinen käyttöaihe: Sydänlihaksen perfuusiokuvantaminen"
monitor_inn: "REGADENOSON"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
---

# Regadenoson
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

## Regadenosoni: Sydänlihaksen perfuusiokuvantamisesta anafylaksiaan
{: .text-alpha }

## Yhden lauseen yhteenveto

Regadenosoni on diagnostinen lääkeaine, jota on alun perin käytetty sydänlihaksen perfuusiokuvantamiseen (MPI). TxGNN-malli ennustaa sen voivan olla tehokas **anafylaksian** hoidossa, mutta ennusteen tueksi ei ole tällä hetkellä **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste on siis pelkkä laskennallinen hypoteesi.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Sydänlihaksen perfuusiokuvantaminen |
| Ennustettu uusi käyttöaihe | Anafylaksia |
| TxGNN-ennusteen pistemäärä | 0,9985 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

Muut ennustetut käyttöaiheet (pistemäärä): ruoka-aineriippuvainen rasituksen aiheuttama anafylaksia (0,9974), esotropia (0,9912) ja pseudoallergia (0,9912). Kaikkien näytön taso on L5.

---

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Regadenoson (epävirallinen käännös): ”Regadenosoni on matala-affiniteettinen agonisti (K i ≈ 1,3 µM) A 2A -adenosiinireseptorille, ja sen affiniteetti A 1 -adenosiinireseptoriin on vähintään 10 kertaa pienempi (K i > 16,5 µM) ja affiniteetti A 2B - ja A 3 -adenosiinireseptoreihin heikko, jos sitä on lainkaan. Regadenosonin aiheuttama A 2A -adenosiinireseptorin aktivaatio saa aikaan sepelvaltimoiden vasodilataation ja lisää sepelvaltimoverenvirtausta (CBF).” Englanninkielinen alkuteksti: "Regadenoson is a low affinity agonist (K i ≈ 1.3 µM) for the A 2A adenosine receptor, with at least 10-fold lower affinity for the A 1 adenosine receptor (K i > 16.5 µM), and weak, if any, affinity for the A 2B and A 3 adenosine receptors. Activation of the A 2A adenosine receptor by regadenoson produces coronary vasodilation and increases coronary blood flow (CBF)." ([DailyMed: Lexiscan (regadenoson) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=057289f4-2e18-4c1e-bed4-6c1858e2ef16), versio 2018-12-21; haettu 2026-11-19). Tunnetun tiedon mukaan regadenosoni on selektiivinen A2A-adenosiinireseptorin agonisti, ja sen teho sydänlihaksen perfuusiokuvantamisessa diagnostisena aineena on osoitettu. Farmakologiatiedot osoittavat sen sitoutuvan myös A1-, A2B- ja A3-reseptoreihin.

Teoreettinen perustelu on, että A2A-reseptorin aktivaatio yleensä vaimentaa syöttösolujen ja tulehdussolujen aktivaatiota, mikä voisi selittää anti-inflammatorisen vaikutuksen allergisissa reaktioissa. Vaikutuksen suunta on kuitenkin epävarma: adenosiinisignalointi voi A2B- ja A3-reseptorien kautta myös edistää syöttösolujen degranulaatiota. Lisäksi regadenosonin omassa valmisteyhteenvedossa on yliherkkyys- ja anafylaksiavaroituksia.

Alkuperäisen käyttöaiheen (sydänlihaksen kuvantaminen) ja ennustetun käyttöaiheen välinen yhteys on heikko. Ruoka-aineriippuvaisen rasitusanafylaksian ja pseudoallergian perustelu on sama kuin anafylaksialla. Esotropialle ei ole havaittavaa mekanistista yhteyttä: korkea pistemäärä heijastaa todennäköisesti tietämysgraafin verkkotason yhteyksiä eikä biologisesti perusteltua linkkiä. Lyhytvaikutteinen suonensisäinen diagnostinen aine soveltuu myös huonosti krooniseen tilaan.

---

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

<!-- review:begin fi-lic-20261106-regadenoson-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Tämä myyntilupa on tilassa "peruutettu". Voimassa olevia myyntilupia ei ole.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-regadenoson-1 -->

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/001176 | Rapiscan | – | Sydänlihaksen perfuusiokuvantaminen |

---

## Turvallisuusnäkökohdat

- **Lääkkeiden yhteisvaikutukset** (10 kirjausta): Kohtalaisen vakavia yhteisvaikutuksia on raportoitu seuraavien kanssa: kofeiini, dipyridamoli, dyfylliini, teofylliini, aminofylliini ja oksitrifylliini. Näiden adenosiinireseptoreihin vaikuttavien aineiden voidaan odottaa muuttavan regadenosonin vaikutusta. Lisäksi farmakologiatiedot vahvistavat sitoutumisen adenosiinireseptoreihin A1, A2A, A2B ja A3.
- **Tietämysgraafiin perustuvat vasta-aihesignaalit** (eivät perustu valmisteyhteenvedon tekstiin): Graafissa regadenosoniin liitetään vasta-aihe- tai varovaisuussignaaleja mm. seuraavissa tiloissa:
  - sydän- ja verisuonitaudit: hypertensio, hypotensio, aorttastenoosi, eteis-kammiokatkos, sairas sinus -oireyhtymä, sepelvaltimotauti, mitraaliläpän ahtauma, perikardiitti, perikardiaalinen effuusio, kaulavaltimon ahtauma ja tromboosi, ohimenevä aivoverenkiertohäiriö, vertebrobasilaarinen vajaatoiminta
  - hengitystiet: astma (myös allerginen ja sisäinen), keuhkoahtaumatauti ja muut keuhkoputkisairaudet
  - muut: epilepsia, autonomisen hermoston sairaudet, Hornerin oireyhtymä
- Regadenosonin yliherkkyys- ja anafylaksiavaroitukset puoltavat erityistä varovaisuutta anafylaksian ja pseudoallergian kohdalla.

Tarkemmat turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennuste perustuu pelkästään laskennalliseen malliin ilman kliinistä tai kirjallista näyttöä (L5). Vaikutuksen suunta on epävarma, ja lääkkeellä itsellään on anafylaksiaan liittyviä varoituksia.

<!-- review:begin fi-lic-20261106-regadenoson-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Vaikutuksen suunta on epävarma, ja lääkkeellä itsellään on anafylaksiaan liittyviä varoituksia. / Suomessa ainoa myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-regadenoson-2 -->

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hakemista Fimean sivustolta (turvallisuusarvioinnin estävä tietoaukko)
- Yksityiskohtaisten vaikutusmekanismitietojen hakemista DrugBankista
- Prekliinistä näyttöä A2A-välitteisestä syöttösolujen vaimennuksesta sekä A2B/A3-reseptorien roolin selvittämistä
- Systemaattista kirjallisuushakua anafylaksiasta ja adenosiinireseptoreista
- Antoreitin ja annostelun soveltuvuuden arviointia (lyhytvaikutteinen suonensisäinen diagnostinen aine vs. akuutti hoitotilanne)
- Esotropian ennusteen käsittelyä todennäköisenä mallin artefaktina, jota ei kannata viedä eteenpäin ilman biologista perustelua

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Tämä myyntilupa on tilassa "peruutettu". Voimassa olevia myyntilupia ei ole” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Suomessa ainoa myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Lexiscan (regadenoson) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=057289f4-2e18-4c1e-bed4-6c1858e2ef16) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

