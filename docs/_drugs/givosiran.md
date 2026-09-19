---
layout: default
title: Givosiran
parent: Vahva näyttö (L1-L2)
nav_order: 175
evidence_level: L2
indication_count: 10
---

# Givosiran
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **10** kpl
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

# Givosiran: Akuutista hepatisesta porfyriasta ALA-dehydrataasin puutosporfyriaan

## Yhden lauseen yhteenveto

Givosiran on hepatiaaliksi kohdennettu siRNA-lääke, jota käytetään alun perin AHP:n (Acute Hepatic Porphyria) hyökkäysten estämiseen, ensisijaisesti AIP:ssa (Acute Intermittent Porphyria), silentoimalla ALAS1-geeniä hemosynteesin reitillä. TxGNN-malli ennustaa lisäksi tehokkuutta **ALA-dehydrataasin puutosporfyriassa (ALADP)** — AHP:n harvinaisimmassa alatyypissä — tuettuna **8 julkaisulla** (sisältäen keskeisen vaiheen 3 RCT:n ja yhden tapausraportin), vaikka **yhtään omaa kliinistä tutkimusta** ei tällä hetkellä ole tälle spesifiselle alatyypille.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Akuutti hepatinen porfyria (dokumentoitu todisteen sisältävässä kirjallisuudessa, esim. PMID 36028858, 35734365) |
| Ennustettu uusi indikaatio | ALA-dehydrataasin puutosporfyria (ALADP) |
| TxGNN-ennuste-pistemäärä | 99,91% |
| Todisteen taso | L2 |
| Suomen markkinointi | Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Jatka varaustein |

*Huomautus: Tällä lääkkeellä on yhteensä 10 TxGNN-ennustettua indikaatiota. Yhdeksän niistä (sijoitus 1–8, 10) ovat pelkästään mallin ennusteita (L5, ilman tutkimusnäyttöä) suosituksella "Hold" (Pidätä), eikä niistä keskustella tarkemmin tässä raportissa. Tämä raportti keskittyy sijoitukseen 9 — ainoaan kandidaattiin, jolla on toimeenpantava todisteen taso.*

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja DrugBankista ei ole saatavilla (`original_moa: [Data Gap]`). Todisteen sisältävän kirjallisuuden tunnettujen tietojen perusteella givosiran on pieni interferoiva RNA (siRNA), joka vaientaa hepatista ALAS1:tä (5-aminolevuliinihapon syntetaasi 1), hemosynteesin reitin rajoittavaa entsyymiä. Sen tehokkuus akuutissa hepatisessa porfyriassa on osoitettu vaiheen 3 ENVISION-tutkimuksessa (PMID 36028858) ja myöhemmissä kohorttitutkimuksissa (PMID 35067977, 40312531).

ALA-dehydrataasin puutosporfyria (ALADP) johtuu ALA-dehydrataasin puutoksesta, entsyymistä, joka on välittömästi **alavirtaan** ALAS1:stä samalla hemosynteesin reitillä. Koska ALAS1:n estäminen vähentää neurotoksisten edeltäjäaineiden ALA:n ja PBG:n tuotantoa riippumatta siitä, mikä alavirtaan oleva entsyymi on puuttuva, givosiraainin soveltuvuudelle ALADP:lle on löydettävissä plausibli mekanistinen perustelu — tämä on nimenomaisesti huomioitu pakkauksen omassa perustelussa ("抑制 ALAS1 仍可降低 ALA 堆積，機轉關聯強").

Kuitenkin tämä mekanistinen plausibiliteetti lieventyy ristiriitaisesta todellisen maailman näytöstä: julkaistu tapausraportti (PMID 35991568) dokumentoi givosiraaniin **kliinisen vasteen puutteen** vahvistetussa ALADP-potilaalla mekanistisesta perustelusta huolimatta. ALADP:n patofysiologia sisältää myös erytropoieettisia tekijöitä, joita AIP:ssa käytetty hepatinen ALAS1-malli ei täysin ota huomioon, mikä saattaa selittää epähomogeenisen vasteen. Ottaen huomioon ALADP:n äärimmäisen harvinaisuuden (alle 10 tapausta raportoitu maailmanlaajuisesti), omia RCT:itä ei ole, ja nykyinen tuki perustuu luokkatasoisiin AHP-tutkimuksiin sekä yhteen ristiriitaiseen tapausraporttiin.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröity siihen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|------|--------|-------|---------|
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | RCT (vaihe 3, jälkikäteinen) | Orphanet Journal of Rare Diseases | ENVISION-tutkimuksen jälkikäteinen analyysi: givosiran vähentää AHP:n sairauskuormaa ja hyökkäysten esiintymistiheyttä; keskeinen tehokkuuden näyttö AHP-lääkkeiden luokalle (ei ALADP-spesifinen) |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Kohortti | Journal of Internal Medicine | RNAi-terapia givosiraanilla vähentää merkittävästi hyökkäysten esiintymistiheyttä akuutissa intermitentissa porfyriassa |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Kohortti | Scientific Reports | Laajennetun käytön tutkimus 10 japanilaisessa AHP-potilaassa kuukausittaisella SC-givosiraanilla 2,5 mg/kg; tukee tehokkuutta/turvallisuutta todellisen maailman Aasialaisten kohorteissa |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Katsaus | Revista clinica espanola | Akuutin hepatisen porfyrian kriisien hoitolähestymistapa; tunnistaa ALA-dehydrataasin puutoksen yhdeksi neljästä AHP:n alatyypistä, jotka jakavat ALAS1-ohjatun mekanismin |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Katsaus | Drug Design, Development and Therapy | Givosiraanin suunnittelun, kehityksen ja aseman yleiskatsaus AHP:n hoidossa aikuisilla |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Katsaus | Blood | RNA-interferenssiterapia AHP:ssa; vahvistaa ALAS1-induktion AHP:n alatyypeissä jaettuna ylävirtaan sijaitsevana ajavana tekijänä |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK/PD | CPT: Pharmacometrics & Systems Pharmacology | PK/PD-malli virtsaperäisen ALA:n vähenemisestä givosiraanin jälkeen koottujen vaiheen I–III tutkimustietojen poikki |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Tapausraportti | Frontiers in Genetics | **Suoraan liittyvä ALADP:hen**: raportoi kliinisen vasteen puutosta givosiraaniin vahvistetussa ALAD-porfyria-potilaassa mekanistisesta perustelusta huolimatta — keskeinen ristiriitainen signaali |

---

## Turvallisuuden näkökohdat

Katso tuotepakkauksen liitettä turvallisuustietojen osalta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varaustein**

**Perustelu:**
Mekanistinen perustelu (ALAS1 toimii ALA-dehydrataasin ylävirtaan samalla hemosynteesin reitillä) on hyvin tuettu AHP-luokan RCT- ja kohorttinäytöillä, mutta ainoa ALADP-spesifinen datapiste — tapausraportti — osoitti vasteen puutteen, ja yhtään omaa tutkimusta ei ole tähän äärimmäisen harvinaiseen alatyypille. Näyttö on suuntaa-antava mutta ei vielä riittävä ehdottomalle etenemiselle.

**Jatkamiseksi tarvitaan seuraavaa:**
- TFDA/Fimea-tuotepakkauksen varoitukset ja vasta-aiheet (tällä hetkellä estävä tietoaukko, DG001)
- Vahvistettu DrugBank-vaikutusmekanismin yksityiskohdat (tällä hetkellä korkean vakavuuden tietoaukko, DG002)
- Lisää ALADP-tapaussarjaa tai rekisteritietoja ristiriitaisen tapausraportin selvittämiseksi
- Lääkkeiden vuorovaikutusprofiilit (DDI) (tällä hetkellä `not_found`)
- Sääntelyyn perustuva reittiarviointi, koska lääke ei ole tällä hetkellä markkinoilla Suomessa (0 hyväksyntää)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

