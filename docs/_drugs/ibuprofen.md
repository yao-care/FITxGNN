---
layout: default
title: Ibuprofen
parent: Pelkkä mallin ennuste (L5)
nav_order: 185
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **7** kpl
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

# Ibuprofeiini: dokumentoimattomasta alkuperäisestä indikaatiosta akromesomeelisen dysplasian, Hunter-Thompson-tyypin, hoitoon

## Yhden lauseen yhteenveto

Ibuprofeiinin alkuperäinen indikaatio ja vaikutusmekanismi eivät olleet hankittavissa saatavilla olevista sääntelylähteistä tälle ehdokkaalle. TxGNN-mallin pääennuste on **akromesomeelinen dysplasia, Hunter-Thompson-tyyppi**, harvinainen GDF5-liittyvä luurankoston dysplasia, mutta **kliinisiä tutkimuksia eikä kirjallisuusviitteitä** ole tällä hetkellä tämän suunnan tueksi, eikä lääkettä ole markkinoilla Suomessa.

## Pikakatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei kirjattu saatavilla oleviin sääntelyaineistoihin |
| Ennustettu uusi indikaatio | Akromesomeelinen dysplasia, Hunter-Thompson-tyyppi |
| TxGNN-ennuste-pistemäärä | 99.74% |
| Näytön taso | L5 |
| Suomen markkinatilanne | Ei markkinoilla |
| Lupien määrä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla ibuprofeiinille tässä näyttöpakkauksessa. Yleisen farmakologisen tiedon perusteella ibuprofeiini on ei-selektiivinen COX-1/COX-2-inhibiittori, jolla on analgeettinen ja tulehduksensuppressiva vaikutus, mutta tämä ei vahvistunut tämän ehdokkaan taustalla olevan DrugBank-kyselyn kautta.

Akromesomeelinen dysplasia, Hunter-Thompson-tyyppi on harvinainen luurankoston dysplasia, jonka aiheuttavat *GDF5*-mutaatiot, jotka vaikuttavat endokondraaaliseen osifikaatioon — väylä, joka ei liity prostaglandiinien synteesiin tai COX-inhibitioon. Näyttöpaketin oma mekanistinen arviointi toteaa, että **ei ole tunnettua mekanistista yhteyttä** ibuprofeiinin ja GDF5/BMP-signaloinnin väylän välillä, ja ehdottaa, että korkea TxGNN-pistemäärä todennäköisesti heijastaa opittua assosiaatiota nivel-oireisiin liittyvän yhteisesiintyvyyden kanssa (esim. nivelrikkotyyppiset kivut, jotka ovat yleisiä luurankoston dysplasioissa) pikemminkin kuin todellista sairauden muovaavaa mekanismia.

Kuusi jäljellä olevaa ennustettua indikaatiota (brakioolmia-amelogeneesin epätäydellisyys -syndrooma, myoskleroosi, brakioolmia, brakydaktylia-syndaktylia-syndrooma, pseudoakondroplaasia ja kolobamaattinen mikroftalmia-risomeelinen dysplasia-syndrooma) osoittavat saman kaavan: TxGNN-pistemäärät yli 99%, mutta jokainen perusteltu nimenomaan huomauttaa puuttuvasta tai puhtaasti oireista (ei sairauden muovaavasta) mekanistisesta perusteesta. Tämä on yhdenmukaista sen kanssa, että malli paljastaa jaetun "harvinainen luurankoston häiriö + analgeettinen yhteisesiintyvyys" -signaalin pikemminkin kuin todellisen uudelleenkäytön mahdollisuuden.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä liittyviä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta

## Suomen markkinatiedot

Ibuprofeiinilla ei ole voimassa olevia markkinointilupia, jotka on kirjattu tälle ehdokkaalle (0 lupaa; markkinatilanne: ei markkinoilla).

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Pääennusteen tueksi ei ole kliinisiä tutkimuksia eikä kirjallisuusviitteitä, ei vahvistettua mekanistista yhteyttä, ja taustalla olevat sääntelytiedot (alkuperäinen indikaatio, vaikutusmekanismi, TFDA-varoitukset, lääkeyhdysvaikutukset) puuttuvat kokonaan — tämä ehdokas ei täytä edes vähimmäisvaatimuksia edistyä eteenpäin.

**Jatkaakseen tarvitaan seuraava:**
- TFDA/EMA-pakkausseloste (varoitukset, vasta-aiheet, lääkeyhdysvaikutukset) turvallisuustietojen kriittisen puutteen ratkaisemiseksi
- Vahvistettu vaikutusmekanismi DrugBankista tai ensisijaisesta kirjallisuudesta
- Itsenäinen biologisen uskottavuuden arviointi GDF5/BMP-väylästä suhteessa COX-inhibitioon, ottaen huomioon mallin oman perustelun kyseenalaistavan syy-yhteyttä
- Uudelleenseulonta alemman sijoituksen saaneille mutta mekanistisesti vahvemmille ehdokkaille, koska kaikki seitsemän ennustetta tässä paketissa saavat samankaltaisen pistemäärän (L5, Odota) ilman erottavaa näyttöä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

