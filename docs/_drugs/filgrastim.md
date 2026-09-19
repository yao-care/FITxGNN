---
layout: default
title: Filgrastim
parent: Pelkkä mallin ennuste (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Filgrastim
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Filgrastiimi: Neutropeniasta/kantasolujen mobilisaatiosta trombosyyttien primaarisen vapautumishäiriön hoitoon

## Yhden lauseen yhteenveto

> Filgrastiimi (ihmisen rekombinantti G-CSF) on hematopoieettinen kasvutekijä, jonka vakiintunut kliininen käyttö on kemoterapian aiheuttaman neutropenia-hoito ja perifeerisen veren kantasolujen mobilisaatio ennen keräämistä.
> TxGNN-malli ennustaa, että se saattaa olla tehokas **trombosyyttien primaarisen vapautumishäiriön** hoitoon,
> mutta tukeva näyttö on heikko: 14:stä löydetystä kliinisestä tutkimuksesta useimmat on luokitettu *ei suoraan asiaan liittyviksi* (kohdentamattomat kantasolujen siirtotukimukset), ja vain **1 julkaisu** (havainnollinen kohorttitutkimus, relevanssin arviointi on vielä kesken) käsittelee aihetta.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Neutropenia (kemoterapian aiheuttama) / perifeerisen veren kantasolujen mobilisaatio — *perustuu lääkkeen tunnettuun G-CSF-mekanismiin, joka on kuvattu näyttöpaketin perustelukentässä; ei virallisesti hyväksytty Taiwan-indikaatio (katso Markkinatilanne)* |
| Ennustettu uusi indikaatio | Trombosyyttien primaarinen vapautumishäiriö |
| TxGNN-ennustepisteet | 99.998% (sijoitus 48) |
| Näyttötaso | L4 (mekanistinen/epäsuora vain — yksikään kliininen tutkimus tai tutkielma ei kohdista suoraan tähän indikaatioon) |
| Taiwanin markkinatilanne | Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | **Pidätetään** |

---

## Miksi tämä ennuste on kohtuullinen?

Filgrastiimi on ihmisen rekombinantti granulosyytti-koloniastimulointikerroin (G-CSF). Se vaikuttaa granulosyytin ennakkosoluihin edistääkseen proliferaatiota ja differentiaatiota, ja se mobilisoi hematopoieettisia kantasoluja luuydinnestä perifeerisen veren kiertokulkuun — tämä muodostaa perustan sen vakiintuneille käyttötarkoituksille neutropenia-hoidossa ja kantasolujen keräämisessä siirtoa ennen.

Trombosyyttien primaarinen vapautumishäiriö (δ-varastoinnin sairaus, joka vaikuttaa trombosyytin granulaarisen aineen vapautumiseen) ei ole vakiintunutta farmakologista yhteyttä G-CSF-signalointiin. Näyttöpaketin oma mekanistinen arviointi on tässä asiassa selkeä: "ei tunnettua suoraa farmakologista mekanismia", joka yhdistäisi filgrastiimin trombosyytin granulaarin vapautumistoimintoon. Ainoa asiaan liittyvä julkaisu kuvaa *epäsuoraa havaintoa* — että G-CSF-mobilisaatio terveillä kantasolujen lahjoittajilla vaikuttaa mieluummin lymfosyytin osajoukkoihin — mikä ei ole hoitomekanismin tutkimus trombosyyttien vapautumishäiriöille.

Lyhyesti sanottuna, korkea TxGNN-pistemäärä näyttää olevan semanttisen/graafi-klusteroinnin ohjaamaa "hematopoieettisen" ja "verenvuotohäiriön" käsitteiden ympärillä pikemminkin kuin validoitu farmakologinen polku. Tämä on yhteneväinen mallin muiden filgrastiimin huippiehdokkaiden kanssa (pseudo-von Willebrand-tauti, Glanzmann-trombastenia, Scottin oireyhtymä ja muut), joiden kaikki näyttöpaketti itse merkitsee olevan **ei mekanistista päällekkäisyyttä** G-CSF-signaloinnin kanssa ja **ei tukevaa tutkimus- tai kirjallisuusnäyttöä** (Näyttötaso L5, Pidätetään-suositus jokaisen niistä kohdalla).

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Tärkeimmät löydökset |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Vaihe 2 | Keskeytetty | 200 | Sukulaisella olevan lahjoittajan kantasolujen siirto hematologisten syöpien hoitoon — *ei asiaa* (luokka C: väestö ja päätetapahtumat ovat hematologinen syöpä, ei trombosyyttien vapautumishäiriö) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Vaihe 2 | Valmistunut | 60 | Allogeeninen/syngeeninen kantasolujen siirto lapsuusajan sarkoomeissa — *ei asiaa* (luokka C) |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Vaihe 2 | Keskeytetty | 16 | Napanuoran veren siirto myeloidiin leukemiaan — *ei asiaa* (luokka C) |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Vaihe 2 | Valmistunut | 19 | Vähennetyn intensiteetin kantasolujen siirto GATA2-mutaatioiden potilaille — relevanssia ei ole vielä arvioitu |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Vaihe 2 | Valmistunut | 64 | CD34+ valittu vs valitsematon autologinen siirto lymfoomassa — *ei asiaa* (luokka C) |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Vaihe 1/2 | Rekrytoi | 260 | Siirtojälkeisen syklofosforamidi-doseerauksen GVHD-profylaksia — *ei asiaa* (luokka C) |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Vaihe 1 | Peruutettu | 0 | Kryopreservoidun sukulaisella olevan lahjoittajan luuydin siirto — relevanssia ei ole vielä arvioitu |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Vaihe 2 | Valmistunut | 9 | Autologinen kantasolujen siirto vakavaan lupukseen (SLE) — relevanssia ei ole vielä arvioitu |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Vaihe 2 | Keskeytetty | 49 | Dapansutrilli COVID-19 sytokinien vapautumisen oireyhtymään — relevanssia ei ole vielä arvioitu |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Vaihe 2 | Rekrytoi | 358 | Siirtojälkeisen syklofosforamidi GVHD-profylaksian alustava tutkimus — relevanssia ei ole vielä arvioitu |

*Huomio: 4 muuta tutkimusta palautettiin, mutta jätettiin pois niiden lyhyyden vuoksi; yksikään niistä ei ole luokiteltu suoraan asiaa olevaksi tähän indikaatioon. Kaikissa 14 haetulla tutkimuksella filgrastiimia ei tutkita trombosyyttien vapautumishäiriön hoitona — kaikissa on kyse hematopoieettisten kantasolujen siirrosta liittymättömille hematologisille syöpiin tai autoimmuunitaudeille.*

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Kohortti/Havainnollinen | Frontiers in Immunology | G-CSF-mobilisaatio terveillä kantasolujen lahjoittajilla mobilisoi mieluummin lymfosyytin osajoukkoja; epäsuora immunologinen havainto, ei tutkimus trombosyytin vapautumisen toiminnasta tai hoitotehokkuudesta (relevanssin luokitus on vielä kesken) |

---

## Taiwanin markkinatiedot

Filgrastiimia **ei tällä hetkellä markkinoida Taiwanissa** — näyttöpaketissa ei ole saatavilla hyväksyntätietoja (0 lisenssejä).

---

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustietoja. *(Tärkeimmät varoitukset, vasta-aiheet ja lääkkeiden vuorovaikutustiedot on kaikki merkitty tietojen puutteiksi tässä näyttöpaketissa — myös niin vakavaksi kuin Blocking-vakavuuden TFDA-pakkausseloste, joka estää alustavaa turvallisuuden arviointia.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätetään**

**Perustelut:**
G-CSF-signaloinnin ja trombosyyttien vapautumisen/granulaarin häiriöiden välinen mekanistinen yhteys on vakiintumaton — näyttöpaketin oma perustelu toteaa, ettei ole tunnettua suoraa farmakologiaa, joka yhdistäisi nämä kaksi. Yksikään kliininen tutkimus tai julkaisu ei tutkimus filgrastiimia tähän indikaatioon; haetut tutkimukset ovat lähes kokonaan kohdentamattomia hematopoieettisia kantasolujen siirtotukimuksia, ja ainoa kirjallisuuden osuma on epäsuora havainnollinen löydös. Tämä sama heikko-näytön kuvio (Näyttötaso L5, Pidätetään) koskee kaikkia yhdeksää muuta TxGNN-ennustettua filgrastiimin indikaatiota tässä paketissa (pseudo-von Willebrand-tauti, Glanzmann-trombastenia, Scottin oireyhtymä, C1-inhibiittorin puutos ja muut), joista yksikään ei ole millään tutkimus- tai kirjallisuusnäytöllä.

**Jotta voitaisiin edetä, seuraavaa tarvitaan:**
- TFDA-pakkausseloste varoitukset/vasta-aiheet (Blocking-tietojen puute — vaaditaan ennen kuin mikään S1 turvallisuuden arviointi voidaan aloittaa)
- Toimintamekanismin dokumentaatio (Korkea vakavuuden tietojen puute — vaaditaan mekanistisen uskottavuuden asianmukaiseen arviointiin)
- Omistettu prekliininen tai mekanistinen tutkimus, joka yhdistää suoraan G-CSF/granulosyytin polut trombosyytin granulaarin vapautumisen toimintoon
- Jos sitä jatketaan, hematologian/hyytymisen asiantuntijan arviointi biologisen uskottavuuden osalta ennen mitään tutkimussuunnittelua

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

