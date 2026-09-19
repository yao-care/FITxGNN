---
layout: default
title: Palonosetron
parent: Kohtalainen näyttö (L3-L4)
nav_order: 282
evidence_level: L4
indication_count: 5
---

# Palonosetron
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **5** kpl
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

# Palonosetron: Sytostaattien aiheuttamasta pahoinvoinnista migreeni-häiriöön

## Yksirivisummary

> Palonosetron on toisen sukupolven 5-HT3-reseptorin antagonisti, antiemeettinen lääke, joka on kliinisesti hyväksytty sytostaattien aiheuttaman pahoinvoinnin ja oksentamisen (CINV) ehkäisyyn — tämä alkuperäisen käyttöindikaation konteksti on yleistä farmakologista tietoa eikä sitä **vahvista** itse näytöaineisto, joka ei sisällä lähdetietoja alkuperäisestä indikaatiosta.
> TxGNN-malli ennustaa mahdollista tehokkuutta **Migreeni-häiriölle** (pistemäärä **99.74%**), mutta ainoa tällä hetkellä käytettävissä oleva tutkimuslitteratuurin todiste on yksittäinen tapausraportti *"Palonosetronin aiheuttama migreenimainen päänsärky"* — eli raportti siitä, että lääke **aiheuttaa** migreenimaisia oireita, ei niitä hoida — ja **yhtään kliinistä tutkimusta** ei ole rekisteröity tälle indikaatiolle.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei saatavilla näytöaineistosta (ei `alkuperäisiä_indikaatioita` tai Suomen lupa-tekstejä arkistossa); yleisesti tiedetään antiemeettiseksi CINV:n ehkäisyyn, mutta vahvistamatonta tätä tietolähdettä vastaan |
| Ennustettu uusi indikaatio | Migreeni-häiriö |
| TxGNN-ennustepistemäärä | 99.74% |
| Näytötaso | L4 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidättäytyminen |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä toimintamekanismin yksityiskohtaisia tietoja ei ole saatavilla (merkitty korkean vakavuusasteen tietovajeeksi, DG002). Yleisen farmakologisen tiedon perusteella palonosetron on erittäin selektiivinen 5-HT3-reseptorin antagonisti, joka on kliinisesti hyväksytty sytostaattien aiheuttaman pahoinvoinnin ja oksentamisen ehkäisyyn.

Mekanistinen perusteltu migreenille on kuitenkin heikko ja jopa ristiriitainen sen sijaan että tukisi sitä. Migreenia hoitavan farmakologisen standardin mukaisesti triptaanit vaikuttavat 5-HT1B/1D-reseptoreihin, jotka ovat erillinen serotoniinireseptorin alatyyppi ilman vakiintunutta positiivista vuorovaikutusta 5-HT3-antagonismiin. Ei ole vakiintunutta mekanismia, jolla 5-HT3:n esto helpottaisi migreeniä.

Vielä tärkeämpää on, että tähän ennusteeseen liittyvä ainoa kirjallisuuden todiste on tapausraportti, joka kuvaa palonosetronin **aiheuttavan** migreenimaista päänsärkyä **haitallisena reaktiona**, ei todisteena terapeuttisesta hyödystä. Tämä tarkoittaa, että tämän lääke-sairaus-parin käytettävissä oleva todellisen maailman signaali osoittaa päinvastaiseen suuntaan kuin TxGNN-pistemäärä viittaisi. Ennuste tulisi lukea graafipohjaisen tilastollisen assosiaation kuin mekanistisesti tai kliinisesti tuetun hypoteesin sijaan tässä vaiheessa.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|------|--------|-------|-----------------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Tapausraportti | Canadian Journal of Anaesthesia | Kuvaa tapausta, jossa palonosetron **aiheutti** migreenimaista päänsärkyä — haittatapahtuma-raportti, ei todiste tehokkuudesta migreenia vastaan |

---

## Suomen markkinatiedot

Palonosetron **ei ole markkinoilla** Suomessa (0 lupaa arkistossa); tuotelupa-tietoja ei ole saatavilla.

---

## Turvallisuushuomiot

Katso turvallisuusohjeet pakkausselosteesta. Yhtään keskeistä varoitusta, vasta-aiheita tai lääkkeen yhteisvaikutustietoja ei ole saatavilla nykyisessä näytöaineistossa — TFDA/pakkausselosteen turvallisuustiedot on merkitty **estäväksi** tietovajeksi (DG001), mikä tarkoittaa, että turvallisuutta ei vielä voi arvioida.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidättäytyminen**

**Perustelut:**
Migreeni-indikaation todisteet koostuvat yksittäisestä tapausraportista **haitallisesta vaikutuksesta** (lääkkeen aiheuttama migreenimainen päänsärky), ei hoitosignaalista, eikä yhtään kliinistä tutkimusta ole olemassa. Ehdotettu mekanismi puuttuu myös positiivisesta farmakologisesta perustelusta (5-HT3-antagonismi vs. triptaanien/5-HT1B/1D-polun käyttö migreenin todellisessa hoitamisessa). Kaikki viisi TxGNN-ennustettu indikaatiota tälle ehdokkaalle suosittelevat pidättäytymistä, ja kahdella alemman sijoituksen ihosairauksilla (atrophoderma vermiculata, ulerythema ophryogenesis) ei ole lainkaan kirjallisuus- tai tutkimustukea.

**Jotta voidaan edetä, seuraavaa tarvitaan:**
- TFDA/Suomen pakkausselosteen tiedot (varoitukset, vasta-aiheet) — tällä hetkellä estävä tietovaje (DG001)
- Vahvistettu toimintamekanismi ja varmennettu alkuperäinen indikaatio, lähdeviitteineen pääteltäväksi yleisestä tiedosta (DG002)
- Riippumaton arviointi siitä, edustaako "palonosetronin aiheuttama migreeni" -tapausraportti luokkatasoisesti 5-HT3-antagonistin turvallisuussignaalia, joka argumentoisi **vastaan** sen sijaan että hyväksi tälle uudelleenkäyttöindikaatiolle
- Mitään lisää kliinistä tai prekliinistä tietoa, joka osoittaa positiivisen (ei pelkän korreloivan) mekanistisen yhteyden migreeniin ennen edistymistä S0-vaiheen yli

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

