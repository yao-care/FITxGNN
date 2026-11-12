---
layout: default
title: Rufinamide
parent: Pelkkä mallin ennuste (L5)
nav_order: 390
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "RUFINAMIDE"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: ennustettu uusi käyttöaihe Perioral myoclonia with absences (näytön taso L5). Alkuperäinen käyttöaihe: Epilepsy"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## Yhden lauseen yhteenveto

Rufinamidi on epilepsialääke, jota on käytetty epilepsian hoitoon. TxGNN-malli ennustaa sen voivan tehoa **kuumeeseen liittyvään epilepsiaoireyhtymään (FIRES)**. Ennustetta tukevia **kliinisiä tutkimuksia ei ole** eikä **julkaisuja** ole, joten näyttö perustuu toistaiseksi vain mallin ennusteeseen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Epilepsy |
| Ennustettu uusi käyttöaihe | Perioral myoclonia with absences |
| TxGNN-ennustepisteet | 0.9951 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Tämän raportin tietoihin ei sisälly yksityiskohtaista kuvausta rufinamidin vaikutusmekanismista. Tiedossa on, että rufinamidi on epilepsialääke, joka pidentää jänniteherkkien natriumkanavien inaktiivista tilaa. Sen teho epilepsiassa on osoitettu, ja mekanistisesti se voisi olla sovellettavissa myös FIRES-oireyhtymään.

FIRES on hoitoresistentti epileptinen enkefalopatia, joka ilmenee kuumeisen sairauden jälkeen ja jonka taustalla on pitkälti hermotulehdus. Natriumkanavien salpaus voisi lievittää kohtauksia oireenmukaisesti, mutta se ei puutu taustalla olevaan sairausprosessiin. Korkea ennustepistemäärä (0,996) heijastaa todennäköisesti mallin verkostossa epilepsiaan liittyvien solmujen läheisyyttä, ei sairauskohtaista näyttöä. Ennusteen tulkinnassa on siksi syytä olla varovainen.

### Muut mallin ennustamat käyttöaiheet

| Sija | Käyttöaihe | Pisteet | Huomio |
|------|------|------|------|
| 2 | Perioraalinen myoklonia ja poissaolot | 0.9951 | Natriumkanavasalpaajat voivat pahentaa poissaolokohtauksia, joten sopivuus on epävarma |

Yhdellekään näistä ei ole kliinisiä tutkimuksia tai julkaisuja.

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000660 | Inovelon (Eisai GmbH) | – | Epilepsia (tila: voimassa) |

<!-- review:begin fi-row-20261112-rufinamide-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/000660 / Inovelon (Eisai GmbH) / – / Epilepsia (tila: peruutettu)” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntilupa Inovelon (EMEA/H/C/000660) on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-rufinamide-1 -->

## Turvallisuushuomiot

Tietojoukossa on tunnistettu seuraavat tiedot:

- **Tietämyskaavion (PrimeKG) vasta-aihesuhteet** (eivät perustu valmisteyhteenvetoon): maksan vajaatoiminta, ahdistuneisuushäiriö, neuroottinen häiriö, dysteeminen häiriö, maksasairaus, sappirakon sairaus ja leukopenia.
- **Lääkeyhteisvaikutukset**: tietokannasta löytyi yhteensä 100 yhteisvaikutusta. Esimerkkejä kohtalaisen tason yhteisvaikutuksista: hydrokortisoni, kolekalsiferoli, pioglitatsoni, bupropioni, triamsinoloni, morfiini, betametasoni, kalsitriolia, ondansetroni, metoklopramidi ja prednisoni.

Muilta osin turvallisuustiedoista on tarkistettava valmisteyhteenveto.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennustetta ei tue yksikään kliininen tutkimus eikä julkaisu (näytön taso L5). Ennuste perustuu mallin verkostoläheisyyteen, ja FIRES:n tulehdusperäinen patologia heikentää mekanistista perustetta.

<!-- review:begin fi-lic-20261106-rufinamide-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Ennuste perustuu mallin verkostoläheisyyteen, ja FIRES:n tulehdusperäinen patologia heikentää mekanistista perustetta. Lisäksi ainoa Suomen myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-rufinamide-1 -->

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta Fimeasta (tämä estää turvallisuusseulonnan jatkamisen)
- Rufinamidin vaikutusmekanismin tiedot DrugBankista
- Kirjallisuushaku FIRES-potilaiden rufinamidihoidosta ja mahdollisten tutkimusten rekisteröinti
- Annosmuodon ja antoreitin yhteensopivuuden arviointi

<!-- review:begin fi-lic-20261106-rufinamide-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kirjallisuushaku FIRES-potilaiden rufinamidihoidosta ja mahdollisten tutkimusten rekisteröinti / Selvitys myyntiluvan peruuntumisen syystä ja valmisteen saatavuudesta Suomessa” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-rufinamide-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi ainoa Suomen myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Selvitys myyntiluvan peruuntumisen syystä ja valmisteen saatavuudesta Suomessa” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Inovelon (EMEA/H/C/000660) on voimassa, ei peruutettu | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

