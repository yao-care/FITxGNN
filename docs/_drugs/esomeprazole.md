---
layout: default
title: Esomeprazole
parent: Kohtalainen näyttö (L3-L4)
nav_order: 155
evidence_level: L4
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **3** kpl
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

# Esomeprazoli: Happoon liittyvistä ruoansulatuskanavan häiriöistä duodenomahaisen refluksiin

## Yhden lauseen yhteenveto

Esomeprazoli on protonienpumpun estäjä (PPI), omeprazoolin S-isomeeri, joka on vakiintuneesti käytössä happoperäisten ruoansulatuskanavan häiriöiden, kuten mahahaavan, H. pylori -infektio, refluksitaudin ja NSAID:n aiheuttamien ruoansulatuskanavan vaurioiden hoitoon. TxGNN-malli ennustaa, että se saattaa olla tehokas **duodenomahaisen refluksiin**, mutta tämä suunta on tällä hetkellä tuettu vain **yhdellä yleisellä katsausartikkelilla** eikä **sairauspesifisillä kliinisillä tutkimuksilla**.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla — tiedostoissa ei ole markkinoilta johtuvaa hyväksyntää tai hyväksyttyä indikaatiota tälle rekisterille |
| Ennustettu uusi indikaatio | Duodenomahainen refluksi |
| TxGNN-ennustepisteet | 99.53% |
| Näyttötaso | L4 |
| Suomen markkinoiden status | ✗ Ei markkinoilla |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on järkevä?

Yksityiskohtaisia vaikutusmekanismin tietoja ei ole tällä hetkellä saatavilla (Tiedon puute). Tämän todistepaketin tukevan kirjallisuuden perusteella esomeprazoli kuuluu protonienpumpun estäjien (PPI) luokkaan, joka palautumattomasti estää mahakalvon parietaalisolulta H+/K+-ATPaasin happon erittymisen estämiseksi; sen tehokkuus happoon liittyvien häiriöiden (mahahaava, H. pylori -infektio, refluksitauti, NSAID:n aiheuttamat ruoansulatuskanavan vauriot, Zollinger-Ellison -oireyhtymä) hoidossa on hyvin vakiintunut.

Kuitenkin mekanistinen yhteys duodenomahaisen refluksiin on nimenomaisesti arvioitu heikoksi tässä todistepaketeissa. Duodenomahainen refluksi johtuu ensisijaisesti sapen ja haiman entsyymin refluksista mahaansa — ei-happaman/emäksisen vauriomekanismin. Esomeprazoli vain estää mahahapon erittymisen, eikä sillä ole suoraa farmakologista vaikutusta sapen refluksiin itseensä; se voi enintään epäsuorasti helpottaa limakalvon vaurioiden hapanta komponenttia sekavaikuttavan tyyppisten refluksien yhteydessä. Korkea TxGNN-pistemäärä tulisi siten tulkita epäsuoraksi päätelmäksi lääkkeen laajemmasta happo-esto-profiilista, ei todisteiksi suorasta terapeuttisesta kohteesta.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|------|--------|--------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Katsaus | European Journal of Clinical Pharmacology | Yleinen päivitys PPI:n kliinisestä käytöstä (mahahaava, H. pylori -infektio, refluksitauti, NSAID:n aiheuttamat ruoansulatuskanavan vauriot, Zollinger-Ellison -oireyhtymä); ei kohdista spesifisesti duodenomahaisen refluksiin |

## Suomen markkinoiden tiedot

Tiedostoissa ei ole markkinoilta johtuvaa hyväksyntää — tämä lääke ei ole tällä hetkellä markkinoilla tämän rekisterin mukaisesti (0 hyväksyntää).

## Turvallisuushuomiot

Katso pakkausselosteesta turvallisuustiedot.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelu:**
TxGNN-ennustepiste on korkea, mutta mekanistinen yhteys duodenomahaisen refluksiin on epäsuora (happo-esto vs. sapesta peräisin oleva vaurio), ja todistepohja koostuu yhdestä yleisestä PPI-katsauksesta ilman sairauspesifisiä kliinisiä tutkimuksia — näyttötaso L4 ei täytä kynnystä edetä.

**Jatkaakseen tarvitaan seuraavaa:**
- Vahvistettu alkuperäinen indikaatio ja vaikutusmekanismin tiedot (tällä hetkellä tiedon puute, estää S1-turvallisuuden esiarviointia)
- TFDA/sääntelyinen pakkausseloste (varoitukset, vasta-aiheet, DDI)
- Prekliiniset tai mekanistiset tutkimukset, jotka erityisesti käsittelevät sapen/emäksisen refluksien modulaatiota
- Sairauspesifinen kliininen näyttö duodenomahaisen refluksiin ennen uudelleenpisteyttämistä

**Huomautus muista tämän todistepaketin ehdokkaista:** Sijoitus 3 ("duodenaalinen haava") osoittaa paljon vahvempaa näyttöä (L1, 50 tutkimusta, 20 julkaisua), mutta sen oma perustelu osoittaa, että tämä on esomeprazoolin hyvin vakiintuneet, jo hyväksytyt PPI-indikaatiot pikemminkin kuin aito uudelleenkäytön ehdokas — tyhjä `original_indications`-kenttä on sinänsä tiedon puute, ei todiste uutuudesta. Sijoitus 2 ("duodenaalinen obstrukstio") ei ole tukevia tutkimuksia tai kirjallisuutta ja heijastaa mekanistista epäsopimattomuutta (rakenteellinen obstrukstio vs. farmakologinen happo-esto); sen tulee pysyä Pidätä-tilassa.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

