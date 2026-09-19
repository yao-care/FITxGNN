---
layout: default
title: Lonoctocog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 233
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# LONOCTOCOG ALFA: Tekijän VIII korvaava hoito pseudo-von Willebrandin taudista

## Yhden lauseen yhteenveto

> Lonoctocog alfa on yksketjuinen rekombinantti tekijä VIII (rFVIII) -korvaustuote, joka vaikuttaa sisäisessä hyytymiskaskaadissa (FVIIIa–FIXa -tenaasikomplekksi).
> TxGNN-malli ennustaa, että se saattaa olla tehokas **pseudo-von Willebrandin taudin** hoitoon,
> mutta tämä kandidaatti – yhdessä 3 muun verihiutale-häiriön kandidaatin kanssa – **ei ole tukevia kliinisiä tutkimuksia tai kirjallisuutta**, ja lääkkeen mekanistiset perusteet nimenomaan vastustavat biologista uskottavuutta.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei vahvistettu — hyväksyttyä lupaa tai indikaatiotekstiä ei ole saatavilla tässä näyttöpaketissa (lääkettä ei ole markkinoilla Suomessa) |
| Ennustettu uusi indikaatio | Pseudo-von Willebrandin tauti |
| TxGNN-ennustepisteet | 99.85% |
| Näyttötaso | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla suoraan (`original_moa` on tietoväli). Uudelleenkäyttöperustelut tässä näyttöpaketissa kuvaavat kuitenkin johdonmukaisesti lonoctocog alfaa yksketjuisenä rekombinantti tekijä VIII (rFVIII) -tuotteena, joka **ei sisällä** von Willebrandin tekijää (VWF), ja joka toimii FVIIIa-kofaktorina sisäisen hyytymisen tenaasikomplekkissa (FVIIIa–FIXa).

Kriittisesti, pseudo-von Willebrandin taudin mekanistinen analyysi selvästi toteaa, että häiriö juontuu **verihiutaleissa tapahtuvan GPIbα-gain-of-function-mutaatiosta** – epänormaalisti lisääntyneestä verihiutaleissa VWF:ään kohdistuvasta affiniteetista, joka kuluttaa korkean molekyylipainon VWF-multimeereja. Patologia sijaitsee verihiutale-reseptorin tasolla, ei hyytymistekijä-tasolla. FVIII-täydennys ei korjaa GPIbα–VWF-sitoutumisen poikkeavuuksia, joten lääkkeen ja tämän indikaation välillä ei ole suoraa mekanistista yhteyttä.

Sama kaava pätee kaikkiin neljään TxGNN-sijoitettuun kandidaattiin (pseudo-vWD, primäärinen verihiutaleista vapautumisen häiriö, Glanzmannin trombasctenia, Scottin oireyhtymä): jokainen on **verihiutale-toiminto- tai verihiutale-reseptori-häiriö**, kun taas lonoctocog alfa kattaa **hyytymistekijän puutoksen**. Näyttöpaketin omien perusteiden mukaan TxGNN:n korkeat pisteet heijastuvat todennäköisesti lähinnä topologiseen läheisyyteen "hemostaasin/hyytymisen" tautiryppään sisällä tietokaavassa, eikä todelliseen farmakologiseen reititykseen. Jopa Scottin oireyhtymiä koskien, jossa FVIIIa on kirjaimellisesti oleellisen entsyymikomplekksin komponentti, vika on verihiutale-kalvon fosfolipidien sekoittumisessa (ANO6), ei FVIII:n saatavuudessa — joten täydennys ei voi palauttaa puuttuvaa biologiaa.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä kliinisiä tutkimuksia liittyen tähän

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla olevaa kirjallisuutta

---

## Suomen markkinatiedot

Lonoctocog alfa ei tällä hetkellä ole hyväksytty Suomessa (0 lupaa rekistereissä); tämän näyttöpaketin tuote-/annosmuoto-/indikaatiotiedot eivät ole saatavilla.

---

## Turvallisuushuomiot

Turvallisuustiedot löytyvät pakkausselosteesta.

---

## Muut TxGNN-luokitellut kandidaatit (ei ensisijaisia)

Täydellisyyden vuoksi, kolme muuta verihiutale-häiriön kandidaattia merkittiin samankaltaisesti korkeilla TxGNN-pisteillä, mutta samalla tutkimusnäytön puutoksella ja samalla mekanistisella erolla (reseptori-/granuuli-/scramblaasivirheistä vs. hyytymistekijän korvaus):

| Sijoitus | Sairaus | TxGNN-pisteet | Näyttötaso | Päätös |
|------|---------|-------------|-----------------|----------|
| 2 | Primäärinen verihiutaleista vapautumisen häiriö | 99.84% | L5 | Pidä |
| 3 | Glanzmannin trombasctenia | 99.76% | L5 | Pidä |
| 4 | Scottin oireyhtymä | 99.44% | L5 | Pidä |

Missään näistä ei ole rekisteröityjä kliinisiä tutkimuksia tai kirjallisuustukea.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
Kaikissa neljässä ennustetussa indikaatiossa tutkimusnäyttö perustuu ainoastaan TxGNN-mallin pisteisiin (L5), eikä kliinisiä tutkimuksia tai kirjallisuusviitteitä ole löydetty 12 kohdennetussa haussa. Lääkkeen mekanistiset perusteet nimenomaan vastustavat biologista uskottavuutta jokaiselle kandidaatille, koska kohdesairaudet ovat verihiutale-toiminto- tai -reseptorivikoja eikä hyytymistekijän puutosta, johon FVIII-korvaus voisi vaikuttaa.

**Jatkaakseen seuraavaa tarvitaan:**
- Lonoctocog alfan alkuperäinen indikaatio ja säätelyn hyväksymishistoria (tällä hetkellä puuttuu)
- Vaikutusmekanismi (MOA) -tiedot DrugBankista tai valmistajan merkinnöistä
- TFDA/Fimean pakkausseloste varoitukset ja vasta-aiheet (tällä hetkellä estävä tietoväli per `DG001`)
- Riippumaton farmakologinen tai prekliininen perustelut, jotka yhdistävät FVIII-täydennyksen mihinkään neljästä verihiutale-häiriön kandidaatista ennen kuin siirrytään eteenpäin S0:sta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

