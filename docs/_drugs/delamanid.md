---
layout: default
title: Delamanid
parent: Vahva näyttö (L1-L2)
nav_order: 136
evidence_level: L2
indication_count: 7
---

# Delamanid
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **7** kpl
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

# Delamanidi: monilääkeresistentin tuberkuloosin hoidosta inaktiiviseen tuberkuloosiin

## Yhden lauseen yhteenveto

Delamanidi on tuberkuloosilääke, jota on käytetty monilääkeresistentin tuberkuloosin (MDR-TB) hoitoon.
TxGNN-malli ennustaa sen voivan tehota **inaktiiviseen tuberkuloosiin**, mutta ennuste perustuu pääosin tautiluokituksen läheisyyteen.
Aineistossa on **1 kliininen tutkimus** (aktiivisen keuhkotuberkuloosin hoito) ja **19 julkaisua** (pääosin yleiskatsauksia), joten näyttö on vain suuntaa-antavaa.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Monilääkeresistentti tuberkuloosi |
| Ennustettu uusi käyttöaihe | Inaktiivinen tuberkuloosi (ennustettu uusi käyttöaihe, jolla vahvin näyttö; TxGNN:n korkeimmin pisteyttämä on naudan tuberkuloosi) |
| TxGNN-ennustepisteet | 99,91 % |
| Näytön taso | L2 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) – tutkimuskysymys, jota on selvitettävä lisää |

Huomautus: ennustelistan sijalla 1 on naudan tuberkuloosi (pisteet 99,91 %, näytön taso L4, suositus Hold). Tässä raportissa tarkastellaan tarkemmin inaktiivista tuberkuloosia, koska sille on ainoa kliininen tutkimus.

---

## Miksi ennuste on järkevä?

Yksityiskohtaista vaikutusmekanismitietoa ei ole tässä aineistossa saatavilla. Tunnetun tiedon perusteella delamanidi on nitroimidatsooliryhmän tuberkuloosilääke, joka estää mykolihappojen synteesiä *Mycobacterium tuberculosis* -bakteerin soluseinässä sen jälkeen, kun Ddn-entsyymi on aktivoinut lääkkeen.

Alkuperäinen käyttöaihe (MDR-TB) ja ennustettu uusi käyttöaihe kuuluvat samaan tautiperheeseen, ja taustalla on sama bakteerikompleksi. Siksi vaikutus on biologisesti uskottava. Aineiston mukaan "inaktiivinen tuberkuloosi" on kuitenkin todennäköisesti TxGNN:n tautiluokituksen kuvaus tuberkuloosiperheelle. Nykynäyttö tukee lähinnä aktiivista lääkeresistenttiä tuberkuloosia. Latentin tuberkuloosi-infektion hoito vaatisi erillistä näyttöä (esimerkiksi delamanidin ja isoniatsidin vertailu MDR-TB-altistuneilla), jota ei ole mukana aineistossa.

Muiden ennustettujen käyttöaiheiden osalta mekanismin yhteys vaihtelee:
- **Naudan tuberkuloosi** (*M. bovis*): kuuluu samaan bakteerikompleksiin, joten vaikutus on uskottava, mutta delamanidille ei ole herkkyys- tai kliinistä dataa.
- **Lintutuberkuloosi** (*M. avium*): bakteerilta puuttuu delamanidin tarvitsema Ddn-aktivaatioreitti, ja teho tuberkuloosia aiheuttamattomiin mykobakteereihin on rajallinen. Korkea pistemäärä heijastaa todennäköisesti tautiluokituksen läheisyyttä.
- **Tuberkuloomi**: mekanismi on periaatteessa uskottava, mutta delamanidin pääsy keskushermostoon on rajallinen ja epävarma.
- **Tuberkuloottinen askites** ja **ihotuberkuloosi**: mekanismi on uskottava laajennuksena hyväksytystä käytöstä, mutta suoraa näyttöä ei ole.
- **Allerginen urtikaria** (nokkosihottuma): uskottavaa mekanistista yhteyttä ei ole, todennäköisesti kyseessä on vääräpositiivinen ennuste.

---

## Kliininen tutkimusnäyttö

Inaktiiviselle tuberkuloosille:

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Vaihe 2/3 (CRUSH-TB) | Aktiivinen, ei rekrytoi | 288 | Selvitetään, ovatko 17 viikon lyhytkuurihoito-ohjelmat (bedakiliini, moksifloksasiini, pyratsiinamidi sekä joko rifabutiini tai delamanidi) yhtä tehokkaita kuin tavanomainen kuuden kuukauden hoito keuhkotuberkuloosissa. Tutkimus koskee aktiivista tautia, ei latenttia tai inaktiivista. |

Muille ennustetuille käyttöaiheille ei ole rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Inaktiiviselle tuberkuloosille (valikoima aineiston julkaisuista, ei yhtään satunnaistettua kontrolloitua tutkimusta):

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Katsaus | Pathogens | Lasten lääkeresistentin tuberkuloosin hoito; uudet lääkkeet, kuten bedakiliini ja delamanidi, ovat helpottaneet turvallisten hoito-ohjelmien suunnittelua |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Katsaus | Lancet Infect Dis | Uudet lääkkeet, lyhyemmät hoito-ohjelmat ja isäntään kohdistuvat hoidot tuberkuloosissa |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Katsaus | Clin Pharmacol Ther | Tuberkuloosin hoito, latentin ja aktiivisen taudin hoidon erot |
| [33319660](https://pubmed.ncbi.nlm.nih.gov/33319660/) | 2021 | Katsaus | Curr Top Med Chem | Patofysiologia, lääkeresistenssin mekanismit, uudet tuberkuloosilääkkeet ja hoito-ohjelmat |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Katsaus | Int J Mol Sci | Tuberkuloosin patogeneesi, nykyiset hoito-ohjelmat ja uudet lääkekohteet |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Katsaus | Zhejiang Da Xue Xue Bao Yi Xue Ban | Latentin tuberkuloosi-infektion diagnostiikan ja hoidon edistysaskeleet |
| [41696339](https://pubmed.ncbi.nlm.nih.gov/41696339/) | 2026 | Prekliininen | ACS Omega | Uudet akiraaliset 4-nitroimidatsoliyhdisteet, joilla on tuberkuloosia vastaan vaikutusta; delamanidi ja pretomanidi on hyväksytty tuberkuloosin hoitoon |

Muiden ennustettujen käyttöaiheiden kirjallisuus:
- Naudan tuberkuloosi: [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) (2024, BMC Genomics) on *M. bovis* -kantojen genomiepidemiologinen tutkimus, ei hoitotutkimus.
- Tuberkuloomi: [33400226](https://pubmed.ncbi.nlm.nih.gov/33400226/) (2021, Acta Neurol Belg) on yleinen neurotuberkuloosikatsaus.
- Ihotuberkuloosi: [31173430](https://pubmed.ncbi.nlm.nih.gov/31173430/) (2019) ja [42469976](https://pubmed.ncbi.nlm.nih.gov/42469976/) (2026) koskevat tuberkuloosilääkkeiden ihohaittavaikutuksia, eivät ihotuberkuloosin hoitoa.
- Allerginen urtikaria: [38800261](https://pubmed.ncbi.nlm.nih.gov/38800261/) (2024) on tapausselostus piperasilliini-tatsobaktaamin aiheuttamasta urtikariasta, eikä liity delamanidiin.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002552 | Deltyba | – | Monilääkeresistentti tuberkuloosi (tila: peruutettu) |

---

## Sytotoksisuus

Delamanidi on antibakteerinen tuberkuloosilääke, ei syöpälääke, joten sytotoksisuusosio ei koske sitä.

---

## Turvallisuusnäkökohdat

Turvallisuustietoja ei ole tässä aineistossa saatavilla. Tutustu valmisteyhteenvetoon turvallisuustietojen osalta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteen pisteet ovat korkeat (yli 99 %), mutta ne heijastavat pääosin tautiluokituksen läheisyyttä. Ainoa kliininen tutkimus koskee aktiivista keuhkotuberkuloosia, ei inaktiivista tai latenttia tautia, ja kirjallisuus koostuu pääosin yleiskatsauksista. Lisäksi delamanidin myyntilupa Suomessa on peruutettu, eikä turvallisuustietoja ole käytettävissä.

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvittäminen (Fimean sivusto), mikä on estävä puute turvallisuusarvioinnissa
- Vaikutusmekanismitietojen täydentäminen DrugBankista
- Latentin tuberkuloosi-infektion hoitoa koskevan näytön hankkiminen (esim. delamanidin ja isoniatsidin vertailu MDR-TB-altistuneilla)
- Delamanidin herkkyys- ja kliinisen datan selvittäminen naudan tuberkuloosille
- Myyntiluvan peruutuksen syyn ja nykyisen saatavuuden selvittäminen Suomessa
- Allergisen urtikarian, lintutuberkuloosin ja tuberkuloottisen askiteksen ennusteet voidaan jättää pois, sillä niille ei ole uskottavaa mekanismia tai näyttöä
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

