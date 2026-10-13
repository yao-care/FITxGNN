---
layout: default
title: Teriflunomide
parent: Vahva näyttö (L1-L2)
nav_order: 431
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **1** kpl
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

# Teriflunomidi: Relapsoivasta-remittoivasta MS-taudista relapsoivaan-remittoivaan MS-tautiin

## Yhden lauseen yhteenveto

Teriflunomidi on suun kautta otettava immuunivastetta muokkaava lääke, jota käytetään alun perin relapsoivan-remittoivan multippeliskleroosin (MS-taudin) hoitoon. TxGNN-malli ennustaa sen tehoavan **relapsoivaan-remittoivaan MS-tautiin**, mikä vastaa lääkkeen alkuperäistä käyttöaihetta eli kyse ei ole varsinaisesta uudelleenkäytöstä. Ennustetta tukee **13 kliinistä tutkimusta** ja **20 julkaisua**, joihin kuuluu useita satunnaistettuja vaiheen 3 tutkimuksia.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Relapsoiva-remittoiva multippeliskleroosi |
| Ennustettu uusi käyttöaihe | Relapsoiva-remittoiva multippeliskleroosi |
| TxGNN-ennustepistemäärä | 99,24 % |
| Näytön taso | L1 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 3 (kaikki peruutettu) |
| Suositeltu päätös | Etene suojatoimin (Proceed with Guardrails) |

---

## Miksi ennuste on perusteltu?

Tälle raporttia varten koottu aineisto ei sisällä yksityiskohtaista vaikutusmekanismitietoa. Tunnetun tiedon perusteella teriflunomidin vaikuttava metaboliitti estää mitokondrion dihydroorotaattidehydrogenaasi-entsyymiä (DHODH). Tämä estää pyrimidiinien de novo -synteesiä ja rajoittaa aktivoituneiden T- ja B-lymfosyyttien lisääntymistä. Tämä mekanismi sopii hyvin autoimmuunivälitteiseen, tulehdukselliseen MS-tautiin.

Koska ennustettu käyttöaihe on sama kuin alkuperäinen, TxGNN-mallin erittäin korkea pistemäärä on johdonmukainen: malli tunnistaa lääkkeen vakiintuneen käytön. Ennuste ei siis tuo uutta terapeuttista suuntaa, vaan vahvistaa tunnetun käyttöaiheen.

Huomionarvoista on, että Suomen markkinatilanne ("vain peruutettuja") heijastaa todennäköisesti yksittäisten valmisteiden myyntilupatilannetta eikä välttämättä vetäytymistä turvallisuus- tai tehosyistä. Tämä tulee varmistaa ajantasaisista viranomaistiedoista.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Vaihe 3 | Päättynyt | 1088 | Satunnaistettu, kaksoissokkoutettu, lumekontrolloitu tutkimus: teriflunomidin vaikutus relapsien esiintyvyyteen ja vammautumisen etenemiseen relapsoivassa MS-taudissa |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Vaihe 3 | Päättynyt | 324 | Teriflunomidi vs. interferoni beeta-1a relapsoivassa MS-taudissa (arvioijasokkoutettu) |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Vaihe 3 | Päättynyt | 742 | Pitkäaikaisjatkotutkimus: teriflunomidin 7 mg ja 14 mg annosten pitkäaikaisturvallisuus |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Vaihe 2 | Päättynyt | 147 | Vaiheen 2 jatkotutkimus: pitkäaikaisturvallisuus ja -teho |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | Ei sovellettavissa | Päättynyt | 106 | Havainnoiva tutkimus teriflunomidin tehosta rutiinihoidossa vähintään kahden vuoden ajan |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | Ei sovellettavissa | Päättynyt | 30 | Mekanistinen tutkimus: säätelijä-B-lymfosyyttien merkitys teriflunomidin vaikutuksessa |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | Ei sovellettavissa | Päättynyt | 24 | Mahdollisten biomarkkereiden yhteys taudin aktiivisuuteen teriflunomidihoidossa |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Vaihe 3 | Päättynyt | 185 | Ofatumumabi vs. ensilinjan MS-lääkkeet vastikään diagnosoiduilla; teriflunomidi epäsuorasti vertailuryhmässä |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Vaihe 4 | Aktiivinen, ei rekrytoi | 800 | Varhaisen tehokkaan hoidon ja porrastetun hoidon vertailu; epäsuora yhteys |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | Ei sovellettavissa | Päättynyt | 900 | Pragmaattinen tutkimus varhaisesta aggressiivisesta vs. porrastetusta hoidosta; epäsuora yhteys |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | Ofatumumabi vs. teriflunomidi MS-taudissa |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | Ublituksimabi vs. teriflunomidi relapsoivassa MS-taudissa |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Tolebrutinibi vs. teriflunomidi relapsoivassa MS-taudissa |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurol | Evobrutinibi vs. teriflunomidi (evolutionRMS1 ja 2, vaihe 3) |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurol | Ponesimodi vs. teriflunomidi (OPTIMUM, vaihe 3) |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Verkostometa-analyysi | Cochrane Database Syst Rev | Immuunivastetta muokkaavien ja immunosuppressiivisten lääkkeiden vertailu RRMS:ssä |
| [38032059](https://pubmed.ncbi.nlm.nih.gov/38032059/) | 2023 | Verkostometa-analyysi | Cochrane Database Syst Rev | MS-taudin immunoterapioiden haittavaikutukset |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Katsaus | Drugs | Teriflunomidi RRMS:ssä: DHODH:n esto, satunnaistettujen tutkimusten ja tosielämän näytön perusteella tehokas ja yleensä hyvin siedetty |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Katsaus | CNS Drugs | EU:n valmisteyhteenvedon tärkeimmät teho- ja turvallisuustulokset |
| [37578431](https://pubmed.ncbi.nlm.nih.gov/37578431/) | 2023 | Havainnoiva | Eur J Neurol | Dimetyylifumaraatin ja teriflunomidin tosielämän vertailu RRMS:ssä |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005962 | Teriflunomide Viatris (aiemmin Teriflunomide Mylan) | – | Relapsoiva-remittoiva multippeliskleroosi (peruutettu) |
| EMEA/H/C/005960 | Teriflunomide Accord | – | Relapsoiva-remittoiva multippeliskleroosi (peruutettu) |
| EMEA/H/C/002514 | Aubagio | – | Multippeliskleroosi (peruutettu) |

---

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Tietokannassa on 100 yhteisvaikutusta. Merkittäviksi (Major) luokiteltuja ovat mm. asetyylisalisyylihappo, deksametasoni, hydrokortisoni, triamsinoloni, betametasoni, budesonidi, klaritromysiini, minosykliini, bupropioni, pioglitatsoni, akarboosi, kenodeoksikoolihappo, oksandrolonI ja oksimetoloni. Kohtalaisia (Moderate) ovat mm. alosetroni, simetidiini, empagliflotsiini ja sitagliptiini.

Varoitusten ja vasta-aiheiden osalta katso valmisteyhteenveto.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Etene suojatoimin (Proceed with Guardrails)**

**Perustelut:**
- Teriflunomidin teho relapsoivassa MS-taudissa on osoitettu useissa satunnaistetuissa vaiheen 3 tutkimuksissa (mm. lumekontrolloitu tutkimus, n=1088, ja interferonivertailu), joten näytön taso on L1. Lääke on kuitenkin jo alun perin tähän käyttöaiheeseen hyväksytty, ja Suomen myyntilupatilanne on epäselvä (kaikki myyntiluvat peruutettu).

**Jatkotoimiin tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kokoaminen (tämä on estävä tietoaukko, joka tulee ratkaista ennen turvallisuusarviointia)
- Yksityiskohtaiset vaikutusmekanismitiedot DrugBankista
- Suomen myyntilupatilanteen varmistaminen ajantasaisista viranomaisrekistereistä (peruutuksen syyt)
- Yhteisvaikutusten kliinisen merkityksen arviointi, erityisesti kortikosteroidien ja muiden Major-tason yhteisvaikutusten osalta
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

