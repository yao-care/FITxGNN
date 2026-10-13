---
layout: default
title: Trastuzumab Emtansine
parent: Pelkkä mallin ennuste (L5)
nav_order: 452
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Trastutsumabiemtansiini: Rintasyövästä progesteronireseptorinegatiiviseen rintasyöpään

## Yhteenveto

Trastutsumabiemtansiini on HER2-kohdennettu vasta-aine–lääkekonjugaatti, jota on alun perin käytetty rintasyövän hoitoon.
TxGNN-malli ennustaa sen voivan tehota **progesteronireseptorinegatiiviseen rintasyöpään**,
mutta tukena on vain **1 kliininen tutkimus** (päättynyt ennenaikaisesti, ei tehotuloksia) ja **11 julkaisua**, jotka ovat pääosin katsauksia, hoitosuosituksia ja tapauskertomuksia. Ennuste kuvaa pikemminkin HER2-positiivisen rintasyövän osajoukkoa kuin aitoa uudelleenkäyttöä.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Rintasyöpä |
| Ennustettu uusi käyttöaihe | Progesteronireseptorinegatiivinen rintasyöpä (pääasiallinen tarkasteltu ennuste; ennusteiden järjestyksessä ensimmäinen on "normaali rinnan kaltainen rintasyövän alatyyppi") |
| TxGNN-ennustepistemäärä | 99,82 % |
| Näytön taso | L3 (progesteronireseptorinegatiivinen rintasyöpä); muilla ennusteilla L4–L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota; lisänäyttöä tarvitaan) |

---

## Miksi ennuste on perusteltu?

Tässä raportissa käytetyissä tiedoissa ei ole saatavilla yksityiskohtaista vaikutusmekanismitietoa. Tunnetun tiedon perusteella trastutsumabiemtansiini koostuu HER2:ta tunnistavasta trastutsumabivasta-aineesta ja siihen liitetystä mikrotubuluksia estävästä DM1-solunsalpaajasta. Sen teho rintasyövässä on osoitettu HER2-positiivisessa taudissa.

Ennustetun käyttöaiheen ja alkuperäisen käyttöaiheen suhde on lähinnä alatyyppipohjainen. Progesteronireseptorin (PR) tila ei ole lääkkeen kohde, vaan vaikutus riippuu kasvaimen HER2-positiivisuudesta. HER2-positiivinen, PR-negatiivinen tauti kuuluu jo hyväksytyn käyttöaiheen piiriin, joten kyse on reseptorien mukaan määritellystä osajoukosta eikä varsinaisesta uudelleenkäytöstä.

Muiden ennusteiden mekanistinen perustelu on heikompi. "Normaali rinnan kaltainen" alatyyppi on tyypillisesti HER2-matala tai HER2-negatiivinen, eikä kohdepohjaista perustetta ole. Luminaali A -kasvaimet ovat yleensä HER2-negatiivisia, ja vain luminaali B (HER2+) -kasvaimet osuvat lääkkeen vaikutusmekanismiin. Korkea TxGNN-pistemäärä heijastaa lääkkeen läheisyyttä rintasyöpään tietämysgraafissa, ei alatyyppikohtaista näyttöä.

---

## Kliininen tutkimusnäyttö

| Tutkimustunnus | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Vaihe 2 | Päättynyt ennenaikaisesti | 139 | Adjuvanttisolunsalpaajahoidon kevennystutkimus HER2-positiivisessa, estrogeenireseptorinegatiivisessa, imusolmukenegatiivisessa varhaisen vaiheen rintasyövässä patologisen täydellisen vasteen jälkeen. Ei vahvistettua tietoa siitä, onko T-DM1 tutkimushaarana; tehotuloksia ei ole. |

Muille ennusteille (normaali rinnan kaltainen alatyyppi, PR-positiivinen rintasyöpä, luminaali A tai B) ei ole rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ennuste: progesteronireseptorinegatiivinen rintasyöpä

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Hoitosuositus | Eur J Cancer | EGTM:n biomarkkerisuositukset: HER2-tila on välttämätön anti-HER2-hoidon (mm. T-DM1) valinnassa, ER/PR ohjaa hormonihoitoa |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Kohorttitutkimus | Sci Rep | HER2-positiivisuuden muutoksen ennusteellinen merkitys metastaattisessa rintasyövässä pertutsumabi- ja/tai T-DM1-hoidolla |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Katsaus | Pharmacol Res | Rintasyövän kohdennetut ja solunsalpaajahoidot; hoito ohjautuu HER2-, HR-, ER- ja PR-tilan mukaan |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Katsaus | Clin Adv Hematol Oncol | Uudet kehityssuunnat metastaattisessa rintasyövässä, alatyyppiluokitus |
| [40642740](https://pubmed.ncbi.nlm.nih.gov/40642740/) | 2025 | Tapauskertomus | J Med Cases | Pitkäkestoinen vaste trastutsumabideruxtekaanille kolmoisnegatiivisessa, HER2-mutatoituneessa rintasyövässä (eri ADC-lääke) |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Tapauskertomus | Front Oncol | Pyrotinibi ja metronominen vinorelbiini HER2-positiivisessa, PR-negatiivisessa rintasyövässä, jossa leptomeningeaalinen tauti |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Tapauskertomus | BMJ Case Rep | Reseptorikonversio rintasyövässä (jopa 32 %:lla potilaista) |
| [33482449](https://pubmed.ncbi.nlm.nih.gov/33482449/) | 2021 | Tapauskertomus | Int J Surg Case Rep | Hemodialyysipotilaan metastaattisen rintasyövän yhdistelmähoito |
| [40433060](https://pubmed.ncbi.nlm.nih.gov/40433060/) | 2025 | Tapauskertomus | Surg Case Rep | Miehen piilevä primaarinen rintasyöpä ja ohutsuolimetastaasit |
| [39827242](https://pubmed.ncbi.nlm.nih.gov/39827242/) | 2025 | Kohorttitutkimus | Sci Rep | Rintasyövän potilasperäisten ksenograftien steroidireseptorit ja hoitovaste |
| [37445276](https://pubmed.ncbi.nlm.nih.gov/37445276/) | 2023 | Prekliininen | J Clin Med | Aminosteroidi RM-581 vähentää kaikkien rintasyövän alatyyppien solujen lisääntymistä |

Huomionarvoista on, että yksikään julkaisu ei ole T-DM1:tä PR-negatiivisessa taudissa selvittävä satunnaistettu tutkimus. Luminaali A/B -ennusteen yhteydessä löytyi DESTINY-Breast03:n pitkäaikaisseuranta ([38825627](https://pubmed.ncbi.nlm.nih.gov/38825627/), RCT, 2024, Nat Med), jossa T-DM1 oli vertailuhoitona trastutsumabideruxtekaanille, ei tutkimuksen kohteena.

---

## Myyntitiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002389 | Kadcyla | – | Rintasyöpä (tila: peruutettu) |

---

## Solunsalpaajaominaisuudet

| Kohde | Sisältö |
|------|------|
| Luokitus | Kohdennettu hoito (HER2-kohdennettu vasta-aine–lääkekonjugaatti, jonka solunsalpaajakuorma DM1 on mikrotubuluksen estäjä) |
| Luuydinsuppression riski | Tämän raportin tiedoissa ei ole tietoa; katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksettavuusluokitus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurantaparametrit | Katso valmisteyhteenveto (yleisesti verenkuva sekä maksa- ja munuaisarvot) |
| Käsittelysuojaus | Noudatettava solunsalpaajien käsittelyohjeita |

---

## Turvallisuusnäkökohdat

**Lääkeaineyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 100 yhteisvaikutusta. Merkittäviksi (Major) luokiteltuja ovat muun muassa:
- asetyylisalisyylihappo
- deferasiroksi
- veren hyytymiseen ja trombosyytteihin vaikuttavat lääkkeet: abtsiksimabi, apiksabaani, argatrobaani, betriksabaani, bivalirudiini, kangrelori, kaplasitsumabi ja silostatsoli

Kohtalaisia (Moderate) yhteisvaikutuksia on mm. klaritromysiinin, metronidatsolin, tinidatsolin, naltreksonin, rosuvastatiinin, simvastatiinin, kobisistaatin, sibutramiinin sekä fenfluramiinin ja deksfenfluramiinin kanssa.

Muilta osin turvallisuustiedot, kuten varoitukset ja vasta-aiheet, on katsottava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennustetta tukee vain yksi päättynyt vaiheen 2 tutkimus, jonka yhteys T-DM1:een on vahvistamaton ja jossa ei ole tehotuloksia, sekä pääosin katsauksia, suosituksia ja tapauskertomuksia. Hyöty riippuu HER2-positiivisuudesta, ei PR-tilasta, joten kyse on jo hyväksytyn käyttöaiheen osajoukosta. Lisäksi Suomessa ainoa myyntilupa on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivustolta (turvallisuusarvio on tällä hetkellä estetty)
- Yksityiskohtaisen vaikutusmekanismitiedon täydentämistä (DrugBank)
- Selvitystä siitä, onko NCT04675827:ssä T-DM1 tutkimushaarana, ja sen tulosten saatavuudesta
- Myyntiluvan peruuntumisen syiden ja nykyisen saatavuuden selvittämistä Suomessa
- HER2-tilaan perustuvaa potilasvalintastrategiaa, jossa PR-tila huomioidaan alaryhmänä
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

