---
layout: default
title: Linaclotide
parent: Pelkkä mallin ennuste (L5)
nav_order: 265
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Linaclotide: ennustettu uusi käyttöaihe Cauda equina -oireyhtymä (näytön taso L5). Alkuperäinen käyttöaihe: Ärtyvän suolen oireyhtymä"
monitor_inn: "LINACLOTIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
---

# Linaclotide
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

## Linaklotidi: Ärtyvän suolen oireyhtymästä cauda equina -oireyhtymään
{: .text-alpha }

## Yhteenveto

Linaklotidi on guanylaattisyklaasi-C:n (GC-C) agonisti, jota on alun perin käytetty ärtyvän suolen oireyhtymän hoitoon.
TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **cauda equina -oireyhtymän**, mutta ennusteen tueksi ei ole löytynyt **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään mallilaskentaan.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Ärtyvän suolen oireyhtymä |
| Ennustettu uusi käyttöaihe | Cauda equina -oireyhtymä |
| TxGNN-ennusteen pistemäärä | 0,9996 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste voisi olla perusteltu?

Linaklotidi on GC-C-agonisti, joka vaikuttaa paikallisesti suolen epiteelissä. Se nostaa solunsisäistä cGMP-pitoisuutta, lisää nesteen eritystä ja nopeuttaa suolen läpikulkua. Lisäksi se vähentää viskeraalista kipua koolonin afferenttien hermojen kautta. Systeeminen imeytyminen on hyvin vähäistä.

Suoraa mekanistista yhteyttä cauda equina -oireyhtymään ei ole osoitettu. Tila on lannerangan hermojuurten puristusvamma, joka vaatii neurokirurgista hoitoa. Ainoa uskottava päällekkäisyys on neurogeenisen suolen toimintahäiriön (ummetuksen) oireenmukainen lievitys, ei taustalla olevan sairauden hoito. Korkea pistemäärä (0,9996) johtuu todennäköisesti siitä, että tietämysgraafissa suolen ja virtsarakon oireet ovat yhteisiä naapureita.

Muut ennustetut käyttöaiheet ovat samalla tavoin heikosti perusteltuja:
- **Neurogeeninen virtsarakko** (pistemäärä 0,9989): linaklotidin vaikutus rajoittuu pääosin suolen luumeniin, eikä suoraa vaikutusta rakon toimintaan odoteta. Tautitermi on lisäksi merkitty ontologiassa vanhentuneeksi, mikä heikentää ennusteen tulkittavuutta.
- **Unettomuus** (pistemäärä 0,9951): linaklotidi ei vaikuta merkittävästi keskushermostoon. Ainoa epäsuora yhteys on, että ärtyvän suolen oireiden lievittyminen voisi parantaa unen laatua.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002490 | Constella (voimassa) | – | Ärtyvän suolen oireyhtymä |

<!-- review:begin fi-row-20261112-linaclotide-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/002490 / Constella (peruutettu) / – / Ärtyvän suolen oireyhtymä” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntilupa Constella (EMEA/H/C/002490) on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-linaclotide-1 -->

---

## Turvallisuushuomiot

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla tähän raporttiin koottujen tietojen perusteella. Tietoa on täydennettävä Fimean valmisteyhteenvedosta.

**Yhteisvaikutukset**: Yhteisvaikutuksia on kirjattu yhteensä 56. Suurin osa niistä on luokiteltu lieviksi. Keskeisimmät kohtalaiset yhteisvaikutukset:
- Levonorgestreeli
- Etinyyliestradioli
- Noretisteroni
- Levotyroksiini
- Kilpirauhasuute (porsas)

Lieviä yhteisvaikutuksia on mm. protonipumpun estäjien (esim. rabepratsoli, esomepratsoli, deksilansopratsoli), tulehduskipulääkkeiden (esim. ibuprofeeni, diklofenaakki, ketorolaakki) sekä muiden ummetuslääkkeiden ja laksatiivien (esim. bisakodyyli, dokusaatti, risiiniöljy) kanssa.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Kaikki kolme ennustetta ovat tasolla L5: pelkkää mallin ennustetta ilman kliinisiä tutkimuksia tai julkaisuja. Mekanistinen yhteys on heikko tai epäsuora, ja mahdollinen hyöty rajoittuisi neurogeenisen suolen oireisiin.

<!-- review:begin fi-lic-20261106-linaclotide-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Mekanistinen yhteys on heikko tai epäsuora, ja mahdollinen hyöty rajoittuisi neurogeenisen suolen oireisiin. Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-linaclotide-1 -->

**Edetäkseen tarvitaan seuraavat:**
- Valmisteyhteenvedon turvallisuustiedot (varoitukset ja vasta-aiheet) Fimean sivuilta. Tämä on estävä tietoaukko.
- Yksityiskohtaiset vaikutusmekanismitiedot DrugBankista.
- Systemaattinen kirjallisuushaku neurogeenisen suolen toimintahäiriön hoidosta linaklotidilla selkäydin- ja cauda equina -vammapotilailla.

<!-- review:begin fi-lic-20261106-linaclotide-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Systemaattinen kirjallisuushaku neurogeenisen suolen toimintahäiriön hoidosta linaklotidilla selkäydin- ja cauda equina -vammapotilailla. / Arvio markkinatilanteesta: nykyisen myyntiluvan peruutuksen syyt ja mahdolliset muut linaklotidivalmisteet EU:ssa.” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-linaclotide-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Arvio markkinatilanteesta: nykyisen myyntiluvan peruutuksen syyt ja mahdolliset muut linaklotidivalmisteet EU:ssa” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Constella (EMEA/H/C/002490) on voimassa, ei peruutettu | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

