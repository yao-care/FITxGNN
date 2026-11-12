---
layout: default
title: Relebactam
parent: Pelkkä mallin ennuste (L5)
nav_order: 372
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Relebactam: ennustettu uusi käyttöaihe Hyperamylasemia (näytön taso L5). Alkuperäinen käyttöaihe: Gramnegatiiviset bakteeri-infektiot"
monitor_inn: "Relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
---

# Relebactam
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

## Relebaktaami: Gramnegatiivisten bakteeri-infektioiden hoidosta hyperamylasemiaan
{: .text-alpha }

## Yhteenveto

Relebaktaami on beetalaktamaasin estäjä, jota on käytetty yhdessä imipeneemin ja silastatiinin kanssa gramnegatiivisten bakteeri-infektioiden hoitoon.
TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **hyperamylasemian**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään mallin laskentaan.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Gramnegatiiviset bakteeri-infektiot |
| Ennustettu uusi käyttöaihe | Hyperamylasemia |
| TxGNN-ennusteen pistemäärä | 0,9922 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Tämän ennusteen perusteita ei voida tukea käytettävissä olevalla aineistolla. Tarkkaa vaikutusmekanismia koskevia tietoja ei ole saatavilla. Tunnetun tiedon mukaan relebaktaami on diatsabisyklooktaanityyppinen beetalaktamaasin estäjä, joka estää bakteerien A- ja C-luokan beetalaktamaaseja ja suojaa yhdistelmässä käytettävää beetalaktaamiantibioottia hajoamiselta. Sillä ei tunneta vaikutusta amylaasin säätelyyn eikä haiman tai sylkirauhasten entsyymieritykseen.

Hyperamylasemia on yleensä laboratoriolöydös tai taustalla olevan sairauden (esim. haimatulehdus, munuaisten vajaatoiminta) oire, eikä varsinainen hoidettava kohdesairaus. Erittäin korkea pistemäärä on mallin ennuste, joka johtuu todennäköisesti verkkopohjaisista assosiaatioista.

Samaa pistemäärää ei kannata tulkita sairauskohtaiseksi signaaliksi: ennuste on identtinen myös toiselle kohteelle (polyklonaalinen hyperviskositeettioireyhtymä, 0,9922), mikä viittaa mallin yhteiseen artefaktaan. Kolmas ennuste, synnynnäinen analbuminemia (0,9908), on samoin vailla mekanistista perustetta: beetalaktamaasin estäjä ei voi korjata albumiinin synteesiä koskevaa geenivirhettä.

---

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

<!-- review:begin fi-lic-20261106-relebactam-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Tämä myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-relebactam-1 -->

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004808 | Recarbrio | – | Gramnegatiiviset bakteeri-infektiot |

---

## Turvallisuusnäkökohdat

Turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Lääkeyhteisvaikutuksia ei löytynyt tätä raporttia varten kootusta aineistosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste on pelkkä mallin tuottama (taso L5), eikä sille ole kliinistä tai kirjallisuusnäyttöä eikä mekanistista selitystä.

<!-- review:begin fi-lic-20261106-relebactam-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ennuste on pelkkä mallin tuottama (taso L5), eikä sille ole kliinistä tai kirjallisuusnäyttöä eikä mekanistista selitystä. Lisäksi Suomessa on vain peruutettu myyntilupa.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-relebactam-2 -->

**Etenemiseksi tarvitaan:**
- Vaikutusmekanismitiedot (MOA) esim. DrugBankista
- Valmisteyhteenvedon varoitukset ja vasta-aiheet Fimean sivustolta (estää turvallisuusseulonnan jatkamisen)
- Mekanistinen perustelu ennustetulle käyttöaiheelle sekä esikliininen tai kirjallisuuteen perustuva näyttö
- Arvio siitä, onko hyperamylasemia ylipäätään sopiva hoitokohde, vai pitäisikö tarkastella taustalla olevia sairauksia

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Tämä myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi Suomessa on vain peruutettu myyntilupa” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

