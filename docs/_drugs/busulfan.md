---
layout: default
title: Busulfan
parent: Vahva näyttö (L1-L2)
nav_order: 83
evidence_level: L1
indication_count: 10
---

# Busulfan
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **10** kpl
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

# Busulfani: kroonisesta myeloidisesta leukemiasta myelodyplastiseen oireyhtymään

## Yhden lauseen yhteenveto

Busulfani on klassinen bifunktiaalinen alkiloiva aine, joka kehitettiin historiallisesti kroonista myeloidista leukemiaa varten ja jota käytetään nykyään lähinnä myeloablatiivisen esilääkityksen aineena allogenisen vermuodostuksellisen kantasiirrännän (allo-HSCT) edellä. TxGNN-malli ennustaa, että se voi olla tehokas **myelodyplastisessa oireyhtymässä (MDS)**, ja tätä suuntaa tukee tällä hetkellä **50 kliinistä tutkimusta** ja **20 julkaisua**, mukaan lukien valmistuneet vaiheen 3 satunnaistetut kokeet.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Krooninen myeloidi leukemia / myeloablatiivinen esilääkitysaine (perustuu yleiseen farmakologiseen tietämykseen — ei sisälly nykyiseen Suomen säännösten mukaiseen tietokantaan, joka ei sisällä lisensointitietueita) |
| Ennustettu uusi indikaatio | Myelodyplastinen oireyhtymä |
| TxGNN-ennusteen pistemäärä | 99.62% |
| Todisteiden taso | L1 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Lupien määrä | 0 |
| Suositeltu päätös | Jatka varavaraisuuksilla |

---

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla todistepakkauksessa (MOA-kenttä merkitty tietoaukoksi). Hyvin vakiintuneen farmakologian perusteella busulfani on bifunktiaalinen alkiloiva aine, joka ristisilloittaa DNA:ta, mikä aiheuttaa syvän, annoksesta riippuvan myeloablation. Sen vakiintuneet nykyaikaisen kliinisen roolit ovat **myeloablatiivisten/vähennetyn intensiteetin esilääkityskaavioiden** komponentit (tyypillisesti yhdistetty fludarabiniin tai syklofosforamidiin), jotka annetaan välittömästi ennen allo-HSCT:ta.

MDS on klonaalinen vermuodostuksellisten kantasolujen häiriö, jolle allo-HSCT jää ainoaksi mahdollisesti paranevaksi hoidoksi korkeamman riskin sairauksissa. Allo-HSCT:n suorittamiseksi potilaan poikkeava ydinaines on ensin abloiduttava, jotta luovuttajan kantasolut voivat istuuntua — tämä on täsmälleen sillä roolilla, joka busulfanipohjaisella esilääkityksellä on jo rutiinissa kliininen käytäntö MDS:n hoidossa. Kuten uudelleenkäytön perusteluissa todetaan, tämä ei ole uusi biologinen hypoteesi, vaan vakiintuneen kliinisen polun vahvistus: busulfanipohjaisella esilääkityksellä (Bu/Flu, Bu/Cy, ajoitetulla peräkkäisellä busulfanilla jne.) käytetään laajasti siirron edellä MDS-potilaiden hoidossa, mikä selittää sekä erittäin korkean TxGNN-pistemäärän että epätavallisen syvän kliinisen tutkimuksen/kirjallisuuspohjan tälle yhdistelmälle.

Mekanistinen yhteys on siis vahva ja sitä tukevat suoraan vuosikymmenten siirtökirjallisuus, eivät pelkästään laskennalliset johtopäätökset — useita vaiheen 3 satunnaistettuja kokeita vertaa suoraan busulfanipohjaisiin esilääkityskaavioihin MDS/AML-populaatioissa, jotka käyvät läpi allo-HSCT:tä.

---

## Kliinisen tutkimuksen todisteet

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT00416598](https://clinicaltrials.gov/study/NCT00416598) | Vaihe 2 | Valmistunut | 546 | Ylläpidon dekitabiini busulfania sisältävän induktion/intensifioinnin jälkeen AML/MDS:ssä; suuri valmistunut tutkimus, luokan A relevanssi |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Vaihe 2 | Aktiivinen, ei rekrytoi | 116 | Venetoclax + ajoitettu peräkkäinen busulfani/kladribiini/fludarabiini esilääkitys suoraan AML:n ja MDS:n potilaissa |
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Vaihe 2 | Rekrytoi | 220 | Satunnaistettu vertailu bendamustinesta vs. ruxolitinibistä, jotka on lisätty fludarabiini/busulfani esilääkitykseen haploidentisen HSCT:n yhteydessä |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Vaihe 2 | Aktiivinen, ei rekrytoi | 204 | Ajoitettu peräkkäinen busulfani sekä siirron jälkeinen siklofosforamidi esilääkitys verisiirauksille, mukaan lukien MDS |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Vaihe 2/3 | Valmistunut | 2000 | Suuri hoitokehitysohjelma vanhemmille AML/korkean riskin MDS-potilaille, sisältäen busulfanipohjaisia kaavioita |
| [NCT00002989](https://clinicaltrials.gov/study/NCT00002989) | Vaihe 3 | Tuntematon | 207 | Satunnaistettu vaiheen 3 tutkimus intensivoida esilääkityskaavioita allo-HSCT:ssa leukemian/MDS:n osalta, joissa on korkea uusiutumisen riski |
| [NCT03779854](https://clinicaltrials.gov/study/NCT03779854) | Vaihe 2 | Rekrytoi | 68 | Monikeskuksinen satunnaistettu tutkimus naiivien T-solujen depletioinnista kronikisen GVHD:n ehkäisemiseksi siirron jälkeen |
| [NCT01861106](https://clinicaltrials.gov/study/NCT01861106) | Vaihe 2 | Rekrytoi | 144 | Allo-HSCT GATA2-puutokselle/MonoMAC-oireyhtymälle, joka usein etenee MDS:ksi |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Valmistunut | 120 | Busulfani, etopositidi ja siklofosforamidi esilääkitys MDS/MPD-potilaille, joiden ikä on 51–60 vuotta |
| [NCT01622556](https://clinicaltrials.gov/study/NCT01622556) | Vaihe 2 | Loppuutettu | 6 | Vähennetyn intensiteetin busulfani/TBI/tymoglobuliini esilääkitys napanuoraverensiirron kanssa; pieni, loppuutettu, rajallinen arvo |

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (Vaihe 3) | The Lancet Haematology | Satunnaistettu ei-alemmuustutkimus: treosulfani vs. busulfani/fludarabiini esilääkitys vanhemmille AML/MDS-potilaille, jotka käyvät läpi allo-HSCT:tä |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (Vaihe 3) | J Clin Oncol | Satunnaistettu tutkimus vertaamassa myeloablatiivista vs. vähennetyn intensiteetin busulfanipohjaista esilääkitystä AML/MDS:lle |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (Vaihe 3) | The Lancet Haematology | Avoin monikeskuksinen satunnaistettu tutkimus: G-CSF+dekitabiini+busulfani/siklofosforamidi vs. busulfani/siklofosforamidi yksinään relapsien vähentämiseksi MDS/sekundaarissa AML:ssä |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Kohortti | American Journal of Hematology | Lopullinen analyysi: treosulfani parantaa tuloksia verrattuna vähennetyn intensiteetin busulfaniin vanhemmille AML/MDS allo-HSCT-potilaille |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Järjelmällinen katsaus / Meta-analyysi | Frontiers in Oncology | Pitkäaikaisten tulosten treosulfani- vs. busulfanipohjaiset esilääkitykset MDS/AML:ssä ennen HSCT:tä |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Kohortti | Transplantation and Cellular Therapy | Taipumuspisteillä sovittu retrospektiivinen vertailu treosulfani- vs. busulfanipohjaista esilääkitystä MDS:ssä (n=138) |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Katsaus | American Journal of Hematology | Nykyaikainen katsaus allogenisesta HSCT:stä MDS:lle ja myelofibroosulle, joka kattaa esilääkitysstrategian |
| [38176654](https://pubmed.ncbi.nlm.nih.gov/38176654/) | 2024 | Retrospektiivinen kohortti | Transplantation and Cellular Therapy | Pitkäaikaiset komplikaatiot treosulfani- vs. busulfanipohjaisen esilääkityksen jälkeen lapsuusiän akuutin leukemian/MDS:n osalta |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Kohortti | Transplantation and Cellular Therapy | Myeloablatiivisen busulfanin + fludarabiinin in vivo T-solujen depletioinnilla on osoitettu olevan turvallinen ja tehokas AML/MDS:lle |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Taipumuspisteillä sovittu kohortti | Bone Marrow Transplantation | Fludarabiini/busulfani vs. busulfani/siklofosforamidi myeloablatiivinen esilääkitys MDS:lle, koko maan laajuinen Japanin rekisteri |

---

## Suomen markkinatiedot

Busulfanilla ei ole tällä hetkellä **mitään markkinoinnin hyväksyntätietueita todistepakkauksessa Suomelle** (markkinatilanne: Ei markkinoilla; 0 hyväksyntää aktiivisia). Tuotteen tasoisesta lisensointitiedosta ei ole saatavilla arviointia varten.

---

## Sytotoksisuus

Busulfani on hyvin vakiintunut sytotoksinen alkiloiva aine, jota käytetään korkean annoksen myeloablatiivisissa kaavioissa; se täyttää antineoplastisen/sytoktoksisen määrityksen lääkeluokan (alkiloiva aine) ja sen roolin perusteella myeloablatiivisessa kemoterapiassa.

| Kohta | Sisältö |
|------|---------|
| Sytoktoksisuuden luokitus | Tavanomaiset sytotoksiset (alkiloiva aine; myeloablatiivinen esilääkitysaine) |
| Myelosuppression-riski | Korkea — myeloablatatio on tarkoituksenmukainen terapeuttinen vaikutus; syvä, pitkäkestoinen pankytopenia odotetaan kaaviolla, erityisesti HSCT-esilääkitysannoksissa |
| Oksentamisen aiheuttamisen luokitus | Korkea (erityisesti korkean annoksen IV esilääkityskaavioissa) |
| Seurannan kohteet | CBC-testi differentiaalilla, maksatoiminta (veno-oklusiivinen tauti/sinusoidaalinen obstruktsiosyndrooman riski), keuhkotoiminta ("busulfan-keuhko"/keuhkofibroosu), saivaisten ennaltaehkäisy korkealla annoksella ja terapeuttinen lääkkeen seuranta (busulfanin plasman tasot), missä sitä käytetään esilääkitykseen |
| Käsittelyn suojaus | Sytoktoksisen lääkkeen käsittelyn varotoimet vaaditaan (PPE, suljetun järjestelmän siirtolaiteet institusionaalisten sytoktoksisten käsittelyprotokollien mukaisesti) |

Yksi tunnistettu julkaisu ([PMID 37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/)) arvioi erityisesti busulfanin yhteyttä sekundaarisen pahanlaatuisen kasvainriskin kanssa, joka on merkityksellinen pitkäaikaisen turvallisuuden seurantaan ei-pahanlaatuisissa tai parantoavan tarkoituksen mukaissa siirtoasetelmissa.

---

## Turvallisuushuomiot

Katso turvallisuustiedoista pakkauksen selosteesta. Tärkeimmät varoitukset, vasta-aiheet ja lääkkeiden väliset vuorovaikutustiedot eivät olleet käytettävissä todistepakkauksessa (DDI-kysely palautti nolla tuloksia), ja tämä merkitään **Blocking**-tietoaukoksi (DG001), joka on ratkaistava ennen mitään S1 turvallisuuden arviointia.

---

## Muut ennustetut indikaatiot (Alhaisempi prioriteetti)

Tämä todistepakkaus pisteitti busulfanin myös 9 muuta ehdokas-indikaatiota vastaan, kaikki sijoittuivat MDS:n alapuolelle ja olivat mekanistisesti siihen liittyvät laajemmaksi verisiirauden/luuydimen vioittumisen klusteriksi, paitsi kaksi, jotka merkittiin todennäköisiksi verkon häiriöiden seurauksiksi:

| Sijoitus | Indikaatio | Todisteiden taso | Suositus |
|------|-----------|----------------|-----------------|
| 2 | Lapsuuden refraktorinen sytopennia | L2 | Tutkimuskysymys |
| 3 | Luokittelematon myelodyplastinen oireyhtymä | L3 | Tutkimuskysymys |
| 4 | Kromosomin 5q:n osittainen poistuminen (5q--oireyhtymä) | L5 | Pidä |
| 5 | Aregeneratiivinen anemia (aplastinen anemia) | L2 | Jatka varavaraisuuksilla |
| 6 | Vakava synnynnäinen hypokrominen anemia rengastettujen sideroblastien kanssa | L5 | Pidä |
| 7 | HIV-infektiosairaus | L3 | Tutkimuskysymys |
| 8 | Neurokeihityshäiriö (ataksinen käynti/puheettomyys) | L5 | Pidä — todennäköisesti verkon häiriö |
| 9 | Seborroinen keratoosi | L5 | Pidä — todennäköisesti väärä positiivinen |
| 10 | Kissojen hankittu immuunikadon oireyhtymä | L5 | Pidä — muille kuin ihmisille kuuluva laji, tulisi sulkea pois arvioinnista |

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varavaraisuuksilla**

**Perustelut:**
Myelodyplastisella oireyhtymällä on vahvin todistepohja kaikista ennustetuista indikaatioista (L1: useita valmistuneita vaiheen 3 RCT:tä, jotka vertaavat suoraan busulfanipohjaisiin esilääkityskaavioihin tässä populaatiossa), ja busulfanipohjaisella esilääkityksellä on jo vakiintunut standardi hoitokallo allo-HSCT:n edellä MDS:lle. Kuitenkin busulfani ei ole tällä hetkellä markkinoilla Suomessa ja kriittiset turvallisuuden dokumentointi (TFDA/Fimea-merkinnän varoitukset ja vasta-aiheet) puuttuvat, joten varavaraisuudet ovat tarpeen ennen jatkamista.

**Jatkaakseen tarvitaan seuraavaa:**
- Ratkaise estävä tietoaukko DG001: hanki viralliset Suomen/EU-pakkauksen selosteesta varoitukset ja vasta-aiheet
- Ratkaise korkea-prioriteettinen tietoaukko DG002: vahvista yksityiskohtainen vaikutusmekanismi DrugBankista tai tuotteen merkinnästä
- Vahvista, onko Suomessa/EU:ssa busulfanille mikään markkinoinnin hyväksyntä missään tuotemerkin alla (esim. Busilvex) huolimatta täällä näytettävästä "ei markkinoilla" -statuksesta
- Muodosta lääkkeiden väliset vuorovaikutusprofiilit (nykyinen DDI-kysely palautti nolla dataa)
- Kehitä seuranta- ja sytoktoksisen käsittelyn protokolla, joka on erityinen esilääkitysannoksen käytölle MDS:n siirron ehdokkaissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

