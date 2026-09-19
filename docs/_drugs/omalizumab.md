---
layout: default
title: Omalizumab
parent: Kohtalainen näyttö (L3-L4)
nav_order: 273
evidence_level: L3
indication_count: 10
---

# Omalizumab
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

# Omalizumab: Allergiasta astmasta keuhkoputkentulehdukseen

## Yhden lauseen yhteenveto

Omalizumabilla (anti-IgE-monoklonaalinen vasta-aine) on vakiintunut käyttö kohtalaisen-vaikean allergiasta astman ja kroonisen spontaanin nettirakkouden hoidossa tämän pakkauksessa olevan tutkimus- ja kirjallisuusaineiston perusteella (Suomen viralliset hyväksynnät osoittavat **0 lupaa** — tiedon puuttuminen, ei farmakologinen tosiasia, sillä todisteet itse huomauttavat tästä). TxGNN-malli ennustaa mahdollista tehokkuutta **keuhkoputkentulehduksessa**, jota tukevat **2 kliinistä tutkimusta** ja **8 julkaisua** — mutta näyttöarviointi osoittaa, että nämä todellisuudessa rekrytoivat allergiasta astma / eosinofiilit keuhkoputkentulehdus-astma / nettirakkous -populaatioita klassisen keuhkoputkentulehduksen sijaan, mikä viittaa mahdolliseen sairauden diagnoosin virhepoikkeamaan, joka vaatii varovaisuutta ennen tämän erityisen ennusteen perusteella toimimista.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Kohtalaisen-vaikea allergiasta astma / krooninen spontaani nettirakkous (kirjallisuusaineiston perusteella; Suomen luvasta tietoja ei saatavilla) |
| Ennustettu uusi indikaatio | Keuhkoputkentulehdus |
| TxGNN-ennustepisteet | 99.9992% |
| Näyttötaso | L3 |
| Suomen markkinatila | Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla DrugBank/TFDA-lähteistä (Tiedon puuttuminen DG002). Tämän pakkauksen omissa tutkimus- ja kirjallisuustietueissa toistuvien tietojen perusteella omalizumab on ihmisen humanisoidun monoklonaalisen vasta-aineen rekombinantti, joka sitoutuu vapaaseen IgE:hen ja estää sen vuorovaikutuksen korkea-affiniteetin IgE-reseptorin (FcεRI) kanssa mastosoluissa, basofiileissa ja dendriittisoluissa, mikä vähentää IgE-välitteistä allergiasta tulehdusta. Sen tehokkuus kohtalaisen-vaikeassa jatkuvassa allergiasta astmassa ja kroonisessa spontaanissa nettirakkoudessa on dokumentoitu toistuvasti tämän pakkauksen lainaamissa tutkimuksissa (esim. NCT00046748, n=484; NCT01202903, n=616), ja mekanistisesti lääkkeen odotetaan olevan relevantti muihin IgE/tyypin-2-tulehduksen aiheuttamiin ilmatieinfektioihin.

Linkki "keuhkoputkentulehdukseen" erityisesti on heikompi kuin TxGNN-pisteet (99.9992%) viittaavat. Molemmat tukevat tutkimukset ovat lähemmässä tarkastelussa populaatioita, jotka ovat lähellä mutta erillisiä: NCT02477332 on vaiheen 2b annosselitystutkimus QGE031:stä (siihen liittyvä anti-IgE-biologinen, ei omalizumab) kroonisen spontaanin nettirakkouden suhteen, ei keuhkoputkentulehduksen; NCT02049294 on pieni (n=11) kortikosteroidiä säästävä tutkimus potilaissa **astma ja eosinofiilit keuhkoputkentulehdus**, ei klassisen tartunnan tai kroonisen keuhkoputkentulehduksen. Pakkauksen oma vanhuuden tarkoitus merkitsee tätä suoraan: tutkimuspopulaatiot edustavat "類緣疾病外推" (ekstrapolointi samankaltaisesta sairaudesta), ja IgE-välitteinen mekanismi ei ole vakiintuneesti tuettu tyypilliselle (ei-eosinofiilit, ei-atopinen) keuhkoputkentulehdukselle. Tämä on todennäköisimmin TxGNN ontologia-viereisyyden artefakti (keuhkoputkentulehdus jakaa upotuksen tilan astma/ilmateiden tulehduksen termien kanssa) eikä validoitu uusi indikaatio.

Huomattavasti tämän saman näyttöpakkauksen 3. sijoitus — "obstruktiivinen keuhkosairaus" (TxGNN pisteet 99.97%, näyttötaso **L1**, päätösvaihe **S3**, suositus **Jatka varaustein**) — on huomattavasti vahvempi vanhuuden signaalin samalle lääkkeelle, tuettuna useilla valmiilla vaiheen 3 RCT-tutkimuksilla (esim. NCT00046748 n=484, NCT01202903 n=616) jotka kohdistavat suoraan allergiasta astmaa, joka on IgE:n ydinvalidoitu indikaatio. Tämä saattaa olla toiminnallisempi ehdokas kuin tässä tarkistettu 1. sijoituksen "keuhkoputkentulehdus" merkintä.

---

## Kliinisen tutkimuksen todisteet

| Tutkimuksen numero | Vaihe | Tila | Rekrytointi | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Vaihe 2 | Valmis | 382 | Vaiheen 2b annosselitystutkimus QGE031:stä (anti-IgE, omalizumabiin liittyvä) lisäterapiana kroonisen spontaanin nettirakkouden hoitoon — ei keuhkoputkentulehdustutkimus; sisällytetty tähän sairauksien välisenä ekstrapolointina (Relevanssusijoitus B). |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Vaihe 2/3 | Valmis | 11 | Kaksoissokea, lumekontrolloitu tutkimus testattaessa, voiko lisäterapiana annettu omalizumab mahdollistaa prednisooniannoksen vähentämisen potilaissa, joilla on astma ja eosinofiilit keuhkoputkentulehdus; hyvin pieni näyte, kortikosteroideja säästävä päätepiste eikä suora keuhkoputkentulehduksen tehokkuus (Relevanssusijoitus C). |

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Turvallisuustutkimus | Current medical research and opinion | Omalizumabbin turvallisuuden yhdistetty analyysi lapsilla, joilla on IgE-välitteinen allergiasta astma; ei keuhkoputkentulehdukseen spesifinen. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Katsaus | Clinical reviews in allergy & immunology | Omalizumabbin hyväksynnän ja hyväksynnän jälkeisen kokemuksen katsaus kohtalaisen-vaikeassa jatkuvassa astmassa; osoittaa ilmateiden tulehduksen vähenemistä IgE/FcεRI-vähenemisen kautta. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Tapauskertomus | Journal of investigational allergology & clinical immunology | Harvinainen plastisen keuhkoputkentulehduksen tapaus bronkiaalilämpökirurgian jälkeen; tangentiaalinen omalizumabbin tehokkuuteen. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | odottaa | Postepy dermatologii i alergologii | Omalizumab iäkkäillä potilailla, joilla on vakava allergiasta astma–COPD päällekkäisyys; ehdottaa mahdollista hyötyä ACO-fenotyypissä. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | odottaa | Expert opinion on pharmacotherapy | Keskustelee tutkimushaasteista tupakoinnin aiheuttamassa ilmatiesairaudessa (krooninen keuhkoputkentulehdus, emfyseema, ACO) astmapotilaissa, huomaten että nämä potilaat tyypillisesti jätetään tutkimusten ulkopuolelle. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | odottaa | Masui (Japanese journal of anesthesiology) | Japanilainen perioperatiivinen hoito-ohje keuhkoputkeen astmassa/krooninen keuhkoputkentulehdus; luettelee omalizumabbin vaihtoehdoksi JGL2012:n mukaan vakavassa allergiasta astmassa. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | odottaa | Revue des maladies respiratoires | Ranskalainen asiantuntija-arvio aikuisten astman ekskasaatioiden määritelmistä ja hoidosta; yleinen konteksti, ei keuhkoputkentulehdukseen spesifinen. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | odottaa | Allergologia et immunopathologia | Yleinen katsaus monoklonaalisten vasta-aineiden osalta pediatriassa, mukaan lukien omalizumab allergiasta sairaudesta. |

---

## Suomen markkinatiedot

Omalizumabilla ei ole tällä hetkellä markkinointilupia Suomessa (0 lupaa; markkinatila: Ei markkinoilla/Ei markkinoilla). Mitään tuotetta, annosmuotoa tai hyväksytyn indikaation tietoja ei ole saatavilla tästä näyttöpaketista.

---

## Turvallisuusnäkökohdat

Ks. pakkausselosteen turvallisuustietoja.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Sijoituksen 1 ennustettu indikaatio ("keuhkoputkentulehdus") ei saa riittävää tukea omista lainatuista tiedoistaan — molemmat tutkimukset tutkivat todellisuudessa allergiasta astma/nettirakkous tai eosinofiilit-keuhkoputkentulehdus-astma -populaatioita klassisen keuhkoputkentulehduksen sijaan, joilla on pienet näytteet ja B/C relevanssisijat, yhdenmukainen TxGNN-sairauden upotuksen viereisyyden artefaktin kanssa eikä validoitu mekanistinen linkki klassiseen keuhkoputkentulehdukseen. Muodollista turvallisuus- ja Suomen lisensointitietoja puuttuvat myös kokonaan (Estävä tiedon puuttuminen DG001), joten ehdokas ei voi läpäistä S1-turvallisuusseulontaa edes ennen tehokkuuden harkintaa.

**Jotta voisimme edetä, seuraava vaaditaan:**
- TFDA/Suomen pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä (DG001)
- Vahvistetut DrugBank-vaikutusmekanismin tiedot (DG002)
- Sairauden ontologia -selkeytys siitä, tarkoittaako "keuhkoputkentulehdus" tässä erityisesti eosinofiilit keuhkoputkentulehdusta (tunnustettu astman päällekkäisyys-fenotyyppi) vs. klassisen tartunnan/kroonisen keuhkoputkentulehduksen
- Omistautuneet tutkimukset tai kirjallisuus vahvistetulla, ei-atooppisella keuhkoputkentulehdus populaatiolla ennen kuin edetään tutkimuskysymyksen vaiheen yli
- Vertailulle: tämä sama näyttöpakkaus osoittaa "obstruktiivinen keuhkosairaus" (sijoitus 3, näyttötaso L1, "Jatka varaustein") huomattavasti paremmin tuetuksi vanhuuden ehdokkaaksi tälle lääkkeelle ja saattaa vaatia erillisen arvioinnin.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

