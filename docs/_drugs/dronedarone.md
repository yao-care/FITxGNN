---
layout: default
title: Dronedarone
parent: Vahva näyttö (L1-L2)
nav_order: 128
evidence_level: L2
indication_count: 10
---

# Dronedarone
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

# Dronedariini: eteisvärinästä/eteislepatyksesta aivohalvaukseen

## Yhden lauseen yhteenveto

Dronedariini on III luokan antiarytmiikkalääke, jota käytetään eteisvärinän ja eteislepatyksen hoitoon. TxGNN-malli ennustaa, että se saattaa myös vähentää **aivohalvausriskiä**, ja käytössä on **19 kliinistä tutkimusta** ja **20 julkaisua** tukemassa — vaikka vain osa niistä tutkii suoraan dronedariinia itseään. Lääkettä **ei markkinoida Taiwanissa**, ja tärkeitä turvallisuusasiakirjoja (TFDA-pakkausseloste, lääke-lääke-yhteisvaikutustiedot) puuttuu edelleen.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Eteisvärinä / Eteislepatys |
| Ennustettu uusi käyttöaihe | Aivohalvaus |
| TxGNN-ennustuskeskiarvo | 99.97% |
| Näyttötaso | L2 |
| Taiwan-markkinatila | Ei markkinoitu (Not Marketed) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksilla |

---

## Miksi tämä ennustus on järkevä?

Yksityiskohtaisia vaikutusmekanismin tietoja ei ole vielä saatavilla tässä näyttöpakettissa (DrugBank MOA -kenttä on tietokuilutapaus). Kerätyjen kliinisten näyttöjen perusteella dronedariini on jodi-vapaaton, monikanavisesti estävä III luokan antiarytmiikkalääke (amiodaronin rakenteellinen analoginen), jota käytetään sinusrytmin ylläpitoon potilailla, joilla on eteisvärinä tai eteislepatys.

Eteisvärinä itsessään on suuri, hyvin tunnistettu iskeemisen aivohalvauksen riskitekijä — arytmia edistää eteisen verenpysähtymistä ja verihyytymien muodostusta, erityisesti vasemman eteisen korvakkeessa. Sinusrytmin palauttamalla ja sitä ylläpitämällä ("rytmin hallinta") dronedariini voi epäsuorasti vähentää tromboembolisia tapahtumia. Tämä yhteys ei ole uusi löydös: se nousi esiin merkittävänä sivulöytönä pivotaalissa Phase 3 **ATHENA-tutkimuksessa**, jossa dronedariini vähensi ensimmäisen sydän- ja verenkiertoelimistön sairaalahoitoa tai kuolemaa, ja jälkikäteisen analyysin (PMID 22149318, 20396635) perusteella aivohalvaustapahtumien ilmaantuvuus vähenee. Yksi mekanistinen tutkimus (PMID 28992468) ehdottaa lisäksi, että dronedariinilla saattaa olla suoria antikoagulantti- ja verihiutaleita estäviä vaikutuksia antiarytmiikkatoiminnastaan riippumatta, mikä tarjoaa mahdollisen farmakologisen selityksen pelkän rytmin hallinnan lisäksi.

Tärkeää on, että tämä mekanistinen yhteys on epäsuora (arytmian hallinnan kautta) eikä suora antitrombottinen mekanismi, ja dronedariiniin liittyy mustan laatikon varoitus käytöstä pysyvässä eteisvärinässä ja sydämen vajaatoimintapotilaissa (PALLAS-tutkimuksen tulosten mukaan, PMID 22082198) — mikä tarkoittaa, että terapiaikkuna tämän uusiokäytön hypoteesille on kapeampi kuin sen alkuperäisen käyttöaiheensa osalta.

---

## Kliinisen tutkimuksen näyttö

| Tutkimuksen numero | Vaihe | Tila | Rekrytointi | Tärkeimmät löydökset |
|---------|------|------|------|---------|
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Valmistunut | 1,015 | Kansainvälinen havaintokohortti, joka vertaa suoraan dronedariinin todellisen maailman tehokkuutta muihin antiarytmiikkalääkkeisiin eteisvärinässä |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A | Valmistunut | 87,810 | Systemaattinen kirjallisuuskatsaus/verkon meta-analyysi Multaq®:sta (dronedariini) vs. solatoli turvallisuudesta eteisvärinässä, mukaan lukien aivohalvausriski |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Valmistunut | 339 | Pragmaattinen satunnaistettu kontrolloitu tutkimus varhaisesta dronedariinista vs. tavallisesta hoidosta ensimmäisen kerran diagnosoidussa eteisvärinässä, parannettujen tulosten arvioimiseksi mukaan lukien tromboemboliset tapahtumat |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Lopetettu | 3,236 | Satunnaistettu kontrolloitu tutkimus dronedariinin 400 mg kahdesti päivässä aivohalvauksen, systeemisen embolismin, sydäninfarktin tai sydän- ja verenkiertoelimistön kuoleman ehkäisyyn pysyvässä eteisvärinässä riskitekijöillä (PALLAS-tutkimus) |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Lopetettu | 22 | EDORA-tutkimus: dronedariini vs. lumelääke ablation jälkeen eteisvärinän uusiutumisen ja eteisen fibroosin etenemisen osalta |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Valmistunut | 2,789 | EAST-tutkimus: varhainen jäsentynyt rytmin hallinta (sisältää antiarytmiikkalääkkeet) vs. tavallinen hoito eteisvärinään liittyvien komplikaatioiden ehkäisemiseksi, mukaan lukien aivohalvaus |
| [NCT02618577](https://clinicaltrials.gov/study/NCT02618577) | Phase 3 | Lopetettu | 2,608 | NOAH-AFNET-tutkimus: NOAC (edoksabaani) vs. nykyinen hoito aivohalvauksen ehkäisyyn eteisen korkean nopeuuden episodeissa (lääkeryhmä poikkeaa dronedariinista) |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Rekrytointi ei vielä alkanut | 1,898 | Monisairaalainen prospektiivinen tutkimus dronedariinin tehokkuudesta, turvallisuudesta ja elämänlaadun vaikutuksista varhaiselle rytmin hallinnalle eteisvärinässä |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Tuntematon | 100 | Amiodaroni vs. dronedariini sinusrytmin ylläpitämiseksi kardioversion jälkeen |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Valmistunut | 500 | Havainnollinen tutkimus NOAC-hallinnasta aivohalvauksen ehkäisyyn iäkkäillä NVAF-potilailla Espanjassa (epäsuora, ei-dronedariini) |

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | Satunnaistettu kontrolloitu tutkimus (PALLAS) | New England Journal of Medicine | Testattiin, vähentääkö dronedariini suuria verisuonitapahtumia korkean riskin pysyvässä eteisvärinässä; tutkimus keskeytettiin aikaisimmin turvallisuushuolista johtuen |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Satunnaistetun kontrolloitun tutkimuksen alianalyysi | Clinical Research in Cardiology | Amiodaronin ja dronedariinin pitkän aikavälin turvallisuus/tehokkuus varhaiselle rytmin hallinnalle EAST-AFNET 4:ssä |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Jälkikäteinen satunnaistetun kontrolloitun tutkimuksen analyysi (ATHENA) | European Journal of Heart Failure | Dronedariini vähentää sydän- ja verenkiertoelimistötapahtumia eteisvärinä/lepatys-potilailla, joilla on samanaikainen HFpEF/HFmrEF |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Retrospektiivinen kohortti | Circulation: Arrhythmia and Electrophysiology | Rinta-rinnan vertailu dronedariinin vs. solatoli tehokkuudesta ja turvallisuudesta eteisvärinä-naiiveilla veteraaneilla |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Retrospektiivinen kohortti | Journal of Atrial Fibrillation | Todellisen maailman sydän- ja verenkiertoelimistötapahtumien, aivohalvauksen, sydämen vajaatoiminnan, sidekudosvaikutuksen keuhkoissa ja maksan vaurion riski: dronedariini vs. amiodaroni ja muut antiarytmiikkalääkkeet |
| [33888353](https://pubmed.ncbi.nlm.nih.gov/33888353/) | 2021 | Todellisen maailman kohortti | Clinical Therapeutics | Digitalisintoksikaation riski samanaikaisessa dronedariinin ja digitaalisin käytössä |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mekanistinen/perustutkimus | Atherosclerosis | Dronedariinilla on antikoagulantti- ja verihiutaleita estävät vaikutukset antiarytmiikkatoiminnastaan riippumatta |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Katsaus | Vascular Health and Risk Management | Yleiskatsaus dronedariinin hyväksynnästä ja tehokkuudesta; jälkikäteinen ATHENA-analyysi viittaa alentuneeseen aivohalvausriskiin |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Katsaus | Current Cardiology Reviews | Aivohalvauksen ehkäisy eteisvärinässä: käsitteet ja kiistakysymykset |
| [24469871](https://pubmed.ncbi.nlm.nih.gov/24469871/) | 2013 | Katsaus | Cardiology Journal | Dronedariinin tehokkuus ja siedettävyys eteisvärinäpotilaille kliinisessä käytännössä |

---

## Taiwan-markkinatiedot

Dronedariinilla on tällä hetkellä **nolla TFDA-markkinointilupaa** ja se **ei ole markkinoilla** Taiwanissa (0 lupaa arkistossa). Tälle lääkkeelle ei ole saatavilla tuote-/annosmuototietoja.

---

## Turvallisuusnäkökohdat

Tutustu pakkausselosteeseen turvallisuustiedoille. Tässä näyttöpakettissa ei ole tällä hetkellä saatavilla TFDA:n varoituksia, vasta-aiheita tai lääke-lääke-yhteisvaikutustietoja dronedariinille — tämä on merkitty **Estävä** tietokuiluksi (DG001: TFDA-pakkausseloste), mikä tarkoittaa, että muodollista S1-turvallisuuden esiarviointia ei voida vielä suorittaa.

Huomautus kirjallisuuden näytöstä edellä: dronedariiniin liittyy tunnettu mustan laatikon varoitus käytöstä **pysyvässä eteisvärinässä** ja **sydämen vajaatoiminnassa** (PALLAS-tutkimus, PMID 22082198), ja dokumentoitu farmakokineettinen yhteisvaikutusriski digitaalisin kanssa P-glykoproteiinin inhiboinnin kautta (PMID 33888353). Nämä tulisi priorisoida, kun muodolliset TFDA-merkintätiedot saadaan käyttöön.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksilla**

**Perustelu:**
Useat tutkimukset ja jälkikäteisen analyysin tulokset (ATHENA, EAST-AFNET 4) tukevat epäsuoraa aivohalvausriskin vähennyssignaalia eteisvärinän rytmin hallinnan kautta, mutta tämä näyttö on suurelta osin sekundaarinen/jälkikäteinen eikä omistettu aivohalvaustutkimus, ja PALLAS-tutkimus osoittaa kapeaa turvallisuusmarginaalia pysyvän eteisvärinän populaatioissa — yhdenmukainen L2-näyttötason kanssa ja varovaisen suosituksen kanssa.

**Jatkamiseksi seuraavat ovat välttämättömiä:**
- TFDA-pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä **Estävä** tietokuilu
- Yksityiskohtaiset vaikutusmekanismin tiedot DrugBankista
- Muodolliset lääke-lääke-yhteisvaikutukset (DDI) -tiedot, erityisesti digitaalisin ja P-glykoproteiinin/CYP3A4-substraattien osalta
- Taiwan-markkinoille pääsypolun arviointi, koska dronedariinia ei markkinoida tällä hetkellä paikallisesti
- Omistettu turvallisuusseurantasuunnitelma mustan laatikon varoituksen vuoksi pysyvässä eteisvärinässä/sydämen vajaatoimintapopulaatioissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

