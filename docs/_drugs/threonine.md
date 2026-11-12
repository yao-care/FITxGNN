---
layout: default
title: Threonine
parent: Pelkkä mallin ennuste (L5)
nav_order: 434
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Threonine: ennustettu uusi käyttöaihe Gastropareesi (näytön taso L5). Alkuperäinen käyttöaihe: Vaahterasiirappitauti (MSUD)"
monitor_inn: "threonine"
predicted_indications: ["gastroparesis (disease)"]
---

# Threonine
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

## Treoniini: Gastropareesi
{: .text-alpha }

## Yhden lauseen yhteenveto

Treoniini on välttämätön aminohappo, jota on käytetty vaahterasiirappitaudin (MSUD) hoitoon. TxGNN-malli ennustaa sen voivan olla hyödyllinen **gastropareesin** hoidossa, mutta ennuste perustuu pelkästään mallin pistemäärään: tähän suuntaan ei ole **yhtään kliinistä tutkimusta** eikä **yhtään julkaisua** kokoamissamme tiedoissa.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Vaahterasiirappitauti (MSUD) |
| Ennustettu uusi käyttöaihe | Gastropareesi |
| TxGNN-ennustepistemäärä | 0,9932 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voi olla perusteltu?

Tähän raportiin koottujen tietojen mukaan lääkkeen tarkkaa vaikutusmekanismia ei ole saatavilla. Treoniini on välttämätön aminohappo, jolla on rooli proteiinisynteesissä, suoliston limakalvon musiinin tuotannossa sekä glysiinin ja seriinin aineenvaihdunnassa.

Tästä voi periaatteessa johtaa yhteyden suoliston limakalvon eheyteen tai motiliteettiin. Yhteys on kuitenkin spekulatiivinen, eikä toimitetut tiedot tue sitä. Myöskään alkuperäinen käyttöaihe (MSUD, haaraketjuisten aminohappojen aineenvaihduntahäiriö) ei tarjoa selvää mekanistista siltaa gastropareesiin.

Ennustetta tulee siksi pitää vain hypoteesia tuottavana signaalina. Korkea mallipistemäärä ei ole näyttöä kliinisestä tehosta.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä aiheeseen liittyvää kirjallisuutta ei ole saatavilla.

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv (Recordati Rare Diseases) | – | Vaahterasiirappitauti (peruutettu) |

## Turvallisuushuomioita

- **Tietämysgraafin kontraindikaatiot** (TxGNN-tietämysgraafi PrimeKG, ei valmisteyhteenvedon teksti): fenyyliketonuria ja fenyylialaniinin aineenvaihdunnan häiriö.

Lääkkeiden yhteisvaikutuksia ei löytynyt kyselyssä. Muilta osin turvallisuustiedot on luettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennuste perustuu vain korkeaan TxGNN-pistemäärään (L5). Kliinisiä tutkimuksia ja kirjallisuutta ei ole, vaikutusmekanismi puuttuu.

<!-- review:begin fi-lic-20261106-threonine-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kliinisiä tutkimuksia ja kirjallisuutta ei ole, vaikutusmekanismi puuttuu ja ainoa myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-threonine-1 -->

**Eteenpäin siirtymiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden haku Fimeasta, sillä niiden puute estää turvallisuusarvioinnin.
- Vaikutusmekanismitiedot (esim. DrugBankista) mekanistisen yhteyden arvioimiseksi.
- Kirjallisuushaku ja prekliininen näyttö treoniinin vaikutuksesta mahalaukun tyhjenemiseen ja motiliteettiin.
- Reittien ja lääkemuodon yhteensopivuuden arviointi, koska ainoalla myyntiluvalla ei ole lääkemuototietoa.
- Fenyylialaniinin aineenvaihduntaan liittyvän kontraindikaatiosignaalin tarkempi selvitys.

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”ja ainoa myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

