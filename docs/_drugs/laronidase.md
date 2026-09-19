---
layout: default
title: Laronidase
parent: Pelkkä mallin ennuste (L5)
nav_order: 214
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Laronidaasi: Arviointi puutteellinen — ei uudelleen käyttötarkoituksen ennustetta saatavilla

## Yhden lauseen yhteenveto

Laronidaasi (DrugBank: DB00090) on rekombinantti entsyymikorvaushoidon lääke, jonka alkuperäisen indikaation tiedot puuttuvat tästä Evidence Pack -paketista.
TxGNN-malli **ei ole tuottanut mitään ennustettuja uusia indikaatioita** tälle yhdisteelle, ja kaksi tietoaukkoa — mekanismi ja turvatiedot — estävät täydellisen uudelleen käyttötarkoituksen arvioinnin.
Tukevia kliinisiä tutkimuksia tai julkaisuja ei ole saatavilla tällä hetkellä.

---

## Pikayhteenveto

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla Evidence Pack -paketissa |
| Ennustettu uusi indikaatio | Ei — ennusteita ei ole luotu |
| TxGNN-ennuste-pistemäärä | N/A |
| Näytön taso | L5 — Ei varsinaisia tutkimuksia, ennustetiedot puuttuvat |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidätetään** |

---

## Miksi tämä ennuste on järkevä?

TxGNN-ennustettuja indikaatioita ei tällä hetkellä ole saatavilla laronidaasille. Ilman kohdeindikaatiota on mahdotonta rakentaa mekanistista perustelua uudelleen käyttötarkoitukselle tai arvioida, onko lääkkeen vaikutusmekanismi siirrettävissä uuden sairauden yhteydessä.

Mekanismin tiedot (DG002) on merkitty korkean vakavuuden tietoaukoksi. Vaikka laronidaasi yleensä tunnistetaan rekombinantin alfa-L-iduronidaasin muodoksi — entsyyminä, joka osallistuu glykosaminoglykaanien hajoamiseen — näitä tietoja ei ole virallisesti lisätty Evidence Pack -pakettiin, ja siksi niitä ei voida lainata minkään ennusteen perustukseksi.

Alkuperäisen indikaation tiedot puuttuvat myös (`original_indications: []`). Yhdessä puuttuvan mekanismin kanssa vaadittavat perustilat uudelleen käyttötarkoituksen arviointikehikossa eivät ole vielä olemassa. Tämä raportti päivitetään, kun tietoaukot on ratkaistu ja TxGNN-ennusteet ovat saatavilla.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

Laronidaasia ei tällä hetkellä markkinoida Suomessa. Hyväksyntöjä ei ole kirjattu.

---

## Turvallisuutta koskevat näkökohdat

Lisätietoja turvallisuudesta löytyy pakkausselosteesta.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pidätetään**

**Perustelut:**
Tämä Evidence Pack -paketti on rakenteellisesti puutteellinen — TxGNN ei ole tuottanut mitään ennustettuja indikaatioita laronidaasille, ja kaksi tietoaukkoa (DG001, DG002) estävät turvallisuuden ja mekanistisen arvioinnin vaadittavat vähimmäissyötteet.

**Jatkamista varten tarvitaan seuraavaa:**

- **Ratkaise DG001 (Estävä):** Hanki Suomen reseptiohjeistus (varoitukset, vasta-aiheet) pakkausselosteesta PDF-muodossa viranomaisen verkkosivuilta
- **Ratkaise DG002 (Korkea):** Täytä mekanismin tiedot käyttämällä DrugBank API:a DB00090:n osalta
- **Täytä `original_indications`:** Tunnettu indikaatio (Mukopolysakkariidoosi tyypin I / Hurler-oireyhtymä) tulisi poimia DrugBankista ja lisätä Evidence Pack -pakettiin
- **Suorita TxGNN-ennustepipeline uudelleen:** Laronidaasi ei näy nykyisessä ennustettujen indikaatioiden tulokseissa — vahvista, oliko yhdiste sisällytetty syöttelääkkeiden luetteloon, ja suorita uudelleen tarvittaessa
- **Suorita näyttöjenkeräys uudelleen:** Kun ennusteet ovat saatavilla, käynnistä kliinisen tutkimuksen ja kirjallisuuden hakupipeline korkeimman arvostetulle ennustetulle indikaatiolle

---

> ⚠️ **Huomautus:** Tämä raportti osoittaa Evidence Pack -paketin tilaa 2026-04-20. Kaikki osiot päivitetään, kun tietoaukot DG001 ja DG002 on ratkaistu ja TxGNN-ennusteet on luotu. Tulokset ovat tarkoitukseltaan vain tutkimuskäyttöä varten eivätkä muodosta lääketieteellistä neuvoa.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

