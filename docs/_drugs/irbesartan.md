---
layout: default
title: Irbesartan
parent: Pelkkä mallin ennuste (L5)
nav_order: 238
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
description: "Irbesartan: ennustettu uusi käyttöaihe Malignant hypertensive renal disease (näytön taso L5). Alkuperäinen käyttöaihe: Hypertension"
---

# Irbesartan
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

## Irbesartan: Malignant hypertensive renal disease
{: .text-alpha }

## Yhden lauseen tiivistelmä

Irbesartaani on angiotensiini II -reseptorin (AT1) salpaaja, jota on alun perin käytetty verenpainetaudin hoitoon.
TxGNN-malli ennustaa sen voivan tehota **pahanlaatuiseen renovaskulaariseen hypertensioon**, mutta ennusteen tueksi ei ole toistaiseksi **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään laskennalliseen mallinnukseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hypertension |
| Ennustettu uusi käyttöaihe | Malignant hypertensive renal disease |
| TxGNN-ennustepistemäärä | 0.9931 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 10/10) |
| Myyntilupien määrä | 10 (voimassa: 10) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Irbesartaani salpaa AT1-reseptoria ja estää angiotensiini II:n verisuonia supistavan ja verenpainetta nostavan vaikutuksen. Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Irbesartan (epävirallinen käännös): ”Angiotensiini II on voimakas vasokonstriktori, jota muodostuu angiotensiini I:stä angiotensiinikonvertaasin (ACE, kininaasi II) katalysoimassa reaktiossa. Angiotensiini II on reniini-angiotensiinijärjestelmän tärkein vasoaktiivinen hormoni ja tärkeä tekijä hypertension patofysiologiassa. […] Irbesartaani salpaa angiotensiini II:n verisuonia supistavat ja aldosteronin eritystä lisäävät vaikutukset sitoutumalla selektiivisesti AT 1 -angiotensiini II -reseptoriin, jota esiintyy monissa kudoksissa (esim. verisuonten sileässä lihaksessa ja lisämunuaisessa).” Englanninkielinen alkuteksti: "Angiotensin II is a potent vasoconstrictor formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. […] Irbesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively binding to the AT 1 angiotensin II receptor found in many tissues (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98), versio 2026-08-24; haettu 2026-11-20). Tunnetun lääkeryhmän perusteella mekanismi on kuitenkin biologisesti uskottava tilanteessa, jossa reniini-angiotensiinijärjestelmä on aktivoitunut.

Renovaskulaarisessa hypertensiossa munuaisvaltimon ahtauma aktivoi reniini-angiotensiinijärjestelmää, joten yhteys alkuperäiseen käyttöaiheeseen on ilmeinen. Kyse on pikemminkin alkuperäisen verenpainelääkityksen laajennuksesta kuin aidosta uudelleenkäytöstä. Huomionarvoista on, että AT1-salpaajiin liittyy varoitus molemminpuolisessa munuaisvaltimon ahtaumassa, jossa ne voivat johtaa akuuttiin munuaisten vajaatoimintaan.

Toinen korkeimman pistemäärän ennuste, **pahanlaatuinen hypertensiivinen munuaissairaus**, on pistemäärältään identtinen (0,9931). Tämä viittaa siihen, että ennusteet johtuvat todennäköisesti samasta tietoverkon naapurustosta eivätkä ole toisistaan riippumatonta näyttöä. Angiotensiini II:n aiheuttama verisuonivaurio ja glomerulaarinen hypertensio tekevät yhteydestä uskottavan, mutta pahanlaatuisen (kiihtyneen) hypertension tilannetta ei tue yksikään tutkimus.

Muita ennustettuja käyttöaiheita ovat keuhkoverenpainetaudin muodot (pistemäärä 0,9925). Hypoksiaan liittyvää keuhkoverenpainetautia tukee vain prekliininen aineisto (ks. alla), ja epäselvän monitekijäisen keuhkoverenpainetaudin kohdalla näyttöä ei ole lainkaan.

---

## Kliininen tutkimusnäyttö

Ensisijaiseen ennusteeseen (pahanlaatuinen renovaskulaarinen hypertensio) liittyviä kliinisiä tutkimuksia ei ole rekisteröity. Myöskään muihin ennustettuihin käyttöaiheisiin ei ole löytynyt kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ensisijaiseen ennusteeseen ei ole saatavilla kirjallisuutta. Alla on kolmanneksi sijoittuneen ennusteen (hypoksiaan liittyvä keuhkoverenpainetauti) tärkeimmät julkaisut. Ne ovat lähes kaikki prekliinisiä, eikä niissä ole keuhkovaltimopaineeseen tai keuhkoverisuonten uudelleenmuovautumiseen liittyviä mittareita lukuun ottamatta kahta rottatutkimusta.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Prekliininen (eläin) | Biomed Pharmacother | Irbesartaani lievitti krooniseen vuoristotautiin liittyviä keuhkovaltimomuutoksia rottamallissa kolesterolin aineenvaihdunnan kautta |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Ei luokiteltu | Eur Rev Med Pharmacol Sci | Irbesartaani vähensi oksidatiivista stressiä korkean vuoristoilman keuhkoverenpainetaudin rottamallissa suoliston bakteeriston kautta |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Prekliininen (in vitro) | PLoS One | Irbesartaani suojasi sydänlihassoluja hypoksiastressiltä |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Prekliininen (eläin) | Sleep Breath | Irbesartaani vähensi uniapneaan liittyvää sydänlihaksen apoptoosia |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Prekliininen (eläin) | Am J Physiol Heart Circ Physiol | Irbesartaani esti kroonisen hypoksian stimuloimaa sepelvaltimoiden uudisverisuonten muodostusta vastasyntyneillä rotilla |
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Katsaus | Inflammopharmacology | AT1-reseptorin salpaajien monivaikutteiset suojavaikutukset sydänkudoksen hypoksiassa |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Prekliininen (eläin) | Ren Fail | Irbesartaani lievitti siklosporiinin munuaistoksisuutta (ei suoraan relevantti) |

Osa haetuista julkaisuista ei liity irbesartaaniin (yrttiuutteita koskevat tutkimukset sekä roksadustaatin yliannostapaus), joten ne on jätetty pois.

<!-- review:begin fi-lic-20261106-irbesartan-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kaikki kymmenen myyntilupaa on peruutettu, eikä voimassa olevia lupia ole.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-irbesartan-1 -->

---

## Markkinatiedot Suomessa

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/000141 | Aprovel | irbesartan | Hypertension | Voimassa |
| EMEA/H/C/000142 | Karvea | irbesartan | Hypertension | Voimassa |
| EMEA/H/C/000221 | Karvezide | irbesartan; hydrochlorothiazide | Hypertension | Voimassa |
| EMEA/H/C/000222 | CoAprovel | irbesartan; hydrochlorothiazide | Hypertension | Voimassa |
| EMEA/H/C/000783 | Irbesartan Hydrochlorothiazide Zentiva (previously Irbesart… | irbesartan; hydrochlorothiazide | Hypertension | Voimassa |
| EMEA/H/C/000785 | Irbesartan Zentiva (previously Irbesartan Winthrop) | irbesartan | Hypertension | Voimassa |
| EMEA/H/C/000962 | Ifirmasta (previously Irbesartan Krka) | irbesartan hydrochloride | Hypertension | Voimassa |
| EMEA/H/C/001093 | Irbesartan Teva | irbesartan | Hypertension | Voimassa |
| EMEA/H/C/001112 | Irbesartan/Hydrochlorothiazide Teva | irbesartan; hydrochlorothiazide | Hypertension | Voimassa |
| EMEA/H/C/002302 | Ifirmacombi | irbesartan; hydrochlorothiazide | Hypertension | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole tämän raportin aineistossa saatavilla, joten niihin tulee tutustua valmisteyhteenvedosta.

Tietämysverkosta (PrimeKG) johdetut vasta-aiheisiin viittaavat yhteydet (eivät valmisteyhteenvedon tekstiä) liittyvät muun muassa seuraaviin tiloihin:
- angioedeema (myös ACE:n/reniini-angiotensiinijärjestelmän salpaajien aiheuttama)
- haimatulehdus
- systeeminen lupus erythematosus
- diabetes ja diabeettinen ketoasidoosi
- kihti ja hyperurikemia
- hypotensio
- maksakooma ja maksaenkefalopatia
- anuria
- munuaisvaltimon tukos
- hyperkalsemia, hyperparatyreoosi ja nefrokalsinoosi
- lihassairaudet ja rabdomyolyysi

**Lääkeyhteisvaikutukset** (100 löydöstä; esimerkit):
- **Merkittävät (Major):** kaliumsitraatti, kaliumbikarbonaatti (hyperkalemian riski)
- **Kohtalaiset (Moderate):** kortikosteroidit (hydrokortisoni, deksametasoni, betametasoni, triamsinoloni, budesonidi), asetyylisalisyylihappo, SGLT2-estäjät (kanagliflotsiini, dapagliflotsiini, empagliflotsiini), insuliinit (aspart, degludek), morfiini, bupropioni, aprepitantti, dronabinoli sekä suolenpuhdistusvalmisteet

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste on uskottava mekanistisesti, mutta se on lähinnä alkuperäisen verenpainekäyttöaiheen laajennus. Näyttö on tasoa L5 (pelkkä mallin ennuste), eikä kliinisiä tutkimuksia tai julkaisuja ole. Valmisteyhteenvedon turvallisuustiedot puuttuvat.
- Hypoksiaan liittyvä keuhkoverenpainetauti (L4) voidaan kirjata tutkimuskysymykseksi, mutta sen näyttö on pelkästään prekliinistä.

<!-- review:begin fi-lic-20261106-irbesartan-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lisäksi kaikki Suomen myyntiluvat on peruutettu ja valmisteyhteenvedon turvallisuustiedot puuttuvat.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-irbesartan-2 -->

**Jatkotoimenpiteet:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta ja läpikäynti (Fimea), koska puute estää turvallisuusseulonnan
- Yksityiskohtaiset vaikutusmekanismitiedot (esim. DrugBankista)
- Kirjallisuushaku ja kliinisten tutkimusten rekisterihaku renovaskulaariselle ja pahanlaatuiselle hypertensiolle
- Arvio munuaisvaltimon ahtauman aiheuttamasta munuaisten vajaatoiminnan riskistä
- Myyntilupatilanteen selvittäminen, jos valmistetta harkitaan käyttöön Suomessa

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Kaikki kymmenen myyntilupaa on peruutettu, eikä voimassa olevia lupia ole” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Lisäksi kaikki Suomen myyntiluvat on peruutettu ja v” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-20 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

