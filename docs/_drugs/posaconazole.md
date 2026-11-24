---
layout: default
title: Posaconazole
parent: Pelkkä mallin ennuste (L5)
nav_order: 352
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: ennustettu uusi käyttöaihe Pneumocystosis (näytön taso L5). Alkuperäinen käyttöaihe: Candidiasis"
---

# Posaconazole
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

## Posaconazole: Pneumocystosis
{: .text-alpha }

## Yhden virkkeen yhteenveto

Posakonatsoli on triatsoliryhmän sienilääke, jota on alun perin käytetty kandidiaasin, muiden sieni-infektioiden (mykoosit), koksidioidomykoosin ja aspergilloosin hoitoon. TxGNN-malli ennustaa sen voivan tehota **pneumokystoosiin** (*Pneumocystis jirovecii* -infektio), mutta suoraa näyttöä on vähän: **1 kliininen tutkimus** (ei testaa posakonatsolia) ja **5 julkaisua** (kaikki epäsuoria) tukevat tätä suuntaa vain välillisesti.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Candidiasis;Mycoses;Coccidioidomycosis;Aspergillosis; Mycoses |
| Ennustettu uusi käyttöaihe | Pneumocystosis |
| TxGNN-ennustepistemäärä | 0.9977 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 3/3) |
| Myyntilupien määrä | 3 (voimassa: 3) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu – ja mitkä ovat sen rajat?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohtien ”Mechanism of Action” ja ”Microbiology” mukaan valmisteesta Posaconazole (epävirallinen käännös): ”Posakonatsoli on atsoliryhmän sienilääke. […] Posakonatsoli estää ergosterolin, sienen solukalvon keskeisen ainesosan, synteesiä estämällä sytokromi P-450 -riippuvaista lanosteroli-14α-demetylaasientsyymiä, joka vastaa lanosterolin muuttamisesta ergosteroliksi sienen solukalvossa. Tämä johtaa metyloituneiden sterolien esiasteiden kertymiseen ja ergosterolin vähenemiseen solukalvossa, mikä heikentää sienen solukalvon rakennetta ja toimintaa.” Englanninkielinen alkuteksti: "Posaconazole is an azole antifungal agent. […] Posaconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84), versio 2026-02-13; haettu 2026-11-20). Yleisen lääketieteellisen tiedon mukaan posakonatsoli on triatsoliryhmän sienilääke, joka estää sienen lanosteroli-14-alfa-demetylaasia (CYP51) ja siten ergosterolin synteesiä. Ergosteroli on useimpien sienten solukalvon keskeinen osa, mikä selittää tehon kandidiaasiin ja aspergilloosiin.

*Pneumocystis jirovecii* poikkeaa kuitenkin useimmista sienistä: sen solukalvossa on vain vähän tai ei lainkaan ergosterolia, ja se käyttää pääasiassa kolesterolia ja muita steroleja. Atsolien kohde on siis pneumokystiksessä suurelta osin poissa. Korkea TxGNN-pistemäärä heijastaa todennäköisesti lääkkeen yleistä sienilääkeprofiilia ja sen läheisyyttä muihin mykooseihin tietämysgraafissa, ei validoitua vaikutusmekanismia pneumokystista vastaan.

Alkuperäisten käyttöaiheiden ja ennustetun käyttöaiheen yhteys on siten lähinnä luokittelullinen (kaikki ovat sieni-infektioita), ei mekanistinen. Tämä arvio perustuu lääkeryhmän yleiseen tietoon, ei toimitettuun aineistoon.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Vaihe 3 | Päättynyt | 602 | Reetsafungiinin (ekinokandiini) tehoa ja turvallisuutta verrattiin vakiohoitoon invasiivisten sieni-infektioiden ehkäisyssä allogeenisen kantasolusiirron saaneilla aikuisilla. Tutkimus ei testaa posakonatsolia pneumokystoosissa. |

Tutkimus on arvioitu heikosti relevantiksi (luokka C), eikä sitä voida pitää suorana vaiheen 3 näyttönä tälle lääkkeelle ja käyttöaiheelle.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Katsaus | Swiss Medical Weekly | Yleiskatsaus yleisiin invasiivisiin sieni-infektioihin (kandidiaasi, aspergilloosi, kryptokokkoosi, pneumokystis-keuhkokuume). Mainitsee, että mould-aktiivinen posakonatsoliprofylaksia on vähentänyt invasiivisia infektioita korkean riskin hematologisilla potilailla. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Katsaus | The Lancet Infectious Diseases | Brittiläisen lääketieteellisen mykologian yhdistyksen päivitetyt suositukset vakavien sieni-infektioiden diagnostiikkaan. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Katsaus | Zhonghua Jie He He Hu Xi Za Zhi | Kiinalaiset ohjeet invasiivisten keuhkosieni-infektioiden diagnostiikkaan ja hoitoon. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Katsaus | Clinical Pharmacokinetics | Sienilääkkeiden pääsy keuhkojen epiteelinestekerrokseen (ELF) eri lääkemuodoilla ja lääkeaineilla. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Kohorttitutkimus | Transplant Infectious Disease | Infektiokomplikaatiot akuutissa graft-versus-host-taudissa maksasiirron jälkeen (retrospektiivinen). |

Mikään julkaisuista ei osoita posakonatsolin tehoa pneumokystoosin hoidossa.

<!-- review:begin fi-lic-20261106-posaconazole-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikki kolme myyntilupaa on tilassa "peruutettu".” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-posaconazole-1 -->

---

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000610 | Noxafil | posaconazole | Candidiasis; Mycoses; Coccidioidomycosis; Aspergillosis | Voimassa |
| EMEA/H/C/005005 | Posaconazole Accord | posaconazole | Mycoses | Voimassa |
| EMEA/H/C/005028 | Posaconazole AHCL | posaconazole | Mycoses | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

**Lääkkeiden yhteisvaikutukset:** Yhteisvaikutuskyselyssä löytyi yhteensä 100 yhteisvaikutusta. Esimerkkejä:

- **Merkittävät (Major):** loperamidi, triamsinoloni, budesonidi
- **Kohtalaiset (Moderate):** famotidiini, ranitidiini, rabepratsoli, omepratsoli, simetidiini, hydrokortisoni, deksametasoni, betametasoni, aprepitantti, klaritromysiini, saksagliptiini, bisakodyyli, pikosulfaatti ja polyetyleeniglykoli

Pelkistä lääkeaineen turvallisuustiedoista (varoitukset, vasta-aiheet) ei ole tällä hetkellä saatavilla tietoa. Katso ne valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu lähinnä mallin korkeaan pistemäärään. Kliininen tutkimus ei testaa posakonatsolia, kirjallisuus on epäsuoraa, ja mekanistisesti *Pneumocystis* on vähäisen ergosterolipitoisuutensa vuoksi atsolien kohteena epätodennäköinen. Näytön taso on L4.
- Valmisteyhteenvedon turvallisuustiedot puuttuvat.

<!-- review:begin fi-lic-20261106-posaconazole-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Valmisteiden myyntiluvat Suomessa on peruutettu, ja valmisteyhteenvedon turvallisuustiedot puuttuvat.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-posaconazole-2 -->

**Eteenpäin siirtyminen edellyttää:**
- Prekliinistä tai kliinistä näyttöä posakonatsolin vaikutuksesta *Pneumocystis jirovecii* -infektioon (in vitro -herkkyys, eläinmallit, tapaussarjat)
- Vertailua nykyiseen vakiohoitoon (esim. trimetoprimi-sulfametoksatsoli)
- Vaikutusmekanismin tietojen täydentämistä (DrugBank)
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivustolta turvallisuusarviota varten
- Selvitystä nykyisestä myyntilupa- ja saatavuustilanteesta Suomessa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Kaikki kolme myyntilupaa on tilassa "peruutettu"” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”almisteiden myyntiluvat Suomessa on peruutettu, ja v” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-20 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

