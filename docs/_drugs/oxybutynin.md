---
layout: default
title: Oxybutynin
parent: Pelkkä mallin ennuste (L5)
nav_order: 277
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynin: määrittelemättömästä alkuperäisestä indikaatiosta Levottomien jalkojen oireyhtymään

## Yhden lauseen yhteenveto

> Oxybutynin (DrugBank DB01062) on antimuskariininen/antispasmodinen aine; sen alkuperäinen hyväksytty indikaatio ei ole dokumentoitu nykyisessä todistusaineistopakkauksessa.
> TxGNN-malli ennustaa, että se voi olla tehokas **levottomien jalkojen oireyhtymään**,
> mutta **kliinisiä tutkimuksia ei ole** ja **kirjallisuutta ei ole** tukevia — kyseessä on **puhtaasti algoritminen ennustus**.

---

## Pikaluettelo

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei dokumentoitu tässä todistusaineistopakkauksessa |
| Ennustettu uusi indikaatio | Levottomien jalkojen oireyhtymä |
| TxGNN-ennusteen pistemäärä | 99.74% (mallin sijaluku 3291) |
| Todistusaste | L5 |
| Suomen markkina-asema | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennustus on järkevä?

Yksityiskohtaiset lääkkeen vaikutusmekanismin tiedot eivät ole saatavilla tässä todistusaineistopakkauksessa, ja alkuperäinen indikaatio ei ole kirjattu, joten lääkkeen vakiintunutta farmakologiaa ei voida vertailla täällä. Yleisen DrugBank-luokituksen perusteella oxybutynin tunnetaan muskulaarisena antispasmodiinina, jolla on kohtalainen antimuskariininen (M3-hallitseva) aktiivisuus.

Mallin omien mekaanisten arvioiden mukaan levottomien jalkojen oireyhtymää ohjaa ensisijaisesti dopaminergisen järjestelmän toimintahäiriö ja raudan aineenvaihdunnan häiriöt — reiteille, joilla **ei ole tunnettu yhteyttä** oxybutyninin antikolinergiseen/sileiden lihasten rentoutumis-mekanismiin. Mitään uskottavaa mekaanista hypoteesia, joka yhdistäisi nämä kaksi, ei ole, ja oxybutyninin ja RLS:n välillä ei ole yhtään kliinistä tutkimusta tai julkaisua.

Lyhyesti sanottuna, tämä ennustus perustuu kokonaan TxGNN-mallin tilastolliseen assosiaatiotulokseen ilman mekaanista, kliinistä tai kirjallisuuden tukea tällä hetkellä.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä liittyviä kliinisiä tutkimuksia

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta

---

## Suomen markkina-asematiedot

Oxybutynin ei ole tällä hetkellä markkinoilla Suomessa tässä todistusaineistopakkauksessa (0 hyväksyntää kirjattu).

---

## Muut arvioidut ennustetut indikaatiot

Tämä todistusaineistopakka ("multi" ehdokas) arvioi kahta muuta TxGNN-ennustusta levottomien jalkojen oireyhtymän lisäksi, molemmat myös odotta-statuksessa:

| Sijaluku | Sairaus | TxGNN-pistemäärä | Todistusaste | Huomautukset |
|----------|---------|-----------------|--------------|-------------|
| 2 | Gastroduodeniitti | 99.62% | L5 | Ei kliinisiä tutkimuksia tai kirjallisuutta; perustelut perustuvat ainoastaan yleiseen antispasmodiseen vaikutukseen GI-sileiden lihasten tasolla |
| 3 | Mahahaavauma | 99.31% | L4 | 3 vanhempaa julkaisua (1964–1990) löytyi; yksi ([PMID 2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/)) kuvailee oxybutyninin **aiheuttavan** refluksiesofagiitin alentamalla alaosillisen ruokatorven sulkijakalvon tonusta — signaali, joka toimii *tätä* indikaatiota vastaan pikemminkin kuin sitä tukee. Nykyaikainen mahahaavauman patologia (H. pylori, NSAIDs) ei ole oxybutyninin antimuskariinisen mekanismin kattama |

Mikään näistä kolmesta ehdokkaasta ei ylitä odottamisen tasoa.

---

## Turvallisuushuomiot

Katso turvallisuustietoja varten pakkaussisältöä.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Korkein sijaluettelossa oleva ennustus (levottomat jalat) ei ole mekaanisesti uskottava, sillä ei ole kliinisiä tutkimuksia, eikä kirjallisuuden tukea (L5/S0). Kaksi seuraavaa ehdokasta ovat samoin tuettamattomat tai sisältävät vastakkaisen turvallisuussignaalin (refluksiesofagitis-riski mainittu mahahaavauman reitille). Lääkettä ei myöskään markkinoida tällä hetkellä Suomessa.

**Jotta voitaisiin edetä, seuraavaa tarvitaan:**
- Fimea/TFDA pakkaussisältö (varoitukset, vasta-aiheet) — tällä hetkellä estää turvallisuusarvion
- Vahvistettu lääkkeen vaikutusmekanismi (MOA) tiedot DrugBankista
- Vahvistettu alkuperäinen hyväksytty indikaatio/indikaatiot lääkkeelle
- Mekaaninen tai prekliininen perusteluja, jotka yhdistävät oxybutyninin levottomien jalkojen oireyhtymään, ennen kuin lisäarviointi on perusteltu

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

