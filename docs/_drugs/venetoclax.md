---
layout: default
title: Venetoclax
parent: Vahva näyttö (L1-L2)
nav_order: 400
evidence_level: L1
indication_count: 10
---

# Venetoclax
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

# Venetoclax: hematologisesta pahanlaatuisesta kasvaimesta akuuttiin myeloidiseen leukemiaan (Taiwanin uudelleenkäytön ehdokas)

## Yhden lauseen yhteenveto

> Venetoclax (DB11581) on selektiivinen BCL-2-inhibiittori, jota käytetään kansainvälisesti useissa B-solujen ja myeloidisten pahanlaatuisten kasvainten hoitoon, mutta sitä **ei tällä hetkellä markkinoida Taiwanissa** (0 hyväksyntää hakemuksessa).
> Kymmenen ehdokkaan indikaatioista, joita TxGNN on ehdottanut tälle lääkkeelle, **Akuutti myeloidiläinen leukemia (myeloidiläinen leukemia)** nousee esiin ainoana, joka on tuettu todella kypsällä näytöpohjalla — **50+ kliininen tutkimus** ja **20 julkaisua**, mukaan lukien yhdistelmähoitojärjestelmät, joita käsitellään jo kansainvälisesti vakiohoidoksi — kun taas loput 9 ehdokasta ovat ohuita, väärin merkittyjä tai puhtaasti pistelaskennasta peräisin.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei dokumentoitu tässä näytösarjassa — venetoclax ei ole vielä markkinoilla Taiwanissa, joten paikallista hyväksyttyä indikaatiotekstiä ei ole olemassa |
| Ennustettu uusi indikaatio (otsikko) | Myeloidiläinen leukemia (Akuutti myeloidiläinen leukemia) |
| TxGNN-ennustepisteet | 99,47% (maailmanlaajuisen mallin sijoitus 5 697) |
| Todistusvoimataso | L1 |
| Taiwanin markkinatila | ✗ Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntojen lukumäärä | 0 |
| Suositeltu päätös | **Pidätä** (sääntelyyn/turvallisuuteen liittyvä este) — katso perustelut alla |

**Huomautus soveltamisalasta:** tämä näytösarja on monihintaisen ehdokkaan kokonaisuus (`TW-DB11581-multi`) joka sisältää 10 luokiteltua ennustetta. Korkein pistelaskennalla mitattu yksittäinen ennuste (tietty pre-germinaaliset CLL/SLL-alaryhmä) on lähes ilman tukea, joten tämä raportti aloitetaan ehdokkaalla, jolla on vahvin, eniten päätökseen liittyvä näyttö sen sijaan, että lähtisimme raa'ista #1-pistelaskennasta. Kaikki 10 on yhteenveto alla kokonaisuuden vuoksi.

### Yleiskatsaus kaikkiin ennustettuihin indikaatioihin

| Sijoitus | Sairaus | TxGNN-pisteet | Todistusvoimataso | Päätösvaihe | Suositus |
|------|---------|--------------|-----------------|-----------------|-----------------|
| 1 | Pre-germinaaliset CLL/SLL | 99,55% | L4 | S1 | Tutkimuskysymys |
| 2 | CLL/SLL (IGHV-mutatoitu alaryhmä) | 99,55% | L5 | S0 | Pidätä |
| 3 | Hodgkinin lymfooma ⚠ | 99,51% | L3 | S1 | Tutkimuskysymys |
| 4 | **Myeloidiläinen leukemia (AML)** | 99,47% | **L1** | **S3** | **Jatka varauksellisesti** |
| 5 | Krooninen myeloidiläinen leukemia (CML), BCR-ABL1+ | 99,36% | L2 | S2 | Tutkimuskysymys |
| 6 | Ewingin sarkooma | 99,21% | L4 | S0 | Pidätä |
| 7 | Follikulaarinen lymfooma | 99,15% | L2 | S2 | Tutkimuskysymys |
| 8 | Metastaattinen neoplasma (yleinen) | 99,14% | L3 | S0 | Pidätä |
| 9 | Pahanlaatuinen spiradenoma | 99,12% | L5 | S0 | Pidätä |
| 10 | AML translokaatiolla t(8;21) | 99,08% | L4 | S1 | Tutkimuskysymys |

⚠ **Tiedon laatukeino (Sijoitus 3, Hodgkinin lymfooma):** 50 liitettyä tutkimusta ja 20 julkaisua käsittelevät ylivoimaisesti CLL-, DLBCL-, manttelisolulymfoomaa ja follikulaarista lymfoomaa — **ei yksikään otsikko viittaa nimenomaisen klassisen Hodgkinin lymfoomaan**. Tämä viittaa vahvasti nimikkeen/luokittelun epäsopivuuteen (laaja "B-solulymfooma"-näyttösarja liitettiin Hodgkinin lymfoomasolmuun). Tätä indikaatiota ei pitäisi edetä ilman perusteellista uudelleentarkistusta taustalla olevasta sairausmäärityksestä.

---

## Miksi tämä ennuste on järkevä?

Jäsennelty `original_moa`-kenttä tälle pakettisarjalle on tyhjä (tiedon puute), ja mitään Taiwanin hyväksymää alkuperäisen indikaation tekstiä ei ole, koska lääkettä ei ole vielä markkinoilla paikallisesti. Mekanismi on kuitenkin johdonmukaisesti dokumentoitu näytösarjan omissa perustelusissa: venetoclax on **selektiivinen, suun kautta otettava BCL-2 (B-solulymfooma-2)-inhibiittori**, joka palauttaa sisäisen apoptoottipolun toiminnan soluissa, jotka ovat tulleet epänormaalisti riippuvaisiksi BCL-2-välitteisestä selviämisestä.

Tämä mekanismi selittää suoraan AML-signaalin vahvuuden: leukemian blast-solut ja leukemian kantasolut usein luottavat BCL-2-välitteiseen apoptoosin välttämiseen, ja venetoclax yhdessä hypometylaintiaineiden (asatsitidin/desitabiinin) tai matalan annoksen sytoaranosin kanssa on tullut hyvin perustetuksi hoitojärjestelmäksi potilaille — erityisesti vanhemmille tai heikossa kunnossa oleville potilaille — joilla on äskettäin diagnosoitu tai relaps/resistentti AML. Toisin kuin useimmat muista 9 ehdokkaasta tässä paketissa, AML-ennuste on tuettu syvällä, useiden vuosikymmen mittaisella tutkimus- ja julkaisutietueella, joka ulottuu 1. vaiheen tutkimuksista 3. vaiheen tutkimuksiin, mukaan lukien kunnossapitorapian ja leikkausta seuraavan istutuksen asetukset.

Sitä vastoin useat muut ehdokkaat tässä paketissa (CLL/SLL-molekyyliset alaryhmät, Ewingin sarkooma, pahanlaatuinen spiradenoma) jakavat saman taustalla olevan BCL-2-perustelun periaatteessa, mutta heillä ei ole sairauskohtaisia tutkimuksia tai vain preklinistä/mekanistista kirjallisuutta — eli mekanistinen uskottavuus on todellinen, mutta kliininen vahvistus on olennaisesti puuttuu.

---

## Kliinisen tutkimuksen näyttö (Myeloidiläinen leukemia / AML)

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT06713837](https://clinicaltrials.gov/study/NCT06713837) | Vaihe 3 | Rekrytoi | 339 | IMPACT-AML: satunnaistettu pragmaattinen tutkimus korkea- vs matala-intensiteetin uudelleen induktiohoidosta 1. / 2. relapsi-AML:ssä |
| [NCT03404193](https://clinicaltrials.gov/study/NCT03404193) | Vaihe 2 | Lopetettiin | 235 | Venetoclax + 10 päivän desitabiini äskettäin diagnosoidussa iäkkäillä tai resistentissä AML:ssä ja korkean riskin MDS:ssä |
| [NCT03941964](https://clinicaltrials.gov/study/NCT03941964) | Vaihe 3 | Valmis | 60 | Poliklininen venetoclax + asatsitidin/desitabiini hoitamattomassa AML:ssä, joka ei kelpaa intensiiviselle kemoterapialle — heijastaa sääntelyarvioitua vakiohoidon hoitojärjestelmää |
| [NCT04161885](https://clinicaltrials.gov/study/NCT04161885) | Vaihe 3 | Lopetettiin | 465 | VIALE-T: venetoclax + asatsitidin allogeenisen istutuksen jälkeisenä kunnossapitona yleisen selviämisen parantamiseksi |
| [NCT05404906](https://clinicaltrials.gov/study/NCT05404906) | Vaihe 2/3 | Rekrytoi | 124 | Asatsitidin + venetoclax kunnossakunto suotuisa-riski-AML:ssä ensimmäisen remission jälkeen |
| [NCT02287233](https://clinicaltrials.gov/study/NCT02287233) | Vaihe 1/2 | Valmis | 94 | Perustutkimus: venetoclax + matalan annoksen sytoaranoosi hoitamattomissa AML-potilaissa ≥60 vuotta, joille antrasiokliini-induktio ei kelpaa |
| [NCT07007312](https://clinicaltrials.gov/study/NCT07007312) | Vaihe 3 | Rekrytoi | 1 300 | Ziftomenibi lisätty vakiohoidon venetoclax+asatsitidiin (tai intensiiviseen 7+3) NPM1-mutatuneessa/KMT2A-uudelleenmuodostaneessa AML:ssä |
| [NCT07469046](https://clinicaltrials.gov/study/NCT07469046) | Vaihe 3 | Ei vielä rekrytointivaiheessa | 308 | Venetoclax+asatsitidin+homoharringtoviini vs venetoclax+asatsitidin yksinään iäkkäillä äskettäin diagnosoiduilla AML:llä |
| [NCT06611839](https://clinicaltrials.gov/study/NCT06611839) | Vaihe 1/2 | Rekrytoi | 29 | Venetoclax + ivosidenib + asatsitidin kolmoishoidon yhdistelmä IDH1-mutatuneessa AML:ssä |
| [NCT04146038](https://clinicaltrials.gov/study/NCT04146038) | Vaihe 2 | Valmis | 5 | Salsalaatti lisätty venetoclax + desitabiini/asatsitidiin AML:ssä tai edistynyt MDS/MPN |

*10 yli 50 käytettävissä olevasta tutkimuksesta, priorisoitu vaiheen, otoskoon ja suoran olevan olevuuden vakiohoidon hoitojärjestelmän mukaan.*

---

## Kirjallisuuden näyttö (Myeloidiläinen leukemia / AML)

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Katsaus | Biomedicine & Pharmacotherapy | Yleiskatsaus venetoclaxin antileukemisesta aktiivisuudesta prekliinisissä AML-malleissa ja kliinisissa tutkimuksissa, yksinään ja yhdessä |
| [31203996](https://pubmed.ncbi.nlm.nih.gov/31203996/) | 2019 | Katsaus | Best Practice & Research Clin Haematology | Venetoclax-pohjaisten hoitojen kontekstualisointi 8:n uuden AML-lääkkeen joukossa, jotka hyväksyttiin vuodesta 2017 lähtien |
| [34329576](https://pubmed.ncbi.nlm.nih.gov/34329576/) | 2021 | Vaihe 2 kohortti | The Lancet Haematology | Venetoclax + kladribiini/idarubisin/sytoaranoosi (CLIA) äskettäin diagnosoidussa AML/korkean riskin MDS:ssä, potilaat ≤65 vuotta |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Kohortti | Clinical Cancer Research | Venetoclax + asatsitidiin teho/turvallisuus hoitamattomissa IDH1/2-mutatuneissa AML:ssä |
| [38866760](https://pubmed.ncbi.nlm.nih.gov/38866760/) | 2024 | Katsaus | Cell Death & Disease | Venetoclax hoito ja nousevat resistenssimekanismit AML:ssä |
| [39303729](https://pubmed.ncbi.nlm.nih.gov/39303729/) | 2024 | Vaihe 2 kohortti | The Lancet Haematology | Desitabiini + venetoclax + ponatinibi edistynyt vaihe Ph+ myeloidinen sairaus ja Ph+ AML |
| [37599456](https://pubmed.ncbi.nlm.nih.gov/37599456/) | 2024 | Verkkometaanalyysi | J Chemotherapy | Venetoclax+asatsitidin vs ivosidenib/enasidenib soveltumattomissa äskettäin diagnosoiduissa IDH1/2-mutatuneissa AML:ssä — suosii venetoclax yhdistelmää yleisessä selviämisessä |
| [34966123](https://pubmed.ncbi.nlm.nih.gov/34966123/) | 2022 | Katsaus | Current Opinion in Hematology | Tutkimus venetoclax-yhdistelmähoidoista AML:ssä ja MDS:ssä |
| [32031033](https://pubmed.ncbi.nlm.nih.gov/32031033/) | 2020 | Katsaus | Leukemia & Lymphoma | Venetoclax + HMA/LDAC perustettu uudeksi vakiohoidoksi etulinjassa soveltumattomissa/iäkkäillä AML:ssa |
| [39246164](https://pubmed.ncbi.nlm.nih.gov/39246164/) | 2024 | Katsaus | Expert Review of Hematology | Relaps ja resistenssi mallit etulinjassa venetoclax-pohjaisesti AML-hoitoa seuraten ja toissijainen strategiat |

---

## Muut huomattavat ennustetut indikaatiot (Toissijaiset ehdokkaat)

- **CML, BCR-ABL1 positiivinen (Sijoitus 5, L2, Tutkimuskysymys):** Useat vaihe 2 tutkimukset yhdistävät venetoclaxin TKI:ihin (dasatinibi, ponatinibi) TKI-kestävien leukemian kantasolujen poistamiseksi — aktiivinen tutkimussuunta, ei vielä vakiohoidon (esim. [NCT02689440](https://clinicaltrials.gov/study/NCT02689440), [NCT04188405](https://clinicaltrials.gov/study/NCT04188405)).
- **Follikulaarinen lymfooma (Sijoitus 7, L2, Tutkimuskysymys):** Suoraan yhdenmukainen t(14;18) BCL-2 ylientoitumisen kanssa, joka määrittelee FL:n. Omistettu vaihe 2 (venetoclax+obinutusumabi+bendamusti, PrE0403, [PMID 40355425](https://pubmed.ncbi.nlm.nih.gov/40355425/)) raportoitu 2025, mutta teho on ollut epäjohdonmukaista riittävän paljon, ettei FL ole vielä rekisteröity indikaatio.
- **Sijoitukset 1, 2, 6, 8, 9, 10 (Pidätä / matala prioriteetti):** Joko erittäin kapeat molekyylialaryhmät ilman omistettuja tutkimuksia, yleinen monisairaus-etiketti ("metastaattinen neoplasma") joka sekoittaa toisiinsa liittymättömiä kiinteitä kasvaimia tai (pahanlaatuinen spiradenoma) harvinainen kasvain, jolla ei ole nolla tutkimusta tai kirjallisuutta. Mitään ei pitäisi edetä ilman uutta omistettua näyttöä.

---

## Taiwanin markkinatiedot

Venetoclaxilla on tällä hetkellä **0 markkinointilupaa Taiwanissa** (markkinatila: Ei markkinoilla / ei markkinoilla). Tuotelisensejä, annosmuotoja tai hyväksyttyjä indikaatiotekstejä ei ole saatavissa tässä näytösarjassa.

---

## Sytostaattisuus

Venetoclax on antineoplastinen aine (BCL-2-inhibiittori, jota käytetään CLL/SLL:n, AML:n ja muiden B-solulymfoomien hoidossa), joten tämä osio koskee sitä.

| Kohta | Sisältö |
|------|------|
| Sytostaattisuuden luokittelu | Kohdennettu hoito (selektiivinen BCL-2-inhibiittori) — johdonmukaisesti tunnistettu sellaiseksi näytösarjan omissa perusteluissa |
| Ydintuotannon vähentymisen riski | Ei saatavissa tässä näytösarjassa |
| Pahoinvointiriskin luokittelu | Ei saatavissa tässä näytösarjassa |
| Valvonnan kohteet | Ei saatavissa tässä näytösarjassa |
| Käsittelysuoja | Ei saatavissa tässä näytösarjassa |

Ydintuotannon vähentymisen riski, pahoinvointiriskin, valvonnan ja käsittelysuojan yksityiskohdat eivät ole saatavissa tässä näytösarjassa — katso pakkausselosteen varoituksia ja varotoimenpiteitä, kun TFDA-merkintä (katso tiedon puute DG001 alla) on saatu.

---

## Turvallisuusharkinnat

Katso pakkausselosteen turvallisuustietoja. (Keskeiset varoitukset, vasta-aiheet ja lääkkeiden välisen yhteisvaikutuksen tiedot ovat kaikki tällä hetkellä saatavissa tässä näytösarjassa — DDI-kysely tila: ei löydetty.)

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä** (sääntelyyn/turvallisuuteen liittyvä este), kun taustalla oleva AML-tehokkuus tapaus muuten täyttää **Jatka varauksellisesti** kriteerit.

**Perustelut:**
- Myeloidiläisen leukemian (AML) indikaatiolla on vahva, kypsä kliininen näyttö (L1, 50+ tutkimusta, 20 julkaisua) ja se heijastaa hoitoa, jota käsitellään jo vakiohoidoksi kansainvälisesti.
- Kuitenkin **kriittinen tiedon puute (DG001)** tarkoittaa, että TFDA-pakkausselosteen varoitukset/vasta-aiheet eivät ole vielä saatavissa, mikä tämän putkilinjan omien kriteerien mukaan estää S1-turvallisuuden ennakkohyväksynnän suorittamisen — joten mikään etenemispäätös ei voi valmistua ennen kuin tämä kuilu on suljettu, riippumatta tehokkuuden vahvuudesta.
- Venetoclax ei ole tällä hetkellä markkinoilla Taiwanissa (0 lupaa), joten mitään paikallisen sääntelyyn kuuluvaa ennakkotapausta ei ole olemassa; mikä tahansa uudelleenkäytön polku vaatisi todennäköisesti täyden uuden rekisteröitimisen reitin pikemminkin kuin etiketin laajennusreitin.

**Jatkaakseen, seuraavat tiedot ovat tarpeen:**
- TFDA-pakkausseloste (varoitukset, vasta-aiheet) — oikaisu: lataa ja jäsennä TFDA:n verkkosivustolta (DG001, Kriittinen).
- Rakennettu vaikutusmekanismi -vahvistus DrugBankista korvaamaan nykyisen tiedon puutetta (DG002, Korkea).
- Hodgkinin lymfoomaetiketti (Sijoitus 3) näytösarjan manuaalinen uudelleentarkistus, joka näyttää epäsopivan sairauden etiketille.
- Muodollinen DDI-kysely, koska nykyinen kysely palautti "not_found" täytetyn tuloksen sijaan.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

