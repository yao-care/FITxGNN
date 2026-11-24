---
layout: default
title: Ramucirumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "RAMUCIRUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
description: "Ramucirumab: ennustettu uusi käyttöaihe Kohdun ligamentin adenokarsinooma (uterine ligament adenocarcinoma) (näytön taso L5). Alkuperäinen käyttöaihe: Stomach Neoplasms"
---

# Ramucirumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

## Ramucirumab: Kohdun ligamentin adenokarsinooma (uterine ligament adenocarcinoma)
{: .text-alpha }

## Yhden lauseen yhteenveto

Ramusirumabi on VEGFR2-reseptoria estävä vasta-aine, jota on alun perin käytetty mahasyövän hoitoon. TxGNN-malli ennustaa sen voivan tehota **kohdun ligamentin adenokarsinoomaan**, mutta tälle käyttöaiheelle ei ole **yhtään kliinistä tutkimusta eikä julkaisua**, joten ennuste perustuu pelkästään mallin laskemaan pisteytykseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Stomach Neoplasms |
| Ennustettu uusi käyttöaihe | Kohdun ligamentin adenokarsinooma (uterine ligament adenocarcinoma) |
| TxGNN-ennustepisteet | 0.9995 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste on perusteltu?

Ramusirumabi on VEGFR2:ta (verisuonten endoteelikasvutekijän reseptori 2) kohdentava vasta-aine. VEGF/VEGFR2-reitin ohjaama verisuonten uudismuodostus on biologisesti uskottava tekijä myös gynekologisissa adenokarsinoomissa. Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Ramucirumab (epävirallinen käännös): ”Ramusirumabi on VEGFR2-antagonisti, joka sitoutuu spesifisesti VEGFR2:een ja estää VEGFR-ligandien VEGF-A:n, VEGF-C:n ja VEGF-D:n sitoutumisen. Tämän seurauksena ramusirumabi estää VEGFR2:n ligandin stimuloimaa aktivaatiota ja siten ihmisen endoteelisolujen ligandin indusoimaa proliferaatiota ja migraatiota. Ramusirumabi esti angiogeneesiä in vivo -eläinmallissa.” Englanninkielinen alkuteksti: "Ramucirumab is a VEGFR2 antagonist that specifically binds VEGFR2 and blocks binding of VEGFR ligands, VEGF-A, VEGF-C, and VEGF-D. As a result, ramucirumab inhibits ligand-stimulated activation of VEGFR2, thereby inhibiting ligand-induced proliferation, and migration of human endothelial cells. Ramucirumab inhibited angiogenesis in an in vivo animal model." ([DailyMed: Cyramza (ramucirumab) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4), versio 2026-06-09; haettu 2026-11-19).

Mahasyöpä ja ennustettu kohdun ligamentin adenokarsinooma ovat molemmat adenokarsinoomia, joiden kasvu voi olla riippuvaista angiogeneesistä. Yhteys on kuitenkin löyhä: ennuste nojaa yksinomaan TxGNN-mallin pisteisiin, eikä sitä tue mikään kliininen näyttö tälle käyttöaiheelle.

<!-- review:begin fi-lic-20261112-ramucirumab-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”Mahasyöpä (tila: mitätöity)” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan Cyramzan (EMEA/H/C/002829) myyntilupa on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261112-ramucirumab-1 -->

Samankaltaisia ennusteita mallin kärkisijoilta ovat muun muassa kohdunkaulan endoserviikaalinen karsinooma, kohdunkaulan adenoidikystinen karsinooma sekä useat kohdun ligamentin adenokarsinoomien histologiset alatyypit (seroosi, endometrioidi, kirkassoluinen, musinoottinen). Kaikissa näissä näyttö on L5-tasoa. Kohdunkaulan syövässä anti-angiogeeninen hoito (bevasitsumabi) on osoittanut tehoa, mikä antaa epäsuoran biologisen perustelun. Signettisolu- ja suolen tyyppiset kohdunkaulan musinoottiset adenokarsinoomat muistuttavat histologisesti maha-suolikanavan syöpää, mutta tämä ei ole näyttöä tehosta. Korkeat pisteet johtuvat todennäköisesti jaetuista kohdunkaulansyövän ontologiaa koskevista naapurisolmuista eikä tautikohtaisesta datasta.

---

## Kliininen tutkimusnäyttö

Tälle käyttöaiheelle ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Aiheesta ei ole tällä hetkellä saatavilla asiaan liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/002829 | Cyramza | ramucirumab | Stomach Neoplasms | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (VEGFR2-vasta-aine), ei perinteinen sytotoksinen solunsalpaaja |
| Luuydinsuppression riski | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Oksentelua aiheuttavuus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Seurantakohteet | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |

---

## Turvallisuusnäkökohdat

Varoituksista ja vasta-aiheista ei ole tämän raportin aineistossa tietoa. Turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

**Lääkeaineyhteisvaikutukset:** Aineistossa on yhteensä 100 yhteisvaikutusta, joista tässä on esitetty 20 ensimmäistä. Merkittävimmät (vakavuusluokka "Major") liittyvät erityisesti verenvuotoriskiin ja veren hyytymiseen vaikuttaviin lääkkeisiin:

- **Verihiutaleiden estäjät ja antikoagulantit:** asetyylisalisyylihappo, abtsiksimabi, alteplaasi, antitrombiini III, apiksabaani, betriksabaani, bivalirudiini, kangrelori, kaplasitsumabi, silostatsoli, klopidogreeli, daltepariini, defibrotidi
- **Radioaktiiviset vasta-aineet:** ibritumomabitiuksetaani, tositumomabi (myös I-131)
- **Muut:** deferasiroksi

Keskivaikeita (Moderate) yhteisvaikutuksia on mm. deksfenfluramiinin, fenfluramiinin ja sibutramiinin kanssa.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-pisteisiin (L5), eikä ainuttakaan kliinistä tutkimusta tai julkaisua ole. Lisäksi turvallisuustiedot puuttuvat.

<!-- review:begin fi-lic-20261112-ramucirumab-2 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”Lisäksi ramusirumabin myyntilupa Suomessa on mitätöity ja turvallisuustiedot puuttuvat.” Poistettu: EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan Cyramzan (EMEA/H/C/002829) myyntilupa on voimassa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261112-ramucirumab-2 -->

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimea), jotta turvallisuusseulonta voidaan tehdä
- Tarkka vaikutusmekanismi (DrugBank)
- Prekliininen tai kliininen näyttö ramusirumabista gynekologisissa adenokarsinoomissa, sekä kirjallisuushaku ja tutkimusrekisterien selvitys
- Selvitys valmisteen saatavuudesta ja myyntilupatilanteesta Suomessa
- Verenvuotoriskiin liittyvä yhteisvaikutusten arviointi (antikoagulantit ja verihiutaleiden estäjät)

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-12 | Taulukko: Cyramza (EMEA/H/C/002829) on voimassa, ei mitätöity | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Poistettu: ”ramusirumabin myyntilupa Suomessa on mitätöity” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Cyramza (ramucirumab) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

