---
layout: default
title: Midazolam
parent: Vahva näyttö (L1-L2)
nav_order: 250
evidence_level: L2
indication_count: 1
---

# Midazolam
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **1** kpl
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

# Midatsoli: toimenpidepohjaisen sedaation soveltamisesta unettomuuden hoitoon

## Yhden lauseen yhteenveto

Midatsoli on lyhytvaikutteinen bentsodiatsipiini, joka on tällä hetkellä tarkoitettu anestesian induktioon ja toimenpidepohjaisen sedaation pikemminkin kuin suun kautta otettavaksi kroonisen unettomuuden hoitolääkkeeksi.
TxGNN-malli ennustaa, että se voi olla tehokas **unettomuuden** hoitoon, ja haussa tunnistettiin **32 kliinistä tutkimusta** ja **11 julkaisua** — vaikka vain pieni, pääosin historiallinen osajoukko suoraan tukee tätä suuntaa.
Koska paikallisen turvallisuus-/merkintätiedon kriittinen aukko on olemassa, nykyinen näyttötaso on **L2** ja suositus on **Pidätä**.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen käyttöaihe | Ei dokumentoitu todistuspaketissa (paikallista myyntilupaa ei ole tiedostoissa); saatavilla olevat tiedot osoittavat, että nykyinen kliininen käyttö on toimenpidepohjainen sedaatio / anestesian induktio |
| Ennustettu uusi käyttöaihe | Unettomuus |
| TxGNN-ennusteen pistemäärä | 99.74% |
| Näyttötaso | L2 |
| Taiwanin markkinatilanne | Ei markkinoilla |
| Lupien määrä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaista DrugBank-toimintamekanismin tekstiä ei ole saatavilla tälle kirjaukselle. Todistuspaketin uudelleensoveltamisen perustelut kuitenkin vahvistavat, että midatsoli on lyhytvaikutteinen bentsodiatsipiini, joka vaikuttaa GABA-A-reseptorin bentsodiatsipiini-sitoutumiskohtaan, tehostamalla GABAergista inhibitorisoivaa neurotransmissiota — farmakologia, joka on luonnostaan sedatiivi-hypnoottinen ja suoraan merkityksellinen unettomuuden hoitoon.

Kliinisesti midatsolia käytetään nykyään lähes yksinomaan anestesian induktion ja toimenpidepohjaisen sedaation hoitoon, ei kroonisen suun kautta otettavan unilääkkeen, pääosin sen erittäin lyhyen puoliintumisajan, injektoitavan antoreitin, kontrolloitavan aineen statuksen ja riippuvuus-/vieroitusoireiden riskin vuoksi. Ennustettu yhteys unettomuuteen ei siis ole uusi mekanistinen löytö vaan heijastaa tunnettua luokkavaikutusta, joka on yhteinen muiden bentsodiatsipiini-unilääkkeiden kanssa (esim. fluratsepaami).

Tätä luokkavaikutusta tukee todellinen historiallinen todiste: useat faasintasoiset satunnaistetut kontrolloidut tutkimukset 1980-luvulta–1990-luvulta testasivat suoraan suun kautta otettavaa midatsolia potilaissa, joilla oli uni-häiriöitä / kroonista unettomuutta, ja havaitsivat sen olevan tehokas ja yleensä hyvin siedetty, ennen kuin sen kliininen käyttö siirtyi lähes kokonaan toimenpidepohjaisen sedaation käyttöön. Tämä antaa TxGNN-ennusteelle uskottavat farmakologiset ja historialliset perusteet, vaikka se ei edustakaan uutta terapeuttista hypoteesia.

---

## Kliininen tutkimustodiste

| Tutkimuksen numero | Faasi | Tila | Rekrytointi | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Faasi 4 | Valmistunut | 111 | IV midatsoli vs. deksmedetomidiini, yhdistetty selkäydintäydytysanesteesiaan, vertaillen postoperatiivista unen laatua TURP:n jälkeen; paketissa arvioitu suoraan relevantimmaksi (Grade B) tutkimukseksi. |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Rekrytointivaiheessa | 280 | Leikkausta edeltävää suun kautta otettavaa midatsolia arvioitiin potilaissa, joilla oli uni-häiriöitä / ahdistusta ja joiden oli määrä saada laparoskoopista kolorektaalisyöpäresektiota; tutkimuskuvaus huomauttaa, että suun kautta otettava midatsoli-liuos on "turvallinen ja tehokas lyhytaikaiseen hypnoosiin." |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Faasi 3 | Rekrytointi ei ole vielä alkanut | 195 | Suun kautta otettava melatoniini vs. suun kautta otettava midatsoli esimedikointina lapsissa, joille tehtiin kurkkurisaleikkaus, vertaamalla uni-indusoivaa ja ahdistusta lievittävää vaikutusta. |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Lopetettu | 5 | Vertasi unen laatua / määrää (24 tunnin polysomnografia) ja deliriumin esiintyvyyttä deksmedetomidiinin ja midatsoolin välillä mekaanisesti ventiloitavissa teho-osastopotilaissa; lopetettu ennenaikaisesti, hyvin pieni otanta. |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Faasi 1 | Lopetettu | 6 | Polysomnografinen vertailu univaiheiden ja kokonaisuniaika:n osalta α2-agonistin (deksmedetomidiini) ja GABA-agonistin (midatsoli) sedaation välillä; lopetettu ennenaikaisesti, hyvin pieni otanta. |

*Huomio: Yhteensä 32 tutkimusta haettiin; suurin osa (arvioitu "C"-arvosanaksi tai arvioitu matalan merkityksellisyydeksi) sisältävät midatsolit vain tausta-sedaatioaineena liittymättömissä kirurgisissa / teho-osasto-tutkimuksissa eikä niitä ole lueteltu tässä näyttötaulukon selventämisen vuoksi.*

---

## Kirjallisuustodiste

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Kaksoissokkoutettu tutkimus 30 naisella lihashermon sairaudesta johtuvalla unettomuudella: midatsoli 15 mg ja Vesparax molemmat tehokkaat unilääkkeet; midatsoli paremmin siedetty ilman jäännösvaikutusta. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | Monikeskus annosten määritystutkimus (75 potilasta, suun kautta otettava midatsoli 10–30 mg) lievään tai keskivaikeaan unettomuuteen, joka oli sekundaarinen lihasluuston ja hermoston häiriöihin; määritti optimaalisen annosalueen. |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Monikeskus-, satunnaistettu, kaksoissokkoutettu, rinnakkaisryhmätutkimus unesta, suorituskyvystä ja plasmapitoisuuksista fluratsepaamin vs. midatsoolin 14 päivän käytön aikana kroonisen unettomuuden potilaissa. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Tiivistelmä yllä olevasta 14 päivän fluratsepaamin vs. midatsoolin kroonisen unettomuuden tutkimuksesta (liitännäisartikkeli; abstrakti ei ole saatavilla). |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Katsaus | Orvosi Hetilap | Yleinen katsaus unettomuuden patogeneesin (yliherätystila) ja sen suhteesta aivojen heikomperfusioon; taustatieto, ei midatsoli-spesifinen. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Katsaus | Acta Psychiatrica Scandinavica Supplementum | Katsaus unilääkkeiden kliiniseen käyttöön, käsitellen bentsodiatsipiinin farmakokineettisia / farmakodynaamisia eroja ja perusteluja eri aineiden käytölle unettomuuden erimuodoissa. |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT | Journal of Clinical Medicine | Pilottitutkimus lemborexantista (ei midatsoli) unettomuuden hoitoon korkean riskin pankreaattis-sappiväylä-potilaat endoskopian jälkeen; tutkimus huomauttaa, että perinteisesti unettomuudessa käytetyt bentsodiatsepiinit voivat pahentaa deliriumin riskiä — merkityksellinen turvallisuuskonteksti. |

---

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta.

*(Tärkeimmät varoitukset, vasta-aiheet ja lääke-lääke-vuorovaikutustiedot eivät ole tällä hetkellä saatavilla tälle kirjaukselle — DDI-kysely palautti "not_found" ja TFDA-pakkausselosteen varoitukset / vasta-aiheet on merkitty estävä tietoaukko, DG001.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Historialliset faasintasoiset satunnaistetut kontrolloidut tutkimukset (1980-luku–1990-luku) osoittavat, että suun kautta otettava midatsoli oli tehokas unettomuudessa / uni-häiriöissä, mutta tämä heijastaa tunnettua bentsodiatsipiini-luokan vaikutusta pikemminkin kuin uutta signaalia, eikä yksikään tuoreemmista tai laajamittaisemmista tutkimuksista kohdistu suoraan krooniseen unettomuuteen. Kriittisesti TFDA-pakkausselosteen varoitukset / vasta-aiheet puuttuvat kokonaan (esto, DG001), mikä estää ehdokkaan etenemisen S1 turvallisuuden seulonnasta riippumatta tehokkuustodisteista.

**Jotta voidaan edetä, seuraavaa tarvitaan:**
- TFDA-pakkausselosteen varoitukset, varotoimet ja vasta-aiheet (DG001, esto)
- DrugBank-toimintamekanismin yksityiskohdat (DG002)
- Lääke-lääke-vuorovaikutustiedot (nykyinen DDI-kyselyn tila: not_found)
- Suun kautta otettavan formulaation ja annostelusäännöksen arviointi kroonisen unettomuuden hoitoon sopivaksi, ottaen huomioon midatsoolin lyhyt puoliintumisaika ja kontrolloitavan aineen status
- Paikallisen markkinointiluvan polun analyysi, koska lääkkeellä on tällä hetkellä nolla rekisteröityä lupaa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

