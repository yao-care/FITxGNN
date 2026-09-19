---
layout: default
title: Ipilimumab
parent: Vahva näyttö (L1-L2)
nav_order: 204
evidence_level: L2
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **2** kpl
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

# Ipilimumab: ihoisen melanooman ei-ihoisen muodon potentiaali

## Yhden lauseen yhteenveto

> Ipilimumab on CTLA-4-immuunitarkastuspiste-estäjä, jolla on vakiintunut käyttöosoitus metastaattisessa melanoomassa (markkinoitu globaalisti nimellä Yervoy).
> TxGNN-malli ennustaa, että se saattaa olla tehokas myös **ei-ihoisen melanooman** (uveaali-, limakalvo-, leptomeningaalisen ja acraalisen alatyyppi) osalta,
> ja sen tueksi on tällä hetkellä saatavilla **50 kliinistä tutkimusta** ja **5 julkaisua**, vaikka useimmat tutkimukset tutkivat melanoomaa laajasti eivätkä erityisesti ei-ihoisia alatyyppi.

*Huomautus: TxGNN-malli merkitsi erillisesti **choroidemiaa** korkeamman pistemäärän saaneeksi kandidaatiksi (pistemäärä 0,99, sijoitus 9029), mutta ilman kliinisiä tutkimuksia tai kirjallisuutta, todisteiden tasolla L5 ja Hold-suositus — sen oman perustelun mukaan ei ole tunnettua biologista yhteyttä CTLA-4-estäjään ja mahdollinen mekanistinen ristiriita (immuunitarkastuspiste-estäjät voivat aiheuttaa silmään liittyviä immuunivasteen sivuvaikutuksia, kuten uveitis). Sitä ei käsitellä tämän raportin ensisijaisena kandidaattina.*

---

## Pikayleiskatsaus

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Metastaattinen melanooma (ipilimumab/Yervoy:n tunnettu julkinen merkintä; ei vahvistettu Suomen lisensointitietojen perusteella — merkintöjä ei tiedostoissa) |
| Ennustettu uusi indikaatio | Ei-ihoinen melanooma |
| TxGNN Ennusteen pistemäärä | 99.02% |
| Todisteiden taso | L2 |
| Suomen markkinatilanne | Ei markkinoitu |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Edistä turvaraioin |

---

## Miksi tämä ennuste on järkevä?

Tällä tietueella on puutteellinen muodollinen vaikutusmekanismi-tieto (DG002). Tunnettujen tietojen ja todistuspaketin oman perustelun perusteella ipilimumab on anti-CTLA-4-monoklonaalinen vasta-aine: se estää CTLA-4-inhibiittorisen tarkastuspiste-reseptorin T-soluissa, vapauttaa jarrut T-solun aktivoinnista ja parantaa anti-tuumori-immuunivasteita. Tämä mekanismi ei ole spesifinen millekään melanooman anatomiselle alkuperälle.

Ei-ihoinen melanooma (uveaali-, limakalvo-, acraalinen ja leptomeningaalinen alatyyppi) on biologisesti erillään ihoisen melanooman mutaatioprofiilin ja ennusteen osalta, mutta CTLA-4-estäjä kohteena olevan immuuniselvitysjärjestelmän taustalla ei ole kudoskohtainen. Koska ipilimumab:in teho melanoomassa laajasti on jo hyvin vakiintunut (mukaan lukien yhdistelmähoidot nivolumab:in kanssa useissa hyväksytyissä ja tutkimuksessa olevissa asetuksissa), mekanistinen laajennus ei-ihoisten alatyypeihin on periaatteellisesti uskottava.

Yksi tärkeä varoitus: syöttöpaketti näyttää `original_indications`-arvona tyhjän ja Suomen `market_status`-arvona "not marketed", mikä on itsessään tietoaukko eikä todiste siitä, että melanooma olisi todella uusi indikaatio tälle lääkkeelle. Ipilimumab (Yervoy) sisältää jo melanooman indikaatiot useissa lainkäyttöalueilla. Tämä ennuste tulisi siksi lukea laajasti tutkitun sairauden jo hyväksytyn alaryhmän laajennukseksi, ei kokonaan uudeksi terapeuttiseksi hypoteesiksi — mikä vaikuttaa siihen, kuinka paljon lisätodisteita todella tarvitaan ennen toimenpidettä.

---

## Kliiniset tutkimukset

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät tulokset |
|---------|------|------|------|---------|
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Phase 3 | Active, not recruiting | 267 | DREAMseq: ipilimumab+nivolumab vs. dabrafenibi+trametinibi:n järjestys BRAF-mutantin edistyneessä melanoomassa; korkean asteen suora todiste ipilimumab-melanooma-mekanismille. |
| [NCT02939300](https://clinicaltrials.gov/study/NCT02939300) | Phase 2 | Completed | 18 | Ipilimumab + nivolumab leptomeningaalisissa melanooman metastaasissä — suoraan relevantti ei-ihoinen/CNS-levinneisyys-väestö. |
| [NCT03645928](https://clinicaltrials.gov/study/NCT03645928) | Phase 2 | Recruiting | 245 | TIL-terapia (lifileusel) yhdessä tarkastuspiste-estäjien kanssa kiinteissä kasvaimissa; ipilimumab apuvälineenä, epäsuora tuki. |
| [NCT04133948](https://clinicaltrials.gov/study/NCT04133948) | Phase 1/2 | Completed | 44 | Neoadjuvantti domatinostat + nivolumab ± ipilimumab Stage III ihoisessa/tuntemattoman alkuperän melanoomassa. |
| [NCT01654692](https://clinicaltrials.gov/study/NCT01654692) | Phase 2 | Completed | 86 | Ipilimumab + fotemustine resektoimattomassa/metastaattisessa melanoomassa; tukeva yhdistelmätieto. |
| [NCT01927419](https://clinicaltrials.gov/study/NCT01927419) | Phase 2 | Completed | 142 | RCT nivolumab + ipilimumab vs. ipilimumab monoterapia käsittelemättömässä resektoimattomassa/metastaattisessa melanoomassa. |
| [NCT01810016](https://clinicaltrials.gov/study/NCT01810016) | Phase 1 | Terminated | 8 | NY-ESO-1-rokote + ipilimumab resektoimattomassa/metastaattisessa melanoomassa; pieni, terminoitu, heikko todiste. |
| [NCT02452294](https://clinicaltrials.gov/study/NCT02452294) | Phase 2 | Unknown | 22 | Buparlisib melanoomassa, jonka aivometastaadit epäonnistuivat aiemmin ipilimumab:issa; ipilimumab on tausta-aine, ei tutkimusaine. |
| [NCT01496807](https://clinicaltrials.gov/study/NCT01496807) | Phase 1 | Completed | 31 | Ipilimumab (Yervoy) + peginterferooni (Sylatron) turvallisuus/siedettävyys Stage IIIB/C/IV melanoomassa. |
| [NCT01940809](https://clinicaltrials.gov/study/NCT01940809) | Phase 1 | Terminated | 15 | Ipilimumab ± dabrafenibi/trametinibi/nivolumab järjestystutkimus BRAF-mutantin metastaattisessa melanoomassa; terminoitu, pieni otanta. |

*Huomautus: haku palautti 50 tutkimusta; paketti arvioi relevanssille vain 10 (1×A, 5×B, 4×C) ja jätti noin 40:n "pending"-arvioita — yllä oleva taulukko luettelee kaikki 10 arvioitua tutkimusta. Yksikään tutkimuksista ei rekrytoi "ei-ihoisen melanooman" kohorttia nimellä; relevanssus päätellään jaetusta mekanismista ja, NCT02939300/NCT02626962-tyyppisissä tutkimuksissa, ei-ihoisten alatyypien (leptomeningaalinen, uveaali) esiintymisestä rekrytoiduissa väestöissä.*

---

## Kirjallisuustodisteet

| PMID | Vuosi | Tyyppi | Julkaisu | Tärkeimmät tulokset |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Kohortti/Laajennettu pääsy | The Medical Journal of Australia | Ipilimumab:in todellisen maailman tehokkuus/siedettävyys ennalta käsitellyissä ihoisissa, **uveaalisissa** ja **limakalvon** melanoomeissa — käsittelee suoraan ei-ihoisia alatyyppi. |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Kohortti | Current Oncology | Retrospektiivinen anti-PD-1-monoterapian vs. anti-PD-1 + ipilimumab:in vertailu ikäryhmittäin edistyneessä melanoomassa. |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Katsaus | Current Cancer Drug Targets | Melanooman adjuvantti-hoitojen katsaus; nimenomaisesti huomautetaan, että vain noin 5 % melanoomeista on ei-ihoista ja käsitellään tutkimusympäristöä 2000–2015. |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Katsaus | Discovery Medicine | Kliininen päivitys anti-PD-1-vasta-aineista yksinään tai yhdessä ipilimumab:in kanssa edistyneessä melanoomassa vakiohoidon etulinjana. |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Tapauskertomus | Cureus | Tapauskertomus melanoomasta peräisin olevasta paksusuolen metastaasista, jonka hoito immuuniterapialla; osoittaa immuunivasteen liittyviä GI-sivuvaikutuksia ipilimumab-sisältävien järjestysten aikana. |

---

## Suomen markkinatiedot

Ipilimumab:in tuotevaltuutuksia ei ole tiedostoissa Suomessa (`total_licenses = 0`, `market_status = Not marketed/not marketed`). Tämä on tietoaukko, ei todiste saatavuudesta, koska ipilimumab (Yervoy) on hyväksytty EU/EEA:ssa laajemmin.

---

## Sytostaattinen vaikutus

Ipilimumab on antineoplastinen aine (käytetään melanooman hoitoon) mutta ei perinteinen sytostaattinen kemoterapia — se on monoklonaalinen vasta-aine immuunitarkastuspiste-estäjä.

| Kohde | Sisältö |
|------|--------|
| Sytostaattisen vaikutuksen luokittelu | Immuuniterapia (anti-CTLA-4-monoklonaalinen vasta-aine) |
| Luuytimen sorkkimisen riski | Matala — immuunitarkastuspiste-estäjät luokkana eivät tyypillisesti aiheuta merkittävää luuytimen sorkkimista, toisin kuin perinteiset sytostaatit |
| Pahoinvointisuus-luokitus | Matala |
| Seurantakohdat | Maksatoiminnon kokeet, kilpirauhasen/endokrinaalisen toiminnon, munuaisten toiminnon ja kliinisen seurannan immuunivasteen sivuvaikutuksille (koliiitti, hepatiitti, dermatitis, endokrinopatiaa) pikemminkin kuin rutiinin sytopenia-seuranta |
| Käsittelysuojaus | Monoklonaalisen vasta-aineen infuusion laitosvaatimukset; ei kuulu sytostaattisen kemoterapian käsittelymääräysten piiriin, mutta paikallisen vaarallisten lääkkeiden politiikan tulee varmistaa |

*Tämä arviointi perustuu CTLA-4-estäjien vakiintuneeseen farmakologisen luokan profiiliin, koska lääkekohtaiset myrkyllisyystiedot eivät palautuneet tähän pakettiin (DG001/DG002).*

---

## Turvallisuusnäkökohdat

Katso tuotetiedotetta turvallisuustiedoista. (Tärkeät varoitukset, vasta-aiheet ja lääkkeiden yhteisvaikutustiedot merkittiin kaikki tietoaukkona tässä paketissa — DG001.)

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Edistä turvaraioin**

**Perustelut:**
CTLA-4-estäjien mekanismi ei ole anatomisesti spesifinen, ja ipilimumab:lla on jo huomattava melanooman kokeilu- ja kirjallisuustuki, mukaan lukien yksi Phase 3 RCT (DREAMseq) ja omistettu näyttö uveaalisen/limakalvon/leptomeningaalisen alatyypeihin (PMID 24999899, NCT02939300). Kuitenkin useimmat 50 tutkimuksesta tutkivat melanoomaa laajasti pikemminkin kuin ei-ihoisia alatyyppi erityisesti, ja tämä kandidaatti on paremmin kehystetty olemassa olevan indikaation alaryhmän laajennukseksi kuin todella uudeksi uudelleenkäyttöhypoteesiksi — näin ollen turvaraioin eikä ehdoton Go.

**Jatkamista varten seuraava on tarpeellista:**
- Virallinen vaikutusmekanismin vahvistus DrugBank:sta (DG002)
- TFDA/Fimea-pakkausseloste varoitukset, vasta-aiheet ja DDI-tiedot (DG001)
- Alaryhmä-stratifioitu teho-näyttö ei-ihoisen melanooman osalta (tällä hetkellä päätelty, ei suoraan ilmoitettu, useimmissa tutkimuksissa)
- Vahvistus todellisesta Suomen/EU-markkinoinnista ja valtuutuksesta, koska "ei markkinoitu" täällä todennäköisesti heijastaa tietoaukkoa pikemminkin kuin todellista saatavuutta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

