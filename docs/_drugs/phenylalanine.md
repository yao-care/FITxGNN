---
layout: default
title: Phenylalanine
parent: Pelkkä mallin ennuste (L5)
nav_order: 343
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Phenylalanine: ennustettu uusi käyttöaihe sklerosoiva kolangiitti (näytön taso L5). Alkuperäinen käyttöaihe: Vaahterasiirappitauti (MSUD)"
monitor_inn: "phenylalanine"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
---

# Phenylalanine
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

## Fenyylialaniini: Vaahterasiirappitaudista kolangiitti-sklerosoivaan (sclerosing cholangitis)
{: .text-alpha }

## Yhteenveto

Fenyylialaniini on aminohappo, jonka Suomessa myyntiluvan saanut valmiste Maapliv oli tarkoitettu vaahterasiirappitaudin (Maple Syrup Urine Disease, MSUD) hoitoon.
TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **sklerosoivan kolangiitin**, mutta ennuste perustuu vain laskennalliseen malliin: **kliinisiä tutkimuksia ei ole** ja löydetyt **3 julkaisua** ovat vain sivuavia.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Vaahterasiirappitauti (MSUD) |
| Ennustettu uusi käyttöaihe | Sklerosoiva kolangiitti |
| TxGNN-ennustepistemäärä | 0,9943 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voi olla perusteltu?

Tämän raportin tarpeisiin koottu aineisto ei sisällä tietoa fenyylialaniinin vaikutusmekanismista. Suoraa mekanistista yhteyttä alkuperäisen käyttöaiheen (MSUD) ja sklerosoivan kolangiitin välillä ei voida osoittaa. MSUD:ssa fenyylialaniini ei myöskään ole varsinainen hoitoaine, mikä lisää epävarmuutta.

Ainoa löydetty vihje liittyy aromaattisten aminohappojen aineenvaihdunnan muutoksiin kolestaattisissa maksasairauksissa: yhdessä tutkimuksessa plasman tyrosiinipitoisuutta (fenyylialaniinin aineenvaihduntatuote) tarkasteltiin suhteessa uupumukseen primaarisessa biliaarisessa kolangiitissa ja primaarisessa sklerosoivassa kolangiitissa. Tämä ei kuitenkaan tue fenyylialaniinia hoitona.

Toinen ennustettu käyttöaihe, synnynnäinen protrombiinin puutos, on vielä heikommin perusteltu. Ei ole uskottavaa mekanismia, jolla fenyylialaniini korjaisi koagulaatiotekijä II:n puutosta. Korkea pistemäärä (0,9926) on todennäköisesti graafipohjaisen mallin artefakti.

---

## Kliiniset tutkimukset

Ennustettuun käyttöaiheeseen ei tällä hetkellä ole rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Kohorttitutkimus | BMC Gastroenterology | Plasman tyrosiinipitoisuuden yhteys uupumukseen primaarisessa biliaarisessa kolangiitissa ja primaarisessa sklerosoivassa kolangiitissa; tavoitteena tunnistaa aminohappoprofiilin poikkeavuuksia |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Kohorttitutkimus | J Clin Exp Hepatol | Sappitiesyövän seerumin metabolinen profiili brittikohortissa; mahdolliset varhaiset biomarkkerit |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Perustutkimus (määritysmenetelmä) | J Gastroenterol Hepatol | Formyylimetionyylileusyylifenyylialaniini-peptidin radioimmunomääritys ja enterohepaattinen kierto; ei tutki fenyylialaniinia hoitona |

Mikään julkaisuista ei testaa fenyylialaniinia hoitona sklerosoivassa kolangiitissa.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv | – | Vaahterasiirappitauti (peruutettu) |

---

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoitus- ja vasta-aihetietoja ei ollut saatavilla. Lääkkeiden yhteisvaikutuksia ei löytynyt.

Tietämysgraafiin (PrimeKG) perustuvat vasta-aiheyhteydet (ei valmisteyhteenvedon teksti):
- **Munuaissairaudet:** munuaisten kroonien vajaatoiminta, loppuvaiheen munuaisten vajaatoiminta, nefrokalsinoosi, munuaiskivitauti, akuutti virtsahapponefropatia
- **Sydän- ja verisuonisairaudet:** sydänsairaus, kammiovärinä, digitalismyrkytys
- **Kalsium- ja fosforiaineenvaihdunta:** hyperkalsemia, maligniteetin humoraalinen hyperkalsemia, sarkoidoosi, fosforiaineenvaihdunnan häiriö
- **Fenyylialaniinin aineenvaihdunta:** fenyyliketonuria ja muut fenyylialaniinin aineenvaihdunnan häiriöt

Fenyyliketonuria on näistä selkeimmin ilmeinen vasta-aihe, sillä fenyylialaniinin kertyminen on siinä haitallista.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään laskennalliseen malliin (L5). Kliinisiä tutkimuksia ei ole, kirjallisuus on vain sivuavaa, eikä mekanistista yhteyttä voida osoittaa.

<!-- review:begin fi-lic-20261106-phenylalanine-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kliinisiä tutkimuksia ei ole, kirjallisuus on vain sivuavaa, eikä mekanistista yhteyttä voida osoittaa. Lisäksi ainoa Suomen myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-phenylalanine-1 -->

**Jatkoa varten tarvitaan:**
- Vaikutusmekanismin tiedot (esim. DrugBankista)
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimea), mikä on estävä tietoaukko turvallisuusseulonnalle
- Prekliiniset tai mekanistiset tutkimukset fenyylialaniinin roolista kolestaattisissa maksasairauksissa
- Arvio ennusteen biologisesta uskottavuudesta ennen mahdollisia jatkotutkimuksia

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi ainoa Suomen myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

