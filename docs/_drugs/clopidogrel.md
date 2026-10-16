---
layout: default
title: Clopidogrel
parent: Pelkkä mallin ennuste (L5)
nav_order: 116
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Clopidogrel: ennustettu uusi käyttöaihe Migreeni, johon liittyy aivorunkoaura (sijalla 2: migreenihäiriö) (näytön taso L5). Alkuperäinen käyttöaihe: Perifeeriset verisuonisairaudet, aivohalvaus…"
---

# Clopidogrel
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **8** kpl
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

# Klopidogreeli: Sepelvaltimotaudin ja aivoinfarktin ehkäisystä migreeniin

## Yhden lauseen yhteenveto

Klopidogreeli on verihiutaleiden aggregaatiota estävä lääke, jota on alun perin käytetty sydäninfarktin, akuutin sepelvaltimo-oireyhtymän, aivohalvauksen ja perifeeristen verisuonisairauksien hoitoon ja ehkäisyyn.
TxGNN-malli ennustaa sen voivan tehota ensisijaisesti **migreenihäiriöön** (ja migreeniin, johon liittyy aivorunkoaura).
Tätä suuntaa tukee **6 kliinistä tutkimusta** (joista vain osa testaa klopidogreelia suoraan) ja **20 julkaisua**, mukaan lukien satunnaistetut tutkimukset.

*Huom. raportti keskittyy sijalla 1 olevaan ennusteeseen (aivorunkoauralliseen migreeniin), mutta vahvin näyttö on sijalla 2 olevasta ennusteesta, migreenihäiriöstä. Kliinisten tutkimusten ja kirjallisuuden osiot käsittelevät tämän vuoksi migreenihäiriötä, koska aivorunkoauralliselle migreenille ei ole rekisteröityjä kliinisiä tutkimuksia.*

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Perifeeriset verisuonisairaudet, aivohalvaus, sydäninfarkti (sekä akuutti sepelvaltimo-oireyhtymä) |
| Ennustettu uusi käyttöaihe | Migreeni, johon liittyy aivorunkoaura (sijalla 2: migreenihäiriö) |
| TxGNN-ennustepistemäärä | 99,44 % (migreenihäiriö: 99,44 %) |
| Näytön taso | L3 aivorunkoauralliselle migreenille; L2 migreenihäiriölle |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 16 (kaikki peruutettuja) |
| Suositeltu päätös | Proceed with Guardrails (migreenihäiriö, PFO-/oikea-vasen-oikovirtauspotilaat); Hold (muut ennusteet) |

---

## Miksi ennuste on perusteltu?

Yksityiskohtaisia vaikutusmekanismitietoja (MOA) ei ole tällä hetkellä saatavilla. Tunnetun tiedon perusteella klopidogreeli estää P2Y12-reseptorivälitteistä verihiutaleiden aggregaatiota. Sen teho valtimotromboosin ehkäisyssä on osoitettu, ja mekanistisesti se voi soveltua migreenin ehkäisyyn tietyillä potilasryhmillä.

Migreenissä, johon liittyy aura, erityisesti avoimen foramen ovalen (PFO) yhteydessä, paradoksaalisten mikroembolioiden tai verihiutaleista vapautuvien vasoaktiivisten aineiden (esim. serotoniinin) arvellaan voivan laukaista aivokuoren leviävän depression. Verihiutaleiden aktivaation estäminen voisi siten vähentää kohtauksia.

Alkuperäinen käyttöaihe (verisuonitukokset) ja uusi käyttöaihe (migreeni) kytkeytyvät toisiinsa verihiutaleiden aktivaation ja mikroembolisaation kautta. Näyttö koskee kuitenkin pääosin aurallista migreeniä PFO-potilailla tai sulkutoimenpiteen jälkeisessä tilanteessa. Aivorunkoauralle ominaista tietoa ei ole, joten päätelmä yleisestä aurallisesta migreenistä on epäsuora. Yleiselle migreenin ehkäisylle näyttö on heikkoa.

---

## Kliininen tutkimusnäyttö (migreenihäiriö)

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Vaihe 2 | Päättynyt | 1000 | COMPETE: antitromboottinen/verihiutaleita estävä hoito vs. migreenilääkitys PFO-migreenissä; tulokset julkaistu |
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Vaihe 4 | Päättynyt | 220 | CANOA: klopidogreeli aspiriinin lisänä uuden migreenin ehkäisyssä eteisväliseinän aukon sulkun jälkeen |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Vaihe 4 | Tuntematon | 50 | Klopidogreeli migreenin ehkäisyyn oikea-vasen-oikovirtauspotilailla; ei vahvistettuja tuloksia |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Vaihe 3 | Käynnissä, ei rekrytoi | 440 | SPRING: PFO-sulku vs. lääkehoito migreenissä; interventio on laite, joten epäsuora |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Vaihe 3 | Päättynyt | 664 | PFO-sulku tai antikoagulantti vs. verihiutaleita estävä hoito aivohalvauksen uusiutumisen ehkäisyssä; migreeni ei ole ensisijainen päätetapahtuma |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Ei sovellettavissa | Keskeytetty | 7 | Septaalisulkulaitteen tutkimus; ei informatiivinen klopidogreelin kannalta |

Sijalla 1 olevalle aivorunkoauralliselle migreenille ei ole rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö (migreenihäiriö)

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|------|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | RCT (monikeskus) | BMJ | Antitromboottisen hoidon teho ja turvallisuus migreenin ehkäisyssä PFO-potilailla |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA: klopidogreeli + aspiriini vs. pelkkä aspiriini migreenikohtauksiin eteisväliseinän aukon sulun jälkeen |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT (1 vuoden seuranta) | JAMA Cardiol | Kolmen kuukauden klopidogreelilisä vähensi uusia migreenikohtauksia; tulokset 6–12 kk:n seurannassa |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT (pilotti) | Cephalalgia | Klopidogreeli migreenin ehkäisyssä, pilottitutkimus |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systemaattinen katsaus | Headache | Antitromboottisten lääkkeiden rooli migreenin ehkäisyssä |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Systemaattinen katsaus | Indian J Thorac Cardiovasc Surg | Uusi päänsärky eteisväliseinän aukon katetrisulun jälkeen: ilmaantuvuus ja hoito |
| [38109984](https://pubmed.ncbi.nlm.nih.gov/38109984/) | 2024 | Tutkimusasetelma | Am Heart J | COMPETE-tutkimuksen suunnittelu ja perustelut |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Havainnointitutkimus | J Investig Med | Klopidogreeli täydentävänä ehkäisynä lääkehoitoon reagoimattomassa PFO-migreenissä |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospektiivinen katsaus | Neurology | Tienopyridiinihoito PFO-migreenipotilailla |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospektiivinen katsaus | Cephalalgia | Klopidogreeli ensisijaisena hoitona migreenipotilailla, joilla oikea-vasen-oikovirtaus |

Aivorunkoauralliselle migreenille (sijalla 1) tärkeimmät lähteet ovat pilotti-RCT (PMID 24836213), retrospektiiviset katsaukset (PMID 30478066) ja pienet avoimet tutkimukset (PMID 32848048, 30478067). Aivorunkoauraa koskevaa suoraa näyttöä ei ole.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000174 | Plavix | – | Aivohalvaus, perifeeriset verisuonisairaudet, eteisvärinä, sydäninfarkti, akuutti sepelvaltimo-oireyhtymä |
| EMEA/H/C/000175 | Iscover | – | Aivohalvaus, perifeeriset verisuonisairaudet, eteisvärinä, sydäninfarkti, akuutti sepelvaltimo-oireyhtymä |
| EMEA/H/C/001143 | DuoPlavin | – | Akuutti sepelvaltimo-oireyhtymä, sydäninfarkti |
| EMEA/H/C/000975 | Clopidogrel Zentiva | – | Aivohalvaus, perifeeriset verisuonisairaudet, sydäninfarkti, akuutti sepelvaltimo-oireyhtymä |
| EMEA/H/C/001056 | Clopidogrel Krka | – | Perifeeriset verisuonisairaudet, aivohalvaus, sydäninfarkti |

Kaikki 16 myyntilupaa on peruutettu, eikä voimassa olevia myyntilupia ole.

---

## Sytotoksisuus

Klopidogreeli ei ole syöpälääke, joten tämä osio ei koske sitä.

---

## Turvallisuushuomiot

- **Tietokannan vasta-aiheet (TxGNN-tietograafi, ei valmisteyhteenveto)**: akuutti maksan vajaatoiminta, maksatulehdus, veren hyytymishäiriö, vamma, trombosytopeeninen purppura, aktiivinen mahahaavatauti ja kallonsisäinen verenvuoto.
- **Lääkeyhteisvaikutukset** (yhteensä 100 löydöstä, tärkeimmät):
  - **Merkittävät (Major)**: omepratsoli, esomepratsoli, rabepratsoli, pioglitatsoni, loperamidi, repaglinidi
  - **Kohtalaiset (Moderate)**: asetyylisalisyylihappo, bupropioni, morfiini, simetidiini, klaritromysiini, lansopratsoli, pantopratsoli ja muita
  - **Lievät (Minor)**: deksansopratsoli, glimepiridi
- **Ennusteisiin liittyvät turvallisuussignaalit**: nivelreumaennusteen yhteydessä on raportoitu klopidogreeliin liittyvää tulehduksellista niveltulehdusta (PMID 38107217) ja systeemisessä skleroosissa endoteelitoiminnan heikkenemistä (PMID 27188755). Nivelrikkopotilailla on kuvattu vuotoriskejä (esim. nivelverenvuoto).

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat tästä aineistosta, joten tarkista turvallisuustiedot valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Proceed with Guardrails (migreenihäiriö, PFO-/oikea-vasen-oikovirtauspotilaat); Hold (aivorunkoauralliseen migreeniin sekä nivelrikko-, jännetulehdus-, myosiitti- ja nivelreumaennusteisiin)**

**Perustelut:**
- Migreenihäiriölle on valmistunut vaiheen 2 tutkimus (COMPETE, n=1000) ja julkaistu satunnaistettu monikeskustutkimus sekä CANOA-tutkimus (vaihe 4, RCT). Tulokset ovat kuitenkin ristiriitaisia: hyöty näkyy PFO:hon liittyvässä tai sulkutoimenpiteen jälkeisessä migreenissä, mutta yleisen migreenin ehkäisyssä näyttö on heikko. Vaiheen 3 tutkimukset koskevat PFO-sulkua, eivät klopidogreelia.
- Aivorunkoauralliselle migreenille on vain epäsuoraa näyttöä (L3). Nivelrikko, jännetulehdus, myosiitit ja nivelreuma ovat pääosin pelkkiä malliennusteita ilman kliinistä tukea, ja nivelreumassa on haittasignaaleja.

**Jatkoon tarvitaan:**
- COMPETE-tutkimuksen tulosten yksityiskohtien varmistaminen ja kriittinen arviointi
- Vaikutusmekanismitiedot (MOA) DrugBankista
- Suomen valmisteyhteenvedon varoitukset ja vasta-aiheet turvallisuusarviointia varten
- Selvitys Suomen markkinatilanteesta, koska kaikki myyntiluvat on peruutettu
- Vaiheen 3 satunnaistettu tutkimus nimenomaan PFO:hon liittyvästä aurallisesta migreenistä, mieluiten aivorunkoauralliset potilaat erikseen tarkasteltuina
- Yhteisvaikutusten (erityisesti protonipumpun estäjät ja CYP2C19-välitteiset yhteisvaikutukset) ja vuotoriskin seurantasuunnitelma
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

