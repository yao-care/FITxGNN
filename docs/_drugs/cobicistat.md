---
layout: default
title: Cobicistat
parent: Pelkkä mallin ennuste (L5)
nav_order: 105
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: HIV:n farmakokineetisesta vahvistuksesta Simiaanien immunodefisienssi-viruksen infektioihin

## Yhden lauseen yhteenveto

Cobicistat ei ole itsessään antiviraalinen aine — se on farmakokineetinen vahvistin (CYP3A4/CYP2D6, P-gp ja OATP1B1/1B3:n inhibiittori), joka on yhteismuotoiltu antiretroviraalisissa lääkkeissä, kuten elvitegravir ja atazanavir, HIV:n hoitoa varten. TxGNN-malli ennustaa, että se saattaa olla merkityksellinen **Simiaanien immunodefisienssi-viruksen (SIV) infektiolle**, mutta tämä ennustus on tällä hetkellä tuettu **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja se perustuu kokonaan verkon upotuksen samankaltaisuuteen HIV-vastaaviin solmuihin.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Hyväksyttävää indikaatiotekstiä ei ole saatavilla — cobicistat ei ole markkinoilla Suomessa; tunnetaan maailmanlaajuisesti farmakokineettisenä vahvistimena, jota käytetään antiretroviraalisaineiden rinnalla (ei omaa suoraa antiviraalista vaikutusta) |
| Ennustettu uusi indikaatio | Simiaanien immunodefisienssi-viruksen infektio |
| TxGNN-ennustuspisteet | 99.92% |
| Näytön taso | L5 |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennustus on järkevä?

Yksityiskohtaiset vaikutusmekanismin tiedot on merkitty tietoaukoksi näyttöpaketissa. Saatavilla olevan farmakologisen tiedon perusteella cobicistat on ritonavirin rakenneanalogi ja toimii CYP3A4/CYP2D6:n ja P-gp- ja OATP1B1/1B3-kuljettajien tehokkaana inhibiittorina. Sen kliininen rooli on nostaa yhdessä annamittujen antiretroviraalisaineiden plasman konsentraatioita pikemminkin kuin harjoittaa suoraa antiviraalista vaikutusta.

SIV on lenitivirus, joka infektoi ei-ihmisiä primaatteja, ja se on taksonomiallisesti sukua HIV:lle, mikä todennäköisesti selittää, miksi TxGNN:n tietoverkko sijoittaa cobicistatia lähelle SIV-infektiosolmuja — molemmat jakavat läheisyyden HIV/lenitivirus-vastaaviin entititeetteihin upotustilassa. Tämä on kuitenkin topologinen samankaltaisuus, ei osoitettu farmakologinen: cobicistatilla ei ole tunnettua suoraa antiviraalista vaikutusta SIV:tä tai HIV:tä vastaan, ja SIV-infektio on eläinlääketieteen/eläinmallin sairaus pikemminkin kuin ihmisen kliininen indikaatio.

Kaksi muuta TxGNN-ehdokasta tässä paketissa vahvistavat saman varotoimenpiteet: kissien immunodefisienssi-oireyhtymä (sijoitus 2) on samoin eläinlääketieteen lentivirus-sairaus, joka on päätelty puhtaasti retrovirus-homologiasta, ja harvinainen neurokehityksellinen valkoisen aineen häiriö (sijoitus 3) ei ole uskottavaa mekanistista yhteyttä cobicistatiin tunnettuun CYP/kuljettaja-inhibitio-profiiliin. Kaikki kolme ennustusta saavat samalla tavalla korkeita pisteitä (~99.9%), vaikka niihin ei ole tukevia tutkimuksia tai kirjallisuutta — mikä on johdonmukaista verkon upotuksen artefaktin kanssa pikemminkin kuin validoitu uudelleenkäyttösignaali.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyviä kirjallisuusviitteitä.

## Suomen markkinatiedot

Cobicistat ei pidä markkinointilupaa Suomessa (markkinatilanne: ei markkinoilla; 0 rekisteröityä hyväksyntää), joten tuote- ja annostelun muotoihin liittyviä tietoja ei ole saatavilla.

## Turvallisuusnäkökohdat

Lisätietoja turvallisuustiedoista on saatavilla pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Kaikki kolme TxGNN-ennustettua indikaatiota (SIV-infektio, kissien immunodefisienssi-oireyhtymä ja harvinainen neurokehityksellinen häiriö) ovat näytön tasolla L5 — pelkkä mallin ennustus ilman tukevia kliinisiä tutkimuksia tai kirjallisuutta — ja kaksi kolmesta kohdistavat eläin-, ei ihmisen, sairauksia. Yhdessä **estävän** tietoaukon kanssa TFDA/Fimea-pakkausselosteen turvallisuustiedoissa (DG001), tämä ehdokas ei voi edetä alkuperäisen seulonnan (S0) ohi.

**Edistymiseksi seuraavat tiedot tarvitaan:**
- TFDA/Fimea-pakkausselosteen tiedot (varoitukset, vasta-aiheet) estävän aukon (DG001) poistamiseksi ennen mitään S1-turvallisuuden tarkastelua
- Vahvistettu vaikutusmekanismin tieto DrugBankista (DG002)
- Riippumaton farmakologinen tai prekliininen näyttö, joka yhdistää cobicistatiin CYP3A4/P-gp/OATP-inhibition ihmiselle relevanttiin indikaatioon, koska nykyiset parhaat ennustukset ovat ei-ihmisen tautimalleja

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

