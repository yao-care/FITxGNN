---
layout: default
title: Lecanemab
parent: Pelkkä mallin ennuste (L5)
nav_order: 219
evidence_level: L5
indication_count: 0
---

# Lecanemab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **0** kpl
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

# Lecanemab: Alzheimerin tauti — TxGNN-ennusteiden puuttuvia tietoja

## Yhden lauseen yhteenveto

Lecanemab (kauppanimi Leqembi) on humanisoidun anti-Aβ (amyloidibeta) -yksikköantikorpi, jonka nykyinen hyväksytty käyttöaihe on varhaisen Alzheimerin taudin lievä kognitiivinen heikkeneminen / lievä dementia.
Tässä todiste-paketissa **TxGNN-ennustetulos on tyhjä**, ja sääntelyturvallisuustiedot eivät ole vielä täysin kerätty, joten standardoitua lääkkeen uudelleenkäyttöön liittyvän potentiaalin arviointia ei voida suorittaa.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihe | Varhainen Alzheimerin tauti (Mild Cognitive Impairment / Mild Alzheimer's Dementia) |
| Ennustettu uusi käyttöaihe | Ei sisällytetty — tämä todiste-paketti ei sisällä TxGNN-ennusteita |
| TxGNN-ennusteen pistemäärä | Ei sovellettavissa |
| Todisteen taso | Ei voida arvioida |
| Taiwanin markkina-asema | Ei markkinoilla |
| Hyväksyttyjen lupien lukumäärä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi tämä ennuste on perusteltu?

MOA-kenttä on tällä hetkellä täyttämätön todiste-paketissa, mutta julkaistun farmakalitteratuurin perusteella Lecanemabin toimintamekanismi on jo melko selvä:

Lecanemab sitoutuu etusijaisesti liukoisen Aβ **protofibrileihin**, edistää immuunijärjestelmän puhdistusta ja vähentää aivosairauden amioidipelaaggien kuormitusta, mikä hidastaa Alzheimerin taudin neurodegeneratiivista etenemistä. Tämä mekanismi poikkeaa aiemmista Aβ-monomeereihin tai liukenemattomiin pelaggeihin kohdistuvista vasta-aineista (kuten adukanumaabi), mikä antoi sille tilastollisesti merkitsevän kognitiivisen toimintakyvyn hidastumisen CLARITY AD Phase 3 -tutkimuksessa (CDR-SB vähentyi 27 %).

Koska **predicted_indications**-matriisi on tyhjä, tämä raportti ei voi analysoida mekanismin yhteyttä uusiin käyttöaiheisiin. Kunnes TxGNN-tietokaavio täydentää Lecanemabin solmujen tiedot, kaikki "Alzheimerin taudista X-tautiin" -ennusteet vailla tietopohjaa, eikä niitä pitäisi tehdä.

---

## Taiwan markkina-tiedot

Taiwanissa ei ole tällä hetkellä Lecanemabin hyväksymisluvituksia (kyselyaika 2026-03-29).

Yhdysvallat FDA on myöntänyt Leqembille täyden hyväksynnän heinäkuussa 2023 (Biologics License Application), jonka käyttöaihe on varhaisen oireellisen Alzheimerin tauti. Taiwan-tarkastuksen edistyminen odottaa Fimean verkkosivuston uusimpia ilmoituksia.

---

## Turvallisuusnäkökohdat

TFDA-valmisteen turvallisuustietojen poimintaprojekti on vielä kesken (ks. tietoaukko DG001). FDA-hyväksytyn valmisteen pakkausselosteen ja julkaistun kliinisen aineiston perusteella seuraavat ovat tiedossa olevia keskeisiä turvallisuusvaroituksia, arviointia varten:

- **Kriittiset varoitukset: ARIA (amyloidiin liittyvät imagoingin poikkeavuudet)**
  - ARIA-E (aivojen turvotus / aivojen sulkuonteloiden nestekerääntyminen) ja ARIA-H (aivon mikroverenvuoto / rautanvetoinen hematoidiini-deposiitti) ovat tärkeimmät turvallisuussignaalit, CLARITY AD -tutkimuksessa ARIA-E:n esiintymisaste oli noin 12,6 %, ARIA-H noin 17,3 %.
  - ApoE ε4 -homotsygootti -kantajien riski on merkittävästi kohonnut, hoidon ennen suositellaan genotyyppiä.
  - Säännöllinen MRI-seuranta on tarpeen.
- **Antikoagulantien yhdessä käyttö**: verenvuodon riski kasvaa, vaatii varovaista arviointia.
- **Vakavat allergiset reaktiot / infuusioihin liittyvät reaktiot**: noin 26 % potilaista kokee laskimoinfuusiota, useimmiten lieviä tai keskivaikeita.

> Täydelliset vasta-aiheet ja varoitukset lisätään TFDA-valmisteen pakkausselosteen analysoinnin jälkeen.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Todiste-paketti puuttuu TxGNN-ennustetulos (`predicted_indications` on tyhjä), ja kaksi kriittistä tietoaukkoa (DG001 turvallisuus valmiste, DG002 MOA) eivät ole vielä poistuneet, tällä hetkellä ei voida suorittaa tehokasta arviointia mistään uudesta käyttöaiheesta.

**Etenemiseksi tarvitaan seuraavaa:**

- **\[DG001 — Blocking\]** Lataa Lecanemabin valmisteen pakkausseloste PDF-muodossa Fimean verkkosivustolta ja jäsennä varoitukset / vasta-aiheet, jotta S1-turvallisuuden alustava arviointi voidaan suorittaa
- **\[DG002 — High\]** Täydennä DrugBank MOA -tiedot (DB14580), vahvista Aβ-protofibrileiden sitoutumismekanismi tietokaavion solmuyhteydessä
- **\[Pipeline\]** Varmista, ovatko TxGNN-ennustelinja ottaneet Lecanemabin solmun käyttöön; jos tietokaavion puuttuu riittävästi reunoja (edges), on ensin lisättävä tauti–kohde–lääke-kolmiyhdistelmät ennen kuin ennuste ajetaan uudelleen
- **\[Regulatory\]** Seuraa TFDA-tarkastuksen etenemistä; jos Taiwanissa ei ole vielä Lecanemabin hyväksyntää, vahvista, muutetaanko data-viitteet FDA/EMA-valmisteen perusteiseksi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

