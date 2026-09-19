---
layout: default
title: Trastuzumab Emtansine
parent: Kohtalainen näyttö (L3-L4)
nav_order: 389
evidence_level: L4
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **4** kpl
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

# Trastuzumab emtansine: HER2-positiivisesta rintasyövästä normal breast-like -alityyppiin

## Yhden lauseen yhteenveto

Trastuzumab emtansine (T-DM1, kaupallinen nimi Kadcyla) on vasta-aine-lääkekonjugaatti, joka on kansainvälisesti hyväksytty HER2-positiiviseen rintasyöpään.
TxGNN-malli ennustaa, että se saattaa olla tehokas **normal breast-like -alityyppisen rintasyövän** kannalta,
mutta tämä indikaatio on tällä hetkellä tuettu vain **1 kliinisellä tutkimuksella** ja **millään julkaistulla kirjallisuudella**, ja mekanistinen yhteys tähän spesifiin molekyylialityyppiin on heikko.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | HER2-positiivinen (HER2+) rintasyöpä (Kadcyla) |
| Ennustettu uusi indikaatio | Normal breast-like -alityyppi rintasyövässä |
| TxGNN-ennustuspistemäärä | 99.82% |
| Näyttötaso | L4 |
| Suomen markkinoinnin tila | Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennustus on kohtuullinen?

Tällä hetkellä yksityiskohtaisia mekanismin vaikutusta koskevia tietoja ei ole saatavilla DrugBankista. Tunnettujen tietojen perusteella trastuzumab emtansine on vasta-aine-lääkekonjugaatti (ADC), joka yhdistää trastuzumabin – HER2:ta kohdistavaa monoklonaalista vasta-ainetta – DM1:een, maytansinoidiseen mikrotubuli-inhibiittoriin. Sen teho riippuu HER2-yleilektolkaisusta (IHC3+/FISH+) syöpäsoluissa, ja sitä käytetään tällä hetkellä Kadcyla-tuotenimellä HER2-positiivisessa rintasyövässä.

"Normal breast-like" on PAM50-sisäinen molekyylinen alityyppiluokitus, joka määritellään geeni-ekspressio-profilointiin perustuen, ei HER2-reseptorin tilan mukaan. Tämä on eri luokitusakseli kuin HER2-positiivisuus, joka on T-DM1-aktiivisuuden todellinen määräävä tekijä. Todiste-osastojen omaan mekanistiseen arviointiin perustuen, yhteys T-DM1:n ja normal-like -alityypin välillä on "epäsuora ja epäselvä", koska normal-like -kasvaimet eivät ole määritellyt, eivätkä korreloivat luotettavasti HER2-yleilektoinnin kanssa.

Seurauksena on, että vaikka TxGNN-ennustuspistemäärä on erittäin korkea (99.82%), taustalla oleva biologinen perusteltu on heikompi kuin HER2-tilaan perustuvissa ennusteissa. Tämä heijastuu alhaisessa näyttötasossa (L4) ja yksittäisessä tukevassa tutkimuksessa, joka käsittelee laajasti anti-HER2-hoitoa HER2+-rintasyövässä ilman, että se erityisesti vahvistaa T-DM1-kättä tai normal-like -alityypin painopistettä.

## Kliiniset tutkimukset

| Tutkimuksen numero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Vaihe 2 | Rekrytoimassa | 74 | Arvioi anti-HER2-pohjaisen terapian (neoadjuvantti adjuvanttiin) tehokkuutta ja turvallisuutta nigerialaisten naisten HER2+-rintasyövässä; ei vahvista erityisiä T-DM1-kättä tai normal-like -alityypin painopistettä (asiallisuusaste B). |

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta

## Suomen markkinatiedot

Lääke ei ole tällä hetkellä markkinoilla Suomessa (Ei markkinoilla), eikä markkinoinnin hyväksyntätietueita ole saatavilla.

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuuden luokitus | Kohdistettu terapia (vasta-aine-lääkekonjugaatti sytotoksisella maytansinoidisella kuormalla, DM1) |
| Luuydintukahdutusriski | Katso pakkausselosteesta varoitukset ja varotoimet |
| Pahoinvoinnin luokitus | Katso pakkausselosteesta varoitukset ja varotoimet |
| Valvontakohdat | Katso pakkausselosteesta varoitukset ja varotoimet |
| Käsittelysuoja | Katso pakkausselosteesta varoitukset ja varotoimet |

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustiedoista.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Parhaaksi rankattu ennustus (normal breast-like -alityyppi) on erittäin korkea TxGNN-pistemäärä, mutta heikko ja epäsuora mekanistinen perusta, minimaalinen kliinisen tutkimuksen tuki (1 tutkimus, asiallisuusaste B) ja ei tukevaa kirjallisuutta – riittämätön edetä. Huomionarvoista on, että muut ennustetut indikaatiot tälle lääkkeelle (PR-positiivinen ja PR-negatiivinen rintasyöpä) osoittavat paljon vahvempaa näyttöä (L1–L2, monet suorat T-DM1-tutkimukset ja kirjallisuus), mutta suurelta osin päällekkäin lääkkeen olemassa olevan HER2-positiivisen rintasyövän indikaation kanssa eivätkä edusta todellista uudelleentarkoitusta.

**Edetäkseen seuraavat tarvitaan:**
- TFDA/Fimea-pakkausseloste tiedot (varoitukset, vasta-indikaatiot) – tällä hetkellä tietovaje, joka estää etenemisen
- DrugBank-mekanismin vaikutus (MOA) -tiedot mekanistisen asiallisuuden analyysin vahvistamiseksi
- Vahvistus siitä, ovatko T-DM1-tutkimuksissa erityisesti rekrytoitu tai ositetusti PAM50 normal-like -alityypin mukaan
- Lisäkirjallisuushaku erityisesti T-DM1:lle ja normal-like/basaalisten molekyylisten alityyppien osalta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

