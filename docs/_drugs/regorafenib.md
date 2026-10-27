---
layout: default
title: Regorafenib
parent: Pelkkä mallin ennuste (L5)
nav_order: 371
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Regorafenib: ennustettu uusi käyttöaihe Liposarkoomaan (näytön taso L5). Alkuperäinen käyttöaihe: Kolorektaalisyöpä (paksu- ja peräsuolen syöpä)"
monitor_inn: "REGORAFENIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "renal cell carcinoma associated with neuroblastoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "unclassified renal cell carcinoma", "childhood kidney cell carcinoma", "vulva sarcoma"]
---

# Regorafenib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **8** kpl
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

## Regorafenibi: Kolorektaalisyövästä liposarkoomaan
{: .text-alpha }

## Yhteenveto

Regorafenibi on suun kautta otettava monikinaasi-estäjä, jota on alun perin käytetty paksu- ja peräsuolen syövän (kolorektaalisyövän) hoitoon.
TxGNN-malli ennustaa sen voivan tehota **liposarkoomaan**.
Tätä suuntaa tukee tällä hetkellä **1 kliininen tutkimus** ja **10 julkaisua**, mutta tulokset liposarkoomassa ovat pääosin negatiivisia.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Kolorektaalisyöpä (paksu- ja peräsuolen syöpä) |
| Ennustettu uusi käyttöaihe | Liposarkoomaan |
| TxGNN-ennustepisteet | 99,76 % |
| Näytön taso | L1 (huomautus: liposarkoomakohtainen hyöty on rajallinen) |
| Markkinatilanne Suomessa | Vain peruutettu myyntilupa |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Proceed with Guardrails (eteneminen varauksin) |

---

## Miksi ennuste on perusteltu?

Regorafenibi on monikinaasi-estäjä, joka kohdistuu angiogeneesiä edistäviin kinaaseihin (VEGFR1–3, TIE2), stroomaa koskeviin kinaaseihin (PDGFR, FGFR) sekä onkogeenisiin reseptorityrosiinikinaaseihin (KIT, RET, RAF). Näiden reittien tiedetään ajavan kasvaimen verisuonittumista ja kasvua pehmytkudossarkoomissa, myös liposarkoomassa. Tarkkaa vaikutusmekanismia ei ollut tähän raporttiin koottujen tietojen mukaan saatavilla tietokannasta, joten kuvaus perustuu kirjallisuuden yleiskatsauksiin.

Alkuperäinen käyttöaihe (kolorektaalisyöpä) ja ennustettu käyttöaihe (liposarkooma) ovat molemmat kiinteitä kasvaimia, joissa angiogeneesin esto voi hidastaa taudin etenemistä. Regorafenibista on satunnaistettua näyttöä pehmytkudossarkoomissa (REGOSARC), mikä tukee ennusteen uskottavuutta.

Tärkeä varauma: REGOSARC-tutkimuksessa hyöty todettiin ei-adiposyyttisissä sarkoomissa, mutta **ei liposarkoomassa**. SARC024-tutkimuksen liposarkoomakohortin tulokset eivät myöskään tue regorafenibin rutiinikäyttöä tässä potilasryhmässä.

---

## Kliininen tutkimusnäyttö

| Tutkimustunnus | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Vaihe 2 | Päättynyt | 131 | SARC024: suun kautta otettavan regorafenibin tutkimus valituissa sarkoomatyypeissä, mukaan lukien liposarkooma |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024:n liposarkoomakohortti: tulokset eivät tue regorafenibin rutiinikäyttöä |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC: satunnaistettu, lumekontrolloitu vaiheen 2 tutkimus pitkälle edenneessä pehmytkudossarkoomassa antrasykliinihoidon jälkeen |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | REGOSARC-päivitys: teho todettiin muissa kuin adiposyyttisissä sarkoomissa, ei liposarkoomassa |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT:n jälkianalyysi | Cancer | Elämänlaatuun mukautettu analyysi (Q-TWiST) regorafenibin kliinisestä hyödystä |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Katsaus | Targeted Oncology | Regorafenibin kasvava rooli sarkoomien hoidossa |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Katsaus | Critical Reviews in Oncology/Hematology | Ylläpitohoito pitkälle edenneen pehmytkudossarkooman ensilinjan hoidon jälkeen |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Tutkimusprotokolla | BMC Cancer | REGOSARC-tutkimuksen protokolla |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospektiivinen tutkimus (eri lääke: anlotinibi) | Anti-Cancer Drugs | Anlotinibin teho ja turvallisuus erilaistuneessa/erilaistumattomassa liposarkoomassa |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Tapausselostus (eri lääke: pdatsopanibi) | Rare Tumors | Perustelee Ewingin sarkooma -haaran lisäämistä SARC024-tutkimukseen |

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002573 | Stivarga (Bayer Pharma AG) | Ei tietoa | Kolorektaalisyöpä (tila: peruutettu) |

---

## Sytotoksisuus

Regorafenibi on kohdennettu syöpälääke (monikinaasi-estäjä), ei perinteinen sytostaatti.

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (monikinaasi-estäjä) |
| Myelosuppressioriski | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksettavuusluokitus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurattavat parametrit | Maksan toiminta (kirjallisuudessa raportoitu maksatoksisuus), verenpaine, proteinuria ja iho-oireet (käsi-jalkaihoreaktio) |
| Käsittelysuojaus | Noudata syöpälääkkeiden käsittelyohjeita |

---

## Turvallisuushuomiot

**Lääkeyhteisvaikutukset:** Yhteisvaikutuksia on kirjattu yhteensä 100. Esimerkkejä tärkeimmistä:
- **Merkittävät (Major):** asetyylisalisyylihappo, deferasiroksi, ibritumomabitiuksetaani, tositumomabi, abtsiksimabi, alteplaasi, antitrombiini III ja apiksabaani. Useat näistä liittyvät verenvuotoriskiin tai hyytymisen vaikutuksiin.
- **Kohtalaiset (Moderate):** deksametasoni, klaritromysiini, naltreksoni, rosuvastatiini, kobisistaatti, fenfluramiini ja sibutramiini.
- **Lievät (Minor):** dapagliflotsiini, naloksegoli ja prukalopridi.

Muista turvallisuustiedoista (varoitukset ja vasta-aiheet) katso valmisteyhteenveto.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Proceed with Guardrails (eteneminen varauksin)**

**Perustelut:**
- Regorafenibista on satunnaistettua näyttöä pehmytkudossarkoomissa, mutta nimenomaan liposarkoomassa REGOSARC- ja SARC024-tutkimusten tulokset eivät tue rutiinikäyttöä. Näyttötaso L1 perustuu laajempaan sarkoomanäyttöön, ei liposarkoomakohtaiseen hyötyyn. Lisäksi myyntilupa Suomessa on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista (Fimea) turvallisuusarviointia varten
- Vaikutusmekanismin tietojen täydentämistä (DrugBank)
- Myyntiluvan ja saatavuuden tilanteen selvittämistä Suomessa
- Liposarkoomakohtaisen hyödyn arviointia, esimerkiksi yhdistelmähoitojen tai alatyyppikohtaisten kohorttien avulla
- Muiden ennustettujen käyttöaiheiden (esim. kirkassoluinen munuaissyöpä, jonka näyttö on varhaisvaiheen ja taso L3) tarkempaa arviointia erikseen; harvinaisista munuaissyövän ja sarkooman alatyypeistä ei ole tutkimusnäyttöä (taso L5, suositus Hold)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

