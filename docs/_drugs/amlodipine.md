---
layout: default
title: Amlodipine
parent: Vahva näyttö (L1-L2)
nav_order: 28
evidence_level: L2
indication_count: 10
---

# Amlodipine
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

# Amlodipiini: Hypertensiosta aivoverenvuotoon (toissijaisestä ehkäisystä)

## Yhden lauseen yhteenveto

> Amlodipiini on pitkävaikutteinen dihyydropyridiinin kalsiumkanavaestin, jota käytetään alun perin verenpainetaudin ja kroonisen vakaan angiinan hoitoon.
> TxGNN-malli ennustaa, että sillä voi olla rooli aivoverenvuodon (ICH) **toissijaisessa ehkäisyssä** intensiivisen verenpaineen hallinnan kautta,
> ja tällä hetkellä **6 kliinistä tutkimusta** (mukaan lukien yksi valmistunut vaihe 3 RCT 1 671 potilaalla) ja **8 julkaisua** tukevat tätä suuntaa.
> Tässä ennustuksessa amlodipiinille ennustettiin myös yhdeksän muuta kandidaattindikaatiota; yhdeksällä paitsi yhdellä on heikko tai olematon tukeva todiste (katso yhteenvetotaulukko alla).

---

## Pika-arvio

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Verenpainetauti (vakiintunut kliininen indikaatio amlodipiinille; Suomen erityistä hyväksytyn indikaation tekstiä ei ole saatavilla, koska lääke **ei ole markkinoilla** tässä aineistossa) |
| Ennustettu uusi indikaatio | Aivoverenvuoto (verenpaineen hallinta toissijaiseen ehkäisyyn) |
| TxGNN-ennustuspistemäärä | 99.79% |
| Todisteen taso | L2 |
| Suomen markkinointistatus | Ei markkinoilla (Ei markkinoilla) |
| Lupamäärien lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksella |

---

## Kaikki ennustetut indikaatiot – yleiskatsaus

TxGNN-ajo amlodipiinille palautti 10 paremmuusjärjestykseen asettua kandidaattia. TxGNN-pistemäärä ei ole todisteen laadun välitysmuuttuja — korkeimmin pisteytyssä oleva kandidaatti ("aivovarren infarkti") ei saa kliinistä tai kirjallisuuden tukea, kun taas alemmassa paremmuusjärjestyksessä oleva kandidaatti (aivoverenvuoto) nauttii vahvimmasta todellisen maailman todistusvoimasta.

| Sijoitus | Ennustettu indikaatio | TxGNN-pistemäärä | Todisteen taso | Suositus |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Aivovarren infarkti | 99.94% | L5 | Odota |
| 2 | Keuhkojen hypertensio, epäselvä monitekijäinen mekanismi | 99.91% | L5 | Odota |
| 3 | Keuhkojen hypertensio keuhkosairaudesta / hypoksiasta johtuen | 99.91% | L5 | Odota |
| 4 | Pahanlaatuinen renovaskulaarinen hypertensio | 99.90% | L4 | Tutkimuskysymys |
| 5 | Pahanlaatuinen hypertensio-indusoitunut munuaissairaus | 99.90% | L5 | Odota |
| 6 | Aivovaltimon tukos | 99.89% | L3 | Tutkimuskysymys |
| 7 | Braddock-oireyhtymä | 99.88% | L5 | Odota |
| 8 | MRI-määritelty aivoinfarkti | 99.86% | L4 | Odota |
| 9 | ABri-amyloidoosi | 99.84% | L5 | Odota |
| **10** | **Aivoverenvuoto** | **99.79%** | **L2** | **Jatka varauksella** |

**Huomautus heikoista kandidaateista (sijoitukset 1, 2, 3, 5, 7, 9):** näillä ei ole kliinisiä tutkimuksia, ja ne saavat joko ei lainkaan kirjallisuutta tai vain avainsana-tasoisia (ei lääkekohtaisia) kirjallisuuden osumia. Useat ovat biologisesti epäuskottavia mekanismin kannalta - esimerkiksi kalsiumkanavaestimia **ei** yleensä suositella hypoksiasta johtuvassa (ryhmä 3) keuhkojen hypertensioossa, koska ne voivat vaimentaa hypoksiaa aiheuttavaa keuhkojen vasokonstriktioita ja pahentaa V/Q-epäsuhteita, ja harvinaiset geneettiset oireyhtymät (Braddock-oireyhtymä, ABri-amyloidoosi) eivät ole tunnetussa mekanistisessa yhteydessä CCB-farmakologiaan. Näitä käsitellään embedding-samankaltaisuuden meluna eikä aitoina repurposingin signaaleina.

---

## Miksi tämä ennustus on järkevä?

Yksityiskohtainen vaikutusmekanismi (MOA) -data ei ole tällä hetkellä saatavilla DrugBankista tämän tietueen osalta (merkitty korkea-vakavuusasteiseksi tietoaukoksi, DG002). Vakiintuneen farmakologisen tiedon perusteella amlodipiini on pitkävaikutteinen **dihyydropyridiinin kalsiumkanavaestin (CCB)**, joka alentaa verenpainetta verisuonten sileiden lihasten rentoutumisen ja systeemisen verisuonitahdinnan pienentämisen kautta. Sen tehokkuus verenpainetaudissa on hyvin todistettu ja muodostaa perustan sen käytölle lukuisissa kiinteän annoksen monilääkiterapian verenpainejärjestelmissä.

Hypertensio on yksittäin tärkein muokattavissa oleva riskitekijä sekä aivojen sisäisen verenvuodon esiintymiselle että toistumiselle. Intensiivinen, jatkuva verenpaineen hallinta ICH-tapahtuman jälkeen on ohjaustoimien hyväksymä toissijaisen ehkäisyn strategia, ja näissä yhteyksissä käytetyt kiinteän matalaannoksen "kolmipilleri" -yhdistelmät (esim. TRIDENT-tutkimus) sisältävät tyypillisesti CCB-komponentin, kuten amlodipiini. Tämä antaa suoran mekanistisen perustelun TxGNN-ennusteelle: lääkettä ei ehdoteta akuutin verenvuodon hoitoon, vaan kroonisen verenpaineen alentamisen aineena toistuvien verenvuoto- ja sydäntapahtumien ehkäisemiseksi aivoverenvuodon selviytyneissä.

Pääasiallinen todisteen puute on, että millään tutkimuksella ei ole eristetty amlodipiinin yksittäistä vaikutusta näissä yhdistelmissä - tukeva RCT (TRIDENT) arvioi kolmipilleri-strategiaa, ei amlodipiinin monoterapiaa, joten kausaalinen atribuutio amlodipiiniin jää epäsuoraksi.

---

## Kliinisen tutkimuksen todisteet

*(Ensisijainen indikaatio: Aivoverenvuoto)*

| Tutkimusnumero | Vaihe | Tila | Rekrytointi | Tärkeimmät löydökset |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Vaihe 3 | Valmistunut | 1 671 | TRIDENT-päätutkimus: kiinteä matalaannoksinen "kolmipilleri" (verenpainetta alentava yhdistelmä, yleensä sisältäen CCB:n) vs. tavallinen hoito toistuvien aivohalvausten vähentämiseksi ICH:n jälkeen — suurin ja suorimmin asiaa koskeva tutkimus tälle indikaatiolle. |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | Rekrytoimassa | 140 | TRICH-pistemäärän ohjattu kolminkertainen antihypertensiivin hoito verenpaineen hallinnalle ICH:n jälkeen; käynnissä, tuloksia ei vielä. |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Vaihe 4 | Rekrytoimassa | 11 414 | Suuri verenpaine-interventiotutkimus tyypin 2 diabeetikoissa; ICH-relevantti mutta ei ICH-spesifinen — epäsuora todiste. |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Vaihe 4 | Valmistunut | 1 000 | ARB-monoterapia vs. ARB + CCB-yhdistelmä sydän- ja verisuonitapahtumien vähentämiseksi ikääntyneissä japanilaisissa hypertensioissa; epäsuora todiste. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Vaihe 3 | Lopetettu | 1 | TRIDENT:n kognitiivinen alitutkimus; lopetettu vain 1 osallistujalla, merkityksetön tilastollinen voima. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Lopetettu | 4 | TRIDENT:n MRI-alitutkimus; lopetettu vain 4 osallistujalla, merkityksetön tilastollinen voima. |

**Toissijainen kandidaatti — Aivovaltimon tukos (L3, tutkimuskysymys):** tunnistettu 5 tutkimusta, kaikki epäsuoria (verenpaine-strategia tai statiini/karotin-endarteriektomia tutkimukset, jotka eivät ole amlodipiini-spesifisiä); relevanttein on [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) (STEP-tutkimus, n=8 000, systolisen verenpaineen interventio ikääntyneissä hypertensioissa, tila tuntematon).

---

## Kirjallisuuden todisteet

*(Ensisijainen indikaatio: Aivoverenvuoto)*

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|-----|------|------|---------|
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT | Hypertension Research | CASE-J-tutkimuksen perustelut — vertaa ARB-pohjaista vs. CCB-pohjaista hoitoskeemaa sydän- ja verisuonitapahtumien vähentämiseksi korkean riskin hypertensioissa. |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Katsaus (Taso 1) | Int J Stroke | TRIDENT-tutkimuksen perustelut ja kuvaus — kolmipilleri-verenpainetta alentava strategia toistuvaan ICH-ehkäisyyn. |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Katsaus | Neurological Sciences | Arvioi beetasalpaajan (atenololiin) roolia akuutin ICH:n lopputulokselle; asiaa koskevat antihypertensiivin strategiassa ICH-yhteydessä mutta ei amlodipiini-spesifisiä. |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Katsaus | Cardiovasc Drugs Ther | Klassinen katsaus kalsiumantagonistien antihypertensiivin mekanismista, mukaan lukien käyttö vakavassa hypertensioissa. |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Kohortti (eläinmalli) | Biol Pharm Bull | Dihyydropyridiini-CCB (benidipiini) parantaa aivojen verenvirtauksen autoregulatiota hypertensioissa olevissa hiirissä — tukeva mekanistinen luokkaan kuuluva todiste. |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Tapauskertomus | Ann Pharmacother | Todennäköinen amlodipiini-indusoitunut angiödeema potilaalla, jolla on verenvuoto-aivohalvaus — turvallisuussignaali, ei tehokkuustodiste. |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Tapauskertomus | Curr Drug Saf | Tizanidiini-indusoitunut hypotensio aivohalvauspotilaalla antihypertensiivilääkkeiden käytön yhteydessä; ei amlodipiini-spesifisiä. |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Tapauskertomus | BMJ Case Rep | PRES (posteriori reversiibeli enkefalopatia-oireyhtymä) nopeasta antihypertensiivilääkkeiden vetäytymisestä bariatrisen leikkauksen jälkeen potilaalla, jolla on aiempi ICH-historia; havainnollistaa verenpaineen hallinnan monimutkaisuutta, ei suoraa tehokkuustodistetta. |

**Toissijainen kandidaatti — Aivovaltimon tukos (L3):** 5 prekliinistä (eläinmalli) -tutkimusta osoittavat amlodipiinin ± atorvastatiinin pienentävän infarktin laajuutta antiapoptootisten / antioxidatiivisten mekanismien kautta väliaikaisen keskimmäisen aivovaltimon tukoksen (MCAO) jälkeen (esim. [PMID 21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/), [PMID 17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/)) — mekanistisesti kannustava mutta ihmisillä tämä kyseinen indikaatio erityisesti tutkimustietoa ei ole olemassa.

---

## Suomen markkinatiedot

Amlodipiini on tällä hetkellä merkitty tässä aineistossa **ei markkinoilla (Ei markkinoilla)**, ja tietueeseen on tallennettu **0 markkinointilupia**. Tuote-tason lisensointitietoja (luvan numero, tuotteen nimi, antomuoto, hyväksytyn indikaation teksti) ei ole saatavilla raportoitavaksi.

---

## Turvallisuusnäkökohdat

Viittaa pakkausselosteeseen turvallisuustietojen osalta.

*(Huomautus: Tärkeimmät varoitukset, vasta-aiheet ja lääkkeen väliset vuorovaikutustiedot kyselyissä palautuivat tietoaukkoina — TFDA:n pakkausselosteen varoitukset/vasta-aiheet on merkitty **estävänä** tietoaukoksi (DG001), joka on ratkaistava ennen kuin tämä kandidaatti voi edetä S1-turvallisuuden arvioon.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksella** (aivoverenvuodon osalta) / **Odota** (kaikki muut 9 kandidaattindikaatiota)

**Perustelut:**
- Aivoverenvuotokandidaatti on tuettu yhdellä valmistellulla vaihe 3 RCT:llä (TRIDENT, n=1 671) ja käynnissä olevalla omalla seurantatutkimuksella (TRICH), mikä antaa sille aidon L2-todisteen ja uskottavan, ohjaustoimesta johdonmukaisen mekanismin (toissijainen verenpaineen hallinta post-ICH). Kuitenkaan millään tutkimuksella ei ole eristetty amlodipiinin yksittäistä vaikutusta näissä yhdistelmissä - varauksilla (seuranta, ei monoterapian nimikevaatimus) on tarpeen.
- Loput 9 kandidaattia puuttuvat lääkekohtaisesta kliinisestä todistusvoimasta — useimmat ovat joko puhtaita TxGNN-pisteen artefakteja (L5, ei tutkimuksia/kirjallisuutta) tai vain epäsuorin / prekliinisin tiedoin tuettuja (L3–L4), ja ne pysäytetään oikein voimakkaamman todisteen odotuksessa.

**Jatkaakseen seuraavaa vaaditaan:**
- Ratkaise DG001 (TFDA / säännöllinen pakkausselosteen varoitukset ja vasta-aiheet) — tällä hetkellä **estävä** aukko, joka estää minkään S1-turvallisuuden arvion.
- Ratkaise DG002 (muodollinen DrugBank MOA-tietue) mekanistisen yhteyden kuvauksen vahvistamiseksi.
- Tutkimus tai alaryhmäanalyysi, joka eristää amlodipiinin erityisen vaikutuksen kolmipilleri-skeemassa ICH-toissijaiseen ehkäisyyn.
- Vahvista todellinen Suomen/Taiwanin sääntely- ja markkinointistatus, koska nykyinen tietue näyttää 0 lupaa, mikä on ristiriidassa amlodipiinin tunnetun maailmanlaajuisen saatavuuden kanssa — tämä on tarkistettava todellisen tietoaukon tai kyselyväärinkäsityksen arvioimiseksi.
- Tutkimuskysymys-tasoisten kandidaattien (pahanlaatuinen renovaskulaarinen hypertensio, aivovaltimon tukos) osalta kohdistettu kirjallisuus / tutkimushaku käyttäen amlodipiini-spesifisiä termejä (nykyinen kirjallisuus oli suurelta osin ei-spesifinen tai pelkästään eläinmalli-pohjaista) ennen mitään muuta priorisointia.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

