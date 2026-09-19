---
layout: default
title: Glucagon
parent: Pelkkä mallin ennuste (L5)
nav_order: 178
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

# Glukaagoni: nimeämättömästä alkuperäisestä indikaatiosta irritaabelin suolitaudin hoitoon

## Yhden lauseen yhteenveto

Glukaagoni (DrugBank DB00040) on haiman hormonaalinen aine; tässä todistusaineistossa ei ole saatavilla alkuperäistä indikaatiota, vaikutusmekanismia tai Suomen markkinointitietoja. TxGNN-malli ennustaa **99.24%**:n pistemäärän **irritaabelin suolitaudille (IBS)**, mutta lähes kaikissa 11 kliinisessä tutkimuksessa ja 20 julkaisussa käsitellään itse asiassa **GLP-1 (glukagonimaisen peptidi-1) reseptorin agonisteja** (liraglutidi, ROSE-010, eksendini-4, luonnollinen GLP-1) — erilaista peptidia ja reseptorijärjestelmää — eikä glukaagonia sinänsä, mikä viittaa voimakkaasti nimen yhteentörmäyksen seurauksiin eikä todelliseen hoitosovellukseen.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Tietoja ei ole saatavilla (lääke ei ole markkinoilla Suomessa; alkuperäistä indikaatiota ei ilmoitettu lähdeaineistossa) |
| Ennustettu uusi indikaatio | Irritaabeli suolitauti |
| TxGNN-ennusteen pistemäärä | 99.24% |
| Todistusaineiston taso | L5 |
| Suomen markkinoinnin tila | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odotus |

## Miksi tämä ennuste on kohtuullinen?

Glukaagonin yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla tässä todistusaineistossa, eikä alkuperäistä indikaatiota tai Suomen lupahallinnon rekisteriä ole vertailun ankkuriksi.

Vielä tärkeämpää on, että haettu todistusaine sinänsä herättää **tietojen laadun huolia pikemminkin kuin tukeakseen ennustusta**. Glukaagoni ja GLP-1 (glukagonimainen peptidi-1) ovat molemmat saman *proglucagon*-geenin pilkkoutumistuotteita, mutta ne vaikuttavat rakenteellisesti eri reseptoreihin, joilla on erilaiset — joiltain osin vastakkaiset — fysiologiset vaikutukset: glukaagoni nostaa veren glukoosia glukaagonireseptorin kautta (maksan glykogeenilyysis/glukoneogeneesi), kun taas GLP-1 on inkretiini, joka vaikuttaa GLP-1-reseptoriin hidastaakseen mahalaukun tyhjentymistä, moduloidakseen suolistonliikkeitä ja estääkseen glukagonipin vapautumista. Käytännössä kaikissa täällä esitetyissä tutkimuksissa ja julkaisuissa (liraglutidi, ROSE-010, eksendini-4, "luonnollinen GLP-1") testataan GLP-1-reseptoriagonisteja, ei glukaagonia.

Tämä kuvio on johdonmukainen hakusana-vastaavuuden seurauksien kanssa: merkkijono "glucagon" esiintyy "glucagon-like peptide-1":n sisällä lähes jokaisessa lähdeasiakirjassa, mikä voi paisuttaa sekä hakutulosten määrää että TxGNN-pistemäärää ilman, että mikään todistusaine todella liittyy glukaagoniin. Mikään tutkimus tai julkaisu tässä paketissa ei testaa glukaagonia (hormonia) suoraan irritaabelia suolitautia vastaan. Puuttuvien vaikutusmekanismien, puuttuvan alkuperäisen indikaation ja "ei markkinoilla" -tilan yhdessä ennuste olisi käsiteltävä kohtuuttomana toimimisen perusteena, kunnes taustalla olevat entiteetin sekaannukset on ratkaistu.

## Kliiniset tutkimusnäytteet

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Valmistunut | 37 | Kolon butyraatin vaikutusmekanismi IBS:ssä; glukagonia ei ole kytkeytynyt (merkitys: C — ei liity asiaan) |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Aktiivinen, ei rekrytoida | 375 | Ohutsuolen organoidimalli ravinnon antigeeneille/terapeuttisille hoidoille; glukagonia ei ole kytkeytynyt (merkitys: C — ei liity asiaan) |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Vaihe 2 | Lopetettu (n=8) | 8 | Testaa liraglutidi (GLP-1-reseptoriagonisti), ei glukaagonia, IPAA-potilailla, joilla on korkea suolistojen toimintatiheys (merkitys: C — väärä lääke) |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Valmistunut | 33 | Täysjyväisen ruisjärneen vaikutus suoliston mikrobiota-aivoakselin toimintaan; glukagonia ei ole kytkeytynyt (merkitys: C — ei liity asiaan) |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Valmistunut | 12 | Frukto-oligosakkaridisuplementointi reaktiivisessa hypoglykemiassa; ei glukagonin interventiotutkimus (merkitys: C — ei liity asiaan) |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Tuntematon | 110 | Matalakalorinen ruokavalio vs. ruokavalio + intragastrinen ilmapallo lihavuudessa; glukagonia ei ole kytkeytynyt (merkitys: C — ei liity asiaan) |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Valmistunut | 41 | Ultraproses soitujen elintarvikkeiden syömisnopeus ja aineenvaihduntavaste; glukagonia ei ole kytkeytynyt (merkitys: C — ei liity asiaan) |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Valmistunut | 66 | Liikuntakoulutuksen vaikutukset suoliston dysbioosiin ja GLP-1:een (ei glukaagonia) IBS:ssä (merkitys: C — väärä hormoni) |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Vaihe 1 | Valmistunut | 12 | Luonnollinen GLP-1 vs. GLP-1-analogi ROSE-010 ruoansulatuselimistön liikkuvuudessa; ei glukaagonia (merkitys: C — väärä lääke) |
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Vaihe 1/2 | Valmistunut | 52 | ROSE-010 (GLP-1-analogi) vaikutus ruoansulatuselimistön liikkuvuuteen ummetusvoittoista IBS:ää vastaan; ei glukaagonia (merkitys: C — väärä lääke) |

Kaikki yllä luetellut 10 tutkimusta on luokiteltu **C (alhainen/ei merkitystä)** -tasolla lähdeaineistossa — mikään niistä ei testaa suoraan glukaagonia IBS:ssä.

## Kirjallisuusnäytteet

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeiset löydökset |
|------|-----|------|------|---------|
| [36269141](https://pubmed.ncbi.nlm.nih.gov/36269141/) | 2022 | RCT | Gut Microbes | Probioottinen *Bacillus subtilis* BS50 vähentää ruoansulatuselimistön oireita terveillä aikuisilla; ei liity glukaagoniin |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | Kivunvaste GLP-1-reseptoriagonistiin ROSE-010 IBS:n alaryhmissä — GLP-1, ei glukaagoni |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Kohortti | Annals of Gastroenterology | GLP-1-reseptoriagonistien määräämisen/keskeyttämisen kaavat IBS-potilailla — GLP-1, ei glukaagoni |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Katsaus | Cell Mol Gastroenterol Hepatol | Aivojen-suoliston-mikrobiomi-akselin yleiskatsaus; ei käsittele glukaagonia erityisesti |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Katsaus | Frontiers in Endocrinology | Systemaattinen katsaus/metaanalyysi GLP-1-reseptoriagonistien vaikutuksesta IBS:n paranemiseen — GLP-1, ei glukaagoni |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Katsaus | The Journal of Headache and Pain | GLP-1-reseptoriagonistit päänsärkyn/kivun häiriöihin; huomautukset siitä, että GLP-1 estää glukagonipin vapautumista (vastakkainen suunta) |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Katsaus | Experimental Physiology | L-soluista peräisin olevan GLP-1:n rooli IBS:n patofysiologiassa — GLP-1, ei glukaagoni |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Katsaus | Adv Exp Med Biol | Aerosoli-GLP-1 diabetekseen ja IBS:ään; GLP-1, ei glukaagoni |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Katsaus | Therapeutic Advances in Gastroenterology | Yleinen IBS-hoidon katsaus kuidun/antispasmodien lisäksi; ei glukagonikohtaisia tietoja |
| [23330973](https://pubmed.ncbi.nlm.nih.gov/23330973/) | 2013 | Katsaus | Expert Opin Drug Metab Toxicol | Aineenvaihdunta- ja toksikologiset näkökulmat uusiin IBS-lääkkeisiin; ei glukagonikohtaisia tietoja |

## Suomen markkinointi-informaatio

Glukaagonia ei ole tällä hetkellä markkinoilla Suomessa — tässä todistusaineistossa ei ole hyväksynnän rekisteritietoja.

## Turvallisuusnäkökohdat

Katso turvakysymysten osalta pakkausselosteesta.

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Odotus**

**Perustelut:**

Ennustusta tukevat näytteet koskevat lähes kokonaan GLP-1-reseptoriagonisteja (erillinen hormoni/reseptorijärjestelmä), eivät itse glukaagonia, mikä osoittaa, että TxGNN-pistemäärä ja haetut näytteet ovat todennäköisesti peräisin nimen yhteentörmäyksen seurauksista ("glucagon" within "glucagon-like peptide-1") pikemminkin kuin todellisesta farmakologisesta signaalista. Yhdessä alkuperäisen indikaation, vaikutusmekanismien ja Suomen markkinointitietojen puuttumisen kanssa, tähän ehdokkaaseen ei ole tällä hetkellä perustaa edetä.

**Jatkaakseen tarvitaan seuraavaa:**

- Vahvistus TxGNN-mallin omistajilta siitä, tunnistettiinko GLUCAGON (DB00040) ja GLP-1/GLP-1-reseptoriagonistit oikein koulutuksen/pisteytyksen aikana

- Kirjallisuus- ja tutkimushaku, joka rajoittuu erityisesti haiman glukaagoniin (ei GLP-1:een) ja ruoansulatuselimistön liikkuvuuteen tai IBS:ään

- DrugBank-lähteinen alkuperäisen indikaation ja vaikutusmekanismin tiedot DB00040:lle

- Suomen/TFDA:n pakkausseloste-tiedot (varoitukset, vasta-aiheet, lääkkeiden yhteisvaikutukset), kun markkinoinnin tila muuttuu tai ehdokasta harkitaan uudelleen

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

