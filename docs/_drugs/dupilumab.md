---
layout: default
title: Dupilumab
parent: Kohtalainen näyttö (L3-L4)
nav_order: 130
evidence_level: L3
indication_count: 10
---

# Dupilumab
{: .fs-9 }

Näytön taso: **L3** | Ennustetut käyttöaiheet: **10** kpl
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

# Dupilumab: Atooppisesta dermatitista keuhkoputkentulehdukseen

## Yhden lauseen yhteenveto

Dupilumab on ihmisen monoklonaalinen vasta-aine, joka kohdistuu IL-4Rα-reseptoriin ja estää IL-4/IL-13-signalointia. Tämän aineiston perusteella sillä on vakiintunut käyttö Th2-välitteisissa inflammatorisissa sairauksissa, kuten atooppisessa dermatitissa, astmassa ja eosinofiilistä COPD:ssa. TxGNN-malli ennustaa, että se saattaa olla tehokas myös **keuhkoputkentulehduksessa**, mutta sitä tukee tällä hetkellä vain **1 kliininen tutkimus** (jonka indikaatioissa on ristiriita) ja **6 julkaisua**, joista useimmat käsittelevät itse asiassa astmaa tai COPD:ta pikemminkin kuin keuhkoputkentulehdusta.

---

## Pikayleiskatsaus

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen käyttöaihe | Ei kirjattu tähän aineistoon (suomalaisia myyntilupauksia ei ole saatavilla); tämän paketin kirjallisuustodisteena osoitetaan, että lääke on hyväksytty atooppiseen dermatitiin, astmaan ja eosinofiilistä COPD:han |
| Ennustettu uusi käyttöaihe | Keuhkoputkentulehdus |
| TxGNN-ennusteen pistemäärä | 99.92% (sijoitus 1226) |
| Todistusaste | L3 |
| Suomen markkinatila | ✗ Ei markkinoinnissa |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaiset toimintamekanismin tiedot eivät ole saatavilla strukturoidussa lääketietueessa (`original_moa: [Tietoaukko]`). Tukevan kirjallisuuden perusteella dupilumab on täysin ihmisen IgG4-monoklonaalinen vasta-aine, joka sitoutuu jakoon IL-4Rα ja estää interleukinan-4 ja interleukinan-13 aiheuttaman signaloinnin — pääkytokiinit, jotka ohjaavat Th2/tyypin-2 ilmaväylä- ja ihotulehdusta. Sen tehokkuus Th2-välitteisissa sairauksissa (atooppinen dermatitis, keskivaikea-vaikea astma, eosinofiilistä COPD) on hyvin dokumentoitu todistepaketissa.

Keuhkoputkentulehdus — erityisesti pitkittynyt tai eosinofiilistä keuhkoputkentulehdus — voi jakaa saman Th2/eosinofiilijohtoisen inflammaatiota-reitin, jota nähdään astmassa ja COPD:n äkäyksissä, mikä on TxGNN-ennusteen mekanistinen perusta. Kuitenkin "keuhkoputkentulehdus" erillisen diagnostisena merkintänä on laajempi ja epäspesifisempi kuin astma tai COPD, ja sairauksiin kohdistuvat tutkimus- ja kirjallisuustodisteet on pääosin lainattu vierekkäisistä, paremmin tutkituista sairauksista pikemminkin kuin keuhkoputkentulehduksesta itsestään.

Kriittisesti ainoa haettu kliininen tutkimus (NCT04362501) arvioitiin **C (tietojen epäsuhta)** relevanssitarkistuksessa — sen todellinen kohdepopulaatio on krooninen rinosinusiitti ilman nenäpolyypejä (CRSsNP), ei keuhkoputkentulehdus, ja se jakaa vain taustalla olevan Th2-mekanismin. Tämä tarkoittaa, että mekanistinen perusteltu on uskottava, mutta suoria, sairauksiin kohdistuvia kliinisiä todistetta keuhkoputkentulehduksesta puuttuu tällä hetkellä.

---

## Kliinisen tutkimuksen todisteet

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset tulokset |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Vaihe 2 | Valmis | 33 | Satunnaistettu, kaksoissokea, lumelääkeohjattu tutkimus dupilumabista krooniessa rinosinusiitissa ilman nenäpolyypejä (CRSsNP) — **relevanssiasteen C**: todellinen kohdesairaus on CRSsNP, ei keuhkoputkentulehdus; jakaa vain Th2-inflammaatiomekanismin, merkitty indikaation-epäsuhta |

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT-laajennus (TRAVERSE) | Lancet Respir Med | Pitkäaikainen (>1 vuosi) avoin laajennus, joka vahvistaa dupilumab-turvallisuuden ja jatkuvan tehokkuuden keskivaikeassa-vaikeassa **astmassa**, ei erityisesti keuhkoputkentulehduksessa |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | RCT-osattutkimus (kuvantaminen) | Chest | MRI-pohjainen ilmanvaihto-puutteen kuvantaminen prednisonista riippuvaisissa vakavissa astman potilaissa, jotka saavat anti-T2-biologiset hoitoa |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Järjestelmällinen katsaus/Meta-analyysi | J Asthma | RCT-tutkimusten meta-analyysi dupilumab-tehokkuudesta ja turvallisuudesta hallitsemattomassa **astmassa** |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Katsaus (COPD) | Tuberc Respir Dis | Kattava katsaus farmakologisista hoidoista (mukaan lukien biologiset lääkkeet) **COPD**:n äkäysten ehkäisyyn |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Katsaus | Expert Opin Pharmacother | Käsittelee hoitohaasteita tupakoinnin aiheuttamissa ilmaväylä-sairauksissa, kuten krooniessa keuhkoputkentulehduksessa, emfyseemassa ja astma-COPD-päällekkäisyydessä; toteaa, että nämä potilaat on tyypillisesti suljettu pois suurista tutkimuksista |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Katsaus (pediatrinen muovibronkitis) | Pediatr Pulmonol | Arvioi uusia terapeuttisia vaihtoehtoja eosinofiilistä pediatrista muovia bronkiittiin (tiivistelmä ei ole saatavilla tässä aineistossa) |

---

## Suomen markkinatiedot

Tähän aineistoon ei ole kirjattu suomalaisia myyntilupauksia dupilumabille — `market_status: Not marketed (Not Marketed)`, `total_licenses: 0`.

---

## Turvallisuushuomioita

Turvallisuustiedoista katso pakkausliite.

> Huomautus: **Blocking**-vakavuuden tietoaukko (DG001 — TFDA/Fimea-pakkausliitteen varoitukset ja vasta-aiheet) on kirjattu tähän aineistoon, joka itsessään estää pääsyn S1-turvallisuus-esiarvioinnin vaiheeseen riippumatta siitä, kuinka vahva tehokkuuden todiste on.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
- Keuhkoputkentulehdusta koskevan todisteen on heikko: ainoa kliininen tutkimus on vahvistettu indikaation-epäsuhta (todellinen kohde: CRSsNP), ja kirjallisuus pääosin kattaa astman ja COPD:n pikemminkin kuin keuhkoputkentulehdusta.
- **Blocking**-vakavuuden tietoaukko (puuttuvat pakkausliitteen varoitukset/vasta-aiheet) estää jopa ensimmäisen turvallisuus-seulonnan (S1), riippumatta tehokkuuskysymyksestä.

**Jotta voidaan jatkaa, seuraava on tarpeen:**
- Hae TFDA/Fimea-pakkausliite (varoitukset, vasta-aiheet) S1-turvallisuus-arviointiesteille (DG001)
- Vahvista toimintamekanismi DrugBank API -kyselyn kautta (DG002)
- Hanki keuhkoputkentulehdus-spesifiset (ei astma/COPD-välitystä) kliiniset tutkimukset ja kirjallisuustodisteet, tai virallisesti uudelleenmääritä käyttöaihe paremmin määriteltävään Th2-välitteiseen fenotyyppiin (esim. eosinofiilistä/kroonista keuhkoputkentulehdusta)
- Erillinen huomautus: toisessa ennustetussa käyttöaiheessa **dermatitis** (2. sijalla) tässä samassa aineistossa on huomattavasti vahvempi todiste (L1, useita valmistuneita vaihe-3/4-RCT-tutkimuksia, "Jatka varauksella") ja se saattaa vaatia priorisoidun arvioinnin keuhkoputkentulehduksen edelle

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

