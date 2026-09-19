---
layout: default
title: Decitabine
parent: Pelkkä mallin ennuste (L5)
nav_order: 113
evidence_level: L5
indication_count: 1
---

# Decitabine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

# Decitabine: Myelodysplastisesta oireyhtymästä lapsuuden refraktooriin sytopeniaan

> **Huomautus alkuperäisestä indikaatiosta**: Näyttöpaketti ei sisällä decitabinen `original_indications`, `original_moa` tai Suomen lisensointitietoja (lääkettä ei ole markkinoilla Suomessa, 0 valtuutusta). Alla esitetty alkuperäisen indikaation konteksti (MDS/AML, DNA-hypometylointiaine) kuvastaa decitabinen kansainvälistä hyväksyttyä identiteettiä, ei näyttöpaketin tarkasteltua kenttää – tämä on flagattu tässä avoimuuden vuoksi eikä esitetä vahvistettuina tietona.

## Yhden lauseen yhteenveto

Decitabine on DNA-hypometylointiaine, jota käytetään kansainvälisesti aikuisten myelodysplastisen oireyhtymän (MDS) ja akuutin myelooisen leukemian hoidossa, mutta sitä ei markkinoida Suomessa eikä TFDA/paikallisia pakkausseloste-turvallisuustietoja ole saatavilla. TxGNN-malli ennustaa, että se saattaa olla tehokas **lapsuuden refraktoorissa sytopeniassa** (pediatrinen MDS-alatyyppi), TxGNN-pistemäärällä **99.03%**, tuettuna tällä hetkellä **0 kliinisellä tutkimuksella** ja **1 julkaisulla**.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei vahvistettu näyttöpaketissa (lisensointitietoa ei löydy); decitabine tunnetaan kansainvälisesti MDS/AML-hypometylointiaineen |
| Ennustettu uusi indikaatio | Lapsuuden refaktorinen sytopenia |
| TxGNN-ennustepisteet | 99.03% |
| Näyttötaso | L3 (yksi takautuva observationaalinen tutkimus, ei RCT:itä) |
| Suomen markkinatilanne | Ei markkinoilla |
| Valtuutusten määrä | 0 |
| Suositeltu päätös | Pidätetään |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla näyttöpaketissa (flagattu tietovajeeksi DG002). Yleisesti tunnetun farmakologian perusteella decitabine on DNA-metyylitransferaasi-inhibiittori (hypometylointiaine), jonka teho aikuisten myelodysplastisen oireyhtymän ja AML:n hoidossa on kansainvälisesti hyvin vahvistettu, vaikka tätä ei ole itsenäisesti vahvistettu tämän lääkkeen näyttöpaketin lähteistä.

Lapsuuden refaktorinen sytopenia on luokiteltu myelodysplastisen oireyhtymän pediatriseksi alatyypiksi, jolla on sama taustalla oleva klonaalinen luuydinpatologia kuin aikuisten MDS:ssä. Mekanistisesti hypometylointiaine, joka on tehokas aikuisten MDS:ssä, odotettaisiin olevan biologisesti perusteltu pediatrisessa MDS-variantissa, mikä on johdonmukainen TxGNN-ennusteen suunnan kanssa.

Tätä mekanistista perustelua tukee edelleen yksi saatavilla oleva kirjallisuusrekisteri: yksittäisen keskuksen takautuva tutkimus decitabinin yhdistelmästä minimaalisen myelosuppressiivisen regimen kanssa (DAC + MMR), käytetty siltana allogeniseen kantasolun siirtämiseen pediatrisissa MDS-potilaissa – kliininen populaatio, joka osittain vastaa lapsuuden refaktorista sytopeniaa.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|--------|--------|--------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Takautuva kohorttitutkimus | BMC Pediatrics | Yksittäisen keskuksen 10 vuoden kokemus decitabinin käytöstä minimaalisen myelosuppressiivisen regimen kanssa (DAC + MMR) siltana allogeniseen kantasolun siirtämiseen pediatrisissa MDS-potilaissa; raportointi tämän lähestymistavan tuloksista ennen siirtämistä. |

## Suomen markkinatiedot

Decitabine ei ole tällä hetkellä markkinoilla Suomessa; valtuutusten rekisteritietoja ei ole saatavilla.

## Sytotoksisyys

Decitabine on antineoplastinen aine (DNA-hypometylointiaine / antimetaboliittiluokka), joten tämä osio koskee.

| Kohta | Sisältö |
|---------|---------|
| Sytotoksisyysluokitus | Perinteinen sytostaattinen aine (hypometylointiaine / antimetaboliittiluokka) |
| Luuytimen suppressio -riski | Katso pakkausseloste varoituksista ja varotoimista |
| Pahoinvoinnintuottavuusluokitus | Katso pakkausseloste varoituksista ja varotoimista |
| Seurantakohdat | Katso pakkausseloste varoituksista ja varotoimista |
| Käsittelyn suojaus | Katso pakkausseloste varoituksista ja varotoimista |

## Turvallisuusnäkökulmat

Katso pakkausseloste turvallisuustiedoista. (TFDA/paikallisen pakkausselosteen tietoja ei ole tällä hetkellä saatavilla – flagattu **esteenä olevaksi** tietovajeeksi, DG001, joka estää S1-turvallisuuden esiarviointiksi.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätetään**

**Perustelut:**
Korkea TxGNN-pistemäärä on tuettu vain yhdellä observationaalisella (ei-RCT) julkaisulla ja nollalla rekisteröidyillä kliinisillä tutkimuksilla tälle erityiselle indikaatiolle, ja esteenä oleva turvallisuuden tietovahe (pakkausseloste varoituksia/vasta-aiheita ei saatavilla) estää tällä hetkellä jopa S1-turvallisuusarvioinnin.

**Jatkaakseen tarvitaan seuraavaa:**
- TFDA/paikallisen pakkausselosteen varoitukset ja vasta-aiheet (ratkaisee DG001, esteenä oleva)
- Vahvistettu vaikutusmekanismin tieto DrugBankista (ratkaisee DG002)
- Decitabinen alkuperäisten hyväksyttyjen indikaatioiden ja lisensointitilan vahvistaminen säätelijän tietokannasta
- Kaikki muut kliiniset tutkimukset tai kontrolloidut tutkimukset, jotka arvioivat decitabineä erityisesti lapsuuden refaktorisessa sytopeniassa / pediatrisessa MDS:ssä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

