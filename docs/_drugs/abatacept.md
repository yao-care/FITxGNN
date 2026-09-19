---
layout: default
title: Abatacept
parent: Pelkkä mallin ennuste (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abatacept
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# ABATACEPT: Lääkkeen uudelleenkäyttöä koskevan arvioinnin raportti

## Yhden lauseen yhteenveto

Abatacept (DrugBank: DB01281) on kansainvälisesti tunnettu biologinen aine, jota käytetään immuunijärjestelmän modulointiin, mutta sillä ei tällä hetkellä ole **markkinointilupia Taiwanissa** eikä **alkuperäisen indikaation tietoja** tässä näyttöpaketissa. TxGNN-malli **ei ole luonut ennusteita uusille indikaatioille** tälle lääkkeelle, ja toimintamekanismin ja turvallisuustietojen osalta on kriittisiä tietojen puutteita.

## Nopea yleiskatsaus

| Kohteet | Sisältö |
|------|------|
| Lääkkeen nimi (INN) | ABATACEPT |
| DrugBank-tunnus | DB01281 |
| Alkuperäinen indikaatio | Tietoja ei saatavilla (ei Taiwanin lupia) |
| Ennustettu uusi indikaatio | Ei (ei TxGNN-ennusteita) |
| TxGNN-ennuste-pistemäärä | N/A |
| Näytön taso | L5 — Vain mallinnusennuste; ennusteita ei luotu |
| Taiwanin markkinatilanne | ✗ Ei markkinoilla (Ei markkinoilla) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | **Pidä odottavalla** |

## Miksi tämä ennuste on kohtuullinen?

Tässä näyttöpaketissa ei ole saatavilla yksityiskohtaisia toimintamekanismin tietoja. Abatacept tunnetaan kansainvälisesti selektiivisenä T-solujen ko-stimulaation modulaattorina (CTLA-4-Ig fusioproteiini), joka estää T-solujen aktivaatiota sitoutumalla CD80/CD86-reseptoreihin antigeenia esittävissä soluissa. Se on hyväksytty monissa maissa reumatoidisen nivelreuman, nuorten idiopaattisen nivelreuman ja psoriaattisen nivelreuman hoitoon; kuitenkaan mitään näistä tiedoista ei ole tallennettu nykyisessä Taiwanin sääntelyaineistossa.

Koska TxGNN-malli ei ole luonut ennusteita Abatacept-lääkkeelle uusista indikaatioista, mekanistista yhdystävää analyysia ei voida toteuttaa tässä vaiheessa. Ennusteiden puuttuminen voi johtua Abataceptin riittämättömästä esittämisestä tietokaaviossa, tai se voi viitata siihen, että malli ei tunnistanut korkean luotettavuuden omaavia uudelleenkäyttökandidaatteja pistemäärärajan yläpuolella.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole ilmoitettavia asiaan liittyviä kliinisiä tutkimuksia, koska TxGNN-malli ei ole ennustanut uusia indikaatioita.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole ilmoitettavaa asiaan liittyvää kirjallisuutta, koska TxGNN-malli ei ole ennustanut uusia indikaatioita.

## Taiwanin markkinatiedot

Abatacept ei tällä hetkellä omista **markkinointilupia (許可證)** Taiwanissa. TFDA:n haussa ei löytynyt lupakirjoja (haettu 2026-03-29).

## Turvallisuuden näkökohdat

> Katso turvallisuustiedot lääkkeen pakkausselosteesta.
>
> Kaikki turvallisuuskentät (tärkeimmät varoitukset, vasta-aiheet, lääkkeiden väliset yhteisvaikutukset) puuttuvat tästä näyttöpaketista. Yhteisvaikutushaku ei tuottanut tuloksia. Täydelliset turvallisuustiedot tulee hankkia kansainvälisistä lähteistä (esim. FDA-merkinnät, EMA SmPC) tai DrugBank-täysprofiilista ennen kliinisen arvioinnin jatkamista.

## Tietojen puutteiden yhteenveto

Seuraavat kriittiset tietojen puutteet tunnistettiin ja ne on ratkaistava ennen tämän kandidaatin edistämistä:

| Aukon tunnus | Luokka | Kohta | Vakavuus | Korjaus |
|--------|----------|------|----------|-------------|
| DG001 | Lääkkeen taso | TFDA:n pakkausselosteen varoitukset/vasta-aiheet | **Estävä** | Lataa ja jäsennä pakkausselosteen PDF TFDA:n verkkosivustolta |
| DG002 | Lääkkeen taso | Toimintamekanismi (MOA) | Korkea | Kysy yksityiskohtaisia tietoja toimintamekanismista DrugBank-sovellusliittymästä |

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä odottavalla**

**Perustelut:**
Abatacept-lääkkeellä ei ole TxGNN-ennustettuja uusia indikaatioita nykyisessä analyysissä, sillä ei ole markkinointilupia Taiwanissa, ja tiedoissa on useita kriittisiä puutteita. Näyttöä ei ole riittävästi tämän kandidaatin edistämiseksi uudelleenkäyttöputkessa tässä vaiheessa.

**Jatkamista varten tarvitaan seuraavaa:**
- Ratkaise **DG001 (Estävä)**: Hanki TFDA:n pakkausselosteen varoitukset ja vasta-aiheet tai vastaavat turvallisuustiedot kansainvälisistä sääntelylähteistä (FDA/EMA)
- Ratkaise **DG002 (Korkea)**: Hae yksityiskohtaiset toimintamekanismin tiedot DrugBank-sovellusliittymästä tietokaavion rikastamisen mahdollistamiseksi
- Suorita TxGNN-ennuste uudelleen, kun tietokaavio on päivitetty täydellisillä Abatacept-lääkkeen farmakologisilla tiedoilla
- Jos kansainväliset indikaatiot (esim. reumatoidinen nivelreuma, JIA, psoriaattinen nivelreuma) vahvistetaan, täytä `original_indications` ja arvioi uudelleen uudelleenkäyttömahdollisuuksien osalta
- Varmista, onko Abataceptin puuttuminen Taiwanin markkinoilta sääntelypuute vai strateginen päätös, sillä tämä vaikuttaa uudelleenkäyttöpolun toteutettavuuteen Taiwanissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

