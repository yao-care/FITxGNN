---
layout: default
title: Febuxostat
parent: Kohtalainen näyttö (L3-L4)
nav_order: 185
evidence_level: L4
indication_count: 3
last_modified_at: 2026-11-24
description: "Febuxostat: ennustettu uusi käyttöaihe Munuaisperäinen hypourikemia (hypouricemia, renal) (näytön taso L4). Alkuperäinen käyttöaihe: Hyperurikemia, kihti"
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **3** kpl
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

## Febuksostaatti: Munuaisperäinen hypourikemia
{: .text-alpha }

## Yhteenveto

Febuksostaatti on ksantiinioksidaasin estäjä, jota on alun perin käytetty kihdin ja hyperurikemian hoitoon.
TxGNN-malli ennustaa sen voivan olla hyödyllinen **munuaisperäisessä hypourikemiassa**, mutta tuen taustalla on vain **1 kliininen tutkimus** (heikosti relevantti) ja **2 julkaisua**, eikä näyttö ole suoraa.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hyperurikemia, kihti |
| Ennustettu uusi käyttöaihe | Munuaisperäinen hypourikemia (hypouricemia, renal) |
| TxGNN-ennustepistemäärä | 0,9999 |
| Näytön taso | L4 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 3/3) |
| Myyntilupien määrä | 3 (voimassa: 3) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu – ja miksi ei?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Febuxostat (epävirallinen käännös): ”ULORIC on ksantiinioksidaasin estäjä, joka saa aikaan hoitovaikutuksensa pienentämällä seerumin virtsahappopitoisuutta. ULORICin ei odoteta estävän muita puriinien ja pyrimidiinien synteesiin ja metaboliaan osallistuvia entsyymejä hoitopitoisuuksina.” Englanninkielinen alkuteksti: "ULORIC, a xanthine oxidase inhibitor, achieves its therapeutic effect by decreasing serum uric acid. ULORIC is not expected to inhibit other enzymes involved in purine and pyrimidine synthesis and metabolism at therapeutic concentrations." ([DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd), versio 2025-12-24; haettu 2026-11-20). Febuksostaatti on tunnetusti ei-puriininen selektiivinen ksantiinioksidaasin estäjä, joka vähentää virtsahapon tuotantoa. Sen teho kihdissä ja hyperurikemiassa on osoitettu.

Munuaisperäisessä hypourikemiassa tilanne on kuitenkin päinvastainen: seerumin virtsahappo on jo valmiiksi matala, koska virtsahapon takaisinimeytyminen munuaisissa on heikentynyt (esim. URAT1- tai GLUT9-varianttien vuoksi). Virtsahappoa laskevalla lääkkeellä ei ole tälle tilalle selkeää hoidollista perustetta, ja virtsahapon edelleen laskeminen voi olla jopa haitallista. Ainoa uskottava yhteys on kirjallisuus ksantiinioksidoreduktaasin estäjien käytöstä rasituksen aiheuttaman akuutin munuaisvaurion (EIAKI) ehkäisyssä munuaisperäistä hypourikemiaa sairastavilla. Tämä on toistaiseksi hypoteesitasoinen ajatus.

Erittäin korkea TxGNN-pistemäärä johtuu todennäköisesti verkostolähellä olevasta artefaktasta (yhteinen virtsahappoaineenvaihdunnan reitti), ei todellisesta hoitohyödystä.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Vaihe 4 | Tuntematon | 100 | Selvitetään virtsahapon hallinnan vaikutusta kivien uusiutumiseen ja munuaisten toimintaan hyperurikemiapotilailla, joilla on virtsakiviä. Tutkimuksella ei ole todennettavaa yhteyttä munuaisperäiseen hypourikemiaan, eikä sitä voi pitää suorana näyttönä. |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Katsaus | Clinical Rheumatology | Päivitys hypourikemiasta (seerumin urea < 2 mg/dl) reumatologin näkökulmasta, etiologia ja luokittelu |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Tapausraportti | Internal Medicine | Munuaisperäistä hypourikemiaa sairastavan 16-vuotiaan jalkapalloilijan toistuvaa rasituksen aiheuttamaa akuuttia munuaisvauriota yritettiin ehkäistä febuksostaatilla, kun nesteytys ei riittänyt |

---

## Myyntiluvat Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000777 | Adenuric | febuxostat | Gout | Voimassa |
| EMEA/H/C/004374 | Febuxostat Viatris (previously Febuxostat Mylan) | febuxostat | Hyperuricemia; Arthritis, Gouty; Gout | Voimassa |
| EMEA/H/C/004773 | Febuxostat Krka | febuxostat | Hyperuricemia; Gout | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

- **Tietämysgraafin mukaiset vasta-aiheet** (eivät ole valmisteyhteenvedon tekstiä): aivoverenkiertohäiriö, aivoinfarkti, sydäninfarkti, sepelvaltimotromboosi, alttius iskeemiselle aivohalvaukselle sekä hemoglobinopatia.
- **Lääkeyhteisvaikutukset** (yhteensä 22 löydettyä, joista tärkeimmät):
  - **Merkittävät (Major):** atsatiopriini, merkaptopuriini, leflunomidi, teriflunomidi
  - **Kohtalaiset (Moderate):** metotreksaatti, teofylliini, aminofylliini, dyfylliini, oksitrifylliini, tioguaniini, epirubisiini, trabektediini, klofarabiini, pegaspargaasi, asparaginaasi, brentuksimabivedotiini, naltreksoni sekä beeta-interferonit (beeta-1a, beeta-1b, peginterferoni beeta-1a)

<!-- review:begin fi-lic-20261106-febuxostat-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikki kolme myyntilupaa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-febuxostat-1 -->

Valmisteyhteenvedon varoitukset ja vasta-aiheet eivät ole tämän raportin aineistossa, joten ne on tarkistettava valmisteyhteenvedosta.

---

## Muut ennustetut käyttöaiheet (lyhyesti)

- **Osittainen HPRT-puutos** (TxGNN 0,9998, L4): mekanistisesti uskottava virtsahapon tuotannon hallinnassa, mutta löydetty kirjallisuus on tapausraportteja, joissa febuksostaatin tuloksia ei kuvata. Suositus: tutkimuskysymys.
- **Lesch-Nyhanin oireyhtymä** (TxGNN 0,9968, L4): febuksostaatti voisi vaikuttaa vain aineenvaihdunnalliseen osaan, ei neurologisiin ja käytösoireisiin. Lasten käyttö on off-label, ja turvallisuustietoa on vähän. Suositus: tutkimuskysymys.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Mekanistinen peruste on heikko tai jopa ristiriitainen, koska virtsahapon laskeminen ei ole järkevää tilassa, jossa virtsahappo on jo matala. Näyttö rajoittuu yhteen tapausraporttiin ja yleiskatsaukseen, ja ainoa kliininen tutkimus ei liity käyttöaiheeseen.

<!-- review:begin fi-lic-20261106-febuxostat-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Näyttö rajoittuu yhteen tapausraporttiin ja yleiskatsaukseen, ja ainoa kliininen tutkimus ei liity käyttöaiheeseen. Suomessa kaikki myyntiluvat on lisäksi peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-febuxostat-2 -->

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvittäminen Fimean sivuilta (turvallisuusarvioinnin estävä tietoaukko)
- Yksityiskohtainen vaikutusmekanismitieto (esim. DrugBankista)
- Tarkempi arvio siitä, onko febuksostaatilla perusteltua roolia rasituksen aiheuttaman akuutin munuaisvaurion ehkäisyssä, sekä kontrolloituja tutkimuksia
- Sydän- ja verisuoniturvallisuuden arviointi, koska tietämysgraafi liittää lääkkeen sydäninfarkti- ja aivohalvausvasta-aiheisiin
- Jos jatketaan, kannattaa priorisoida osittainen HPRT-puutos ja Lesch-Nyhanin oireyhtymä, joissa mekanistinen perustelu on vahvempi kuin munuaisperäisessä hypourikemiassa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Kaikki kolme myyntilupaa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Suomessa kaikki myyntiluvat on lisäksi peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-20 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

