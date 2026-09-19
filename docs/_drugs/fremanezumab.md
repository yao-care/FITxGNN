---
layout: default
title: Fremanezumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 169
evidence_level: L5
indication_count: 2
---

# Fremanezumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Fremanezumabi: migreenienprofylaksiasta brainstem-auralliseen migreeniinn

## Yhden lauseen yhteenveto

> Fremanezumabi on täysin humanisoidtu anti-CGRP-monoklonaalinen vasta-aine, joka on vakiintunut profylaktinen hoito episodiselle ja krooniselle migreeniille.
> TxGNN-malli ennustaa sen voivan olla tehokas myös **brainstem-auralliseen migreeniiin**, harvinaiseen migreenin alatyypille, jossa triptaanit ovat vasta-aiheisiä vasokonstriktion riskin vuoksi.
> Tätä suuntaa tukee tällä hetkellä vain **mekanistinen ja tapaus-tasoinen kirjallisuus (0 varsinaista kliinistä tutkimusta, 20 asiaan liittyvää julkaisua)** — mikään tutkimus ei ole erityisesti rekrytoinut tätä alatyyppiä.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Migreenin profylaksia (episodinen/krooninen migreeni) — kirjallisuustutkimusten perusteella; ei virallisesti vahvistettu Suomen valmisteyhteenvedossa |
| Ennustettu uusi indikaatio | Brainstem-aurallinen migreeni |
| TxGNN-ennusteen pistemäärä | 99.94% |
| Todisteiden taso | L4 (mekanistinen/prekliininen + tapaus-tasoiset todisteet, ei varsinaisia tutkimuksia) |
| Suomen markkinoiden asema | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä (tutkimuskysymys) |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia toimintamekanismin tietoja (DrugBank MOA -kenttä) ei ole saatavilla tässä todistepaketissa [Tietovaje: DG002]. Uudelleenkäytön perustelujen ja tukevien tutkimusten perusteella fremanezumabi on humanisoidtu anti-CGRP-monoklonaalinen vasta-aine, joka estää kalytoniin-geeniin liittyvän peptidien (CGRP) signaloinnin perifeereisesti, mikä estää trigeminovaskulaarisen järjestelmän aktivaatiota — sen vakiintuneen käytön migreenin profylaksiassa perustana (esim. PMID 30725283, "Role of CGRP in Migraine").

Brainstem-aurallinen migreeni on migreenin alaryhmä, joka on systemaattisesti suljettu pois vakiomigreeniudtutkimuksista, historiallisesti siksi, että triptaanit sisältävät vasokonstriktiivisen vasta-aiheisyyden tälle väestölle. Koska CGRP-monoklonaalivasta-aineet toimivat suoran vasokonstriktion sijaan perifeereisen CGRP-estokkeen kautta, ne ovat mekanistisesti uskottavia tälle alaryhmälle ilman triptaanin käyttöä rajoittavia turvallisuushuolia — perustelua vahvistavat tapaus-pohjainen kirjallisuus hemiplegisestä migreeniista ja migreeniista auralla yleisemmin (PMID 35268319, PMID 40264646, PMID 41618146).

Kuitenkin mekanistinen uskottavuus tulisi erottaa suorasta tehokkuuden todisteesta. Prekliiniset tutkimukset käyttäen kortikaalisen leviämisen masennusta (CSD) — hyväksyttyä migreenin auran fysiologista korrelaattia — osoittivat, että fremanezumabi **ei** estänyt CSD-esiintymistä ja ei vaikuttanut CSD-indusoituihin valtimoiden laajenemisiin/plasman proteiinin ekstravasaatioon (PMID 31127003, PMID 31895266), vaikka se hidasti CSD-leviämistä ja lyhensi kortikaalista palautumista yhdessä mallissa. Tämä sekamelska prekliininen signaali tarkoittaa, että tehokkuuden tapaus erityisesti brainstem-aurassa säilyy tutkimuskysymyksenä vakiintuneen mekanistisen siirron sijaan.

---

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole aiheeseen liittyviä kliinisiä tutkimuksia rekisteröitynä.

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|-------|--------|-------|----------|
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Tapausraportteja/Katsaus | J Clin Med | Tarkastellaan niukkoja todisteita anti-CGRP-mAb:ista (ml. fremanezumabi) migreenin auran profylaksiassa huolimatta hyvin dokumentoidusta tehokkuudesta päänsärkyjen kivun suhteen |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Katsaus | Handb Exp Pharmacol | Yleinen katsaus CGRP:n rooliin migreenin patofysiologiassa, mukaan lukien aura-alaryhmä |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Tapausraportti/Katsaus | Frontiers in Neurology | Hemiplegisen migreeni-tapaus (aura-alaryhmä) hoidettuna anti-CGRP-mAb:lla; huomautuksia siitä, että nämä potilaat on systemaattisesti suljettu pois satunnaistetuista kontrolloiduista tutkimuksista |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Yksilöpotilaan analyysi | J Headache Pain | Kvantitatiivinen analyysi anti-CGRP-mAb:n tehokkuudesta/turvallisuudesta hemiplegisessa migreeniissa, harvinaisessa aura-alaryhmässä, joka on suljettu pois satunnaistetuista kontrolloiduista tutkimuksista |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Havainnoiva tapaussarja | CNS Neurosci Ther | Havainnoiva tapaussarja anti-CGRP-kohdistetusta terapiasta sen vaikutuksesta migreenin auraan |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Kohortti (jälkianalyysi, Phase 3b FOCUS) | Eur J Neurol | Fremanezumabin tehokkuus/elämänlaatu analysoituna väestöissä, joilla on tai ei ole auraa tai neurologisia häiriöitä |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Perustutkimus/Mekanistinen (CSD-malli) | J Neurosci | Fremanezumabi ei vaikuttanut CSD-indusoituihin valtimoiden laajenemisiin tai plasman proteiinin ekstravasaatioon eläin-aura-mallissa |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Perustutkimus/Mekanistinen (CSD-malli) | Pain | Fremanezumabi hidasti CSD-leviämistä ja lyhensi kortikaalista palautumista, mutta ei estänyt CSD-esiintymää rotuissa |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Todellisen maailman kohortti | Frontiers in Neurology | 3 kuukauden todellisen maailman tehokkuus/sietokyky fremanezumabin osalta kroonisessa migreeniissa (ei aura-spesifinen) |
| [35775208](https://pubmed.ncbi.nlm.nih.gov/35775208/) | 2022 | Kohortti | Cephalalgia | Anti-CGRP-mAb:ien (ml. fremanezumabi) vaikutukset migreenin keskus- ja neurologisiin oireisiin |

---

## Suomen markkinatiedot

Fremanezumabi ei ole tällä hetkellä markkinoilla Suomessa (0 lupaa arkistossa; markkinoiden asema: Ei markkinoilla).

---

## Turvallisuusnäkökohdat

Katso turvallisuustietoja valmisteyhteenvedosta. [DG001: TFDA/pakkausselosteen varoitukset ja vasta-aiheet ovat estävä tietovaje; DDI-kysely palautti ei tuloksia.]

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä (tutkimuskysymys)**

**Perustelut:**
Mekanistinen tapaus — perifeereinen CGRP-esto, joka välttää vasokonstriktiivisen riskin, joka sulkee triptaanit tälle alaryhmälle — on perusteltu, mutta mikään kliininen tutkimus ei ole varsinaisesti rekrytoinut brainstem-aurallisen migreeni-potilaita, ja ainoat suoraan relevantit prekliiniset (CSD) tiedot osoittavat, että fremanezumabi ei estä auran fysiologista ilmiötä itseään. Todisteiden taso on L4, mikä vastaa tutkimushypoteesia pikemminkin kuin päätöskuntoiselta signaalilta.

**Jatkamisen edellytykset:**
- TFDA/EU-pakkausselosteen varoitukset ja vasta-aiheet (tällä hetkellä estävä — DG001)
- DrugBank-lähteinen toimintamekanismin yksityiskohta (tällä hetkellä puuttuu — DG002)
- Varsinainen havainnollinen tutkimus tai tapaussarja brainstem-aurallisen migreeni-potilaissa (nykyiset todisteet ovat joko yleisesti migreeniä tai hemiplegista migreenia koskevia, asiaan liittyviä mutta erillisiä aura-alaryhmiä)
- Selvennys siitä, miksi prekliiniset CSD-tiedot eivät osoita vaikutusta aura-korrelaatin fysiologiaan huolimatta kliinisistä tapausraporteista, jotka viittaavat hyötyyn

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

