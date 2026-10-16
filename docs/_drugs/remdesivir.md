---
layout: default
title: Remdesivir
parent: Pelkkä mallin ennuste (L5)
nav_order: 373
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Remdesivir: ennustettu uusi käyttöaihe Multippeli endokriininen neoplasia (näytön taso L5). Alkuperäinen käyttöaihe: COVID-19-virusinfektio"
monitor_inn: "REMDESIVIR"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
---

# Remdesivir
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Remdesiviiri: COVID-19-infektiosta moniin endokriiniseen neoplasiaan

## Yhden lauseen yhteenveto

Remdesiviiri on antiviraalinen lääke, jota on alun perin käytetty COVID-19-virusinfektion hoitoon.
TxGNN-malli ennustaa sen voivan tehota **moniin endokriiniseen neoplasiaan** (korkein pistemäärä), mutta tälle ennusteelle ei löydy **yhtään kliinistä tutkimusta eikä julkaisua**.
Ennuste perustuu pelkästään tietoverkkoon pohjautuvaan mallinnukseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | COVID-19-virusinfektio |
| Ennustettu uusi käyttöaihe | Multippeli endokriininen neoplasia |
| TxGNN-ennustepistemäärä | 99,50 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Tällä hetkellä yksityiskohtaisia tietoja vaikutusmekanismista ei ole saatavilla. Tunnetun tiedon mukaan remdesiviiri on nukleotidianalogin esilääke, joka estää viruksen RNA-riippuvaista RNA-polymeraasia. Sen teho COVID-19:ssä on osoitettu.

Multippeli endokriininen neoplasia on perinnöllinen kasvainoireyhtymä (esim. MEN1- ja RET-mutaatiot), jolla ei ole virusten RNA-polymeraasiin liittyvää kohdetta. Tunnistettavaa mekanistista yhteyttä alkuperäisen ja ennustetun käyttöaiheen välillä ei siis ole. Korkea pistemäärä (0,995) on vain verkkopohjainen ennuste, jolta puuttuu biologinen tuki.

**Muut ennustetut käyttöaiheet** (kaikki suositus Hold):

| Sija | Käyttöaihe | Pistemäärä | Näytön taso | Huomio |
|---|---|---|---|---|
| 2 | HIV-infektio | 99,32 % | L4 | Käsitteellinen yhteys (RNA-virus, nukleotidianalogi), mutta HIV-spesifistä vaikutusta ei ole osoitettu |
| 3 | Kissan hankinnainen immuunikatooireyhtymä | 99,07 % | L5 | Eläinlääketieteellinen käyttöaihe, ei tukea |
| 4 | Apinan immuunikatovirusinfektio (SIV) | 99,07 % | L5 | Lähinnä eläinmalli, ei kliininen käyttöaihe |
| 5 | Neurokehityshäiriö (ataksinen kävely, puheen puuttuminen) | 99,03 % | L5 | Ei uskottavaa mekanistista yhteyttä |
| 6 | Homotsygoottinen familiaalinen hyperkolesterolemia | 99,03 % | L5 | Ei uskottavaa mekanistista yhteyttä |

---

## Kliinisen tutkimuksen näyttö

Ensisijaiselle ennusteelle (multippeli endokriininen neoplasia) ei ole rekisteröityjä kliinisiä tutkimuksia.

Toiseksi sijoittuneelle HIV-ennusteelle löytyi yksi tutkimus, jonka relevanssi on heikko (luokka C):

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04385719](https://clinicaltrials.gov/study/NCT04385719) | Vaihe 2 | Päättynyt | 24 | Avoin satunnaistettu kerta-annostutkimus terveillä ugandalaisilla vapaaehtoisilla: tenofoviiri/lamivudiini- tai atatsanaviiri/ritonaviiri-yhdistelmien vaikutus remdesiviirin farmakokinetiikkaan. Kyse on lääkeinteraktio-/farmakokinetiikkatutkimuksesta, ei remdesiviirin tehosta HIV:n hoidossa. |

---

## Kirjallisuusnäyttö

Ensisijaiselle ennusteelle ei ole kirjallisuutta. Alla on tärkeimmät HIV-ennusteeseen liittyvät julkaisut. Ne käsittelevät lähes yksinomaan COVID-19:ää, eivät remdesiviirin HIV-tehoa.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [33264556](https://pubmed.ncbi.nlm.nih.gov/33264556/) | 2021 | RCT | N Engl J Med | WHO:n Solidarity-tutkimuksen väliraportti: uudelleenkäytettyjen viruslääkkeiden (mm. remdesiviiri) vaikutus sairaalahoidettujen COVID-19-potilaiden kuolleisuuteen |
| [35817072](https://pubmed.ncbi.nlm.nih.gov/35817072/) | 2022 | RCT | Lancet Respir Med | Tiksagevimabi-silgavimabi sairaalahoidetuilla COVID-19-potilailla, jotka saivat remdesiviiriä ja tavanomaista hoitoa |
| [42017206](https://pubmed.ncbi.nlm.nih.gov/42017206/) | 2026 | RCT | Clin Infect Dis | Ensitrelviiri sairaalahoidetuilla aikuisilla COVID-19-potilailla, vaiheen 3 tutkimus |
| [41136410](https://pubmed.ncbi.nlm.nih.gov/41136410/) | 2025 | Katsaus | Nat Rev Dis Primers | Akuutin SARS-CoV-2-infektion yleiskatsaus |
| [34696838](https://pubmed.ncbi.nlm.nih.gov/34696838/) | 2021 | Katsaus | The Enzymes | Nukleotidianalogien RNA-replikaation estomekanismit; vertailu SARS-CoV-2:n RdRp:hen, HIV:n käänteiskopioijaentsyymiin ja hepatiitti C:n RdRp:hen |
| [38675889](https://pubmed.ncbi.nlm.nih.gov/38675889/) | 2024 | Kohortti | Viruses | Remdesiviiriresistenssiä ei havaittu vaiheen 3 SIMPLE-tutkimuksissa (COVID-19) |
| [34859557](https://pubmed.ncbi.nlm.nih.gov/34859557/) | 2022 | Kohortti | HIV Med | HIV-positiivisten COVID-19-potilaiden mahdolliset lääkeinteraktiot antiretroviraalisten ja COVID-19-lääkkeiden välillä |
| [35229634](https://pubmed.ncbi.nlm.nih.gov/35229634/) | 2022 | Prekliininen | mBio | Kobisistaatti tehostaa remdesiviirin vaikutusta SARS-CoV-2:ta vastaan soluissa ja hamstereilla |
| [36097825](https://pubmed.ncbi.nlm.nih.gov/36097825/) | 2023 | Kohortti | Clin Infect Dis | Subgenomisen RNA:n seuranta remdesiviirihoidon vasteen arvioinnissa COVID-19-potilailla |
| [33002954](https://pubmed.ncbi.nlm.nih.gov/33002954/) | 2020 | Katsaus | Curr Opin HIV AIDS | Uudelleenkäytettyjen lääkkeiden katsaus COVID-19:n hoidossa |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005622 | Veklury | – | COVID-19-virusinfektio |

Myyntilupa (valmistaja Gilead Sciences Ireland UC) on tilassa peruutettu. Voimassa olevia myyntilupia ei ole.

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Tietokannasta löytyi yhteensä 100 mahdollista yhteisvaikutusta. Ensimmäiset 20 ovat kaikki tasoa "kohtalainen" (Moderate), mm.:
- Antibiootit: doksisykliini, minosykliini, tetrasykliini, klaritromysiini, levofloksasiini, vankomysiini, kanamysiini, neomysiini
- Amfoterisiini B (myös lipidikompleksi)
- Diabeteslääkkeet: akarboosi, pioglitatsoni
- Muut: bupropioni, naltreksoni, mesalatsiini, balsalatsidi, olsalatsiini, kenodeoksikoolihappo, oksandroloni, oksymetoloni

Muista varoituksista ja vasta-aiheista katso valmisteyhteenveto.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ensisijaiselle ennusteelle (multippeli endokriininen neoplasia) ei ole kliinistä tai kirjallista näyttöä eikä uskottavaa mekanistista yhteyttä, joten ennuste on vain mallipohjainen (L5). Lisäksi Suomen myyntilupa on peruutettu.

**Jatkamiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvitys (Fimean sivusto), sillä turvallisuusseulonta ei ole mahdollista ilman niitä
- Vaikutusmekanismitiedot (esim. DrugBank-kyselyllä) mekanistisen yhteyden arviointiin
- Prekliininen näyttö, joka tukisi ennustettua käyttöaihetta, ennen kuin kliinisiä tutkimuksia harkitaan
- Mahdollisesti uusi arvio HIV-ennusteesta (L4), jos remdesiviirin HIV-spesifistä aktiivisuutta voidaan osoittaa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

