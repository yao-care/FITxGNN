---
layout: default
title: Imiquimod
parent: Pelkkä mallin ennuste (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Imiquimod: ennustettu uusi käyttöaihe Esisyövällinen kasvain (pre-malignant neoplasm) (näytön taso L5). Alkuperäinen käyttöaihe: Keratoosi, aktiininen keratoosi"
monitor_inn: "IMIQUIMOD"
predicted_indications: ["benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

# Imikimodi: Aktiinisesta keratoosista esisyövällisiin kasvaimiin

## Yhden lauseen yhteenveto

Imikimodi on paikallisesti iholle levitettävä immuunivastetta muokkaava lääke, jota on käytetty aktiinisen keratoosin, kondylooman ja tyvisolusyövän hoitoon. TxGNN-malli ennustaa sen voivan tehota **esisyövällisiin kasvaimiin** (pre-malignant neoplasm). Ennustetta tukee tällä hetkellä **2 kliinistä tutkimusta** ja **9 julkaisua**, mutta tutkimukset ovat pieniä.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Keratoosi, aktiininen keratoosi |
| Ennustettu uusi käyttöaihe | Esisyövällinen kasvain (pre-malignant neoplasm) |
| TxGNN-ennustepisteet | 99,92 % |
| Näytön taso | L1 (huomautus alla) |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 2 (molemmat peruutettu) |
| Suositeltu päätös | Proceed with Guardrails (eteneminen suojatoimin) |

*Huomautus näytön tasosta:* Taso L1 on kerätyssä aineistossa annettu luokitus. Aineistossa on kuitenkin vain yksi valmistunut vaiheen 3 tutkimus (n=20, ei kontrolliryhmää) ja yksi ennenaikaisesti päättynyt tutkimus (n=9). L1-ehto eli vähintään kaksi valmistunutta vaiheen 3 satunnaistettua tutkimusta ei täyty tiukasti tulkittuna. Näyttö on käytännössä heikompaa, noin L2–L3-tasoa.

---

## Miksi ennuste on järkevä?

Yksityiskohtaista vaikutusmekanismitietoa (MOA) ei ole tässä aineistossa saatavilla. Yleisen farmakologian perusteella imikimodi on TLR7-agonisti, joka käynnistää paikallisen synnynnäisen ja hankitun immuunivasteen (mm. interferoni-alfa, TNF-alfa ja IL-12). Tämä immuunivaste voi poistaa dysplastista epiteeliä. Tämä päätelmä perustuu yleiseen tietoon, ei toimitettuun tietueeseen.

Alkuperäinen käyttöaihe, aktiininen keratoosi, on itsessään esisyövällinen ihomuutos. Ennuste laajentaa siis jo hyväksyttyä käyttöaihetta lähisukuisiin intraepiteliaalisiin neoplasioihin, kuten kohdunkaulan, ulkosynnyttimien ja peräaukon alueen muutoksiin.

Ennusteen piirissä on myös useita muita kohteita, joista suurimmalla osalla ei ole kliinistä näyttöä (esim. sylkirauhasen kasvain, kaulaperäaukon schwannooma). Niille suositus on Hold tai tutkimuskysymys.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Vaihe 3 | Valmistunut | 20 | Avoin tutkimus: imikimodikreemi 5 % kolmena päivänä viikossa aktiinisen keratoosin hoidossa päänalueella. Pieni ja kontrolloimaton, tukee vain vaatimattomasti tehoa ja turvallisuutta. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Vaihe 3 | Päättynyt ennenaikaisesti | 9 | Satunnaistettu tutkimus, jossa paikallista imikimodia käytettiin korkea-asteisen kohdunkaulan intraepiteliaalisen neoplasian hoitoon. Vain 9 osallistujaa, joten teho ei ole arvioitavissa. |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systemaattinen katsaus (Cochrane) | Cochrane Database Syst Rev | Peräaukon kanavan intraepiteliaalisen neoplasian hoitovaihtoehdot. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systemaattinen katsaus (Cochrane) | Cochrane Database Syst Rev | Korkea-asteisen ulkosynnyttimien intraepiteliaalisen neoplasian lääkehoidot. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Katsaus | Int J Mol Sci | Fotodynaamisen hoidon yhdistelmähoidot ihon ei-melanoomasyövissä. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Katsaus | Skin Therapy Letter | Aktiinisten keratoosien nykyhoito; keratoosit voivat edetä levyepiteelisyöväksi. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Katsaus | Semin Cutan Med Surg | Ihon ei-melanoomasyöpien ja esiasteiden paikallishoidot (mm. fluorourasiili, diklofenaakki, imikimodi). |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Tapausselostus | Int J STD AIDS | Korkea-asteinen ulkosynnyttimien intraepiteliaalinen neoplasia hoidettiin onnistuneesti imikimodilla munuaisensiirron saajalla. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Tapausselostus | Int J STD AIDS | Peniksen bowenoidi papuloosi parani imikimodikreemillä. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Prekliininen | Urol Oncol | Kahden TLR7-agonistin farmakokinetiikka rotilla (virtsarakon syöpä). |

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002387 | Zyclara | – | Keratoosi, aktiininen keratoosi (peruutettu) |
| EMEA/H/C/000179 | Aldara | – | Kondyloomat, keratoosi, aktiininen keratoosi, tyvisolusyöpä (peruutettu) |

Molemmat myyntiluvat ovat peruutettuja, joten voimassa olevaa myyntilupaa Suomessa ei ole.

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Immuunivasteen muokkaaja (TLR7-agonisti), ei perinteinen sytotoksinen solunsalpaaja |
| Luuydinsuppression riski | Aineistossa ei tietoa; paikallisesti käytettynä systeeminen altistus on yleensä vähäinen |
| Pahoinvointia aiheuttavuus | Aineistossa ei tietoa |
| Seurantakohteet | Paikalliset ihoreaktiot; tarvittaessa verenkuva sekä maksa- ja munuaisarvot |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja varotoimet |

---

## Turvallisuusnäkökohdat

- **Tietämysgraafin mukaiset vasta-aiheet** (eivät perustu valmisteyhteenvetoon): valoallergiset reaktiot (photoparoxysmal response), valoherkkyyssairaus, autoimmuunisairaus, käänteishyljintäreaktio (graft versus host disease) ja auringonpolttama.
- **Lääkeyhteisvaikutukset:** Aineistossa on 59 mahdollista yhteisvaikutusta (mm. pantopratsoli, morfiini, omepratsoli, prednisoni, simvastatiini, varfariini, klopidogreeli ja ibuprofeeni). Vaikeusasteluokitusta ei ole saatavilla.
- **Kirjallisuuden turvallisuushuomiot:** Yhdessä tapausselostuksessa suun papillomatoosi muuttui pahanlaatuiseksi imikimodihoidon aikana, ja suun alueen off-label-käytön turvallisuutta on kyseenalaistettu. Lisäksi on raportoitu muun muassa jäkälämäinen hiuspohjan tulehdus ja erythema multiforme imikimodihoidon yhteydessä.

Valmisteyhteenvedon varoitukset ja vasta-aiheet eivät ole tässä aineistossa saatavilla, joten niihin on tutustuttava erikseen.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Proceed with Guardrails**

**Perustelut:**
- Ensisijainen ennuste (esisyövälliset kasvaimet) on mekanistisesti uskottava ja lähellä jo hyväksyttyä aktiinisen keratoosin käyttöaihetta. Suorat tutkimukset ovat kuitenkin pieniä, ja toinen päättyi ennenaikaisesti. Eteneminen edellyttää siksi tiukkoja suojatoimia.
- Muut ennustetut kohteet: suun limakalvon ja kielen hyvänlaatuiset kasvaimet sekä odontogeeninen kysta ovat enintään tutkimuskysymyksiä, ja loput (mm. kaulan neuroblastooma, nenänielun teratooma, sisäkorvan kasvain, sylkirauhasen kasvain ja kaulaperäaukon schwannooma) tulee pitää odotustilassa (Hold) ilman näyttöä.

**Eteneminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta Fimeasta (estää turvallisuusarvioinnin etenemisen).
- Yksityiskohtaiset vaikutusmekanismitiedot (esim. DrugBankista).
- Riittävän kokoiset satunnaistetut tutkimukset intraepiteliaalisista neoplasioista (kohdunkaula, ulkosynnyttimet, peräaukko).
- Selvitys Suomen myyntilupatilanteesta (kaikki luvat peruutettu) ja mahdollisista saatavuusvaihtoehdoista.
- Valoherkkyyden, autoimmuunisairauksien ja suun alueen pahanlaatuistumisriskin turvallisuussuunnitelma.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

