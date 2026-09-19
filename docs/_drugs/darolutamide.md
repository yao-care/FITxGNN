---
layout: default
title: Darolutamide
parent: Pelkkä mallin ennuste (L5)
nav_order: 110
evidence_level: L5
indication_count: 3
---

# Darolutamide
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

# Darolutamide: eturauhassyövästä homotsygootiseen perinnölliseen hyperkolesterolemeiaan

## Yhden lauseen yhteenveto

Darolutamide on androgeeninreseptori (AR) -antagonisti, joka on vakiintuneesti käytössä kastraation kestävään eturauhassyöpään. TxGNN-malli ennustaa, että se voisi olla tehokas **homotsygootiseen perinnölliseen hyperkolesterolemeiaan (HoFH)**, mutta tätä ennustusta tuetaan tällä hetkellä vain **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja mallin omat perustelut osoittavat sen olevan todennäköisesti embedding-samankaltaisuuden artefakti mekanistisesti perustellun hypoteesin sijaan.

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Eturauhassyöpä (kastraation kestävä eturauhassyöpä) — virallista indikaatiotekstiä ei ole saatavilla tässä tietojen noudosta |
| Ennustettu uusi indikaatio | Homotsygootinen perinnöllinen hyperkolesterolemie |
| TxGNN-ennusteen pistemäärä | 99.11% |
| Todistusten taso | L5 |
| Taiwan-markkinoiden asema | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaisia toimintamekanismin tietoja ei ole saatavilla (merkitty kriittiseksi tietovajeen osaksi tässä paketissa). Tunnettujen tietojen perusteella darolutamide on toisen sukupolven androgeeninreseptori-antagonisti, jota käytetään kastraation kestävään eturauhassyöpään; sen teho tuossa yhteydessä on hyvin todistettu, mutta mitään MOA-tietoja ei ole täällä yhdistämään sitä rasva-aineenvaihduntaan.

Homotsygootinen perinnöllinen hyperkolesterolemie on geneettinen sairaus, jonka aiheuttavat LDLR/APOB/PCSK9-puutokset, jotka heikentävät LDL-reseptorin toimintaa ja aiheuttavat äärimmäisen LDL-C-nousun. Tämä on reitti, jolla ei ole tunnettua mekanistista päällekkäisyyttä AR-signaloinnin kanssa. Todisteen paketin omat perustelut ovat selkeitä tässä asiassa: se kuvaa linkin olevan ilman "suoraa tai tunnettua epäsuoraa mekanistista yhteyttä" ja toteaa, että tämä on "ennustus, joka perustuu puhtaasti TxGNN-pisteisiin vahvistavia todisteita."

Toisin sanoen tätä ehdokasta tulisi lukea matalan luottamustason mallin tuotoksena eikä biologisesti motivoituna hypoteesinä. Kaksi muuta ennustettua indikaatiota tässä paketissa (moninaisendokriininen neoplasia, HIV-infektio) osoittavat saman kaavan — uskottavan kuuloisia sairauksien nimiä ilman mekanistista tai empiiristä tukea — mikä viittaa siihen, että järjestysalue, josta nämä ennusteet tulevat (rank ~8,600–9,200), saattaa sijaita TxGNN:n korkean luottamustason alueen ulkopuolella.

---

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Taiwan-markkinoiden tiedot

Darolutamide ei ole tällä hetkellä markkinoilla Taiwanissa (0 lupaa, käytettävissä olevia lisenssitietueita ei ole tässä tietojen noudosta).

---

## Syytoksisyys

| Kohta | Sisältö |
|------|---------|
| Syytoksisyyden luokitus | Kohdennettu hoito — androgeeninreseptori-antagonisti (hormonihoitoinen antineoplastinen aine, ei tavanomainen syytoksinen kemikaalihoito) |
| Ydinrihmaston suppressio -riski | Katso pakettiselosteen varoituksia ja varotoimenpiteitä |
| Pahoinvoinnin aiheuttavuuden luokitus | Katso pakettiselosteen varoituksia ja varotoimenpiteitä |
| Valvottavat tekijät | Katso pakettiselosteen varoituksia ja varotoimenpiteitä |
| Käsittelysuojaus | Katso pakettiselosteen varoituksia ja varotoimenpiteitä |

---

## Turvallisuushuomiot

Turvallisuustiedot löytyvät pakettiselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Ennustetulla indikaatiolla (HoFH) ei ole tukevia kliinisiä tutkimuksia tai kirjallisuutta, eikä sillä ole uskottavasti mekanistista yhteyttä darolutamiden tunnettuun farmakologiaan — todisteen paketti itse kuvailee tämän pisteisiin perustuvaksi artefaktiksi (L5, päätösvaihe S0). Kaksi vaihtoehtoista ehdokasta (moninaisendokriininen neoplasia, HIV-infektio) ovat samoin tuettuja; yksi niistä perustuu yksittäiseen lopetettuun 2 potilaan basket-tutkimukseen, jolla ei ole sairauskohtaista relevanssia.

**Jatkamiseksi tarvitaan seuraavaa:**
- TFDA-pakettiseloste (varoitukset/vasta-aiheet) — tällä hetkellä kriittinen tietovaje
- Vahvistettu toimintamekanismin (MOA) tieto DrugBankista — tällä hetkellä korkean vakavuuden tietovaje
- Vahvistettu alkuperäinen indikaatioteksti (virallinen lähde, ei vain perusteluihin sulautetut maininnat)
- Kaikki prekliiniset tai mekanistiset perustelut, jotka yhdistävät AR-antagonismin rasva-aineenvaihduntaan, ennen kuin tätä ehdokasta voidaan harkita uudelleen S0:n yläpuolella

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

