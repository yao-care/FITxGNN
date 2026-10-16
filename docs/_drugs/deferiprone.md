---
layout: default
title: Deferiprone
parent: Kohtalainen näyttö (L3-L4)
nav_order: 133
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-13
description: "Deferiprone: ennustettu uusi käyttöaihe Maksaporfyria (näytön taso L4). Alkuperäinen käyttöaihe: Beta-talassemia"
monitor_inn: "DEFERIPRONE"
predicted_indications: ["hepatic porphyria", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "pyruvate kinase deficiency of red cells", "beta-thalassemia with other manifestations", "pyropoikilocytosis, hereditary"]
---

# Deferiprone
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **9** kpl
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

# Deferipron: Beta-talassemiasta ja rautakuormasta maksaporfyriaan

## Yhteenveto

Deferipron on suun kautta otettava rautakelaattori, jota on alun perin käytetty beta-talassemian yhteydessä esiintyvän rautakuorman hoitoon.
TxGNN-malli ennustaa sen voivan tehota **maksaporfyriaan**,
mutta ennusteen tukena on toistaiseksi vain **2 julkaisua** (prekliinisiä tutkimuksia) eikä yhtään rekisteröityä kliinistä tutkimusta.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Beta-talassemia; rautakuorma |
| Ennustettu uusi käyttöaihe | Maksaporfyria |
| TxGNN-ennustepistemäärä | 99,20 % |
| Näytön taso | L4 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 2 (molemmat peruutettu) |
| Suositeltu päätös | Hold (odota) – käsitellään tutkimuskysymyksenä |

---

## Miksi ennuste on perusteltu?

Tässä raportissa käytetyssä aineistossa ei ole saatavilla yksityiskohtaista vaikutusmekanismitietoa. Tiedossa on kuitenkin, että deferipron on rautakelaattori, jonka teho rautakuorman hoidossa beta-talassemiassa on osoitettu, ja mekanistisesti se voi soveltua myös sellaisiin sairauksiin, joissa rauta on osa taudin syntymekanismia.

Porfyrioissa raudalla on patogeeninen rooli. Porphyria cutanea tardassa (PCT) maksan runsas rautapitoisuus estää uroporfyrinogeenidekarboksylaasin toimintaa. Synnynnäisessä erytropoieettisessa porfyriassa raudan kelaatio voi vähentää hemin synteesin virtaa ja porfyriinien kertymistä.

Haetut kaksi julkaisua tukevat tätä rautariippuvaista mekanismia: vuoden 2020 tutkimus synnynnäisestä erytropoieettisesta porfyriasta ja vuoden 2007 hiirimalli uroporfyriasta. Ne ovat kuitenkin prekliinisiä tai pienimuotoisia tutkimuksia, eivätkä ne ole kliinisiä tutkimuksia maksaporfyriapotilailla.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Prekliininen | Blood | Raudan kelaatio lievitti hemolyyttistä anemiaa ja ihon valoherkkyyttä synnynnäisen erytropoieettisen porfyrian mallissa |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Prekliininen (hiirimalli) | Hepatology | Suun kautta otettavaa rautakelaattoria (deferipronia) ja rautaköyhää ruokavaliota verrattiin maksan uroporfyriinin kertymiseen PCT-hiirimallissa |

---

## Myyntiluvat Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000236 | Ferriprox (peruutettu) | – | Beta-talassemia; rautakuorma |
| EMEA/H/C/004710 | Deferiprone Lipomed (peruutettu) | – | Rautakuorma; beta-talassemia |

---

## Turvallisuusnäkökohdat

**Lääkeaineyhteisvaikutukset:** Yhteisvaikutustietokannasta löytyi yhteensä 100 yhteisvaikutusta. Aineistossa luetelluista tasoltaan kohtalaisia (Moderate) ovat muun muassa:
- Kalsiumia sisältävät valmisteet (kalsiumfosfaatti, -asetaatti, -karbonaatti, -sitraatti, -glukonaatti, -laktaatti)
- Magnesiumia sisältävät valmisteet (magnesiumoksidi, -karbonaatti, -kloridi, -sitraatti, -hydroksidi, -sulfaatti)
- Alumiinihydroksidi, magaldraatti, attapulgiitti, kaoliini ja sukralfaatti
- Rauta

Nämä ovat pääosin antasideja ja metalli-ioneja sisältäviä valmisteita, jotka voivat sitoutua kelaattoriin. Antoajankohtien huolellinen erottelu on syytä selvittää valmisteyhteenvedosta.

Lisäksi valmisteyhteenvedon varoitukset ja vasta-aiheet tulee tarkistaa, sillä niitä ei ole tässä aineistossa saatavilla.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Maksaporfyrian ennuste perustuu korkeaan TxGNN-pisteeseen ja kahteen prekliiniseen tutkimukseen. Kliinistä näyttöä ei ole. Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa, ja turvallisuustiedot (varoitukset, vasta-aiheet) puuttuvat, mikä estää etenemisen turvallisuusseulontaan.

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen ja läpikäynti (estävä aukko)
- Vaikutusmekanismitietojen täydentäminen
- Maksaporfyrian (erityisesti PCT) kliinisten tutkimusten ja tapaussarjojen kartoitus
- Selvitys siitä, miksi myyntiluvat on peruutettu, ja mahdollisen saatavuuden arviointi Suomessa
- Muut ennustetut käyttöaiheet (esim. pyruvaattikinaasin puutos, beta-talassemian muut ilmenemismuodot) ovat joko vailla näyttöä tai päällekkäisiä alkuperäisen käyttöaiheen kanssa, joten niitä ei suositella ensisijaisiksi.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

