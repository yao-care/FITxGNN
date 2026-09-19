---
layout: default
title: Ezetimibe
parent: Vahva näyttö (L1-L2)
nav_order: 160
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **4** kpl
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

# Ezetimibe: hyperkolesterolemasta hyperlipoproteinemaan

## Yhden lauseen yhteenveto

Ezetimibe on kolesterolin absorptiota estävä lääke, joka on alun perin kehitetty LDL-kolesteriinin alentamiseen hyperkolesterolemian hoitoon, jota käytetään joko yksinään tai yhdessä statiinin kanssa.
TxGNN-malli ennustaa, että se voi olla tehokas myös **hyperlipoproteinemian** hoitoon, mitä tukee **50 kliinistä tutkimusta** (19 tautiin sopivaa PubMed-haun perusteella) ja **19 julkaisua**, mukaanlukien useita valmistuneita Phase 3 -satunnaistutkimuksia.
Koska hyperlipoproteinemia kuuluu lääkkeen jo vakiintuneiden farmakologisten vaikutusten piiriin, tämä näyttää enemmän nykyisen käytön viralliselta laajentamiselta kuin uudelta mekanistiselta hypoteesilta.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Hyperkolesterolemian hoito (LDL-C/kokonaiskolesteriinin alentaminen, yksinään tai statiinin kanssa) |
| Ennustettu uusi indikaatio | Hyperlipoproteinemia |
| TxGNN-ennusteen pistemäärä | 99.63% |
| Näytön taso | L1 |
| Suomen markkinointi | ✗ Ei markkinoitu |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Jatka varautumisilla |

---

## Miksi tämä ennuste on perusteltu?

Evidence Pack -aineistossa ei tällä hetkellä ole käytettävissä strukturoitua DrugBank-mekanismi-toiminta-tietuetta tälle lääkkeelle (tietokuilussa DG002). Tähän kandidaattiin liittyvän uudelleenkäyttöperustelun mukaan: ezetimibe estää valikoivasti NPC1L1-kuljettajaa suoliston harjasreunan kohdalla, mikä estää ruoan ja sappiissa olevan kolesteriinin imeytymisen (sekä kasvisteroleja). Tämä vähentää kilomikreonien sisältämän kolesteriinin toimittamista maksaan, minkä seurauksena maksa kompensatorisesti lisää hepatiisten LDL-reseptoreiden ilmentymistä ja alentaa LDL-C:tä sekä muita apoB-sisältäviä lipoproteiineja.

Hyperlipoproteinemia on laajempi kliininen luokittelu, joka kattaa kohonneet LDL-C-tasot ja sekalaiset lipidipoikkeamat — pohjimmiltaan patofysiologian, jota ezetimibe:n ydintoimintamekanismi jo kohdistuu. Tämä ei ole mekanistisen ekstrapolaation siirtymä uudelle tautialueelle; se on lääkkeen olemassa olevan farmakologisen vaikutuksen virallinen kartoitus asiaan liittyvään diagnostiseen luokkaan.

Kliinisten tutkimusten kirjaus vahvistaa tämän: ezetimibea on tutkittu monoteerapiana, kiinteissä yhdistelmissä statiinien/fenofibraaatin/bempedoiinihapon kanssa ja aktiivisen vertailuaineen roolissa lukuisissa Phase 3 -tutkimuksissa sekavaisissa hyperlipidemioissa ja hyperkolesterolemian tapauksissa, mikä antaa tälle ennusteelle epätavallisen vahvaa tosielämän kliinistä tukea TxGNN:n johtamalle kandidaatille.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Valmistunut | 611 | Ezetimibe/simvastatiinin ja fenofibraaatin samanaikaisen antamisen arviointi kolesteroolia alentavassa vaikutuksessa sekavaisissa hyperlipidemioissa (korkea kolesteroli + korkeat triglyseridit) |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Phase 3 | Valmistunut | 615 | Evolocumabia verrattuna lumelääkkeeseen ja ezetimibeen (aktiivinen verrokkiaine) LDL-C-muutoksissa matalan Framingham-riskin hyperkolesterolemisilla aikuisilla |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Valmistunut | 407 | Obicetrapii 10 mg/ezetimibe 10 mg:n kiinteä yhdistelmä maksimaalisen siedetyn hoidon lisäksi HeFH/ASCVD-potilailla |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Valmistunut | 245 | IVUS-mitatun sepelvaltimon plakkin regressio kolesteriiinin absorptiota estävän lääkkeen (ezetimibe) ja synteesiä estävän lääkkeen välillä |
| [NCT04433533](https://clinicaltrials.gov/study/NCT04433533) | Phase 4 | Tuntematon | 200 | Rosuvastatiiinin/ezetimibe-yhdistelmää verrattuna rosuvastatiiinin monoterapiaan korealaisia potilaita koskevassa tutkimuksessa vasemman kammion diastolisella toimintahäiriöllä ja hyperlipidemioilla |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Valmistunut | 587 | Fenofibraaatin ja ezetimibe:n samanaikaisen antamisen turvallisuus ja teho sekavaisissa hyperlipidemioissa |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Valmistunut | 576 | Fenofibraaatin/ezetimibe-yhdistelmän samanaikaisen antamisen Phase 3 -tutkimus sekavaisissa hyperlipidemioissa |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Valmistunut | 181 | Fenofibraatti vs. ezetimibe vs. yhdistelmä Type IIb dyslipidemioissa metaboliaoireyhtymän piirteineen |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Valmistunut | 50 | Ezetimibe 10 mg:n lisäannos atorvastatiiniin tai simvastatiiniin homotsygoottisessa perheperustaisessa hyperkolesterolemioissa |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Valmistunut | 1794 | 52 viikon pituinen japanilainen markkinoinnin jälkeinen seuranta Zetian (ezetimibe) monohoidon ja yhdistelmähoidon turvallisuudesta ja tehokkuudesta |

---

## Kirjallisuusaineiston näyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM Phase 3 RCT: obicetrapii/ezetimibe-kiinteä yhdistelmä alentaa merkittävästi LDL-C:tä |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Suun kautta otettava PCSK9-esto enlicitide:n satunnaistutkimus heterotsygoottisessa familiaalisessa hyperkolesterolemioissa väestössä, jota on historiallisesti hoidettu ezetimibe-pohjaisilla hoitoskeemoilla |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Katsaus | Int J Mol Sci | Ruoanjälkeisen hyperlipidemian patofysiologia, diagnostiikka ja hoito sekä yhteys ateroskleroosiiin |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Katsaus | Mol Med Rep | Katsaus nykyisistä hyperlipidemioita ja ASCVD-profylaksiaa kohtelevista lääkkeistä |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Katsaus | J Cardiovasc Pharmacol Ther | Kattava katsaus PCSK9-estäjistä potilaissa, jotka eivät saavuta LDL-C-tavoitteita statiinilla/ezetimibellä |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Katsaus | J Am Coll Cardiol | Uudet ja kehittyvät LDL-C/apoB-alenevat terapiat, ezetimibe:n sijoittaminen hoitomaisemaan |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Katsaus | Circulation Research | Yleiskatsaus kolesteroolia alentaviin lääkkeisiin, mukaanlukien ezetimibe ja PCSK9-estäjät |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Katsaus | Cardiology Clinics | Perinnöllisen hyperkolesterolemian hoito, jossa mainitaan statiinit, ezetimibe ja LDL-afereeesi perushoitoina |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Katsaus | Drug and Therapeutics Bulletin | Päivitys ezetimibe:n LDL/kokonaiskolesteriinin alentavista vaikutuksista yksinään tai yhdessä statiinien kanssa |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Pääkirjoitus | New England Journal of Medicine | Pääkirjoituksen kommentti kolesteroolia alentavista vaikutuksista ja ezetimibe:stä |

---

## Suomen markkinointitiedot

Ezetimibe ei ole tällä hetkellä markkinoitu Suomessa tämän Evidence Pack -aineiston mukaan — arkistoitujen markkinointilupien määrä on 0 (`taiwan_regulatory.total_licenses = 0`, `market_status = Not marketed`). Fimean lupaa koskevat tiedot eivät ole saatavilla.

---

## Turvallisuusnäkökohdat

Turvallisuustiedoista on viitattava pakkausselosteeseen. (Evidence Pack:n keskeiset varoitukset, vasta-aiheet ja lääkeinteraktioiden tiedot puuttuvat kokonaan — DG001 "TFDA/Fimean pakkausselosteen varoitukset ja vasta-aiheet" on merkitty **estäväksi** tietokuiluksi, joka on ratkaistava ennen kuin kattava turvallisuusarviointi voi jatkua.)

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varautumisilla**

**Perustelut:**
Ennustettu indikaatio on vahvasti tuettu — näytön taso L1, useiden valmistuneiden Phase 3 -satunnaistutkimusten kera, joissa ezetimibe:ä arvioitiin suoraan (yksinään tai kiinteässä yhdistelmässä) hyperlipoproteinemia-/sekavaisen hyperlipidemian populaatioissa, ja mekanismi on ezetimibe:n jo vakiintuneet farmakologiset vaikutukset pikemminkin kuin uusi hypoteesi. Lääkettä ei kuitenkaan ole tällä hetkellä markkinoitu Suomessa ja paikalliset turvallisuus- ja merkintätiedot puuttuvat kokonaan, joten varautumistoimia vaaditaan ennen mitään paikallista kehitystä tai viestintää.

**Jatkamiseksi seuraava on tarpeen:**
- TFDA/Fimean pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä (DG001)
- Strukturoitu DrugBank MOA -tietue DG002:n muodolliseksi sulkemiseksi
- Suomen-spesifinen sääntelytie-arviointi ottaen huomioon nykyinen "ei markkinoitu" -tila (0 lupaa)
- Lääkkeiden väliset interaktiotiedot (nykyinen DDI-kysely palautti `not_found`)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

