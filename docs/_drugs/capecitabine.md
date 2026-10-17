---
layout: default
title: Capecitabine
parent: Pelkkä mallin ennuste (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Capecitabine: ennustettu uusi käyttöaihe Mahalaukun adenokarsinooma ja mahalaukun proksimaalinen polypoosi (en… (näytön taso L5). Alkuperäinen käyttöaihe: Paksusuolen syöpä, rintasyöpä, kolorektaalis…"
monitor_inn: "CAPECITABINE"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach", "gastric tubular adenocarcinoma", "signet ring cell gastric adenocarcinoma", "gastric cardia adenocarcinoma"]
---

# Capecitabine
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

# Kapesitabiini: Mahasyövästä ja rintasyövästä mahalaukun adenokarsinooman alatyyppeihin

## Yhden lauseen yhteenveto

Kapesitabiini on suun kautta otettava 5-fluorourasiilin esilääke, jonka alkuperäisiä käyttöaiheita ovat paksusuolen syöpä, rintasyöpä, kolorektaalisyöpä ja mahasyöpä. TxGNN-malli ennustaa sen voivan tehota ensisijaisesti ennustelistan kärjessä olevaan **mahalaukun adenokarsinoomaan ja mahalaukun proksimaaliseen polypoosiin (GAPPS)**. Tälle tarkalle diagnoosille ei kuitenkaan löydy yhtään tutkimusta. Vahvin näyttö liittyy listan kolmanteen kohtaan, **mahalaukun tubulaariseen adenokarsinoomaan**, jota tukee 20 julkaisua, mukaan lukien useita vaiheen 3 satunnaistettuja tutkimuksia.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Paksusuolen syöpä, rintasyöpä, kolorektaalisyöpä, mahasyöpä |
| Ennustettu uusi käyttöaihe | Mahalaukun adenokarsinooma ja mahalaukun proksimaalinen polypoosi (ennustelistan sijalla 1) |
| TxGNN-ennustepisteet | 99,94 % |
| Näytön taso | L5 (sijan 1 ennuste); vahvin näyttö sijalla 3 (tubulaarinen adenokarsinooma): L1 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 5 (kaikki peruutettu) |
| Suositeltu päätös | Hold (sijan 1 ennuste); Proceed with Guardrails (tubulaarinen adenokarsinooma) |

### Ennustelistan kymmenen parasta kohdetta

| Sija | Käyttöaihe | Pisteet | Näytön taso | Suositus |
|------|------|------|------|------|
| 1 | Mahalaukun adenokarsinooma ja proksimaalinen polypoosi | 99,94 % | L5 | Hold |
| 2 | Mikroinvasiivinen mahasyöpä | 99,94 % | L5 | Hold |
| 3 | Mahalaukun tubulaarinen adenokarsinooma | 99,94 % | L1 | Proceed with Guardrails |
| 4 | Sinettisolumahasyöpä | 99,94 % | L3 | Tutkimuskysymys |
| 5 | Mahalaukun kardian adenokarsinooma | 99,91 % | L2 | Tutkimuskysymys |
| 6 | Syljenerityskudostyyppinen mahakarsinooma | 99,91 % | L4 | Hold |
| 7 | Mahalaukun pylorus-karsinooma | 99,91 % | L4 | Hold |
| 8 | Mahalaukun korpuksen karsinooma | 99,90 % | L1 | Proceed with Guardrails |
| 9 | Epstein–Barr-virukseen liittyvä mahakarsinooma | 99,90 % | L3 | Tutkimuskysymys |
| 10 | Pahanlaatuinen mahalaukun rakeissolukasvain | 99,89 % | L5 | Hold |

## Miksi ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa ei ole tällä hetkellä saatavilla. Tunnetun tiedon perusteella kapesitabiini on 5-fluorourasiilin (5-FU) esilääke, joka muuttuu aktiiviseksi pääasiassa kasvainkudoksessa ja estää tymidylaattisyntaasia. Sen teho mahasyövässä on osoitettu, ja mekanistisesti se voi soveltua myös mahasyövän alatyyppeihin.

Ennustetut käyttöaiheet ovat pääosin mahalaukun adenokarsinooman eri histologisia tai anatomisia alaryhmiä. Tämä tarkoittaa, että kyse ei ole varsinaisesta uudelleenkäytöstä, vaan alkuperäisen mahasyöpäkäyttöaiheen tarkentumisesta. Tubulaarinen adenokarsinooma on mahasyöpätutkimusten yleisin histologia, ja kapesitabiini on vakiintunut osa CAPOX- ja XP-hoito-ohjelmia liitännäis- ja ensilinjan hoidossa.

Ennusteet eivät ole kaikki yhtä luotettavia. Mikroinvasiivinen (varhainen) mahasyöpä hoidetaan yleensä endoskooppisesti tai leikkauksella, eikä systeemisen solunsalpaajahoidon hyödystä ole näyttöä. Pahanlaatuinen rakeissolukasvain on Schwannin solusta lähtöisin oleva, ei-epiteliaalinen kasvain, joten korkea pistemäärä on todennäköisesti virheellinen positiivinen löydös.

## Kliiniset tutkimukset

Alla on tutkimukset niistä ennustetuista käyttöaiheista, joille tutkimuksia löytyi.

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Vaihe 3 | Päättynyt | 763 | Pembrolitsumabi yksin tai solunsalpaajan (sisplatiini + 5-FU tai kapesitabiini) kanssa vs. lumelääke + solunsalpaaja pitkälle edenneessä mahasyövässä (korpus) |
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Vaihe 2 | Päättynyt | 48 | Oksaliplatiini + kapesitabiini metastaattisessa ruokatorven, GEJ:n ja mahalaukun kardian adenokarsinoomassa |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Vaihe 2 | Päättynyt | 73 | Satunnaistettu laajennettu neoadjuvanttihoito paikallisesti edenneessä ruokatorven, GEJ:n ja kardian adenokarsinoomassa |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | Ei määritelty | Päättynyt | 27 | Dosetakseli, oksaliplatiini ja kapesitabiini + trastutsumabi HER2-positiivisessa edenneessä syövässä; annoksen määritys, ei tehotietoa |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Vaihe 2 | Ei vielä rekrytoi | 66 | AK112 + solunsalpaaja neoadjuvanttina sinettisolua sisältävässä mahasyövässä; kapesitabiinin kuulumista hoitoon ei ole vahvistettu |
| [NCT06349044](https://clinicaltrials.gov/study/NCT06349044) | Ei määritelty | Tila tuntematon | 120 | Hypofraktioitu sädehoito/SBRT + immunoterapia ruoansulatuskanavan syövissä; kapesitabiinin rooli epäselvä |
| [NCT05007106](https://clinicaltrials.gov/study/NCT05007106) | Vaihe 2 | Päättynyt | 611 | MK-7684A (vibostolimabi/pembrolitsumabi) valikoiduissa kiinteissä kasvaimissa; ei kapesitabiinikeskeinen |
| [NCT00021047](https://clinicaltrials.gov/study/NCT00021047) | Vaihe 1/2 | Päättynyt | Ei tietoa | Epirubisiini + karboplatiini + kapesitabiini edenneissä kiinteissä kasvaimissa; ei spesifinen mahasyövälle |
| [NCT00010023](https://clinicaltrials.gov/study/NCT00010023) | Vaihe 1 | Päättynyt | Ei tietoa | Kapesitabiini + suonensisäinen sisplatiini edenneissä ruoansulatuskanavan syövissä; yleinen annosetsintä |

## Kirjallisuusnäyttö

Taulukossa on tärkeimmät julkaisut. Tubulaarisen adenokarsinooman osalta julkaisuja on yhteensä 20.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT (vaihe 3, CLASSIC) | Lancet | Liitännäishoito kapesitabiini + oksaliplatiini D2-gastrektomian jälkeen vs. pelkkä leikkaus |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT (vaihe 3, RESOLVE) | Lancet Oncol | Oksaliplatiini + S-1 vs. oksaliplatiini + kapesitabiini paikallisesti edenneessä mahasyövässä |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | RCT (vaihe 3, RESOLVE) | Lancet Oncol | RESOLVE-tutkimuksen lopullinen selviytymisanalyysi |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT (vaihe 2/3, FLOT4) | Lancet | Perioperatiivinen FLOT vs. ECF/ECX (sisältää kapesitabiinia) |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT (vaihe 3, GLOW) | Nature Medicine | Zolbetuksimabi + CAPOX CLDN18.2-positiivisessa mahasyövässä |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT (vaihe 3, CheckMate 649) | Lancet | Nivolumabi + solunsalpaaja vs. pelkkä solunsalpaaja ensilinjassa |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | RCT (vaihe 3, KEYNOTE-859) | Lancet Oncol | Pembrolitsumabi + solunsalpaaja HER2-negatiivisessa edenneessä mahasyövässä |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | RCT (vaihe 3, ToGA) | Lancet | Trastutsumabi + solunsalpaaja HER2-positiivisessa edenneessä mahasyövässä |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | RCT (vaihe 3, ORIENT-16) | JAMA | Sintilimabi + solunsalpaaja ei-leikattavassa mahasyövässä |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | RCT (vaihe 3, RATIONALE-305) | BMJ | Tislelitsumabi + solunsalpaaja ensilinjassa |
| [16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/) | 2006 | Vaihe 2 | Ann Oncol | Oksaliplatiini + kapesitabiini metastaattisessa ruokatorven, GEJ:n ja kardian adenokarsinoomassa |
| [42026044](https://pubmed.ncbi.nlm.nih.gov/42026044/) | 2026 | Vaihe 2 | Nat Commun | Neoadjuvantti toripalimabi + CapeOX EBV-liitännäisessä mahasyövässä (17 potilasta) |
| [18665164](https://pubmed.ncbi.nlm.nih.gov/18665164/) | 2008 | Vaihe 2 (RCT) | Br J Cancer | Kapesitabiini vs. S-1 ensilinjassa iäkkäillä potilailla |
| [35085931](https://pubmed.ncbi.nlm.nih.gov/35085931/) | 2022 | Kohorttitutkimus | Eur J Cancer | FLOT vs. MAGIC perioperatiivisessa hoidossa (epäsuora) |
| [36051651](https://pubmed.ncbi.nlm.nih.gov/36051651/) | 2022 | Tapausselostus | Case Rep Surg | AFP:tä tuottava mahasyöpä, maksametastaasi hoidettu kapesitabiini/oksaliplatiini-hoidolla |

Huomio: monissa vaiheen 3 tutkimuksissa kapesitabiini on solunsalpaajarungon osa tai vertailuhaara, eikä tutkimuksen päävertailu koske kapesitabiinia sinänsä.

## Markkinatiedot Suomessa

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000316 | Xeloda | – | Paksusuolen syöpä, rintasyöpä, kolorektaalisyöpä, mahasyöpä |
| EMEA/H/C/002568 | Capecitabine Medac | – | Kolorektaalisyöpä |
| EMEA/H/C/002605 | Ecansya (aiemmin Capecitabine Krka) | – | Paksusuolen syöpä, rintasyöpä, kolorektaalisyöpä, mahasyöpä |
| EMEA/H/C/002386 | Capecitabine Accord | – | Paksusuolen syöpä, rintasyöpä, kolorektaalisyöpä, mahasyöpä |
| EMEA/H/C/002362 | Capecitabine Teva | – | Paksusuolen syöpä, rintasyöpä, kolorektaalisyöpä, mahasyöpä |

Kaikki viisi myyntilupaa on merkitty peruutetuiksi, eikä voimassa olevia lupia ole. Luvat ovat EU:n keskitettyjä myyntilupia (EMEA/H/C), joten tilanne kannattaa tarkistaa Fimealta.

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Perinteinen sytotoksinen solunsalpaaja (fluoropyrimidiini) |
| Luuydinsuppression riski | Keskisuuri (neutropenia ja trombosytopenia mahdollisia; tietoa kohdennetusti ei ole saatavilla) |
| Oksentelua aiheuttavuus | Matala–keskisuuri (lääkeryhmän yleisen luokituksen mukaan) |
| Seurattavat parametrit | Verenkuva erittelylaskennalla, maksa- ja munuaisarvot, bilirubiini |
| Käsittelysuojaus | Noudatettava solunsalpaajien käsittelyohjeita |

Tarkemmat tiedot löytyvät valmisteyhteenvedon varoituksista ja varotoimista.

## Turvallisuushuomioita

**Tietograafiin perustuvat vasta-aiheet** (TxGNN-tietämysgraafi, ei valmisteyhteenvedon teksti): maksasairaus, sappirakkosairaus, trombosytopenia, infektiosairaus, neutropenia, agranulosytoosi, sepelvaltimotauti, anemia, makrosyyttinen anemia, hyperbilirubinemia, perinnöllinen hyperbilirubinemia, Gilbertin oireyhtymä, munuaisten vajaatoiminta, äkillinen sydänpysähdys, sydämen johtumishäiriö, nekrotisoiva enterokoliitti, stomatiitti ja dihydropyrimidiinidehydrogenaasin (DPD) puutos.

**Lääkeyhteisvaikutukset:** tietoja on yhteensä 100 yhteisvaikutuksesta. Esimerkkejä:
- Keskivaikeat: metronidatsoli, tinidatsoli
- Lievät: alumiinihydroksidi, levofloksasiini, magaldraatti, magnesiumkarbonaatti, magnesiumhydroksidi, magnesiumoksidi
- Vaikutusasteeltaan tuntemattomat: mm. pantopratsoli, omepratsoli, lansopratsoli, metformiini, morfiini, prednisoni, simvastatiini

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatu, joten ne on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja jatkotoimet

**Päätös: Hold (ennustelistan sija 1); Proceed with Guardrails (tubulaarinen adenokarsinooma ja korpuksen karsinooma)**

**Perustelut:**
- Ennustelistan kärki (GAPPS) perustuu pelkkään mallin ennusteeseen (L5), eikä sille löydy tutkimuksia tai julkaisuja, joten sen edistäminen ei ole perusteltua. Tubulaarisen adenokarsinooman ja korpuksen karsinooman tukena on useita vaiheen 3 satunnaistettuja tutkimuksia (L1), mutta tämä vastaa lääkkeen jo olemassa olevaa mahasyöpäkäyttöaihetta eikä ole todellinen uudelleenkäyttösignaali.
- Kardian karsinoomalla (L2) ja EBV-liitännäisellä mahasyövällä (L3) on rajallisempi tai epäsuora näyttö. Mikroinvasiivinen mahasyöpä, syljenerityskudostyyppinen karsinooma, pylorus-karsinooma ja rakeissolukasvain vaativat lisänäyttöä, ja rakeissolukasvain on todennäköisesti virheellinen positiivinen löydös.

**Jatkaminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (estävä tietoaukko)
- Yksityiskohtainen vaikutusmekanismitieto (DrugBank)
- Histologiakohtaiset alaryhmätiedot tubulaarisesta adenokarsinoomasta
- Hoito-ohjelman yhteys (yhdistelmäkumppani, hoitolinja, HER2-/CLDN18.2-/PD-L1-status) on otettava huomioon
- DPD-puutoksen testaus ja turvallisuusseurantasuunnitelma
- Suomen myyntilupatilanteen selvittäminen, koska kaikki luvat on peruutettu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

